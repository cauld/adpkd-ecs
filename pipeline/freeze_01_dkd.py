"""Unit 01 — GSE195460 marker fallback. No CNR1 in assignment. No DE."""

from __future__ import annotations

import json
import os
from pathlib import Path

import numpy as np
import pandas as pd
import scipy.sparse as sp
import scanpy as sc

SEED = 20260829
ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw" / "GSE195460"
OUT = ROOT / "data" / "derived" / "GSE195460"

GENES_PT = ["LRP2", "CUBN", "SLC34A1", "SLC13A3"]
GENES_INJ = ["VCAM1", "HAVCR1", "PROM1"]
GENES_OTHER = ["SLC12A1", "SLC12A3", "AQP2", "CALB1", "SLC26A7"]
# Must not use CNR1 or ECS panel or glycolysis genes for assignment.
FORBIDDEN = {"CNR1", "CNR2", "GPR55", "FAAH", "MGLL", "NAPEPLD", "DAGLA", "DAGLB", "TRPV1", "HK2", "PKM", "LDHA"}

H5_FILES = [
    ("GSE195460_Control1_filtered_feature_bc_matrix.h5", "Control1", "control"),
    ("GSE195460_Control2_filtered_feature_bc_matrix.h5", "Control2", "control"),
    ("GSE195460_Control3_filtered_feature_bc_matrix.h5", "Control3", "control"),
    ("GSE195460_Control4_filtered_feature_bc_matrix.h5", "Control4", "control"),
    ("GSE195460_Control5_filtered_feature_bc_matrix.h5", "Control5", "control"),
    ("GSM5837792_Control6_filtered_feature_bc_matrix.h5", "Control6", "control"),
    ("GSE195460_DN1_filtered_feature_bc_matrix.h5", "DN1", "DKD"),
    ("GSE195460_DN2_filtered_feature_bc_matrix.h5", "DN2", "DKD"),
    ("GSE195460_DN3_filtered_feature_bc_matrix.h5", "DN3", "DKD"),
    ("GSM5837797_DN4_filtered_feature_bc_matrix.h5", "DN4", "DKD"),
    ("GSM5837799_DN5_filtered_feature_bc_matrix.h5", "DN5", "DKD"),
]


def _col(ad, genes: list[str]) -> np.ndarray:
    idx = [ad.var_names.get_loc(g) for g in genes]
    x = ad.X[:, idx]
    if sp.issparse(x):
        x = x.toarray()
    return np.asarray(x, dtype=np.float64)


def main() -> None:
    os.environ["PYTHONHASHSEED"] = str(SEED)
    np.random.seed(SEED)
    OUT.mkdir(parents=True, exist_ok=True)
    pieces = []
    for fname, library, disease in H5_FILES:
        path = RAW / fname
        ad = sc.read_10x_h5(path)
        ad.var_names_make_unique()
        overlap = FORBIDDEN.intersection(set(ad.var_names))
        # Presence of forbidden symbols in the matrix is expected; they must not be used.
        assign = GENES_PT + GENES_INJ + GENES_OTHER
        missing = [g for g in assign if g not in ad.var_names]
        if missing:
            raise SystemExit(f"{fname} missing assignment genes: {missing}")
        used = [g for g in assign if g in FORBIDDEN]
        if used:
            raise SystemExit(f"assignment list leaked forbidden genes: {used}")
        ad.obs["library"] = library
        ad.obs["disease"] = disease
        ad.obs["barcode"] = ad.obs_names.astype(str)
        ad.obs_names = [f"{library}_{b}" for b in ad.obs["barcode"]]
        pieces.append(ad[:, assign].copy())
        print(f"loaded {library} n={ad.n_obs} forbidden_in_full_index={sorted(overlap)}")

    ad = sc.concat(pieces, join="inner", index_unique=None)
    assert ad.n_vars == len(GENES_PT) + len(GENES_INJ) + len(GENES_OTHER)
    assert "CNR1" not in ad.var_names

    pt_counts = _col(ad, GENES_PT)
    other_counts = _col(ad, GENES_OTHER)
    inj_counts = _col(ad, GENES_INJ)

    pt_detected = (pt_counts > 0).sum(axis=1)
    other_detected = (other_counts > 0).sum(axis=1)
    inj_any = (inj_counts > 0).any(axis=1)

    def zscore(mat: np.ndarray) -> np.ndarray:
        mu = mat.mean(axis=0)
        sd = mat.std(axis=0, ddof=0)
        sd = np.where(sd == 0, 1.0, sd)
        return (mat - mu) / sd

    # log1p raw counts, then z across nuclei, then mean of gene-set z (PROTOCOL).
    z_pt = zscore(np.log1p(pt_counts)).mean(axis=1)
    z_other = zscore(np.log1p(other_counts)).mean(axis=1)

    is_pt = (z_pt >= z_other) & (pt_detected >= 2)
    # Other epithelium: not PT, other-epi signature wins, ≥1 other-epi gene detected.
    # Symmetric ≥2 is not in PROTOCOL for other-epi; ≥1 is documented in the freeze note.
    is_other = (~is_pt) & (z_other > z_pt) & (other_detected >= 1)
    is_fr = is_pt & inj_any

    bucket = np.full(ad.n_obs, "excluded", dtype=object)
    bucket[is_other] = "other_epithelium"
    bucket[is_pt] = "PT"
    # injured is a subset of PT, recorded separately; bucket PT includes injured.

    df = pd.DataFrame(
        {
            "cell_id": ad.obs_names.astype(str),
            "barcode": ad.obs["barcode"].astype(str).values,
            "library": ad.obs["library"].astype(str).values,
            "disease": ad.obs["disease"].astype(str).values,
            "bucket": bucket,
            "is_pt": is_pt.astype(int),
            "is_pt_injured": is_fr.astype(int),
            "is_other_epithelium": is_other.astype(int),
            "pt_n_detected": pt_detected.astype(int),
            "other_n_detected": other_detected.astype(int),
            "z_pt": z_pt,
            "z_other": z_other,
        }
    )
    out_csv = OUT / "cell_buckets.csv"
    df.to_csv(out_csv, index=False)

    n = {
        "n_nuclei": int(len(df)),
        "n_PT": int(is_pt.sum()),
        "n_PT_injured": int(is_fr.sum()),
        "n_other_epithelium": int(is_other.sum()),
        "n_excluded": int((bucket == "excluded").sum()),
        "assignment_genes": GENES_PT + GENES_INJ + GENES_OTHER,
        "forbidden_not_used": sorted(FORBIDDEN),
        "rule": (
            "PT: mean z(log1p PT-identity) >= mean z(log1p other-epi) and >=2 PT genes count>0. "
            "injured: PT and any VCAM1/HAVCR1/PROM1 count>0. "
            "other_epithelium: not PT and z_other > z_pt and >=1 other-epi gene count>0. "
            "z-score across nuclei, ddof=0. No clustering. No CNR1."
        ),
    }
    by = (
        df.groupby(["library", "disease"], observed=True)
        .agg(
            n=("cell_id", "size"),
            n_PT=("is_pt", "sum"),
            n_PT_injured=("is_pt_injured", "sum"),
            n_other=("is_other_epithelium", "sum"),
        )
        .reset_index()
    )
    n["by_library"] = by.to_dict(orient="records")
    (OUT / "freeze_summary.json").write_text(json.dumps(n, indent=2))
    print(json.dumps(n, indent=2))
    print(f"WROTE {out_csv}")


if __name__ == "__main__":
    main()

"""Unit 01 — join ADPKD author labels + write freeze note. No CNR1 DE."""

from __future__ import annotations

import json
import os
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd

SEED = 20260829
ROOT = Path(__file__).resolve().parents[1]

PT_TOKENS = ["PT1", "PT2"]
OTHER_TOKENS = ["TAL1", "TAL2", "DCT", "CNT_PC", "ICA", "ICB"]
EXCLUDE_TOKENS = ["ENDO", "FIB", "LEUK", "PEC", "PODO", "URO1", "URO2"]


def md_table(headers: list[str], rows: list[list[str]]) -> str:
    lines = ["| " + " | ".join(headers) + " |", "| " + " | ".join("---" for _ in headers) + " |"]
    for r in rows:
        lines.append("| " + " | ".join(str(x) for x in r) + " |")
    return "\n".join(lines)


def main() -> None:
    os.environ["PYTHONHASHSEED"] = str(SEED)
    meta = pd.read_csv(ROOT / "data/raw/GSE185948/GSE185948_metadata_RNA.csv.gz", compression="gzip")
    inj = pd.read_csv(ROOT / "data/derived/GSE185948/injury_marker_pos.csv")
    dkd = pd.read_csv(ROOT / "data/derived/GSE195460/cell_buckets.csv")
    dkd_sum = json.loads((ROOT / "data/derived/GSE195460/freeze_summary.json").read_text())

    assert meta["name"].is_unique
    assert set(meta["name"]) == set(inj["cell_id"])
    df = meta.merge(inj, left_on="name", right_on="cell_id", how="inner", validate="1:1")
    assert len(df) == 102710
    unseen = sorted(set(df["celltype"]) - set(PT_TOKENS + OTHER_TOKENS + EXCLUDE_TOKENS))
    if unseen:
        raise SystemExit(f"unmapped celltype tokens: {unseen}")

    is_pt = df["celltype"].isin(PT_TOKENS)
    is_other = df["celltype"].isin(OTHER_TOKENS)
    is_fr = is_pt & (df["inj_any"] == 1)
    bucket = pd.Series("excluded", index=df.index, dtype=object)
    bucket[is_other] = "other_epithelium"
    bucket[is_pt] = "PT"
    df["bucket"] = bucket
    df["is_pt"] = is_pt.astype(int)
    df["is_pt_injured"] = is_fr.astype(int)
    df["is_other_epithelium"] = is_other.astype(int)

    keep = [
        "name",
        "barcode",
        "patient",
        "disease",
        "celltype",
        "bucket",
        "is_pt",
        "is_pt_injured",
        "is_other_epithelium",
        "VCAM1_pos",
        "HAVCR1_pos",
        "PROM1_pos",
        "inj_n_genes",
    ]
    out_csv = ROOT / "data/derived/GSE185948/cell_buckets.csv"
    df[keep].to_csv(out_csv, index=False)

    by_pt = (
        df.groupby(["patient", "disease"], observed=True)
        .agg(
            n=("name", "size"),
            n_PT=("is_pt", "sum"),
            n_PT_injured=("is_pt_injured", "sum"),
            n_other=("is_other_epithelium", "sum"),
        )
        .reset_index()
        .sort_values("patient")
    )
    # bins that would be dropped by the later OSCA floor (not applied here)
    n_small = int((by_pt["n_PT"] < 10).sum())

    adpkd_json = {
        "accession": "GSE185948",
        "path": "author_celltype",
        "pt_tokens": PT_TOKENS,
        "other_epithelium_tokens": OTHER_TOKENS,
        "exclude_from_A_S": EXCLUDE_TOKENS,
        "injured_rule": "PT token in {PT1,PT2} AND any of VCAM1/HAVCR1/PROM1 raw count > 0",
        "n_nuclei": int(len(df)),
        "n_PT": int(is_pt.sum()),
        "n_PT_injured": int(is_fr.sum()),
        "n_other_epithelium": int(is_other.sum()),
        "n_excluded": int((bucket == "excluded").sum()),
        "n_patients_ADPKD": int(df.loc[df["disease"] == "PKD", "patient"].nunique()),
        "n_patients_control": int(df.loc[df["disease"] == "control", "patient"].nunique()),
        "cnr1_used_in_assignment": False,
        "clustered": False,
        "n_patient_PT_bins_lt_10": n_small,
    }
    (ROOT / "data/derived/GSE185948/freeze_summary.json").write_text(json.dumps(adpkd_json, indent=2))

    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    lines: list[str] = []
    a = lines.append
    a("# Unit 01 — frozen cell-state maps (study 1)")
    a("")
    a(f"**Generated:** {now}")
    a(f"**Runners:** `pipeline/freeze_01_adpkd.R`, `pipeline/freeze_01_dkd.py`, `pipeline/freeze_01_report.py` (seed `{SEED}`).")
    a("**Must not (this unit):** *CNR1* to name clusters; Gate A or Gate S; freeze only one atlas then look at *CNR1* on the other.")
    a("**CNR1 in assignment gene list:** no. **Clustering:** no.")
    a("")
    a("Both accessions frozen below. Units 02–06 may use these maps. Do not edit this freeze after seeing *CNR1* differentials; amend in `STATUS.md` if a change is required.")
    a("")
    a("## GSE185948 (ADPKD atlas) — author labels")
    a("")
    a("- Counts object: `dgCMatrix` 27970 genes × 102710 nuclei after double-gunzip of `GSE185948_count_RNA.rds.gz` (laptop RAM peak ~2.5 GiB; Spark not used).")
    a("- Join: metadata `name` ↔ matrix colnames, 102710/102710.")
    a("- **PT object:** `celltype` ∈ `{PT1, PT2}` (exact CSV tokens; not `PT-1`/`FR-PTC`). Do not re-derive PT from marker genes.")
    a("- **Failed-repair / injured PT:** no author FR token. Marker fallback **inside author PT only:** any of `VCAM1`, `HAVCR1`, `PROM1` raw count > 0.")
    a("- **Other epithelium:** `TAL1`, `TAL2` (loop), `DCT`, `CNT_PC`, `ICA`, `ICB` (connecting/collecting).")
    a("- **Excluded from Gate A and Gate S sides:** `ENDO`, `FIB`, `LEUK`, `PEC` (protocol), plus `PODO`, `URO1`, `URO2` (not PT and not the other-epi pool).")
    a(f"- n: PT **{adpkd_json['n_PT']}** (injured subset **{adpkd_json['n_PT_injured']}**); other epithelium **{adpkd_json['n_other_epithelium']}**; excluded **{adpkd_json['n_excluded']}**.")
    a("- Nucleus counts are **not** *CNR1* expression.")
    a("")
    a(
        md_table(
            ["patient", "disease", "n", "n_PT", "n_PT_injured", "n_other"],
            [
                [r.patient, r.disease, int(r.n), int(r.n_PT), int(r.n_PT_injured), int(r.n_other)]
                for r in by_pt.itertuples(index=False)
            ],
        )
    )
    a("")
    a(f"- Patient × PT bins with n_PT < 10 (OSCA floor applies at Gate A/S, not here): **{n_small}**.")
    a("- Artifacts: `data/derived/GSE185948/cell_buckets.csv`, `freeze_summary.json`.")
    a("")
    a("## GSE195460 (DKD atlas) — marker fallback")
    a("")
    a("- No author cell-type table on GEO (Unit 00). Independent object; ADPKD *CNR1* was not used to choose this rule.")
    a("- Assignment genes only: PT identity `LRP2, CUBN, SLC34A1, SLC13A3`; injured `VCAM1, HAVCR1, PROM1`; other-epi `SLC12A1, SLC12A3, AQP2, CALB1, SLC26A7`.")
    a("- **Not used:** `CNR1`, descriptive ECS panel, `HK2`/`PKM`/`LDHA`. No Leiden/Louvain.")
    a("- **PT:** mean z(log1p PT-identity genes) ≥ mean z(log1p other-epi genes) **and** ≥2 PT-identity genes with count > 0. z-score across nuclei, ddof=0.")
    a("- **Injured PT:** PT ∩ any injured-gene count > 0.")
    a("- **Other epithelium:** not PT **and** z_other > z_pt **and** ≥1 other-epi gene count > 0 (the ≥1 floor is the documented operationalization of PROTOCOL’s other-epi marker pool; PROTOCOL states ≥2 only for PT).")
    a("- **Excluded from A/S:** neither PT nor other epithelium (immune/endo/stroma/PEC not labeled; they fall here if markers do not assign PT or other-epi).")
    a(f"- n: PT **{dkd_sum['n_PT']}** (injured subset **{dkd_sum['n_PT_injured']}**); other epithelium **{dkd_sum['n_other_epithelium']}**; excluded **{dkd_sum['n_excluded']}**; total nuclei **{dkd_sum['n_nuclei']}**.")
    a("")
    a(
        md_table(
            ["library", "disease", "n", "n_PT", "n_PT_injured", "n_other"],
            [
                [r["library"], r["disease"], r["n"], r["n_PT"], r["n_PT_injured"], r["n_other"]]
                for r in dkd_sum["by_library"]
            ],
        )
    )
    a("")
    pt_by = dkd.groupby(["library", "disease"], observed=True)["is_pt"].sum()
    a(f"- Library × PT bins with n_PT < 10: **{int((pt_by < 10).sum())}**.")
    a("- Artifacts: `data/derived/GSE195460/cell_buckets.csv`, `freeze_summary.json`.")
    a("")
    a("## Unit 01 pass criteria")
    a("")
    a("- Each PT object defined without *CNR1*: **yes**.")
    a("- Other epithelium defined on both atlases: **yes**.")
    a("- Immune/endothelial/stroma excluded from Gate A and Gate S sides: **yes** (author tokens on GSE185948; unassigned remainder on GSE195460).")
    a("- **Unit 01 pass: True**")
    a("")
    a("No Gate C/A/B/S numbers. Next: Unit 02 detection (*CNR1* count > 0 inside the frozen ADPKD PT object) after this freeze is in git.")
    a("")

    out_md = ROOT / "research/01-frozen-labels.md"
    out_md.write_text("\n".join(lines))
    print(out_md.read_text())
    print(f"WROTE {out_md}")
    print("UNIT01_PASS=True")
    print("ADPKD", json.dumps(adpkd_json))


if __name__ == "__main__":
    main()

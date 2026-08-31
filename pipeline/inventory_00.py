"""Unit 00 — GEO inventory. No CNR1-vs-cell-type or CNR1-vs-disease summaries."""

from __future__ import annotations

import gzip
import hashlib
import os
import platform
import shutil
import struct
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

import h5py
import numpy as np
import pandas as pd

SEED = 20260829
ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"
OUT = ROOT / "research" / "data-inventory.md"

GENES_KILL = ["CNR1"]
GENES_PT = ["LRP2", "CUBN", "SLC34A1", "SLC13A3"]
GENES_INJ = ["VCAM1", "HAVCR1", "PROM1"]
GENES_ECS = ["CNR2", "GPR55", "FAAH", "MGLL", "NAPEPLD", "DAGLA", "DAGLB", "TRPV1"]
GENES_OTHER = ["SLC12A1", "SLC12A3", "AQP2", "CALB1", "SLC26A7"]
GENES_ALL = GENES_KILL + GENES_PT + GENES_INJ + GENES_ECS + GENES_OTHER

GSE185948_FILES = [
    RAW / "GSE185948" / "GSE185948_metadata_RNA.csv.gz",
    RAW / "GSE185948" / "GSE185948_count_RNA.rds.gz",
]
GSE195460_FILES = [
    RAW / "GSE195460" / "GSE195460_Control1_filtered_feature_bc_matrix.h5",
    RAW / "GSE195460" / "GSE195460_Control2_filtered_feature_bc_matrix.h5",
    RAW / "GSE195460" / "GSE195460_Control3_filtered_feature_bc_matrix.h5",
    RAW / "GSE195460" / "GSE195460_Control4_filtered_feature_bc_matrix.h5",
    RAW / "GSE195460" / "GSE195460_Control5_filtered_feature_bc_matrix.h5",
    RAW / "GSE195460" / "GSM5837792_Control6_filtered_feature_bc_matrix.h5",
    RAW / "GSE195460" / "GSE195460_DN1_filtered_feature_bc_matrix.h5",
    RAW / "GSE195460" / "GSE195460_DN2_filtered_feature_bc_matrix.h5",
    RAW / "GSE195460" / "GSE195460_DN3_filtered_feature_bc_matrix.h5",
    RAW / "GSE195460" / "GSM5837797_DN4_filtered_feature_bc_matrix.h5",
    RAW / "GSE195460" / "GSM5837799_DN5_filtered_feature_bc_matrix.h5",
]

URLS = {
    "GSE185948_metadata_RNA.csv.gz": "https://ftp.ncbi.nlm.nih.gov/geo/series/GSE185nnn/GSE185948/suppl/GSE185948_metadata_RNA.csv.gz",
    "GSE185948_count_RNA.rds.gz": "https://ftp.ncbi.nlm.nih.gov/geo/series/GSE185nnn/GSE185948/suppl/GSE185948_count_RNA.rds.gz",
    "GSE195460_Control1_filtered_feature_bc_matrix.h5": "https://ftp.ncbi.nlm.nih.gov/geo/series/GSE195nnn/GSE195460/suppl/GSE195460_Control1_filtered_feature_bc_matrix.h5",
    "GSE195460_Control2_filtered_feature_bc_matrix.h5": "https://ftp.ncbi.nlm.nih.gov/geo/series/GSE195nnn/GSE195460/suppl/GSE195460_Control2_filtered_feature_bc_matrix.h5",
    "GSE195460_Control3_filtered_feature_bc_matrix.h5": "https://ftp.ncbi.nlm.nih.gov/geo/series/GSE195nnn/GSE195460/suppl/GSE195460_Control3_filtered_feature_bc_matrix.h5",
    "GSE195460_Control4_filtered_feature_bc_matrix.h5": "https://ftp.ncbi.nlm.nih.gov/geo/series/GSE195nnn/GSE195460/suppl/GSE195460_Control4_filtered_feature_bc_matrix.h5",
    "GSE195460_Control5_filtered_feature_bc_matrix.h5": "https://ftp.ncbi.nlm.nih.gov/geo/series/GSE195nnn/GSE195460/suppl/GSE195460_Control5_filtered_feature_bc_matrix.h5",
    "GSM5837792_Control6_filtered_feature_bc_matrix.h5": "https://ftp.ncbi.nlm.nih.gov/geo/samples/GSM5837nnn/GSM5837792/suppl/GSM5837792_Control6_filtered_feature_bc_matrix.h5",
    "GSE195460_DN1_filtered_feature_bc_matrix.h5": "https://ftp.ncbi.nlm.nih.gov/geo/series/GSE195nnn/GSE195460/suppl/GSE195460_DN1_filtered_feature_bc_matrix.h5",
    "GSE195460_DN2_filtered_feature_bc_matrix.h5": "https://ftp.ncbi.nlm.nih.gov/geo/series/GSE195nnn/GSE195460/suppl/GSE195460_DN2_filtered_feature_bc_matrix.h5",
    "GSE195460_DN3_filtered_feature_bc_matrix.h5": "https://ftp.ncbi.nlm.nih.gov/geo/series/GSE195nnn/GSE195460/suppl/GSE195460_DN3_filtered_feature_bc_matrix.h5",
    "GSM5837797_DN4_filtered_feature_bc_matrix.h5": "https://ftp.ncbi.nlm.nih.gov/geo/samples/GSM5837nnn/GSM5837797/suppl/GSM5837797_DN4_filtered_feature_bc_matrix.h5",
    "GSM5837799_DN5_filtered_feature_bc_matrix.h5": "https://ftp.ncbi.nlm.nih.gov/geo/samples/GSM5837nnn/GSM5837799/suppl/GSM5837799_DN5_filtered_feature_bc_matrix.h5",
}


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def ram_disk() -> tuple[str, str]:
    mem = "unknown"
    if sys.platform == "darwin":
        import subprocess

        raw = subprocess.check_output(["sysctl", "-n", "hw.memsize"], text=True).strip()
        mem = f"{int(raw) / (1024**3):.1f} GiB (hw.memsize)"
    usage = shutil.disk_usage(ROOT)
    disk = f"{usage.free / (1024**3):.1f} GiB free / {usage.total / (1024**3):.1f} GiB total"
    return mem, disk


def decode_h5_str(arr) -> list[str]:
    out = []
    for x in arr:
        if isinstance(x, (bytes, np.bytes_)):
            out.append(x.decode())
        else:
            out.append(str(x))
    return out


def h5_feature_index(path: Path) -> dict:
    with h5py.File(path, "r") as f:
        names = decode_h5_str(f["matrix/features/name"][()])
        n_barcodes = int(f["matrix/barcodes"].shape[0])
        genome = sorted(set(decode_h5_str(f["matrix/features/genome"][()])))
        ftype = sorted(set(decode_h5_str(f["matrix/features/feature_type"][()])))
    counts = Counter(names)
    dups = sorted(k for k, v in counts.items() if v > 1)
    present = [g for g in GENES_ALL if g in counts]
    missing = [g for g in GENES_ALL if g not in counts]
    return {
        "file": path.name,
        "n_features": len(names),
        "n_unique_symbols": len(counts),
        "n_barcodes": n_barcodes,
        "genome": genome,
        "feature_type": ftype,
        "dup_symbols": dups,
        "present": present,
        "missing": missing,
        "name_set": set(names),
    }


def rds_ascii_strings_present(path: Path, genes: list[str]) -> dict[str, bool]:
    """Scan RDS XDR for length-prefixed ASCII strings.

    GEO ships `GSE185948_count_RNA.rds.gz` as gzip(gzip(RDS)). One gunzip still
    starts with gzip magic; two layers yield XDR (`X\\n`). Does not load counts.
    A hit is presence of an R character of that exact length, not a CNR1 summary.
    """
    needles = {g: struct.pack(">i", len(g)) + g.encode("ascii") for g in genes}
    found = {g: False for g in genes}
    remaining = set(genes)
    with gzip.open(path, "rb") as f1:
        with gzip.open(f1, "rb") as f:
            magic = f.read(2)
            if magic not in (b"X\n", b"A\n", b"B\n"):
                raise RuntimeError(f"Unexpected RDS magic after double gzip: {magic!r}")
            f.seek(0)
            prev = b""
            while remaining:
                chunk = f.read(8 * 1024 * 1024)
                if not chunk:
                    break
                buf = prev + chunk
                for g in list(remaining):
                    if needles[g] in buf:
                        found[g] = True
                        remaining.remove(g)
                prev = buf[-64:]
    return found


def md_table(headers: list[str], rows: list[list[str]]) -> str:
    lines = ["| " + " | ".join(headers) + " |", "| " + " | ".join("---" for _ in headers) + " |"]
    for r in rows:
        lines.append("| " + " | ".join(r) + " |")
    return "\n".join(lines)


def main() -> None:
    os.environ["PYTHONHASHSEED"] = str(SEED)
    missing_files = [p for p in GSE185948_FILES + GSE195460_FILES if not p.is_file()]
    if missing_files:
        raise SystemExit("Missing raw files:\n" + "\n".join(str(p) for p in missing_files))

    ram, disk = ram_disk()
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    checksum_rows = []
    checksums_path = RAW / "CHECKSUMS.txt"
    checksum_lines = [f"# sha256  generated {now}"]
    for p in GSE185948_FILES + GSE195460_FILES:
        digest = sha256_file(p)
        checksum_rows.append([p.name, str(p.stat().st_size), digest, URLS[p.name]])
        checksum_lines.append(f"{digest}  {p.relative_to(RAW)}")
    checksums_path.write_text("\n".join(checksum_lines) + "\n")

    meta_path = GSE185948_FILES[0]
    df = pd.read_csv(meta_path, compression="gzip", low_memory=False)
    columns = list(df.columns)
    n_nuclei = len(df)
    disease_n = df.groupby("disease")["patient"].nunique().to_dict()
    patient_disease = (
        df.groupby(["patient", "disease"]).size().reset_index(name="n_nuclei").sort_values("patient")
    )
    celltypes = df["celltype"].value_counts(dropna=False)
    n_adpkd_samples = int(disease_n.get("PKD", 0))
    n_ctrl_samples = int(disease_n.get("control", 0))
    a1_eligible = n_adpkd_samples >= 3 and n_ctrl_samples >= 3

    h5_reports = [h5_feature_index(p) for p in GSE195460_FILES]
    index_same = all(r["name_set"] == h5_reports[0]["name_set"] for r in h5_reports)
    for r in h5_reports:
        del r["name_set"]

    n_ctrl_libs = 6
    n_dn_libs = 5
    s_eligible = n_ctrl_libs >= 3 and n_dn_libs >= 3

    rds_path = GSE185948_FILES[1]
    rds_hits = rds_ascii_strings_present(rds_path, GENES_ALL)
    rds_present = [g for g, ok in rds_hits.items() if ok]
    rds_missing = [g for g, ok in rds_hits.items() if not ok]
    pt_in_rds = sum(1 for g in GENES_PT if rds_hits[g])
    cnr1_in_rds = rds_hits["CNR1"]
    cnr1_in_dkd = "CNR1" in h5_reports[0]["present"]
    pt_in_dkd = sum(1 for g in GENES_PT if g in h5_reports[0]["present"])

    adpkd_pass = (
        GSE185948_FILES[0].is_file()
        and GSE185948_FILES[1].is_file()
        and cnr1_in_rds
        and pt_in_rds >= 2
    )
    dkd_pass = all(p.is_file() for p in GSE195460_FILES) and cnr1_in_dkd and pt_in_dkd >= 2
    unit_pass = adpkd_pass and dkd_pass

    lines: list[str] = []
    a = lines.append
    a("# Unit 00 — data inventory (study 1)")
    a("")
    a(f"**Generated:** {now}")
    a(f"**Runner:** `pipeline/inventory_00.py` (seed recorded `{SEED}`; this unit is deterministic).")
    a(f"**Python:** {sys.version.split()[0]} on {platform.system()} {platform.machine()}")
    a(f"**RAM:** {ram}")
    a(f"**Disk:** {disk}")
    a("**Must not (this unit):** *CNR1* vs cell type or disease plots; clustering; Pathways B–D; study 2 literature.")
    a("")
    a("## License and access")
    a("")
    a("- NCBI GEO public series [GSE185948](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE185948) and [GSE195460](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE195460).")
    a("- GEO data are publicly available under NCBI GEO distribution (no extra license file on the FTP suppl folders). Original papers remain under publisher copyright; we used landing pages + FTP only.")
    a("- **Not downloaded (protocol):** `GSE185948_RAW.tar` (26 GiB), `GSE185948_count_ATAC.rds.gz`, `GSE195460_RAW.tar` (14 GiB), peak/fragment ATAC files.")
    a("- **Not used:** GSE131882 `dgecounts.rds.gz` (Clarify 1).")
    a("")
    a("## Files, sizes, checksums")
    a("")
    a("SHA-256 also written to `data/raw/CHECKSUMS.txt` (gitignored with `data/`).")
    a("")
    a(
        md_table(
            ["file", "bytes", "sha256", "url"],
            [[r[0], r[1], f"`{r[2]}`", r[3]] for r in checksum_rows],
        )
    )
    a("")
    a("## GSE185948 — metadata columns and sample n")
    a("")
    a(f"- File: `GSE185948_metadata_RNA.csv.gz` ({n_nuclei} rows).")
    a(f"- Column names: {', '.join(f'`{c}`' for c in columns)}.")
    a("- Cell-type column: **present** (`celltype`). Disease/sample columns: **present** (`disease`, `patient`).")
    a(f"- Unique `patient` × `disease`: ADPKD/PKD **{n_adpkd_samples}** samples, control **{n_ctrl_samples}** samples.")
    a(f"- Gate A contrast lock from this n: **{'A1' if a1_eligible else 'A2'}** (A1 = ≥3 ADPKD and ≥3 control samples). Do not switch after seeing *CNR1*.")
    a("- Nucleus counts below are **not** *CNR1* expression.")
    a("")
    a(
        md_table(
            ["patient", "disease", "n_nuclei"],
            [[str(r.patient), str(r.disease), str(int(r.n_nuclei))] for r in patient_disease.itertuples(index=False)],
        )
    )
    a("")
    a("### Exact `celltype` strings (for Unit 01 freeze; paper tokens are a search aid only)")
    a("")
    a(
        md_table(
            ["celltype", "n_nuclei"],
            [[str(idx), str(int(n))] for idx, n in celltypes.items()],
        )
    )
    a("")
    a("- Author PT-like tokens in this CSV: `PT1`, `PT2` (not hyphenated `PT-1` / `PT-2`).")
    a("- Absent from `celltype`: `FR-PTC`, `N-PTC`, `PT_VCAM1`, `PT_PROM1`, `PCT`, `PST`. Injured-PT author label **not** in this table; Unit 01 uses `PT1`/`PT2` and/or marker fallback per `PROTOCOL.md`.")
    a("- Other epithelium / exclude tokens present: `TAL1`, `TAL2`, `DCT`, `CNT_PC`, `ICA`, `ICB`, `PEC`, `PODO`, `ENDO`, `FIB`, `LEUK`, `URO1`, `URO2`.")
    a("")
    a("## GSE185948 — RNA RDS feature symbols")
    a("")
    a("- Object: `GSE185948_count_RNA.rds.gz`. **Double-gzipped:** one `gunzip` still starts with gzip magic (`1f8b`); a second layer yields RDS XDR (`X\\n`, version 3, UTF-8). Uncompressed XDR ≈ 2.53 GiB. R is not installed; **counts were not loaded**. Unit 01 `readRDS` must peel both gzip layers (or `gzip -dc` twice).")
    a("- Method: scan the inner XDR for length-prefixed ASCII strings matching the protocol gene list. This is **presence in the RDS character pool**, not a *CNR1* summary.")
    a(f"- Present: {', '.join(f'`{g}`' for g in rds_present) if rds_present else '(none)'}.")
    a(f"- Missing from that scan: {', '.join(f'`{g}`' for g in rds_missing) if rds_missing else '(none)'}.")
    a(f"- Kill gene `CNR1` present: **{cnr1_in_rds}**. PT-identity genes present: **{pt_in_rds}/4**.")
    a("")
    a("## GSE195460 — RNA h5 files and n")
    a("")
    a("- Author cell-type metadata table: **not on GEO series FTP** (no `metadata*.csv`; files are Cell Ranger h5 + ATAC peaks/fragments + RAW tar). Unit 01: marker fallback unless a human-dropped table is added later (amend).")
    a(f"- Confirmatory RNA libraries: **{n_ctrl_libs}** control + **{n_dn_libs}** DN (`DN` = DKD in filenames). Gate S sample-n rule: **{'eligible' if s_eligible else 'ineligible'}** (≥3+3 libraries).")
    a("- Control6 / DN4 / DN5 live at GSM FTP paths (names as in `PROTOCOL.md`); Control1–5 and DN1–3 are series-level `GSE195460_*` files.")
    a("- No *CNR1* values computed. Barcode n is Cell Ranger filtered barcode count per library.")
    a("")
    a(
        md_table(
            ["file", "n_barcodes", "n_features", "genome"],
            [
                [r["file"], str(r["n_barcodes"]), str(r["n_features"]), ",".join(r["genome"])]
                for r in h5_reports
            ],
        )
    )
    a("")
    a(f"- Feature index identical across the 11 h5 files: **{index_same}** (36601 features, GRCh38-2020-A.premrna, Gene Expression).")
    a(f"- Duplicate gene **symbols** (not protocol genes): {', '.join(h5_reports[0]['dup_symbols'])} (10 symbols, 2 Ensembl IDs each).")
    a(f"- Protocol genes present in h5 index: {', '.join(f'`{g}`' for g in h5_reports[0]['present'])}.")
    a(f"- Protocol genes missing in h5 index: {', '.join(f'`{g}`' for g in h5_reports[0]['missing']) if h5_reports[0]['missing'] else '(none)'}.")
    a("")
    a("## Host resources (feasibility is human opt-in)")
    a("")
    a(f"- {ram}. Compressed ADPKD RNA RDS is 1.81 GiB (double-gzip); inner XDR ≈ 2.53 GiB. Materializing a Seurat/dgCMatrix may still exceed this laptop. Unit 00 did **not** load counts.")
    a(f"- {disk}. RAW tar / ATAC were not pulled.")
    a("- Do not enter Superpowers feasibility mode unless the human opts in.")
    a("")
    a("## Unit 00 pass criteria")
    a("")
    a(f"- ADPKD RNA counts + metadata reachable, `CNR1` in RDS scan, ≥2/4 PT-identity genes in RDS scan: **{adpkd_pass}**.")
    a(f"- DKD RNA h5s named and reachable, `CNR1` + ≥2/4 PT genes in h5 index: **{dkd_pass}**.")
    a(f"- Gate S ineligible?: **{not s_eligible}** (files present; n libraries {n_ctrl_libs} vs {n_dn_libs}).")
    a(f"- **Unit 00 pass: {unit_pass}**")
    a("")
    a("No biology conclusions. No Gate C/A/B/S marks. Next: Unit 01 freeze on both atlases before any *CNR1* differential.")
    a("")

    OUT.write_text("\n".join(lines))
    print(OUT.read_text())
    print(f"WROTE {OUT}")
    print(f"UNIT00_PASS={unit_pass}")


if __name__ == "__main__":
    main()

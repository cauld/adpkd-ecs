# Unit 00 — data inventory (study 1)

**Generated:** 2026-08-30 16:35 UTC
**Runner:** `pipeline/inventory_00.py` (seed recorded `20260829`; this unit is deterministic).
**Python:** 3.12.12 on Darwin arm64
**RAM:** 24.0 GiB (hw.memsize)
**Disk:** 153.3 GiB free / 460.4 GiB total
**Must not (this unit):** *CNR1* vs cell type or disease plots; clustering; Pathways B–D; study 2 literature.

## License and access

- NCBI GEO public series [GSE185948](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE185948) and [GSE195460](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE195460).
- GEO data are publicly available under NCBI GEO distribution (no extra license file on the FTP suppl folders). Original papers remain under publisher copyright; we used landing pages + FTP only.
- **Not downloaded (protocol):** `GSE185948_RAW.tar` (26 GiB), `GSE185948_count_ATAC.rds.gz`, `GSE195460_RAW.tar` (14 GiB), peak/fragment ATAC files.
- **Not used:** GSE131882 `dgecounts.rds.gz` (Clarify 1).

## Files, sizes, checksums

SHA-256 also written to `data/raw/CHECKSUMS.txt` (gitignored with `data/`).

| file | bytes | sha256 | url |
| --- | --- | --- | --- |
| GSE185948_metadata_RNA.csv.gz | 3406974 | `73f21c765e263b6110dc417e02cb54ef1dd115429cbc2ae50110b8974990acae` | https://ftp.ncbi.nlm.nih.gov/geo/series/GSE185nnn/GSE185948/suppl/GSE185948_metadata_RNA.csv.gz |
| GSE185948_count_RNA.rds.gz | 1895074813 | `2f376fa67e445cd3fde520816e0dc1ff94b920de42f81e7d43624ddb22235dbd` | https://ftp.ncbi.nlm.nih.gov/geo/series/GSE185nnn/GSE185948/suppl/GSE185948_count_RNA.rds.gz |
| GSE195460_Control1_filtered_feature_bc_matrix.h5 | 25123192 | `34cd7afa392c2f37af43dcd7632733a8cf770dbd9f7775f022fe5f206d67268f` | https://ftp.ncbi.nlm.nih.gov/geo/series/GSE195nnn/GSE195460/suppl/GSE195460_Control1_filtered_feature_bc_matrix.h5 |
| GSE195460_Control2_filtered_feature_bc_matrix.h5 | 7845772 | `8d3eaad682e350097da584e39526a67bf7e198dadca4e7708185ffb6a58c2904` | https://ftp.ncbi.nlm.nih.gov/geo/series/GSE195nnn/GSE195460/suppl/GSE195460_Control2_filtered_feature_bc_matrix.h5 |
| GSE195460_Control3_filtered_feature_bc_matrix.h5 | 17432614 | `97d1d35a2e6bda599e19f5a5788cf7be03810106f7687cb191c9ef5504ffe042` | https://ftp.ncbi.nlm.nih.gov/geo/series/GSE195nnn/GSE195460/suppl/GSE195460_Control3_filtered_feature_bc_matrix.h5 |
| GSE195460_Control4_filtered_feature_bc_matrix.h5 | 11464250 | `e4b5b08efda8c90cf0fb372f9a59877f0ada44ef4ff3794762403b3616587e82` | https://ftp.ncbi.nlm.nih.gov/geo/series/GSE195nnn/GSE195460/suppl/GSE195460_Control4_filtered_feature_bc_matrix.h5 |
| GSE195460_Control5_filtered_feature_bc_matrix.h5 | 9190876 | `4bb81950d2335934b1b25b18ca383b63f1bcffc1d2e94015d4235864ac55a791` | https://ftp.ncbi.nlm.nih.gov/geo/series/GSE195nnn/GSE195460/suppl/GSE195460_Control5_filtered_feature_bc_matrix.h5 |
| GSM5837792_Control6_filtered_feature_bc_matrix.h5 | 55455540 | `62a12b7050a429e6ce4f6c3360862b8b05ae49d6ed812702383112992d8fdefe` | https://ftp.ncbi.nlm.nih.gov/geo/samples/GSM5837nnn/GSM5837792/suppl/GSM5837792_Control6_filtered_feature_bc_matrix.h5 |
| GSE195460_DN1_filtered_feature_bc_matrix.h5 | 17301104 | `4b5f8d952f6b8a8b10f57c6ac0571dc735e04e82f82c9b8378c296cc3bca0d87` | https://ftp.ncbi.nlm.nih.gov/geo/series/GSE195nnn/GSE195460/suppl/GSE195460_DN1_filtered_feature_bc_matrix.h5 |
| GSE195460_DN2_filtered_feature_bc_matrix.h5 | 9825947 | `b71d08371d75aa3326c1c9d6865477fb0f9cb666b24136682814ac931604a5e4` | https://ftp.ncbi.nlm.nih.gov/geo/series/GSE195nnn/GSE195460/suppl/GSE195460_DN2_filtered_feature_bc_matrix.h5 |
| GSE195460_DN3_filtered_feature_bc_matrix.h5 | 10066380 | `8843e78fefb4d4860aeb759f5821aec07d3c40a2a1622165df670b9f01371495` | https://ftp.ncbi.nlm.nih.gov/geo/series/GSE195nnn/GSE195460/suppl/GSE195460_DN3_filtered_feature_bc_matrix.h5 |
| GSM5837797_DN4_filtered_feature_bc_matrix.h5 | 14639852 | `12cfa43fd23b174a4a9784b11cc233789c6b9250b90e836da14eff3fe64b8262` | https://ftp.ncbi.nlm.nih.gov/geo/samples/GSM5837nnn/GSM5837797/suppl/GSM5837797_DN4_filtered_feature_bc_matrix.h5 |
| GSM5837799_DN5_filtered_feature_bc_matrix.h5 | 13370759 | `47b6d82aad1d10eb6bba64f83bad7df8c831596ecef75dddecb25df7cfb81ced` | https://ftp.ncbi.nlm.nih.gov/geo/samples/GSM5837nnn/GSM5837799/suppl/GSM5837799_DN5_filtered_feature_bc_matrix.h5 |

## GSE185948 — metadata columns and sample n

- File: `GSE185948_metadata_RNA.csv.gz` (102710 rows).
- Column names: `name`, `barcode`, `patient`, `gender`, `disease`, `celltype`, `nCount_RNA`, `nFeature_RNA`, `UMAP_1`, `UMAP_2`.
- Cell-type column: **present** (`celltype`). Disease/sample columns: **present** (`disease`, `patient`).
- Unique `patient` × `disease`: ADPKD/PKD **8** samples, control **5** samples.
- Gate A contrast lock from this n: **A1** (A1 = ≥3 ADPKD and ≥3 control samples). Do not switch after seeing *CNR1*.
- Nucleus counts below are **not** *CNR1* expression.

| patient | disease | n_nuclei |
| --- | --- | --- |
| PKD1 | PKD | 9303 |
| PKD2 | PKD | 10912 |
| PKD3 | PKD | 9109 |
| PKD4 | PKD | 9050 |
| PKD5 | PKD | 7999 |
| PKD6 | PKD | 10699 |
| PKD7 | PKD | 2509 |
| PKD8 | PKD | 2492 |
| control1 | control | 6412 |
| control2 | control | 9553 |
| control3 | control | 6696 |
| control4 | control | 10203 |
| control5 | control | 7773 |

### Exact `celltype` strings (for Unit 01 freeze; paper tokens are a search aid only)

| celltype | n_nuclei |
| --- | --- |
| TAL1 | 24283 |
| PT1 | 19807 |
| CNT_PC | 14890 |
| DCT | 10285 |
| FIB | 8869 |
| ENDO | 5522 |
| LEUK | 4403 |
| PT2 | 3365 |
| ICA | 2996 |
| PEC | 2503 |
| PODO | 2209 |
| TAL2 | 2117 |
| ICB | 1375 |
| URO1 | 65 |
| URO2 | 21 |

- Author PT-like tokens in this CSV: `PT1`, `PT2` (not hyphenated `PT-1` / `PT-2`).
- Absent from `celltype`: `FR-PTC`, `N-PTC`, `PT_VCAM1`, `PT_PROM1`, `PCT`, `PST`. Injured-PT author label **not** in this table; Unit 01 uses `PT1`/`PT2` and/or marker fallback per `PROTOCOL.md`.
- Other epithelium / exclude tokens present: `TAL1`, `TAL2`, `DCT`, `CNT_PC`, `ICA`, `ICB`, `PEC`, `PODO`, `ENDO`, `FIB`, `LEUK`, `URO1`, `URO2`.

## GSE185948 — RNA RDS feature symbols

- Object: `GSE185948_count_RNA.rds.gz`. **Double-gzipped:** one `gunzip` still starts with gzip magic (`1f8b`); a second layer yields RDS XDR (`X\n`, version 3, UTF-8). Uncompressed XDR ≈ 2.53 GiB. R is not installed; **counts were not loaded**. Unit 01 `readRDS` must peel both gzip layers (or `gzip -dc` twice).
- Method: scan the inner XDR for length-prefixed ASCII strings matching the protocol gene list. This is **presence in the RDS character pool**, not a *CNR1* summary.
- Present: `CNR1`, `LRP2`, `CUBN`, `SLC34A1`, `SLC13A3`, `VCAM1`, `HAVCR1`, `PROM1`, `CNR2`, `GPR55`, `FAAH`, `MGLL`, `NAPEPLD`, `DAGLA`, `DAGLB`, `TRPV1`, `SLC12A1`, `SLC12A3`, `AQP2`, `CALB1`, `SLC26A7`.
- Missing from that scan: (none).
- Kill gene `CNR1` present: **True**. PT-identity genes present: **4/4**.

## GSE195460 — RNA h5 files and n

- Author cell-type metadata table: **not on GEO series FTP** (no `metadata*.csv`; files are Cell Ranger h5 + ATAC peaks/fragments + RAW tar). Unit 01: marker fallback unless a human-dropped table is added later (amend).
- Confirmatory RNA libraries: **6** control + **5** DN (`DN` = DKD in filenames). Gate S sample-n rule: **eligible** (≥3+3 libraries).
- Control6 / DN4 / DN5 live at GSM FTP paths (names as in `PROTOCOL.md`); Control1–5 and DN1–3 are series-level `GSE195460_*` files.
- No *CNR1* values computed. Barcode n is Cell Ranger filtered barcode count per library.

| file | n_barcodes | n_features | genome |
| --- | --- | --- | --- |
| GSE195460_Control1_filtered_feature_bc_matrix.h5 | 7069 | 36601 | GRCh38-2020-A.premrna |
| GSE195460_Control2_filtered_feature_bc_matrix.h5 | 4362 | 36601 | GRCh38-2020-A.premrna |
| GSE195460_Control3_filtered_feature_bc_matrix.h5 | 6763 | 36601 | GRCh38-2020-A.premrna |
| GSE195460_Control4_filtered_feature_bc_matrix.h5 | 4784 | 36601 | GRCh38-2020-A.premrna |
| GSE195460_Control5_filtered_feature_bc_matrix.h5 | 4990 | 36601 | GRCh38-2020-A.premrna |
| GSM5837792_Control6_filtered_feature_bc_matrix.h5 | 14617 | 36601 | GRCh38-2020-A.premrna |
| GSE195460_DN1_filtered_feature_bc_matrix.h5 | 5508 | 36601 | GRCh38-2020-A.premrna |
| GSE195460_DN2_filtered_feature_bc_matrix.h5 | 3933 | 36601 | GRCh38-2020-A.premrna |
| GSE195460_DN3_filtered_feature_bc_matrix.h5 | 3817 | 36601 | GRCh38-2020-A.premrna |
| GSM5837797_DN4_filtered_feature_bc_matrix.h5 | 6611 | 36601 | GRCh38-2020-A.premrna |
| GSM5837799_DN5_filtered_feature_bc_matrix.h5 | 5786 | 36601 | GRCh38-2020-A.premrna |

- Feature index identical across the 11 h5 files: **True** (36601 features, GRCh38-2020-A.premrna, Gene Expression).
- Duplicate gene **symbols** (not protocol genes): ARMCX5-GPRASP2, CYB561D2, GGT1, GOLGA8M, HSPA14, LINC01238, LINC01505, MATR3, TBCE, TMSB15B (10 symbols, 2 Ensembl IDs each).
- Protocol genes present in h5 index: `CNR1`, `LRP2`, `CUBN`, `SLC34A1`, `SLC13A3`, `VCAM1`, `HAVCR1`, `PROM1`, `CNR2`, `GPR55`, `FAAH`, `MGLL`, `NAPEPLD`, `DAGLA`, `DAGLB`, `TRPV1`, `SLC12A1`, `SLC12A3`, `AQP2`, `CALB1`, `SLC26A7`.
- Protocol genes missing in h5 index: (none).

## Host resources (feasibility is human opt-in)

- 24.0 GiB (hw.memsize). Compressed ADPKD RNA RDS is 1.81 GiB (double-gzip); inner XDR ≈ 2.53 GiB. Materializing a Seurat/dgCMatrix may still exceed this laptop. Unit 00 did **not** load counts.
- 153.3 GiB free / 460.4 GiB total. RAW tar / ATAC were not pulled.
- Do not enter Superpowers feasibility mode unless the human opts in.

## Unit 00 pass criteria

- ADPKD RNA counts + metadata reachable, `CNR1` in RDS scan, ≥2/4 PT-identity genes in RDS scan: **True**.
- DKD RNA h5s named and reachable, `CNR1` + ≥2/4 PT genes in h5 index: **True**.
- Gate S ineligible?: **False** (files present; n libraries 6 vs 5).
- **Unit 00 pass: True**

No biology conclusions. No Gate C/A/B/S marks. Next: Unit 01 freeze on both atlases before any *CNR1* differential.

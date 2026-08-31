# Unit 01 — frozen cell-state maps (study 1)

**Generated:** 2026-08-30 16:48 UTC
**Runners:** `pipeline/freeze_01_adpkd.R`, `pipeline/freeze_01_dkd.py`, `pipeline/freeze_01_report.py` (seed `20260829`).
**Must not (this unit):** *CNR1* to name clusters; Gate A or Gate S; freeze only one atlas then look at *CNR1* on the other.
**CNR1 in assignment gene list:** no. **Clustering:** no.

Both accessions frozen below. Units 02–06 may use these maps. Do not edit this freeze after seeing *CNR1* differentials; amend in `STATUS.md` if a change is required.

## GSE185948 (ADPKD atlas) — author labels

- Counts object: `dgCMatrix` 27970 genes × 102710 nuclei after double-gunzip of `GSE185948_count_RNA.rds.gz` (laptop RAM peak ~2.5 GiB; Spark not used).
- Join: metadata `name` ↔ matrix colnames, 102710/102710.
- **PT object:** `celltype` ∈ `{PT1, PT2}` (exact CSV tokens; not `PT-1`/`FR-PTC`). Do not re-derive PT from marker genes.
- **Failed-repair / injured PT:** no author FR token. Marker fallback **inside author PT only:** any of `VCAM1`, `HAVCR1`, `PROM1` raw count > 0.
- **Other epithelium:** `TAL1`, `TAL2` (loop), `DCT`, `CNT_PC`, `ICA`, `ICB` (connecting/collecting).
- **Excluded from Gate A and Gate S sides:** `ENDO`, `FIB`, `LEUK`, `PEC` (protocol), plus `PODO`, `URO1`, `URO2` (not PT and not the other-epi pool).
- n: PT **23172** (injured subset **12278**); other epithelium **55946**; excluded **23592**.
- Nucleus counts are **not** *CNR1* expression.

| patient | disease | n | n_PT | n_PT_injured | n_other |
| --- | --- | --- | --- | --- | --- |
| PKD1 | PKD | 9303 | 2677 | 2212 | 5129 |
| PKD2 | PKD | 10912 | 2718 | 2426 | 3394 |
| PKD3 | PKD | 9109 | 1842 | 1360 | 4399 |
| PKD4 | PKD | 9050 | 529 | 278 | 3113 |
| PKD5 | PKD | 7999 | 4243 | 3758 | 1821 |
| PKD6 | PKD | 10699 | 414 | 310 | 9240 |
| PKD7 | PKD | 2509 | 195 | 119 | 882 |
| PKD8 | PKD | 2492 | 31 | 17 | 2004 |
| control1 | control | 6412 | 1181 | 252 | 4592 |
| control2 | control | 9553 | 2206 | 509 | 6360 |
| control3 | control | 6696 | 1399 | 230 | 4795 |
| control4 | control | 10203 | 3973 | 586 | 5049 |
| control5 | control | 7773 | 1764 | 221 | 5168 |

- Patient × PT bins with n_PT < 10 (OSCA floor applies at Gate A/S, not here): **0**.
- Artifacts: `data/derived/GSE185948/cell_buckets.csv`, `freeze_summary.json`.

## GSE195460 (DKD atlas) — marker fallback

- No author cell-type table on GEO (Unit 00). Independent object; ADPKD *CNR1* was not used to choose this rule.
- Assignment genes only: PT identity `LRP2, CUBN, SLC34A1, SLC13A3`; injured `VCAM1, HAVCR1, PROM1`; other-epi `SLC12A1, SLC12A3, AQP2, CALB1, SLC26A7`.
- **Not used:** `CNR1`, descriptive ECS panel, `HK2`/`PKM`/`LDHA`. No Leiden/Louvain.
- **PT:** mean z(log1p PT-identity genes) ≥ mean z(log1p other-epi genes) **and** ≥2 PT-identity genes with count > 0. z-score across nuclei, ddof=0.
- **Injured PT:** PT ∩ any injured-gene count > 0.
- **Other epithelium:** not PT **and** z_other > z_pt **and** ≥1 other-epi gene count > 0 (the ≥1 floor is the documented operationalization of PROTOCOL’s other-epi marker pool; PROTOCOL states ≥2 only for PT).
- **Excluded from A/S:** neither PT nor other epithelium (immune/endo/stroma/PEC not labeled; they fall here if markers do not assign PT or other-epi).
- n: PT **25230** (injured subset **5162**); other epithelium **34779**; excluded **8231**; total nuclei **68240**.

| library | disease | n | n_PT | n_PT_injured | n_other |
| --- | --- | --- | --- | --- | --- |
| Control1 | control | 7069 | 2030 | 340 | 4322 |
| Control2 | control | 4362 | 2014 | 118 | 1694 |
| Control3 | control | 6763 | 2280 | 296 | 3660 |
| Control4 | control | 4784 | 1005 | 88 | 3440 |
| Control5 | control | 4990 | 1933 | 153 | 2609 |
| Control6 | control | 14617 | 7896 | 2156 | 6658 |
| DN1 | DKD | 5508 | 1824 | 381 | 2658 |
| DN2 | DKD | 3933 | 799 | 299 | 2034 |
| DN3 | DKD | 3817 | 590 | 118 | 2791 |
| DN4 | DKD | 6611 | 3054 | 785 | 2824 |
| DN5 | DKD | 5786 | 1805 | 428 | 2089 |

- Library × PT bins with n_PT < 10: **0**.
- Artifacts: `data/derived/GSE195460/cell_buckets.csv`, `freeze_summary.json`.

## Unit 01 pass criteria

- Each PT object defined without *CNR1*: **yes**.
- Other epithelium defined on both atlases: **yes**.
- Immune/endothelial/stroma excluded from Gate A and Gate S sides: **yes** (author tokens on GSE185948; unassigned remainder on GSE195460).
- **Unit 01 pass: True**

No Gate C/A/B/S numbers. Next: Unit 02 detection (*CNR1* count > 0 inside the frozen ADPKD PT object).

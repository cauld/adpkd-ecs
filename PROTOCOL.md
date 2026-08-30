# PROTOCOL (kill phase)

**Seal status:** DRAFT. After seal, do not edit sections marked CONFIRMATORY without a dated amendment in `STATUS.md`.

This protocol is **study 1 only**: Pathway A atlas kill (*CNR1* on GSE185948 + locked DKD specificity on GSE195460). Cannabis/CBD/tolvaptan evidence is [`studies/cannabis-safety/PROTOCOL.md`](studies/cannabis-safety/PROTOCOL.md). Docking, dual ligands, ADMET, and MQ1 stay in [`EXPLORE.md`](EXPLORE.md) until a **new** sealed protocol (study 3) after Decide.

Human-readable brief: [`PLAN.md`](PLAN.md). If PLAN and this file disagree, **this file wins**. Briefing: [`docs/briefing/cannabinoid-adpkd-pathways.md`](docs/briefing/cannabinoid-adpkd-pathways.md) is **not** confirmatory. Published claim under audit: Hinden et al., *Mol Med* 2026 ([doi:10.1186/s10020-026-01457-w](https://doi.org/10.1186/s10020-026-01457-w)).

**Seed:** `20260829` for any stochastic step (clustering fallback only).

## CONFIRMATORY — gene lists (freeze at seal)

**Kill gene (sole confirmatory expression test):** `CNR1`

**PT identity (assignment only; do not test these as the kill):** first present in the matrix, used as a **positive** PT signature, never including `CNR1`:

`LRP2, CUBN, SLC34A1, SLC13A3`

**Failed-repair / injured PT (assignment only):** `VCAM1, HAVCR1, PROM1`

If the author metadata already contains a PT or failed-repair label, **use that label** and do not re-derive it from these genes. The gene lists are the fallback when labels are absent (Unit 00 records which path **per accession**).

**Other epithelium (pooled contrast group):** labels or marker fallback containing (substring, first match): thick ascending limb / loop of Henle (`SLC12A1`), distal convoluted (`SLC12A3`), connecting / collecting (`AQP2`, `CALB1`, `SLC26A7`). Immune, endothelial, fibroblast, and parietal epithelium are **excluded** from both sides of Gate A and Gate S.

**Descriptive ECS panel (report; cannot pass or rescue Gate A or Gate S):**

`CNR2, GPR55, FAAH, MGLL, NAPEPLD, DAGLA, DAGLB, TRPV1`

**Must not enter assignment or DE gene lists for the kill:** `CNR1` as a cluster marker; glycolysis genes (`HK2`, `PKM`, `LDHA`) as PT definers.

## CONFIRMATORY — dataset roles

| Role | Dataset | Allowed |
|---|---|---|
| Define states (ADPKD) | GSE185948 snRNA. Prefer author `GSE185948_metadata_RNA.csv.gz` labels. Fallback: frozen marker assignment above. | Cell types. **No** using *CNR1* to name clusters. |
| Primary confirmatory (A/B/C) | Same object, ADPKD vs control as recorded in Unit 00 | Gate A/B/C on *CNR1* only |
| Define states (DKD) | GSE195460 Cell Ranger `filtered_feature_bc_matrix.h5` only: `GSE195460_Control1`…`Control5`, `GSM5837792_Control6`, `GSE195460_DN1`…`DN3`, `GSM5837797_DN4`, `GSM5837799_DN5` (names as on GEO/FTP). Prefer author cell-type labels if a metadata table exists; else marker fallback. | Same freeze rules. **No** *CNR1*-named clusters. **Do not** use GSE131882 `dgecounts.rds.gz` (zUMIs) as the confirmatory matrix. **Do not** require `GSE195460_RAW.tar`. ATAC h5/fragments are exploratory. |
| Specificity confirmatory (S) | Frozen DKD PT object, DKD vs control | Gate S only. **Cannot** pass Gate A. |
| Provenance only (Unit 00) | GEO landing pages, file names, sizes, license | Reachability. No count load before Seal |
| Not in study 1 kill | GSE7869, PDB 5XRA / 6KPF / 5M4V, FAERS, ChEMBL, Epidiolex/Jynarque labels | `EXPLORE.md` or study 2 |

Paired snATAC (`GSE185948_count_ATAC.rds.gz` and DKD ATAC if present) is **exploratory**. Do not use chromatin peaks to pass Gate A or Gate S.

**Freeze order:** Commit frozen label maps for **both** accessions in git **before** any *CNR1* differential on **either** accession (Unit 01 before Units 02–06).

## CONFIRMATORY — state definition wall

1. Unit 00: for each accession, record whether metadata has cell-type and disease/sample columns (column **names** only before Seal; after Seal, values for labels, not *CNR1* plots). Record n per disease group.
2. If author PT / injured-PT / failed-repair labels exist, freeze those strings in Unit 01 notes **per accession**. Do **not** cluster. Prefer tokens in the same family as Muto 2022 / Wilson 2022 (`PT`, `PT-1`/`PT-2`, `FR-PTC`, `N-PTC`, `PT_VCAM1`, `PCT`, `PST`, `PT_PROM1`) **only if they appear in metadata**; Unit 00 records the exact strings. Do not invent labels from the paper if the CSV uses different tokens.
3. If labels are missing: assign each nucleus to PT if mean z-score of available PT-identity genes ≥ mean z-score of available other-epithelium genes **and** at least 2 PT-identity genes are detected; failed-repair PT = PT ∩ (any of VCAM1/HAVCR1/PROM1 count > 0). No Leiden/Louvain whose features include *CNR1*. If unsupervised clustering is unavoidable, freeze: Scanpy PP defaults, `random_state=20260829`, resolution `0.5`, features = HVGs **excluding** `CNR1` and the descriptive ECS panel; then map clusters to PT by PT-identity genes only.
4. Do not use ADPKD *CNR1* results to choose DKD clustering, labels, or estimator.

## CONFIRMATORY — statistics

**Gate C:** detection = fraction of nuclei in the frozen **ADPKD-atlas** PT / failed-repair object with `CNR1` count > 0. Thresholds in `KILL.md`.

**C_S:** same detection definition on the frozen **DKD-atlas** PT object. Eligibility for Gate S only.

**Which Gate A contrast:** If Unit 00 records ≥ 3 ADPKD samples **and** ≥ 3 control samples → **A1** (within PT, ADPKD vs control). Else → **A2** (within ADPKD, PT vs other epithelium). Do not run A1 after seeing A2 *CNR1* results.

**Gate A / Gate S estimator:**

- If the chosen contrast has **≥ 3** samples per group: **pseudobulk** — sum **raw** counts per sample in the contrast cells (not averaged normalized nucleus values), `log1p` of CPM, Welch t on sample means of *CNR1*. **Drop** donor × PT bins with **< 10** nuclei before the t-test (OSCA-style floor). Pass rules in `KILL.md`. This t-test is the **sole** pass metric; do not add edgeR/limma as an alternate pass route.
- Else: nucleus-level Wilcoxon rank-sum, two-sided. Pass = p < 0.05 **and** Hodges–Lehmann difference in the hypothesized direction. Report Cliff’s delta; it is not the pass metric.

**Multiple testing:** one confirmatory gene per gate. Descriptive ECS genes: same contrast, FDR-adjusted, narrative only.

**Gate B:** see `KILL.md`. B1 is a protocol check. B2/B3 are reported after A; they cannot convert an A fail into a pass.

**Gate S:** see `KILL.md`. Do not score all cells to pass S.

## CONFIRMATORY — pass/fail

See `KILL.md`. Human marks gates. Agent may draft numbers.

## How (operational, not outcome-fitted)

- Environment: `uv sync`; after Seal, `uv sync --group scrna` for Units 01+.
- Raw files under `data/raw/` (gitignored), checksums in `research/data-inventory.md`.
- Do not use university proxy for publisher PDFs. Human drops e-library PDFs if needed.
- GEO ADPKD: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE185948
- GEO DKD: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE195460
- DGX Spark is allowed for load/compute after Seal; ARM/aarch64 build issues are operational, not a reason to change confirmatory fields.

## Sample size (fixed public n)

A1/S use the donors in the accessions (Hinden reported 8 vs 5 ADPKD/control and 5 vs 6 DKD/control; Unit 00 records actual n). These tests are powered only for **large** donor-level effects. A fail does **not** prove absence of within-PT induction.

## Clarify (2026-08-30, before Seal)

1. DKD confirmatory files are the GSE195460 Cell Ranger RNA h5s listed above, not GSE131882 zUMIs RDS.
2. Author label tokens are recorded in Unit 00; paper strings are a search aid only.
3. Pseudobulk floor: ≥10 nuclei per donor × PT bin.
4. Welch t remains the only confirmatory estimator when n≥3; edgeR is not a second gate.
5. Underpowered fail ≠ “ECS unchanged” (see Sample size).

## Amendments

None after Seal. (2026-08-30 draft: DKD Gate S + Clarify 1–5 before Seal.)

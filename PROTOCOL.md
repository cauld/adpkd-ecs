# PROTOCOL (kill phase)

**Seal status:** DRAFT. After seal, do not edit sections marked CONFIRMATORY without a dated amendment in `STATUS.md`.

This protocol is **only the v1 kill test** (Pathway A: *CNR1* localization on GSE185948). Docking, dual ligands, ADMET, MQ1, DKD specificity, and bulk microarray require a new sealed protocol.

Human-readable brief: [`PLAN.md`](PLAN.md). If PLAN and this file disagree, **this file wins**. Briefing: [`docs/briefing/cannabinoid-adpkd-pathways.md`](docs/briefing/cannabinoid-adpkd-pathways.md) is **not** confirmatory.

**Seed:** `20260829` for any stochastic step (clustering fallback only).

## CONFIRMATORY — gene lists (freeze at seal)

**Kill gene (sole confirmatory expression test):** `CNR1`

**PT identity (assignment only; do not test these as the kill):** first present in the matrix, used as a **positive** PT signature, never including `CNR1`:

`LRP2, CUBN, SLC34A1, SLC13A3`

**Failed-repair / injured PT (assignment only):** `VCAM1, HAVCR1, PROM1`

If the author metadata already contains a PT or failed-repair label, **use that label** and do not re-derive it from these genes. The gene lists are the fallback when labels are absent (Unit 00 records which path).

**Other epithelium (pooled contrast group):** labels or marker fallback containing (substring, first match): thick ascending limb / loop of Henle (`SLC12A1`), distal convoluted (`SLC12A3`), connecting / collecting (`AQP2`, `CALB1`, `SLC26A7`). Immune, endothelial, fibroblast, and parietal epithelium are **excluded** from both sides of Gate A.

**Descriptive ECS panel (report; cannot pass or rescue Gate A):**

`CNR2, GPR55, FAAH, MGLL, NAPEPLD, DAGLA, DAGLB, TRPV1`

**Must not enter assignment or DE gene lists for the kill:** `CNR1` as a cluster marker; glycolysis genes (`HK2`, `PKM`, `LDHA`) as PT definers.

## CONFIRMATORY — dataset roles

| Role | Dataset | Allowed |
|---|---|---|
| Define states | GSE185948 snRNA. Prefer author `GSE185948_metadata_RNA.csv.gz` labels. Fallback: frozen marker assignment above. | Cell types. **No** using *CNR1* to name clusters. |
| Primary confirmatory | Same object, ADPKD donors/samples as recorded in Unit 00 | Gate A/B/C on *CNR1* only |
| Provenance only (Unit 00) | GEO landing page, file names, sizes, license | Reachability. No count load before Seal |
| Not in v1 kill | GSE7869, GSE195460, PDB 5XRA / 6KPF / 5M4V, FAERS, ChEMBL | EXPLORE.md |

Paired snATAC (`GSE185948_count_ATAC.rds.gz`) is **exploratory**. Do not use chromatin peaks to pass Gate A.

## CONFIRMATORY — state definition wall

1. Unit 00: record whether metadata has cell-type and disease/sample columns (column **names** only before Seal; after Seal, values for labels, not *CNR1* plots).
2. If author PT / injured-PT / failed-repair labels exist, freeze those strings in Unit 01 notes. Do **not** cluster.
3. If labels are missing: assign each nucleus to PT if mean z-score of available PT-identity genes ≥ mean z-score of available other-epithelium genes **and** at least 2 PT-identity genes are detected; failed-repair PT = PT ∩ (any of VCAM1/HAVCR1/PROM1 count > 0). No Leiden/Louvain whose features include *CNR1*. If unsupervised clustering is unavoidable, freeze: Scanpy PP defaults, `random_state=20260829`, resolution `0.5`, features = HVGs **excluding** `CNR1` and the descriptive ECS panel; then map clusters to PT by PT-identity genes only.
4. Commit the frozen label mapping in git **before** any *CNR1* differential (Unit 02 before Unit 03).

## CONFIRMATORY — statistics

**Gate C:** detection = fraction of nuclei in the frozen PT / failed-repair object with `CNR1` count > 0. Thresholds in `KILL.md`.

**Which Gate A contrast:** If Unit 00 records ≥ 3 ADPKD samples **and** ≥ 3 control samples → **A1** (within PT, ADPKD vs control). Else → **A2** (within ADPKD, PT vs other epithelium). Do not run A1 after seeing A2 *CNR1* results.

**Gate A estimator:**

- If the chosen contrast has **≥ 3** samples per group: **pseudobulk** — sum counts per sample in the contrast cells, `log1p` of CPM, Welch t on sample means of *CNR1*. Pass = 95% CI excludes 0 and direction matches `KILL.md`.
- Else: nucleus-level Wilcoxon rank-sum, two-sided. Pass = p < 0.05 **and** Hodges–Lehmann difference in the hypothesized direction. Report Cliff’s delta; it is not the pass metric.

**Multiple testing:** one confirmatory gene. Descriptive ECS genes: same contrast, FDR-adjusted, narrative only.

**Gate B:** see `KILL.md`. B1 is a protocol check. B2/B3 are reported after A; they cannot convert an A fail into a pass.

## CONFIRMATORY — pass/fail

See `KILL.md`. Human marks gates. Agent may draft numbers.

## How (operational, not outcome-fitted)

- Environment: `uv sync`; after Seal, `uv sync --group scrna` for Units 01+.
- Raw files under `data/raw/` (gitignored), checksums in `research/data-inventory.md`.
- Do not use university proxy for publisher PDFs.
- GEO: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE185948

## Amendments

None.

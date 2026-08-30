# CNR1 localization and DKD specificity (GSE185948 + GSE195460)

**Research question:** After freezing proximal-tubule / failed-repair epithelium without *CNR1* as a marker, is *CNR1* higher in ADPKD than in control inside that state in GSE185948 (after a composition check), and is that within-PT induction absent in diabetic kidney disease under the same freeze (GSE195460)?

**Background / motivation:** Hinden et al. (*Mol Med* 2026) and the source briefing argue ECS collapse in ADPKD (*CNR1* up in failed-repair PT, little change in DKD) as the rationale for peripheral CB1 blockade. Their ADPKD snRNA primary statistic averaged expression across all cell types per sample. This study is a registered audit: frozen states, within-PT A1, composition wall, locked DKD contrast. Sibling repo `ecs-lab` is a harvest lab. Study 2 (cannabis/CBD safety) is a separate seal. Root SEAL files are the contract; this page is the Superpowers framing copy.

**Hypotheses:**
- H0 (null): After frozen PT assignment, *CNR1* 95% CI for the locked ADPKD contrast (A1 or A2) includes 0, or detection is below Gate C.
- H1 (alternative): Gate C passes and the locked ADPKD contrast shows higher *CNR1* in the hypothesized group.
- H0_S: If A1 passed and S is eligible, within DKD-atlas PT the DKD−control *CNR1* CI excludes 0 with DKD higher (same pattern as A1).
- H1_S (specificity): A1 passed and S contrast does not show DKD-higher *CNR1* (CI includes 0 or opposite direction).

**Population & unit of analysis:** Human kidney nuclei in GSE185948 (primary) and GSE195460 (specificity). Confirmatory tests are sample-level pseudobulk when n allows; otherwise nucleus-level ranks. Unit of Decide is study 1 (human-marked gates).

**Key variables (operationalized):**
- Outcome: *CNR1* expression (counts → locked CPM/log1p or ranks)
- Predictor / grouping: frozen PT / failed-repair vs other epithelium; disease label for A1 and S
- Confounders: cell-type composition (`p_PT`); constitutive PT expression (A1 vs A2 split); generic injury (Gate S)

**What counts as an answer:** Human-marked gates in `KILL.md`. Exact estimators in `PROTOCOL.md`.

**Scope & exclusions:** No docking, dual ligands, CYP models, MQ1, GSE7869 primary, wet lab, or clinical advice. Cannabis/CBD/tolvaptan counseling is study 2. Those stay in `EXPLORE.md` or `studies/cannabis-safety/`.

**Open questions for prior-work survey:** Author cell-type ontology for both accessions; exact DKD count-matrix filenames on GEO; standard failed-repair PT markers in human kidney atlases (do not add *CNR1* to that list after seeing results).

**Canonical SEAL copies:** repo-root `QUESTION.md`, `KILL.md`, `CLAIMS.md`, `PROTOCOL.md`. If this file and those disagree after Seal, SEAL wins.

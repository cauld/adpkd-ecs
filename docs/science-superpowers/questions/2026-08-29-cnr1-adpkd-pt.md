# CNR1 localization in ADPKD snRNA-seq (GSE185948)

**Research question:** In public adult ADPKD snRNA-seq (GSE185948), is *CNR1* expression enriched in a proximal-tubule / failed-repair epithelial state defined without *CNR1* as a marker, and — if control kidneys exist in the accession — is that enrichment ADPKD-vs-control inside PT rather than a constitutive PT marker or a cell-type composition artifact?

**Background / motivation:** A written briefing argues ECS collapse in ADPKD (*CNR1* up in failed-repair PT, ligands down) as the rationale for peripheral CB1 blockade and later docking. That localization claim is the cheapest public-data falsifier. Sibling repo `ecs-lab` is a harvest lab; this study answers one question. SEAL files at repo root are the contract; this page is the Superpowers framing copy.

**Hypotheses:**
- H0 (null): After frozen PT assignment, *CNR1* 95% CI for the locked contrast (A1: ADPKD vs control within PT; else A2: PT vs other epithelium in ADPKD) includes 0, or detection is below Gate C.
- H1 (alternative): Gate C passes and the locked contrast shows higher *CNR1* in the hypothesized group (ADPKD PT or PT vs other epithelium).

**Population & unit of analysis:** Human kidney nuclei in GSE185948. Confirmatory tests are sample-level pseudobulk when n allows; otherwise nucleus-level ranks. Unit of Decide is the study (human-marked gates).

**Key variables (operationalized):**
- Outcome: *CNR1* expression (counts → locked CPM/log1p or ranks)
- Predictor / grouping: frozen PT / failed-repair vs other epithelium; disease label if A1
- Confounders: cell-type composition (`p_PT`); constitutive PT expression (A1 vs A2 split)

**What counts as an answer:** Human-marked gates in `KILL.md`. Exact estimators in `PROTOCOL.md`.

**Scope & exclusions:** No docking, dual ligands, CYP, MQ1, GSE7869 primary, GSE195460, wet lab, or clinical advice. Those stay in `EXPLORE.md`.

**Open questions for prior-work survey:** Author cell-type ontology for GSE185948; whether controls are in the series; standard failed-repair PT markers in human ADPKD atlases (do not add *CNR1* to that list after seeing results).

**Canonical SEAL copies:** `QUESTION.md`, `KILL.md`, `CLAIMS.md`, `PROTOCOL.md`. If this file and those disagree after Seal, SEAL wins.

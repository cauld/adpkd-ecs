# Prior-work survey — study 1 (*CNR1* atlas kill)

**Date:** 2026-08-30  
**Question:** [`../questions/2026-08-29-cnr1-adpkd-pt.md`](../questions/2026-08-29-cnr1-adpkd-pt.md)  
**Constraint:** GEO landing pages and papers only. No count-matrix load. No *CNR1* plots.

## Relationship to prior work

This is a **registered audit / extension**, not a first discovery. Hinden et al., *Mol Med* 2026 ([doi:10.1186/s10020-026-01457-w](https://doi.org/10.1186/s10020-026-01457-w), PMC13104467) already reported *CNR1* up in GSE185948 and little ECS change in GSE195460. Their snRNA primary statistic averaged expression **across all cell types per sample**. Muto et al., *Nat Commun* 2022 ([doi:10.1038/s41467-022-34255-z](https://www.nature.com/articles/s41467-022-34255-z)) is the ADPKD atlas (cell states, not ECS). Wilson et al., *Nat Commun* 2022 ([doi:10.1038/s41467-022-32972-z](https://doi.org/10.1038/s41467-022-32972-z)) is the DKD atlas (GSE195460).

## Established methods (adopted)

- **Unit of inference = donor**, not nucleus. Sum counts per (donor × frozen cell type), then a sample-level test (Crowell/muscat 2020; Squair et al. 2021; OSCA `pseudoBulkDGE`). Nucleus Wilcoxon is reserved for n < 3 per group as already locked.
- **Pass metric stays Welch t 95% CI on log1p(CPM) of *CNR1* only** — Type I honest for one pre-specified gene; conservative vs edgeR QL at this n. Do **not** add edgeR as a second pass route (researcher degrees of freedom).
- **Composition:** test inside frozen PT; all-cell means cannot pass A or S (Trapnell 2015; Gate B3 diagnostic only).

## Confounds (already in `KILL.md`)

1. Composition (π change without μ change).  
2. Constitutive PT marker (A2 ≠ induction).  
3. Generic injury (Gate S).  
Additional operational: sparse detection (Gate C / C_S); procurement mix (tumor nephrectomy vs healthy) — accepted limitation, not adjustable in public metadata.

## Prior effect size / power

Hinden reported a significant all-cell *CNR1* difference; that is **not** a usable within-PT effect size for A1. Fixed public n (Hinden: ADPKD 8 vs control 5; DKD 5 vs control 6) is **underpowered for modest fold changes** (Schurch et al. 2016: ≥6–12 per group for modest DE). A1/S are **large-effect** tests. **Fail ≠ proof of no induction.** Scribe must not convert a fail into “ECS is normal.”

## Marker lists

PT identity `LRP2, CUBN, SLC34A1, SLC13A3` and injured `VCAM1, HAVCR1, PROM1` are defensible **assignment** genes (Kirita 2020 FR-PTC *Vcam1*; Muto 2021/2022 `PT_VCAM1` / FR-PTC). The union is a **broad injured PT** object, not Kirita-strict FR-PTC-only. Prefer author labels. **Do not add *CNR1*.**

Muto 2022 paper strings (lock from metadata in Unit 00, not from this list as a second ontology): top-level `PT`, `PT-1`, `PT-2`; control PT `N-PTC`, `FR-PTC`; ADPKD PT subcluster `PT-1`…`PT-4`. Wilson 2022 family: `PT_VCAM1`, `PT_PROM1`, `PCT`, `PST`.

## DKD files (landing page / FTP; not loaded)

No single GSE195460 RDS. Use **Cell Ranger `filtered_feature_bc_matrix.h5`** on GSE195460 (Control1–6, DN1–5). Do **not** use GSE131882 zUMIs `dgecounts.rds.gz` as the confirmatory matrix (different pipeline). Skip `GSE195460_RAW.tar` (14 GiB, ATAC fragments). Hinden: Cell Ranger filtered matrices from GEO; n=5 DKD, n=6 controls.

## Citations (methods)

Crowell et al. 2020 https://doi.org/10.1038/s41467-020-19894-4  
Squair et al. 2021 https://doi.org/10.1038/s41467-021-25960-2  
OSCA multi-sample: https://bioconductor.org/books/release/OSCA.multisample/multi-sample-comparisons.html  
Schurch et al. 2016 https://doi.org/10.1261/rna.053959.115  
Kirita et al. 2020 (FR-PTC) — PNAS GSE139107  
Muto 2022 https://doi.org/10.1038/s41467-022-34255-z  
Wilson 2022 https://doi.org/10.1038/s41467-022-32972-z  
Hinden 2026 https://doi.org/10.1186/s10020-026-01457-w  

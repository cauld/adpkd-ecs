# Study 1 report — *CNR1* atlas kill (GSE185948)

**Decide.** 2026-09-01. Gate **C fail**. Stop this ADPKD accession; do not dock.  
**Scribe ceiling.** [`CLAIMS.md`](../CLAIMS.md) and [`DECIDE.md`](../DECIDE.md). This is not study 2.  
**Lock.** Git Seal `db44b3086ae8c4d640dc40f44945bcef27ffe6bc` · OSF https://osf.io/7g3tn/  
**Re-run (this report).** 2026-09-03 13:19 UTC · `Rscript pipeline/gate_c_02.R` · R 4.6.1 · Matrix 1.7.5 · same 51 / 23172.

## Question

After freezing proximal-tubule / failed-repair epithelium **without** *CNR1* as a marker, is *CNR1* higher in ADPKD than in control inside that state in GSE185948, and is that within-PT induction absent in DKD (GSE195460)?

Gate C is a detectability screen that must pass before those contrasts run.

## Confirmatory (as registered)

**Object.** Frozen GSE185948 PT: author `celltype` ∈ `{PT1, PT2}` (Unit 01). n = **23172** nuclei. *CNR1* was not used to name the state.

**Estimator.** Fraction of those nuclei with *CNR1* matrix value > 0. Thresholds in `KILL.md`: ≥ **1%** and n ≥ **100**.

**Result.** **51** nuclei positive. Fraction **0.002201** (0.2201%). n ≥ 100: yes. Fraction ≥ 0.01: no. Gate C **fail**.

**Consequence (registered).** Do not run Gate A or Gate S. Decide row: stop this ADPKD accession; do not dock.

Claim 1 in `CLAIMS.md` (detectability in the frozen PT state) is **not** made. Claims 2–6 were not eligible.

## Exploratory (not Decide)

- Deposited `count_RNA` values are log-like (PT max 1.84), not integer UMI. Gate C used value > 0 on that object. For a 0-preserving transform this should match UMI > 0; integer UMIs were not re-derived from GEO gzip.
- Full matrix: 247 / 102710 nuclei *CNR1* > 0 (gene-row check only). Not a pass.
- Injured-PT-only, PT2-only, and all-nuclei detection were not used to mark C.
- Plugin `prereg.sh audit` fails INTEGRITY against first commit `95780fa`. This study’s lock is human Seal `db44b30` + OSF. Gate C’s 1% / 100 text is unchanged from `95780fa` through that Seal. Do not call this a plugin-style confirmatory finding.

## What this is not

*CNR1* absent from kidney or from ADPKD PT. ECS biologically “dark” as protein. Hinden et al. 2026 disproved (their statistic was not this test). Gate A tested. Docking banned forever. Patients should start or stop cannabis, CBD, THCV, or CB1 drugs. CBD–tolvaptan (study 2).

## Limitations

Public snRNA; GPCRs are sparse; 1% is a locked floor, not a biological proof of absence. Controls exist in GSE185948 but were not contrasted because C failed. GSE195460 was frozen in Unit 01 and then not used for *CNR1*.

## Reproducibility

- Seed `20260829` (detection is deterministic).
- Raw files: GEO GSE185948 / GSE195460; SHA-256 in [`raw-checksums.txt`](raw-checksums.txt) and [`data-inventory.md`](data-inventory.md). Counts stay on GEO; not uploaded to OSF.
- Re-run Gate C: `Rscript pipeline/gate_c_02.R` after Unit 01 derived RDS exists.
- Environment: Python 3.12 via `uv` (`uv.lock`); R 4.6.1 + `Matrix` for this runner.
- Numbers: [`02-detection.md`](02-detection.md), [`gate_c_stats.json`](gate_c_stats.json).

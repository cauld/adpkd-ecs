# Unit 06 — Converge (study 1)

**Generated:** 2026-09-01  
**Reads:** `KILL.md`, `PROTOCOL.md`, `CLAIMS.md`, `research/02-detection.md`, Units 00–02.  
**Must not:** edit CONFIRMATORY fields to match figures; import study 2 DDI language.

## What ran vs what the seal required

| Sealed step | Output | Match? |
|---|---|---|
| Unit 00 inventory both GEO; no *CNR1* plots | `research/data-inventory.md` | Yes. A1 eligible (8 vs 5). S eligible (6 vs 5 libraries). |
| Unit 01 freeze both atlases without *CNR1*; commit before detection | `research/01-frozen-labels.md` | Yes. GSE185948 author `PT1`/`PT2` (n_PT = 23172). No `FR-PTC` token on GEO. GSE195460 marker fallback. |
| Unit 02 Gate C on frozen **ADPKD** PT only | `research/02-detection.md` | Yes. 51 / 23172 = 0.2201%. DKD not loaded. No ADPKD vs control. 1% / 100 not moved. |
| Gate C pass ≥ 1% and n ≥ 100 | Numbers vs `KILL.md` | **Fail.** n ≥ 100 true; fraction ≥ 0.01 false. |
| If C fail: do not run A or S | Units 03–05 | **Skipped.** |
| Decide table row `C fail` | `DECIDE.md` | Stop this ADPKD accession; do not dock. |

## Gaps (append-only; not protocol rewrites)

- Gate A / B / S: not run (correct under C fail). `QUESTION.md` induction and DKD clauses remain untested.
- Welch pseudobulk simulation (analysis-plan Task 3): not run; it was a Gate A estimator check, not required to score C.
- `prereg.sh audit` fails INTEGRITY against first commit `95780fa`. Repo lock is Seal `db44b30` + OSF. Gate C thresholds unchanged since `95780fa`. Documented in `DECIDE.md`; not a license to ignore `KILL.md`.
- Deposited matrix is log-like, not integer UMI. Documented; 1% bar not moved.

## Leftovers → `EXPLORE.md`

Study 3 docking, protein/*CNR1* assays, integer-UMI re-extraction, other accessions: not this Decide. Study 2 remains its own seal.

## Red-team (before Decide)

Adversarial review 2026-09-01: operational C-fail + skip A/S **survives**. No Critical that flips the inequality. Important: do not use plugin confirmatory label; do not upgrade to *CNR1*-absent / Hinden-refuted / docking-forever; state log-like estimator. Those ceilings are in `DECIDE.md`.

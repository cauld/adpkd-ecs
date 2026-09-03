# Decide (study 1)

**Date.** 2026-09-01 (chat: mark Gate C with the fail recommendation and proceed).  
**Human marks.** Gate **C fail**. Gates **A, B, S not run**.  
**Decision.** C fail → **stop this ADPKD accession; do not dock** (`KILL.md` Decide table).  
**Protocol freeze.** `db44b3086ae8c4d640dc40f44945bcef27ffe6bc` + OSF https://osf.io/7g3tn/ .

This is not study 2. Do not import cannabis/CBD/tolvaptan claims.

---

## Confirmatory (≤ `CLAIMS.md`)

1. In the frozen GSE185948 PT object (`celltype` ∈ `{PT1, PT2}`, n = **23172**, defined without *CNR1*), *CNR1* matrix value > 0 in **51** nuclei (**0.2201%**). n ≥ 100 holds; detection ≥ 1% does not. Gate C **fail**. Claim 1 in `CLAIMS.md` (detectability in that state) is **not** made.

2. Gate A (within-PT ADPKD vs control) and Gate S (DKD specificity) were **not run**. This Decide does **not** answer `QUESTION.md`’s induction or specificity clauses. It is a detectability stop, not a finding that induction is absent, and not a refutation of Hinden et al.’s all-cell statistic.

3. States were frozen without *CNR1* (Unit 01) before this detection table. Freeze order was not broken.

4. Chemistry (study 3 / docking) is **not** licensed from this Decide. A later assay, accession, or protein readout would need a **new** sealed protocol, specified before looking.

## Must not (scribe)

*CNR1* is absent from kidney or from ADPKD PT. ECS is biologically “dark” as a protein/pathway claim. Hinden et al. 2026 is disproved. Patients should start or stop cannabis, CBD, THCV, or CB1 antagonists. CB1 is or is not the driver of cysts. Docking is banned forever. Gate A was tested. CBD–tolvaptan (study 2). Lowering the 1% bar after seeing 0.22%.

**Framing.** Registered audit of the published *CNR1* map: on this snRNA object, frozen PT is below the pre-specified detection floor. Stop this accession.

---

## Estimator and lock (not slogans)

- Deposited `count_RNA` values are **log-like** (PT max 1.84), not integer UMI. Gate C is value > 0 on that matrix. For a 0-preserving transform this should match UMI > 0; integer UMIs were not re-derived from GEO gzip for Decide.
- Plugin `prereg.sh audit` **fails** INTEGRITY because it treats first commit `95780fa` as freeze; this repo’s confirmatory lock is human Seal `db44b30` + OSF, and Gate C’s 1% / 100 text is unchanged from `95780fa` through that Seal. Do not call this a plugin-style confirmatory finding. Call it locked by this study’s git-seal/OSF contract.
- Full-matrix *CNR1* > 0 in 247 / 102710 nuclei is a gene-row check only, not a pass.

---

## Exploratory (not confirmatory; not Decide)

Injured-PT-only, PT2-only, or all-nuclei detection were not used to mark C. snRNA dropout vs biology is unresolved and is not a reason to move 1%. Integer-UMI re-extraction from GEO gzip is a leftover if anyone reopens chemistry under a new protocol.

Leftovers: [`EXPLORE.md`](EXPLORE.md). Converge: [`research/06-converge.md`](research/06-converge.md). Scribe: [`research/07-scribe.md`](research/07-scribe.md). OSF packet: [`docs/osf/study1-closeout.md`](docs/osf/study1-closeout.md).

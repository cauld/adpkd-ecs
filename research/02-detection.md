# Unit 02 — Gate C detection (study 1)

**Generated:** 2026-09-03 13:19 UTC
**Runner:** `pipeline/gate_c_02.R` (seed `20260829`; detection is deterministic).
**Object:** Frozen GSE185948 PT (`is_pt` from Unit 01: `celltype` ∈ `{PT1, PT2}`, including injured subset).
**Must not (this unit):** change 1% / 100 after seeing Gate A or S; DKD *CNR1*; *CNR1*-defined PT; Gate A contrast.

## Detection

- n nuclei in frozen PT / failed-repair object: **23172**.
- Nuclei with *CNR1* matrix value > 0: **51**.
- Detection fraction: **0.002201** (0.2201%).
- Max *CNR1* value in frozen PT: **1.8376** (non-integer; deposited `count_RNA` is log-like, not integer UMI).
- Estimator: indicator value > 0 on the Unit 01 RDS, unweighted over nuclei in the frozen PT object. Same >0 rule as `KILL.md` / `PROTOCOL.md` Gate C. No pseudobulk. No ADPKD vs control split (that is Gate A). No DKD matrix loaded.

## Diagnostics (not Gate C)

- *CNR1* is a unique row (neighbors `HTR1E`, `AL590814.1`).
- Full GSE185948 matrix: **247** / **102710** nuclei have *CNR1* > 0 (join and gene-row check only; not a localization claim; not used to change 1% / 100).

## Frozen decision rule (`KILL.md` Gate C)

- Pass if detection ≥ **1%** **and** n ≥ **100**.
- n ≥ 100: **TRUE**.
- fraction ≥ 0.01: **FALSE**.
- Numbers meet the written rule: **FALSE**.
- **Gate C mark is human.** Agent does not pass or fail the gate.

No Gate A/B/S numbers. If the human marks C fail, do not run A or S.

Human Gate C mark is recorded in `DECIDE.md` / `STATUS.md`, not in this generated file.


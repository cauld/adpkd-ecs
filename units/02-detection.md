---
id: 02
role: Operator
status: done
reads:
  - PROTOCOL.md
  - KILL.md
  - research/01-frozen-labels.md
must_not:
  - Change detection thresholds after seeing Gate A or Gate S
---

# Unit 02 — Gate C detection

**Goal.** *CNR1* detectability in the frozen **ADPKD-atlas** PT object.

**Procedure.** Compute fraction of nuclei with count > 0 and n. Write `research/02-detection.md`. Human marks Gate C. Do not interpret DKD *CNR1* here.

**Pass criteria.** `KILL.md` Gate C.

## Notes (after run)

- Ran 2026-09-01. Output: `research/02-detection.md`. Runner: `pipeline/gate_c_02.R`.
- Frozen PT n = **23172** (matches Unit 01). *CNR1* unique row. DKD not loaded. No ADPKD vs control split.
- Detection: **51** / 23172 = **0.2201%**. n ≥ 100: yes. fraction ≥ 1%: no. Numbers meet the written `KILL.md` Gate C rule: **no**.
- Deposited `count_RNA` values are log-like (PT max 1.84), not integer UMI. Gate C uses value > 0 on that matrix.
- Full-matrix sanity (not Gate C): 247 / 102710 nuclei *CNR1* > 0 — not a missing-gene or empty-join failure.
- **Gate C mark is human.** Do not start Unit 03 until marked. If C fail, do not run A or S.
- Human mark **2026-09-01 (chat):** Gate C **fail**. See [`DECIDE.md`](../DECIDE.md). Units 03–05 not started.

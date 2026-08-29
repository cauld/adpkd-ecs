---
id: 01
role: Operator
status: blocked-until-seal
reads:
  - PROTOCOL.md
  - research/data-inventory.md
must_not:
  - Use CNR1 to name or merge clusters
  - Run Gate A
---

# Unit 01 — Freeze PT labels

**Goal.** Commit the cell-state map used for Gates C–B. Author labels if present; else marker fallback in `PROTOCOL.md`.

**Inputs.** Inventory; frozen gene lists.

**Procedure.**

1. If metadata has PT / injured-PT / failed-repair strings, lock the exact strings in `research/01-frozen-labels.md`.
2. Else apply marker assignment; write the rule and n per bucket. Stochastic clustering only as `PROTOCOL.md` fallback (`random_state=20260829`, HVGs excluding ECS panel).
3. Commit before Unit 02 *CNR1* detection tables are interpreted as pass/fail.

**Outputs.** `research/01-frozen-labels.md` (+ optional `research/01-frozen-labels.json`)

**Pass criteria.** PT object defined without *CNR1*. Other epithelium defined. Immune/endothelial/stroma excluded from Gate A.

## Notes (after run)

- Not run.

---
id: 01
role: Operator
status: blocked-until-osf
reads:
  - PROTOCOL.md
  - research/data-inventory.md
must_not:
  - Use CNR1 to name or merge clusters
  - Run Gate A or Gate S
  - Freeze only one atlas then look at CNR1 on the other
---

# Unit 01 — Freeze PT labels (both atlases)

**Goal.** Commit the cell-state maps used for Gates C–S. Author labels if present; else marker fallback in `PROTOCOL.md`. **Both** accessions before any *CNR1* differential.

**Inputs.** Inventory; frozen gene lists.

**Procedure.**

1. GSE185948: if metadata has PT / injured-PT / failed-repair strings, lock the exact strings in `research/01-frozen-labels.md`. Else apply marker assignment; write the rule and n per bucket. Stochastic clustering only as `PROTOCOL.md` fallback (`random_state=20260829`, HVGs excluding ECS panel).
2. GSE195460 (and count files Unit 00 named): same rules, same gene lists, independent object. Record exact label strings or marker path.
3. Commit both maps before Unit 02 *CNR1* detection tables are interpreted as pass/fail.

**Outputs.** `research/01-frozen-labels.md` (+ optional JSON per accession)

**Pass criteria.** Each PT object defined without *CNR1*. Other epithelium defined. Immune/endothelial/stroma excluded from Gate A and Gate S.

## Notes (after run)

- Not run.

# Units

A **unit** is BMAD’s story file without Agile: everything the Operator needs in one place. One unit, one run, one note.

Kill protocol is **git-sealed**. OSF: https://osf.io/7g3tn/ . **Decide 2026-09-01:** Gate C fail. Units 03–05 skipped.

| ID | Title | Gate | Depends on |
|---|---|---|---|
| 00 | Data access inventory (both GEO) | — | **done** 2026-08-30 |
| 01 | Freeze PT / failed-repair labels (both atlases) | — | **done** 2026-08-30 |
| 02 | *CNR1* detection (ADPKD) | C | **fail** 2026-09-01 |
| 03 | Gate A contrast | A | **skipped** (C fail) |
| 04 | Gate B diagnostics | B | **skipped** (C fail) |
| 05 | Gate S DKD specificity | S | **skipped** (C fail) |
| 06 | Converge + Decide | — | **done** 2026-09-01 |

Templates: [`_template.md`](_template.md) or [`.seal/templates/unit.md`](../.seal/templates/unit.md). After a run, fill **Notes**. Operator does not edit sealed `PROTOCOL.md` confirmatory fields.

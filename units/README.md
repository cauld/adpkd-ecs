# Units

A **unit** is BMAD’s story file without Agile: everything the Operator needs in one place. One unit, one run, one note.

Kill protocol is **git-sealed**. OSF: https://osf.io/7g3tn/ . Units 00–01 done. Unit 02 Gate C is next.

| ID | Title | Gate | Depends on |
|---|---|---|---|
| 00 | Data access inventory (both GEO) | — | **done** 2026-08-30 |
| 01 | Freeze PT / failed-repair labels (both atlases) | — | **done** 2026-08-30 |
| 02 | *CNR1* detection (ADPKD) | C | 01 |
| 03 | Gate A contrast | A | 02 |
| 04 | Gate B diagnostics | B | 03 (A pass to interpret) |
| 05 | Gate S DKD specificity | S | 01 + A1 pass |
| 06 | Converge + Decide | — | 03–05 as applicable |

Templates: [`_template.md`](_template.md) or [`.seal/templates/unit.md`](../.seal/templates/unit.md). After a run, fill **Notes**. Operator does not edit sealed `PROTOCOL.md` confirmatory fields.

# Units

A **unit** is BMAD’s story file without Agile: everything the Operator needs in one place. One unit, one run, one note.

Kill protocol is **git-sealed**. Do not run Units 00–06 until OSF submit is in `STATUS.md` (inventory without *CNR1* plots).

| ID | Title | Gate | Depends on |
|---|---|---|---|
| 00 | Data access inventory (both GEO) | — | After OSF |
| 01 | Freeze PT / failed-repair labels (both atlases) | — | 00 |
| 02 | *CNR1* detection (ADPKD) | C | 01 |
| 03 | Gate A contrast | A | 02 |
| 04 | Gate B diagnostics | B | 03 (A pass to interpret) |
| 05 | Gate S DKD specificity | S | 01 + A1 pass |
| 06 | Converge + Decide | — | 03–05 as applicable |

Templates: [`_template.md`](_template.md) or [`.seal/templates/unit.md`](../.seal/templates/unit.md). After a run, fill **Notes**. Operator does not edit sealed `PROTOCOL.md` confirmatory fields.

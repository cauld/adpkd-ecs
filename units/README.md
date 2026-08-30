# Units

A **unit** is BMAD’s story file without Agile: everything the Operator needs in one place. One unit, one run, one note.

Kill protocol is **draft**. Do not run Units 01–06 until Seal + OSF. Unit 00 is listed so the packet exists; it still waits on Seal (inventory without *CNR1* plots).

| ID | Title | Gate | Depends on |
|---|---|---|---|
| 00 | Data access inventory (both GEO) | — | After Seal |
| 01 | Freeze PT / failed-repair labels (both atlases) | — | 00 |
| 02 | *CNR1* detection (ADPKD) | C | 01 |
| 03 | Gate A contrast | A | 02 |
| 04 | Gate B diagnostics | B | 03 (A pass to interpret) |
| 05 | Gate S DKD specificity | S | 01 + A1 pass |
| 06 | Converge + Decide | — | 03–05 as applicable |

Templates: [`_template.md`](_template.md) or [`.seal/templates/unit.md`](../.seal/templates/unit.md). After a run, fill **Notes**. Operator does not edit sealed `PROTOCOL.md` confirmatory fields.

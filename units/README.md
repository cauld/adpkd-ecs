# Units

A **unit** is BMAD’s story file without Agile: everything the Operator needs in one place. One unit, one run, one note.

Kill protocol is **draft**. Do not run Units 01–05 until Seal + OSF. Unit 00 is listed so the packet exists; it still waits on Seal (inventory without *CNR1* plots).

| ID | Title | Gate | Depends on |
|---|---|---|---|
| 00 | Data access inventory | — | After Seal |
| 01 | Freeze PT / failed-repair labels | — | 00 |
| 02 | *CNR1* detection | C | 01 |
| 03 | Gate A contrast | A | 02 |
| 04 | Gate B diagnostics | B | 03 (A pass to interpret) |
| 05 | Converge + Decide | — | 03–04 |

Templates: [`_template.md`](_template.md) or [`.seal/templates/unit.md`](../.seal/templates/unit.md). After a run, fill **Notes**. Operator does not edit sealed `PROTOCOL.md` confirmatory fields.

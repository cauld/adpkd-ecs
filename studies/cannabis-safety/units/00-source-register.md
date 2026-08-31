---
id: 00
role: Operator
status: done
reads:
  - PROTOCOL.md
must_not:
  - Load GSE185948 or GSE195460 counts
  - Write DDI conclusions before Gates L/U
---

# Unit 00 — Source register

**Goal.** Pin URLs and human-dropped PDFs. No claims.

**Outputs.** `research/00-sources.md` (create `studies/cannabis-safety/research/` at run).

**Pass criteria.** DailyMed/FDA PI URLs for Jynarque and Epidiolex recorded. KDIGO PDF URL recorded. CT.gov query string copied from `PROTOCOL.md`.

OSF recorded 2026-08-30: https://osf.io/t6rzu/ . May run; still no GEO; no DDI conclusions in this unit.

## Notes (after run)

- Ran 2026-08-30 UTC. Artifact: [`research/00-sources.md`](../research/00-sources.md).
- DailyMed setids unchanged. Jynarque SPL v19 (`effectiveTime` 20251106); Epidiolex SPL v35 (`effectiveTime` 20260529).
- KDIGO official PDF retrieved (SHA-256 in the artifact). PP 7.3.4.1 / Table 19 locators recorded; wording not quoted.
- CT.gov query string copied; API not called (Unit 01).
- Human-dropped PDF inventory: empty.

---
id: 01
role: Operator
status: done
reads:
  - PROTOCOL.md
  - KILL.md
  - research/00-sources.md
must_not:
  - Load GSE185948 or GSE195460 counts
  - Rewrite query.cond or query.intr
  - Drop API hits silently
  - Mark Gate R (human)
  - Write DDI conclusions
---

# Unit 01 — ClinicalTrials.gov export (Gate R)

**Goal.** Run the frozen API query once. Record UTC date, `totalCount`, and every NCT. Classify include/exclude. No claims beyond the list.

**Inputs.** `PROTOCOL.md` CONFIRMATORY sources and ClinicalTrials.gov query. Query strings already copied in `research/00-sources.md`.

**Procedure.**

1. Run the registered dummy-JSON fixture (ADPKD+tolvaptan exclude; ADPKD+cannabidiol include).
2. `GET https://clinicaltrials.gov/api/v2/studies` with `countTotal=true` and the frozen `query.cond` / `query.intr`. Paginate until complete. Do not substitute a UI search.
3. Save the JSON export and SHA-256. Record UTC timestamp and `totalCount`.
4. For every returned study, classify include/exclude with a one-line reason under the PROTOCOL rule: ADPKD/PKD **condition** and cannabis/cannabinoid **intervention** (not eligibility-only).
5. Human marks Gate R in `KILL.md` / Decide later. Operator does not mark the gate.

**Outputs.** `research/01-ctgov.md` + JSON export under `data/raw/` (gitignored).

**Pass criteria.** `KILL.md` Gate R: query string, date, and either zero studies meeting the rule or a complete NCT list (no silent dropping). Human marks pass/fail.

## Notes (after run)

- Ran 2026-08-30T16:30:50Z. Artifact: [`research/01-ctgov.md`](../research/01-ctgov.md) + [`research/01-ctgov-export.json`](../research/01-ctgov-export.json).
- Fixture PASS (tolvaptan exclude; cannabidiol include; eligibility-only exclude).
- API HTTP 200, `totalCount` 0, NCT list empty. Verification re-GET 16:31:14Z also 0.
- Human has not marked Gate R.

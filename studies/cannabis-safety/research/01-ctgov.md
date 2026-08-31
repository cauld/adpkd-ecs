# Unit 01 — ClinicalTrials.gov export (Gate R)

**Run (confirmatory).** 2026-08-30T16:30:50Z  
**Verification re-GET.** 2026-08-30T16:31:14Z — `totalCount` 0, HTTP 200 (same frozen URL).  
**OSF.** https://osf.io/t6rzu/  
**Protocol freeze.** `db44b3086ae8c4d640dc40f44945bcef27ffe6bc`  
**Operator does not mark Gate R.** Human marks `KILL.md` Gate R.

**This unit does not claim** CBD–tolvaptan DDI class, label facts, taxonomy, or that cannabis is safe or effective in ADPKD. Empty registry search is an absence finding for **this frozen query**, not a proof that no unpublished trial exists (`PROTOCOL` / OSF item 16).

**Must not (held).** No GEO counts. Query strings not rewritten. No silent dropping (there were no rows to drop).

---

## Frozen query (character-for-character from PROTOCOL)

**Endpoint.** `GET https://clinicaltrials.gov/api/v2/studies`  
**`countTotal`.** `true`  
**`query.cond`.**

```
"polycystic kidney" OR ADPKD OR PKD1 OR PKD2
```

**`query.intr`.**

```
cannabis OR cannabidiol OR cannabinoid OR THC OR dronabinol OR nabiximols OR epidiolex
```

**Request URL (fetched):**

```
https://clinicaltrials.gov/api/v2/studies?format=json&countTotal=true&pageSize=1000&query.cond=%22polycystic+kidney%22+OR+ADPKD+OR+PKD1+OR+PKD2&query.intr=cannabis+OR+cannabidiol+OR+cannabinoid+OR+THC+OR+dronabinol+OR+nabiximols+OR+epidiolex
```

Matches Unit 00 copy and `PROTOCOL.md`.

---

## Fixture (before the live GET)

Script: `pipeline/ctgov_include.py --fixture` (uv Python 3.12). Seed `20260829` unused.

| Dummy NCT | Setup | Registered expectation | Result |
|---|---|---|---|
| NCT00000001 | ADPKD + tolvaptan intervention | exclude | exclude |
| NCT00000002 | ADPKD + cannabidiol intervention | include | include |
| NCT00000003 | ADPKD + tolvaptan; cannabis only in eligibility | exclude | exclude |

**FIXTURE PASS.**

---

## Live export

| Field | Value |
|---|---|
| HTTP | 200 |
| Pages | 1 (`nextPageToken` absent) |
| `totalCount` | **0** |
| Studies downloaded | **0** (equals `totalCount`) |
| Classified include | 0 |
| Classified exclude | 0 |
| NCT IDs | *(none — empty list)* |

JSON export (also gitignored raw copy): [`01-ctgov-export.json`](01-ctgov-export.json)

| File | SHA-256 |
|---|---|
| `data/raw/ctgov-unit01.json` | `e38953376fc79ec83a161ae952e475945fc524180f945f64a3ed61d7acd1acf9` |
| `data/raw/ctgov-unit01-classified.json` (`[]`) | `37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570` |

**NCT list (complete):** no identifiers to list. Nothing omitted.

**Include/exclude table:** no API rows. The rule was applied to fixtures only.

---

## Decision rule (as written; not re-decided after seeing 0)

A hit counts if the study lists an ADPKD/PKD **condition** and a cannabis/cannabinoid **intervention** (not eligibility prose alone). With `totalCount` 0, zero studies meet that rule.

**Gate R (human).** Pass if this file records the query, the UTC date, and zero matching studies (or a complete NCT list). Fail if the query was not frozen or hits were omitted. Operator assessment: query frozen; date recorded; NCT list empty because the API returned none. **Human marked Gate R pass** (chat 2026-08-30). Do not treat a Specify-era search as this export.

---

## Not this unit

- Label extraction (Unit 02 / Gate L)
- Taxonomy / KDIGO quotes (Unit 03 / Gate T)
- CBD–tolvaptan DDI class (Unit 04 / Gate U)

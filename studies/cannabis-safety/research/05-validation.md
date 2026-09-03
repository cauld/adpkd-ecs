# Validation (study 2) — 2026-08-31

**Not a new confirmatory unit.** Re-run and audit of Units 00–04 against `PROTOCOL.md` / `KILL.md`. No GEO.

## Fresh re-runs (read the output)

| Check | Output |
|---|---|
| `pipeline/ctgov_include.py --fixture` | FIXTURE PASS (tolvaptan exclude; cannabidiol include; eligibility-only exclude) |
| Frozen CT.gov GET 2026-08-31T18:24:25Z | HTTP 200, `totalCount` **0**, 0 studies (same as Unit 01 2026-08-30T16:30:50Z) |
| SHA-256 of all `data/raw/` files in `CHECKSUMS.txt` | all PASS |
| Query strings in 00 / 01 / export vs PROTOCOL | character match |
| Jynarque / Epidiolex setids vs PROTOCOL | match |
| Pair-name search in SPL XML | epidiolex not in Jynarque; tolvaptan not in Epidiolex |
| Label quotes in `02-labels.md` | present in SPL XML (CYP3A exclusive metabolism; strong-inhibitor CI; boxed liver + REMS; midazolam no change; everolimus ~2.5×) |
| Phrase `sensitive CYP3A` on Jynarque SPL | **absent** (CLAIMS ceiling corrected 2026-08-31) |
| KDIGO PP 7.3.4.1 / Table 19 “Not recommended” in `03-taxonomy.md` | present vs official PDF |

## PROTOCOL vs seal SHA `db44b30`

`KILL.md`, `CLAIMS.md` (until 2026-08-31 ceiling edit), `QUESTION.md`: no CONFIRMATORY-section drift at seal. `PROTOCOL.md` header only: DRAFT → GIT-SEALED + OSF URL (not a query/rule change).

## Papers

No paywalled PDFs required for v1. See `04-ddi.md` exploratory block. Human e-library drop not needed for the five Gateways PMIDs.

Operator vs human gates: R pass (2026-08-30). L/T/U pass and Decide complete v1 (2026-08-31). See [`DECIDE.md`](../DECIDE.md).

Red-team (2026-08-31): Gate R zero is not pair-PK evidence; CLAIMS “sensitive CYP3A” was not on the Jynarque SPL. Follow-up: `04-ddi.md` table rewritten; `CLAIMS.md` ceiling already amended; empty-trial and CB1-class language scoped; KDIGO p.164 re-extracted (`Cannabis Not recommended`; PP 7.3.4.1 present). ICTRP not added as confirmatory (would be a Gate R deviation).

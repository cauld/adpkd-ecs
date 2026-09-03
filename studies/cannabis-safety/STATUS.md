# STATUS

**Study:** ADPKD-ECS study 2 (cannabis / CBD / CB1-drug evidence map)  
**Program:** repo root [`README.md`](../../README.md)  
**Protocol seal:** GIT-SEALED 2026-08-30 — OSF recorded  
**Confirmatory git SHA:** `db44b3086ae8c4d640dc40f44945bcef27ffe6bc`  
**CLAIMS ceiling:** amended 2026-08-31 (label wording; Unit 00 does not classify the pair). CONFIRMATORY query/rules unchanged.  
**OSF URL:** https://osf.io/t6rzu/ ([overview](https://osf.io/t6rzu/overview))  
**Current stage:** After Decide. v1 map complete. Scribe written: [`REPORT.md`](REPORT.md) (≤ [`CLAIMS.md`](CLAIMS.md)). Leftovers in [`EXPLORE.md`](EXPLORE.md).  
**Decision:** complete v1 map (T+R+L+U pass). Recorded in [`DECIDE.md`](DECIDE.md).  
**Must not:** load study 1 GEO counts; write *CNR1* claims; rewrite unstudied DDI as safe or contraindicated  
**Superpowers:** Framing approved. Survey and plan frozen with protocol. OSF recorded. Units 00–04 ran 2026-08-30. Gates R 2026-08-30; L/T/U and Decide 2026-08-31.

## Ledger

| Date | Event |
|---|---|
| 2026-08-30 | Study directory opened as sibling seal to atlas kill |
| 2026-08-30 | Human approved framing. Survey + plan. Clarify 1–5. Analyze. No GEO. |
| 2026-08-30 | Human **Seal**. Git freeze SHA `db44b3086ae8c4d640dc40f44945bcef27ffe6bc`. OSF still open. |
| 2026-08-30 | Human recorded study 2 OSF URL https://osf.io/t6rzu/ . Unit 00 unblocked. |
| 2026-08-30 | Unit 00 source register written (`research/00-sources.md`). No DDI conclusions. Gate R not run. |
| 2026-08-30 | Unit 01 CT.gov export (`research/01-ctgov.md`). Frozen query, 2026-08-30T16:30:50Z, `totalCount` 0. |
| 2026-08-30 | Human marked Gate R **pass** (chat: update accordingly). Empty frozen query + complete NCT list (none). |
| 2026-08-30 | Units 02–04 written (`02-labels.md`, `03-taxonomy.md`, `04-ddi.md`). Pair class **unstudied**. L/T/U/Decide not human-marked. |
| 2026-08-31 | Validation re-GET frozen CT.gov still `totalCount` 0. Exploratory pair-PK look (not Gate R): no dedicated CBD–tolvaptan study; five PubMed hits are Gateways indexes — do not fetch. `CLAIMS.md` item 3: drop “sensitive CYP3A substrate” (not on Jynarque SPL); item 5: pair class is Units 01–04, not Unit 00. `research/05-validation.md`. |
| 2026-08-31 | Red-team follow-up: `04-ddi.md` no longer uses Gate R as pair-PK evidence; `unstudied` stated as default. Taxonomy/CT.gov wording scoped. OSF paste at `db44b30` may still contain the old CLAIMS sentence; scribe follows amended git `CLAIMS.md`. |
| 2026-08-31 | Human applied gate recommendations (chat). **L pass.** **T pass** (four headings, not a full CB1/OTC census). **U pass** (pair unstudied). **Decide: complete v1 map.** Paywalled PDFs not needed. |
| 2026-08-31 | OSF CLAIMS-amendment comment posted on https://osf.io/t6rzu/ (comment `yk2xgmj9tpd3`, 2026-08-31T19:26:50Z). Not a re-registration. Scribe follows git `CLAIMS.md`. |
| 2026-09-03 | Scribe write-up [`REPORT.md`](REPORT.md). Confirmatory vs exploratory separated. No query expansion. |

## Blockers before confirmatory execution

- [x] Framing (`QUESTION.md`) approved in chat 2026-08-30
- [x] Clarify recorded in `PROTOCOL.md`
- [x] Analyze recorded below
- [x] Human Seal (chat 2026-08-30)
- [x] Seal date + confirmatory git SHA
- [x] OSF prereg URL (https://osf.io/t6rzu/)

## Analyze

**Ran 2026-08-30 (read-only).** Isolation from study 1 holds. Gate R is Unit 01, not a Specify-era API ping.

## OSF (human)

Separate registration from study 1 (https://osf.io/7g3tn/). Literature / secondary sources. Map this folder’s `QUESTION.md`, `KILL.md`, `CLAIMS.md`, `PROTOCOL.md`. Disclose DailyMed, ClinicalTrials.gov, and KDIGO 2025 as sources; git SHA `db44b3086ae8c4d640dc40f44945bcef27ffe6bc`.

Recorded: https://osf.io/t6rzu/ ([overview](https://osf.io/t6rzu/overview)). OSF API `/v2/registrations/t6rzu/` returned 401 at record time (private or embargoed is fine). Units 00–04 may run as confirmatory. Do not load GEO. Gate R is Unit 01.

CLAIMS amendment comment posted 2026-08-31T19:26:50Z on https://osf.io/t6rzu/ (id `yk2xgmj9tpd3`). **Not a re-registration.** Text in [`docs/osf/study2-osf-comment-2026-08-31-claims-amendment.txt`](../../docs/osf/study2-osf-comment-2026-08-31-claims-amendment.txt). Scribe follows git `CLAIMS.md`.

## Human remaining

- [x] OSF submit + URL in this file
- [x] Unit 00 source register (no DDI conclusions)
- [x] Unit 01 ClinicalTrials.gov export (operator; `totalCount` 0)
- [x] Human marks Gate R (pass, chat 2026-08-30)
- [x] Unit 02 label extraction (operator)
- [x] Unit 03 taxonomy + KDIGO (operator)
- [x] Unit 04 DDI class **unstudied** (operator)
- [x] Human marks Gate L (pass, 2026-08-31)
- [x] Human marks Gate T (pass, scoped, 2026-08-31)
- [x] Human marks Gate U (pass) and Decide (complete v1, 2026-08-31)
- [x] Paywalled PDFs — none required for v1
- [x] OSF comment on CLAIMS amendment (posted 2026-08-31; comment `yk2xgmj9tpd3` on https://osf.io/t6rzu/)
- [x] Scribe ≤ `CLAIMS.md` ([`REPORT.md`](REPORT.md), 2026-09-03)

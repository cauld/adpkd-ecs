# STATUS

**Study:** ADPKD-ECS study 1 (atlas kill)  
**Program:** cannabis / ECS × ADPKD — see [`README.md`](README.md)  
**Flow:** [`.seal/E2E_FLOW.md`](.seal/E2E_FLOW.md) (generic) · [`E2E_FLOW.md`](E2E_FLOW.md) (this study)  
**Protocol seal:** GIT-SEALED 2026-08-30 — OSF recorded  
**Confirmatory git SHA:** `db44b3086ae8c4d640dc40f44945bcef27ffe6bc`  
**OSF URL:** https://osf.io/7g3tn/ ([overview](https://osf.io/7g3tn/overview))  
**Current stage:** Unit 01 freeze in git (`research/01-frozen-labels.md`). Next: Unit 02 Gate C.  
**Decision:** none yet  
**Superpowers:** Framing approved. Survey and plan frozen with protocol. Study 1 OSF URL recorded 2026-08-30.  
**Sibling:** [`studies/cannabis-safety/`](studies/cannabis-safety/)

## Ledger

| Date | Event |
|---|---|
| 2026-08-29 | Study directory opened (SEAL kernel copied from SCENDO `.seal/`) |
| 2026-08-29 | Source briefing archived under `docs/briefing/` |
| 2026-08-29 | v1 scoped to Pathway A (GSE185948 *CNR1* localization). B–D parked in `EXPLORE.md` |
| 2026-08-30 | Human chose program: study 1 + study 2; study 3 after Decide. Gate S added. `studies/cannabis-safety/` opened. |
| 2026-08-30 | Human approved framings. Prior-work survey + analysis plan. Clarify 1–5. Analyze. **No count matrices loaded.** |
| 2026-08-30 | Human **Seal**. Git freeze SHA `db44b3086ae8c4d640dc40f44945bcef27ffe6bc`. OSF still open. |
| 2026-08-30 | Human recorded study 1 OSF URL https://osf.io/7g3tn/ . Unit 00 unblocked. |
| 2026-08-30 | Unit 00 inventory. A1 lock (8 vs 5). S eligible (6 vs 5 libraries). No *CNR1* plots. |
| 2026-08-30 | Unit 01 freeze both atlases (`research/01-frozen-labels.md`). No *CNR1* DE. Laptop RAM sufficient; Spark not used. |

## Confirmatory vs exploratory

Git-sealed: do **not** edit CONFIRMATORY fields in `PROTOCOL.md` / `KILL.md` / `CLAIMS.md` except by dated amendment.  
OSF URL is recorded. Unit 00–01 complete. Unit 01 freeze is in git. Unit 02 may run Gate C. Study 2 OSF is separate: https://osf.io/t6rzu/ .

## Blockers before confirmatory execution

- [x] Framing (`QUESTION.md`) approved in chat 2026-08-30
- [x] Human Seal (chat 2026-08-30)
- [x] Clarify (five gaps) recorded in `PROTOCOL.md`
- [x] Analyze pass recorded below
- [x] Seal date + confirmatory git SHA (`db44b30`)
- [x] OSF secondary-data prereg URL (https://osf.io/7g3tn/)

## Analyze

**Ran 2026-08-30 (read-only, no outcomes).** See prior table. Verdict stood; human Sealed.

## OSF (human)

Create a project; choose **OSF Preregistration** → **Secondary Data**. Map `QUESTION.md`, `KILL.md`, `CLAIMS.md`, `PROTOCOL.md`. Disclose:

- Datasets GSE185948 and GSE195460 are public GEO.
- The protocol was specified with knowledge of those accessions and of Hinden et al. 2026’s published claims.
- Confirmatory *CNR1*-vs-cell-type / *CNR1*-vs-disease plots were **not** used to choose the model.
- Git SHA `db44b3086ae8c4d640dc40f44945bcef27ffe6bc`.

Recorded: https://osf.io/7g3tn/ ([overview](https://osf.io/7g3tn/overview)). OSF API `/v2/registrations/7g3tn/` returned 401 at record time (private or embargoed is fine; do not treat a sibling project as this lock).

## Human remaining

- [x] OSF submit + URL in this file
- [x] Unit 00 inventory (both GEO); still no *CNR1* plots
- [x] Unit 01 freeze PT labels both atlases
- [ ] Unit 02 Gate C
- [ ] Do not start docking / study 3 until study 1 Decide
- [x] Study 2 OSF (separate registration): https://osf.io/t6rzu/

# STATUS

**Study:** ADPKD-ECS study 1 (atlas kill)  
**Program:** cannabis / ECS × ADPKD — see [`README.md`](README.md)  
**Flow:** [`.seal/E2E_FLOW.md`](.seal/E2E_FLOW.md) (generic) · [`E2E_FLOW.md`](E2E_FLOW.md) (this study)  
**Protocol seal:** GIT-SEALED 2026-08-30 — **OSF not submitted**  
**Confirmatory git SHA:** `db44b3086ae8c4d640dc40f44945bcef27ffe6bc`  
**OSF URL:** none  
**Current stage:** Seal (git). Blocked on OSF before Unit 00 / count load.  
**Decision:** none yet  
**Superpowers:** Framing approved. Survey and plan frozen with protocol. Prereg incomplete until OSF submit.  
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

## Confirmatory vs exploratory

Git-sealed: do **not** edit CONFIRMATORY fields in `PROTOCOL.md` / `KILL.md` / `CLAIMS.md` except by dated amendment.  
Until **OSF URL** is recorded here: do not download count matrices, do not plot *CNR1* vs cell type or disease, do not run Units 01–06. Unit 00 waits on OSF (same rule as `AGENTS.md`).

## Blockers before confirmatory execution

- [x] Framing (`QUESTION.md`) approved in chat 2026-08-30
- [x] Human Seal (chat 2026-08-30)
- [x] Clarify (five gaps) recorded in `PROTOCOL.md`
- [x] Analyze pass recorded below
- [x] Seal date + confirmatory git SHA (`db44b30`)
- [ ] OSF secondary-data prereg URL

## Analyze

**Ran 2026-08-30 (read-only, no outcomes).** See prior table. Verdict stood; human Sealed.

## OSF (human)

Create a project; choose **OSF Preregistration** → **Secondary Data**. Map `QUESTION.md`, `KILL.md`, `CLAIMS.md`, `PROTOCOL.md`. Disclose:

- Datasets GSE185948 and GSE195460 are public GEO.
- The protocol was specified with knowledge of those accessions and of Hinden et al. 2026’s published claims.
- Confirmatory *CNR1*-vs-cell-type / *CNR1*-vs-disease plots were **not** used to choose the model.
- Git SHA `db44b3086ae8c4d640dc40f44945bcef27ffe6bc`.

Paste the registration URL into **OSF URL** above, then Unit 00 may run.

## Human remaining

- [ ] OSF submit + URL in this file
- [ ] Do not start docking / study 3 until study 1 Decide

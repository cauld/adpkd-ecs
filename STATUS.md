# STATUS

**Study:** ADPKD-ECS study 1 (atlas kill)  
**Program:** cannabis / ECS × ADPKD — see [`README.md`](README.md)  
**Flow:** [`.seal/E2E_FLOW.md`](.seal/E2E_FLOW.md) (generic) · [`E2E_FLOW.md`](E2E_FLOW.md) (this study)  
**Protocol seal:** DRAFT — not sealed  
**Confirmatory git SHA:** none  
**OSF URL:** none  
**Current stage:** Plan (Clarify + Analyze recorded). Next: human Seal + OSF.  
**Decision:** none yet  
**Superpowers:** Framing approved 2026-08-30. Survey [`docs/science-superpowers/surveys/2026-08-30-study1-cnr1-atlas.md`](docs/science-superpowers/surveys/2026-08-30-study1-cnr1-atlas.md). Plan [`docs/science-superpowers/plans/2026-08-30-study1-cnr1-atlas.md`](docs/science-superpowers/plans/2026-08-30-study1-cnr1-atlas.md). Prereg = Seal/OSF (human).  
**Sibling:** [`studies/cannabis-safety/`](studies/cannabis-safety/)

## Ledger

| Date | Event |
|---|---|
| 2026-08-29 | Study directory opened (SEAL kernel copied from SCENDO `.seal/`) |
| 2026-08-29 | Source briefing archived under `docs/briefing/` |
| 2026-08-29 | v1 scoped to Pathway A (GSE185948 *CNR1* localization). B–D parked in `EXPLORE.md` |
| 2026-08-30 | Human chose program: study 1 + study 2; study 3 after Decide. Gate S added. `studies/cannabis-safety/` opened. |
| 2026-08-30 | Human approved framings. Prior-work survey + analysis plan. Clarify 1–5 in `PROTOCOL.md`. Analyze (below). **No count matrices loaded.** |

## Confirmatory vs exploratory

Until seal: planning is exploratory. Do not load count matrices to choose models.  
After seal: Operator runs units; new ideas → `EXPLORE.md` or a dated protocol amendment. **Do not edit CONFIRMATORY fields** in `PROTOCOL.md` / `KILL.md` / `CLAIMS.md` except by dated amendment.

## Blockers before Seal

- [x] Framing (`QUESTION.md`) approved in chat 2026-08-30
- [ ] Human skims Clarify 1–5 in `PROTOCOL.md` / Gate S in `KILL.md` and agrees to Seal
- [x] Clarify (five gaps) recorded in `PROTOCOL.md`
- [x] Analyze pass recorded below
- [ ] Seal date + git SHA
- [ ] OSF secondary-data prereg URL (submit starts confirmatory execution)

## Analyze

**Ran 2026-08-30 (read-only, no outcomes).**

| Check | Result |
|---|---|
| One question vs two studies | Root SEAL = atlas only; cannabis map = `studies/cannabis-safety/`. Claims files cross-forbid. |
| QUESTION vs KILL vs CLAIMS | A1/A2/C/B/S present in all three. S cannot pass A. A2 cannot claim induction. Fail ≠ absence added to CLAIMS. |
| PROTOCOL vs KILL estimators | Welch t + CI; Wilcoxon only if n<3; freeze both atlases before *CNR1*. |
| DKD files | Clarify 1: GSE195460 RNA h5, not GSE131882 zUMIs. Matches survey. |
| Units 00–06 vs PHASES / E2E_FLOW | Same order; 05 = S; 06 = Decide. |
| PLAN.md vs PROTOCOL | PLAN restates; PROTOCOL wins. DKD is Gate S, not “bless docking.” |
| Superpowers plan vs PROTOCOL | Plan defers to PROTOCOL; sim check after Seal; no extra pass metric. |
| Study 2 leakage | No GEO in study 2 PROTOCOL. No DDI in study 1 Decide unit. |
| Open gaps (accepted) | Exact metadata **values** wait Unit 00 after Seal. Control tissue type (cortex vs medulla) not adjustable. n underpowered for modest effects. |

**Analyze verdict:** Artifacts consistent enough to Seal **if** the human accepts Clarify 1–5. Not sealed.

## Human remaining (not agent-clickable)

- [ ] Seal + OSF **per study** when ready (git commit of SEAL files, SHA in this STATUS, OSF secondary-data prereg disclosing the datasets are public and that *CNR1* plots were not used to choose the model)
- [ ] Do not start docking / study 3 until study 1 Decide

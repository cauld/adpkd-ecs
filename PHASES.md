# PHASES

Generic loop: [`.seal/E2E_FLOW.md`](.seal/E2E_FLOW.md). Study instantiation: [`E2E_FLOW.md`](E2E_FLOW.md). This file is the checklist.

## Phase 0 — Spec (in progress)

| Step | Workflow | Output |
|---|---|---|
| 0.1 | Question | `QUESTION.md`, `CLAIMS.md` — **draft 2026-08-29** |
| 0.2 | Kill | `KILL.md` — **draft** |
| 0.3 | Protocol | `PROTOCOL.md` — **draft** |
| 0.4 | Clarify | Not run |
| 0.5 | Analyze | Not run |
| 0.6 | **Seal** (human) | git SHA + OSF — **not done** |

**Exit:** Kill protocol sealed. Agent will not edit CONFIRMATORY sections.

## Phase 1 — Kill test (after Seal)

Units in `units/` (Operator). Order is dependency order.

0. Inventory (reachability, metadata columns, sample n) — **after Seal**, no *CNR1* plots  
1. Freeze PT / failed-repair labels  
2. Gate C detection  
3. Gate A (*CNR1*)  
4. Gate B diagnostics  
5. Converge + Decide  

**Exit:** human Decide per `KILL.md`.

## Phase 2 — After Decide

Stop / map-only / induction path — as in `KILL.md`. Pathways B–D need a **new** sealed protocol (`EXPLORE.md`).

## Deferred (not this study)

Docking, dual ligands, ADMET, MQ1, GSE7869 primary, GSE195460 DKD, wet lab, clinical guidelines.

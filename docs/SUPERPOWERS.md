# Science Superpowers × SEAL

SEAL is the **contract** (what is frozen, who marks the gate, what may be claimed). Science Superpowers is the **agent methodology** (frame, survey, design, prereg, execute, anomaly, verify, red-team).

The plugin lives at `~/.cursor/plugins/local/science-superpowers` (K-Dense-AI). It is not a Python dependency of this repo and not a git submodule. ecs-lab Scout chats ignore it; **this study follows it**.

## Mapping

| SEAL stage | Superpowers skill | This study |
|---|---|---|
| Explore / Question | `framing-research-questions` | Study 1: [`QUESTION.md`](../QUESTION.md). Study 2: [`studies/cannabis-safety/QUESTION.md`](../studies/cannabis-safety/QUESTION.md). Copies in [`docs/science-superpowers/questions/`](science-superpowers/questions/) |
| Analyst notes | `surveying-prior-work` | After the human approves the framing. Notes in `research/`. Briefing is prior context, not a survey. |
| Protocol | `designing-the-analysis` | [`PROTOCOL.md`](../PROTOCOL.md), [`PLAN.md`](../PLAN.md) |
| Seal | `preregistering-analysis` | Git SHA in `STATUS.md` + OSF secondary-data prereg. SEAL adds human Seal and a claims ceiling. |
| Before Unit 00 | `setting-up-reproducible-analysis` | Pinned uv env, seed `20260829`, `data/raw/` immutable |
| Run | `executing-analysis` or `subagent-driven-analysis` | One `units/*.md` at a time |
| Surprise | `investigating-anomalous-results` | Before patching the protocol |
| Before a claim | `verifying-results-before-claiming` | Re-run; read the output |
| Before Decide / Scribe | `requesting-red-team-review` | Adversarial pass vs `KILL.md` |
| After Decide | `reporting-and-archiving-findings` | Scribe ≤ `CLAIMS.md`; leftovers → `EXPLORE.md` |

## Rules of composition

1. **Skills say HOW. Sealed files say WHAT.** After Seal, do not edit CONFIRMATORY fields because a skill suggested a nicer test.
2. **Human gates stay human.** Superpowers does not mark Gate A/B/C/S or Decide.
3. **Named confound is required** even if a skill’s template omits it. Write it in `KILL.md`.
4. **Feasibility mode** is opt-in only (human). GSE185948 RNA counts are ~1.8 GB compressed. If laptop RAM is unknown, offer feasibility; do not enter it unasked. Nothing from feasibility is confirmatory.
5. **Do not install Superpowers inside this git tree.** User plugin only, same as ecs-lab’s Runner decision.

## Until Seal

Allowed: framing, literature notes, protocol text, Unit packets, GEO **landing-page** reachability (filenames, sizes, license). Forbidden: loading count matrices, plotting *CNR1*, clustering to peek the answer, docking, CYP models.

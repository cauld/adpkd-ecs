# ADPKD-ECS

Public-data program on the **endocannabinoid system and cannabis-related questions in autosomal dominant polycystic kidney disease**. No wet lab.

This git tree is the **program**. Each confirmatory question is its own seal.

| Study | Question (one line) | Status |
|---|---|---|
| **1 — Atlas kill** (this directory’s root SEAL files) | Frozen *CNR1* in ADPKD PT (GSE185948) + DKD specificity (GSE195460) | GIT-SEALED; [OSF](https://osf.io/7g3tn/) |
| **2 — Safety map** | [`studies/cannabis-safety/`](studies/cannabis-safety/) — plant vs CBD vs synthetics vs CB1 drugs; Jynarque / Epidiolex | GIT-SEALED; [OSF](https://osf.io/t6rzu/) |
| **3 — Chemistry** | Docking / ADMET | Parked in [`EXPLORE.md`](EXPLORE.md) until study 1 Decide |

| Read first | What it is |
|---|---|
| [`QUESTION.md`](QUESTION.md) | Study 1 one sentence |
| [`KILL.md`](KILL.md) | Named confounds + pass/fail (study 1) |
| [`CLAIMS.md`](CLAIMS.md) | What study 1 may / may not say |
| [`PROTOCOL.md`](PROTOCOL.md) | Study 1 confirmatory fields (git-sealed; [OSF](https://osf.io/7g3tn/)) |
| [`STATUS.md`](STATUS.md) | You are here (study 1) |
| [`docs/briefing/cannabinoid-adpkd-pathways.md`](docs/briefing/cannabinoid-adpkd-pathways.md) | Source briefing (not a protocol) |
| [`docs/SUPERPOWERS.md`](docs/SUPERPOWERS.md) | How Science Superpowers maps onto SEAL |
| [`EXPLORE.md`](EXPLORE.md) | Parked work including study 3 |

**Protocol seal (study 1):** GIT-SEALED 2026-08-30 (`db44b30`). OSF: https://osf.io/7g3tn/ . Unit 01 freeze is in `research/01-frozen-labels.md`. Next: Unit 02 Gate C.

Study text is [CC BY 4.0](LICENSE). Third-party datasets stay under their original licenses.

## Setup

Python **3.12** and [uv](https://docs.astral.sh/uv/):

```bash
uv sync
```

The `scrna` extra (scanpy) is for after study 1 Seal. Unit 00 is the first runner.

Process kernel: [`.seal/E2E_FLOW.md`](.seal/E2E_FLOW.md). This folder is study 1: [`E2E_FLOW.md`](E2E_FLOW.md).

## Chat shorthand

**Explore → Question → Kill → Protocol → Clarify → Analyze → Seal (OSF) → Unit → Run → Converge → Decide → Archive.**

Science Superpowers skills fire inside those stages ([`docs/SUPERPOWERS.md`](docs/SUPERPOWERS.md)). After Seal, say **Unit** then **Run**. Do not say Run on outcomes before Seal. Do not use study 1 *CNR1* results to write study 2 claims, or the reverse.

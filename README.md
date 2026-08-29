# ADPKD-ECS

Public-data computational study of the **endocannabinoid system in autosomal dominant polycystic kidney disease**. No wet lab. v1 is a **kill test**: is *CNR1* upregulation in public ADPKD snRNA-seq restricted to a frozen proximal-tubule / failed-repair state after a composition check?

This is a **SCENDO-shaped study**, not an ecs-lab harvest loop. The sibling lab (`../ecs-lab`) finds ideas. This folder answers one frozen question.

| Read first | What it is |
|---|---|
| [`QUESTION.md`](QUESTION.md) | One sentence |
| [`KILL.md`](KILL.md) | Named confound + pass/fail |
| [`CLAIMS.md`](CLAIMS.md) | What we may / may not say |
| [`PROTOCOL.md`](PROTOCOL.md) | Confirmatory fields (draft until Seal) |
| [`STATUS.md`](STATUS.md) | You are here |
| [`docs/briefing/cannabinoid-adpkd-pathways.md`](docs/briefing/cannabinoid-adpkd-pathways.md) | Source briefing (not the protocol) |
| [`docs/SUPERPOWERS.md`](docs/SUPERPOWERS.md) | How Science Superpowers maps onto SEAL |
| [`EXPLORE.md`](EXPLORE.md) | Pathways B–D and other non-confirmatory work |

**Protocol seal:** DRAFT. Do not download count matrices to choose the model. Do not plot *CNR1* vs cell type or disease until git seal + OSF submit.

Study text is [CC BY 4.0](LICENSE). Third-party datasets stay under their original licenses.

## Setup

Python **3.12** and [uv](https://docs.astral.sh/uv/):

```bash
uv sync
```

The `scrna` extra (scanpy) is for after Seal. Unit 00 is the first runner.

Process kernel: [`.seal/E2E_FLOW.md`](.seal/E2E_FLOW.md). This folder is the study instance: [`E2E_FLOW.md`](E2E_FLOW.md).

## Chat shorthand

**Explore → Question → Kill → Protocol → Clarify → Analyze → Seal (OSF) → Unit → Run → Converge → Decide → Archive.**

Science Superpowers skills fire inside those stages ([`docs/SUPERPOWERS.md`](docs/SUPERPOWERS.md)). After Seal, say **Unit** then **Run**. Do not say Run on outcomes before Seal.

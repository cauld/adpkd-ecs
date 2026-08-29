# KILL

**Purpose.** Stop or shrink the project before docking, dual-ligand design, ADMET, MQ1, or a therapeutic manuscript. Human-owned pass/fail.

**Named confound.** Two stacked alternatives, both of which would make a CB1-antagonist-for-ADPKD pitch premature:

1. **Composition.** ADPKD kidneys contain more injured / failed-repair proximal-tubule (PT) nuclei, so a whole-kidney *CNR1* mean rises without any per-cell change.
2. **Constitutive PT marker.** *CNR1* is higher in PT than in distal nephron in healthy kidney too, so an ADPKD-only PT vs other-epithelium contrast is not disease biology.

Unit 00 records whether GSE185948 includes non-ADPKD control kidneys. That decides which Gate A contrast is legal (`PROTOCOL.md`).

## Gate C — detectability

**Data:** GSE185948 snRNA counts + shipped metadata. No *CNR1*-driven cluster search.

**Pass if:** *CNR1* count > 0 in **≥ 1%** of nuclei in the frozen PT / failed-repair object **and** that object has **≥ 100** nuclei.

**Fail if:** Detection < 1% or n < 100. Stop or reframe as “ECS dark in this atlas.” **Do not run Gate A** as a localization or disease-induction claim.

**Not a kill:** Low *CNR1* in immune or distal clusters.

## Gate A — disease induction inside frozen PT (preferred) or localization (fallback)

**States** are frozen **without** *CNR1* in the assignment list.

### A1 (preferred, if Unit 00 finds ≥ 3 ADPKD and ≥ 3 control samples)

**Contrast:** Within the frozen PT / failed-repair object only, *CNR1* ADPKD vs control.

**Pass if:** Locked estimator 95% CI for ADPKD − control **excludes 0** and the ADPKD mean is **higher**. Sole confirmatory gene: *CNR1*.

**Fail:** CI includes 0, opposite direction, or *CNR1* was used to define PT.

### A2 (fallback, if controls are absent or n too small)

**Contrast:** Within ADPKD samples only, *CNR1* in frozen PT / failed-repair vs frozen other epithelium.

**Pass if:** Locked estimator 95% CI for PT − other epithelium **excludes 0** and PT is **higher**.

**Fail:** CI includes 0, opposite direction, or protocol breach.

**If A1 was eligible, A2 is descriptive only and cannot pass Gate A.**

**If A fail:** Do **not** run Gate B as a therapeutic-target confirmation. Optional atlas-only note if Gate C passed.

## Gate B — not composition / not a mixed bag

Run only if Gate A passed.

**B1 (always):** The Gate A table used the frozen PT object, not all nuclei. If the operator scored all cells, **fail** (protocol breach).

**B2 (if A1 ran):** Inside ADPKD PT, failed-repair vs non-injured PT (frozen labels or locked VCAM1/HAVCR1/PROM1 split). Report 95% CI. This **does not** reverse A1. If failed-repair is **lower** *CNR1* than non-injured PT, Scribe may not say “restricted to failed-repair”; A1 may still stand as PT disease induction.

**B3 (diagnostic, cannot pass A):** Sample-level epithelial mean *CNR1* ~ `p_PT` (fraction PT among epithelial nuclei). Expected if *CNR1* is PT-enriched; not a rescue.

## Decide (after gates)

| Result | Decision |
|---|---|
| C pass, A1 pass | v1 localization + disease-induction path. Pathways B–D stay parked until a **new** protocol |
| C pass, A2 pass (A1 ineligible) | Map-only: PT-enriched *CNR1* in ADPKD atlas; **do not** claim ADPKD-specific induction |
| C pass, A fail | Negative v1; do not claim CB1 as an ADPKD PT target from this atlas |
| C fail | Stop this accession; do not dock |
| Protocol breach (*CNR1* defined the state) | Not confirmatory |

## Explicitly not in the kill

Docking / THCV / JD5037 (Pathway B). Dual CB1/CB2 MD (Pathway C). CYP3A4, CBD–tolvaptan, MQ1 (Pathway D). GSE7869 as primary. GSE195460 DKD specificity. Ligand assays. Wet-lab *Pkd1* mice. Clinical advice.

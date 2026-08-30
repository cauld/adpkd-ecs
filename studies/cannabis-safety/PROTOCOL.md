# PROTOCOL (kill phase)

**Seal status:** GIT-SEALED 2026-08-30. Confirmatory content frozen at `db44b3086ae8c4d640dc40f44945bcef27ffe6bc`. After seal, do not edit sections marked CONFIRMATORY without a dated amendment in `STATUS.md`. OSF: https://osf.io/t6rzu/ (recorded in this study’s `STATUS.md` 2026-08-30).

This protocol is **study 2 only** (evidence map). Study 1: repo-root `PROTOCOL.md`. Do not load GSE185948 or GSE195460 counts.

Human-readable brief: [`PLAN.md`](PLAN.md). If PLAN and this file disagree, **this file wins**.

## CONFIRMATORY — sources (freeze at seal)

Allowed at run (open web + human-supplied PDFs):

- DailyMed / FDA prescribing information for **Jynarque** (tolvaptan) and **Epidiolex** (cannabidiol)
  - Jynarque setid `3febc0a1-9e5a-4ce0-843d-210f21d862c4` — https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=3febc0a1-9e5a-4ce0-843d-210f21d862c4
  - Epidiolex setid `8bf27097-4870-43fb-94f0-f3d0871d1eec` — https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=8bf27097-4870-43fb-94f0-f3d0871d1eec
  - If DailyMed revises the label, Unit 00 records the new revision date and still extracts the same fact types.
- ClinicalTrials.gov API v2: `GET https://clinicaltrials.gov/api/v2/studies` with `countTotal=true`
  - `query.cond` = `"polycystic kidney" OR ADPKD OR PKD1 OR PKD2`
  - `query.intr` = `cannabis OR cannabidiol OR cannabinoid OR THC OR dronabinol OR nabiximols OR epidiolex`
- KDIGO 2025 ADPKD guideline (official PDF): https://kdigo.org/wp-content/uploads/2025/01/KDIGO-2025-ADPKD-Guideline.pdf
  - Required excerpts: Practice Point **7.3.4.1**; **Table 19** cannabis row. Key-takeaways PDF may supplement, not replace, the full guideline.
- Peer-reviewed papers the Operator can access without a library **proxy crawl**; paywalled PDFs the **human** places in `studies/cannabis-safety/data/pdfs/` (gitignored if large)

Not confirmatory: ChEMBL IC50 models, docking, OpenFDA ROR, study 1 *CNR1* tables, ecs-lab Scout dumps.

## CONFIRMATORY — ClinicalTrials.gov query

Run once at Unit 01. Record UTC date.

Use the API parameters in **CONFIRMATORY — sources**. Record UTC date and `totalCount`.  
**Rule:** A hit counts if the study lists an ADPKD/PKD condition **and** a cannabis/cannabinoid **intervention** (not merely a mention in eligibility prose without intervention). Borderline hits: list and classify include/exclude with a one-line reason; do not drop silently.  
A pre-seal API ping is **not** Gate R.

## CONFIRMATORY — exposure taxonomy

Must appear as separate analytic classes (Gate T):

1. Plant *Cannabis sativa* (smoked/vaped/edible as reported in sources)
2. CBD (prescription Epidiolex vs non-prescription products when sources distinguish)
3. Synthetic cannabinoid receptor agonists (e.g. Spice/K2 / named SCB case series)
4. CB1-targeting **drugs** (rimonabant, monlunabant/INV-202, JD5037, AM6545, anti-CB1 mAbs as they appear in trials/labels)

## CONFIRMATORY — label facts to extract (not to invent)

From Jynarque label: CYP3A metabolism; strong/moderate inhibitor language; boxed hepatotoxicity / REMS if present.  
From Epidiolex label: midazolam / CYP3A4 probe statement; P-gp substrate examples (e.g. everolimus); hepatotoxicity warnings; renal-impairment language if present.  
**Pair:** whether either label names the other product.

## CONFIRMATORY — DDI classification (Gate U)

Allowed classes for CBD + tolvaptan:

- **Documented pair PK** — dedicated study of the two drugs
- **Labeled interaction** — one label names the other
- **Unstudied** — default if neither of the above
- **Analog only** — midazolam, everolimus, tacrolimus, grapefruit as **bounds**, not as the pair

`Unstudied` + analogs **must not** be rewritten as contraindicated or safe.

## CONFIRMATORY — statistics

None. This is a structured evidence map. No p-values. No FAERS ROR.

## CONFIRMATORY — pass/fail

See `KILL.md`. Human marks gates.

## How (operational)

- No `uv sync --group scrna` required.
- Human e-library PDFs: do not commit copyrighted full text if the license forbids it; cite and excerpt per fair use / journal rules.
- Do not use a university proxy to bulk-download publisher PDFs via the agent.

## Clarify (2026-08-30, before Seal)

1. DailyMed setids frozen as above; revision dates recorded at Unit 00.
2. ClinicalTrials.gov is API v2 `query.cond` + `query.intr`, not a free-text UI only.
3. KDIGO excerpts are PP 7.3.4.1 and Table 19 from the full guideline PDF.
4. Gate R is the Unit 01 export, not a Specify-era search.
5. Analog PK (midazolam, everolimus) stays Gate U **analog only**.

## Amendments

None after Seal.

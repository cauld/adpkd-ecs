# Prior-work survey — study 2 (cannabis / CBD / CB1-drug map)

**Date:** 2026-08-30  
**Question:** [`../questions/2026-08-30-cannabis-adpkd-safety.md`](../questions/2026-08-30-cannabis-adpkd-safety.md)  
**Constraint:** labels, KDIGO PDFs, ClinicalTrials.gov API. No GEO. Gate R is **not** passed by this survey.

## Relationship to prior work

Structured **uncertainty map**, not a new trial. KDIGO 2025 already counsels on cannabis (Practice Point 7.3.4.1; Table 19 “Not recommended”). No ADPKD cannabinoid RCT was identified in Specify-era search; Unit 01 must re-run the frozen API query. Hinden 2026 and Klawitter 2022 are **ECS biology**, not cannabis exposure — cite only as background, not as treatment evidence.

## Established methods

- PRISMA-style source register + frozen registry query (this protocol is a **map**, not a meta-analysis of effect sizes).
- DDI classification from **labels and pair-specific PK**, not from in vitro CYP stories (FDA probe-substrate logic).

## Confounds

1. Collapsed exposures (Gate T).  
2. Label laundering (Gate U / L).  
3. KDIGO AKI language refers to **contamination and synthetics**, not proven plant-cannabis CKD progression.

## Prior “effect size”

Not applicable. Empty trial search is an **absence** finding. Analog PK (midazolam null; everolimus ~2.5× on Epidiolex label) are **bounds**, not the pair.

## Identifiers to freeze (retrieved 2026-08-30; re-check at Unit 00 if DailyMed revises)

| Product | DailyMed setid | URL |
|---|---|---|
| Jynarque (tolvaptan) | `3febc0a1-9e5a-4ce0-843d-210f21d862c4` | https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=3febc0a1-9e5a-4ce0-843d-210f21d862c4 |
| Epidiolex (cannabidiol) | `8bf27097-4870-43fb-94f0-f3d0871d1eec` | https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=8bf27097-4870-43fb-94f0-f3d0871d1eec |

Epidiolex §12.3 CYP3A4 substrates (DailyMed, retrieval date above): coadministration of EPIDIOLEX 750 mg twice daily with midazolam 2.5 mg **did not result in changes in plasma concentrations of midazolam**. Jynarque label: no cannabis/CBD/Epidiolex string on that retrieval. Neither label named the other product.

KDIGO full PDF: https://kdigo.org/wp-content/uploads/2025/01/KDIGO-2025-ADPKD-Guideline.pdf  
Practice Point **7.3.4.1**; **Table 19** cannabis row.

ClinicalTrials.gov API v2: `https://clinicaltrials.gov/api/v2/studies` with `query.cond` and `query.intr` (OpenAPI: https://clinicaltrials.gov/api/oas/v2). A pre-seal **API ping is not Gate R**.

## Citations

KDIGO 2025 ADPKD guideline (kdigo.org PDFs above).  
DailyMed setids as table.  
ClinicalTrials.gov API docs: https://clinicaltrials.gov/data-api/about-api  

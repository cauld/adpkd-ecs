# Unit 03 — Exposure taxonomy and KDIGO excerpts (Gate T)

**Run.** 2026-08-30.  
**Sources.** Unit 01 CT.gov export (`totalCount` 0); Unit 02 labels; KDIGO 2025 full guideline PDF (Unit 00 URL and SHA-256 `302f80af1aa44377ad2f23b619933412ab3c306b6a00cc90bce7e1471839bc0c`).  
**Not this unit.** DDI class (Unit 04). GEO / *CNR1*. One pooled “cannabinoid” recommendation.

KDIGO page locators: PP 7.3.4.1 on PDF pp. **46** (summary list, journal S45) and **164** (chapter body, journal **S163**). Table 19 body on PDF p. **164** (journal **S163**). Text extracted with `pypdf` from that PDF.

---

## Four classes (required)

### (i) Plant *Cannabis sativa* (smoked / vaped / edible as reported)

KDIGO discusses “cannabis products” and Table 19 row **Cannabis**, not smoked vs edible vs vaped as separate rows. Unit 01: no CT.gov study with a cannabis/cannabinoid **intervention** and an ADPKD/PKD **condition**. This map keeps plant cannabis as its own class. It does not claim plant cannabis causes or slows ADPKD (`CLAIMS.md`).

### (ii) CBD (prescription Epidiolex vs non-prescription when sources distinguish)

**Prescription.** Epidiolex (cannabidiol) oral solution — DailyMed setid `8bf27097-4870-43fb-94f0-f3d0871d1eec` — indicated for seizures (LGS, Dravet, TSC), **not** ADPKD. Label facts: Unit 02.

**Non-prescription CBD.** KDIGO does not split OTC CBD from plant cannabis in Table 19 (single **Cannabis** row). This class stays separate from (i) and from (iv). No ADPKD CBD RCT in the Unit 01 export.

### (iii) Synthetic cannabinoid receptor agonists (e.g. Spice/K2 / named SCB case series)

KDIGO PP 7.3.4.1 names **synthetic versions** in the AKI-contamination counsel (quote below). Table 19 cannabis row does not list Spice/K2 by name. This class is not pooled with Epidiolex or with CB1 antagonist **drugs**.

### (iv) CB1-targeting drugs (antagonist / inverse agonist / antibody as labeled in sources)

PROTOCOL names rimonabant, monlunabant/INV-202, JD5037, AM6545, anti-CB1 mAbs as they appear in trials/labels. They are **not** Jynarque (tolvaptan is a V2 antagonist). They are **not** Epidiolex. Unit 01’s frozen query was cannabis/cannabinoid **interventions**, not a dedicated CB1-antagonist registry search; emptiness of that query is not an efficacy finding for this class. **Do not** write that CB1 antagonists treat ADPKD.

---

## KDIGO quotes (required excerpts)

**Practice Point 7.3.4.1** (PDF p. 164 / S163; also listed p. 46 / S45):

> All people with ADPKD should be asked about their use of cannabis products and should be counseled about potential dangers of AKI related to product contamination and synthetic versions.

**Table 19 cannabis row** (PDF p. 164 / S163; TOC: S163):

| Product | Recommendation | Supporting explanation |
|---|---|---|
| Cannabis | Not recommended | No evidence of clinical benefits of cannabis. Potential danger of AKI. |

Chapter narrative on the same page (not a substitute for the PP or the table row): “Currently, no evidence has been reported, beyond anecdotal case reports, of any clinical benefits of cannabis use.” “In absence of dedicated studies, we advise against the use of cannabis products to alleviate complications in people with ADPKD.” Case reports of synthetic cannabinoids and AKI are cited in that paragraph.

Key-takeaways PDF was not used (PROTOCOL: may supplement, not replace).

---

## Gate T checklist (operator; human marks pass/fail)

| Required | In this file |
|---|---|
| ≥ four rows/sections: plant cannabis; CBD (Rx vs OTC if sources allow); synthetics; CB1 drugs | Yes |
| Not one pooled cannabinoid recommendation | Yes |

**Human marks Gate T.**

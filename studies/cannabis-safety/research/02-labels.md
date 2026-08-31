# Unit 02 — Label extraction (Gate L)

**Run.** 2026-08-30. SPL XML retrieved same day as Unit 00 revision dates.  
**Sources (not the briefing).** DailyMed SPL XML, setids frozen in `PROTOCOL.md` / Unit 00.

| Product | Setid | SPL version | `effectiveTime` | XML SHA-256 |
|---|---|---|---|---|
| Jynarque (tolvaptan) | `3febc0a1-9e5a-4ce0-843d-210f21d862c4` | 19 | 20251106 | `d9f3be572bc80711f1aa542d399f6709645aa6a75f9eaf3133773d9e6dd5924d` |
| Epidiolex (cannabidiol) | `8bf27097-4870-43fb-94f0-f3d0871d1eec` | 35 | 20260529 | `24c34f8f442235eea558b28a56ddb16f04c52aa0615f793a89d1423483b5666a` |

HTML: https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=3febc0a1-9e5a-4ce0-843d-210f21d862c4  
https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=8bf27097-4870-43fb-94f0-f3d0871d1eec

**This unit does not classify** the CBD–tolvaptan pair (Unit 04). Quotes are from SPL text nodes. Ligature/whitespace normalized when the XML used non-breaking hyphens.

---

## Pair: does either label name the other product?

Case-insensitive search of each full SPL XML:

| Needle | In Jynarque SPL | In Epidiolex SPL |
|---|---|---|
| Epidiolex / epidiolex | 0 | (own name) |
| cannabidiol / cannabis / marijuana / nabiximols / dronabinol | 0 | (own class) |
| `CBD` | 0 | (own metabolite strings, e.g. 7-OH-CBD) |
| Jynarque / tolvaptan / Samsca | (own name) | 0 |
| ADPKD | (own indication) | 0 |

**Operator finding.** Neither label names the other product as a listed interaction. Jynarque does not name cannabis, cannabidiol, or Epidiolex. Epidiolex does not name Jynarque or tolvaptan.

---

## Jynarque — CYP3A, boxed liver, REMS, inhibitors

**Metabolism (12.3).** “Tolvaptan is metabolized almost exclusively by CYP3A.”

The exact phrase “sensitive CYP3A substrate” does **not** appear in this SPL (search `sensitive CYP3A`: 0 hits). Do not put that phrase in the scribe’s mouth as a **label quote**.

**Strong / moderate inhibitors (5.4).** “Concomitant use of JYNARQUE with drugs that are moderate or strong CYP3A inhibitors (e.g., ketoconazole, itraconazole, lopinavir/ritonavir, indinavir/ritonavir, ritonavir, and conivaptan) increases tolvaptan exposure. Use with strong CYP3A inhibitors is contraindicated; dose reduction of JYNARQUE is recommended for patients while taking moderate CYP3A inhibitors.”

**Contraindications (4).** “Taking strong CYP3A inhibitors” / “Concomitant use of strong CYP3A inhibitors is contraindicated.”

**Ketoconazole magnitude (7.1 / 12.3).** “Tolvaptan's AUC was 5.4 times as large and Cmax was 3.5 times as large after co-administration of tolvaptan and 200 mg ketoconazole.”

**Grapefruit (7.1).** “Patients should avoid grapefruit juice beverages while taking JYNARQUE.” (12.3: 60 mg tolvaptan with 240 mL grapefruit juice: Cmax +90%, AUC +60%.)

**Boxed warning (34066-1).** “JYNARQUE (tolvaptan) can cause serious and potentially fatal liver injury. Acute liver failure requiring liver transplantation has been reported.” Monitoring: ALT, AST, and bilirubin before initiation, at 2 and 4 weeks, monthly for 18 months, then every 3 months. “Because of the risks of serious liver injury, JYNARQUE is available only through a restricted distribution program under a Risk Evaluation and Mitigation Strategy (REMS) called the Tolvaptan for ADPKD Shared System REMS.”

**REMS (5.2).** Present as quoted above (prescriber/patient/pharmacy certification).

**Renal (8.7).** Efficacy studies included normal and reduced renal function (TEMPO 3:4 eCrCl ≥ 60 mL/min; REPRISE eGFR 25–65). Not a CBD statement.

---

## Epidiolex — midazolam, P-gp, hepatotoxicity, renal

**Midazolam / CYP3A4 probe (12.3).** “Coadministration of EPIDIOLEX (750 mg twice daily) with a single dose of midazolam (2.5 mg), a sensitive CYP3A4 substrate, did not result in changes in plasma concentrations of midazolam compared to midazolam administered alone.”

Section **7.2** lists CYP1A2, CYP2B6, CYP2C8, CYP2C19, UGT1A9, and orally administered P-gp substrates. It does **not** instruct a general dose reduction of CYP3A4 substrates.

**P-gp / everolimus (7.2).** “Concomitant use of EPIDIOLEX with orally administered everolimus results in an approximately 2.5-fold increase in plasma exposures of everolimus.” “Increases in exposure of other orally administered P-gp substrates (e.g., sirolimus, tacrolimus, digoxin) may be observed when concomitantly used with EPIDIOLEX.”

**Hepatotoxicity (5.1).** “EPIDIOLEX can cause dose-related elevations of liver transaminases (alanine aminotransferase [ALT] and/or aspartate aminotransferase [AST]).” Controlled-study ALT >3× ULN rates vs placebo are on the label; postmarketing cholestatic/mixed injury is described. This is **not** Jynarque’s boxed fatal-injury / REMS language.

**Renal-impairment language if present.** There is **no** “8.7 Use in Patients with Renal Impairment” section. Present instead: “EPIDIOLEX is excreted in feces, with minor renal clearance.” Also “Increases in Creatinine”: ~10% serum creatinine rise within 2 weeks; “the increases in serum creatinine noted with EPIDIOLEX are not due to a reduction in glomerular filtration rate.” Geriatric text mentions decreased hepatic, renal, or cardiac function as a general dosing caution.

---

## Gate L checklist (operator; human marks pass/fail)

| Required (`KILL.md`) | In this file |
|---|---|
| (a) whether each names the other drug | Neither names the other |
| (b) tolvaptan CYP3A / boxed liver as on the label | Quoted (CYP3A exclusive metabolism; strong-inhibitor contraindication; boxed liver + REMS) |
| (c) Epidiolex midazolam and P-gp as on the label | Quoted (midazolam no change; everolimus ~2.5×; other oral P-gp examples) |
| Labels opened (DailyMed setids) | Yes |
| Briefing not used as the label | Yes |

**Human marks Gate L.** Operator does not mark it.

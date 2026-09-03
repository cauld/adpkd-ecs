# Cannabis, CBD, and CB1-targeting drugs in ADPKD: a pre-specified uncertainty map (study 2)

**Scribe.** After human Decide 2026-08-31 (complete v1 map). Language does not exceed [`CLAIMS.md`](CLAIMS.md).  
**Not study 1.** No GEO counts. No *CNR1*.  
**Question.** Using FDA labels, trial registries, KDIGO, and published human evidence, what can be stated—and what must remain unknown—about cannabis, CBD, synthetic cannabinoids, and CB1-targeting drugs in people with ADPKD, including co-use with tolvaptan?

**Framing.** This is an **uncertainty map** with a claims ceiling, not a demonstration that cannabis is safe or effective in ADPKD, and not advice to start or stop cannabis, CBD, or THCV.

**Locks.** Protocol freeze git SHA `db44b3086ae8c4d640dc40f44945bcef27ffe6bc`. OSF: https://osf.io/t6rzu/ . CLAIMS ceiling amended 2026-08-31 (comment `yk2xgmj9tpd3`); confirmatory query strings and gate rules unchanged.

---

## Confirmatory

Human marks (2026-08-30 / 2026-08-31): Gates **R, L, T, U pass**. Decide: complete v1 map ([`DECIDE.md`](DECIDE.md)).

### 1. Frozen ClinicalTrials.gov query (Gate R)

`GET https://clinicaltrials.gov/api/v2/studies` with `countTotal=true`, 2026-08-30T16:30:50Z (HTTP 200). Re-GET 2026-08-31 still `totalCount` **0**.

- `query.cond` = `"polycystic kidney" OR ADPKD OR PKD1 OR PKD2`
- `query.intr` = `cannabis OR cannabidiol OR cannabinoid OR THC OR dronabinol OR nabiximols OR epidiolex`

No record matching this search treated cannabis, CBD, THC, or a named cannabinoid as an **intervention** in ADPKD/PKD. The NCT list is complete because it is empty. Dummy-JSON fixture (`pipeline/ctgov_include.py --fixture`) passed before the live GET.

This is **this query**, not a census of all registries, and not of tokens omitted from `query.intr` (marijuana, nabilone, Sativex, hemp, THCV). Emptiness is not proof that no unpublished trial exists, and is not proof that no healthy-volunteer pair-PK study exists (that design would not need an ADPKD condition).

### 2. KDIGO 2025 (quoted from the official guideline PDF)

SHA-256 `302f80af1aa44377ad2f23b619933412ab3c306b6a00cc90bce7e1471839bc0c`. Practice Point **7.3.4.1** and Table 19 cannabis row: PDF p. 164 / journal **S163**. Not from study 1.

> All people with ADPKD should be asked about their use of cannabis products and should be counseled about potential dangers of AKI related to product contamination and synthetic versions.

Table 19: **Cannabis / Not recommended** — “No evidence of clinical benefits of cannabis. Potential danger of AKI.”

### 3. Jynarque and Epidiolex labels (Gate L)

DailyMed setids frozen in the protocol. Jynarque SPL v19 (`effectiveTime` 20251106); Epidiolex SPL v35 (`effectiveTime` 20260529). Neither product names the other as a listed interaction.

**Jynarque (tolvaptan).** “Tolvaptan is metabolized almost exclusively by CYP3A.” Strong CYP3A inhibitors are contraindicated. Boxed warning: serious and potentially fatal liver injury; available only through the Tolvaptan for ADPKD Shared System REMS. The phrase **“sensitive CYP3A substrate” is not on this SPL** and is not a label quote.

**Epidiolex (cannabidiol).** Midazolam 2.5 mg with 750 mg BID “did not result in changes in plasma concentrations of midazolam.” Oral everolimus ~2.5-fold; other oral P-gp examples include tacrolimus. Dose-related transaminase elevations are labeled. This is not Jynarque’s boxed fatal-injury / REMS language.

### 4. Four exposure classes kept separate (Gate T)

Reported as separate headings, not one pooled “cannabinoid” recommendation:

1. Plant *Cannabis sativa*
2. CBD (prescription Epidiolex vs non-prescription when sources distinguish)
3. Synthetic cannabinoid receptor agonists
4. CB1-targeting **drugs** (antagonist / inverse agonist / antibody as labeled in sources)

Gate T is four headings. It is not a completed CB1-drug or OTC-CBD literature census. KDIGO Table 19 has a single **Cannabis** row and does not split OTC CBD. Do not write that CB1 antagonists treat ADPKD.

### 5. CBD–tolvaptan pair class (Gate U)

**Unstudied** (protocol default): no cited dedicated pair PK/DDI study, and no labeled named interaction. Unit 00 is a source register only and does not classify the pair.

Analog bounds stay analog only and do **not** convert the pair to contraindicated or safe:

- Epidiolex + midazolam: no change in midazolam levels (not a CBD–tolvaptan study; not proof the pair is safe)
- Epidiolex + oral everolimus: ~2.5-fold (not tolvaptan)
- Tacrolimus: labeled as an example oral P-gp substrate that may have increased exposure (not pair PK)
- Grapefruit juice with Jynarque: labeled Cmax +90%, AUC +60% (not a CBD product)

---

## We do not claim

- Patients should start or stop cannabis, CBD, or THCV for ADPKD or for pain.
- CBD **is contraindicated** with tolvaptan.
- CBD **is safe** with tolvaptan.
- Plant cannabis **causes** or **slows** ADPKD.
- *CNR1* localization or study 1 Gate A/S.
- CB1 antagonists treat ADPKD.
- A FAERS reporting-odds ratio as a confirmatory DDI or AKI signal.
- A computed CYP IC50 or docking score as a clinical DDI.
- Midazolam-null as proof the pair is safe.
- Gate R zero as proof no healthy-volunteer pair-PK study exists.

Dual hepatotoxicity of co-use (Jynarque boxed liver + REMS; Epidiolex transaminase elevations) is **unknown**, distinct from pair PK.

---

## Exploratory (not confirmatory)

2026-08-31 CT.gov/PubMed pair-term look (not Gate R; not a new frozen query): no dedicated CBD–tolvaptan PK study found. Five PubMed hits are *Methods Find Exp Clin Pharmacol* “Gateways to clinical trials” indexes (PMIDs 20401351, 18040531, 17440629, 16541195, 16273137) — **do not fetch**.

Jynarque 12.3: tolvaptan is a P-gp substrate. Epidiolex increases some oral P-gp substrates. That overlap is an **unregistered analog hypothesis**, not pair PK and not a labeled named interaction.

ICTRP / EU CTR / jRCT were not searched. Adding them as confirmatory Gate R would be a protocol deviation.

Leftovers remain in [`EXPLORE.md`](EXPLORE.md) until a **new** sealed protocol.

---

## Limitations

- ClinicalTrials.gov only for Gate R; frozen `query.intr` is a token list, not a synonym expansion.
- Four taxonomy headings are not a systematic review of each class.
- Empty `data/pdfs/` means no human-dropped paywalled paper, not a completed literature census.
- Analog PK cannot stand in for a dedicated pair study.

---

## Reproducibility

| Item | Value |
|---|---|
| Protocol freeze | `db44b3086ae8c4d640dc40f44945bcef27ffe6bc` |
| OSF | https://osf.io/t6rzu/ |
| CLAIMS amendment comment | `yk2xgmj9tpd3` (2026-08-31T19:26:50Z) |
| Fixture | From `studies/cannabis-safety/`: `uv run python pipeline/ctgov_include.py --fixture` |
| Operator notes | [`research/`](research/) Units 00–04; validation in [`research/05-validation.md`](research/05-validation.md) |

Raw DailyMed XML, KDIGO PDF, and CT.gov JSON live under gitignored `studies/cannabis-safety/data/`. Checksums are in the unit notes.

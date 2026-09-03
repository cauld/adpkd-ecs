# Unit 04 — CBD–tolvaptan DDI class (Gate U)

**Run.** 2026-08-30.  
**Inputs.** Unit 02 (neither label names the other); PROTOCOL allowed classes; human PDF drop empty. Gate R is **not** a pair-PK search.  
**Not this unit.** GEO. FAERS ROR. CYP IC50 / docking. Advice to start or stop cannabis.

---

## Pair classification (CBD + tolvaptan)

PROTOCOL classes: documented pair PK · labeled interaction · unstudied (default) · analog only (bounds, not the pair).

| Class | Applies? | Why |
|---|---|---|
| Documented pair PK | **Not found in sources searched** | No dedicated PK/DDI study of cannabidiol/Epidiolex **with tolvaptan** is cited. Gate R cannot show this: a healthy-volunteer DDI trial would not match `query.cond` ADPKD/PKD. Empty `data/pdfs/` means no human-dropped paper, not a completed literature census. Exploratory (not frozen) CT.gov/PubMed look 2026-08-31 is below; it is **not** Gate R and **not** proof no unpublished study exists. |
| Labeled interaction | **No** | Unit 02: Jynarque SPL does not name Epidiolex/cannabidiol/cannabis; Epidiolex SPL does not name Jynarque/tolvaptan. |
| Unstudied | **Yes (PROTOCOL default)** | Neither a cited pair-PK study nor a labeled named interaction. Default, not a demonstration that no pair study exists anywhere. |
| Analog only | Narrative **bounds**, not the pair class | Midazolam, everolimus, tacrolimus, grapefruit — PROTOCOL list. |

**Operator class for the pair: `unstudied`.**

`Unstudied` + analogs **must not** be rewritten as contraindicated or safe (`PROTOCOL.md`, `KILL.md` Gate U).

---

## Analog bounds (not the pair)

These are **analog only**. They do not move Gate U.

1. **Midazolam (Epidiolex 12.3).** Coadministration of EPIDIOLEX 750 mg twice daily with midazolam 2.5 mg (sensitive CYP3A4 substrate) **did not** change midazolam plasma concentrations. This is **not** a CBD–tolvaptan study and is **not** proof the pair is safe. Jynarque is metabolized almost exclusively by CYP3A; strong CYP3A **inhibitors** are contraindicated — Epidiolex is not named as such an inhibitor on the Jynarque label.

2. **Everolimus (Epidiolex 7.2 / 12.3).** Oral everolimus exposures ~2.5-fold with EPIDIOLEX (P-gp and CYP3A4 substrate). **Not** tolvaptan.

3. **Tacrolimus (Epidiolex 7.2).** Named as an example oral P-gp substrate that **may** have increased exposure. **Not** a pair PK study with tolvaptan.

4. **Grapefruit (Jynarque 7.1 / 12.3).** Avoid grapefruit juice with JYNARQUE (Cmax +90%, AUC +60% in the labeled juice study). **Not** a CBD product.

**Unregistered analog (not in PROTOCOL’s analog list).** Jynarque 12.3: “Tolvaptan is a substrate of P-gp and an inhibitor of P-gp and BCRP.” Epidiolex increases some **oral** P-gp substrates. That overlap is an exploratory analog hypothesis constructed at Unit 04. It is **not** documented pair PK, **not** a labeled named interaction, and **must not** be written as a CBD–tolvaptan DDI. Midazolam is a CYP3A4 probe, not a P-gp substrate; the midazolam-null result does not bound P-gp.

---

## What this unit will not write

- CBD **is contraindicated** with tolvaptan.  
- CBD **is safe** with tolvaptan.  
- Empty CT.gov = cannabis is safe or effective in ADPKD.  
- Midazolam probe = the pair is safe.  
- Theoretical CYP3A4 story = labeled CBD–tolvaptan DDI.  
- Empty Gate R = no healthy-volunteer pair-PK study exists.  
- Dual hepatotoxicity (Jynarque boxed liver + REMS; Epidiolex transaminase elevations) as a studied co-use liver outcome — that co-use risk is **unknown**, distinct from pair PK.

---

## Converge (operator)

| Gate | Operator artifact | Human mark |
|---|---|---|
| R | `01-ctgov.md` — query frozen, 2026-08-30T16:30:50Z, `totalCount` 0 | Pass (chat 2026-08-30) |
| L | `02-labels.md` — setids, pair names, CYP3A/box, midazolam/P-gp | **Pass** (2026-08-31) |
| T | `03-taxonomy.md` — four classes + KDIGO quotes | **Pass** (scoped; 2026-08-31) |
| U | this file — pair **unstudied**; analogs remain analogs | **Pass** (2026-08-31) |

**Decide** (human, 2026-08-31): T+R+L+U pass → **complete v1 map**. Scribe ≤ `CLAIMS.md`. See [`DECIDE.md`](../DECIDE.md).

---

## Exploratory pair-PK look (2026-08-31) — not Gate R, not a new frozen query

Unit 01 emptiness does **not** by itself rule out a healthy-volunteer CBD–tolvaptan PK study (that study would not need an ADPKD condition). PROTOCOL allows peer-reviewed papers without a proxy crawl. This block is **exploratory** support for Gate U, labeled as such.

| Look | Result |
|---|---|
| CT.gov `query.intr` = `tolvaptan AND (cannabidiol OR epidiolex OR cannabis)` | `totalCount` 0 |
| CT.gov `query.term` = `tolvaptan AND (cannabidiol OR epidiolex)` | `totalCount` 0 |
| PubMed `cannabidiol[tiab] AND tolvaptan[tiab]` | 5 PMIDs, all *Methods Find Exp Clin Pharmacol* “Gateways to clinical trials” (2005–2010) drug-index lists; both names appear as separate catalog entries, not a pair study |
| PubMed `cannabidiol[tiab] AND tolvaptan[tiab] AND (pharmacokinetic* OR interaction OR DDI)` | 0 |
| PubMed `epidiolex[tiab] AND (tolvaptan[tiab] OR jynarque[tiab])` | 0 |
| PubMed `cannabidiol[ti] AND tolvaptan[ti]` | 0 |
| Europe PMC `TITLE_ABS:(cannabidiol AND tolvaptan)` | same 5 Gateways records |

**Do not fetch** PMIDs 20401351, 18040531, 17440629, 16541195, 16273137. They cannot change Gate U.

ICTRP / EU CTR / jRCT were **not** searched (PROTOCOL froze ClinicalTrials.gov for Gate R only). Adding those registries as confirmatory Gate R would be a deviation.

Pair class remains **`unstudied`** as the default. This look does not convert analogs into safe or contraindicated, and does not claim that no unpublished pair study exists.

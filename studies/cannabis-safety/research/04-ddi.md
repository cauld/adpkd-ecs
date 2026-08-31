# Unit 04 — CBD–tolvaptan DDI class (Gate U)

**Run.** 2026-08-30.  
**Inputs.** Unit 01 (`totalCount` 0); Unit 02 (neither label names the other); PROTOCOL allowed classes.  
**Not this unit.** GEO. FAERS ROR. CYP IC50 / docking. Advice to start or stop cannabis.

---

## Pair classification (CBD + tolvaptan)

PROTOCOL classes: documented pair PK · labeled interaction · unstudied (default) · analog only (bounds, not the pair).

| Class | Applies? | Why |
|---|---|---|
| Documented pair PK | **No** | No dedicated PK/DDI study of cannabidiol (or Epidiolex) **with tolvaptan** cited. Unit 01 frozen CT.gov query returned `totalCount` 0 (no ADPKD/PKD + cannabis/cannabinoid intervention). Unit 00 PDF inventory empty. |
| Labeled interaction | **No** | Unit 02: Jynarque SPL does not name Epidiolex/cannabidiol/cannabis; Epidiolex SPL does not name Jynarque/tolvaptan. |
| Unstudied | **Yes (default)** | Neither documented pair PK nor labeled interaction. |
| Analog only | Narrative **bounds**, not the pair class | Midazolam, everolimus, tacrolimus, grapefruit — below. |

**Operator class for the pair: `unstudied`.**

`Unstudied` + analogs **must not** be rewritten as contraindicated or safe (`PROTOCOL.md`, `KILL.md` Gate U).

---

## Analog bounds (not the pair)

These are **analog only**. They do not move Gate U.

1. **Midazolam (Epidiolex 12.3).** Coadministration of EPIDIOLEX 750 mg twice daily with midazolam 2.5 mg (sensitive CYP3A4 substrate) **did not** change midazolam plasma concentrations. This is **not** a CBD–tolvaptan study and is **not** proof the pair is safe. Jynarque is metabolized almost exclusively by CYP3A; strong CYP3A **inhibitors** are contraindicated — Epidiolex is not named as such an inhibitor on the Jynarque label.

2. **Everolimus (Epidiolex 7.2 / 12.3).** Oral everolimus exposures ~2.5-fold with EPIDIOLEX (P-gp and CYP3A4 substrate). **Not** tolvaptan.

3. **Tacrolimus (Epidiolex 7.2).** Named as an example oral P-gp substrate that **may** have increased exposure. **Not** a pair PK study with tolvaptan.

4. **Grapefruit (Jynarque 7.1 / 12.3).** Avoid grapefruit juice with JYNARQUE (Cmax +90%, AUC +60% in the labeled juice study). **Not** a CBD product.

Jynarque is a P-gp substrate (12.3). Epidiolex increases some **oral** P-gp substrates. That overlap is an analog hypothesis, **not** documented pair PK and **not** a labeled named interaction.

---

## What this unit will not write

- CBD **is contraindicated** with tolvaptan.  
- CBD **is safe** with tolvaptan.  
- Empty CT.gov = cannabis is safe or effective in ADPKD.  
- Midazolam probe = the pair is safe.  
- Theoretical CYP3A4 story = labeled CBD–tolvaptan DDI.

---

## Converge (operator)

| Gate | Operator artifact | Human mark |
|---|---|---|
| R | `01-ctgov.md` — query frozen, 2026-08-30T16:30:50Z, `totalCount` 0 | Pass (chat 2026-08-30) |
| L | `02-labels.md` — setids, pair names, CYP3A/box, midazolam/P-gp | **Open** |
| T | `03-taxonomy.md` — four classes + KDIGO quotes | **Open** |
| U | this file — pair **unstudied**; analogs remain analogs | **Open** |

**Decide** (human): T+R+L+U pass → complete v1 map; claims ceiling in `CLAIMS.md`. Operator does not Decide. Scribe must not exceed `CLAIMS.md`.

**Human marks Gate U and Decide.**

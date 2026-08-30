# ADPKD-ECS kill-test plan (external review)

**Study:** ADPKD-ECS study 1 — *CNR1* localization in GSE185948 and specificity vs DKD in GSE195460.  
**Program:** cannabis / ECS × ADPKD. Study 2 (safety map) is a **separate** seal.  
**Stage:** Protocol **GIT-SEALED** 2026-08-30 (`db44b30`). OSF not submitted. No *CNR1*-vs-cell-type analysis has been run.  
**Audience:** Independent reviewer (stats / computational nephrology / pharmacology).  
**Ask:** Can this protocol be frozen as a secondary-data preregistration, or must it change first?

**Source of truth:** `PROTOCOL.md` and `KILL.md`. This brief restates them. If anything here disagrees with those files, **those files win**. Related: `QUESTION.md`, `CLAIMS.md`. Source narrative (not confirmatory): [`docs/briefing/cannabinoid-adpkd-pathways.md`](docs/briefing/cannabinoid-adpkd-pathways.md). Claim under audit: Hinden et al., *Mol Med* 2026.

**What we are not asking you to bless:** docking, THCV analog generation, dual CB1/CB2 ligands, CYP3A4 models, MQ1, wet lab, a clinical guideline, or study 2’s CBD–tolvaptan map. **GSE195460 is in study 1 as Gate S** (cannot pass Gate A).

---

## 1. Question and claims

**Question.** After a *CNR1*-blind PT freeze, is *CNR1* higher in ADPKD vs control **inside PT** in GSE185948 (not a whole-kidney mean), and is that upshift **absent** as DKD vs control inside PT in GSE195460?

**If gates pass, we may say:** Gate C detectability; A1 disease induction inside PT **or** A2 map-only; Gate B composition wall; Gate S specificity **only if** A1 passed and S passed.

**We will not say:** take or avoid cannabinoids for ADPKD; CB1 causes cysts; any compound treats PKD; CBD contraindicated with Jynarque.

A clean **negative** on Gate A is a complete v1.

**Named confounds.** (1) More injured PT nuclei in ADPKD. (2) *CNR1* already a PT gene in controls. (3) Same within-PT upshift in DKD.

---

## 2. Design in one picture

```
Unit 00  GEO landing pages (GSE185948 + GSE195460) + metadata column names
        ↓
Seal + OSF (study 1 only)
        ↓
Unit 01  freeze PT labels on BOTH atlases (author or marker fallback, no CNR1)
        ↓
Unit 02  Gate C detection (ADPKD atlas)
        ↓
Unit 03  Gate A (A1 if controls else A2)
        ↓
Unit 04  Gate B protocol/composition diagnostics
        ↓
Unit 05  Gate S (DKD within-PT) — only if A1 passed and S eligible
        ↓
Unit 06  Converge + human Decide
```

Train/test wall: both state maps locked before *CNR1* differentials on either accession.

---

## 3. Frozen objects

**Kill gene:** `CNR1` only.

**PT identity (not the kill):** `LRP2, CUBN, SLC34A1, SLC13A3`  
**Injured PT:** `VCAM1, HAVCR1, PROM1`  
**Descriptive ECS:** `CNR2, GPR55, FAAH, MGLL, NAPEPLD, DAGLA, DAGLB, TRPV1`

Prefer author metadata labels when present. Same lists on both atlases.

---

## 4. Gates

See `KILL.md` (C, A1/A2, B1–B3, S). Human pass/fail. S cannot pass A.

---

## 5. What would change this protocol

- GSE185948 lacks usable PT labels **and** the marker fallback is not identifiable in the matrix → amend or stop.
- Fewer than 3+3 samples for A1 → A2 only; claims ceiling already forbids calling that induction; S cannot claim specificity.
- GSE195460 count files are not the matrices Hinden used, or n < 3+3 → S ineligible; A1 may still stand without a specificity claim.
- Laptop/Spark cannot load the RNA objects → human may opt into Superpowers feasibility mode; still not confirmatory.

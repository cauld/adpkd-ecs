# ADPKD-ECS kill-test plan (external review)

**Study:** ADPKD-ECS — endocannabinoid system localization in public ADPKD snRNA-seq.  
**Stage:** Protocol **DRAFT**, not sealed. No *CNR1*-vs-cell-type analysis has been run.  
**Audience:** Independent reviewer (stats / computational nephrology / pharmacology).  
**Ask:** Can this protocol be frozen as a secondary-data preregistration, or must it change first?

**Source of truth:** `PROTOCOL.md` and `KILL.md`. This brief restates them. If anything here disagrees with those files, **those files win**. Related: `QUESTION.md`, `CLAIMS.md`. Source narrative (not confirmatory): [`docs/briefing/cannabinoid-adpkd-pathways.md`](docs/briefing/cannabinoid-adpkd-pathways.md).

**What we are not asking you to bless:** docking, THCV analog generation, dual CB1/CB2 ligands, CYP3A4 models, MQ1, DKD GEO, wet lab, or a clinical guideline.

---

## 1. Question and claims

**Question.** In GSE185948, is *CNR1* enriched in a frozen PT / failed-repair state, and (if controls exist) is that enrichment ADPKD-vs-control inside PT rather than a constitutive PT marker or a composition artifact?

**If gates pass, we may say:** Gate C detectability; A1 disease induction inside PT **or** A2 map-only PT enrichment; protocol wall against *CNR1*-defined clusters.

**We will not say:** take or avoid cannabinoids for ADPKD; CB1 causes cysts; any compound treats PKD.

A clean **negative** is a complete v1.

**Named confounds.** (1) More injured PT nuclei in ADPKD. (2) *CNR1* already a PT gene in controls.

---

## 2. Design in one picture

```
Unit 00  GEO landing page + metadata column names   [no CNR1 plots]
        ↓
Seal + OSF
        ↓
Unit 01  freeze PT labels (author or marker fallback, no CNR1)
        ↓
Unit 02  Gate C detection
        ↓
Unit 03  Gate A (A1 if controls else A2)
        ↓
Unit 04  Gate B protocol/composition diagnostics
        ↓
Unit 05  Converge + human Decide
```

Train/test wall: cell states locked before *CNR1* differentials.

---

## 3. Frozen objects

**Kill gene:** `CNR1` only.

**PT identity (not the kill):** `LRP2, CUBN, SLC34A1, SLC13A3`  
**Injured PT:** `VCAM1, HAVCR1, PROM1`  
**Descriptive ECS:** `CNR2, GPR55, FAAH, MGLL, NAPEPLD, DAGLA, DAGLB, TRPV1`

Prefer author metadata labels when present.

---

## 4. Gates

See `KILL.md` (C, A1/A2, B1–B3). Human pass/fail.

---

## 5. What would change this protocol

- GSE185948 lacks usable PT labels **and** the marker fallback is not identifiable in the matrix → amend or stop.
- Fewer than 3+3 samples for A1 → A2 only; claims ceiling already forbids calling that induction.
- Laptop cannot load `GSE185948_count_RNA.rds.gz` (~1.8 GB compressed) → human may opt into Superpowers feasibility mode; still not confirmatory.

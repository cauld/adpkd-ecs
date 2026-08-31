# Cannabis / CBD / CB1-drug ADPKD evidence map — Analysis Plan

> **For agentic workers:** REQUIRED SUB-SKILL: pre-register this plan with science-superpowers:preregistering-analysis BEFORE execution. In this repo that lock is **human Seal + OSF** for **this study directory**, not study 1’s OSF. Then execute units. Steps use checkbox (`- [ ]`) syntax.

**Question:** Using FDA labels, trial registries, KDIGO, and published human evidence, what can be stated—and what must remain unknown—about cannabis, CBD, synthetic cannabinoids, and CB1-targeting drugs in people with ADPKD, including co-use with tolvaptan?

**Design:** Structured evidence map (not a meta-analysis of treatment effects).

**Data:** DailyMed setids in `PROTOCOL.md`; ClinicalTrials.gov API v2; KDIGO 2025 full guideline PDF; human-dropped papers.

**Primary analysis:** Frozen queries + label extraction + four-class taxonomy + DDI class {documented pair, labeled, unstudied, analog only}.

**Decision rule:** Human marks Gates T, R, L, U in `studies/cannabis-safety/KILL.md`. Unstudied + analogs must not be rewritten as contraindicated or safe.

---

**Survey:** [`docs/science-superpowers/surveys/2026-08-30-study2-cannabis-safety.md`](../surveys/2026-08-30-study2-cannabis-safety.md)  
**Contract:** `studies/cannabis-safety/PROTOCOL.md`. PROTOCOL wins.

**Confounds:** collapsed exposures (T); label laundering (L/U). No GEO *CNR1*.

**Power:** Not applicable.

**Do not load GSE185948 / GSE195460.** Do not treat a Specify-era API ping as Gate R.

### Task 1: Source register (Unit 00)

**Artifacts:** `studies/cannabis-safety/research/00-sources.md`

- [x] **Step 1:** Record DailyMed URLs, setids, label revision dates.
- [x] **Step 2:** Record KDIGO PDF URL and page/section for PP 7.3.4.1 and Table 19.
- [x] **Step 3:** Validate: both setids match PROTOCOL; no study 1 count paths.

### Task 2: Registry query (Unit 01, Gate R)

**Artifacts:** `studies/cannabis-safety/research/01-ctgov.md` + JSON export

- [x] **Step 1:** `GET https://clinicaltrials.gov/api/v2/studies?countTotal=true` with frozen `query.cond` and `query.intr`.
- [x] **Step 2:** Save UTC timestamp, `totalCount`, and NCT IDs of hits.
- [x] **Step 3:** Classify each hit include/exclude with one-line reason.
- [x] **Step 4:** Human marks Gate R.

### Task 3: Labels (Unit 02, Gate L)

**Artifacts:** `studies/cannabis-safety/research/02-labels.md`

- [x] **Step 1:** Extract Jynarque CYP3A / boxed liver / whether cannabis or Epidiolex is named.
- [x] **Step 2:** Extract Epidiolex midazolam sentence, P-gp examples, hepatotoxicity, whether Jynarque/tolvaptan is named.
- [ ] **Step 3:** Human marks Gate L. Quote labels; do not quote the briefing as a label.

### Task 4: Taxonomy + KDIGO (Unit 03, Gate T)

**Artifacts:** `studies/cannabis-safety/research/03-taxonomy.md`

- [x] **Step 1:** Four sections: plant cannabis; CBD (Rx vs OTC if sources distinguish); synthetic cannabinoids; CB1-targeting drugs.
- [x] **Step 2:** Quote PP 7.3.4.1 and Table 19 cannabis row.
- [ ] **Step 3:** Human marks Gate T.

### Task 5: DDI class + converge (Unit 04, Gate U)

**Artifacts:** `studies/cannabis-safety/research/04-ddi.md`

- [x] **Step 1:** Classify CBD + tolvaptan as documented pair / labeled / unstudied / analog only per PROTOCOL.
- [x] **Step 2:** Analogs (midazolam, everolimus, tacrolimus, grapefruit) stay analog only.
- [ ] **Step 3:** Human marks U and Decide. Scribe ≤ study 2 `CLAIMS.md`.

### Simulated-data analog

Not a statistical estimator. **Validation:** a dummy JSON with one NCT that is ADPKD+tolvaptan (not cannabis) must be **excluded** by the include rule; a dummy NCT with cannabidiol intervention + ADPKD condition must be **included**. Implement as a fixture test after Seal, seed not required.

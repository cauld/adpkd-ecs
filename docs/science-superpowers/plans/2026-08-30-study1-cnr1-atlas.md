# CNR1 two-atlas kill — Analysis Plan

> **For agentic workers:** REQUIRED SUB-SKILL: pre-register this plan with science-superpowers:preregistering-analysis BEFORE execution. In this repo that lock is **human Seal + OSF** (`STATUS.md`), not an agent OSF click. Then use science-superpowers:subagent-driven-analysis or executing-analysis. Steps use checkbox (`- [ ]`) syntax for tracking.

**Question:** After freezing PT / failed-repair without *CNR1* as a marker, is *CNR1* higher in ADPKD than in control inside that state in GSE185948 (after a composition check), and is that within-PT induction absent in DKD under the same freeze (GSE195460)?

**Design:** Observational secondary analysis of public snRNA-seq; cross-sectional donor groups; confirmatory gene *CNR1* only.

**Data:** GSE185948 RNA counts + metadata; GSE195460 Cell Ranger RNA h5 (Control1–6, DN1–5). Unit = donor for A1/S; nucleus detection for Gate C.

**Primary analysis:** Within frozen PT, pseudobulk sum → log1p(CPM) → Welch t 95% CI for ADPKD − control (A1) or the locked A2 contrast; Gate S is the same estimator for DKD − control and **cannot** pass A.

**Decision rule:** Human marks `KILL.md` (C, A1/A2, B, S). CI excludes 0 in the hypothesized direction to pass A1 or to **fail** S (DKD higher). S pass = CI includes 0 or DKD not higher. Fail ≠ proof of no effect.

---

**Survey inputs:** [`docs/science-superpowers/surveys/2026-08-30-study1-cnr1-atlas.md`](../surveys/2026-08-30-study1-cnr1-atlas.md)  
**Contract:** repo-root `PROTOCOL.md`, `KILL.md`, `CLAIMS.md`. If this plan and PROTOCOL disagree, **PROTOCOL wins**.

**Confounds:** composition → Gate A/S inside PT + B1/B3; constitutive PT marker → A1 vs A2; generic injury → Gate S; pseudoreplication → donor-level t; label leakage → freeze without *CNR1*.

**Power:** Fixed public n; large-effect only; recorded in PROTOCOL.

**Do not run any step that loads counts until Seal + OSF.**

### Task 1: Immutable raw + inventory (Unit 00)

**Artifacts:**
- Create: `pipeline/inventory_00.py` (after Seal)
- Reads: GEO files under `data/raw/` (gitignored, immutable)
- Writes: `research/data-inventory.md`

- [ ] **Step 1:** After Seal, download GSE185948 `GSE185948_metadata_RNA.csv.gz` and `GSE185948_count_RNA.rds.gz` (or landing-page names if GEO renamed; record aliases). Checksums into inventory.
- [ ] **Step 2:** Download GSE195460 RNA h5 only (Control1–6, DN1–5). Do not unpack 14 GiB RAW tar.
- [ ] **Step 3:** Record **column names** and sample n per disease group. Confirm `CNR1` and ≥2/4 PT-identity genes in each feature index. **No *CNR1* summaries.**
- [ ] **Step 4:** Validate: inventory lists files, sizes, checksums, n, missing genes. If `CNR1` absent in ADPKD matrix → stop/amend, do not run A.

### Task 2: Freeze labels both atlases (Unit 01)

**Artifacts:** `research/01-frozen-labels.md`

- [ ] **Step 1:** Map author PT / FR-PTC strings if present; else PROTOCOL marker rule (mean z PT vs other epithelium, ≥2 PT genes; injured = any of VCAM1/HAVCR1/PROM1).
- [ ] **Step 2:** Exclude immune/endothelial/fibroblast/PEC from A and S contrast sides.
- [ ] **Step 3:** **Commit** both maps before Unit 02.
- [ ] **Step 4:** Validate: *CNR1* not in assignment gene list; n nuclei per bucket recorded **without** *CNR1* DE.

### Task 3: Simulated estimator check (mandatory, after Seal, before real *CNR1* DE)

**Artifacts:** `pipeline/sim_welch_pseudobulk.py`

- [ ] **Step 1:** Simulate two groups of donors, ≥3 each, with a known log-mean difference on one gene and extra zero-inflated genes.
- [ ] **Step 2:** Run the locked pipeline (sum, drop bins <10 nuclei, log1p CPM, Welch t).
- [ ] **Step 3:** Validate: when the planted difference is large, 95% CI excludes 0 in the true direction; when difference is 0, CI typically includes 0 (report seed `20260829`).
- [ ] **Step 4:** Do **not** retune Gate C 1% / 100-nucleus thresholds from the simulation.

### Task 4: Gate C (Unit 02)

**Artifacts:** `research/02-detection.md`

- [ ] **Step 1:** Fraction of nuclei with *CNR1* count > 0 in frozen ADPKD PT object; n nuclei.
- [ ] **Step 2:** Human marks Gate C per `KILL.md`.
- [ ] **Step 3:** If C fail, stop A and S.

### Task 5: Gate A (Unit 03)

**Artifacts:** `research/03-gate-a.md`

- [ ] **Step 1:** If Unit 00 n ≥3 ADPKD and ≥3 control → A1 only (within PT). Else A2. Do not switch after seeing *CNR1*.
- [ ] **Step 2:** Pseudobulk *CNR1*; Welch t; 95% CI. Descriptive ECS genes FDR appendix only.
- [ ] **Step 3:** Human marks Gate A.
- [ ] **Step 4:** Validate: table used PT object only (B1 will re-check).

### Task 6: Gate B (Unit 04)

**Artifacts:** `research/04-gate-b.md`

- [ ] **Step 1:** Run only if A passed. B1 protocol wall; B2 failed-repair split if A1; B3 epithelial mean vs p_PT (cannot pass A).

### Task 7: Gate S (Unit 05)

**Artifacts:** `research/05-gate-s.md`

- [ ] **Step 1:** Run only if C passed **and** A1 passed **and** S eligible (n≥3 DKD and ≥3 control).
- [ ] **Step 2:** C_S detection on DKD PT object; if fail, S ineligible.
- [ ] **Step 3:** Same estimator, DKD vs control within PT. Human marks S.

### Task 8: Converge (Unit 06)

**Artifacts:** `research/06-converge.md`

- [ ] **Step 1:** Fill Decide table from `KILL.md`. Scribe ≤ `CLAIMS.md`.
- [ ] **Step 2:** Human Decide. No confirmatory-field edits.

### Figures (planned, after gates)

Detection bar (C); forest/CI of A1 or A2; B3 scatter optional; S CI. No UMAP colored by *CNR1* to name clusters.

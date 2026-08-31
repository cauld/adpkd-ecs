---
id: 00
role: Operator
status: done
reads:
  - PROTOCOL.md
must_not:
  - Download-and-plot CNR1 vs cell type or disease to choose the model
  - Cluster nuclei using CNR1
  - Open Pathways B–D structure files as confirmatory
  - Load study 2 literature into Gate A
---

# Unit 00 — Data access inventory

**Goal.** Prove GSE185948 and GSE195460 (plus any GEO files they point to for counts) open, pin exact files, record whether author cell-type and control-sample columns exist. No biology conclusions. **Run blocker for Units 01–06** after Seal.

**Inputs.**

- GEO https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE185948
- GEO https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE195460
- Prefer processed metadata + count matrices named on the landing pages. Do not use the 25 GB GSE185948 RAW tar for v1.

**Procedure.**

1. Record license, URLs, file sizes, checksums after download into `data/raw/`.
2. From metadata: **column names** and sample/donor counts for ADPKD vs control and DKD vs control (if any). Do not summarize *CNR1*.
3. Confirm PT-identity and injured-PT genes from `PROTOCOL.md` are present in each feature index (symbol match). Record missing genes per accession.
4. Record RAM/disk so the human can opt into feasibility mode if an RNA object will not load. Do not enter feasibility unasked.
5. Write `research/data-inventory.md`.

**Outputs.** `research/data-inventory.md`

**Pass criteria.** ADPKD RNA counts + metadata reachable. Feature index contains `CNR1` and at least 2/4 PT-identity genes. DKD files named and reachable, or Unit 00 records S ineligible with reason. If `CNR1` absent from the ADPKD matrix → do not Seal Gate A (amend or stop).

## Notes (after run)

- Ran 2026-08-30. Output: `research/data-inventory.md`. Runner: `pipeline/inventory_00.py`.
- Pass: ADPKD metadata + RDS reachable; DKD 11 RNA h5s reachable. `CNR1` + 4/4 PT-identity genes in both feature scans. No *CNR1* plots.
- Gate A contrast lock: **A1** (8 PKD + 5 control patients). Gate S sample n: eligible (6 control + 5 DN libraries).
- GSE185948 `celltype` tokens include `PT1`/`PT2`; no `FR-PTC`. GSE195460: no author cell-type table on GEO.
- RDS is **double-gzipped**. Unit 01 must peel both layers. Counts not loaded. 24 GiB RAM — do not enter feasibility unasked.

---
id: 00
role: Operator
status: blocked-until-seal
reads:
  - PROTOCOL.md
must_not:
  - Download-and-plot CNR1 vs cell type or disease to choose the model
  - Cluster nuclei using CNR1
  - Open Pathways B–D structure files as confirmatory
---

# Unit 00 — Data access inventory

**Goal.** Prove GSE185948 opens, pin exact files, record whether author cell-type and control-sample columns exist. No biology conclusions. **Run blocker for Units 01–05** after Seal.

**Inputs.**

- GEO series https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE185948
- Prefer processed `GSE185948_metadata_RNA.csv.gz` and `GSE185948_count_RNA.rds.gz` (names on the landing page). Do not use the 25 GB RAW tar for v1.

**Procedure.**

1. Record license, URLs, file sizes, checksums after download into `data/raw/`.
2. From metadata: **column names** and sample/donor counts for ADPKD vs control (if any). Do not summarize *CNR1*.
3. Confirm PT-identity and injured-PT genes from `PROTOCOL.md` are present in the feature index (symbol match). Record missing genes.
4. Record RAM/disk so the human can opt into feasibility mode if the RNA RDS will not load. Do not enter feasibility unasked.
5. Write `research/data-inventory.md`.

**Outputs.** `research/data-inventory.md`

**Pass criteria.** RNA counts + metadata reachable. Feature index contains `CNR1` and at least 2/4 PT-identity genes. If `CNR1` absent → do not Seal Gate A (amend or stop).

## Notes (after run)

- Not run. Waiting on Seal.

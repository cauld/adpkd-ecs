# Study 1 OSF close-out — what to post

**Registration (already exists).** https://osf.io/7g3tn/  
**Do not** re-register. **Do not** edit the frozen ITEM 1–26 answers. Same pattern as study 2’s 2026-08-31 comment.

**Results git SHA.** `857d872c3b986dcc65f2aafae386680c2d651e62` (Decide + numbers + this packet). Protocol freeze remains `db44b30`.

## 1. Comment (posted 2026-09-18)

Posted as comment `nqwkh6jmruxd` on https://osf.io/7g3tn/ (text: [`study1-osf-comment-2026-09-03-decide.txt`](study1-osf-comment-2026-09-03-decide.txt)). **Do not** re-register.

## 2. File archive (git; OSF files locked)

**Blocked 2026-09-18.** OSF WaterButler returned `400 Registered Nodes are immutable`. These files stay in **git** (do not upload GEO counts):

| File | Why |
|---|---|
| `DECIDE.md` | Human Decide (C fail) |
| `research/07-scribe.md` | Short report ≤ claims ceiling |
| `research/02-detection.md` | Gate C numbers |
| `research/gate_c_stats.json` | Machine-readable Gate C |
| `research/06-converge.md` | Protocol vs outputs |
| `research/01-frozen-labels.md` | PT freeze (no *CNR1* DE) |
| `research/data-inventory.md` | Accessions, n, checksums |
| `research/raw-checksums.txt` | SHA-256 of downloaded GEO files |
| `pipeline/gate_c_02.R` | Detection runner |
| `docs/osf/study1-prereg-audit-2026-09-03.txt` | Plugin audit FAIL (documented) |

## 3. Do not upload

- `data/` counts, RDS, Cell Ranger h5 (public on GEO; gitignored; large)
- Study 2 files or https://osf.io/t6rzu/ comments
- Docking / PDB / ADMET
- Secrets (`.env`, OSF tokens)

## 4. After you post

Record the OSF comment ID in `STATUS.md` (same as study 2 `yk2xgmj9tpd3`). Wiki optional: one sentence pointing at the comment + `DECIDE.md`.

**Posted.** Comment `nqwkh6jmruxd` (2026-09-18T18:19:35Z). Files stay in git.

# Study 1 OSF close-out — what to post

**Registration (already exists).** https://osf.io/7g3tn/  
**Do not** re-register. **Do not** edit the frozen ITEM 1–26 answers. Same pattern as study 2’s 2026-08-31 comment.

**Results git SHA.** `857d872c3b986dcc65f2aafae386680c2d651e62` (Decide + numbers + this packet). Protocol freeze remains `db44b30`.

## 1. Comment (required)

Paste [`study1-osf-comment-2026-09-03-decide.txt`](study1-osf-comment-2026-09-03-decide.txt) as a **registration comment** on https://osf.io/7g3tn/ .

Optional API (token with `osf.nodes_write`; do not commit it):

```bash
export OSF_TOKEN='...'
curl -sS -X POST 'https://api.osf.io/v2/registrations/7g3tn/comments/' \
  -H "Authorization: Bearer $OSF_TOKEN" \
  -H 'Content-Type: application/vnd.api+json' \
  -d @docs/osf/study1-osf-comment-2026-09-03-decide.json
```

## 2. Files to upload (required)

On the same registration, **Files** → upload these (plain text / markdown / JSON only). Do **not** upload GEO count matrices, RDS, h5, or `.env`.

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

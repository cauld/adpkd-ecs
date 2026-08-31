# Unit 00 — Source register (study 2)

**Run.** 2026-08-30, retrieval window ~16:19–16:21 UTC.  
**OSF.** https://osf.io/t6rzu/  
**Protocol freeze.** `db44b3086ae8c4d640dc40f44945bcef27ffe6bc`  
**This unit does not claim.** No DDI class, no Gate R/L/T/U, no *CNR1*, no GEO.

**Toolchain.** `curl` 8.7.1; DailyMed REST v2; KDIGO PDF SHA-256; page locators via `pypdf` on that PDF (not a statistic). Seed `20260829` is unused (no stochastic step). ClinicalTrials.gov API was **not** called.

Raw copies (gitignored under `studies/cannabis-safety/data/`):

| File | SHA-256 |
|---|---|
| `data/raw/KDIGO-2025-ADPKD-Guideline.pdf` (9 537 380 bytes) | `302f80af1aa44377ad2f23b619933412ab3c306b6a00cc90bce7e1471839bc0c` |
| `data/raw/dailymed-jynarque-history.json` | `03f9129a75755e5720138abcb42a2891087e929ef904ea975177f69d16f2e6a6` |
| `data/raw/dailymed-jynarque-spls.json` | `e10a2c5c224ed718c01bdb8b28dbc3da3231ceb18fe54add21531d78dd44b1f5` |
| `data/raw/dailymed-epidiolex-history.json` | `18b1b6cd743d40f561020ce24b156823fdd8c361c99a2838c6e8f362b4c24cc7` |
| `data/raw/dailymed-epidiolex-spls.json` | `353f4c00f618e74ffd7082c7a308d67b9de553960cd431935a31f3037c3a4511` |

---

## 1. DailyMed / FDA PI

Setids match `PROTOCOL.md` CONFIRMATORY sources. HTTP GET of each `drugInfo.cfm` URL returned 200.

| Product | Setid (frozen) | DailyMed label | DailyMed PI PDF | SPL history | Current SPL |
|---|---|---|---|---|---|
| Jynarque (tolvaptan) | `3febc0a1-9e5a-4ce0-843d-210f21d862c4` | https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=3febc0a1-9e5a-4ce0-843d-210f21d862c4 | https://dailymed.nlm.nih.gov/dailymed/getFile.cfm?setid=3febc0a1-9e5a-4ce0-843d-210f21d862c4&type=pdf | https://dailymed.nlm.nih.gov/dailymed/services/v2/spls/3febc0a1-9e5a-4ce0-843d-210f21d862c4/history.json | https://dailymed.nlm.nih.gov/dailymed/services/v2/spls.json?setid=3febc0a1-9e5a-4ce0-843d-210f21d862c4 |
| Epidiolex (cannabidiol) | `8bf27097-4870-43fb-94f0-f3d0871d1eec` | https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=8bf27097-4870-43fb-94f0-f3d0871d1eec | https://dailymed.nlm.nih.gov/dailymed/getFile.cfm?setid=8bf27097-4870-43fb-94f0-f3d0871d1eec&type=pdf | https://dailymed.nlm.nih.gov/dailymed/services/v2/spls/8bf27097-4870-43fb-94f0-f3d0871d1eec/history.json | https://dailymed.nlm.nih.gov/dailymed/services/v2/spls.json?setid=8bf27097-4870-43fb-94f0-f3d0871d1eec |

### Revision dates recorded at this run

DailyMed uses more than one clock. Unit 02 extracts fact types from this current SPL; it does not treat a newer `published_date` as a license to change those fact types.

| Product | SPL `setId` | `versionNumber` | SPL `effectiveTime` (label revision) | DailyMed HTML “Updated” | Highlights “Revised” | History `published_date` (this version) |
|---|---|---|---|---|---|---|
| Jynarque | `3febc0a1-9e5a-4ce0-843d-210f21d862c4` | 19 | 20251106 | November 6, 2025 | 3/2025 | Nov 17, 2025 |
| Epidiolex | `8bf27097-4870-43fb-94f0-f3d0871d1eec` | 35 | 20260529 | May 29, 2026 | 5/2026 | Jun 15, 2026 |

SPL document `id` roots at this retrieval (not the setid): Jynarque `3be8a6fe-a8d0-43ca-a84d-183b522a3cf4`; Epidiolex `1eb7ac65-8df5-4a4a-9156-802cfaa92b06`. Titles from `/spls.json`: JYNARQUE (TOLVAPTAN) … [OTSUKA AMERICA PHARMACEUTICAL, INC.]; EPIDIOLEX (CANNABIDIOL) SOLUTION [JAZZ PHARMACEUTICALS, INC.].

Neither setid 404’d or was retired. No successor URL.

---

## 2. KDIGO 2025 ADPKD guideline

**Official PDF (frozen URL).** https://kdigo.org/wp-content/uploads/2025/01/KDIGO-2025-ADPKD-Guideline.pdf  

HEAD 200; `Content-Type: application/pdf`; `Last-Modified: Tue, 21 Jan 2025 06:07:02 GMT`; `Content-Length: 9537380`. GET matched that size. SHA-256 above.

**PDF metadata (locator only).** 240 pages. Title: *KDIGO 2025 Clinical Practice Guideline for the Evaluation, Management, and Treatment of Autosomal Dominant Polycystic Kidney Disease (ADPKD)*. DOI `10.1016/j.kint.2024.07.009`. Journal citation in metadata: *Kidney International*, 107 (2024) S1–S239.

**Required excerpt locators** (page numbers only; quoting is Unit 03):

| Item | Where in this PDF |
|---|---|
| Practice Point 7.3.4.1 | PDF pages **46** (repeated practice-point list) and **164** (chapter body) |
| Table 19 | TOC lists journal page **S163**; table body on PDF page **164** |

Key-takeaways PDF: not retrieved. PROTOCOL: it may supplement, not replace, this full guideline.

---

## 3. ClinicalTrials.gov query (copied, not run)

Gate R is **Unit 01**. This block is the frozen string from `PROTOCOL.md`, recorded so Unit 01 cannot silently rewrite it.

**Endpoint.** `GET https://clinicaltrials.gov/api/v2/studies` with `countTotal=true`

**`query.cond`** (exact):

```
"polycystic kidney" OR ADPKD OR PKD1 OR PKD2
```

**`query.intr`** (exact):

```
cannabis OR cannabidiol OR cannabinoid OR THC OR dronabinol OR nabiximols OR epidiolex
```

**Constructed URL (not fetched):**

```
https://clinicaltrials.gov/api/v2/studies?countTotal=true&query.cond=%22polycystic%20kidney%22%20OR%20ADPKD%20OR%20PKD1%20OR%20PKD2&query.intr=cannabis%20OR%20cannabidiol%20OR%20cannabinoid%20OR%20THC%20OR%20dronabinol%20OR%20nabiximols%20OR%20epidiolex
```

API docs (not a result): https://clinicaltrials.gov/data-api/about-api

**Not recorded:** `totalCount`, NCT list, include/exclude. A Specify-era ping is still not Gate R.

---

## 4. Human-dropped PDFs

Directory `studies/cannabis-safety/data/pdfs/` does not exist. Inventory: **zero** paywalled papers. Unit 00 pass criteria do not require any. Do not proxy-crawl publishers to fill this.

---

## 5. Validation (this unit)

- [x] Jynarque setid equals PROTOCOL `3febc0a1-9e5a-4ce0-843d-210f21d862c4`
- [x] Epidiolex setid equals PROTOCOL `8bf27097-4870-43fb-94f0-f3d0871d1eec`
- [x] KDIGO URL equals PROTOCOL official PDF URL
- [x] CT.gov `query.cond` / `query.intr` copied from PROTOCOL; API not called
- [x] No `GSE185948` / `GSE195460` / study 1 count paths used
- [x] No CBD–tolvaptan DDI class written
- [x] No label CYP / midazolam / P-gp / boxed-warning facts extracted (Unit 02)
- [x] No KDIGO practice-point or Table 19 wording quoted (Unit 03)

## Pass criteria (unit packet)

| Criterion | Status |
|---|---|
| DailyMed/FDA PI URLs for Jynarque and Epidiolex recorded | met |
| KDIGO PDF URL recorded | met |
| CT.gov query string copied from PROTOCOL | met |
| DailyMed revision dates recorded (Clarify 1) | met |

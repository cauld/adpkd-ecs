"""Study 2 Unit 01 — frozen ClinicalTrials.gov include/exclude rule.

Does not load GEO. Does not rewrite query.cond / query.intr.
Seed is unused (no stochastic step).
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.parse import urlencode

import requests

SEED = 20260829  # recorded; unused

# Frozen — PROTOCOL.md CONFIRMATORY sources (must match character-for-character)
QUERY_COND = '"polycystic kidney" OR ADPKD OR PKD1 OR PKD2'
QUERY_INTR = (
    "cannabis OR cannabidiol OR cannabinoid OR THC OR dronabinol OR nabiximols OR epidiolex"
)
API_BASE = "https://clinicaltrials.gov/api/v2/studies"
PAGE_SIZE = 1000
UA = "adpkd-ecs-study2-unit01/0.1 (github.com/cauld/adpkd-ecs)"

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"
RESEARCH = ROOT / "research"

# Disease-condition locators (not gene-only in an unrelated indication)
_PKD_CONDITION = re.compile(
    r"polycystic\s+kidney|\badpkd\b|autosomal\s+dominant\s+polycystic|\bpkd\s*[- ]?1\b|\bpkd\s*[- ]?2\b|\bpkd\b",
    re.I,
)

# PROTOCOL query.intr tokens, applied to intervention names (not eligibility)
_INTR_PROTOCOL = re.compile(
    r"cannabis|cannabidiol|cannabinoid|\bthc\b|dronabinol|nabiximols|epidiolex",
    re.I,
)
# Same intervention class as cannabis / cannabidiol if they appear as names
_INTR_SYNONYM = re.compile(r"marijuana|marihuana|\bcbd\b", re.I)


def _blob(parts: list[str]) -> str:
    return " | ".join(p for p in parts if p)


def extract(study: dict[str, Any]) -> dict[str, Any]:
    ps = study.get("protocolSection") or {}
    ident = ps.get("identificationModule") or {}
    cond = ps.get("conditionsModule") or {}
    arms = ps.get("armsInterventionsModule") or {}
    elig = ps.get("eligibilityModule") or {}
    interventions = arms.get("interventions") or []
    names: list[str] = []
    types: list[str] = []
    for iv in interventions:
        if not isinstance(iv, dict):
            continue
        names.append(str(iv.get("name") or ""))
        types.append(str(iv.get("type") or ""))
        for other in iv.get("otherNames") or []:
            names.append(str(other))
    conditions = [str(c) for c in (cond.get("conditions") or [])]
    return {
        "nct_id": ident.get("nctId") or ident.get("nct_id") or "",
        "brief_title": ident.get("briefTitle") or "",
        "conditions": conditions,
        "intervention_names": names,
        "intervention_types": types,
        "eligibility": elig.get("eligibilityCriteria") or "",
    }


def classify(study: dict[str, Any]) -> dict[str, str]:
    """Apply PROTOCOL Gate R rule. Never drop; always return include or exclude."""
    row = extract(study)
    nct = row["nct_id"] or "UNKNOWN"
    cond_text = _blob(row["conditions"])
    iv_text = _blob(row["intervention_names"])
    elig = row["eligibility"]

    pkd_cond = bool(_PKD_CONDITION.search(cond_text))
    iv_match = bool(_INTR_PROTOCOL.search(iv_text) or _INTR_SYNONYM.search(iv_text))
    elig_only = bool(
        (_INTR_PROTOCOL.search(elig) or _INTR_SYNONYM.search(elig)) and not iv_match
    )

    if pkd_cond and iv_match:
        decision = "include"
        reason = "ADPKD/PKD condition and cannabis/cannabinoid intervention name"
    elif pkd_cond and elig_only:
        decision = "exclude"
        reason = "ADPKD/PKD condition; cannabinoid mention in eligibility only, not an intervention"
    elif pkd_cond and not iv_match:
        decision = "exclude"
        reason = "ADPKD/PKD condition; no cannabis/cannabinoid intervention listed"
    elif iv_match and not pkd_cond:
        decision = "exclude"
        reason = "cannabinoid intervention; condition list is not ADPKD/PKD"
    else:
        decision = "exclude"
        reason = "neither ADPKD/PKD condition nor cannabinoid intervention"

    return {
        "nct_id": nct,
        "brief_title": row["brief_title"],
        "conditions": "; ".join(row["conditions"]),
        "interventions": "; ".join(row["intervention_names"]),
        "decision": decision,
        "reason": reason,
    }


def dummy_exclude_tolvaptan() -> dict[str, Any]:
    return {
        "protocolSection": {
            "identificationModule": {
                "nctId": "NCT00000001",
                "briefTitle": "Tolvaptan in ADPKD (fixture, not a real NCT)",
            },
            "conditionsModule": {
                "conditions": ["Autosomal Dominant Polycystic Kidney Disease"]
            },
            "armsInterventionsModule": {
                "interventions": [{"name": "Tolvaptan", "type": "DRUG"}]
            },
            "eligibilityModule": {"eligibilityCriteria": "Adults with ADPKD."},
        }
    }


def dummy_include_cbd() -> dict[str, Any]:
    return {
        "protocolSection": {
            "identificationModule": {
                "nctId": "NCT00000002",
                "briefTitle": "Cannabidiol in ADPKD (fixture, not a real NCT)",
            },
            "conditionsModule": {"conditions": ["ADPKD"]},
            "armsInterventionsModule": {
                "interventions": [{"name": "Cannabidiol", "type": "DRUG"}]
            },
            "eligibilityModule": {"eligibilityCriteria": "Adults with ADPKD."},
        }
    }


def dummy_exclude_elig_only() -> dict[str, Any]:
    """Eligibility cannabis mention must not count as an intervention."""
    return {
        "protocolSection": {
            "identificationModule": {
                "nctId": "NCT00000003",
                "briefTitle": "Tolvaptan; cannabis in eligibility only (fixture)",
            },
            "conditionsModule": {"conditions": ["ADPKD"]},
            "armsInterventionsModule": {
                "interventions": [{"name": "Tolvaptan", "type": "DRUG"}]
            },
            "eligibilityModule": {
                "eligibilityCriteria": "Exclusion: current cannabis or cannabidiol use."
            },
        }
    }


def run_fixtures() -> None:
    ex = classify(dummy_exclude_tolvaptan())
    inc = classify(dummy_include_cbd())
    elig = classify(dummy_exclude_elig_only())
    errors: list[str] = []
    if ex["decision"] != "exclude":
        errors.append(f"tolvaptan dummy expected exclude, got {ex}")
    if inc["decision"] != "include":
        errors.append(f"cannabidiol dummy expected include, got {inc}")
    if elig["decision"] != "exclude":
        errors.append(f"eligibility-only dummy expected exclude, got {elig}")
    if errors:
        print("FIXTURE FAIL", file=sys.stderr)
        for e in errors:
            print(e, file=sys.stderr)
        raise SystemExit(1)
    print("FIXTURE PASS")
    print(f"  NCT00000001 {ex['decision']}: {ex['reason']}")
    print(f"  NCT00000002 {inc['decision']}: {inc['reason']}")
    print(f"  NCT00000003 {elig['decision']}: {elig['reason']}")


def request_url(page_token: str | None = None) -> str:
    q = {
        "format": "json",
        "countTotal": "true",
        "pageSize": str(PAGE_SIZE),
        "query.cond": QUERY_COND,
        "query.intr": QUERY_INTR,
    }
    if page_token:
        q["pageToken"] = page_token
    return f"{API_BASE}?{urlencode(q)}"


def fetch_all() -> dict[str, Any]:
    session = requests.Session()
    session.headers.update({"User-Agent": UA, "Accept": "application/json"})
    retrieved_utc = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    studies: list[dict[str, Any]] = []
    total_count: int | None = None
    pages = 0
    token: str | None = None
    urls: list[str] = []
    statuses: list[int] = []

    while True:
        url = request_url(token)
        urls.append(url)
        resp = session.get(url, timeout=60)
        statuses.append(resp.status_code)
        resp.raise_for_status()
        payload = resp.json()
        pages += 1
        if total_count is None:
            total_count = int(payload.get("totalCount") or 0)
        batch = payload.get("studies") or []
        if not isinstance(batch, list):
            raise RuntimeError("API studies field is not a list")
        studies.extend(batch)
        token = payload.get("nextPageToken") or None
        if not token:
            break
        if pages > 50:
            raise RuntimeError("pagination exceeded 50 pages; stopping to avoid a runaway loop")

    if total_count is None:
        raise RuntimeError("API omitted totalCount")
    return {
        "retrieved_utc": retrieved_utc,
        "query.cond": QUERY_COND,
        "query.intr": QUERY_INTR,
        "api_base": API_BASE,
        "request_urls": urls,
        "http_status": statuses,
        "page_count": pages,
        "totalCount": total_count,
        "n_studies_downloaded": len(studies),
        "studies": studies,
    }


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--fixture", action="store_true")
    p.add_argument("--fetch", action="store_true")
    args = p.parse_args()
    if args.fixture:
        run_fixtures()
        return
    if args.fetch:
        run_fixtures()
        RAW.mkdir(parents=True, exist_ok=True)
        bundle = fetch_all()
        raw_path = RAW / "ctgov-unit01.json"
        encoded = json.dumps(bundle, indent=2, sort_keys=True).encode("utf-8")
        raw_path.write_bytes(encoded)
        digest = sha256_bytes(encoded)
        rows = [classify(s) for s in bundle["studies"]]
        class_path = RAW / "ctgov-unit01-classified.json"
        class_path.write_text(json.dumps(rows, indent=2) + "\n", encoding="utf-8")
        summary = {
            "retrieved_utc": bundle["retrieved_utc"],
            "totalCount": bundle["totalCount"],
            "n_studies_downloaded": bundle["n_studies_downloaded"],
            "page_count": bundle["page_count"],
            "http_status": bundle["http_status"],
            "sha256_ctgov_unit01_json": digest,
            "n_include": sum(1 for r in rows if r["decision"] == "include"),
            "n_exclude": sum(1 for r in rows if r["decision"] == "exclude"),
            "rows": rows,
        }
        print(json.dumps({k: v for k, v in summary.items() if k != "rows"}, indent=2))
        print(f"raw={raw_path}")
        print(f"sha256={digest}")
        print(f"classified={class_path}")
        if bundle["n_studies_downloaded"] != bundle["totalCount"]:
            print(
                "ANOMALY: n_studies_downloaded != totalCount",
                bundle["n_studies_downloaded"],
                bundle["totalCount"],
                file=sys.stderr,
            )
            raise SystemExit(2)
        return
    p.error("pass --fixture or --fetch")


if __name__ == "__main__":
    main()

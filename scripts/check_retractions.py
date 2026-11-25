#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Check all primary-source-verified DOIs for Crossref retraction / correction notices.

Playbook v1.3 Checklist #16 (Retraction Watch / Crossref update-to audit).
Reads `data/citation-verification-log.json`, queries Crossref politely for every
verified DOI (using concurrent worker threads + polite Mailto User-Agent), inspects
`update-to`, `updated-by`, `relation`, `type`, and title retraction indicators, and
writes `data/retraction-audit.json`.

Usage:
    python scripts/check_retractions.py
    python scripts/check_retractions.py --check   # verify existing log reports 0 retractions
"""

from __future__ import annotations

import argparse
import concurrent.futures
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
CIT_LOG = ROOT / "data" / "citation-verification-log.json"
OUT_PATH = ROOT / "data" / "retraction-audit.json"
CONTACT = os.environ.get("ATLAS_CONTACT_EMAIL", "0_0@0thernes.art")
VERSION = (ROOT / "VERSION").read_text(encoding="utf-8").strip() if (ROOT / "VERSION").exists() else "0.4.0"
USER_AGENT = f"UnsolvedMathematicsAtlas/{VERSION} (https://github.com/0thernes/unsolved-mathematics; mailto:{CONTACT})"

RETRACTION_RE = re.compile(r"\b(retract(?:ed|ion)|withdraw(?:n|al)|erratum|corrigendum)\b", re.I)


def extract_verified_dois(cit_data: dict[str, Any]) -> list[str]:
    dois: set[str] = set()
    for rec in cit_data.get("records", []):
        if rec.get("verdict") != "verified":
            continue
        doi = rec.get("doi")
        if doi and isinstance(doi, str) and doi.strip():
            dois.add(doi.strip())
    return sorted(dois)


def fetch_datacite_status(doi: str, timeout: float = 15.0) -> dict[str, Any]:
    encoded = urllib.parse.quote(doi, safe="")
    url = f"https://api.datacite.org/dois/{encoded}"
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Accept": "application/json"})
    last_err = ""
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                payload = json.loads(resp.read().decode("utf-8"))
            attrs = payload.get("data", {}).get("attributes", {})
            titles = attrs.get("titles") or []
            title = str(titles[0].get("title", "")) if titles and isinstance(titles[0], dict) else ""
            descs = attrs.get("descriptions") or []
            desc_text = " ".join(str(d.get("description", "")) for d in descs if isinstance(d, dict))
            flags: list[str] = []
            retracted = False
            corrected = False
            for rel in attrs.get("relatedIdentifiers") or []:
                rtype = str(rel.get("relationType", "")).lower()
                if "retract" in rtype or "withdraw" in rtype:
                    retracted = True
                    flags.append(f"datacite-relation:{rtype}:{rel.get('relatedIdentifier', '')}")
            if RETRACTION_RE.search(title) or re.search(r"\b(?:this paper has been withdrawn|withdrawn by the author|retracted)\b", desc_text, re.I):
                retracted = True
                flags.append("datacite-withdrawal-notice")
            return {
                "doi": doi,
                "registry": "datacite",
                "http_status": 200,
                "retracted": retracted,
                "corrected_or_updated": corrected,
                "flags": flags,
                "title": title[:140],
                "error": None,
            }
        except urllib.error.HTTPError as e:
            last_err = f"HTTP {e.code}"
            if e.code == 429 or e.code >= 500:
                time.sleep(1.5 * (attempt + 1))
                continue
            break
        except Exception as e:
            last_err = str(e)
            time.sleep(1.0 * (attempt + 1))
    return {
        "doi": doi,
        "registry": "datacite",
        "http_status": None,
        "retracted": False,
        "corrected_or_updated": False,
        "flags": [],
        "title": "",
        "error": last_err,
    }


def fetch_crossref_status(doi: str, timeout: float = 15.0) -> dict[str, Any]:
    if doi.lower().startswith("10.48550/"):
        return fetch_datacite_status(doi, timeout=timeout)
    encoded = urllib.parse.quote(doi, safe="")
    url = f"https://api.crossref.org/works/{encoded}"
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Accept": "application/json"})
    last_err = ""
    for attempt in range(5):
        try:
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                payload = json.loads(resp.read().decode("utf-8"))
            msg = payload.get("message", {})
            titles = msg.get("title") or []
            title = str(titles[0]) if titles else ""
            update_to = msg.get("update-to") or []
            updated_by = msg.get("updated-by") or []
            relation = msg.get("relation") or {}

            flags: list[str] = []
            retracted = False
            corrected = False

            for u in updated_by:
                utype = str(u.get("type", "")).lower()
                ulabel = str(u.get("label", "")).lower()
                if "retract" in utype or "retract" in ulabel or "withdraw" in utype:
                    retracted = True
                    flags.append(f"updated-by:{utype or ulabel}:{u.get('DOI', '')}")
                elif utype or ulabel:
                    corrected = True
                    flags.append(f"updated-by:{utype or ulabel}:{u.get('DOI', '')}")

            for u in update_to:
                utype = str(u.get("type", "")).lower()
                if "retract" in utype:
                    retracted = True
                    flags.append(f"update-to:{utype}:{u.get('DOI', '')}")

            for rel_key, rel_vals in relation.items():
                if "retract" in str(rel_key).lower():
                    retracted = True
                    flags.append(f"relation:{rel_key}:{len(rel_vals) if isinstance(rel_vals, list) else 1}")

            if RETRACTION_RE.search(title):
                m = RETRACTION_RE.search(title)
                if m and m.group(1).lower().startswith(("retract", "withdraw")):
                    retracted = True
                else:
                    corrected = True
                flags.append(f"title-match:{title[:80]}")

            return {
                "doi": doi,
                "registry": "crossref",
                "http_status": 200,
                "retracted": retracted,
                "corrected_or_updated": corrected,
                "flags": flags,
                "title": title[:140],
                "error": None,
            }
        except urllib.error.HTTPError as e:
            last_err = f"HTTP {e.code}"
            if e.code == 429 or e.code >= 500:
                time.sleep(1.5 * (attempt + 1))
                continue
            break
        except Exception as e:
            last_err = str(e)
            time.sleep(1.0 * (attempt + 1))
    return {
        "doi": doi,
        "registry": "crossref",
        "http_status": None,
        "retracted": False,
        "corrected_or_updated": False,
        "flags": [],
        "title": "",
        "error": last_err,
    }


def check_existing() -> int:
    if not OUT_PATH.exists():
        print("ERROR: data/retraction-audit.json missing. Run python scripts/check_retractions.py", file=sys.stderr)
        return 1
    data = json.loads(OUT_PATH.read_text(encoding="utf-8"))
    summary = data.get("summary", {})
    retracted = summary.get("retracted", -1)
    net_errs = summary.get("network_errors", -1)
    if retracted != 0:
        print(f"ERROR: {retracted} retracted DOI(s) recorded in data/retraction-audit.json!", file=sys.stderr)
        return 1
    if net_errs != 0:
        print(f"ERROR: {net_errs} network error(s) recorded in data/retraction-audit.json!", file=sys.stderr)
        return 1
    print(
        f"OK: data/retraction-audit.json clean — {summary.get('dois_checked', 0)} verified DOIs audited, "
        f"0 retracted, {summary.get('corrected_or_updated', 0)} with publisher update/corrigendum notices, 0 errors."
    )
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit verified DOIs for Crossref retraction notices.")
    parser.add_argument("--check", action="store_true", help="Offline verify existing data/retraction-audit.json.")
    parser.add_argument("--workers", type=int, default=6, help="Concurrent Crossref query threads (default 6).")
    args = parser.parse_args()

    if args.check:
        return check_existing()

    cit_data = json.loads(CIT_LOG.read_text(encoding="utf-8"))
    dois = extract_verified_dois(cit_data)
    print(f"Auditing {len(dois)} primary-source-verified DOIs against Crossref retraction/update metadata...")

    results: list[dict[str, Any]] = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as pool:
        for res in pool.map(fetch_crossref_status, dois):
            results.append(res)

    results.sort(key=lambda r: r["doi"])
    retracted = [r for r in results if r["retracted"]]
    corrected = [r for r in results if r["corrected_or_updated"] and not r["retracted"]]
    errors = [r for r in results if r["error"]]

    report = {
        "audited_utc": datetime.now(UTC).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "source_log": "data/citation-verification-log.json",
        "method": "Crossref REST API v1 (/works/{doi}) inspection of updated-by, update-to, relation, and title retraction/withdrawal/erratum fields",
        "summary": {
            "dois_checked": len(results),
            "retracted": len(retracted),
            "corrected_or_updated": len(corrected),
            "clean": len(results) - len(retracted) - len(corrected) - len(errors),
            "network_errors": len(errors),
        },
        "retracted_records": retracted,
        "corrected_or_updated_records": corrected,
        "error_records": errors,
    }
    OUT_PATH.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n")
    print(
        f"Done -> {OUT_PATH.relative_to(ROOT)}: checked={len(results)}, "
        f"retracted={len(retracted)}, corrected_or_updated={len(corrected)}, network_errors={len(errors)}"
    )
    return 0 if not retracted and not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())

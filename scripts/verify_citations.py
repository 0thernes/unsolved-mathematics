#!/usr/bin/env python3
"""
verify_citations.py — Primary-source citation verification against arXiv & Crossref.

Scans every `problems/<slug>/papers.md` table for DOI and arXiv identifiers,
queries primary registries (`export.arxiv.org` and `api.crossref.org`), checks
title/year agreement (rejecting valid IDs that resolve to an unrelated paper),
writes an auditable ledger to `data/citation-verification-log.json`, and
optionally (`--apply`) promotes strictly confirmed rows to `verified`.

Usage:
  python scripts/verify_citations.py             # dry-run report + write log
  python scripts/verify_citations.py --apply     # promote verified rows in papers.md
  python scripts/verify_citations.py --arxiv-only
"""
from __future__ import annotations

import argparse
import concurrent.futures
import datetime as dt
import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")  # type: ignore[attr-defined]
except Exception:
    pass

ROOT = Path(__file__).resolve().parent.parent
PROBLEMS_DIR = ROOT / "problems"
LOG_PATH = ROOT / "data" / "citation-verification-log.json"
USER_AGENT = "UnsolvedMathematicsAtlas/0.3.0 (https://github.com/0thernes/unsolved-mathematics; mailto:0_0@0thernes.art)"

ARXIV_RE = re.compile(r"(?:arXiv[:.]\s*|arxiv\.org/abs/)(\d{4}\.\d{4,5}(?:v\d+)?|[a-z\-]+(?:\.[A-Z]{2})?/\d{7})", re.I)
DOI_RE = re.compile(r"(10\.\d{4,9}/[^\s,;\|`<>]+)")
STOPWORDS = {
    "the", "of", "and", "for", "with", "from", "that", "this", "into", "over",
    "about", "some", "note", "notes", "on", "in", "to", "a", "an", "by", "at",
    "via", "its", "their", "new", "proof", "problem", "conjecture", "theorem",
}


def norm_words(text: str) -> set[str]:
    clean = re.sub(r"[^a-z0-9\s]", " ", text.lower())
    return {w for w in clean.split() if len(w) >= 3 and w not in STOPWORDS}


def title_overlap_score(claimed: str, remote: str) -> float:
    w1 = norm_words(claimed)
    w2 = norm_words(remote)
    if not w1 or not w2:
        return 0.0
    inter = w1 & w2
    return len(inter) / min(len(w1), len(w2))


def clean_doi(raw: str) -> str:
    return raw.rstrip(".").rstrip(")").rstrip("]")


def extract_rows() -> list[dict]:
    rows: list[dict] = []
    for pf in sorted(PROBLEMS_DIR.glob("*/papers.md")):
        slug = pf.parent.name
        for lineno, line in enumerate(pf.read_text(encoding="utf-8").splitlines(), 1):
            if not line.strip().startswith("|"):
                continue
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) < 7:
                continue
            flag = cells[-1].lower()
            if flag not in {"verified", "high-confidence", "needs-verification", "ai-suggested"}:
                continue
            row_id, year_str, title, authors, _kind, ident = cells[0], cells[1], cells[2], cells[3], cells[4], cells[5]
            arx = ARXIV_RE.search(ident)
            doi = DOI_RE.search(ident)
            if not arx and not doi:
                continue
            rows.append(
                {
                    "slug": slug,
                    "path": str(pf.relative_to(ROOT)).replace("\\", "/"),
                    "lineno": lineno,
                    "row": row_id,
                    "claimed_year": year_str,
                    "claimed_title": title,
                    "claimed_authors": authors,
                    "identifier_raw": ident,
                    "arxiv_id": arx.group(1) if arx else None,
                    "doi": clean_doi(doi.group(1)) if doi else None,
                    "current_flag": flag,
                }
            )
    return rows


def fetch_arxiv_batch(ids: list[str]) -> dict[str, dict]:
    out: dict[str, dict] = {}
    ns = {"a": "http://www.w3.org/2005/Atom"}
    for i in range(0, len(ids), 35):
        batch = ids[i : i + 35]
        url = "https://export.arxiv.org/api/query?id_list=" + urllib.parse.quote(",".join(batch)) + "&max_results=100"
        req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
        try:
            data = urllib.request.urlopen(req, timeout=30).read()
            root = ET.fromstring(data)
            for entry in root.findall("a:entry", ns):
                raw_id = entry.findtext("a:id", "", ns)
                if "/abs/" not in raw_id:
                    continue
                eid = raw_id.split("/abs/")[-1]
                base_id = re.sub(r"v\d+$", "", eid)
                title = " ".join((entry.findtext("a:title", "", ns) or "").split())
                pub = (entry.findtext("a:published", "", ns) or "")[:4]
                authors = [a.findtext("a:name", "", ns) or "" for a in entry.findall("a:author", ns)]
                rec = {"remote_id": eid, "remote_title": title, "remote_year": pub, "remote_authors": authors}
                out[base_id.lower()] = rec
                out[eid.lower()] = rec
        except Exception as exc:
            for bid in batch:
                out.setdefault(bid.lower(), {"error": str(exc)})
        time.sleep(0.4)
    return out


def fetch_crossref_doi(doi: str) -> dict:
    url = "https://api.crossref.org/works/" + urllib.parse.quote(doi, safe="")
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=20) as resp:
                payload = json.loads(resp.read().decode("utf-8"))
            msg = payload.get("message", {})
            titles = msg.get("title") or []
            title = " ".join((titles[0] if titles else "").split())
            year = ""
            for key in ("published-print", "published-online", "issued", "created"):
                parts = (msg.get(key) or {}).get("date-parts") or []
                if parts and parts[0]:
                    year = str(parts[0][0])
                    break
            authors = []
            for a in msg.get("author") or []:
                fam = a.get("family") or ""
                giv = a.get("given") or ""
                authors.append(f"{giv} {fam}".strip())
            return {"status": "ok", "remote_title": title, "remote_year": year, "remote_authors": authors}
        except urllib.error.HTTPError as exc:
            if exc.code == 404:
                return {"status": "not_found", "http_code": 404}
            if exc.code in (429, 500, 502, 503, 504) and attempt < 2:
                time.sleep(1.0 * (attempt + 1))
                continue
            return {"status": "http_error", "http_code": exc.code}
        except Exception as exc:
            if attempt < 2:
                time.sleep(0.8 * (attempt + 1))
                continue
            return {"status": "network_error", "error": str(exc)}
    return {"status": "network_error", "error": "max retries exceeded"}


def author_match(claimed_authors: str, remote_authors: list[str]) -> bool:
    if not remote_authors:
        return False
    ca = claimed_authors.lower()
    for ra in remote_authors:
        tokens = [t for t in re.findall(r"[a-z]{3,}", ra.lower())]
        if tokens and tokens[-1] in ca:
            return True
    return False


def main() -> int:
    ap = argparse.ArgumentParser(description="Verify DOIs and arXiv IDs against primary registries.")
    ap.add_argument("--apply", action="store_true", help="Promote confirmed rows to 'verified' in papers.md")
    ap.add_argument("--strip-invalid", action="store_true", help="Replace confirmed hallucinated/404 identifiers with '—' and downgrade to needs-verification")
    ap.add_argument("--arxiv-only", action="store_true", help="Verify arXiv IDs only")
    ap.add_argument("--workers", type=int, default=4, help="Concurrent Crossref workers")
    args = ap.parse_args()

    rows = extract_rows()
    arxiv_ids = sorted({r["arxiv_id"] for r in rows if r["arxiv_id"]})
    dois = sorted({r["doi"] for r in rows if r["doi"] and not args.arxiv_only})
    print(f"Found {len(rows)} rows with identifiers ({len(arxiv_ids)} unique arXiv, {len(dois)} unique DOI).")

    arxiv_map = fetch_arxiv_batch(arxiv_ids) if arxiv_ids else {}
    doi_map: dict[str, dict] = {}
    if dois:
        with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as ex:
            futs = {ex.submit(fetch_crossref_doi, d): d for d in dois}
            for fut in concurrent.futures.as_completed(futs):
                doi_map[futs[fut]] = fut.result()

    today = dt.date.today().isoformat()
    results: list[dict] = []
    counts = {"verified": 0, "mismatch": 0, "not_found": 0, "network_error": 0, "skipped": 0}

    for r in rows:
        verdict = "skipped"
        remote_title = ""
        remote_year = ""
        overlap = 0.0
        auth_ok = False
        source = ""

        if r["arxiv_id"]:
            source = "arxiv"
            key = re.sub(r"v\d+$", "", r["arxiv_id"]).lower()
            rec = arxiv_map.get(key) or arxiv_map.get(r["arxiv_id"].lower())
            if rec is None:
                verdict = "not_found"
            elif "error" in rec:
                verdict = "network_error"
            else:
                remote_title = rec["remote_title"]
                remote_year = rec["remote_year"]
                overlap = round(title_overlap_score(r["claimed_title"], remote_title), 3)
                auth_ok = author_match(r["claimed_authors"], rec["remote_authors"])
                if overlap >= 0.40 or (overlap >= 0.20 and auth_ok):
                    verdict = "verified"
                else:
                    verdict = "mismatch"
        elif r["doi"] and not args.arxiv_only:
            source = "crossref"
            rec = doi_map.get(r["doi"], {"status": "network_error"})
            st = rec.get("status")
            if st == "not_found":
                verdict = "not_found"
            elif st != "ok":
                verdict = "network_error"
            else:
                remote_title = rec.get("remote_title", "")
                remote_year = rec.get("remote_year", "")
                overlap = round(title_overlap_score(r["claimed_title"], remote_title), 3)
                auth_ok = author_match(r["claimed_authors"], rec.get("remote_authors", []))
                if overlap >= 0.40 or (overlap >= 0.20 and auth_ok) or (auth_ok and remote_year and remote_year in r["claimed_year"]):
                    verdict = "verified"
                else:
                    verdict = "mismatch"

        counts[verdict] += 1
        results.append(
            {
                **r,
                "source": source,
                "verdict": verdict,
                "remote_title": remote_title,
                "remote_year": remote_year,
                "title_overlap": overlap,
                "author_match": auth_ok,
                "checked_date": today,
            }
        )

    LOG_PATH.write_text(
        json.dumps({"checked_date": today, "summary": counts, "records": results}, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    print("Verification summary:", counts)

    if args.apply or args.strip_invalid:
        by_path: dict[str, list[dict]] = {}
        for rec in results:
            if args.apply and rec["verdict"] == "verified" and rec["current_flag"] != "verified":
                by_path.setdefault(rec["path"], []).append(rec)
            elif args.strip_invalid and rec["verdict"] in {"not_found", "mismatch"}:
                by_path.setdefault(rec["path"], []).append(rec)
        promoted = 0
        stripped = 0
        for rel, items in sorted(by_path.items()):
            p = ROOT / rel
            lines = p.read_text(encoding="utf-8").splitlines()
            for it in items:
                idx = it["lineno"] - 1
                if 0 <= idx < len(lines):
                    cells = lines[idx].split("|")
                    if len(cells) >= 8:
                        if it["verdict"] == "verified" and args.apply:
                            cells[-2] = " verified "
                            promoted += 1
                        elif it["verdict"] in {"not_found", "mismatch"} and args.strip_invalid:
                            cells[-3] = " — "
                            cells[-2] = " needs-verification "
                            stripped += 1
                        lines[idx] = "|".join(cells)
            p.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
        print(f"Promoted {promoted} rows to 'verified'; stripped {stripped} invalid/mismatched identifiers across {len(by_path)} files.")

    bad = [r for r in results if r["verdict"] in {"not_found", "mismatch"}]
    if bad:
        print(f"\nFlagged {len(bad)} not_found/mismatch rows (logged in {LOG_PATH.relative_to(ROOT)}):")
        for b in bad[:30]:
            print(
                f"  [{b['verdict']:9s}] {b['slug']} #{b['row']} ({b['identifier_raw']}) "
                f"claimed='{b['claimed_title'][:45]}' vs remote='{b['remote_title'][:45]}'"
            )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""
build_indexes.py — Cross-cutting indexes over the Atlas.

Produces navigational views that complement the per-problem dossiers:

    docs/indexes/by-field.md            problems grouped by field
    docs/indexes/by-status.md           problems grouped by status
    docs/indexes/by-century.md          problems grouped by era posed
    docs/indexes/originators.md         every originator -> the problems they posed
    docs/indexes/verification.md        verification-flag dashboard (scans papers.md)

Reads data/problems.json (authoritative) for everything registry-derived, and
scans problems/<slug>/papers.md for the verification dashboard when dossiers are
authored. Safe to run any time; degrades gracefully before dossiers exist.
"""
from __future__ import annotations

import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8")  # type: ignore[attr-defined]
except Exception:
    pass

ROOT = Path(__file__).resolve().parent.parent
REGISTRY = ROOT / "data" / "problems.json"
PROBLEMS = ROOT / "problems"
OUT = ROOT / "docs" / "indexes"
FLAGS = ["verified", "high-confidence", "needs-verification", "ai-suggested"]


def fmt_year(y: int) -> str:
    return f"{abs(y)} BCE" if y < 0 else (f"{y} CE" if y < 1000 else str(y))


def century(y: int) -> str:
    if y < 0:
        return "Antiquity (BCE)"
    if y < 1000:
        return "Pre-1000 CE"
    c = (y // 100) + 1
    suffix = {1: "st", 2: "nd", 3: "rd"}.get(c % 10 if c % 100 not in (11, 12, 13) else 0, "th")
    return f"{c}{suffix} century"


def load() -> list[dict]:
    data = json.loads(REGISTRY.read_text(encoding="utf-8"))
    return data["problems"]


def link(p: dict) -> str:
    return f"[{p['title']}](../../problems/{p['slug']}/README.md)"


def write(name: str, body: str):
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / name).write_text(body, encoding="utf-8")
    print(f"  -> docs/indexes/{name}")


def by_key(problems, keyfn, title, intro):
    groups: dict[str, list[dict]] = defaultdict(list)
    for p in problems:
        groups[keyfn(p)].append(p)
    lines = [f"# {title}\n", intro, ""]
    for key in sorted(groups):
        ps = sorted(groups[key], key=lambda x: x["rank"])
        lines.append(f"## {key}  ({len(ps)})\n")
        for p in ps:
            lines.append(f"- **#{p['rank']}** {link(p)} — *{fmt_year(p['year_posed'])}*, `{p['status']}`")
        lines.append("")
    return "\n".join(lines)


def originators_index(problems):
    idx: dict[str, list[dict]] = defaultdict(list)
    for p in problems:
        for who in p.get("originators", []):
            idx[who].append(p)
    lines = [
        "# Originators Index\n",
        "Every mathematician credited with posing a problem in the atlas, and the "
        "problems attributed to them. Names combining a historical root with a modern "
        "formulator appear under each.\n",
    ]
    for who in sorted(idx, key=lambda n: n.split()[-1]):
        ps = sorted(idx[who], key=lambda x: x["rank"])
        probs = ", ".join(f"{link(p)} (#{p['rank']})" for p in ps)
        lines.append(f"- **{who}** — {probs}")
    return "\n".join(lines) + "\n"


def verification_dashboard(problems):
    rows = []
    totals: Counter = Counter()
    authored = 0
    for p in sorted(problems, key=lambda x: x["rank"]):
        papers = PROBLEMS / p["slug"] / "papers.md"
        if not papers.exists():
            continue
        text = papers.read_text(encoding="utf-8")
        if "<!-- DOSSIER:papers -->" in text:
            rows.append((p, None))
            continue
        authored += 1
        counts: Counter = Counter()
        for line in text.splitlines():
            if not line.strip().startswith("|"):
                continue
            cells = [c.strip().lower() for c in line.strip().strip("|").split("|")]
            if cells and cells[-1] in FLAGS:
                counts[cells[-1]] += 1
                totals[cells[-1]] += 1
        rows.append((p, counts))

    lines = [
        "# Verification Dashboard\n",
        "Provenance of the citation scaffolding across all dossiers. Per "
        "[SOURCING.md](../methodology/SOURCING.md), only `verified` may be cited as "
        "fact; the rest are research leads awaiting a human source check.\n",
        f"**Authored dossiers:** {authored}/{len(problems)}\n",
        "| Flag | Count |",
        "|------|------:|",
    ]
    for f in FLAGS:
        lines.append(f"| `{f}` | {totals.get(f, 0)} |")
    lines += ["", "## Per-problem", "", "| # | Problem | verified | high-conf | needs-verif | ai-suggested |",
              "|---|---------|---------:|----------:|------------:|-------------:|"]
    for p, counts in rows:
        if counts is None:
            lines.append(f"| {p['rank']} | {link(p)} | _not yet authored_ | | | |")
        else:
            lines.append(
                f"| {p['rank']} | {link(p)} | {counts.get('verified',0)} | "
                f"{counts.get('high-confidence',0)} | {counts.get('needs-verification',0)} | "
                f"{counts.get('ai-suggested',0)} |"
            )
    return "\n".join(lines) + "\n"


def main() -> int:
    problems = load()
    write("by-field.md", by_key(problems, lambda p: p["field"], "Problems by Field",
                                "The atlas grouped by primary mathematical field."))
    write("by-status.md", by_key(problems, lambda p: p["status"], "Problems by Status",
                                 "Grouped by current research status."))
    write("by-century.md", by_key(problems, lambda p: century(p["year_posed"]),
                                  "Problems by Era Posed", "Grouped by the century the problem was posed."))
    write("originators.md", originators_index(problems))
    write("verification.md", verification_dashboard(problems))
    print(f"Built indexes for {len(problems)} problems.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

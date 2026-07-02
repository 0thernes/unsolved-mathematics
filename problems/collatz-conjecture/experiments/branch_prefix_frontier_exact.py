#!/usr/bin/env python3
"""Exact survivor-frontier check for prefix branch-potential dominance.

The sampled prefix-dominance run checks ordinary starts, hard records, stress
families, and selected survivor-frontier slices.  This script checks every
positive residue in the exact certificate survivor frontier at a chosen base
depth.  It is a finite exact audit of the known obstruction set, not a proof of
the universal Collatz conjecture.
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path
from time import perf_counter

sys.path.insert(0, str(Path(__file__).resolve().parent))

from branch_potential_analyzer import enumerate_frontier, powers_of_three, round_float, unique_preserving_order
from branch_prefix_dominance_analyzer import analyze_prefix_start, summarize_prefix


def run(args: argparse.Namespace) -> dict[str, object]:
    started = perf_counter()
    frontier, frontier_stats = enumerate_frontier(args.base_depth, powers_of_three(args.max_depth))
    leaves = sorted(frontier, key=lambda leaf: leaf.residue)
    if args.max_frontier is not None:
        leaves = leaves[: args.max_frontier]

    rows: list[dict[str, object]] = []
    by_class: dict[str, list[dict[str, object]]] = defaultdict(list)
    by_odd_count: dict[str, list[dict[str, object]]] = defaultdict(list)
    excluded_small = 0
    seen_residues: set[int] = set()

    for leaf in leaves:
        if leaf.residue <= 1:
            excluded_small += 1
            continue
        if leaf.residue in seen_residues:
            continue
        seen_residues.add(leaf.residue)
        row = analyze_prefix_start(leaf.residue, args.max_steps)
        row["frontier_depth"] = leaf.depth
        row["frontier_odd_count"] = leaf.odd_count
        row["frontier_image"] = leaf.image
        rows.append(row)
        by_class[str(row["class"])].append(row)
        by_odd_count[str(leaf.odd_count)].append(row)

    uncertified = [row for row in rows if not row["certified"]]
    prefix_failures = [row for row in rows if not row["prefix_unit_sufficient"]]

    odd_count_histogram = Counter(str(row["frontier_odd_count"]) for row in rows)
    return {
        "status": "branch-prefix-frontier-exact",
        "elapsed_seconds": round_float(perf_counter() - started, 6),
        "parameters": {
            key: (str(value) if isinstance(value, Path) else value)
            for key, value in vars(args).items()
        },
        "frontier": {
            **frontier_stats,
            "selected_leaf_count": len(leaves),
            "excluded_residue_0_or_1": excluded_small,
            "positive_unique_residues_checked": len(rows),
            "positive_frontier_odd_count_histogram": dict(sorted(odd_count_histogram.items(), key=lambda item: int(item[0]))),
        },
        "total_checked": len(rows),
        "class_counts": dict(sorted(Counter(str(row["class"]) for row in rows).items())),
        "class_summaries": {name: summarize_prefix(members) for name, members in sorted(by_class.items())},
        "odd_count_summaries": {name: summarize_prefix(members) for name, members in sorted(by_odd_count.items(), key=lambda item: int(item[0]))},
        "failure_counts": {
            "uncertified": len(uncertified),
            "prefix_unit": len(prefix_failures),
            "high_formula": sum(int(row["high_formula_failure_count"]) for row in rows),
            "high_alignment_burn": sum(int(row["high_alignment_burn_failure_count"]) for row in rows),
            "low_repeat_law": sum(int(row["low_repeat_law_failure_count"]) for row in rows),
        },
        "max_prefix_deficit": max((int(row["max_prefix_deficit"]) for row in rows), default=0),
        "min_prefix_surplus": min((int(row["min_prefix_surplus"]) for row in rows), default=0),
        "max_prefix_required": max((int(row["max_prefix_required"]) for row in rows), default=0),
        "largest_prefix_failures": sorted(
            prefix_failures,
            key=lambda row: (int(row["max_prefix_deficit"]), float(row["max_excess"]), int(row["start"])),
            reverse=True,
        )[: args.top_n],
        "tightest_prefix_surplus": sorted(
            rows,
            key=lambda row: (int(row["min_prefix_surplus"]), -float(row["max_excess"]), int(row["start"])),
        )[: args.top_n],
        "largest_excess": sorted(rows, key=lambda row: (float(row["max_excess"]), int(row["start"])), reverse=True)[
            : args.top_n
        ],
        "largest_escape": sorted(rows, key=lambda row: (int(row["escape_d"]), int(row["start"])), reverse=True)[
            : args.top_n
        ],
        "interpretation": (
            "Finite exact survivor-frontier audit at the requested base depth. "
            "A positive max_prefix_deficit would falsify prefix dominance on "
            "the exact obstruction frontier at that depth. Zero failures are "
            "evidence only and do not prove the universal theorem."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base-depth", type=int, default=24)
    parser.add_argument("--max-depth", type=int, default=1024)
    parser.add_argument("--max-steps", type=int, default=50000)
    parser.add_argument("--max-frontier", type=int)
    parser.add_argument("--top-n", type=int, default=12)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--quiet", action="store_true")
    args = parser.parse_args()

    if args.base_depth < 1:
        raise SystemExit("--base-depth must be positive")
    if args.max_depth < args.base_depth:
        raise SystemExit("--max-depth must be at least --base-depth")
    if args.max_steps < 1:
        raise SystemExit("--max-steps must be positive")
    if args.max_frontier is not None and args.max_frontier < 1:
        raise SystemExit("--max-frontier must be positive when provided")
    if args.top_n < 1:
        raise SystemExit("--top-n must be positive")

    payload = run(args)
    text = json.dumps(payload, indent=2, sort_keys=True)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text + "\n", encoding="utf-8")
    if not args.quiet:
        print(text)


if __name__ == "__main__":
    main()

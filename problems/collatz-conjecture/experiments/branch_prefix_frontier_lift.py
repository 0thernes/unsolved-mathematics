#!/usr/bin/env python3
"""Multi-depth lift audit for prefix branch-potential dominance.

This script checks exact survivor frontiers at multiple depths and records how
live residues lift from one checked depth to the next.  It is a finite audit of
the proposed lift theorem:

    prefix dominance should persist, or receive visible new credit, as survivor
    frontier shadows are refined to deeper positive residues.
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


def parse_depths(raw_depths: list[str]) -> list[int]:
    depths = unique_preserving_order(int(raw) for raw in raw_depths)
    if not depths:
        raise SystemExit("--depths must include at least one depth")
    bad = [depth for depth in depths if depth < 1]
    if bad:
        raise SystemExit("all --depths values must be positive")
    return sorted(depths)


def frontier_residues(depth: int, max_depth: int) -> tuple[list[object], dict[str, object]]:
    frontier, stats = enumerate_frontier(depth, powers_of_three(max_depth))
    return sorted(frontier, key=lambda leaf: leaf.residue), stats


def summarize_rows(rows: list[dict[str, object]]) -> dict[str, object]:
    prefix_failures = [row for row in rows if not row["prefix_unit_sufficient"]]
    uncertified = [row for row in rows if not row["certified"]]
    return {
        "total_checked": len(rows),
        "class_counts": dict(sorted(Counter(str(row["class"]) for row in rows).items())),
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
        "max_escape": max((int(row["escape_d"]) for row in rows), default=0),
        "max_excess": round_float(max((float(row["max_excess"]) for row in rows), default=0.0)),
        "high_ladder_credit_total": sum(int(row["high_ladder_credit"]) for row in rows),
        "low_repeat_credit_total": sum(int(row["low_repeat_credit"]) for row in rows),
        "largest_prefix_failures": sorted(
            prefix_failures,
            key=lambda row: (int(row["max_prefix_deficit"]), float(row["max_excess"]), int(row["start"])),
            reverse=True,
        ),
        "tightest_prefix_surplus": sorted(
            rows,
            key=lambda row: (int(row["min_prefix_surplus"]), -float(row["max_excess"]), int(row["start"])),
        ),
        "largest_excess": sorted(rows, key=lambda row: (float(row["max_excess"]), int(row["start"])), reverse=True),
        "largest_escape": sorted(rows, key=lambda row: (int(row["escape_d"]), int(row["start"])), reverse=True),
    }


def truncate_examples(summary: dict[str, object], top_n: int) -> dict[str, object]:
    trimmed = dict(summary)
    for key in ("largest_prefix_failures", "tightest_prefix_surplus", "largest_excess", "largest_escape"):
        trimmed[key] = list(trimmed[key])[:top_n]
    return trimmed


def parent_lift_summary(
    *,
    previous_depth: int,
    previous_positive_residues: set[int],
    current_depth: int,
    current_positive_residues: list[int],
) -> dict[str, object]:
    mask = (1 << previous_depth) - 1
    child_counts: Counter[int] = Counter()
    orphan_count = 0
    for residue in current_positive_residues:
        parent = residue & mask
        if parent not in previous_positive_residues:
            orphan_count += 1
            continue
        child_counts[parent] += 1

    histogram = Counter(child_counts.values())
    missing_parent_count = len(previous_positive_residues) - len(child_counts)
    return {
        "previous_depth": previous_depth,
        "current_depth": current_depth,
        "previous_positive_frontier_count": len(previous_positive_residues),
        "current_positive_frontier_count": len(current_positive_residues),
        "current_residues_with_live_parent": sum(child_counts.values()),
        "orphan_current_residues": orphan_count,
        "live_parents_with_children": len(child_counts),
        "live_parents_without_children": missing_parent_count,
        "children_per_live_parent_histogram": dict(sorted((str(k), v) for k, v in histogram.items())),
        "max_children_per_live_parent": max(child_counts.values(), default=0),
    }


def run(args: argparse.Namespace) -> dict[str, object]:
    started = perf_counter()
    depths = parse_depths(args.depths)
    max_depth = max(args.max_depth, max(depths))

    depth_payloads: dict[str, dict[str, object]] = {}
    lift_payloads: dict[str, dict[str, object]] = {}
    previous_depth: int | None = None
    previous_positive_residue_set: set[int] | None = None

    all_rows: list[dict[str, object]] = []

    for depth in depths:
        depth_started = perf_counter()
        leaves, frontier_stats = frontier_residues(depth, max_depth)
        positive_residues: list[int] = []
        rows: list[dict[str, object]] = []
        by_class: dict[str, list[dict[str, object]]] = defaultdict(list)
        by_odd_count: dict[str, list[dict[str, object]]] = defaultdict(list)

        for leaf in leaves:
            if leaf.residue <= 1:
                continue
            positive_residues.append(leaf.residue)
            row = analyze_prefix_start(leaf.residue, args.max_steps)
            row["frontier_depth"] = leaf.depth
            row["frontier_odd_count"] = leaf.odd_count
            row["frontier_image"] = leaf.image
            rows.append(row)
            by_class[str(row["class"])].append(row)
            by_odd_count[str(leaf.odd_count)].append(row)

        summary = summarize_rows(rows)
        depth_payloads[str(depth)] = {
            "elapsed_seconds": round_float(perf_counter() - depth_started, 6),
            "frontier": {
                **frontier_stats,
                "positive_unique_residues_checked": len(rows),
                "positive_frontier_odd_count_histogram": dict(
                    sorted(Counter(str(row["frontier_odd_count"]) for row in rows).items(), key=lambda item: int(item[0]))
                ),
            },
            **truncate_examples(summary, args.top_n),
            "class_summaries": {name: summarize_prefix(members) for name, members in sorted(by_class.items())},
            "odd_count_summaries": {
                name: summarize_prefix(members)
                for name, members in sorted(by_odd_count.items(), key=lambda item: int(item[0]))
            },
        }
        all_rows.extend(rows)

        positive_residue_set = set(positive_residues)
        if previous_depth is not None and previous_positive_residue_set is not None:
            lift_payloads[f"{previous_depth}->{depth}"] = parent_lift_summary(
                previous_depth=previous_depth,
                previous_positive_residues=previous_positive_residue_set,
                current_depth=depth,
                current_positive_residues=positive_residues,
            )
        previous_depth = depth
        previous_positive_residue_set = positive_residue_set

    global_summary = summarize_rows(all_rows)
    return {
        "status": "branch-prefix-frontier-lift",
        "elapsed_seconds": round_float(perf_counter() - started, 6),
        "parameters": {
            key: (str(value) if isinstance(value, Path) else value)
            for key, value in vars(args).items()
        },
        "depths": depth_payloads,
        "lifts": lift_payloads,
        "aggregate": truncate_examples(global_summary, args.top_n),
        "interpretation": (
            "Finite multi-depth survivor-frontier lift audit. Zero prefix "
            "failures across checked depths support, but do not prove, the "
            "universal lift theorem for entry-visible branch credit."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--depths", nargs="+", default=["24", "25", "26"])
    parser.add_argument("--max-depth", type=int, default=1024)
    parser.add_argument("--max-steps", type=int, default=50000)
    parser.add_argument("--top-n", type=int, default=12)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--quiet", action="store_true")
    args = parser.parse_args()

    depths = parse_depths(args.depths)
    if args.max_depth < max(depths):
        raise SystemExit("--max-depth must be at least the largest checked depth")
    if args.max_steps < 1:
        raise SystemExit("--max-steps must be positive")
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

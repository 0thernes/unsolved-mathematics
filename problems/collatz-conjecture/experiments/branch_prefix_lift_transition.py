#!/usr/bin/env python3
"""Parent-child transition audit for prefix branch-potential lifts.

The multi-depth lift audit showed no prefix failures on exact survivor
frontiers at depths 24, 25, and 26.  This script looks inside one depth lift
`d -> d+1`: for each live parent residue, classify its live children, pruned
siblings, prefix-pressure deltas, and structural-credit deltas.

The goal is to make the desired local lift lemma concrete and falsifiable.
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


def compact_row(row: dict[str, object]) -> dict[str, object]:
    return {
        "start": row["start"],
        "class": row["class"],
        "b": row["b"],
        "escape_d": row["escape_d"],
        "max_excess": row["max_excess"],
        "max_prefix_required": row["max_prefix_required"],
        "max_prefix_deficit": row["max_prefix_deficit"],
        "min_prefix_surplus": row["min_prefix_surplus"],
        "combined_unit_credit": row["combined_unit_credit"],
        "high_ladder_credit": row["high_ladder_credit"],
        "low_repeat_credit": row["low_repeat_credit"],
        "high_ladder_count": row["high_ladder_count"],
        "low_repeat_count": row["low_repeat_count"],
    }


def transition_record(
    *,
    parent: int,
    child: int,
    child_bit: int,
    parent_row: dict[str, object],
    child_row: dict[str, object],
    child_leaf: object,
) -> dict[str, object]:
    req_delta = int(child_row["max_prefix_required"]) - int(parent_row["max_prefix_required"])
    credit_delta = int(child_row["combined_unit_credit"]) - int(parent_row["combined_unit_credit"])
    high_delta = int(child_row["high_ladder_credit"]) - int(parent_row["high_ladder_credit"])
    low_delta = int(child_row["low_repeat_credit"]) - int(parent_row["low_repeat_credit"])
    shortfall = max(0, req_delta - credit_delta)
    return {
        "parent": parent,
        "child": child,
        "child_bit": child_bit,
        "frontier_odd_count": child_leaf.odd_count,
        "frontier_image": child_leaf.image,
        "parent_class": parent_row["class"],
        "child_class": child_row["class"],
        "parent_required": parent_row["max_prefix_required"],
        "child_required": child_row["max_prefix_required"],
        "required_delta": req_delta,
        "parent_credit": parent_row["combined_unit_credit"],
        "child_credit": child_row["combined_unit_credit"],
        "credit_delta": credit_delta,
        "high_credit_delta": high_delta,
        "low_credit_delta": low_delta,
        "delta_shortfall_after_new_credit": shortfall,
        "parent_min_prefix_surplus": parent_row["min_prefix_surplus"],
        "child_min_prefix_surplus": child_row["min_prefix_surplus"],
        "child_prefix_deficit": child_row["max_prefix_deficit"],
        "child_escape_d": child_row["escape_d"],
        "child_max_excess": child_row["max_excess"],
    }


def summarize_rows(rows: list[dict[str, object]]) -> dict[str, object]:
    if not rows:
        return {
            "count": 0,
            "failure_counts": {"uncertified": 0, "prefix_unit": 0},
            "class_counts": {},
            "max_escape": 0,
            "max_excess": 0.0,
            "max_prefix_required": 0,
            "max_prefix_deficit": 0,
        }
    prefix_failures = [row for row in rows if not row["prefix_unit_sufficient"]]
    uncertified = [row for row in rows if not row["certified"]]
    return {
        "count": len(rows),
        "failure_counts": {
            "uncertified": len(uncertified),
            "prefix_unit": len(prefix_failures),
            "high_formula": sum(int(row["high_formula_failure_count"]) for row in rows),
            "high_alignment_burn": sum(int(row["high_alignment_burn_failure_count"]) for row in rows),
            "low_repeat_law": sum(int(row["low_repeat_law_failure_count"]) for row in rows),
        },
        "class_counts": dict(sorted(Counter(str(row["class"]) for row in rows).items())),
        "max_escape": max(int(row["escape_d"]) for row in rows),
        "max_excess": round_float(max(float(row["max_excess"]) for row in rows)),
        "max_prefix_required": max(int(row["max_prefix_required"]) for row in rows),
        "max_prefix_deficit": max(int(row["max_prefix_deficit"]) for row in rows),
        "min_prefix_surplus": min(int(row["min_prefix_surplus"]) for row in rows),
    }


def run(args: argparse.Namespace) -> dict[str, object]:
    started = perf_counter()
    parent_depth = args.parent_depth
    child_depth = parent_depth + 1
    max_depth = max(args.max_depth, child_depth)

    parent_frontier, parent_stats = enumerate_frontier(parent_depth, powers_of_three(max_depth))
    child_frontier, child_stats = enumerate_frontier(child_depth, powers_of_three(max_depth))

    parent_leaves = {leaf.residue: leaf for leaf in parent_frontier if leaf.residue > 1}
    child_leaves = {leaf.residue: leaf for leaf in child_frontier if leaf.residue > 1}
    parent_rows = {residue: analyze_prefix_start(residue, args.max_steps) for residue in sorted(parent_leaves)}

    child_rows: dict[int, dict[str, object]] = {}
    pruned_rows: list[dict[str, object]] = []
    live_records: list[dict[str, object]] = []
    orphan_live_children: list[int] = []
    parent_child_counts: Counter[int] = Counter()
    child_bit_counts: Counter[int] = Counter()
    pruned_child_bit_counts: Counter[int] = Counter()
    transition_counts: Counter[str] = Counter()
    class_transition_counts: Counter[str] = Counter()

    step = 1 << parent_depth
    for parent in sorted(parent_leaves):
        parent_row = parent_rows[parent]
        live_child_count = 0
        for child_bit in (0, 1):
            child = parent + child_bit * step
            if child in child_leaves:
                live_child_count += 1
                child_bit_counts[child_bit] += 1
                child_row = child_rows.get(child)
                if child_row is None:
                    child_row = analyze_prefix_start(child, args.max_steps)
                    child_rows[child] = child_row
                record = transition_record(
                    parent=parent,
                    child=child,
                    child_bit=child_bit,
                    parent_row=parent_row,
                    child_row=child_row,
                    child_leaf=child_leaves[child],
                )
                live_records.append(record)
                class_transition_counts[f"{parent_row['class']}->{child_row['class']}"] += 1

                req_delta = int(record["required_delta"])
                credit_delta = int(record["credit_delta"])
                if req_delta <= 0:
                    transition_counts["nonincreasing_required"] += 1
                else:
                    transition_counts["increased_required"] += 1
                    if credit_delta >= req_delta:
                        transition_counts["increase_paid_by_new_credit"] += 1
                    elif credit_delta > 0:
                        transition_counts["increase_partially_paid_by_new_credit"] += 1
                    else:
                        transition_counts["increase_without_new_credit"] += 1
            else:
                pruned_child_bit_counts[child_bit] += 1
                pruned_rows.append(analyze_prefix_start(child, args.max_steps))
        parent_child_counts[live_child_count] += 1

    for child in sorted(child_leaves):
        parent = child & ((1 << parent_depth) - 1)
        if parent not in parent_leaves:
            orphan_live_children.append(child)

    positive_required_increases = [record for record in live_records if int(record["required_delta"]) > 0]
    credit_shortfalls = [
        record
        for record in positive_required_increases
        if int(record["delta_shortfall_after_new_credit"]) > 0
    ]
    required_delta_signs = Counter(
        "positive" if int(record["required_delta"]) > 0 else "zero" if int(record["required_delta"]) == 0 else "negative"
        for record in live_records
    )
    credit_delta_signs = Counter(
        "positive" if int(record["credit_delta"]) > 0 else "zero" if int(record["credit_delta"]) == 0 else "negative"
        for record in live_records
    )

    return {
        "status": "branch-prefix-lift-transition",
        "elapsed_seconds": round_float(perf_counter() - started, 6),
        "parameters": {
            key: (str(value) if isinstance(value, Path) else value)
            for key, value in vars(args).items()
        },
        "frontiers": {
            "parent": {
                **parent_stats,
                "positive_live_count": len(parent_leaves),
                "depth": parent_depth,
            },
            "child": {
                **child_stats,
                "positive_live_count": len(child_leaves),
                "depth": child_depth,
            },
        },
        "parent_summary": summarize_rows(list(parent_rows.values())),
        "live_child_summary": summarize_rows(list(child_rows.values())),
        "pruned_child_summary": summarize_rows(pruned_rows),
        "lift_summary": {
            "parent_depth": parent_depth,
            "child_depth": child_depth,
            "live_parent_count": len(parent_leaves),
            "live_child_count": len(child_leaves),
            "live_transition_count": len(live_records),
            "pruned_child_count": len(pruned_rows),
            "orphan_live_child_count": len(orphan_live_children),
            "parent_live_child_count_histogram": dict(sorted((str(k), v) for k, v in parent_child_counts.items())),
            "live_child_bit_counts": dict(sorted((str(k), v) for k, v in child_bit_counts.items())),
            "pruned_child_bit_counts": dict(sorted((str(k), v) for k, v in pruned_child_bit_counts.items())),
        },
        "transition_counts": dict(sorted(transition_counts.items())),
        "class_transition_counts": dict(sorted(class_transition_counts.items())),
        "required_delta_histogram": dict(
            sorted((str(k), v) for k, v in Counter(int(record["required_delta"]) for record in live_records).items())
        ),
        "credit_delta_histogram": dict(
            sorted((str(k), v) for k, v in Counter(int(record["credit_delta"]) for record in live_records).items())
        ),
        "required_delta_sign_counts": dict(sorted(required_delta_signs.items())),
        "credit_delta_sign_counts": dict(sorted(credit_delta_signs.items())),
        "max_required_delta": max((int(record["required_delta"]) for record in live_records), default=0),
        "min_required_delta": min((int(record["required_delta"]) for record in live_records), default=0),
        "max_credit_delta": max((int(record["credit_delta"]) for record in live_records), default=0),
        "min_credit_delta": min((int(record["credit_delta"]) for record in live_records), default=0),
        "max_simple_delta_shortfall_all_transitions": max(
            (int(record["delta_shortfall_after_new_credit"]) for record in live_records),
            default=0,
        ),
        "max_positive_required_delta_shortfall_after_new_credit": max(
            (int(record["delta_shortfall_after_new_credit"]) for record in credit_shortfalls),
            default=0,
        ),
        "largest_required_increases": sorted(
            positive_required_increases,
            key=lambda record: (int(record["required_delta"]), float(record["child_max_excess"]), int(record["child"])),
            reverse=True,
        )[: args.top_n],
        "largest_credit_shortfalls": sorted(
            credit_shortfalls,
            key=lambda record: (
                int(record["delta_shortfall_after_new_credit"]),
                int(record["required_delta"]),
                float(record["child_max_excess"]),
                int(record["child"]),
            ),
            reverse=True,
        )[: args.top_n],
        "largest_child_excess": sorted(
            live_records,
            key=lambda record: (float(record["child_max_excess"]), int(record["child"])),
            reverse=True,
        )[: args.top_n],
        "longest_child_escape": sorted(
            live_records,
            key=lambda record: (int(record["child_escape_d"]), int(record["child"])),
            reverse=True,
        )[: args.top_n],
        "sample_orphan_live_children": orphan_live_children[: args.top_n],
        "interpretation": (
            "Finite parent-child transition audit. Required-delta increases "
            "not paid by new credit are not proof failures when prefix deficits "
            "remain zero; they mark where a proof needs inherited buffer or a "
            "more local event-timing argument."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--parent-depth", type=int, default=25)
    parser.add_argument("--max-depth", type=int, default=1024)
    parser.add_argument("--max-steps", type=int, default=50000)
    parser.add_argument("--top-n", type=int, default=12)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--quiet", action="store_true")
    args = parser.parse_args()

    if args.parent_depth < 1:
        raise SystemExit("--parent-depth must be positive")
    if args.max_depth < args.parent_depth + 1:
        raise SystemExit("--max-depth must be at least --parent-depth + 1")
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

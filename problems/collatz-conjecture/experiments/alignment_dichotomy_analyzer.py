#!/usr/bin/env python3
"""Test the low-alignment / high-alignment descent dichotomy.

The kick-repulsion audit found a real gap: some starts descend quickly with
`max_align <= 2`, so counted high-alignment repulsions cannot be the whole
proof mechanism.

This script tests the repaired theorem shape:

* low-alignment branch: if no odd iterate gets close to `-1 mod 8`, descent
  should happen quickly;
* high-alignment branch: if the orbit does align near `-1`, the existing
  kick/carry repulsion accounting should pay the excess debt.

This is finite evidence, not a proof.  Its purpose is to turn a broken
"repulsion alone" claim into a falsifiable two-branch lemma.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path
from time import perf_counter

from kick_repulsion_claim_audit import (
    TRANSFER_FAILURE_STARTS,
    starts_from_frontier,
    top_rows,
    unique_preserving_order,
)
from master_kick_rejection_lemma import GAMMA_CEIL, get_hard_records, simulate_kick_repulsion
from repayment_envelope_scan import parse_ints, round_float
from terminal_residue_tree_sweep_analyzer import parse_offset_set


def alignment_class(max_align: int, high_threshold: int) -> str:
    if max_align < high_threshold:
        return "low-alignment"
    return "high-alignment"


def stats(rows: list[dict[str, object]]) -> dict[str, object]:
    if not rows:
        return {
            "count": 0,
            "all_certified": True,
            "all_repulsions_sufficient": True,
            "escape_max": None,
            "steps_per_bit_max": None,
        }
    escapes = [int(row["escape_d"]) for row in rows]
    ratios = [float(row["steps_per_bit"]) for row in rows]
    max_aligns = [int(row["max_align"]) for row in rows]
    max_excesses = [float(row["max_excess"]) for row in rows]
    return {
        "count": len(rows),
        "all_certified": all(bool(row["certified"]) for row in rows),
        "all_repulsions_sufficient": all(bool(row["repulsions_sufficient"]) for row in rows),
        "certified_count": sum(1 for row in rows if row["certified"]),
        "repulsions_sufficient_count": sum(1 for row in rows if row["repulsions_sufficient"]),
        "escape_min": min(escapes),
        "escape_max": max(escapes),
        "escape_avg": round_float(sum(escapes) / len(escapes)),
        "steps_per_bit_min": round_float(min(ratios)),
        "steps_per_bit_max": round_float(max(ratios)),
        "steps_per_bit_avg": round_float(sum(ratios) / len(ratios)),
        "max_align_min": min(max_aligns),
        "max_align_max": max(max_aligns),
        "max_excess_max": round_float(max(max_excesses)),
        "max_excess_avg": round_float(sum(max_excesses) / len(max_excesses)),
    }


def bound_violations(
    rows: list[dict[str, object]],
    *,
    slope: float,
    additive: float,
) -> list[dict[str, object]]:
    out = []
    for row in rows:
        if int(row["escape_d"]) > slope * int(row["b"]) + additive:
            out.append(row)
    return out


def run(args: argparse.Namespace) -> dict[str, object]:
    started = perf_counter()
    frontier_offsets = parse_offset_set(
        args.frontier_sample_offsets,
        args.frontier_sample_stride,
        default=[
            0,
            args.frontier_sample_stride // 4,
            args.frontier_sample_stride // 2,
            (3 * args.frontier_sample_stride) // 4,
        ],
    )
    explicit_starts = parse_ints(args.starts)
    frontier_starts, frontier_meta = starts_from_frontier(
        base_depth=args.frontier_base_depth,
        max_depth=args.frontier_max_depth,
        sample_stride=args.frontier_sample_stride,
        sample_offsets=frontier_offsets,
        max_frontier=args.frontier_max_frontier,
    )

    groups = {
        "initial_scan": list(range(2, args.limit_scan + 1)),
        "hard_records": get_hard_records(),
        "transfer_failure_starts": TRANSFER_FAILURE_STARTS,
        "sampled_frontier_shadows": frontier_starts,
        "explicit_starts": explicit_starts,
    }

    rows: list[dict[str, object]] = []
    by_group: dict[str, list[dict[str, object]]] = defaultdict(list)
    by_alignment: dict[str, list[dict[str, object]]] = defaultdict(list)
    by_group_alignment: dict[str, list[dict[str, object]]] = defaultdict(list)

    for group_name, starts in groups.items():
        for start in unique_preserving_order(starts):
            row = simulate_kick_repulsion(start, max_steps=args.max_steps)
            row["group"] = group_name
            row["alignment_class"] = alignment_class(int(row["max_align"]), args.high_alignment_threshold)
            rows.append(row)
            by_group[group_name].append(row)
            by_alignment[row["alignment_class"]].append(row)
            by_group_alignment[f"{group_name}:{row['alignment_class']}"].append(row)

    low_rows = by_alignment["low-alignment"]
    high_rows = by_alignment["high-alignment"]
    low_violations = bound_violations(
        low_rows,
        slope=args.low_alignment_slope,
        additive=args.low_alignment_additive,
    )
    gamma_violations = bound_violations(rows, slope=args.gamma_slope, additive=args.gamma_additive)
    high_repulsion_failures = [row for row in high_rows if not row["repulsions_sufficient"]]
    uncertified = [row for row in rows if not row["certified"]]

    return {
        "status": "alignment-dichotomy-analysis",
        "elapsed_seconds": round_float(perf_counter() - started, 6),
        "parameters": {
            "limit_scan": args.limit_scan,
            "max_steps": args.max_steps,
            "frontier_base_depth": args.frontier_base_depth,
            "frontier_max_depth": args.frontier_max_depth,
            "frontier_sample_stride": args.frontier_sample_stride,
            "frontier_sample_offsets": frontier_offsets,
            "frontier_max_frontier": args.frontier_max_frontier,
            "high_alignment_threshold": args.high_alignment_threshold,
            "low_alignment_slope": args.low_alignment_slope,
            "low_alignment_additive": args.low_alignment_additive,
            "gamma_slope": args.gamma_slope,
            "gamma_additive": args.gamma_additive,
        },
        "frontier_selection": frontier_meta,
        "total_checked": len(rows),
        "alignment_histogram": dict(sorted(Counter(row["alignment_class"] for row in rows).items())),
        "group_stats": {name: stats(members) for name, members in sorted(by_group.items())},
        "alignment_stats": {name: stats(members) for name, members in sorted(by_alignment.items())},
        "group_alignment_stats": {name: stats(members) for name, members in sorted(by_group_alignment.items())},
        "dichotomy_checks": {
            "uncertified_count": len(uncertified),
            "uncertified": top_rows(uncertified, "escape_d", args.top_n),
            "global_gamma_bound_violation_count": len(gamma_violations),
            "global_gamma_bound_violations": top_rows(gamma_violations, "escape_d", args.top_n),
            "low_alignment_bound": {
                "slope": args.low_alignment_slope,
                "additive": args.low_alignment_additive,
                "violation_count": len(low_violations),
                "violations": top_rows(low_violations, "steps_per_bit", args.top_n),
            },
            "high_alignment_repulsion_failure_count": len(high_repulsion_failures),
            "high_alignment_repulsion_failures": top_rows(high_repulsion_failures, "max_excess", args.top_n),
        },
        "worst_low_alignment_by_ratio": top_rows(low_rows, "steps_per_bit", args.top_n),
        "worst_low_alignment_by_escape": top_rows(low_rows, "escape_d", args.top_n),
        "worst_high_alignment_by_ratio": top_rows(high_rows, "steps_per_bit", args.top_n),
        "largest_high_alignment_repulsion_counts": top_rows(high_rows, "num_repulsions", args.top_n),
        "interpretation": (
            "The repaired proof target is a dichotomy: low-alignment branches must "
            "have a direct quick-descent/potential-drop proof, while high-alignment "
            "branches are eligible for the kick/carry repulsion lemma."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit-scan", type=int, default=1000000)
    parser.add_argument("--max-steps", type=int, default=20000)
    parser.add_argument("--frontier-base-depth", type=int, default=28)
    parser.add_argument("--frontier-max-depth", type=int, default=1024)
    parser.add_argument("--frontier-sample-stride", type=int, default=1024)
    parser.add_argument("--frontier-sample-offsets", nargs="+")
    parser.add_argument("--frontier-max-frontier", type=int)
    parser.add_argument("--starts", nargs="*")
    parser.add_argument("--high-alignment-threshold", type=int, default=3)
    parser.add_argument("--low-alignment-slope", type=float, default=2.0)
    parser.add_argument("--low-alignment-additive", type=float, default=16.0)
    parser.add_argument("--gamma-slope", type=float, default=GAMMA_CEIL)
    parser.add_argument("--gamma-additive", type=float, default=32.0)
    parser.add_argument("--top-n", type=int, default=12)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--quiet", action="store_true")
    args = parser.parse_args()

    if args.limit_scan < 2:
        raise SystemExit("--limit-scan must be >= 2")
    if args.max_steps < 1:
        raise SystemExit("--max-steps must be positive")
    if args.frontier_base_depth < 1:
        raise SystemExit("--frontier-base-depth must be positive")
    if args.frontier_max_depth < 1:
        raise SystemExit("--frontier-max-depth must be positive")
    if args.frontier_sample_stride < 1:
        raise SystemExit("--frontier-sample-stride must be positive")
    if args.high_alignment_threshold < 1:
        raise SystemExit("--high-alignment-threshold must be positive")
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

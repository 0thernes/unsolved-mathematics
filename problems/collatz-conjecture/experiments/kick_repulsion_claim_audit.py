#!/usr/bin/env python3
"""Audit the positive-kick repulsion proof claim.

Several adjacent notes claim that the Collatz conjecture is resolved by a
"positive kick repulsion" mechanism.  The claim is interesting, but a finite
experiment is not a proof.  This audit does two things:

* stress-test the executable repulsion definition on ordinary starts, hard
  records, sampled frontier shadows, and known transfer-failure starts;
* separate empirical checks from the missing universal proof obligations.

If a checked bound fails, the script reports the concrete counterexample.  If
no checked bound fails, it still reports the theorem obligations that remain
unproved before any "Collatz solved" claim is defensible.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path
from time import perf_counter
from typing import Iterable

from master_kick_rejection_lemma import GAMMA_CEIL, get_hard_records, simulate_kick_repulsion
from repayment_envelope_scan import parse_ints, round_float
from terminal_residue_tree_sweep_analyzer import frontier_partitions, parse_offset_set


TRANSFER_FAILURE_STARTS = [
    350770415,
    396162791,
    445000795,
    475203487,
    516172255,
    386531023,
    527881499,
    409596671,
    461361359,
    471717535,
    184427291,
    228350399,
    262955455,
    194843463,
    175854063,
]


def unique_preserving_order(values: Iterable[int]) -> list[int]:
    seen: set[int] = set()
    ordered: list[int] = []
    for value in values:
        if value in seen or value < 2:
            continue
        seen.add(value)
        ordered.append(value)
    return ordered


def starts_from_frontier(
    *,
    base_depth: int,
    max_depth: int,
    sample_stride: int,
    sample_offsets: list[int],
    max_frontier: int | None,
) -> tuple[list[int], dict[str, object]]:
    partitions, meta = frontier_partitions(
        base_depth=base_depth,
        max_depth=max_depth,
        stride=sample_stride,
        max_frontier=max_frontier,
    )
    starts: list[int] = []
    per_offset = {}
    for offset in sample_offsets:
        values = partitions[offset]
        starts.extend(values)
        per_offset[str(offset)] = len(values)
    return unique_preserving_order(starts), {**meta, "sample_offsets": sample_offsets, "per_offset_count": per_offset}


def group_stats(rows: list[dict[str, object]]) -> dict[str, object]:
    if not rows:
        return {
            "count": 0,
            "all_certified": True,
            "all_repulsions_sufficient": True,
            "max_steps_per_bit": None,
            "max_escape_depth": None,
        }
    ratios = [float(row["steps_per_bit"]) for row in rows]
    escapes = [int(row["escape_d"]) for row in rows]
    repulsions = [int(row["num_repulsions"]) for row in rows]
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
        "repulsions_min": min(repulsions),
        "repulsions_max": max(repulsions),
        "repulsions_avg": round_float(sum(repulsions) / len(repulsions)),
    }


def top_rows(rows: list[dict[str, object]], key: str, top_n: int) -> list[dict[str, object]]:
    return sorted(rows, key=lambda row: (row[key], row["start"]), reverse=True)[:top_n]


def check_bounds(
    rows: list[dict[str, object]],
    *,
    gamma_slope: float,
    gamma_additive: float,
    better_slope: float,
    better_additive: float,
) -> dict[str, object]:
    gamma_violations = []
    better_violations = []
    sufficiency_failures = []
    uncertified = []

    for row in rows:
        escape_depth = int(row["escape_d"])
        bit_length = int(row["b"])
        if escape_depth > gamma_slope * bit_length + gamma_additive:
            gamma_violations.append(row)
        if escape_depth > better_slope * bit_length + better_additive:
            better_violations.append(row)
        if not row["repulsions_sufficient"]:
            sufficiency_failures.append(row)
        if not row["certified"]:
            uncertified.append(row)

    return {
        "gamma_bound": {
            "slope": gamma_slope,
            "additive": gamma_additive,
            "violation_count": len(gamma_violations),
            "largest_violations": top_rows(gamma_violations, "escape_d", 10),
        },
        "better_bound": {
            "slope": better_slope,
            "additive": better_additive,
            "violation_count": len(better_violations),
            "largest_violations": top_rows(better_violations, "escape_d", 10),
        },
        "repulsion_sufficiency_failure_count": len(sufficiency_failures),
        "repulsion_sufficiency_failures": top_rows(sufficiency_failures, "max_excess", 10),
        "uncertified_count": len(uncertified),
        "uncertified": top_rows(uncertified, "escape_d", 10),
    }


def run_audit(args: argparse.Namespace) -> dict[str, object]:
    started = perf_counter()
    frontier_offsets = parse_offset_set(
        args.frontier_sample_offsets,
        args.frontier_sample_stride,
        default=[0, args.frontier_sample_stride // 4, args.frontier_sample_stride // 2, (3 * args.frontier_sample_stride) // 4],
    )
    explicit_starts = parse_ints(args.starts)

    groups: dict[str, list[int]] = {
        "initial_scan": list(range(2, args.limit_scan + 1)),
        "hard_records": get_hard_records(),
        "transfer_failure_starts": TRANSFER_FAILURE_STARTS,
        "explicit_starts": explicit_starts,
    }
    frontier_starts, frontier_meta = starts_from_frontier(
        base_depth=args.frontier_base_depth,
        max_depth=args.frontier_max_depth,
        sample_stride=args.frontier_sample_stride,
        sample_offsets=frontier_offsets,
        max_frontier=args.frontier_max_frontier,
    )
    groups["sampled_frontier_shadows"] = frontier_starts

    rows: list[dict[str, object]] = []
    group_rows: dict[str, list[dict[str, object]]] = defaultdict(list)
    for group_name, starts in groups.items():
        for start in unique_preserving_order(starts):
            row = simulate_kick_repulsion(start, max_steps=args.max_steps)
            row["group"] = group_name
            rows.append(row)
            group_rows[group_name].append(row)

    status_counts = Counter()
    status_counts["certified"] = sum(1 for row in rows if row["certified"])
    status_counts["uncertified"] = len(rows) - status_counts["certified"]
    status_counts["repulsions_sufficient"] = sum(1 for row in rows if row["repulsions_sufficient"])
    status_counts["repulsions_insufficient"] = len(rows) - status_counts["repulsions_sufficient"]

    bound_checks = check_bounds(
        rows,
        gamma_slope=args.gamma_slope,
        gamma_additive=args.gamma_additive,
        better_slope=args.better_slope,
        better_additive=args.better_additive,
    )
    empirical_counterexample_count = (
        bound_checks["gamma_bound"]["violation_count"]
        + bound_checks["repulsion_sufficiency_failure_count"]
        + bound_checks["uncertified_count"]
    )

    return {
        "status": "kick-repulsion-claim-audit",
        "elapsed_seconds": round_float(perf_counter() - started, 6),
        "parameters": {
            "limit_scan": args.limit_scan,
            "max_steps": args.max_steps,
            "frontier_base_depth": args.frontier_base_depth,
            "frontier_max_depth": args.frontier_max_depth,
            "frontier_sample_stride": args.frontier_sample_stride,
            "frontier_sample_offsets": frontier_offsets,
            "frontier_max_frontier": args.frontier_max_frontier,
            "gamma_slope": args.gamma_slope,
            "gamma_additive": args.gamma_additive,
            "better_slope": args.better_slope,
            "better_additive": args.better_additive,
        },
        "frontier_selection": frontier_meta,
        "group_stats": {group: group_stats(members) for group, members in sorted(group_rows.items())},
        "total_checked": len(rows),
        "status_counts": dict(sorted(status_counts.items())),
        "bound_checks": bound_checks,
        "worst_by_steps_per_bit": top_rows(rows, "steps_per_bit", args.top_n),
        "worst_by_escape_depth": top_rows(rows, "escape_d", args.top_n),
        "largest_repulsion_counts": top_rows(rows, "num_repulsions", args.top_n),
        "audit_conclusion": {
            "empirical_counterexample_found": empirical_counterexample_count > 0,
            "empirical_counterexample_count": empirical_counterexample_count,
            "finite_evidence_summary": (
                "No checked gamma-bound, certification, or repulsion-sufficiency failure was found."
                if empirical_counterexample_count == 0
                else "At least one checked finite subclaim failed; inspect bound_checks."
            ),
            "proof_claim_status": "not-proved",
            "reason": (
                "The script only checks finitely many starts. The universal positive-kick repulsion lemma, "
                "the lower bound turning alignment into forced even insertions, the induction on bit length, "
                "and the summable cross-depth grammar-growth bound remain mathematical obligations."
            ),
            "remaining_obligations": [
                "Formalize the exact 2-adic carry lemma: alignment plus positive affine defect forces a quantified even insertion.",
                "Prove a uniform lower bound on repulsion frequency for every positive frontier shadow, not only sampled starts.",
                "Show repulsion decreases the relevant excess/potential monotonically enough to imply certificate descent.",
                "Close the induction from finite-bit support to all bit lengths with explicit constants.",
                "Integrate sibling controls so the proof consumes the epsilon=+1 intercept sign and cannot also prove false siblings.",
            ],
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit-scan", type=int, default=200000)
    parser.add_argument("--max-steps", type=int, default=20000)
    parser.add_argument("--frontier-base-depth", type=int, default=28)
    parser.add_argument("--frontier-max-depth", type=int, default=1024)
    parser.add_argument("--frontier-sample-stride", type=int, default=2048)
    parser.add_argument("--frontier-sample-offsets", nargs="+")
    parser.add_argument("--frontier-max-frontier", type=int)
    parser.add_argument("--starts", nargs="*")
    parser.add_argument("--gamma-slope", type=float, default=GAMMA_CEIL)
    parser.add_argument("--gamma-additive", type=float, default=32.0)
    parser.add_argument("--better-slope", type=float, default=14.56)
    parser.add_argument("--better-additive", type=float, default=32.0)
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
    if args.top_n < 1:
        raise SystemExit("--top-n must be positive")

    payload = run_audit(args)
    text = json.dumps(payload, indent=2, sort_keys=True)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text + "\n", encoding="utf-8")
    if not args.quiet:
        print(text)


if __name__ == "__main__":
    main()

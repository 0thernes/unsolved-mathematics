#!/usr/bin/env python3
"""Adversarial stress tests for the branch-potential ledger.

The baseline branch-potential run checks the inherited million-start
population.  This script tries to break the candidate inequality by generating
starts that deliberately sit on the two exact grammar boundaries:

* low repeat spines:  x = 2^h*q - 5, h >= 6, q odd;
* high ladders:       x = 2^a*q - 1, a >= 3, q odd;
* fresh frontier-shadow slices not used by the baseline run;
* high-bit random and near-boundary starts.

It reports the worst deficit `R - C_unit`.  Positive deficit means a concrete
counterexample to the proposed finite branch-potential ledger.
"""

from __future__ import annotations

import argparse
import json
import random
import sys
from collections import Counter, defaultdict
from pathlib import Path
from time import perf_counter

sys.path.insert(0, str(Path(__file__).resolve().parent))

from branch_potential_analyzer import (
    analyze_start,
    get_hard_records,
    parse_ints,
    parse_offset_set,
    round_float,
    starts_from_frontier,
    summarize,
    unique_preserving_order,
)


def odd_q_values(max_q: int) -> list[int]:
    fixed = [1, 3, 5, 7, 9, 15, 21, 31, 43, 63, 85, 127, 255, 511, 1023]
    values = [q for q in fixed if q <= max_q and q % 2 == 1]
    for q in range(1, max_q + 1, 2):
        if q not in values:
            values.append(q)
    return values


def low_repeat_spines(max_h: int, max_q: int) -> list[int]:
    starts = []
    for h in range(6, max_h + 1):
        for q in odd_q_values(max_q):
            starts.append((1 << h) * q - 5)
    return starts


def high_ladder_spines(max_a: int, max_q: int) -> list[int]:
    starts = []
    for a in range(3, max_a + 1):
        for q in odd_q_values(max_q):
            starts.append((1 << a) * q - 1)
    return starts


def near_boundaries(max_bits: int, width: int) -> list[int]:
    starts = []
    for bits in range(8, max_bits + 1):
        base = 1 << bits
        for delta in range(1, width + 1, 2):
            starts.append(base - delta)
            starts.append(base + delta)
        starts.append(base - 5)
    return [n for n in starts if n > 1]


def random_high_bit(count: int, min_bits: int, max_bits: int, seed: int) -> list[int]:
    rng = random.Random(seed)
    starts = []
    for _ in range(count):
        bits = rng.randint(min_bits, max_bits)
        n = (1 << (bits - 1)) | rng.getrandbits(bits - 1) | 1
        starts.append(n)
    return starts


def biased_boundary_random(count: int, max_bits: int, seed: int) -> list[int]:
    rng = random.Random(seed ^ 0xBAD5EED)
    starts = []
    for _ in range(count):
        bits = rng.randint(12, max_bits)
        mode = rng.choice(["low", "high"])
        align = rng.randint(3 if mode == "high" else 6, min(max_bits - 2, 96))
        q_bits = max(1, bits - align)
        q = rng.getrandbits(q_bits) | 1
        if mode == "high":
            starts.append((1 << align) * q - 1)
        else:
            starts.append((1 << align) * q - 5)
    return [n for n in starts if n > 1]


def build_groups(args: argparse.Namespace) -> tuple[dict[str, list[int]], dict[str, object]]:
    frontier_offsets = parse_offset_set(
        args.frontier_sample_offsets,
        args.frontier_sample_stride,
        default=[
            args.frontier_sample_stride // 8,
            (3 * args.frontier_sample_stride) // 8,
            (5 * args.frontier_sample_stride) // 8,
            (7 * args.frontier_sample_stride) // 8,
        ],
    )
    frontier_starts, frontier_meta = starts_from_frontier(
        base_depth=args.frontier_base_depth,
        max_depth=args.frontier_max_depth,
        sample_stride=args.frontier_sample_stride,
        sample_offsets=frontier_offsets,
        max_frontier=args.frontier_max_frontier,
    )
    groups = {
        "hard_records": get_hard_records(),
        "low_repeat_spines": low_repeat_spines(args.low_max_h, args.max_q),
        "high_ladder_spines": high_ladder_spines(args.high_max_a, args.max_q),
        "near_boundaries": near_boundaries(args.max_bits, args.boundary_width),
        "random_high_bit": random_high_bit(args.random_count, args.random_min_bits, args.max_bits, args.seed),
        "biased_boundary_random": biased_boundary_random(args.biased_count, args.max_bits, args.seed),
        "fresh_frontier_shadows": frontier_starts,
        "explicit_starts": parse_ints(args.starts),
    }
    return groups, {**frontier_meta, "sample_offsets": frontier_offsets}


def run(args: argparse.Namespace) -> dict[str, object]:
    started = perf_counter()
    groups, frontier_meta = build_groups(args)
    rows: list[dict[str, object]] = []
    by_group: dict[str, list[dict[str, object]]] = defaultdict(list)
    by_class: dict[str, list[dict[str, object]]] = defaultdict(list)

    for group_name, starts in groups.items():
        for start in unique_preserving_order(starts):
            row = analyze_start(start, args.max_steps)
            row["group"] = group_name
            row["unit_credit_deficit"] = int(row["min_credit_required"]) - int(row["combined_unit_credit"])
            row["rank_credit_deficit"] = int(row["min_credit_required"]) - int(row["combined_rank_credit"])
            rows.append(row)
            by_group[group_name].append(row)
            by_class[str(row["class"])].append(row)

    unit_failures = [row for row in rows if int(row["unit_credit_deficit"]) > 0]
    rank_failures = [row for row in rows if int(row["rank_credit_deficit"]) > 0]
    uncertified = [row for row in rows if not row["certified"]]

    return {
        "status": "branch-potential-stress",
        "elapsed_seconds": round_float(perf_counter() - started, 6),
        "parameters": {
            key: (str(value) if isinstance(value, Path) else value)
            for key, value in vars(args).items()
        },
        "frontier_selection": frontier_meta,
        "total_checked": len(rows),
        "class_counts": dict(sorted(Counter(str(row["class"]) for row in rows).items())),
        "group_counts": {name: len(members) for name, members in sorted(by_group.items())},
        "group_summaries": {name: summarize(members) for name, members in sorted(by_group.items())},
        "class_summaries": {name: summarize(members) for name, members in sorted(by_class.items())},
        "failure_counts": {
            "uncertified": len(uncertified),
            "unit_credit": len(unit_failures),
            "rank_credit": len(rank_failures),
        },
        "max_unit_credit_deficit": max((int(row["unit_credit_deficit"]) for row in rows), default=0),
        "max_rank_credit_deficit": max((int(row["rank_credit_deficit"]) for row in rows), default=0),
        "min_unit_credit_surplus": min((int(row["unit_credit_surplus"]) for row in rows), default=0),
        "min_rank_credit_surplus": min((int(row["rank_credit_surplus"]) for row in rows), default=0),
        "largest_unit_failures": sorted(
            unit_failures,
            key=lambda row: (int(row["unit_credit_deficit"]), float(row["max_excess"])),
            reverse=True,
        )[: args.top_n],
        "largest_rank_failures": sorted(
            rank_failures,
            key=lambda row: (int(row["rank_credit_deficit"]), float(row["max_excess"])),
            reverse=True,
        )[: args.top_n],
        "tightest_unit_surplus": sorted(
            rows,
            key=lambda row: (int(row["unit_credit_surplus"]), -float(row["max_excess"])),
        )[: args.top_n],
        "largest_excess": sorted(rows, key=lambda row: (float(row["max_excess"]), int(row["start"])), reverse=True)[
            : args.top_n
        ],
        "largest_escape": sorted(rows, key=lambda row: (int(row["escape_d"]), int(row["start"])), reverse=True)[
            : args.top_n
        ],
        "interpretation": (
            "Adversarial finite stress test. A positive max_unit_credit_deficit "
            "would falsify the proposed C_unit >= R finite ledger. Zero failures "
            "are evidence only and do not prove the universal theorem."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-steps", type=int, default=50000)
    parser.add_argument("--low-max-h", type=int, default=96)
    parser.add_argument("--high-max-a", type=int, default=96)
    parser.add_argument("--max-q", type=int, default=63)
    parser.add_argument("--max-bits", type=int, default=160)
    parser.add_argument("--boundary-width", type=int, default=63)
    parser.add_argument("--random-count", type=int, default=2000)
    parser.add_argument("--random-min-bits", type=int, default=32)
    parser.add_argument("--biased-count", type=int, default=2000)
    parser.add_argument("--seed", type=int, default=20260702)
    parser.add_argument("--frontier-base-depth", type=int, default=28)
    parser.add_argument("--frontier-max-depth", type=int, default=1024)
    parser.add_argument("--frontier-sample-stride", type=int, default=1024)
    parser.add_argument("--frontier-sample-offsets", nargs="+")
    parser.add_argument("--frontier-max-frontier", type=int)
    parser.add_argument("--starts", nargs="*")
    parser.add_argument("--top-n", type=int, default=12)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--quiet", action="store_true")
    args = parser.parse_args()

    if args.max_steps < 1:
        raise SystemExit("--max-steps must be positive")
    if args.low_max_h < 6:
        raise SystemExit("--low-max-h must be >= 6")
    if args.high_max_a < 3:
        raise SystemExit("--high-max-a must be >= 3")
    if args.max_q < 1:
        raise SystemExit("--max-q must be positive")
    if args.max_bits < 12:
        raise SystemExit("--max-bits must be >= 12")
    if args.random_min_bits < 2 or args.random_min_bits > args.max_bits:
        raise SystemExit("--random-min-bits must be between 2 and --max-bits")
    if args.frontier_base_depth < 1:
        raise SystemExit("--frontier-base-depth must be positive")
    if args.frontier_max_depth < 1:
        raise SystemExit("--frontier-max-depth must be positive")
    if args.frontier_sample_stride < 1:
        raise SystemExit("--frontier-sample-stride must be positive")
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

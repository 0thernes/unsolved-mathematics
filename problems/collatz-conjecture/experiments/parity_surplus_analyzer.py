#!/usr/bin/env python3
"""Analyze parity-surplus structure behind hard Collatz certificate examples.

For the shortcut map, a depth-d prefix survives the multiplier descent test
exactly when

    3^o >= 2^d,

where o is the number of odd shortcut steps in the first d steps.  Equivalently
o is at least the exact integer boundary

    min_o(d) = min { o : 3^o >= 2^d }.

This script profiles hard positive starts against that boundary.  It is meant
to identify structural proof targets: do hard starts cling to the critical
line, accumulate bounded surplus, or escape by another mechanism?
"""

from __future__ import annotations

import argparse
import json
import math
from collections import Counter
from dataclasses import dataclass
from statistics import mean

from certificate_depth_scan import certificate_for_start, total_stopping_profile
from collatz_residue_lab import shortcut


LOG2_3 = math.log2(3)


@dataclass(frozen=True)
class RunSummary:
    bit: int
    length: int

    def as_dict(self) -> dict[str, int]:
        return {"bit": self.bit, "length": self.length}


def powers_of_three(max_depth: int) -> list[int]:
    pow3 = [1]
    for _ in range(max_depth):
        pow3.append(pow3[-1] * 3)
    return pow3


def min_surviving_odd_counts(max_depth: int, pow3: list[int]) -> list[int]:
    """Return m[d] = least o with 3^o >= 2^d, exactly."""
    counts = [0]
    odd_count = 0
    for depth in range(1, max_depth + 1):
        target = 1 << depth
        while pow3[odd_count] < target:
            odd_count += 1
        counts.append(odd_count)
    return counts


def run_summaries(bits: list[int]) -> list[RunSummary]:
    if not bits:
        return []
    runs: list[RunSummary] = []
    current = bits[0]
    length = 1
    for bit in bits[1:]:
        if bit == current:
            length += 1
            continue
        runs.append(RunSummary(current, length))
        current = bit
        length = 1
    runs.append(RunSummary(current, length))
    return runs


def longest_streak(flags: list[bool]) -> int:
    best = 0
    current = 0
    for flag in flags:
        if flag:
            current += 1
            best = max(best, current)
        else:
            current = 0
    return best


def analyze_start(
    start: int,
    max_depth: int,
    certificate_search_depth: int,
    corridor_width: int,
    sample_limit: int,
) -> dict[str, object]:
    pow3 = powers_of_three(max(certificate_search_depth, max_depth))
    cert = certificate_for_start(start, certificate_search_depth, pow3)
    if cert["certified"] and max_depth <= 0:
        depth_limit = int(cert["depth"])
    elif max_depth > 0:
        depth_limit = max_depth
    else:
        depth_limit = certificate_search_depth

    min_odd = min_surviving_odd_counts(depth_limit, pow3)
    mechanical_bits = [min_odd[depth] - min_odd[depth - 1] for depth in range(1, depth_limit + 1)]

    x = start
    odd_count = 0
    parity_bits: list[int] = []
    excess_values: list[int] = []
    margin_bits_values: list[float] = []
    image_ratios_log2: list[float] = []
    first_multiplier_contract_depth: int | None = None
    first_below_start_depth: int | None = None
    boundary_touch_depths: list[int] = []
    corridor_flags: list[bool] = []
    negative_excess_depths: list[int] = []
    prefix_samples: list[dict[str, int | float | bool]] = []

    for depth in range(1, depth_limit + 1):
        was_odd = x & 1
        parity_bits.append(was_odd)
        odd_count += was_odd
        x = shortcut(x)

        excess = odd_count - min_odd[depth]
        margin_bits = odd_count * LOG2_3 - depth
        ratio_log2 = math.log2(x) - math.log2(start) if x > 0 and start > 0 else float("-inf")
        excess_values.append(excess)
        margin_bits_values.append(margin_bits)
        image_ratios_log2.append(ratio_log2)

        if first_multiplier_contract_depth is None and pow3[odd_count] < (1 << depth):
            first_multiplier_contract_depth = depth
        if first_below_start_depth is None and x < start:
            first_below_start_depth = depth
        if excess == 0:
            boundary_touch_depths.append(depth)
        if excess < 0:
            negative_excess_depths.append(depth)
        corridor_flags.append(0 <= excess <= corridor_width)

        if (
            depth <= sample_limit
            or depth == depth_limit
            or depth == first_multiplier_contract_depth
            or depth == first_below_start_depth
            or len(boundary_touch_depths) <= sample_limit and excess == 0
        ):
            prefix_samples.append(
                {
                    "depth": depth,
                    "parity_bit": was_odd,
                    "odd_count": odd_count,
                    "min_surviving_odd_count": min_odd[depth],
                    "excess": excess,
                    "surplus_margin_bits": round(margin_bits, 9),
                    "image_log2_ratio_to_start": round(ratio_log2, 9),
                    "multiplier_contracts": pow3[odd_count] < (1 << depth),
                    "below_start": x < start,
                }
            )

    runs = run_summaries(parity_bits)
    run_histogram = Counter((run.bit, run.length) for run in runs)
    hamming_to_mechanical = sum(1 for a, b in zip(parity_bits, mechanical_bits) if a != b)
    excess_counter = Counter(excess_values)
    max_excess = max(excess_values) if excess_values else 0
    min_excess = min(excess_values) if excess_values else 0
    final_excess = excess_values[-1] if excess_values else 0
    profile = total_stopping_profile(start, max(10000, depth_limit * 4))

    return {
        "start": start,
        "bit_length": start.bit_length(),
        "depth_limit": depth_limit,
        "certificate": cert,
        "profile": profile,
        "first_multiplier_contract_depth": first_multiplier_contract_depth,
        "first_below_start_depth": first_below_start_depth,
        "critical_line": {
            "definition": "min_surviving_odd_count[d] is the least o with 3^o >= 2^d",
            "final_min_surviving_odd_count": min_odd[-1] if min_odd else 0,
            "final_odd_count": odd_count,
            "final_excess": final_excess,
            "min_excess": min_excess,
            "max_excess": max_excess,
            "mean_excess": round(mean(excess_values), 6) if excess_values else 0,
            "boundary_touch_count": len(boundary_touch_depths),
            "boundary_touch_depth_samples": boundary_touch_depths[:sample_limit],
            "negative_excess_first_depth": negative_excess_depths[0] if negative_excess_depths else None,
            "longest_corridor_streak": longest_streak(corridor_flags),
            "corridor_width": corridor_width,
            "excess_histogram": {str(k): excess_counter[k] for k in sorted(excess_counter)},
        },
        "surplus_margin_bits": {
            "min": round(min(margin_bits_values), 9) if margin_bits_values else 0,
            "max": round(max(margin_bits_values), 9) if margin_bits_values else 0,
            "final": round(margin_bits_values[-1], 9) if margin_bits_values else 0,
        },
        "image_ratio_log2": {
            "max": round(max(image_ratios_log2), 9) if image_ratios_log2 else 0,
            "final": round(image_ratios_log2[-1], 9) if image_ratios_log2 else 0,
        },
        "parity_structure": {
            "ones": odd_count,
            "zeros": depth_limit - odd_count,
            "ones_ratio": round(odd_count / depth_limit, 9) if depth_limit else 0,
            "mechanical_hamming_distance": hamming_to_mechanical,
            "mechanical_hamming_ratio": round(hamming_to_mechanical / depth_limit, 9) if depth_limit else 0,
            "run_count": len(runs),
            "longest_odd_run": max((run.length for run in runs if run.bit == 1), default=0),
            "longest_even_run": max((run.length for run in runs if run.bit == 0), default=0),
            "first_runs": [run.as_dict() for run in runs[:sample_limit]],
            "last_runs": [run.as_dict() for run in runs[-sample_limit:]],
            "run_histogram_samples": {
                f"{bit}:{length}": count
                for (bit, length), count in sorted(run_histogram.items())[: sample_limit * 2]
            },
        },
        "prefix_samples": prefix_samples[: sample_limit * 4],
    }


def compare_starts(rows: list[dict[str, object]]) -> list[dict[str, int | float | None]]:
    comparison: list[dict[str, int | float | None]] = []
    for row in rows:
        cert = row["certificate"]
        critical = row["critical_line"]
        parity = row["parity_structure"]
        margin = row["surplus_margin_bits"]
        assert isinstance(cert, dict)
        assert isinstance(critical, dict)
        assert isinstance(parity, dict)
        assert isinstance(margin, dict)
        comparison.append(
            {
                "start": int(row["start"]),
                "bit_length": int(row["bit_length"]),
                "certificate_depth": int(cert["depth"]) if cert["depth"] is not None else None,
                "certificate_odd_count": int(cert["odd_count"]) if cert["odd_count"] is not None else None,
                "first_multiplier_contract_depth": (
                    int(row["first_multiplier_contract_depth"])
                    if row["first_multiplier_contract_depth"] is not None
                    else None
                ),
                "first_below_start_depth": (
                    int(row["first_below_start_depth"]) if row["first_below_start_depth"] is not None else None
                ),
                "max_excess": int(critical["max_excess"]),
                "mean_excess": float(critical["mean_excess"]),
                "boundary_touch_count": int(critical["boundary_touch_count"]),
                "longest_corridor_streak": int(critical["longest_corridor_streak"]),
                "mechanical_hamming_ratio": float(parity["mechanical_hamming_ratio"]),
                "longest_odd_run": int(parity["longest_odd_run"]),
                "longest_even_run": int(parity["longest_even_run"]),
                "final_surplus_margin_bits": float(margin["final"]),
            }
        )
    return sorted(comparison, key=lambda item: (item["certificate_depth"] or -1, int(item["start"])))


def parse_starts(raw_values: list[str]) -> list[int]:
    starts: list[int] = []
    for raw in raw_values:
        for part in raw.split(","):
            part = part.strip().replace("_", "")
            if part:
                starts.append(int(part, 0))
    return starts


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--starts",
        nargs="+",
        default=[
            "27",
            "703",
            "626331",
            "217740015",
            "2416326538309822975",
            "2358909599867980429759",
        ],
        help="positive starts to analyze; accepts comma-separated groups and 0x prefixes",
    )
    parser.add_argument(
        "--max-depth",
        type=int,
        default=0,
        help="profile depth; 0 means use each start's certificate depth",
    )
    parser.add_argument("--certificate-search-depth", type=int, default=4096, help="certificate search depth")
    parser.add_argument("--corridor-width", type=int, default=4, help="excess range 0..width treated as near-boundary")
    parser.add_argument("--sample-limit", type=int, default=10, help="number of samples for runs and boundary touches")
    parser.add_argument("--summary", action="store_true", help="omit per-start prefix samples and emit comparison only")
    args = parser.parse_args()

    starts = parse_starts(args.starts)
    if not starts or any(start < 1 for start in starts):
        raise SystemExit("--starts must contain positive integers")
    if args.max_depth < 0:
        raise SystemExit("--max-depth must be nonnegative")
    if args.certificate_search_depth < 1:
        raise SystemExit("--certificate-search-depth must be at least 1")
    if args.corridor_width < 0:
        raise SystemExit("--corridor-width must be nonnegative")

    rows = [
        analyze_start(
            start=start,
            max_depth=args.max_depth,
            certificate_search_depth=args.certificate_search_depth,
            corridor_width=args.corridor_width,
            sample_limit=args.sample_limit,
        )
        for start in starts
    ]
    payload: dict[str, object] = {
        "status": "parity-surplus-analysis",
        "parameters": {
            "starts": starts,
            "max_depth": args.max_depth,
            "certificate_search_depth": args.certificate_search_depth,
            "corridor_width": args.corridor_width,
        },
        "comparison": compare_starts(rows),
        "interpretation": (
            "Hard certificate examples are compared against the exact multiplier survival boundary. "
            "Small excess and long near-boundary streaks indicate paths that hug the critical line; "
            "large excess means delayed descent is also controlled by image height, not just multiplier survival."
        ),
    }
    if not args.summary:
        payload["rows"] = rows
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

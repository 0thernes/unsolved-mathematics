#!/usr/bin/env python3
"""Dual-debt phase analysis for hard Collatz certificate examples.

The residue-certificate route has two separate debts to clear.

1. Multiplier debt:

       M_d = o(d) * log2(3) - d

   This is positive while the affine multiplier 3^o / 2^d is expanding.

2. Height debt:

       H_d = log2(T^d(n) / n)

   This is positive while the actual iterate remains above the start.

A usable certificate for a finite representative occurs once both debts are
negative.  This script records phase transitions and peak/repayment spans for
hard examples.  It is a structural diagnostic, not a proof.
"""

from __future__ import annotations

import argparse
import json
import math
from statistics import mean

from certificate_depth_scan import certificate_for_start, total_stopping_profile
from collatz_residue_lab import shortcut
from parity_surplus_analyzer import min_surviving_odd_counts, powers_of_three


LOG2_3 = math.log2(3)


def pearson(xs: list[float], ys: list[float]) -> float | None:
    if len(xs) != len(ys) or len(xs) < 2:
        return None
    mean_x = mean(xs)
    mean_y = mean(ys)
    numerator = sum((x - mean_x) * (y - mean_y) for x, y in zip(xs, ys))
    denominator_x = sum((x - mean_x) ** 2 for x in xs)
    denominator_y = sum((y - mean_y) ** 2 for y in ys)
    if denominator_x == 0 or denominator_y == 0:
        return None
    return numerator / math.sqrt(denominator_x * denominator_y)


def first_index(flags: list[bool]) -> int | None:
    for index, flag in enumerate(flags, start=1):
        if flag:
            return index
    return None


def max_event(values: list[float]) -> tuple[int, float]:
    if not values:
        return 0, 0.0
    depth, value = max(enumerate(values, start=1), key=lambda item: (item[1], -item[0]))
    return depth, value


def positive_area(values: list[float]) -> float:
    return sum(value for value in values if value > 0)


def classify(
    certificate_depth: int | None,
    max_multiplier_debt: float,
    max_height_debt: float,
    longest_corridor_streak: int,
) -> str:
    if certificate_depth is None or certificate_depth <= 0:
        return "unclassified"
    corridor_ratio = longest_corridor_streak / certificate_depth
    if corridor_ratio >= 0.4 and max_multiplier_debt < 16:
        return "critical-line-corridor"
    if max_multiplier_debt >= 20 or max_height_debt >= 20:
        return "surplus-height-repayment"
    return "mixed-transition"


def analyze_start(
    start: int,
    max_depth: int,
    certificate_search_depth: int,
    corridor_width_bits: float,
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
    x = start
    odd_count = 0
    multiplier_debts: list[float] = []
    height_debts: list[float] = []
    translation_gaps: list[float] = []
    dual_debts: list[float] = []
    excesses: list[int] = []
    corridor_flags: list[bool] = []
    samples: list[dict[str, int | float | bool]] = []

    for depth in range(1, depth_limit + 1):
        was_odd = x & 1
        odd_count += was_odd
        x = shortcut(x)

        multiplier_debt = odd_count * LOG2_3 - depth
        height_debt = math.log2(x) - math.log2(start)
        translation_gap = height_debt - multiplier_debt
        dual_debt = max(multiplier_debt, height_debt)
        excess = odd_count - min_odd[depth]
        is_near_corridor = 0 <= multiplier_debt <= corridor_width_bits

        multiplier_debts.append(multiplier_debt)
        height_debts.append(height_debt)
        translation_gaps.append(translation_gap)
        dual_debts.append(dual_debt)
        excesses.append(excess)
        corridor_flags.append(is_near_corridor)

        if (
            depth <= sample_limit
            or depth == depth_limit
            or len(samples) < sample_limit * 2 and (multiplier_debt < 0 or height_debt < 0)
        ):
            samples.append(
                {
                    "depth": depth,
                    "parity_bit": was_odd,
                    "odd_count": odd_count,
                    "excess": excess,
                    "multiplier_debt_bits": round(multiplier_debt, 9),
                    "height_debt_bits": round(height_debt, 9),
                    "translation_gap_bits": round(translation_gap, 9),
                    "dual_debt_bits": round(dual_debt, 9),
                    "multiplier_clear": multiplier_debt < 0,
                    "height_clear": height_debt < 0,
                }
            )

    multiplier_peak_depth, multiplier_peak = max_event(multiplier_debts)
    height_peak_depth, height_peak = max_event(height_debts)
    dual_peak_depth, dual_peak = max_event(dual_debts)
    first_multiplier_clear = first_index([value < 0 for value in multiplier_debts])
    first_height_clear = first_index([value < 0 for value in height_debts])
    first_dual_clear = first_index([value < 0 for value in dual_debts])
    longest_corridor = longest_true_streak(corridor_flags)
    max_excess = max(excesses) if excesses else 0
    mean_excess = mean(excesses) if excesses else 0

    phase_graph = [
        {"node": "start", "depth": 0, "value_bits": 0.0},
        {
            "node": "multiplier_peak",
            "depth": multiplier_peak_depth,
            "value_bits": round(multiplier_peak, 9),
        },
        {"node": "height_peak", "depth": height_peak_depth, "value_bits": round(height_peak, 9)},
        {
            "node": "multiplier_clears",
            "depth": first_multiplier_clear,
            "value_bits": round(multiplier_debts[first_multiplier_clear - 1], 9)
            if first_multiplier_clear
            else None,
        },
        {
            "node": "height_clears",
            "depth": first_height_clear,
            "value_bits": round(height_debts[first_height_clear - 1], 9) if first_height_clear else None,
        },
        {
            "node": "dual_clears",
            "depth": first_dual_clear,
            "value_bits": round(dual_debts[first_dual_clear - 1], 9) if first_dual_clear else None,
        },
    ]

    height_repayment_span = first_height_clear - height_peak_depth if first_height_clear else None
    multiplier_repayment_span = first_multiplier_clear - multiplier_peak_depth if first_multiplier_clear else None
    profile = total_stopping_profile(start, max(10000, depth_limit * 4))

    return {
        "start": start,
        "bit_length": start.bit_length(),
        "depth_limit": depth_limit,
        "certificate": cert,
        "profile": profile,
        "classification": classify(
            int(cert["depth"]) if cert["depth"] is not None else None,
            multiplier_peak,
            height_peak,
            longest_corridor,
        ),
        "phase_events": {
            "first_multiplier_clear_depth": first_multiplier_clear,
            "first_height_clear_depth": first_height_clear,
            "first_dual_clear_depth": first_dual_clear,
            "multiplier_peak_depth": multiplier_peak_depth,
            "height_peak_depth": height_peak_depth,
            "dual_peak_depth": dual_peak_depth,
            "peak_depth_gap": abs(height_peak_depth - multiplier_peak_depth),
            "multiplier_repayment_span": multiplier_repayment_span,
            "height_repayment_span": height_repayment_span,
            "synchronized_clearance": first_multiplier_clear == first_height_clear == first_dual_clear,
        },
        "debt_extrema_bits": {
            "max_multiplier_debt": round(multiplier_peak, 9),
            "max_height_debt": round(height_peak, 9),
            "max_translation_gap": round(max(translation_gaps), 9) if translation_gaps else 0,
            "mean_translation_gap": round(mean(translation_gaps), 9) if translation_gaps else 0,
            "max_dual_debt": round(dual_peak, 9),
            "final_multiplier_debt": round(multiplier_debts[-1], 9) if multiplier_debts else 0,
            "final_height_debt": round(height_debts[-1], 9) if height_debts else 0,
            "final_translation_gap": round(translation_gaps[-1], 9) if translation_gaps else 0,
            "final_dual_debt": round(dual_debts[-1], 9) if dual_debts else 0,
        },
        "debt_area_bits": {
            "positive_multiplier_area": round(positive_area(multiplier_debts), 9),
            "positive_height_area": round(positive_area(height_debts), 9),
            "positive_dual_area": round(positive_area(dual_debts), 9),
        },
        "coupling": {
            "pearson_multiplier_height": round(correlation, 9)
            if (correlation := pearson(multiplier_debts, height_debts)) is not None
            else None,
            "max_excess": max_excess,
            "mean_excess": round(mean_excess, 6),
            "longest_multiplier_corridor_streak": longest_corridor,
            "corridor_width_bits": corridor_width_bits,
        },
        "phase_graph": phase_graph,
        "samples": samples[: sample_limit * 3],
    }


def longest_true_streak(flags: list[bool]) -> int:
    best = 0
    current = 0
    for flag in flags:
        if flag:
            current += 1
            best = max(best, current)
        else:
            current = 0
    return best


def compare_rows(rows: list[dict[str, object]]) -> list[dict[str, int | float | str | bool | None]]:
    comparison: list[dict[str, int | float | str | bool | None]] = []
    for row in rows:
        cert = row["certificate"]
        phase = row["phase_events"]
        extrema = row["debt_extrema_bits"]
        area = row["debt_area_bits"]
        coupling = row["coupling"]
        assert isinstance(cert, dict)
        assert isinstance(phase, dict)
        assert isinstance(extrema, dict)
        assert isinstance(area, dict)
        assert isinstance(coupling, dict)
        comparison.append(
            {
                "start": int(row["start"]),
                "bit_length": int(row["bit_length"]),
                "classification": str(row["classification"]),
                "certificate_depth": int(cert["depth"]) if cert["depth"] is not None else None,
                "certificate_odd_count": int(cert["odd_count"]) if cert["odd_count"] is not None else None,
                "max_multiplier_debt_bits": float(extrema["max_multiplier_debt"]),
                "max_height_debt_bits": float(extrema["max_height_debt"]),
                "max_translation_gap_bits": float(extrema["max_translation_gap"]),
                "mean_translation_gap_bits": float(extrema["mean_translation_gap"]),
                "height_peak_depth": int(phase["height_peak_depth"]),
                "first_dual_clear_depth": int(phase["first_dual_clear_depth"])
                if phase["first_dual_clear_depth"] is not None
                else None,
                "height_repayment_span": int(phase["height_repayment_span"])
                if phase["height_repayment_span"] is not None
                else None,
                "positive_dual_area": float(area["positive_dual_area"]),
                "pearson_multiplier_height": (
                    float(coupling["pearson_multiplier_height"])
                    if coupling["pearson_multiplier_height"] is not None
                    else None
                ),
                "longest_multiplier_corridor_streak": int(coupling["longest_multiplier_corridor_streak"]),
                "max_excess": int(coupling["max_excess"]),
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
            "217740015",
            "2416326538309822975",
            "2358909599867980429759",
        ],
        help="positive starts to analyze; accepts comma-separated groups and 0x prefixes",
    )
    parser.add_argument("--max-depth", type=int, default=0, help="profile depth; 0 means each certificate depth")
    parser.add_argument("--certificate-search-depth", type=int, default=4096, help="certificate search depth")
    parser.add_argument("--corridor-width-bits", type=float, default=4.0, help="near-critical multiplier debt width")
    parser.add_argument("--sample-limit", type=int, default=8, help="number of event samples to keep")
    parser.add_argument("--summary", action="store_true", help="omit per-start samples and phase graphs")
    args = parser.parse_args()

    starts = parse_starts(args.starts)
    if not starts or any(start < 1 for start in starts):
        raise SystemExit("--starts must contain positive integers")
    if args.max_depth < 0:
        raise SystemExit("--max-depth must be nonnegative")
    if args.certificate_search_depth < 1:
        raise SystemExit("--certificate-search-depth must be at least 1")
    if args.corridor_width_bits < 0:
        raise SystemExit("--corridor-width-bits must be nonnegative")

    rows = [
        analyze_start(
            start=start,
            max_depth=args.max_depth,
            certificate_search_depth=args.certificate_search_depth,
            corridor_width_bits=args.corridor_width_bits,
            sample_limit=args.sample_limit,
        )
        for start in starts
    ]
    payload: dict[str, object] = {
        "status": "debt-phase-analysis",
        "parameters": {
            "starts": starts,
            "max_depth": args.max_depth,
            "certificate_search_depth": args.certificate_search_depth,
            "corridor_width_bits": args.corridor_width_bits,
        },
        "comparison": compare_rows(rows),
        "interpretation": (
            "Multiplier debt and height debt must both clear before a usable certificate. "
            "Critical-line cases have long low multiplier-debt corridors; repayment cases "
            "build high dual debt and require a long clearance span."
        ),
    }
    if not args.summary:
        payload["rows"] = rows
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Scan Collatz debt repayment windows.

The certificate frontier tools identify starts whose shortcut trajectory stays
above its initial value for a long time.  This script looks at the return leg:
after the trajectory reaches peak dual debt, how much low-odd-density interval
is needed before both multiplier debt and actual height debt clear?

For shortcut depth d with o odd shortcut steps:

    multiplier_debt(d) = o log2(3) - d
    height_debt(d)     = log2(T^d(n) / n)
    dual_debt(d)       = max(multiplier_debt(d), height_debt(d))

A usable descent certificate for the concrete start has cleared exactly when
the multiplier is contracting and the current iterate is below the start.  The
repayment interval from peak dual debt to clearance is therefore a concrete
finite shadow of the proof obligation.
"""

from __future__ import annotations

import argparse
import json
import math
from collections import Counter
from statistics import mean
from time import perf_counter
from typing import Iterable

from certificate_depth_scan import certificate_for_start, total_stopping_profile
from collatz_residue_lab import shortcut
from frontier_escape_analyzer import enumerate_frontier
from parity_surplus_analyzer import min_surviving_odd_counts


LOG2_3 = math.log2(3)
CRITICAL_ODD_RATIO = 1 / LOG2_3


def powers_of_three(max_depth: int) -> list[int]:
    pow3 = [1]
    for _ in range(max_depth):
        pow3.append(pow3[-1] * 3)
    return pow3


def parse_ints(raw_values: list[str] | None) -> list[int]:
    if not raw_values:
        return []
    values: list[int] = []
    for raw in raw_values:
        for part in raw.split(","):
            part = part.strip().replace("_", "")
            if part:
                values.append(int(part, 0))
    return values


def unique_preserving_order(values: Iterable[int]) -> list[int]:
    seen: set[int] = set()
    ordered: list[int] = []
    for value in values:
        if value in seen:
            continue
        seen.add(value)
        ordered.append(value)
    return ordered


def round_float(value: float | None, digits: int = 9) -> float | None:
    if value is None:
        return None
    return round(value, digits)


def first_dual_clear_index(rows: list[dict[str, int | float | bool]], pow3: list[int]) -> int | None:
    for index, row in enumerate(rows):
        depth = int(row["depth"])
        odd_count = int(row["odd_count"])
        if pow3[odd_count] < (1 << depth) and bool(row["below_start"]):
            return index
    return None


def classify_row(row: dict[str, object]) -> str:
    if not row["certified"]:
        return "uncertified"
    repayment = row["repayment_window"]
    extrema = row["debt_extrema"]
    assert isinstance(repayment, dict)
    assert isinstance(extrema, dict)
    span = int(repayment["length"])
    peak = float(extrema["max_dual_debt_bits"])
    deficit_rate = float(repayment["multiplier_deficit_per_step_bits"])
    if span == 0:
        return "already-clear"
    if peak < 16 and span >= 128:
        return "slow-critical-repayment"
    if peak >= 32 and deficit_rate >= 0.12:
        return "high-debt-fast-repayment"
    if peak >= 20:
        return "high-debt-repayment"
    if deficit_rate < 0.08 and span >= 64:
        return "low-slope-repayment"
    return "mixed-repayment"


def analyze_start(
    start: int,
    max_depth: int,
    pow3: list[int],
    sample_limit: int,
    step_limit: int,
) -> dict[str, object]:
    if start < 1:
        raise ValueError("starts must be positive")

    cert = certificate_for_start(start, max_depth, pow3)
    if start == 1:
        return {
            "start": start,
            "bit_length": 1,
            "certified": True,
            "certificate": cert,
            "classification": "trivial-cycle-entry",
            "debt_extrema": {
                "max_multiplier_debt_bits": 0.0,
                "max_height_debt_bits": 0.0,
                "max_dual_debt_bits": 0.0,
                "peak_dual_depth": 0,
                "peak_odd_count": 0,
                "peak_excess": None,
            },
            "repayment_window": {
                "start_depth": 0,
                "clear_depth": 0,
                "length": 0,
                "odd_count": 0,
                "even_count": 0,
                "odd_ratio": 0.0,
                "critical_odd_ratio": round_float(CRITICAL_ODD_RATIO),
                "odd_ratio_gap_to_critical": round_float(CRITICAL_ODD_RATIO),
                "multiplier_deficit_bits": 0.0,
                "multiplier_deficit_per_step_bits": 0.0,
                "clearance_margin_bits": 0.0,
            },
            "samples": [],
            "profile": total_stopping_profile(start, step_limit),
        }

    depth_limit = int(cert["depth"]) if cert["certified"] and cert["depth"] is not None else max_depth
    min_odd = min_surviving_odd_counts(depth_limit, pow3)
    x = start
    odd_count = 0
    rows: list[dict[str, int | float | bool]] = []

    for depth in range(1, depth_limit + 1):
        was_odd = x & 1
        odd_count += was_odd
        x = shortcut(x)
        multiplier_debt = odd_count * LOG2_3 - depth
        height_debt = math.log2(x) - math.log2(start)
        translation_gap = height_debt - multiplier_debt
        dual_debt = max(multiplier_debt, height_debt)
        rows.append(
            {
                "depth": depth,
                "value": x,
                "parity_bit": was_odd,
                "odd_count": odd_count,
                "min_surviving_odd_count": min_odd[depth],
                "excess": odd_count - min_odd[depth],
                "multiplier_debt_bits": multiplier_debt,
                "height_debt_bits": height_debt,
                "translation_gap_bits": translation_gap,
                "dual_debt_bits": dual_debt,
                "below_start": x < start,
                "multiplier_contracts": pow3[odd_count] < (1 << depth),
            }
        )

    if rows:
        peak_index, peak_row = max(
            enumerate(rows),
            key=lambda item: (float(item[1]["dual_debt_bits"]), -int(item[1]["depth"])),
        )
        max_multiplier = max(float(row["multiplier_debt_bits"]) for row in rows)
        max_height = max(float(row["height_debt_bits"]) for row in rows)
        max_translation_gap = max(float(row["translation_gap_bits"]) for row in rows)
        clear_index = first_dual_clear_index(rows, pow3)
    else:
        peak_index = -1
        peak_row = None
        max_multiplier = max_height = max_translation_gap = 0.0
        clear_index = None

    if clear_index is not None and peak_row is not None:
        clear_row = rows[clear_index]
        peak_depth = int(peak_row["depth"])
        clear_depth = int(clear_row["depth"])
        span = clear_depth - peak_depth
        interval_odd_count = int(clear_row["odd_count"]) - int(peak_row["odd_count"])
        even_count = span - interval_odd_count
        odd_ratio = interval_odd_count / span if span else 0.0
        multiplier_deficit = span - interval_odd_count * LOG2_3
        multiplier_deficit_per_step = multiplier_deficit / span if span else 0.0
        clearance_margin = -float(clear_row["dual_debt_bits"])
        peak_to_clear_height_drop = float(peak_row["height_debt_bits"]) - float(clear_row["height_debt_bits"])
        peak_to_clear_multiplier_drop = (
            float(peak_row["multiplier_debt_bits"]) - float(clear_row["multiplier_debt_bits"])
        )
        repayment_window = {
            "start_depth": peak_depth,
            "clear_depth": clear_depth,
            "length": span,
            "odd_count": interval_odd_count,
            "even_count": even_count,
            "odd_ratio": round_float(odd_ratio),
            "critical_odd_ratio": round_float(CRITICAL_ODD_RATIO),
            "odd_ratio_gap_to_critical": round_float(CRITICAL_ODD_RATIO - odd_ratio),
            "multiplier_deficit_bits": round_float(multiplier_deficit),
            "multiplier_deficit_per_step_bits": round_float(multiplier_deficit_per_step),
            "peak_to_clear_height_drop_bits": round_float(peak_to_clear_height_drop),
            "peak_to_clear_multiplier_drop_bits": round_float(peak_to_clear_multiplier_drop),
            "clearance_margin_bits": round_float(clearance_margin),
        }
    elif peak_row is not None:
        repayment_window = {
            "start_depth": int(peak_row["depth"]),
            "clear_depth": None,
            "length": None,
            "odd_count": None,
            "even_count": None,
            "odd_ratio": None,
            "critical_odd_ratio": round_float(CRITICAL_ODD_RATIO),
            "odd_ratio_gap_to_critical": None,
            "multiplier_deficit_bits": None,
            "multiplier_deficit_per_step_bits": None,
            "peak_to_clear_height_drop_bits": None,
            "peak_to_clear_multiplier_drop_bits": None,
            "clearance_margin_bits": None,
        }
    else:
        repayment_window = {
            "start_depth": None,
            "clear_depth": None,
            "length": None,
            "odd_count": None,
            "even_count": None,
            "odd_ratio": None,
            "critical_odd_ratio": round_float(CRITICAL_ODD_RATIO),
            "odd_ratio_gap_to_critical": None,
            "multiplier_deficit_bits": None,
            "multiplier_deficit_per_step_bits": None,
            "peak_to_clear_height_drop_bits": None,
            "peak_to_clear_multiplier_drop_bits": None,
            "clearance_margin_bits": None,
        }

    sample_rows: list[dict[str, int | float | bool]] = []
    if rows:
        interesting_depths = {
            1,
            int(peak_row["depth"]) if peak_row is not None else 1,
            int(rows[-1]["depth"]),
        }
        if clear_index is not None:
            interesting_depths.add(int(rows[clear_index]["depth"]))
        for row in rows:
            depth = int(row["depth"])
            if depth <= sample_limit or depth in interesting_depths:
                sample_rows.append(
                    {
                        "depth": depth,
                        "parity_bit": int(row["parity_bit"]),
                        "odd_count": int(row["odd_count"]),
                        "excess": int(row["excess"]),
                        "multiplier_debt_bits": round_float(float(row["multiplier_debt_bits"])),
                        "height_debt_bits": round_float(float(row["height_debt_bits"])),
                        "translation_gap_bits": round_float(float(row["translation_gap_bits"])),
                        "dual_debt_bits": round_float(float(row["dual_debt_bits"])),
                        "below_start": bool(row["below_start"]),
                        "multiplier_contracts": bool(row["multiplier_contracts"]),
                    }
                )

    result: dict[str, object] = {
        "start": start,
        "bit_length": start.bit_length(),
        "certified": bool(cert["certified"]),
        "certificate": cert,
        "debt_extrema": {
            "max_multiplier_debt_bits": round_float(max_multiplier),
            "max_height_debt_bits": round_float(max_height),
            "max_translation_gap_bits": round_float(max_translation_gap),
            "max_dual_debt_bits": round_float(float(peak_row["dual_debt_bits"]) if peak_row else 0.0),
            "peak_dual_depth": int(peak_row["depth"]) if peak_row else None,
            "peak_odd_count": int(peak_row["odd_count"]) if peak_row else None,
            "peak_excess": int(peak_row["excess"]) if peak_row else None,
        },
        "repayment_window": repayment_window,
        "profile": total_stopping_profile(start, step_limit),
        "samples": sample_rows[: sample_limit * 3],
    }
    result["classification"] = classify_row(result)
    return result


def compact_row(row: dict[str, object]) -> dict[str, int | float | str | bool | None]:
    cert = row["certificate"]
    extrema = row["debt_extrema"]
    repayment = row["repayment_window"]
    assert isinstance(cert, dict)
    assert isinstance(extrema, dict)
    assert isinstance(repayment, dict)
    return {
        "start": int(row["start"]),
        "bit_length": int(row["bit_length"]),
        "certified": bool(row["certified"]),
        "classification": str(row["classification"]),
        "certificate_depth": int(cert["depth"]) if cert["depth"] is not None else None,
        "certificate_odd_count": int(cert["odd_count"]) if cert["odd_count"] is not None else None,
        "max_dual_debt_bits": float(extrema["max_dual_debt_bits"]),
        "peak_dual_depth": int(extrema["peak_dual_depth"]) if extrema["peak_dual_depth"] is not None else None,
        "peak_excess": int(extrema["peak_excess"]) if extrema["peak_excess"] is not None else None,
        "repayment_length": int(repayment["length"]) if repayment["length"] is not None else None,
        "repayment_odd_ratio": (
            float(repayment["odd_ratio"]) if repayment["odd_ratio"] is not None else None
        ),
        "odd_ratio_gap_to_critical": (
            float(repayment["odd_ratio_gap_to_critical"])
            if repayment["odd_ratio_gap_to_critical"] is not None
            else None
        ),
        "multiplier_deficit_bits": (
            float(repayment["multiplier_deficit_bits"])
            if repayment["multiplier_deficit_bits"] is not None
            else None
        ),
        "multiplier_deficit_per_step_bits": (
            float(repayment["multiplier_deficit_per_step_bits"])
            if repayment["multiplier_deficit_per_step_bits"] is not None
            else None
        ),
        "clearance_margin_bits": (
            float(repayment["clearance_margin_bits"])
            if repayment["clearance_margin_bits"] is not None
            else None
        ),
    }


def top_records(
    rows: list[dict[str, object]],
    key_name: str,
    top_n: int,
) -> list[dict[str, int | float | str | bool | None]]:
    compact = [compact_row(row) for row in rows]
    return sorted(
        compact,
        key=lambda item: (
            item[key_name] if item[key_name] is not None else -1,
            item["start"] if item["start"] is not None else -1,
        ),
        reverse=True,
    )[:top_n]


def record_setters_by_certificate(rows: list[dict[str, object]]) -> list[dict[str, int | float | str | bool | None]]:
    best = -1
    records: list[dict[str, int | float | str | bool | None]] = []
    for row in sorted(rows, key=lambda item: int(item["start"])):
        compact = compact_row(row)
        depth = compact["certificate_depth"]
        if depth is not None and depth > best:
            best = depth
            records.append(compact)
    return records


def frontier_starts(
    base_depth: int,
    max_depth: int,
    max_frontier: int | None,
    sample_stride: int,
    sample_offset: int,
) -> tuple[list[int], dict[str, object]]:
    pow3 = powers_of_three(max_depth)
    frontier, stats = enumerate_frontier(base_depth, pow3)
    selected = sorted(frontier, key=lambda leaf: leaf.residue)
    if sample_stride > 1:
        selected = [leaf for index, leaf in enumerate(selected) if index % sample_stride == sample_offset]
    if max_frontier is not None:
        selected = selected[:max_frontier]
    starts = [leaf.residue for leaf in selected if leaf.residue > 0]
    return starts, {
        **stats,
        "selected_count": len(starts),
        "sample_stride": sample_stride,
        "sample_offset": sample_offset,
        "max_frontier": max_frontier,
    }


def summarize(rows: list[dict[str, object]], top_n: int) -> dict[str, object]:
    compact = [compact_row(row) for row in rows]
    certified = [row for row in compact if row["certified"]]
    classes = Counter(row["classification"] for row in compact)
    rates = [
        float(row["multiplier_deficit_per_step_bits"])
        for row in certified
        if row["multiplier_deficit_per_step_bits"] is not None
        and row["repayment_length"] is not None
        and int(row["repayment_length"]) > 0
    ]
    spans = [
        int(row["repayment_length"])
        for row in certified
        if row["repayment_length"] is not None and int(row["repayment_length"]) > 0
    ]
    depths = [int(row["certificate_depth"]) for row in certified if row["certificate_depth"] is not None]
    peaks = [float(row["max_dual_debt_bits"]) for row in certified]
    return {
        "analyzed_count": len(compact),
        "certified_count": len(certified),
        "uncertified_count": len(compact) - len(certified),
        "classification_histogram": {str(k): classes[k] for k in sorted(classes)},
        "max_certificate_depth": max(depths) if depths else None,
        "max_repayment_length": max(spans) if spans else None,
        "max_dual_debt_bits": round_float(max(peaks)) if peaks else None,
        "min_repayment_deficit_per_step_bits": round_float(min(rates)) if rates else None,
        "mean_repayment_deficit_per_step_bits": round_float(mean(rates)) if rates else None,
        "top_by_certificate_depth": top_records(rows, "certificate_depth", top_n),
        "top_by_repayment_length": top_records(rows, "repayment_length", top_n),
        "top_by_dual_debt": top_records(rows, "max_dual_debt_bits", top_n),
        "record_setters_by_certificate_depth": record_setters_by_certificate(rows)[-top_n:],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--starts",
        nargs="+",
        default=None,
        help="explicit starts; accepts comma-separated values, underscores, and 0x prefixes",
    )
    parser.add_argument("--limit", type=int, default=0, help="also scan starts 1..limit")
    parser.add_argument("--frontier-base-depth", type=int, default=0, help="also scan exact frontier residues")
    parser.add_argument("--max-depth", type=int, default=1200, help="certificate/debt search depth")
    parser.add_argument("--top-n", type=int, default=12, help="number of top rows to keep")
    parser.add_argument("--step-limit", type=int, default=100000, help="trajectory profile step cap")
    parser.add_argument("--sample-limit", type=int, default=8, help="per-start sample rows when not summary-only")
    parser.add_argument("--max-frontier", type=int, help="frontier mode: analyze at most this many selected leaves")
    parser.add_argument("--sample-stride", type=int, default=1, help="frontier mode: analyze every kth leaf")
    parser.add_argument("--sample-offset", type=int, default=0, help="frontier mode offset")
    parser.add_argument("--summary", action="store_true", help="omit full per-start rows")
    args = parser.parse_args()

    if args.max_depth < 1:
        raise SystemExit("--max-depth must be at least 1")
    if args.limit < 0:
        raise SystemExit("--limit must be nonnegative")
    if args.top_n < 1:
        raise SystemExit("--top-n must be at least 1")
    if args.sample_stride < 1:
        raise SystemExit("--sample-stride must be at least 1")
    if not 0 <= args.sample_offset < args.sample_stride:
        raise SystemExit("--sample-offset must satisfy 0 <= offset < stride")
    if args.max_frontier is not None and args.max_frontier < 1:
        raise SystemExit("--max-frontier must be positive when provided")

    started = perf_counter()
    explicit_starts = parse_ints(args.starts)
    if not explicit_starts and args.limit == 0 and args.frontier_base_depth == 0:
        explicit_starts = [
            27,
            703,
            626331,
            217740015,
            2416326538309822975,
            2358909599867980429759,
        ]
    if any(start < 1 for start in explicit_starts):
        raise SystemExit("--starts must contain positive integers")

    frontier_metadata: dict[str, object] | None = None
    frontier_values: list[int] = []
    if args.frontier_base_depth:
        if args.frontier_base_depth < 1:
            raise SystemExit("--frontier-base-depth must be positive when provided")
        if args.max_depth <= args.frontier_base_depth:
            raise SystemExit("--max-depth must exceed --frontier-base-depth in frontier mode")
        frontier_values, frontier_metadata = frontier_starts(
            base_depth=args.frontier_base_depth,
            max_depth=args.max_depth,
            max_frontier=args.max_frontier,
            sample_stride=args.sample_stride,
            sample_offset=args.sample_offset,
        )

    starts = unique_preserving_order(
        [
            *explicit_starts,
            *range(1, args.limit + 1),
            *frontier_values,
        ]
    )
    pow3 = powers_of_three(args.max_depth)
    rows = [
        analyze_start(
            start=start,
            max_depth=args.max_depth,
            pow3=pow3,
            sample_limit=args.sample_limit,
            step_limit=args.step_limit,
        )
        for start in starts
    ]

    payload: dict[str, object] = {
        "status": "repayment-envelope-scan",
        "elapsed_seconds": round_float(perf_counter() - started, 6),
        "parameters": {
            "starts": explicit_starts,
            "limit": args.limit,
            "frontier_base_depth": args.frontier_base_depth or None,
            "max_depth": args.max_depth,
            "top_n": args.top_n,
            "critical_odd_ratio": round_float(CRITICAL_ODD_RATIO),
        },
        "frontier": frontier_metadata,
        "summary": summarize(rows, args.top_n),
        "interpretation": (
            "A repayment window is the interval from peak dual debt to first exact clearance. "
            "Its odd ratio must fall below 1/log2(3), creating a multiplier deficit large enough "
            "to erase accumulated debt plus the affine translation gap. Uniform repayment-window "
            "control is the concrete theorem target suggested by this certificate route."
        ),
    }
    if not args.summary:
        payload["rows"] = rows
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Test subcritical motif forcing in finite Collatz shadows.

The previous motif miner records the repayment window that clears accumulated
debt.  This script asks a slightly different question:

    how soon is a finite positive shadow forced to contain *any* subcritical
    parity window of a chosen length family?

For a window of length L with a odd steps, the multiplier deficit is

    L - a log2(3).

Positive deficit means the window has odd density below the critical ratio
log_3(2).  The all-odd 2-adic path can avoid these windows forever, so this
analyzer only claims evidence for finite positive shadows and their deterministic
continuations.
"""

from __future__ import annotations

import argparse
import heapq
import json
import math
from collections import Counter
from dataclasses import dataclass
from statistics import mean
from time import perf_counter
from typing import Iterable

from certificate_depth_scan import certificate_for_start
from collatz_residue_lab import shortcut
from frontier_escape_analyzer import enumerate_frontier
from repayment_envelope_scan import CRITICAL_ODD_RATIO, LOG2_3, parse_ints, round_float


DEFAULT_HARD_STARTS = [
    27,
    703,
    626331,
    217740015,
    2416326538309822975,
    2358909599867980429759,
]


@dataclass(frozen=True)
class WindowHit:
    start: int
    scope: str
    scope_depth: int
    window_start_depth: int
    window_end_depth: int
    length: int
    odd_count: int
    deficit_bits: float
    odd_ratio: float
    peak_depth: int
    certificate_depth: int | None

    def motif(self) -> str:
        return f"{self.length}:{self.odd_count}"

    def as_dict(self) -> dict[str, int | float | str | None]:
        return {
            "start": self.start,
            "scope": self.scope,
            "scope_depth": self.scope_depth,
            "window_start_depth": self.window_start_depth,
            "window_end_depth": self.window_end_depth,
            "wait_after_scope": self.window_start_depth - self.scope_depth,
            "length": self.length,
            "odd_count": self.odd_count,
            "motif": self.motif(),
            "odd_ratio": round_float(self.odd_ratio),
            "critical_odd_ratio": round_float(CRITICAL_ODD_RATIO),
            "deficit_bits": round_float(self.deficit_bits),
            "deficit_per_step_bits": round_float(self.deficit_bits / self.length if self.length else 0.0),
            "peak_depth": self.peak_depth,
            "certificate_depth": self.certificate_depth,
        }


def powers_of_three(max_depth: int) -> list[int]:
    pow3 = [1]
    for _ in range(max_depth):
        pow3.append(pow3[-1] * 3)
    return pow3


def unique_preserving_order(values: Iterable[int]) -> list[int]:
    seen: set[int] = set()
    ordered: list[int] = []
    for value in values:
        if value in seen:
            continue
        seen.add(value)
        ordered.append(value)
    return ordered


def parse_lengths(raw: str | None, min_length: int, max_length: int) -> list[int]:
    if raw:
        lengths: set[int] = set()
        for chunk in raw.split(","):
            chunk = chunk.strip()
            if not chunk:
                continue
            if "-" in chunk:
                left, right = chunk.split("-", 1)
                start = int(left)
                end = int(right)
                lengths.update(range(start, end + 1))
            else:
                lengths.add(int(chunk))
        parsed = sorted(length for length in lengths if length > 0)
    else:
        parsed = list(range(min_length, max_length + 1))
    if not parsed:
        raise ValueError("at least one positive window length is required")
    return parsed


def choose_scope_depth(scope: str, base_depth: int | None, peak_depth: int) -> int:
    if scope == "start":
        return 0
    if scope == "post-base":
        return base_depth or 0
    if scope == "post-peak":
        return peak_depth
    raise ValueError(f"unknown scope {scope}")


def trajectory_profile(start: int, max_depth: int, pow3: list[int]) -> dict[str, object]:
    cert = certificate_for_start(start, max_depth, pow3)
    depth_limit = int(cert["depth"]) if cert["certified"] and cert["depth"] is not None else max_depth
    x = start
    bits: list[int] = []
    prefix_odd = [0]
    dual_debts: list[float] = []

    for depth in range(1, depth_limit + 1):
        was_odd = x & 1
        bits.append(was_odd)
        x = shortcut(x)
        odd_count = prefix_odd[-1] + was_odd
        prefix_odd.append(odd_count)
        multiplier_debt = odd_count * LOG2_3 - depth
        height_debt = math.log2(x) - math.log2(start)
        dual_debts.append(max(multiplier_debt, height_debt))

    if dual_debts:
        peak_depth, peak_debt = max(enumerate(dual_debts, start=1), key=lambda item: (item[1], -item[0]))
    else:
        peak_depth = 0
        peak_debt = 0.0

    return {
        "certificate": cert,
        "depth_limit": depth_limit,
        "bits": bits,
        "prefix_odd": prefix_odd,
        "peak_depth": peak_depth,
        "peak_dual_debt_bits": peak_debt,
    }


def window_for(
    start: int,
    scope: str,
    scope_depth: int,
    peak_depth: int,
    certificate_depth: int | None,
    prefix_odd: list[int],
    window_start: int,
    length: int,
) -> WindowHit:
    window_end = window_start + length
    odd_count = prefix_odd[window_end] - prefix_odd[window_start]
    deficit = length - odd_count * LOG2_3
    return WindowHit(
        start=start,
        scope=scope,
        scope_depth=scope_depth,
        window_start_depth=window_start,
        window_end_depth=window_end,
        length=length,
        odd_count=odd_count,
        deficit_bits=deficit,
        odd_ratio=odd_count / length if length else 0.0,
        peak_depth=peak_depth,
        certificate_depth=certificate_depth,
    )


def find_first_window(
    start: int,
    scope: str,
    scope_depth: int,
    peak_depth: int,
    certificate_depth: int | None,
    prefix_odd: list[int],
    lengths: list[int],
    min_deficit_bits: float,
    max_odd_ratio: float | None,
) -> WindowHit | None:
    depth_limit = len(prefix_odd) - 1
    min_length = min(lengths)
    length_set = set(lengths)
    for window_end in range(scope_depth + min_length, depth_limit + 1):
        for length in lengths:
            window_start = window_end - length
            if window_start < scope_depth:
                continue
            if length not in length_set:
                continue
            odd_count = prefix_odd[window_end] - prefix_odd[window_start]
            deficit = length - odd_count * LOG2_3
            odd_ratio = odd_count / length if length else 0.0
            if deficit >= min_deficit_bits and (max_odd_ratio is None or odd_ratio <= max_odd_ratio):
                return WindowHit(
                    start=start,
                    scope=scope,
                    scope_depth=scope_depth,
                    window_start_depth=window_start,
                    window_end_depth=window_end,
                    length=length,
                    odd_count=odd_count,
                    deficit_bits=deficit,
                    odd_ratio=odd_ratio,
                    peak_depth=peak_depth,
                    certificate_depth=certificate_depth,
                )
    return None


def top_push(heap: list[tuple[tuple[float, int, int], WindowHit]], hit: WindowHit, limit: int, mode: str) -> None:
    if mode == "latest":
        key = (hit.window_start_depth - hit.scope_depth, hit.window_end_depth, hit.start)
    elif mode == "deficit":
        key = (hit.deficit_bits, hit.length, hit.start)
    elif mode == "critical":
        key = (-hit.deficit_bits / hit.length if hit.length else 0.0, hit.length, hit.start)
    else:
        raise ValueError(f"unknown mode {mode}")
    if len(heap) < limit:
        heapq.heappush(heap, (key, hit))
    elif key > heap[0][0]:
        heapq.heapreplace(heap, (key, hit))


def strongest_windows(
    start: int,
    scope: str,
    scope_depth: int,
    peak_depth: int,
    certificate_depth: int | None,
    prefix_odd: list[int],
    lengths: list[int],
    min_deficit_bits: float,
    max_odd_ratio: float | None,
    top_n: int,
) -> dict[str, list[dict[str, int | float | str | None]]]:
    depth_limit = len(prefix_odd) - 1
    deficit_heap: list[tuple[tuple[float, int, int], WindowHit]] = []
    critical_heap: list[tuple[tuple[float, int, int], WindowHit]] = []
    for window_start in range(scope_depth, depth_limit + 1):
        for length in lengths:
            window_end = window_start + length
            if window_end > depth_limit:
                continue
            odd_count = prefix_odd[window_end] - prefix_odd[window_start]
            deficit = length - odd_count * LOG2_3
            odd_ratio = odd_count / length if length else 0.0
            if deficit < min_deficit_bits or (max_odd_ratio is not None and odd_ratio > max_odd_ratio):
                continue
            hit = WindowHit(
                start=start,
                scope=scope,
                scope_depth=scope_depth,
                window_start_depth=window_start,
                window_end_depth=window_end,
                length=length,
                odd_count=odd_count,
                deficit_bits=deficit,
                odd_ratio=odd_ratio,
                peak_depth=peak_depth,
                certificate_depth=certificate_depth,
            )
            top_push(deficit_heap, hit, top_n, "deficit")
            top_push(critical_heap, hit, top_n, "critical")

    return {
        "top_by_deficit": [
            hit.as_dict() for _, hit in sorted(deficit_heap, key=lambda item: item[0], reverse=True)
        ],
        "closest_to_threshold": [
            hit.as_dict() for _, hit in sorted(critical_heap, key=lambda item: item[0], reverse=True)
        ],
    }


def analyze_start(
    start: int,
    max_depth: int,
    pow3: list[int],
    lengths: list[int],
    scope: str,
    base_depth: int | None,
    min_deficit_bits: float,
    max_odd_ratio: float | None,
    include_strongest: bool,
    top_n: int,
) -> dict[str, object]:
    profile = trajectory_profile(start, max_depth, pow3)
    cert = profile["certificate"]
    assert isinstance(cert, dict)
    prefix_odd = profile["prefix_odd"]
    assert isinstance(prefix_odd, list)
    peak_depth = int(profile["peak_depth"])
    scope_depth = choose_scope_depth(scope, base_depth, peak_depth)
    certificate_depth = int(cert["depth"]) if cert["depth"] is not None else None
    hit = find_first_window(
        start=start,
        scope=scope,
        scope_depth=scope_depth,
        peak_depth=peak_depth,
        certificate_depth=certificate_depth,
        prefix_odd=[int(value) for value in prefix_odd],
        lengths=lengths,
        min_deficit_bits=min_deficit_bits,
        max_odd_ratio=max_odd_ratio,
    )
    row: dict[str, object] = {
        "start": start,
        "bit_length": start.bit_length(),
        "certified": bool(cert["certified"]),
        "certificate_depth": certificate_depth,
        "certificate_odd_count": int(cert["odd_count"]) if cert["odd_count"] is not None else None,
        "depth_limit": int(profile["depth_limit"]),
        "peak_depth": peak_depth,
        "peak_dual_debt_bits": round_float(float(profile["peak_dual_debt_bits"])),
        "scope": scope,
        "scope_depth": scope_depth,
        "first_forced_window": hit.as_dict() if hit else None,
    }
    if include_strongest:
        row["strong_windows"] = strongest_windows(
            start=start,
            scope=scope,
            scope_depth=scope_depth,
            peak_depth=peak_depth,
            certificate_depth=certificate_depth,
            prefix_odd=[int(value) for value in prefix_odd],
            lengths=lengths,
            min_deficit_bits=min_deficit_bits,
            max_odd_ratio=max_odd_ratio,
            top_n=top_n,
        )
    return row


def frontier_starts(
    base_depth: int,
    max_depth: int,
    max_frontier: int | None,
    sample_stride: int,
    sample_offset: int,
) -> tuple[list[int], dict[str, object]]:
    frontier, stats = enumerate_frontier(base_depth, powers_of_three(max_depth))
    selected = sorted(frontier, key=lambda leaf: leaf.residue)
    if sample_stride > 1:
        selected = [leaf for index, leaf in enumerate(selected) if index % sample_stride == sample_offset]
    if max_frontier is not None:
        selected = selected[:max_frontier]
    return [leaf.residue for leaf in selected if leaf.residue > 0], {
        **stats,
        "selected_count": len(selected),
        "sample_stride": sample_stride,
        "sample_offset": sample_offset,
        "max_frontier": max_frontier,
    }


def summarize(rows: list[dict[str, object]], top_n: int) -> dict[str, object]:
    hits = [row["first_forced_window"] for row in rows if isinstance(row.get("first_forced_window"), dict)]
    missing = [int(row["start"]) for row in rows if row.get("first_forced_window") is None]
    motif_counts = Counter(str(hit["motif"]) for hit in hits)
    waits = [int(hit["wait_after_scope"]) for hit in hits]
    ends = [int(hit["window_end_depth"]) for hit in hits]
    rates = [float(hit["deficit_per_step_bits"]) for hit in hits]
    return {
        "analyzed_count": len(rows),
        "forced_count": len(hits),
        "unforced_count": len(missing),
        "unforced_samples": missing[:top_n],
        "distinct_first_motifs": len(motif_counts),
        "max_wait_after_scope": max(waits) if waits else None,
        "max_forcing_end_depth": max(ends) if ends else None,
        "min_deficit_per_step_bits": round_float(min(rates)) if rates else None,
        "mean_deficit_per_step_bits": round_float(mean(rates)) if rates else None,
        "most_common_first_motifs": [
            {"motif": motif, "count": count} for motif, count in motif_counts.most_common(top_n)
        ],
        "latest_forcing_windows": sorted(
            [hit for hit in hits],
            key=lambda hit: (int(hit["wait_after_scope"]), int(hit["window_end_depth"]), int(hit["start"])),
            reverse=True,
        )[:top_n],
        "closest_to_threshold_first_windows": sorted(
            [hit for hit in hits],
            key=lambda hit: (float(hit["deficit_per_step_bits"]), -int(hit["length"]), int(hit["start"])),
        )[:top_n],
    }


def compact_rows(rows: list[dict[str, object]], top_n: int) -> list[dict[str, object]]:
    return rows[:top_n]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--starts", nargs="+", help="explicit starts; accepts comma-separated values")
    parser.add_argument("--limit", type=int, default=0, help="also scan starts 1..limit")
    parser.add_argument("--frontier-base-depth", type=int, default=0, help="also scan exact survivor frontier")
    parser.add_argument("--max-depth", type=int, default=1200, help="trajectory/certificate search depth")
    parser.add_argument("--window-lengths", help="comma/range list, e.g. 8-64,209,210")
    parser.add_argument("--min-window-length", type=int, default=8, help="used when --window-lengths is omitted")
    parser.add_argument("--max-window-length", type=int, default=256, help="used when --window-lengths is omitted")
    parser.add_argument("--min-deficit-bits", type=float, default=0.01, help="minimum positive deficit")
    parser.add_argument("--max-odd-ratio", type=float, help="optional odd-ratio ceiling")
    parser.add_argument(
        "--scope",
        choices=["start", "post-base", "post-peak"],
        default="post-peak",
        help="where motif search may begin",
    )
    parser.add_argument("--max-frontier", type=int, help="frontier mode: analyze at most this many leaves")
    parser.add_argument("--sample-stride", type=int, default=1, help="frontier mode: analyze every kth leaf")
    parser.add_argument("--sample-offset", type=int, default=0, help="frontier mode offset")
    parser.add_argument("--top-n", type=int, default=12, help="top rows per table")
    parser.add_argument("--summary", action="store_true", help="omit compact per-start rows")
    parser.add_argument("--include-strongest", action="store_true", help="include strongest windows per start")
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
    if args.min_window_length < 1:
        raise SystemExit("--min-window-length must be at least 1")
    if args.max_window_length < args.min_window_length:
        raise SystemExit("--max-window-length must be at least --min-window-length")

    lengths = parse_lengths(args.window_lengths, args.min_window_length, args.max_window_length)
    explicit_starts = parse_ints(args.starts)
    if not explicit_starts and args.limit == 0 and args.frontier_base_depth == 0:
        explicit_starts = DEFAULT_HARD_STARTS
    if any(start < 1 for start in explicit_starts):
        raise SystemExit("--starts must contain positive integers")

    started = perf_counter()
    frontier_meta = None
    frontier_values: list[int] = []
    if args.frontier_base_depth:
        if args.frontier_base_depth < 1:
            raise SystemExit("--frontier-base-depth must be positive when provided")
        frontier_values, frontier_meta = frontier_starts(
            base_depth=args.frontier_base_depth,
            max_depth=args.max_depth,
            max_frontier=args.max_frontier,
            sample_stride=args.sample_stride,
            sample_offset=args.sample_offset,
        )

    starts = unique_preserving_order([*explicit_starts, *range(1, args.limit + 1), *frontier_values])
    pow3 = powers_of_three(args.max_depth)
    rows = [
        analyze_start(
            start=start,
            max_depth=args.max_depth,
            pow3=pow3,
            lengths=lengths,
            scope=args.scope,
            base_depth=args.frontier_base_depth if args.frontier_base_depth else None,
            min_deficit_bits=args.min_deficit_bits,
            max_odd_ratio=args.max_odd_ratio,
            include_strongest=args.include_strongest,
            top_n=args.top_n,
        )
        for start in starts
    ]

    payload: dict[str, object] = {
        "status": "motif-forcing-analysis",
        "elapsed_seconds": round_float(perf_counter() - started, 6),
        "parameters": {
            "starts": explicit_starts,
            "limit": args.limit,
            "frontier_base_depth": args.frontier_base_depth or None,
            "max_depth": args.max_depth,
            "window_lengths": lengths if len(lengths) <= 32 else f"{lengths[0]}..{lengths[-1]} ({len(lengths)} lengths)",
            "min_deficit_bits": args.min_deficit_bits,
            "max_odd_ratio": args.max_odd_ratio,
            "scope": args.scope,
            "critical_odd_ratio": round_float(CRITICAL_ODD_RATIO),
        },
        "frontier": frontier_meta,
        "summary": summarize(rows, args.top_n),
        "interpretation": (
            "This is a finite-shadow forcing test. A forced window means the deterministic "
            "trajectory contains a chosen subcritical motif after the selected scope depth. "
            "The all-odd 2-adic path is not ruled out by this test; the point is to measure "
            "how positive finite shadows separate from it."
        ),
    }
    if not args.summary:
        payload["rows"] = compact_rows(rows, args.top_n)
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

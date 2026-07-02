#!/usr/bin/env python3
"""Compress repayment motifs into coarse cover families.

The motif miner shows that finite positive shadows repay debt through concrete
subcritical parity windows.  This script asks whether those windows compress
into a small number of coarse motif families.

It computes the peak-to-clear repayment motif for each selected start, then
groups motifs by:

* exact `(length, odd_count)`;
* length bands;
* odd-ratio bands;
* deficit-per-step bands;
* combined `(length band, odd-ratio band)` cover families.

The output is finite evidence only.  A compact cover in a finite frontier is not
a proof, but it is a candidate shape for a future uniform motif-forcing theorem.
"""

from __future__ import annotations

import argparse
import json
import math
from collections import Counter, defaultdict
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
class RepaymentMotif:
    start: int
    bit_length: int
    certificate_depth: int
    certificate_odd_count: int
    peak_depth: int
    peak_dual_debt_bits: float
    length: int
    odd_count: int
    deficit_bits: float
    clearance_margin_bits: float

    @property
    def exact_key(self) -> str:
        return f"{self.length}:{self.odd_count}"

    @property
    def odd_ratio(self) -> float:
        return self.odd_count / self.length if self.length else 0.0

    @property
    def deficit_per_step_bits(self) -> float:
        return self.deficit_bits / self.length if self.length else 0.0

    @property
    def post_peak_coverage_ratio(self) -> float:
        return self.length / self.certificate_depth if self.certificate_depth else 0.0

    def as_dict(self) -> dict[str, int | float | str]:
        return {
            "start": self.start,
            "bit_length": self.bit_length,
            "certificate_depth": self.certificate_depth,
            "certificate_odd_count": self.certificate_odd_count,
            "peak_depth": self.peak_depth,
            "peak_dual_debt_bits": round_float(self.peak_dual_debt_bits),
            "motif": self.exact_key,
            "length": self.length,
            "odd_count": self.odd_count,
            "odd_ratio": round_float(self.odd_ratio),
            "deficit_bits": round_float(self.deficit_bits),
            "deficit_per_step_bits": round_float(self.deficit_per_step_bits),
            "clearance_margin_bits": round_float(self.clearance_margin_bits),
            "post_peak_coverage_ratio": round_float(self.post_peak_coverage_ratio),
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


def band_label(value: float, width: float, digits: int = 3) -> str:
    if width <= 0:
        raise ValueError("band width must be positive")
    lower = math.floor(value / width) * width
    upper = lower + width
    return f"{lower:.{digits}f}-{upper:.{digits}f}"


def length_band(length: int, width: int) -> str:
    lower = (length // width) * width
    upper = lower + width - 1
    return f"{lower}-{upper}"


def classify_motif(motif: RepaymentMotif) -> str:
    if motif.length >= 192 and motif.odd_ratio >= 0.59:
        return "slow-critical-long"
    if motif.length >= 128 and motif.odd_ratio >= 0.56:
        return "slow-long"
    if motif.peak_dual_debt_bits >= 20 and motif.deficit_per_step_bits >= 0.12:
        return "high-debt-fast"
    if motif.length <= 32 and motif.deficit_per_step_bits >= 0.30:
        return "short-high-deficit"
    if motif.deficit_per_step_bits < 0.08:
        return "low-slope"
    return "mixed"


def repayment_motif_for_start(start: int, max_depth: int, pow3: list[int]) -> RepaymentMotif | None:
    cert = certificate_for_start(start, max_depth, pow3)
    if not cert["certified"] or cert["depth"] is None:
        return None

    certificate_depth = int(cert["depth"])
    x = start
    odd_count = 0
    prefix_odd = [0]
    values: list[int] = [start]
    dual_debts: list[float] = []

    for depth in range(1, certificate_depth + 1):
        was_odd = x & 1
        odd_count += was_odd
        x = shortcut(x)
        prefix_odd.append(odd_count)
        values.append(x)
        multiplier_debt = odd_count * LOG2_3 - depth
        height_debt = math.log2(x) - math.log2(start) if start > 0 else float("-inf")
        dual_debts.append(max(multiplier_debt, height_debt))

    if dual_debts:
        peak_depth, peak_dual_debt = max(enumerate(dual_debts, start=1), key=lambda item: (item[1], -item[0]))
    else:
        peak_depth = 0
        peak_dual_debt = 0.0

    length = certificate_depth - peak_depth
    if length < 0:
        return None
    interval_odd_count = prefix_odd[certificate_depth] - prefix_odd[peak_depth]
    deficit = length - interval_odd_count * LOG2_3
    final_dual_debt = dual_debts[-1] if dual_debts else 0.0
    return RepaymentMotif(
        start=start,
        bit_length=start.bit_length(),
        certificate_depth=certificate_depth,
        certificate_odd_count=int(cert["odd_count"]) if cert["odd_count"] is not None else prefix_odd[-1],
        peak_depth=peak_depth,
        peak_dual_debt_bits=peak_dual_debt,
        length=length,
        odd_count=interval_odd_count,
        deficit_bits=deficit,
        clearance_margin_bits=-final_dual_debt,
    )


def frontier_values(
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


def top_counter(counter: Counter[str], top_n: int) -> list[dict[str, int | str]]:
    return [{"key": key, "count": count} for key, count in counter.most_common(top_n)]


def greedy_cover(
    motif_indices_by_family: dict[str, set[int]],
    universe_size: int,
    top_n: int,
    target_fraction: float,
) -> list[dict[str, int | float | str]]:
    uncovered = set(range(universe_size))
    selected: list[dict[str, int | float | str]] = []
    target_count = math.ceil(universe_size * target_fraction)

    while uncovered and universe_size - len(uncovered) < target_count:
        best_family = None
        best_hits: set[int] = set()
        for family, indices in motif_indices_by_family.items():
            hits = indices & uncovered
            if len(hits) > len(best_hits):
                best_family = family
                best_hits = hits
        if best_family is None or not best_hits:
            break
        uncovered -= best_hits
        covered = universe_size - len(uncovered)
        selected.append(
            {
                "family": best_family,
                "newly_covered": len(best_hits),
                "covered_total": covered,
                "covered_fraction": round_float(covered / universe_size if universe_size else 0.0),
            }
        )
        if len(selected) >= top_n:
            break
    return selected


def summarize(
    motifs: list[RepaymentMotif],
    top_n: int,
    length_bin_size: int,
    ratio_bin_size: float,
    deficit_bin_size: float,
    cover_target: float,
) -> dict[str, object]:
    exact_counter: Counter[str] = Counter()
    length_counter: Counter[str] = Counter()
    ratio_counter: Counter[str] = Counter()
    deficit_counter: Counter[str] = Counter()
    class_counter: Counter[str] = Counter()
    combined_counter: Counter[str] = Counter()
    family_indices: dict[str, set[int]] = defaultdict(set)

    for index, motif in enumerate(motifs):
        exact_counter[motif.exact_key] += 1
        length_key = length_band(motif.length, length_bin_size)
        ratio_key = band_label(motif.odd_ratio, ratio_bin_size, digits=3)
        deficit_key = band_label(motif.deficit_per_step_bits, deficit_bin_size, digits=3)
        class_key = classify_motif(motif)
        combined_key = f"L{length_key}|r{ratio_key}"

        length_counter[length_key] += 1
        ratio_counter[ratio_key] += 1
        deficit_counter[deficit_key] += 1
        class_counter[class_key] += 1
        combined_counter[combined_key] += 1

        family_indices[f"class:{class_key}"].add(index)
        family_indices[f"length:{length_key}"].add(index)
        family_indices[f"ratio:{ratio_key}"].add(index)
        family_indices[f"deficit:{deficit_key}"].add(index)
        family_indices[f"length_ratio:{combined_key}"].add(index)

    lengths = [motif.length for motif in motifs]
    ratios = [motif.odd_ratio for motif in motifs]
    deficits = [motif.deficit_per_step_bits for motif in motifs]
    cert_depths = [motif.certificate_depth for motif in motifs]
    peak_debts = [motif.peak_dual_debt_bits for motif in motifs]

    return {
        "motif_count": len(motifs),
        "distinct_exact_motifs": len(exact_counter),
        "distinct_length_ratio_families": len(combined_counter),
        "length": {
            "min": min(lengths) if lengths else None,
            "max": max(lengths) if lengths else None,
            "mean": round_float(mean(lengths)) if lengths else None,
        },
        "odd_ratio": {
            "min": round_float(min(ratios)) if ratios else None,
            "max": round_float(max(ratios)) if ratios else None,
            "mean": round_float(mean(ratios)) if ratios else None,
            "critical": round_float(CRITICAL_ODD_RATIO),
        },
        "deficit_per_step_bits": {
            "min": round_float(min(deficits)) if deficits else None,
            "max": round_float(max(deficits)) if deficits else None,
            "mean": round_float(mean(deficits)) if deficits else None,
        },
        "certificate_depth": {
            "max": max(cert_depths) if cert_depths else None,
        },
        "peak_dual_debt_bits": {
            "max": round_float(max(peak_debts)) if peak_debts else None,
        },
        "top_exact_motifs": top_counter(exact_counter, top_n),
        "top_length_bands": top_counter(length_counter, top_n),
        "top_ratio_bands": top_counter(ratio_counter, top_n),
        "top_deficit_bands": top_counter(deficit_counter, top_n),
        "class_histogram": {key: class_counter[key] for key in sorted(class_counter)},
        "top_length_ratio_families": top_counter(combined_counter, top_n),
        "greedy_cover": greedy_cover(family_indices, len(motifs), top_n, cover_target),
        "hardest_by_certificate_depth": [
            motif.as_dict()
            for motif in sorted(motifs, key=lambda item: (item.certificate_depth, item.start), reverse=True)[:top_n]
        ],
        "slowest_by_deficit_rate": [
            motif.as_dict()
            for motif in sorted(
                motifs,
                key=lambda item: (item.deficit_per_step_bits, -item.length, item.start),
            )[:top_n]
        ],
        "largest_peak_debt": [
            motif.as_dict()
            for motif in sorted(motifs, key=lambda item: (item.peak_dual_debt_bits, item.start), reverse=True)[
                :top_n
            ]
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--starts", nargs="+", help="explicit starts; accepts comma-separated values")
    parser.add_argument("--limit", type=int, default=0, help="also scan starts 1..limit")
    parser.add_argument("--frontier-base-depth", type=int, default=0, help="also scan exact survivor frontier")
    parser.add_argument("--max-depth", type=int, default=1200, help="certificate/debt search depth")
    parser.add_argument("--max-frontier", type=int, help="frontier mode: analyze at most this many leaves")
    parser.add_argument("--sample-stride", type=int, default=1, help="frontier mode: analyze every kth leaf")
    parser.add_argument("--sample-offset", type=int, default=0, help="frontier mode offset")
    parser.add_argument("--length-bin-size", type=int, default=16, help="length band width")
    parser.add_argument("--ratio-bin-size", type=float, default=0.025, help="odd-ratio band width")
    parser.add_argument("--deficit-bin-size", type=float, default=0.05, help="deficit-per-step band width")
    parser.add_argument("--cover-target", type=float, default=0.95, help="greedy cover target fraction")
    parser.add_argument("--top-n", type=int, default=12, help="top rows per table")
    parser.add_argument("--summary", action="store_true", help="omit individual motif rows")
    args = parser.parse_args()

    if args.max_depth < 1:
        raise SystemExit("--max-depth must be at least 1")
    if args.limit < 0:
        raise SystemExit("--limit must be nonnegative")
    if args.sample_stride < 1:
        raise SystemExit("--sample-stride must be at least 1")
    if not 0 <= args.sample_offset < args.sample_stride:
        raise SystemExit("--sample-offset must satisfy 0 <= offset < stride")
    if args.length_bin_size < 1:
        raise SystemExit("--length-bin-size must be positive")
    if args.ratio_bin_size <= 0 or args.deficit_bin_size <= 0:
        raise SystemExit("ratio/deficit bin sizes must be positive")
    if not 0 < args.cover_target <= 1:
        raise SystemExit("--cover-target must satisfy 0 < target <= 1")
    if args.top_n < 1:
        raise SystemExit("--top-n must be positive")

    started = perf_counter()
    explicit_starts = parse_ints(args.starts)
    if not explicit_starts and args.limit == 0 and args.frontier_base_depth == 0:
        explicit_starts = DEFAULT_HARD_STARTS
    if any(start < 1 for start in explicit_starts):
        raise SystemExit("--starts must contain positive integers")

    frontier_meta = None
    frontier_starts: list[int] = []
    if args.frontier_base_depth:
        if args.frontier_base_depth < 1:
            raise SystemExit("--frontier-base-depth must be positive when provided")
        frontier_starts, frontier_meta = frontier_values(
            base_depth=args.frontier_base_depth,
            max_depth=args.max_depth,
            max_frontier=args.max_frontier,
            sample_stride=args.sample_stride,
            sample_offset=args.sample_offset,
        )

    starts = unique_preserving_order([*explicit_starts, *range(1, args.limit + 1), *frontier_starts])
    pow3 = powers_of_three(args.max_depth)
    motifs = [
        motif
        for start in starts
        if (motif := repayment_motif_for_start(start, args.max_depth, pow3)) is not None
    ]

    payload: dict[str, object] = {
        "status": "motif-cover-analysis",
        "elapsed_seconds": round_float(perf_counter() - started, 6),
        "parameters": {
            "starts": explicit_starts,
            "limit": args.limit,
            "frontier_base_depth": args.frontier_base_depth or None,
            "max_depth": args.max_depth,
            "length_bin_size": args.length_bin_size,
            "ratio_bin_size": args.ratio_bin_size,
            "deficit_bin_size": args.deficit_bin_size,
            "cover_target": args.cover_target,
        },
        "frontier": frontier_meta,
        "summary": summarize(
            motifs=motifs,
            top_n=args.top_n,
            length_bin_size=args.length_bin_size,
            ratio_bin_size=args.ratio_bin_size,
            deficit_bin_size=args.deficit_bin_size,
            cover_target=args.cover_target,
        ),
        "interpretation": (
            "A compact finite cover of observed repayment motifs suggests a candidate "
            "motif-family taxonomy. It is not a proof unless the cover is derived uniformly "
            "for all positive finite shadows rather than mined at a fixed depth."
        ),
    }
    if not args.summary:
        payload["motifs"] = [motif.as_dict() for motif in motifs[: args.top_n]]
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Mine subcritical repayment motifs in hard Collatz trajectories.

`repayment_envelope_scan.py` measures the interval from peak dual debt to first
clearance.  This script keeps the actual parity word of that interval and
groups repeated motifs by `(length, odd_count)`.

The goal is to turn "there is a repayment window" into a more structural
object:

    interval length L
    odd count a
    deficit L - a log2(3)
    parity-run grammar inside the interval

For explicit starts, the script can also mine all subcritical intervals in the
trajectory up to the first usable certificate.  That is intentionally bounded
to explicit starts because all-interval mining is quadratic in certificate
depth.
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
class MotifRecord:
    start: int
    start_depth: int
    end_depth: int
    length: int
    odd_count: int
    odd_ratio: float
    deficit_bits: float
    deficit_per_step_bits: float
    role: str
    run_count: int
    longest_odd_run: int
    longest_even_run: int
    first_runs: tuple[str, ...]
    last_runs: tuple[str, ...]
    bit_sample: str

    def as_dict(self) -> dict[str, int | float | str | list[str]]:
        return {
            "start": self.start,
            "start_depth": self.start_depth,
            "end_depth": self.end_depth,
            "length": self.length,
            "odd_count": self.odd_count,
            "odd_ratio": round_float(self.odd_ratio),
            "critical_odd_ratio": round_float(CRITICAL_ODD_RATIO),
            "deficit_bits": round_float(self.deficit_bits),
            "deficit_per_step_bits": round_float(self.deficit_per_step_bits),
            "role": self.role,
            "run_count": self.run_count,
            "longest_odd_run": self.longest_odd_run,
            "longest_even_run": self.longest_even_run,
            "first_runs": list(self.first_runs),
            "last_runs": list(self.last_runs),
            "bit_sample": self.bit_sample,
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


def parity_runs(bits: list[int]) -> list[tuple[int, int]]:
    if not bits:
        return []
    runs: list[tuple[int, int]] = []
    current = bits[0]
    length = 1
    for bit in bits[1:]:
        if bit == current:
            length += 1
        else:
            runs.append((current, length))
            current = bit
            length = 1
    runs.append((current, length))
    return runs


def run_labels(runs: list[tuple[int, int]], limit: int) -> tuple[str, ...]:
    return tuple(f"{bit}^{length}" for bit, length in runs[:limit])


def bit_sample(bits: list[int], edge: int = 32) -> str:
    if len(bits) <= edge * 2 + 1:
        return "".join(str(bit) for bit in bits)
    return "".join(str(bit) for bit in bits[:edge]) + "..." + "".join(str(bit) for bit in bits[-edge:])


def interval_role(start_depth: int, end_depth: int, peak_depth: int, clear_depth: int | None) -> str:
    if end_depth <= peak_depth:
        return "pre-peak"
    if start_depth >= peak_depth:
        return "post-peak"
    if clear_depth is not None and start_depth <= peak_depth and end_depth >= clear_depth:
        return "peak-to-clear-cover"
    return "cross-peak"


def make_motif(
    start: int,
    start_depth: int,
    end_depth: int,
    prefix_odd: list[int],
    bits: list[int],
    peak_depth: int,
    clear_depth: int | None,
    run_limit: int,
) -> MotifRecord:
    length = end_depth - start_depth
    odd_count = prefix_odd[end_depth] - prefix_odd[start_depth]
    interval_bits = bits[start_depth:end_depth]
    runs = parity_runs(interval_bits)
    deficit = length - odd_count * LOG2_3
    odd_ratio = odd_count / length if length else 0.0
    return MotifRecord(
        start=start,
        start_depth=start_depth,
        end_depth=end_depth,
        length=length,
        odd_count=odd_count,
        odd_ratio=odd_ratio,
        deficit_bits=deficit,
        deficit_per_step_bits=deficit / length if length else 0.0,
        role=interval_role(start_depth, end_depth, peak_depth, clear_depth),
        run_count=len(runs),
        longest_odd_run=max((length for bit, length in runs if bit == 1), default=0),
        longest_even_run=max((length for bit, length in runs if bit == 0), default=0),
        first_runs=run_labels(runs, run_limit),
        last_runs=run_labels(runs[-run_limit:], run_limit),
        bit_sample=bit_sample(interval_bits),
    )


def analyze_start(start: int, max_depth: int, pow3: list[int], run_limit: int) -> dict[str, object]:
    cert = certificate_for_start(start, max_depth, pow3)
    if not cert["certified"] or cert["depth"] is None:
        return {
            "start": start,
            "bit_length": start.bit_length(),
            "certified": False,
            "certificate": cert,
            "trajectory_depth": max_depth,
            "repayment_motif": None,
            "bits": [],
            "prefix_odd": [0],
            "peak": None,
            "clear_depth": None,
        }

    depth_limit = int(cert["depth"])
    x = start
    bits: list[int] = []
    prefix_odd = [0]
    dual_debts: list[float] = []
    first_clear_depth: int | None = None

    for depth in range(1, depth_limit + 1):
        was_odd = x & 1
        bits.append(was_odd)
        x = shortcut(x)
        odd_count = prefix_odd[-1] + was_odd
        prefix_odd.append(odd_count)
        multiplier_debt = odd_count * LOG2_3 - depth
        height_debt = math.log2(x) - math.log2(start) if start > 0 else float("-inf")
        dual_debt = max(multiplier_debt, height_debt)
        dual_debts.append(dual_debt)
        if first_clear_depth is None and pow3[odd_count] < (1 << depth) and x < start:
            first_clear_depth = depth

    if dual_debts:
        peak_index, peak_debt = max(enumerate(dual_debts, start=1), key=lambda item: (item[1], -item[0]))
    else:
        peak_index = 0
        peak_debt = 0.0

    repayment_motif = None
    if first_clear_depth is not None and first_clear_depth >= peak_index:
        repayment_motif = make_motif(
            start=start,
            start_depth=peak_index,
            end_depth=first_clear_depth,
            prefix_odd=prefix_odd,
            bits=bits,
            peak_depth=peak_index,
            clear_depth=first_clear_depth,
            run_limit=run_limit,
        )

    return {
        "start": start,
        "bit_length": start.bit_length(),
        "certified": True,
        "certificate": cert,
        "trajectory_depth": depth_limit,
        "repayment_motif": repayment_motif.as_dict() if repayment_motif else None,
        "bits": bits,
        "prefix_odd": prefix_odd,
        "peak": {
            "depth": peak_index,
            "dual_debt_bits": round_float(peak_debt),
            "odd_count": prefix_odd[peak_index] if peak_index < len(prefix_odd) else 0,
        },
        "clear_depth": first_clear_depth,
    }


def motif_key(motif: dict[str, object]) -> str:
    return f"{motif['length']}:{motif['odd_count']}"


def summarize_repayment_motifs(rows: list[dict[str, object]], top_n: int) -> dict[str, object]:
    motifs = [row["repayment_motif"] for row in rows if row.get("repayment_motif")]
    typed_motifs = [motif for motif in motifs if isinstance(motif, dict)]
    motif_counts = Counter(motif_key(motif) for motif in typed_motifs)
    class_counts = Counter(str(motif["role"]) for motif in typed_motifs)
    rates = [float(motif["deficit_per_step_bits"]) for motif in typed_motifs if float(motif["length"]) > 0]
    lengths = [int(motif["length"]) for motif in typed_motifs]
    deficits = [float(motif["deficit_bits"]) for motif in typed_motifs]

    top_motifs = []
    for key, count in motif_counts.most_common(top_n):
        length_text, odd_text = key.split(":")
        length = int(length_text)
        odd_count = int(odd_text)
        ratio = odd_count / length if length else 0.0
        deficit = length - odd_count * LOG2_3
        examples = [
            int(row["start"])
            for row in rows
            if isinstance(row.get("repayment_motif"), dict) and motif_key(row["repayment_motif"]) == key
        ][: min(5, top_n)]
        top_motifs.append(
            {
                "motif": key,
                "count": count,
                "length": length,
                "odd_count": odd_count,
                "odd_ratio": round_float(ratio),
                "deficit_bits": round_float(deficit),
                "deficit_per_step_bits": round_float(deficit / length if length else 0.0),
                "example_starts": examples,
            }
        )

    return {
        "motif_count": len(typed_motifs),
        "distinct_length_odd_motifs": len(motif_counts),
        "role_histogram": {key: class_counts[key] for key in sorted(class_counts)},
        "max_repayment_length": max(lengths) if lengths else None,
        "max_repayment_deficit_bits": round_float(max(deficits)) if deficits else None,
        "min_deficit_per_step_bits": round_float(min(rates)) if rates else None,
        "mean_deficit_per_step_bits": round_float(mean(rates)) if rates else None,
        "most_common_length_odd_motifs": top_motifs,
        "top_by_length": sorted(
            [motif for motif in typed_motifs],
            key=lambda motif: (int(motif["length"]), float(motif["deficit_bits"]), int(motif["start"])),
            reverse=True,
        )[:top_n],
        "top_by_deficit": sorted(
            [motif for motif in typed_motifs],
            key=lambda motif: (float(motif["deficit_bits"]), int(motif["length"]), int(motif["start"])),
            reverse=True,
        )[:top_n],
        "closest_to_critical": sorted(
            [motif for motif in typed_motifs if int(motif["length"]) > 0],
            key=lambda motif: (
                float(motif["deficit_per_step_bits"]),
                -int(motif["length"]),
                int(motif["start"]),
            ),
        )[:top_n],
    }


def interval_sort_key(record: MotifRecord, mode: str) -> tuple[float, int, int, int]:
    if mode == "length":
        return (record.length, record.deficit_bits, record.end_depth, record.start)
    if mode == "deficit":
        return (record.deficit_bits, record.length, record.end_depth, record.start)
    if mode == "critical":
        return (-record.deficit_per_step_bits, record.length, record.end_depth, record.start)
    raise ValueError(f"unknown mode {mode}")


def top_push(heap: list[tuple[tuple[float, int, int, int], MotifRecord]], record: MotifRecord, limit: int, mode: str) -> None:
    key = interval_sort_key(record, mode)
    if len(heap) < limit:
        heapq.heappush(heap, (key, record))
    elif key > heap[0][0]:
        heapq.heapreplace(heap, (key, record))


def mine_all_subcritical_intervals(
    row: dict[str, object],
    min_length: int,
    max_length: int,
    top_n: int,
    run_limit: int,
) -> dict[str, object]:
    bits = row["bits"]
    prefix_odd = row["prefix_odd"]
    peak = row["peak"]
    clear_depth = row["clear_depth"]
    if not isinstance(bits, list) or not isinstance(prefix_odd, list) or not isinstance(peak, dict):
        return {"start": row["start"], "interval_count": 0}

    depth_limit = len(bits)
    peak_depth = int(peak["depth"])
    longest_heap: list[tuple[tuple[float, int, int, int], MotifRecord]] = []
    deficit_heap: list[tuple[tuple[float, int, int, int], MotifRecord]] = []
    critical_heap: list[tuple[tuple[float, int, int, int], MotifRecord]] = []
    role_counter: Counter[str] = Counter()
    interval_count = 0
    positive_count = 0

    for start_depth in range(depth_limit):
        max_end = min(depth_limit, start_depth + max_length)
        for end_depth in range(start_depth + min_length, max_end + 1):
            length = end_depth - start_depth
            odd_count = int(prefix_odd[end_depth]) - int(prefix_odd[start_depth])
            deficit = length - odd_count * LOG2_3
            interval_count += 1
            if deficit <= 0:
                continue
            positive_count += 1
            record = make_motif(
                start=int(row["start"]),
                start_depth=start_depth,
                end_depth=end_depth,
                prefix_odd=[int(value) for value in prefix_odd],
                bits=[int(value) for value in bits],
                peak_depth=peak_depth,
                clear_depth=int(clear_depth) if clear_depth is not None else None,
                run_limit=run_limit,
            )
            role_counter[record.role] += 1
            top_push(longest_heap, record, top_n, "length")
            top_push(deficit_heap, record, top_n, "deficit")
            top_push(critical_heap, record, top_n, "critical")

    def unpack(heap: list[tuple[tuple[float, int, int, int], MotifRecord]], reverse: bool = True) -> list[dict[str, object]]:
        return [record.as_dict() for _, record in sorted(heap, key=lambda item: item[0], reverse=reverse)]

    return {
        "start": int(row["start"]),
        "trajectory_depth": depth_limit,
        "min_length": min_length,
        "max_length": max_length,
        "interval_count": interval_count,
        "subcritical_interval_count": positive_count,
        "role_histogram": {key: role_counter[key] for key in sorted(role_counter)},
        "longest_subcritical": unpack(longest_heap),
        "max_deficit": unpack(deficit_heap),
        "closest_to_critical_positive": unpack(critical_heap),
    }


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


def compact_rows(rows: list[dict[str, object]], top_n: int) -> list[dict[str, object]]:
    compact = []
    for row in rows[:top_n]:
        compact.append(
            {
                "start": row["start"],
                "bit_length": row["bit_length"],
                "certified": row["certified"],
                "certificate_depth": row["certificate"]["depth"] if isinstance(row["certificate"], dict) else None,
                "certificate_odd_count": row["certificate"]["odd_count"]
                if isinstance(row["certificate"], dict)
                else None,
                "peak": row["peak"],
                "clear_depth": row["clear_depth"],
                "repayment_motif": row["repayment_motif"],
            }
        )
    return compact


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--starts", nargs="+", help="explicit starts; accepts comma-separated values")
    parser.add_argument("--limit", type=int, default=0, help="also scan starts 1..limit")
    parser.add_argument("--frontier-base-depth", type=int, default=0, help="also scan exact survivor frontier")
    parser.add_argument("--max-depth", type=int, default=1200, help="certificate search depth")
    parser.add_argument("--max-frontier", type=int, help="frontier mode: analyze at most this many leaves")
    parser.add_argument("--sample-stride", type=int, default=1, help="frontier mode: analyze every kth leaf")
    parser.add_argument("--sample-offset", type=int, default=0, help="frontier mode offset")
    parser.add_argument("--top-n", type=int, default=12, help="top rows per table")
    parser.add_argument("--run-limit", type=int, default=6, help="run labels kept at each motif edge")
    parser.add_argument("--summary", action="store_true", help="omit compact per-start rows")
    parser.add_argument("--all-intervals", action="store_true", help="mine all subcritical intervals for explicit starts")
    parser.add_argument("--min-interval-length", type=int, default=8, help="minimum interval length for all-interval mining")
    parser.add_argument("--max-interval-length", type=int, default=512, help="maximum interval length for all-interval mining")
    parser.add_argument(
        "--max-all-interval-starts",
        type=int,
        default=16,
        help="safety cap for all-interval mining",
    )
    args = parser.parse_args()

    if args.max_depth < 1:
        raise SystemExit("--max-depth must be at least 1")
    if args.limit < 0:
        raise SystemExit("--limit must be nonnegative")
    if args.sample_stride < 1:
        raise SystemExit("--sample-stride must be at least 1")
    if not 0 <= args.sample_offset < args.sample_stride:
        raise SystemExit("--sample-offset must satisfy 0 <= offset < stride")
    if args.top_n < 1:
        raise SystemExit("--top-n must be at least 1")
    if args.min_interval_length < 1:
        raise SystemExit("--min-interval-length must be at least 1")
    if args.max_interval_length < args.min_interval_length:
        raise SystemExit("--max-interval-length must be at least --min-interval-length")

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
    rows = [analyze_start(start, args.max_depth, pow3, args.run_limit) for start in starts]

    all_interval_payload = None
    if args.all_intervals:
        if len(explicit_starts) > args.max_all_interval_starts:
            raise SystemExit("--all-intervals only runs on explicit starts within --max-all-interval-starts")
        explicit_set = set(explicit_starts)
        all_interval_payload = [
            mine_all_subcritical_intervals(
                row=row,
                min_length=args.min_interval_length,
                max_length=args.max_interval_length,
                top_n=args.top_n,
                run_limit=args.run_limit,
            )
            for row in rows
            if int(row["start"]) in explicit_set
        ]

    payload: dict[str, object] = {
        "status": "repayment-motif-mining",
        "elapsed_seconds": round_float(perf_counter() - started, 6),
        "parameters": {
            "starts": explicit_starts,
            "limit": args.limit,
            "frontier_base_depth": args.frontier_base_depth or None,
            "max_depth": args.max_depth,
            "critical_odd_ratio": round_float(CRITICAL_ODD_RATIO),
            "all_intervals": args.all_intervals,
        },
        "frontier": frontier_meta,
        "summary": summarize_repayment_motifs(rows, args.top_n),
        "interpretation": (
            "Repeated repayment motifs are finite parity words whose odd density is below "
            "log_3(2).  A proof along the certificate route would need to show that every "
            "positive finite shadow of the 2-adic survivor frontier eventually forces one "
            "of these subcritical motif classes with enough deficit to clear accumulated debt."
        ),
    }
    if all_interval_payload is not None:
        payload["all_interval_mining"] = all_interval_payload
    if not args.summary:
        payload["rows"] = compact_rows(rows, max(args.top_n, len(explicit_starts)))
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Mine low-bit terminal residue covers for rare outlier endpoints.

The endpoint analyzer showed that rare outlier certificates land in terminal
classes after one descent generation.  This script compresses those endpoints
as residue buckets modulo `2^k` and asks:

    How many low endpoint bits are enough for every bucket to have one
    terminal next-class label?

This gives a finite "terminal residue grammar" for the observed endpoint set.
It is still finite evidence, not a proof that every future rare endpoint lands
in the same buckets.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from time import perf_counter

from endpoint_terminal_analyzer import endpoint_record_for_start, selected_starts
from motif_cover_analyzer import DEFAULT_HARD_STARTS, powers_of_three
from outlier_transition_analyzer import DEFAULT_TERMINAL_CLASSES, parse_classes
from repayment_envelope_scan import parse_ints, round_float


def bits(value: int, width: int) -> str:
    return format(value, f"0{width}b")


def bucket_key(endpoint: int, residue_bits: int) -> str:
    residue = endpoint & ((1 << residue_bits) - 1)
    return f"{residue}/{1 << residue_bits} ({bits(residue, residue_bits)})"


def cover_for_bits(records: list[object], residue_bits: int) -> dict[str, object]:
    buckets: dict[int, list[object]] = defaultdict(list)
    for record in records:
        buckets[record.endpoint & ((1 << residue_bits) - 1)].append(record)

    pure_buckets = 0
    records_in_pure_buckets = 0
    class_hist = Counter()
    bucket_rows = []
    for residue, members in sorted(buckets.items(), key=lambda item: (len(item[1]), item[0]), reverse=True):
        next_classes = Counter(member.next_class or "uncertified" for member in members)
        class_hist.update(next_classes)
        is_pure = len(next_classes) == 1
        if is_pure:
            pure_buckets += 1
            records_in_pure_buckets += len(members)
        bucket_rows.append(
            {
                "bucket": bucket_key(residue, residue_bits),
                "count": len(members),
                "pure": is_pure,
                "next_class_histogram": dict(sorted(next_classes.items())),
                "initial_class_histogram": dict(sorted(Counter(member.initial_class for member in members).items())),
                "endpoint_v2_histogram": dict(
                    sorted(Counter(str(member.endpoint_v2) for member in members).items(), key=lambda item: int(item[0]))
                ),
                "sample_starts": [member.start for member in members[:5]],
                "sample_endpoints": [member.endpoint for member in members[:5]],
            }
        )

    return {
        "residue_bits": residue_bits,
        "bucket_count": len(buckets),
        "pure_bucket_count": pure_buckets,
        "mixed_bucket_count": len(buckets) - pure_buckets,
        "records_in_pure_buckets": records_in_pure_buckets,
        "pure_record_fraction": round_float(records_in_pure_buckets / len(records) if records else 0.0),
        "next_class_histogram": dict(sorted(class_hist.items())),
        "largest_buckets": bucket_rows,
    }


def find_minimal_pure_cover(records: list[object], max_residue_bits: int) -> tuple[int | None, dict[str, object] | None]:
    for residue_bits in range(1, max_residue_bits + 1):
        cover = cover_for_bits(records, residue_bits)
        if cover["mixed_bucket_count"] == 0:
            return residue_bits, cover
    return None, None


def summarize(records: list[object], max_residue_bits: int, top_n: int) -> dict[str, object]:
    covers = [cover_for_bits(records, residue_bits) for residue_bits in range(1, max_residue_bits + 1)]
    min_bits, min_cover = find_minimal_pure_cover(records, max_residue_bits)
    endpoint_v2_hist = Counter(str(record.endpoint_v2) for record in records)
    next_hist = Counter(record.next_class or "uncertified" for record in records)
    initial_hist = Counter(record.initial_class for record in records)

    compact_rows = [
        {
            key: cover[key]
            for key in (
                "residue_bits",
                "bucket_count",
                "pure_bucket_count",
                "mixed_bucket_count",
                "records_in_pure_buckets",
                "pure_record_fraction",
            )
        }
        for cover in covers
    ]
    displayed_cover = None
    if min_cover is not None:
        displayed_cover = {
            **{key: min_cover[key] for key in min_cover if key != "largest_buckets"},
            "largest_buckets": min_cover["largest_buckets"][:top_n],
        }

    return {
        "record_count": len(records),
        "minimal_pure_cover_bits": min_bits,
        "initial_class_histogram": dict(sorted(initial_hist.items())),
        "next_class_histogram": dict(sorted(next_hist.items())),
        "endpoint_v2_histogram": dict(sorted(endpoint_v2_hist.items(), key=lambda item: int(item[0]))),
        "cover_progression": compact_rows,
        "minimal_pure_cover": displayed_cover,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--starts", nargs="+", help="explicit starts; accepts comma-separated values")
    parser.add_argument("--limit", type=int, default=0, help="also scan starts 1..limit")
    parser.add_argument("--frontier-base-depth", type=int, default=0, help="also scan exact survivor frontier")
    parser.add_argument("--max-depth", type=int, default=1200, help="certificate/debt search depth")
    parser.add_argument("--terminal-classes", help="comma-separated terminal classes")
    parser.add_argument("--include-terminal-initial", action="store_true", help="keep starts already in terminal classes")
    parser.add_argument("--max-frontier", type=int, help="frontier mode: analyze at most this many leaves")
    parser.add_argument("--sample-stride", type=int, default=1, help="frontier mode: analyze every kth leaf")
    parser.add_argument("--sample-offset", type=int, default=0, help="frontier mode offset")
    parser.add_argument("--max-residue-bits", type=int, default=12, help="largest endpoint residue width")
    parser.add_argument("--top-n", type=int, default=12, help="top rows per table")
    parser.add_argument("--summary", action="store_true", help="omit endpoint rows")
    args = parser.parse_args()

    if args.max_depth < 1:
        raise SystemExit("--max-depth must be at least 1")
    if args.limit < 0:
        raise SystemExit("--limit must be nonnegative")
    if args.sample_stride < 1:
        raise SystemExit("--sample-stride must be at least 1")
    if not 0 <= args.sample_offset < args.sample_stride:
        raise SystemExit("--sample-offset must satisfy 0 <= offset < stride")
    if args.max_residue_bits < 1:
        raise SystemExit("--max-residue-bits must be positive")
    if args.top_n < 1:
        raise SystemExit("--top-n must be positive")

    started = perf_counter()
    explicit_starts = parse_ints(args.starts)
    if not explicit_starts and args.limit == 0 and args.frontier_base_depth == 0:
        explicit_starts = DEFAULT_HARD_STARTS
    terminal_classes = parse_classes(args.terminal_classes)
    terminal_set = set(terminal_classes)

    starts, frontier_meta = selected_starts(
        explicit_starts=explicit_starts,
        limit=args.limit,
        frontier_base_depth=args.frontier_base_depth,
        max_depth=args.max_depth,
        max_frontier=args.max_frontier,
        sample_stride=args.sample_stride,
        sample_offset=args.sample_offset,
    )
    pow3 = powers_of_three(args.max_depth)

    records = []
    skipped_terminal_initial = 0
    uncertified_initial = 0
    nonterminal_next = 0
    for start in starts:
        record = endpoint_record_for_start(start, args.max_depth, pow3)
        if record is None:
            uncertified_initial += 1
            continue
        if record.initial_class in terminal_set and not args.include_terminal_initial:
            skipped_terminal_initial += 1
            continue
        if record.next_class not in terminal_set:
            nonterminal_next += 1
        records.append(record)

    payload: dict[str, object] = {
        "status": "terminal-residue-cover-analysis",
        "elapsed_seconds": round_float(perf_counter() - started, 6),
        "parameters": {
            "starts": explicit_starts,
            "limit": args.limit,
            "frontier_base_depth": args.frontier_base_depth or None,
            "max_depth": args.max_depth,
            "terminal_classes": list(terminal_classes),
            "include_terminal_initial": args.include_terminal_initial,
            "max_frontier": args.max_frontier,
            "sample_stride": args.sample_stride,
            "sample_offset": args.sample_offset,
            "max_residue_bits": args.max_residue_bits,
        },
        "frontier": frontier_meta,
        "selection": {
            "candidate_starts": len(starts),
            "records_analyzed": len(records),
            "skipped_terminal_initial": skipped_terminal_initial,
            "uncertified_initial": uncertified_initial,
            "nonterminal_next": nonterminal_next,
        },
        "summary": summarize(records, args.max_residue_bits, args.top_n),
        "interpretation": (
            "A pure low-bit endpoint cover is finite evidence for a terminal "
            "residue grammar. A proof would need to derive the endpoint buckets "
            "for all positive finite survivor shadows."
        ),
    }
    if not args.summary:
        payload["records"] = [record.as_dict() for record in records[: args.top_n]]

    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

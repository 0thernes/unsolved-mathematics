#!/usr/bin/env python3
"""Inspect why rare motif-cover outliers terminate after descent.

`outlier_transition_analyzer.py` showed that the rare base-24 outliers do not
reproduce after one certified descent generation.  This script asks what the
certificate endpoint looks like:

    x = T^d(n), where d is the first usable certificate depth of n.

It records the endpoint parity/2-adic valuation, the next certificate class,
and the transition by initial outlier class.  The goal is to distinguish a
mere empirical class transition from a possible proof shape:

    rare outlier -> endpoint in a simple terminal residue family.

The output is finite evidence only.
"""

from __future__ import annotations

import argparse
import json
import math
from collections import Counter, defaultdict
from dataclasses import dataclass
from time import perf_counter
from typing import Iterable

from motif_cover_analyzer import (
    DEFAULT_HARD_STARTS,
    RepaymentMotif,
    frontier_values,
    powers_of_three,
    repayment_motif_for_start,
    unique_preserving_order,
)
from outlier_transition_analyzer import DEFAULT_TERMINAL_CLASSES, iterate_shortcut, parse_classes, transition_class
from repayment_envelope_scan import parse_ints, round_float


def v2(value: int) -> int:
    if value == 0:
        return 0
    return (value & -value).bit_length() - 1


@dataclass(frozen=True)
class EndpointRecord:
    start: int
    initial_motif: RepaymentMotif
    initial_class: str
    endpoint: int
    endpoint_v2: int
    endpoint_ratio_bits: float
    next_motif: RepaymentMotif | None
    next_class: str | None

    @property
    def transition_key(self) -> str:
        return f"{self.initial_class}->{self.next_class or 'uncertified'}"

    @property
    def endpoint_parity(self) -> str:
        return "even" if self.endpoint_v2 else "odd"

    def as_dict(self) -> dict[str, int | float | str | None]:
        return {
            "start": self.start,
            "bit_length": self.start.bit_length(),
            "initial_class": self.initial_class,
            "initial_certificate_depth": self.initial_motif.certificate_depth,
            "initial_motif": self.initial_motif.exact_key,
            "initial_deficit_per_step_bits": round_float(self.initial_motif.deficit_per_step_bits),
            "initial_clearance_margin_bits": round_float(self.initial_motif.clearance_margin_bits),
            "endpoint": self.endpoint,
            "endpoint_bit_length": self.endpoint.bit_length(),
            "endpoint_parity": self.endpoint_parity,
            "endpoint_v2": self.endpoint_v2,
            "endpoint_ratio_bits": round_float(self.endpoint_ratio_bits),
            "next_class": self.next_class,
            "next_certificate_depth": self.next_motif.certificate_depth if self.next_motif else None,
            "next_motif": self.next_motif.exact_key if self.next_motif else None,
            "transition": self.transition_key,
        }


def selected_starts(
    explicit_starts: Iterable[int],
    limit: int,
    frontier_base_depth: int,
    max_depth: int,
    max_frontier: int | None,
    sample_stride: int,
    sample_offset: int,
) -> tuple[list[int], dict[str, object] | None]:
    frontier_meta = None
    frontier_starts: list[int] = []
    if frontier_base_depth:
        frontier_starts, frontier_meta = frontier_values(
            base_depth=frontier_base_depth,
            max_depth=max_depth,
            max_frontier=max_frontier,
            sample_stride=sample_stride,
            sample_offset=sample_offset,
        )
    return unique_preserving_order([*explicit_starts, *range(1, limit + 1), *frontier_starts]), frontier_meta


def endpoint_record_for_start(start: int, max_depth: int, pow3: list[int]) -> EndpointRecord | None:
    initial_motif = repayment_motif_for_start(start, max_depth, pow3)
    if initial_motif is None:
        return None
    initial_class = transition_class(initial_motif)
    endpoint = iterate_shortcut(start, initial_motif.certificate_depth)
    next_motif = repayment_motif_for_start(endpoint, max_depth, pow3) if endpoint > 1 else None
    next_class = transition_class(next_motif) if next_motif else ("reached-one" if endpoint <= 1 else None)
    endpoint_ratio_bits = math.log2(endpoint) - math.log2(start) if endpoint > 0 else float("-inf")
    return EndpointRecord(
        start=start,
        initial_motif=initial_motif,
        initial_class=initial_class,
        endpoint=endpoint,
        endpoint_v2=v2(endpoint),
        endpoint_ratio_bits=endpoint_ratio_bits,
        next_motif=next_motif,
        next_class=next_class,
    )


def top_counter(counter: Counter[str], top_n: int) -> list[dict[str, int | str]]:
    return [{"key": key, "count": count} for key, count in counter.most_common(top_n)]


def nested_counter_rows(nested: dict[str, Counter[str]], top_n: int) -> dict[str, list[dict[str, int | str]]]:
    return {key: top_counter(counter, top_n) for key, counter in sorted(nested.items())}


def summarize(records: list[EndpointRecord], terminal_classes: tuple[str, ...], top_n: int) -> dict[str, object]:
    initial_classes = Counter(record.initial_class for record in records)
    endpoint_parity = Counter(record.endpoint_parity for record in records)
    endpoint_v2_hist = Counter(str(record.endpoint_v2) for record in records)
    next_classes = Counter(record.next_class or "uncertified" for record in records)
    transitions = Counter(record.transition_key for record in records)
    v2_by_initial: dict[str, Counter[str]] = defaultdict(Counter)
    next_by_initial: dict[str, Counter[str]] = defaultdict(Counter)
    transition_by_v2: dict[str, Counter[str]] = defaultdict(Counter)
    terminal_set = set(terminal_classes)

    for record in records:
        v2_key = str(record.endpoint_v2)
        v2_by_initial[record.initial_class][v2_key] += 1
        next_by_initial[record.initial_class][record.next_class or "uncertified"] += 1
        transition_by_v2[v2_key][record.transition_key] += 1

    terminal_hits = sum(1 for record in records if record.next_class in terminal_set)
    even_endpoint_hits = sum(1 for record in records if record.endpoint_v2 > 0)
    odd_endpoint_hits = len(records) - even_endpoint_hits
    slowest_endpoint_drop = sorted(records, key=lambda record: (record.endpoint_ratio_bits, record.start), reverse=True)[
        :top_n
    ]
    deepest_initial = sorted(
        records,
        key=lambda record: (record.initial_motif.certificate_depth, record.start),
        reverse=True,
    )[:top_n]

    return {
        "record_count": len(records),
        "terminal_classes": list(terminal_classes),
        "terminal_next_class_hits": terminal_hits,
        "terminal_next_class_fraction": round_float(terminal_hits / len(records) if records else 0.0),
        "even_endpoint_hits": even_endpoint_hits,
        "odd_endpoint_hits": odd_endpoint_hits,
        "even_endpoint_fraction": round_float(even_endpoint_hits / len(records) if records else 0.0),
        "initial_class_histogram": dict(sorted(initial_classes.items())),
        "endpoint_parity_histogram": dict(sorted(endpoint_parity.items())),
        "endpoint_v2_histogram": dict(sorted(endpoint_v2_hist.items(), key=lambda item: int(item[0]))),
        "next_class_histogram": dict(sorted(next_classes.items())),
        "transition_histogram": top_counter(transitions, top_n),
        "endpoint_v2_by_initial_class": nested_counter_rows(v2_by_initial, top_n),
        "next_class_by_initial_class": nested_counter_rows(next_by_initial, top_n),
        "transition_by_endpoint_v2": nested_counter_rows(transition_by_v2, top_n),
        "least_descent_margin_records": [record.as_dict() for record in slowest_endpoint_drop],
        "deepest_initial_certificate_records": [record.as_dict() for record in deepest_initial],
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
    parser.add_argument("--top-n", type=int, default=12, help="top rows per table")
    parser.add_argument("--summary", action="store_true", help="omit individual endpoint rows")
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
        raise SystemExit("--top-n must be positive")

    started = perf_counter()
    explicit_starts = parse_ints(args.starts)
    if not explicit_starts and args.limit == 0 and args.frontier_base_depth == 0:
        explicit_starts = DEFAULT_HARD_STARTS
    if any(start < 1 for start in explicit_starts):
        raise SystemExit("--starts must contain positive integers")

    terminal_classes = parse_classes(args.terminal_classes)
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

    skipped_terminal_initial = 0
    uncertified_initial = 0
    records: list[EndpointRecord] = []
    terminal_set = set(terminal_classes)
    for start in starts:
        record = endpoint_record_for_start(start, args.max_depth, pow3)
        if record is None:
            uncertified_initial += 1
            continue
        if record.initial_class in terminal_set and not args.include_terminal_initial:
            skipped_terminal_initial += 1
            continue
        records.append(record)

    payload: dict[str, object] = {
        "status": "endpoint-terminal-analysis",
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
        },
        "frontier": frontier_meta,
        "selection": {
            "candidate_starts": len(starts),
            "records_analyzed": len(records),
            "skipped_terminal_initial": skipped_terminal_initial,
            "uncertified_initial": uncertified_initial,
        },
        "summary": summarize(records, terminal_classes, args.top_n),
        "interpretation": (
            "Endpoint parity is finite evidence. A proof would need a uniform "
            "reason that rare outlier certificates land in terminal residue "
            "families rather than creating a new rare outlier."
        ),
    }
    if not args.summary:
        payload["records"] = [record.as_dict() for record in records[: args.top_n]]

    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Test whether mixed terminal endpoint residues resolve after lifting.

The stability analyzer showed that the exact base-24 terminal endpoint grammar
modulo 256 is not a universal fixed table: deeper sampled base-28 endpoints can
share the same low 8 bits while having different terminal next classes.

This script combines several rare-endpoint populations and asks the next
question:

    If a low-bit bucket is mixed, how many additional endpoint bits make its
    children pure again?

Finite positive evidence for "mixed buckets resolve under lifting" is not a
proof.  It is, however, the correct theorem shape after the fixed-table
hypothesis has been falsified.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from dataclasses import dataclass
from time import perf_counter

from endpoint_terminal_analyzer import EndpointRecord
from outlier_transition_analyzer import parse_classes
from repayment_envelope_scan import round_float
from terminal_residue_stability_analyzer import parse_offsets, rare_endpoint_records, residue_label


@dataclass(frozen=True)
class TaggedRecord:
    source: str
    record: EndpointRecord

    @property
    def next_class(self) -> str:
        return self.record.next_class or "uncertified"

    @property
    def endpoint(self) -> int:
        return self.record.endpoint


def collect_tagged_records(
    *,
    reference_frontier_base_depth: int,
    reference_max_depth: int,
    target_frontier_base_depth: int,
    target_max_depth: int,
    target_sample_stride: int,
    target_sample_offsets: list[int],
    terminal_classes: tuple[str, ...],
    include_terminal_initial: bool,
    max_frontier: int | None,
) -> tuple[list[TaggedRecord], list[dict[str, object]]]:
    tagged: list[TaggedRecord] = []
    selections: list[dict[str, object]] = []

    reference_records, reference_selection = rare_endpoint_records(
        frontier_base_depth=reference_frontier_base_depth,
        max_depth=reference_max_depth,
        terminal_classes=terminal_classes,
        include_terminal_initial=include_terminal_initial,
        sample_stride=1,
        sample_offset=0,
        max_frontier=max_frontier,
    )
    reference_source = f"base{reference_frontier_base_depth}:exact"
    tagged.extend(TaggedRecord(reference_source, record) for record in reference_records)
    selections.append({"source": reference_source, **reference_selection})

    for offset in target_sample_offsets:
        target_records, target_selection = rare_endpoint_records(
            frontier_base_depth=target_frontier_base_depth,
            max_depth=target_max_depth,
            terminal_classes=terminal_classes,
            include_terminal_initial=include_terminal_initial,
            sample_stride=target_sample_stride,
            sample_offset=offset,
            max_frontier=max_frontier,
        )
        source = f"base{target_frontier_base_depth}:stride{target_sample_stride}:offset{offset}"
        tagged.extend(TaggedRecord(source, record) for record in target_records)
        selections.append({"source": source, **target_selection})

    return tagged, selections


def buckets_for_bits(records: list[TaggedRecord], residue_bits: int) -> dict[int, list[TaggedRecord]]:
    mask = (1 << residue_bits) - 1
    buckets: dict[int, list[TaggedRecord]] = defaultdict(list)
    for tagged in records:
        buckets[tagged.endpoint & mask].append(tagged)
    return dict(buckets)


def class_histogram(records: list[TaggedRecord]) -> Counter[str]:
    return Counter(tagged.next_class for tagged in records)


def source_histogram(records: list[TaggedRecord]) -> Counter[str]:
    return Counter(tagged.source for tagged in records)


def row_for_bucket(residue: int, residue_bits: int, records: list[TaggedRecord]) -> dict[str, object]:
    classes = class_histogram(records)
    return {
        "residue": residue_label(residue, residue_bits),
        "count": len(records),
        "pure": len(classes) == 1,
        "class_histogram": dict(sorted(classes.items())),
        "source_histogram": dict(sorted(source_histogram(records).items())),
        "sample_starts": [tagged.record.start for tagged in records[:5]],
        "sample_endpoints": [tagged.endpoint for tagged in records[:5]],
    }


def largest_bucket_rows(buckets: dict[int, list[TaggedRecord]], residue_bits: int, top_n: int) -> list[dict[str, object]]:
    rows = [row_for_bucket(residue, residue_bits, records) for residue, records in buckets.items()]
    return sorted(rows, key=lambda row: (row["count"], row["residue"]), reverse=True)[:top_n]


def progression(records: list[TaggedRecord], max_residue_bits: int) -> list[dict[str, object]]:
    rows = []
    for residue_bits in range(1, max_residue_bits + 1):
        buckets = buckets_for_bits(records, residue_bits)
        mixed_bucket_count = 0
        records_in_mixed_buckets = 0
        records_in_pure_buckets = 0
        for members in buckets.values():
            if len(class_histogram(members)) == 1:
                records_in_pure_buckets += len(members)
            else:
                mixed_bucket_count += 1
                records_in_mixed_buckets += len(members)
        rows.append(
            {
                "residue_bits": residue_bits,
                "bucket_count": len(buckets),
                "pure_bucket_count": len(buckets) - mixed_bucket_count,
                "mixed_bucket_count": mixed_bucket_count,
                "records_in_pure_buckets": records_in_pure_buckets,
                "records_in_mixed_buckets": records_in_mixed_buckets,
                "pure_record_fraction": round_float(records_in_pure_buckets / len(records) if records else 0.0),
            }
        )
    return rows


def minimal_pure_bits(rows: list[dict[str, object]]) -> int | None:
    for row in rows:
        if row["mixed_bucket_count"] == 0:
            return int(row["residue_bits"])
    return None


def lift_resolution_rows(
    records: list[TaggedRecord],
    base_residue_bits: int,
    max_residue_bits: int,
    top_n: int,
) -> list[dict[str, object]]:
    base_buckets = buckets_for_bits(records, base_residue_bits)
    mixed_parents = {
        residue: members
        for residue, members in base_buckets.items()
        if len(class_histogram(members)) > 1
    }
    parent_rows = []
    base_mask = (1 << base_residue_bits) - 1

    for parent_residue, parent_records in sorted(
        mixed_parents.items(), key=lambda item: (len(item[1]), item[0]), reverse=True
    ):
        resolved_bits = None
        resolved_child_count = None
        resolved_largest_children: list[dict[str, object]] = []
        progression_rows = []
        for residue_bits in range(base_residue_bits + 1, max_residue_bits + 1):
            child_buckets = buckets_for_bits(parent_records, residue_bits)
            # Paranoia: every child should project back to the parent.
            child_buckets = {
                residue: members
                for residue, members in child_buckets.items()
                if residue & base_mask == parent_residue
            }
            mixed_child_count = sum(1 for members in child_buckets.values() if len(class_histogram(members)) > 1)
            records_in_mixed_children = sum(
                len(members) for members in child_buckets.values() if len(class_histogram(members)) > 1
            )
            progression_rows.append(
                {
                    "residue_bits": residue_bits,
                    "child_bucket_count": len(child_buckets),
                    "mixed_child_bucket_count": mixed_child_count,
                    "records_in_mixed_children": records_in_mixed_children,
                }
            )
            if mixed_child_count == 0 and resolved_bits is None:
                resolved_bits = residue_bits
                resolved_child_count = len(child_buckets)
                resolved_largest_children = largest_bucket_rows(child_buckets, residue_bits, top_n)
                break

        parent_rows.append(
            {
                **row_for_bucket(parent_residue, base_residue_bits, parent_records),
                "resolved_bits": resolved_bits,
                "additional_bits_needed": None if resolved_bits is None else resolved_bits - base_residue_bits,
                "resolved_child_bucket_count": resolved_child_count,
                "resolution_progression": progression_rows,
                "resolved_largest_children": resolved_largest_children,
            }
        )

    return parent_rows[:top_n]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--reference-frontier-base-depth", type=int, default=24)
    parser.add_argument("--reference-max-depth", type=int, default=768)
    parser.add_argument("--target-frontier-base-depth", type=int, default=28)
    parser.add_argument("--target-max-depth", type=int, default=1024)
    parser.add_argument("--target-sample-stride", type=int, default=32)
    parser.add_argument("--target-sample-offsets", nargs="+", default=["0", "8", "16"])
    parser.add_argument("--base-residue-bits", type=int, default=8)
    parser.add_argument("--max-residue-bits", type=int, default=16)
    parser.add_argument("--terminal-classes")
    parser.add_argument("--include-terminal-initial", action="store_true")
    parser.add_argument("--max-frontier", type=int)
    parser.add_argument("--top-n", type=int, default=12)
    args = parser.parse_args()

    if args.reference_frontier_base_depth < 1:
        raise SystemExit("--reference-frontier-base-depth must be positive")
    if args.reference_max_depth < 1:
        raise SystemExit("--reference-max-depth must be positive")
    if args.target_frontier_base_depth < 1:
        raise SystemExit("--target-frontier-base-depth must be positive")
    if args.target_max_depth < 1:
        raise SystemExit("--target-max-depth must be positive")
    if args.target_sample_stride < 1:
        raise SystemExit("--target-sample-stride must be positive")
    if args.base_residue_bits < 1:
        raise SystemExit("--base-residue-bits must be positive")
    if args.max_residue_bits < args.base_residue_bits:
        raise SystemExit("--max-residue-bits must be >= --base-residue-bits")
    if args.top_n < 1:
        raise SystemExit("--top-n must be positive")

    offsets = parse_offsets(args.target_sample_offsets)
    bad_offsets = [offset for offset in offsets if not 0 <= offset < args.target_sample_stride]
    if bad_offsets:
        raise SystemExit("all target offsets must satisfy 0 <= offset < target stride")

    started = perf_counter()
    terminal_classes = parse_classes(args.terminal_classes)
    tagged_records, selections = collect_tagged_records(
        reference_frontier_base_depth=args.reference_frontier_base_depth,
        reference_max_depth=args.reference_max_depth,
        target_frontier_base_depth=args.target_frontier_base_depth,
        target_max_depth=args.target_max_depth,
        target_sample_stride=args.target_sample_stride,
        target_sample_offsets=offsets,
        terminal_classes=terminal_classes,
        include_terminal_initial=args.include_terminal_initial,
        max_frontier=args.max_frontier,
    )
    progress = progression(tagged_records, args.max_residue_bits)
    base_buckets = buckets_for_bits(tagged_records, args.base_residue_bits)
    max_buckets = buckets_for_bits(tagged_records, args.max_residue_bits)

    payload = {
        "status": "terminal-residue-lift-analysis",
        "elapsed_seconds": round_float(perf_counter() - started, 6),
        "parameters": {
            "reference_frontier_base_depth": args.reference_frontier_base_depth,
            "reference_max_depth": args.reference_max_depth,
            "target_frontier_base_depth": args.target_frontier_base_depth,
            "target_max_depth": args.target_max_depth,
            "target_sample_stride": args.target_sample_stride,
            "target_sample_offsets": offsets,
            "base_residue_bits": args.base_residue_bits,
            "max_residue_bits": args.max_residue_bits,
            "terminal_classes": list(terminal_classes),
            "include_terminal_initial": args.include_terminal_initial,
            "max_frontier": args.max_frontier,
        },
        "selection": selections,
        "record_count": len(tagged_records),
        "source_histogram": dict(sorted(source_histogram(tagged_records).items())),
        "next_class_histogram": dict(sorted(class_histogram(tagged_records).items())),
        "cover_progression": progress,
        "minimal_pure_cover_bits": minimal_pure_bits(progress),
        "base_largest_buckets": largest_bucket_rows(base_buckets, args.base_residue_bits, args.top_n),
        "max_largest_buckets": largest_bucket_rows(max_buckets, args.max_residue_bits, args.top_n),
        "mixed_parent_lift_resolution": lift_resolution_rows(
            tagged_records,
            args.base_residue_bits,
            args.max_residue_bits,
            args.top_n,
        ),
        "interpretation": (
            "If mixed parent buckets resolve at higher residue width, the fixed-table "
            "failure is compatible with a residue-lifting theorem. If mixed buckets "
            "persist, the terminal-family theorem needs another invariant."
        ),
    }
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

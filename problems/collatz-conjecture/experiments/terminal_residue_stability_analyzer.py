#!/usr/bin/env python3
"""Compare terminal endpoint residue grammars across frontier depths.

`terminal_residue_cover_analyzer.py` finds a low-bit endpoint grammar for one
finite rare-outlier population.  This script asks whether such a grammar is
stable when moved to deeper sampled survivor frontiers:

    reference endpoint residue mod 2^k -> terminal next class

For each target sample it reports agreement, contradictions, and novel endpoint
residues not seen in the reference grammar.  This is a falsification tool for
the tempting theorem "the base grammar already explains deeper frontiers."
"""

from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from time import perf_counter

from endpoint_terminal_analyzer import EndpointRecord, endpoint_record_for_start, selected_starts
from motif_cover_analyzer import powers_of_three
from outlier_transition_analyzer import parse_classes
from repayment_envelope_scan import parse_ints, round_float


def residue_label(residue: int, residue_bits: int) -> str:
    return f"{residue}/{1 << residue_bits} ({residue:0{residue_bits}b})"


def parse_offsets(raw_offsets: list[str] | None) -> list[int]:
    if not raw_offsets:
        return [0]
    parsed = parse_ints(raw_offsets)
    return parsed


def rare_endpoint_records(
    *,
    frontier_base_depth: int,
    max_depth: int,
    terminal_classes: tuple[str, ...],
    include_terminal_initial: bool,
    sample_stride: int,
    sample_offset: int,
    max_frontier: int | None,
) -> tuple[list[EndpointRecord], dict[str, object]]:
    starts, frontier_meta = selected_starts(
        explicit_starts=[],
        limit=0,
        frontier_base_depth=frontier_base_depth,
        max_depth=max_depth,
        max_frontier=max_frontier,
        sample_stride=sample_stride,
        sample_offset=sample_offset,
    )
    pow3 = powers_of_three(max_depth)
    terminal_set = set(terminal_classes)

    records: list[EndpointRecord] = []
    skipped_terminal_initial = 0
    uncertified_initial = 0
    nonterminal_next = 0
    for start in starts:
        record = endpoint_record_for_start(start, max_depth, pow3)
        if record is None:
            uncertified_initial += 1
            continue
        if record.initial_class in terminal_set and not include_terminal_initial:
            skipped_terminal_initial += 1
            continue
        if record.next_class not in terminal_set:
            nonterminal_next += 1
        records.append(record)

    return records, {
        "frontier": frontier_meta,
        "candidate_starts": len(starts),
        "records_analyzed": len(records),
        "skipped_terminal_initial": skipped_terminal_initial,
        "uncertified_initial": uncertified_initial,
        "nonterminal_next": nonterminal_next,
    }


def grammar(records: list[EndpointRecord], residue_bits: int) -> dict[int, Counter[str]]:
    mask = (1 << residue_bits) - 1
    buckets: dict[int, Counter[str]] = defaultdict(Counter)
    for record in records:
        buckets[record.endpoint & mask][record.next_class or "uncertified"] += 1
    return dict(buckets)


def pure_labels(buckets: dict[int, Counter[str]]) -> dict[int, str]:
    labels: dict[int, str] = {}
    for residue, classes in buckets.items():
        if len(classes) == 1:
            labels[residue] = next(iter(classes))
    return labels


def bucket_rows(
    buckets: dict[int, Counter[str]],
    residue_bits: int,
    top_n: int,
) -> list[dict[str, object]]:
    rows = []
    for residue, classes in buckets.items():
        rows.append(
            {
                "residue": residue_label(residue, residue_bits),
                "count": sum(classes.values()),
                "class_histogram": dict(sorted(classes.items())),
                "pure": len(classes) == 1,
            }
        )
    return sorted(rows, key=lambda row: (row["count"], row["residue"]), reverse=True)[:top_n]


def reference_conflict_rows(
    conflicts: dict[int, Counter[str]],
    reference_buckets: dict[int, Counter[str]],
    residue_bits: int,
    top_n: int,
) -> list[dict[str, object]]:
    rows = []
    for residue, target_classes in conflicts.items():
        reference_classes = reference_buckets.get(residue, Counter())
        rows.append(
            {
                "residue": residue_label(residue, residue_bits),
                "count": sum(target_classes.values()),
                "reference_class_histogram": dict(sorted(reference_classes.items())),
                "target_conflict_histogram": dict(sorted(target_classes.items())),
            }
        )
    return sorted(rows, key=lambda row: (row["count"], row["residue"]), reverse=True)[:top_n]


def compare_to_reference(
    *,
    reference_records: list[EndpointRecord],
    target_records: list[EndpointRecord],
    residue_bits: int,
    top_n: int,
) -> dict[str, object]:
    mask = (1 << residue_bits) - 1
    reference_buckets = grammar(reference_records, residue_bits)
    reference_labels = pure_labels(reference_buckets)
    target_buckets = grammar(target_records, residue_bits)

    covered = 0
    agreeing = 0
    contradicting = 0
    novel = 0
    reference_conflicts: dict[int, Counter[str]] = defaultdict(Counter)
    novel_buckets: dict[int, Counter[str]] = defaultdict(Counter)
    merged_buckets: dict[int, Counter[str]] = defaultdict(Counter)

    for residue, classes in reference_buckets.items():
        merged_buckets[residue].update(classes)

    for record in target_records:
        residue = record.endpoint & mask
        next_class = record.next_class or "uncertified"
        merged_buckets[residue][next_class] += 1
        if residue in reference_labels:
            covered += 1
            if next_class == reference_labels[residue]:
                agreeing += 1
            else:
                contradicting += 1
                reference_conflicts[residue][next_class] += 1
        else:
            novel += 1
            novel_buckets[residue][next_class] += 1

    mixed_reference_buckets = sum(1 for classes in reference_buckets.values() if len(classes) > 1)
    mixed_target_buckets = sum(1 for classes in target_buckets.values() if len(classes) > 1)
    mixed_merged_buckets = sum(1 for classes in merged_buckets.values() if len(classes) > 1)

    return {
        "residue_bits": residue_bits,
        "reference_bucket_count": len(reference_buckets),
        "reference_mixed_bucket_count": mixed_reference_buckets,
        "target_bucket_count": len(target_buckets),
        "target_mixed_bucket_count": mixed_target_buckets,
        "merged_bucket_count": len(merged_buckets),
        "merged_mixed_bucket_count": mixed_merged_buckets,
        "target_records": len(target_records),
        "covered_by_reference_records": covered,
        "covered_by_reference_fraction": round_float(covered / len(target_records) if target_records else 0.0),
        "agreement_records": agreeing,
        "agreement_fraction_of_covered": round_float(agreeing / covered if covered else 0.0),
        "contradiction_records": contradicting,
        "novel_records": novel,
        "novel_record_fraction": round_float(novel / len(target_records) if target_records else 0.0),
        "reference_conflict_buckets": reference_conflict_rows(
            dict(reference_conflicts), reference_buckets, residue_bits, top_n
        ),
        "novel_buckets": bucket_rows(dict(novel_buckets), residue_bits, top_n),
        "target_largest_buckets": bucket_rows(target_buckets, residue_bits, top_n),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--reference-frontier-base-depth", type=int, default=24)
    parser.add_argument("--reference-max-depth", type=int, default=768)
    parser.add_argument("--reference-residue-bits", type=int, default=8)
    parser.add_argument("--target-frontier-base-depth", type=int, default=28)
    parser.add_argument("--target-max-depth", type=int, default=1024)
    parser.add_argument("--target-sample-stride", type=int, default=32)
    parser.add_argument("--target-sample-offsets", nargs="+", default=["0", "8", "16"])
    parser.add_argument("--terminal-classes")
    parser.add_argument("--include-terminal-initial", action="store_true")
    parser.add_argument("--max-frontier", type=int)
    parser.add_argument("--top-n", type=int, default=12)
    args = parser.parse_args()

    if args.reference_frontier_base_depth < 1:
        raise SystemExit("--reference-frontier-base-depth must be positive")
    if args.reference_max_depth < 1:
        raise SystemExit("--reference-max-depth must be positive")
    if args.reference_residue_bits < 1:
        raise SystemExit("--reference-residue-bits must be positive")
    if args.target_frontier_base_depth < 1:
        raise SystemExit("--target-frontier-base-depth must be positive")
    if args.target_max_depth < 1:
        raise SystemExit("--target-max-depth must be positive")
    if args.target_sample_stride < 1:
        raise SystemExit("--target-sample-stride must be positive")
    if args.top_n < 1:
        raise SystemExit("--top-n must be positive")

    offsets = parse_offsets(args.target_sample_offsets)
    bad_offsets = [offset for offset in offsets if not 0 <= offset < args.target_sample_stride]
    if bad_offsets:
        raise SystemExit("all target offsets must satisfy 0 <= offset < target stride")

    started = perf_counter()
    terminal_classes = parse_classes(args.terminal_classes)
    reference_records, reference_selection = rare_endpoint_records(
        frontier_base_depth=args.reference_frontier_base_depth,
        max_depth=args.reference_max_depth,
        terminal_classes=terminal_classes,
        include_terminal_initial=args.include_terminal_initial,
        sample_stride=1,
        sample_offset=0,
        max_frontier=args.max_frontier,
    )

    target_runs = []
    for offset in offsets:
        target_records, target_selection = rare_endpoint_records(
            frontier_base_depth=args.target_frontier_base_depth,
            max_depth=args.target_max_depth,
            terminal_classes=terminal_classes,
            include_terminal_initial=args.include_terminal_initial,
            sample_stride=args.target_sample_stride,
            sample_offset=offset,
            max_frontier=args.max_frontier,
        )
        target_runs.append(
            {
                "sample_offset": offset,
                "selection": target_selection,
                "comparison": compare_to_reference(
                    reference_records=reference_records,
                    target_records=target_records,
                    residue_bits=args.reference_residue_bits,
                    top_n=args.top_n,
                ),
            }
        )

    payload = {
        "status": "terminal-residue-stability-analysis",
        "elapsed_seconds": round_float(perf_counter() - started, 6),
        "parameters": {
            "reference_frontier_base_depth": args.reference_frontier_base_depth,
            "reference_max_depth": args.reference_max_depth,
            "reference_residue_bits": args.reference_residue_bits,
            "target_frontier_base_depth": args.target_frontier_base_depth,
            "target_max_depth": args.target_max_depth,
            "target_sample_stride": args.target_sample_stride,
            "target_sample_offsets": offsets,
            "terminal_classes": list(terminal_classes),
            "include_terminal_initial": args.include_terminal_initial,
            "max_frontier": args.max_frontier,
        },
        "reference_selection": reference_selection,
        "target_runs": target_runs,
        "interpretation": (
            "Contradictions falsify direct reuse of the reference low-bit grammar. "
            "Novel residues mean the theorem must include a lifting or extension rule, "
            "not just a fixed finite table at the reference depth."
        ),
    }
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

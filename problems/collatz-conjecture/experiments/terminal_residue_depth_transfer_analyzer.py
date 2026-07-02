#!/usr/bin/env python3
"""Transfer the full terminal endpoint grammar to deeper frontiers.

The full base-28 sweep showed that the rare endpoint population at one depth
is absorbed by a pure adaptive low-bit tree.  This script asks the next
falsifiable question:

    If that full grammar is trained at depth B, how well does it predict rare
    endpoint classes sampled from depth B+1 or beyond?

It trains on exact base-24 rare endpoints plus a complete stride partition of
one frontier depth, then evaluates sampled offsets from a deeper frontier.
Novel branches and contradictions are not treated as failures to hide; they
are the exact places where a controlled-growth theorem must work harder.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from time import perf_counter

from outlier_transition_analyzer import parse_classes
from repayment_envelope_scan import round_float
from terminal_residue_lift_analyzer import TaggedRecord, class_histogram, source_histogram
from terminal_residue_stability_analyzer import rare_endpoint_records
from terminal_residue_tree_analyzer import build_tree, summarize_tree
from terminal_residue_tree_cv_analyzer import evaluate_records
from terminal_residue_tree_sweep_analyzer import (
    endpoint_records_for_starts,
    frontier_partitions,
    parse_offset_set,
)
from motif_cover_analyzer import powers_of_three


def tagged_records_from_partitions(
    *,
    base_depth: int,
    max_depth: int,
    stride: int,
    offsets: list[int],
    max_frontier: int | None,
    terminal_classes: tuple[str, ...],
    include_terminal_initial: bool,
) -> tuple[list[TaggedRecord], dict[str, object], list[dict[str, object]]]:
    partitions, frontier_meta = frontier_partitions(
        base_depth=base_depth,
        max_depth=max_depth,
        stride=stride,
        max_frontier=max_frontier,
    )
    pow3 = powers_of_three(max_depth)
    tagged: list[TaggedRecord] = []
    runs = []

    for offset in offsets:
        source = f"base{base_depth}:stride{stride}:offset{offset}"
        records, selection = endpoint_records_for_starts(
            starts=partitions[offset],
            max_depth=max_depth,
            pow3=pow3,
            terminal_classes=terminal_classes,
            include_terminal_initial=include_terminal_initial,
        )
        tagged.extend(TaggedRecord(source, record) for record in records)
        runs.append({"sample_offset": offset, "selection": {"source": source, **selection}})

    return tagged, frontier_meta, runs


def run_transfer(args: argparse.Namespace) -> dict[str, object]:
    started = perf_counter()
    terminal_classes = parse_classes(args.terminal_classes)
    train_offsets = parse_offset_set(
        args.train_sample_offsets,
        args.train_sample_stride,
        default=list(range(args.train_sample_stride)),
    )
    probe_offsets = parse_offset_set(
        args.probe_sample_offsets,
        args.probe_sample_stride,
        default=[0, args.probe_sample_stride // 4, args.probe_sample_stride // 2, (3 * args.probe_sample_stride) // 4],
    )

    reference_records, reference_selection = rare_endpoint_records(
        frontier_base_depth=args.reference_frontier_base_depth,
        max_depth=args.reference_max_depth,
        terminal_classes=terminal_classes,
        include_terminal_initial=args.include_terminal_initial,
        sample_stride=1,
        sample_offset=0,
        max_frontier=args.reference_max_frontier,
    )
    train_records = [
        TaggedRecord(f"base{args.reference_frontier_base_depth}:exact", record)
        for record in reference_records
    ]

    train_frontier_records, train_frontier_meta, train_runs = tagged_records_from_partitions(
        base_depth=args.train_frontier_base_depth,
        max_depth=args.train_max_depth,
        stride=args.train_sample_stride,
        offsets=train_offsets,
        max_frontier=args.train_max_frontier,
        terminal_classes=terminal_classes,
        include_terminal_initial=args.include_terminal_initial,
    )
    train_records.extend(train_frontier_records)
    root = build_tree(train_records, 0, 0, args.max_tree_depth)

    probe_records, probe_frontier_meta, probe_runs = tagged_records_from_partitions(
        base_depth=args.probe_frontier_base_depth,
        max_depth=args.probe_max_depth,
        stride=args.probe_sample_stride,
        offsets=probe_offsets,
        max_frontier=args.probe_max_frontier,
        terminal_classes=terminal_classes,
        include_terminal_initial=args.include_terminal_initial,
    )

    probe_runs_with_evaluation = []
    for run in probe_runs:
        source = run["selection"]["source"]
        records_for_source = [tagged for tagged in probe_records if tagged.source == source]
        probe_runs_with_evaluation.append(
            {
                **run,
                "evaluation": evaluate_records(root, records_for_source, args.top_n),
            }
        )

    combined_root = build_tree([*train_records, *probe_records], 0, 0, args.max_tree_depth)

    return {
        "status": "terminal-residue-depth-transfer-analysis",
        "elapsed_seconds": round_float(perf_counter() - started, 6),
        "parameters": {
            "reference_frontier_base_depth": args.reference_frontier_base_depth,
            "reference_max_depth": args.reference_max_depth,
            "reference_max_frontier": args.reference_max_frontier,
            "train_frontier_base_depth": args.train_frontier_base_depth,
            "train_max_depth": args.train_max_depth,
            "train_sample_stride": args.train_sample_stride,
            "train_sample_offsets": train_offsets,
            "train_max_frontier": args.train_max_frontier,
            "probe_frontier_base_depth": args.probe_frontier_base_depth,
            "probe_max_depth": args.probe_max_depth,
            "probe_sample_stride": args.probe_sample_stride,
            "probe_sample_offsets": probe_offsets,
            "probe_max_frontier": args.probe_max_frontier,
            "max_tree_depth": args.max_tree_depth,
            "terminal_classes": list(terminal_classes),
            "include_terminal_initial": args.include_terminal_initial,
        },
        "reference_selection": {"source": f"base{args.reference_frontier_base_depth}:exact", **reference_selection},
        "train_frontier": train_frontier_meta,
        "train_runs": train_runs,
        "train_source_histogram": dict(sorted(source_histogram(train_records).items())),
        "train_next_class_histogram": dict(sorted(class_histogram(train_records).items())),
        "train_tree_summary": summarize_tree(root, args.top_n, args.top_samples),
        "probe_frontier": probe_frontier_meta,
        "probe_runs": probe_runs_with_evaluation,
        "probe_source_histogram": dict(sorted(source_histogram(probe_records).items())),
        "probe_next_class_histogram": dict(sorted(class_histogram(probe_records).items())),
        "probe_total_evaluation": evaluate_records(root, probe_records, args.top_n),
        "combined_tree_summary": summarize_tree(combined_root, args.top_n, args.top_samples),
        "interpretation": (
            "Depth transfer is the honest stress test for the endpoint grammar. "
            "High coverage means the learned low-bit tree is stable; contradictions "
            "and novel branches identify the precise child residues that a proof of "
            "controlled grammar growth must force to terminate."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--reference-frontier-base-depth", type=int, default=24)
    parser.add_argument("--reference-max-depth", type=int, default=768)
    parser.add_argument("--reference-max-frontier", type=int)
    parser.add_argument("--train-frontier-base-depth", type=int, default=28)
    parser.add_argument("--train-max-depth", type=int, default=1024)
    parser.add_argument("--train-sample-stride", type=int, default=32)
    parser.add_argument("--train-sample-offsets", nargs="+", default=["all"])
    parser.add_argument("--train-max-frontier", type=int)
    parser.add_argument("--probe-frontier-base-depth", type=int, default=29)
    parser.add_argument("--probe-max-depth", type=int, default=1152)
    parser.add_argument("--probe-sample-stride", type=int, default=64)
    parser.add_argument("--probe-sample-offsets", nargs="+", default=["0", "16", "32", "48"])
    parser.add_argument("--probe-max-frontier", type=int)
    parser.add_argument("--max-tree-depth", type=int, default=28)
    parser.add_argument("--terminal-classes")
    parser.add_argument("--include-terminal-initial", action="store_true")
    parser.add_argument("--top-n", type=int, default=12)
    parser.add_argument("--top-samples", type=int, default=5)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--quiet", action="store_true")
    args = parser.parse_args()

    for name in [
        "reference_frontier_base_depth",
        "reference_max_depth",
        "train_frontier_base_depth",
        "train_max_depth",
        "train_sample_stride",
        "probe_frontier_base_depth",
        "probe_max_depth",
        "probe_sample_stride",
        "max_tree_depth",
        "top_n",
        "top_samples",
    ]:
        if getattr(args, name) < 1:
            raise SystemExit(f"--{name.replace('_', '-')} must be positive")

    payload = run_transfer(args)
    text = json.dumps(payload, indent=2, sort_keys=True)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text + "\n", encoding="utf-8")
    if not args.quiet:
        print(text)


if __name__ == "__main__":
    main()

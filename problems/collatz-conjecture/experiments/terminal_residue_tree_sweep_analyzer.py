#!/usr/bin/env python3
"""Active-learning sweep for the adaptive terminal residue grammar.

The cross-validation analyzer tests a few held-out frontier slices against one
trained endpoint tree.  This script pushes the same idea across a complete
stride partition:

* build the base-28 frontier once;
* train on exact base-24 rare endpoints plus selected seed base-28 offsets;
* evaluate each remaining offset before adding it to the grammar;
* record how many contradictions, novel branches, and tree nodes appear.

The output is finite evidence only.  The useful mathematical object is the
growth curve: a proof would need to show that new endpoint residue branches
remain controlled instead of reproducing hard classes forever.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path
from time import perf_counter

from endpoint_terminal_analyzer import EndpointRecord, endpoint_record_for_start
from frontier_escape_analyzer import enumerate_frontier
from motif_cover_analyzer import powers_of_three
from outlier_transition_analyzer import parse_classes
from repayment_envelope_scan import parse_ints, round_float
from terminal_residue_lift_analyzer import TaggedRecord, class_histogram, source_histogram
from terminal_residue_stability_analyzer import rare_endpoint_records
from terminal_residue_tree_analyzer import build_tree, summarize_tree
from terminal_residue_tree_cv_analyzer import evaluate_records


def parse_offset_set(raw_offsets: list[str] | None, stride: int, default: list[int]) -> list[int]:
    if not raw_offsets:
        offsets = default
    elif any(raw.strip().lower() == "all" for raw in raw_offsets):
        offsets = list(range(stride))
    else:
        offsets = parse_ints(raw_offsets)

    bad_offsets = [offset for offset in offsets if not 0 <= offset < stride]
    if bad_offsets:
        raise SystemExit("all offsets must satisfy 0 <= offset < target stride")

    seen: set[int] = set()
    ordered: list[int] = []
    for offset in offsets:
        if offset in seen:
            continue
        seen.add(offset)
        ordered.append(offset)
    return ordered


def frontier_partitions(
    *,
    base_depth: int,
    max_depth: int,
    stride: int,
    max_frontier: int | None,
) -> tuple[dict[int, list[int]], dict[str, object]]:
    frontier, stats = enumerate_frontier(base_depth, powers_of_three(max_depth))
    leaves = sorted(frontier, key=lambda leaf: leaf.residue)
    if max_frontier is not None:
        leaves = leaves[:max_frontier]

    partitions: dict[int, list[int]] = {offset: [] for offset in range(stride)}
    for index, leaf in enumerate(leaves):
        if leaf.residue <= 0:
            continue
        partitions[index % stride].append(leaf.residue)

    return partitions, {
        **stats,
        "selected_count": len(leaves),
        "sample_stride": stride,
        "sample_offset": "partitioned",
        "max_frontier": max_frontier,
    }


def endpoint_records_for_starts(
    *,
    starts: list[int],
    max_depth: int,
    pow3: list[int],
    terminal_classes: tuple[str, ...],
    include_terminal_initial: bool,
) -> tuple[list[EndpointRecord], dict[str, object]]:
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
        "candidate_starts": len(starts),
        "records_analyzed": len(records),
        "skipped_terminal_initial": skipped_terminal_initial,
        "uncertified_initial": uncertified_initial,
        "nonterminal_next": nonterminal_next,
    }


def tree_curve_row(offset: int | str, record_count: int, tree_summary: dict[str, object]) -> dict[str, object]:
    quantiles = tree_summary["weighted_leaf_depth_quantiles"]
    return {
        "offset_added": offset,
        "record_count": record_count,
        "node_count": tree_summary["node_count"],
        "leaf_count": tree_summary["leaf_count"],
        "pure_leaf_count": tree_summary["pure_leaf_count"],
        "unresolved_leaf_count": tree_summary["unresolved_leaf_count"],
        "max_leaf_depth": tree_summary["max_leaf_depth"],
        "weighted_mean_leaf_depth": tree_summary["weighted_mean_leaf_depth"],
        "p90_leaf_depth": quantiles["p90"],
        "p99_leaf_depth": quantiles["p99"],
    }


def run_sweep(args: argparse.Namespace) -> dict[str, object]:
    started = perf_counter()
    terminal_classes = parse_classes(args.terminal_classes)
    seed_offsets = parse_offset_set(
        args.seed_target_sample_offsets,
        args.target_sample_stride,
        default=[0, 8, 16],
    )
    requested_sweep_offsets = parse_offset_set(
        args.sweep_target_sample_offsets,
        args.target_sample_stride,
        default=list(range(args.target_sample_stride)),
    )
    sweep_offsets = [offset for offset in requested_sweep_offsets if offset not in set(seed_offsets)]

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

    partitions, frontier_meta = frontier_partitions(
        base_depth=args.target_frontier_base_depth,
        max_depth=args.target_max_depth,
        stride=args.target_sample_stride,
        max_frontier=args.target_max_frontier,
    )
    pow3 = powers_of_three(args.target_max_depth)

    seed_runs = []
    for offset in seed_offsets:
        source = f"base{args.target_frontier_base_depth}:stride{args.target_sample_stride}:offset{offset}"
        records, selection = endpoint_records_for_starts(
            starts=partitions[offset],
            max_depth=args.target_max_depth,
            pow3=pow3,
            terminal_classes=terminal_classes,
            include_terminal_initial=args.include_terminal_initial,
        )
        tagged = [TaggedRecord(source, record) for record in records]
        train_records.extend(tagged)
        seed_runs.append({"sample_offset": offset, "selection": {"source": source, **selection}})

    root = build_tree(train_records, 0, 0, args.max_tree_depth)
    initial_tree_summary = summarize_tree(root, args.top_n, args.top_samples)
    growth_curve = [tree_curve_row("seed", len(train_records), initial_tree_summary)]

    sweep_runs = []
    all_sweep_records: list[TaggedRecord] = []
    pre_update_status = Counter()
    for offset in sweep_offsets:
        source = f"base{args.target_frontier_base_depth}:stride{args.target_sample_stride}:offset{offset}"
        records, selection = endpoint_records_for_starts(
            starts=partitions[offset],
            max_depth=args.target_max_depth,
            pow3=pow3,
            terminal_classes=terminal_classes,
            include_terminal_initial=args.include_terminal_initial,
        )
        tagged = [TaggedRecord(source, record) for record in records]
        all_sweep_records.extend(tagged)
        evaluation = evaluate_records(root, tagged, args.top_n)
        pre_update_status.update(evaluation["status_histogram"])

        train_records.extend(tagged)
        root = build_tree(train_records, 0, 0, args.max_tree_depth)
        updated_summary = summarize_tree(root, args.top_n, args.top_samples)
        growth_curve.append(tree_curve_row(offset, len(train_records), updated_summary))
        sweep_runs.append(
            {
                "sample_offset": offset,
                "selection": {"source": source, **selection},
                "pre_update_evaluation": evaluation,
                "post_update_tree_curve": growth_curve[-1],
            }
        )

    final_summary = summarize_tree(root, args.top_n, args.top_samples)
    initial_root = build_tree(
        train_records[: len(reference_records) + sum(run["selection"]["records_analyzed"] for run in seed_runs)],
        0,
        0,
        args.max_tree_depth,
    )

    return {
        "status": "terminal-residue-tree-sweep-analysis",
        "elapsed_seconds": round_float(perf_counter() - started, 6),
        "parameters": {
            "reference_frontier_base_depth": args.reference_frontier_base_depth,
            "reference_max_depth": args.reference_max_depth,
            "reference_max_frontier": args.reference_max_frontier,
            "target_frontier_base_depth": args.target_frontier_base_depth,
            "target_max_depth": args.target_max_depth,
            "target_sample_stride": args.target_sample_stride,
            "target_max_frontier": args.target_max_frontier,
            "seed_target_sample_offsets": seed_offsets,
            "sweep_target_sample_offsets": sweep_offsets,
            "max_tree_depth": args.max_tree_depth,
            "terminal_classes": list(terminal_classes),
            "include_terminal_initial": args.include_terminal_initial,
        },
        "reference_selection": {"source": f"base{args.reference_frontier_base_depth}:exact", **reference_selection},
        "target_frontier": frontier_meta,
        "seed_runs": seed_runs,
        "initial_tree_summary": initial_tree_summary,
        "sweep_total_evaluation_against_seed_tree": evaluate_records(initial_root, all_sweep_records, args.top_n),
        "pre_update_status_histogram": dict(sorted(pre_update_status.items())),
        "sweep_runs": sweep_runs,
        "growth_curve": growth_curve,
        "final_source_histogram": dict(sorted(source_histogram(train_records).items())),
        "final_next_class_histogram": dict(sorted(class_histogram(train_records).items())),
        "final_tree_summary": final_summary,
        "interpretation": (
            "A slowly growing pure tree supports a controlled adaptive grammar target. "
            "Contradictions and novel branches are not failures here; they are the exact "
            "new residue children that any endpoint-lifting theorem must explain."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--reference-frontier-base-depth", type=int, default=24)
    parser.add_argument("--reference-max-depth", type=int, default=768)
    parser.add_argument("--reference-max-frontier", type=int)
    parser.add_argument("--target-frontier-base-depth", type=int, default=28)
    parser.add_argument("--target-max-depth", type=int, default=1024)
    parser.add_argument("--target-sample-stride", type=int, default=32)
    parser.add_argument("--target-max-frontier", type=int)
    parser.add_argument("--seed-target-sample-offsets", nargs="+", default=["0", "8", "16"])
    parser.add_argument("--sweep-target-sample-offsets", nargs="+", default=["all"])
    parser.add_argument("--max-tree-depth", type=int, default=18)
    parser.add_argument("--terminal-classes")
    parser.add_argument("--include-terminal-initial", action="store_true")
    parser.add_argument("--top-n", type=int, default=12)
    parser.add_argument("--top-samples", type=int, default=5)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--quiet", action="store_true")
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
    if args.max_tree_depth < 1:
        raise SystemExit("--max-tree-depth must be positive")
    if args.top_n < 1:
        raise SystemExit("--top-n must be positive")
    if args.top_samples < 1:
        raise SystemExit("--top-samples must be positive")

    payload = run_sweep(args)
    text = json.dumps(payload, indent=2, sort_keys=True)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text + "\n", encoding="utf-8")
    if not args.quiet:
        print(text)


if __name__ == "__main__":
    main()

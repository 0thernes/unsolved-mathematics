#!/usr/bin/env python3
"""Cross-validate the adaptive terminal residue tree on held-out slices.

The tree analyzer builds a compact finite grammar from one merged endpoint
population.  This script turns it into a falsifiable classifier:

* train on exact base-24 rare endpoints plus selected sampled base-28 offsets;
* test on held-out sampled base-28 offsets;
* separate correct predictions, class contradictions, and novel unseen branches.

The goal is not to prove Collatz.  The goal is to find whether the adaptive
endpoint-bit grammar generalizes, and if not, exactly how it must grow.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from dataclasses import dataclass
from time import perf_counter

from outlier_transition_analyzer import parse_classes
from repayment_envelope_scan import round_float
from terminal_residue_lift_analyzer import TaggedRecord, class_histogram, collect_tagged_records, residue_label
from terminal_residue_stability_analyzer import parse_offsets, rare_endpoint_records
from terminal_residue_tree_analyzer import TreeNode, build_tree, summarize_tree


@dataclass(frozen=True)
class EvaluationResult:
    tagged: TaggedRecord
    status: str
    predicted_class: str | None
    actual_class: str
    depth: int
    residue: int
    train_histogram: Counter[str]


def child_by_residue(node: TreeNode) -> dict[int, TreeNode]:
    return {child.residue: child for child in node.children}


def evaluate_record(root: TreeNode, tagged: TaggedRecord) -> EvaluationResult:
    node = root
    while node.children:
        next_depth = node.depth + 1
        next_residue = tagged.endpoint & ((1 << next_depth) - 1)
        child = child_by_residue(node).get(next_residue)
        if child is None:
            return EvaluationResult(
                tagged=tagged,
                status="novel-branch",
                predicted_class=None,
                actual_class=tagged.next_class,
                depth=next_depth,
                residue=next_residue,
                train_histogram=node.class_histogram,
            )
        node = child

    hist = node.class_histogram
    if len(hist) != 1:
        return EvaluationResult(
            tagged=tagged,
            status="unresolved-train-leaf",
            predicted_class=None,
            actual_class=tagged.next_class,
            depth=node.depth,
            residue=node.residue,
            train_histogram=hist,
        )

    predicted_class = next(iter(hist))
    return EvaluationResult(
        tagged=tagged,
        status="agreement" if predicted_class == tagged.next_class else "contradiction",
        predicted_class=predicted_class,
        actual_class=tagged.next_class,
        depth=node.depth,
        residue=node.residue,
        train_histogram=hist,
    )


def result_bucket_rows(results: list[EvaluationResult], top_n: int) -> list[dict[str, object]]:
    grouped: dict[tuple[int, int, str], list[EvaluationResult]] = defaultdict(list)
    for result in results:
        grouped[(result.depth, result.residue, result.status)].append(result)

    rows = []
    for (depth, residue, status), members in grouped.items():
        actual_hist = Counter(result.actual_class for result in members)
        predicted_hist = Counter(result.predicted_class or "none" for result in members)
        source_hist = Counter(result.tagged.source for result in members)
        train_hist = Counter()
        for result in members:
            train_hist.update(result.train_histogram)
        rows.append(
            {
                "depth": depth,
                "residue": "root" if depth == 0 else residue_label(residue, depth),
                "status": status,
                "count": len(members),
                "actual_class_histogram": dict(sorted(actual_hist.items())),
                "predicted_class_histogram": dict(sorted(predicted_hist.items())),
                "train_class_histogram": dict(sorted(train_hist.items())),
                "source_histogram": dict(sorted(source_hist.items())),
                "sample_starts": [result.tagged.record.start for result in members[:5]],
                "sample_endpoints": [result.tagged.endpoint for result in members[:5]],
            }
        )

    return sorted(rows, key=lambda row: (row["count"], row["depth"], row["residue"]), reverse=True)[:top_n]


def evaluate_records(root: TreeNode, tagged_records: list[TaggedRecord], top_n: int) -> dict[str, object]:
    results = [evaluate_record(root, tagged) for tagged in tagged_records]
    status_hist = Counter(result.status for result in results)
    leaf_depths = [result.depth for result in results if result.status in {"agreement", "contradiction"}]
    predicted_count = status_hist["agreement"] + status_hist["contradiction"]
    agreement_count = status_hist["agreement"]
    contradiction_results = [result for result in results if result.status == "contradiction"]
    novel_results = [result for result in results if result.status == "novel-branch"]
    unresolved_results = [result for result in results if result.status == "unresolved-train-leaf"]

    return {
        "record_count": len(results),
        "status_histogram": dict(sorted(status_hist.items())),
        "predicted_records": predicted_count,
        "prediction_coverage_fraction": round_float(predicted_count / len(results) if results else 0.0),
        "agreement_records": agreement_count,
        "accuracy_on_predicted": round_float(agreement_count / predicted_count if predicted_count else 0.0),
        "contradiction_records": len(contradiction_results),
        "novel_branch_records": len(novel_results),
        "unresolved_train_leaf_records": len(unresolved_results),
        "mean_prediction_depth": round_float(sum(leaf_depths) / len(leaf_depths) if leaf_depths else 0.0),
        "contradiction_buckets": result_bucket_rows(contradiction_results, top_n),
        "novel_branch_buckets": result_bucket_rows(novel_results, top_n),
        "unresolved_train_leaf_buckets": result_bucket_rows(unresolved_results, top_n),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--reference-frontier-base-depth", type=int, default=24)
    parser.add_argument("--reference-max-depth", type=int, default=768)
    parser.add_argument("--target-frontier-base-depth", type=int, default=28)
    parser.add_argument("--target-max-depth", type=int, default=1024)
    parser.add_argument("--target-sample-stride", type=int, default=32)
    parser.add_argument("--train-target-sample-offsets", nargs="+", default=["0", "8", "16"])
    parser.add_argument("--heldout-target-sample-offsets", nargs="+", default=["4", "12", "20"])
    parser.add_argument("--max-tree-depth", type=int, default=16)
    parser.add_argument("--terminal-classes")
    parser.add_argument("--include-terminal-initial", action="store_true")
    parser.add_argument("--max-frontier", type=int)
    parser.add_argument("--top-n", type=int, default=12)
    parser.add_argument("--top-samples", type=int, default=5)
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

    train_offsets = parse_offsets(args.train_target_sample_offsets)
    heldout_offsets = parse_offsets(args.heldout_target_sample_offsets)
    bad_offsets = [
        offset
        for offset in [*train_offsets, *heldout_offsets]
        if not 0 <= offset < args.target_sample_stride
    ]
    if bad_offsets:
        raise SystemExit("all offsets must satisfy 0 <= offset < target stride")

    started = perf_counter()
    terminal_classes = parse_classes(args.terminal_classes)
    train_records, train_selections = collect_tagged_records(
        reference_frontier_base_depth=args.reference_frontier_base_depth,
        reference_max_depth=args.reference_max_depth,
        target_frontier_base_depth=args.target_frontier_base_depth,
        target_max_depth=args.target_max_depth,
        target_sample_stride=args.target_sample_stride,
        target_sample_offsets=train_offsets,
        terminal_classes=terminal_classes,
        include_terminal_initial=args.include_terminal_initial,
        max_frontier=args.max_frontier,
    )
    root = build_tree(train_records, 0, 0, args.max_tree_depth)

    heldout_runs = []
    all_heldout_records: list[TaggedRecord] = []
    for offset in heldout_offsets:
        heldout_records, heldout_selection = rare_endpoint_records(
            frontier_base_depth=args.target_frontier_base_depth,
            max_depth=args.target_max_depth,
            terminal_classes=terminal_classes,
            include_terminal_initial=args.include_terminal_initial,
            sample_stride=args.target_sample_stride,
            sample_offset=offset,
            max_frontier=args.max_frontier,
        )
        source = f"base{args.target_frontier_base_depth}:stride{args.target_sample_stride}:offset{offset}"
        tagged_heldout = [TaggedRecord(source, record) for record in heldout_records]
        all_heldout_records.extend(tagged_heldout)
        heldout_runs.append(
            {
                "sample_offset": offset,
                "selection": {"source": source, **heldout_selection},
                "evaluation": evaluate_records(root, tagged_heldout, args.top_n),
            }
        )
    combined_root = build_tree([*train_records, *all_heldout_records], 0, 0, args.max_tree_depth)

    payload = {
        "status": "terminal-residue-tree-cv-analysis",
        "elapsed_seconds": round_float(perf_counter() - started, 6),
        "parameters": {
            "reference_frontier_base_depth": args.reference_frontier_base_depth,
            "reference_max_depth": args.reference_max_depth,
            "target_frontier_base_depth": args.target_frontier_base_depth,
            "target_max_depth": args.target_max_depth,
            "target_sample_stride": args.target_sample_stride,
            "train_target_sample_offsets": train_offsets,
            "heldout_target_sample_offsets": heldout_offsets,
            "max_tree_depth": args.max_tree_depth,
            "terminal_classes": list(terminal_classes),
            "include_terminal_initial": args.include_terminal_initial,
            "max_frontier": args.max_frontier,
        },
        "train_selection": train_selections,
        "train_tree_summary": summarize_tree(root, args.top_n, args.top_samples),
        "heldout_total_evaluation": evaluate_records(root, all_heldout_records, args.top_n),
        "combined_tree_summary": summarize_tree(combined_root, args.top_n, args.top_samples),
        "heldout_runs": heldout_runs,
        "interpretation": (
            "High prediction coverage with few contradictions supports a stable adaptive grammar. "
            "Novel branches identify the exact new endpoint residue leaves that the grammar must add."
        ),
    }
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

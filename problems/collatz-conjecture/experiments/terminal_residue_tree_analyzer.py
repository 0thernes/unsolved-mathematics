#!/usr/bin/env python3
"""Build an adaptive low-bit decision tree for terminal endpoint classes.

The lift analyzer showed that a merged finite rare-endpoint population becomes
pure after enough endpoint bits are exposed.  A fixed-width table is still a
blunt object.  This script builds the smaller adaptive classifier:

    inspect low endpoint bits only until the bucket has one terminal class.

The output is a finite decision tree over endpoint residues.  It is not a proof
that future endpoints follow the same tree, but it is a compact grammar target
for a possible lifting theorem.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter
from dataclasses import dataclass
from time import perf_counter

from outlier_transition_analyzer import parse_classes
from repayment_envelope_scan import round_float
from terminal_residue_lift_analyzer import (
    TaggedRecord,
    class_histogram,
    collect_tagged_records,
    residue_label,
    source_histogram,
)
from terminal_residue_stability_analyzer import parse_offsets


@dataclass
class TreeNode:
    depth: int
    residue: int
    records: list[TaggedRecord]
    children: list["TreeNode"]

    @property
    def class_histogram(self) -> Counter[str]:
        return class_histogram(self.records)

    @property
    def pure(self) -> bool:
        return len(self.class_histogram) == 1

    @property
    def leaf(self) -> bool:
        return not self.children


def split_records(records: list[TaggedRecord], depth: int) -> dict[int, list[TaggedRecord]]:
    mask = (1 << depth) - 1
    buckets: dict[int, list[TaggedRecord]] = {}
    for tagged in records:
        residue = tagged.endpoint & mask
        buckets.setdefault(residue, []).append(tagged)
    return buckets


def build_tree(records: list[TaggedRecord], depth: int, residue: int, max_depth: int) -> TreeNode:
    if not records:
        return TreeNode(depth=depth, residue=residue, records=[], children=[])
    if len(class_histogram(records)) == 1 or depth >= max_depth:
        return TreeNode(depth=depth, residue=residue, records=records, children=[])

    next_depth = depth + 1
    buckets = split_records(records, next_depth)
    children = [
        build_tree(members, next_depth, child_residue, max_depth)
        for child_residue, members in sorted(buckets.items())
        if members
    ]
    return TreeNode(depth=depth, residue=residue, records=records, children=children)


def walk(node: TreeNode) -> list[TreeNode]:
    nodes = [node]
    for child in node.children:
        nodes.extend(walk(child))
    return nodes


def row_for_node(node: TreeNode, top_samples: int) -> dict[str, object]:
    hist = node.class_histogram
    sources = source_histogram(node.records)
    return {
        "depth": node.depth,
        "residue": "root" if node.depth == 0 else residue_label(node.residue, node.depth),
        "count": len(node.records),
        "pure": node.pure,
        "class_histogram": dict(sorted(hist.items())),
        "source_histogram": dict(sorted(sources.items())),
        "sample_starts": [tagged.record.start for tagged in node.records[:top_samples]],
        "sample_endpoints": [tagged.endpoint for tagged in node.records[:top_samples]],
    }


def leaf_depth_quantiles(leaves: list[TreeNode]) -> dict[str, int | None]:
    if not leaves:
        return {"p50": None, "p90": None, "p95": None, "p99": None}
    depths = []
    for leaf in leaves:
        depths.extend([leaf.depth] * len(leaf.records))
    depths.sort()

    def q(probability: float) -> int:
        index = min(len(depths) - 1, int(probability * (len(depths) - 1)))
        return depths[index]

    return {"p50": q(0.50), "p90": q(0.90), "p95": q(0.95), "p99": q(0.99)}


def summarize_tree(root: TreeNode, top_n: int, top_samples: int) -> dict[str, object]:
    nodes = walk(root)
    leaves = [node for node in nodes if node.leaf]
    internal = [node for node in nodes if not node.leaf]
    unresolved = [leaf for leaf in leaves if not leaf.pure]
    pure = [leaf for leaf in leaves if leaf.pure]
    weighted_depth_sum = sum(leaf.depth * len(leaf.records) for leaf in leaves)
    record_count = len(root.records)
    leaf_class_counter = Counter()
    for leaf in pure:
        leaf_class_counter[next(iter(leaf.class_histogram))] += 1
    record_class_counter = Counter()
    for leaf in pure:
        record_class_counter[next(iter(leaf.class_histogram))] += len(leaf.records)

    leaves_by_count = sorted(leaves, key=lambda node: (len(node.records), node.depth, node.residue), reverse=True)
    leaves_by_depth = sorted(leaves, key=lambda node: (node.depth, len(node.records), node.residue), reverse=True)
    internal_by_count = sorted(internal, key=lambda node: (len(node.records), node.depth, node.residue), reverse=True)

    return {
        "record_count": record_count,
        "node_count": len(nodes),
        "internal_node_count": len(internal),
        "leaf_count": len(leaves),
        "pure_leaf_count": len(pure),
        "unresolved_leaf_count": len(unresolved),
        "max_leaf_depth": max((leaf.depth for leaf in leaves), default=0),
        "min_leaf_depth": min((leaf.depth for leaf in leaves), default=0),
        "weighted_mean_leaf_depth": round_float(weighted_depth_sum / record_count if record_count else 0.0),
        "weighted_leaf_depth_quantiles": leaf_depth_quantiles(leaves),
        "leaf_count_by_class": dict(sorted(leaf_class_counter.items())),
        "record_count_by_leaf_class": dict(sorted(record_class_counter.items())),
        "largest_leaves": [row_for_node(node, top_samples) for node in leaves_by_count[:top_n]],
        "deepest_leaves": [row_for_node(node, top_samples) for node in leaves_by_depth[:top_n]],
        "largest_internal_nodes": [row_for_node(node, top_samples) for node in internal_by_count[:top_n]],
        "unresolved_leaves": [row_for_node(node, top_samples) for node in unresolved[:top_n]],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--reference-frontier-base-depth", type=int, default=24)
    parser.add_argument("--reference-max-depth", type=int, default=768)
    parser.add_argument("--target-frontier-base-depth", type=int, default=28)
    parser.add_argument("--target-max-depth", type=int, default=1024)
    parser.add_argument("--target-sample-stride", type=int, default=32)
    parser.add_argument("--target-sample-offsets", nargs="+", default=["0", "8", "16"])
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
    root = build_tree(tagged_records, 0, 0, args.max_tree_depth)

    payload = {
        "status": "terminal-residue-tree-analysis",
        "elapsed_seconds": round_float(perf_counter() - started, 6),
        "parameters": {
            "reference_frontier_base_depth": args.reference_frontier_base_depth,
            "reference_max_depth": args.reference_max_depth,
            "target_frontier_base_depth": args.target_frontier_base_depth,
            "target_max_depth": args.target_max_depth,
            "target_sample_stride": args.target_sample_stride,
            "target_sample_offsets": offsets,
            "max_tree_depth": args.max_tree_depth,
            "terminal_classes": list(terminal_classes),
            "include_terminal_initial": args.include_terminal_initial,
            "max_frontier": args.max_frontier,
        },
        "selection": selections,
        "source_histogram": dict(sorted(source_histogram(tagged_records).items())),
        "next_class_histogram": dict(sorted(class_histogram(tagged_records).items())),
        "summary": summarize_tree(root, args.top_n, args.top_samples),
        "interpretation": (
            "A compact pure decision tree is finite evidence for an adaptive "
            "terminal-residue grammar. A proof must derive why mixed endpoint "
            "parents cannot keep branching into mixed children forever."
        ),
    }
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

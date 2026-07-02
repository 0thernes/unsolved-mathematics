#!/usr/bin/env python3
"""Measure surplus margins for every retimed above-parent pressure layer.

The three-regime ledger proves finite coverage and the event-index layer law.
This script re-enumerates the same exact frontier lifts and records the credit
surplus at each pressure layer, grouped by dynamic regime.

The output is finite theorem-discovery data, not a proof of Collatz.
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path
from time import perf_counter

sys.path.insert(0, str(Path(__file__).resolve().parent))

from branch_potential_analyzer import enumerate_frontier, powers_of_three, round_float
from branch_prefix_dominance_analyzer import analyze_prefix_start
from branch_prefix_retimed_post_ladder_tail import as_counter_dict
from branch_prefix_retimed_pressure import pressure_trace, transition_row
from branch_prefix_retimed_signature import classify_pressure_unit


def update_from_counter(target: Counter[str], source: Counter[object]) -> None:
    target.update({str(key): int(value) for key, value in source.items()})


def keep_smallest(records: list[dict[str, object]], record: dict[str, object], top_n: int) -> None:
    records.append(record)
    records.sort(
        key=lambda row: (
            int(row["surplus"]),
            int(row["required_above_parent"]),
            str(row["regime"]),
            int(row["child"]),
            int(row["step"]),
        )
    )
    del records[top_n:]


def compact_record(
    *,
    parent: int,
    child: int,
    parent_depth: int,
    event_index: int,
    event: dict[str, object],
    regime: str,
    transition: dict[str, object],
) -> dict[str, object]:
    last = event.get("last_credit_event")
    last_event = {} if last is None else dict(last)
    required_above_parent = int(event["required"]) - int(transition["parent_required"])
    surplus = int(event["credit"]) - int(event["required"])
    return {
        "parent": parent,
        "child": child,
        "event_index": event_index,
        "event": event["event"],
        "regime": regime,
        "step": event["step"],
        "step_offset_from_parent_depth": int(event["step"]) - parent_depth,
        "state": event["state"],
        "parent_required": transition["parent_required"],
        "child_required": transition["child_required"],
        "required_delta": transition["required_delta"],
        "credit_delta": transition["credit_delta"],
        "required": event["required"],
        "required_above_parent": required_above_parent,
        "credit": event["credit"],
        "surplus": surplus,
        "margin_above_layer": surplus,
        "credit_above_parent": int(event["credit"]) - int(transition["parent_required"]),
        "last_credit_kind": last_event.get("kind"),
        "last_credit_align": last_event.get("align"),
        "last_credit_step": last_event.get("step"),
        "last_credit_state": last_event.get("state"),
        "lag_from_credit": None if not last_event else int(event["step"]) - int(last_event["step"]),
    }


def analyze_depth(args: argparse.Namespace, parent_depth: int) -> dict[str, object]:
    started = perf_counter()
    child_depth = parent_depth + 1
    max_depth = max(args.max_depth, child_depth)

    parent_frontier, parent_stats = enumerate_frontier(parent_depth, powers_of_three(max_depth))
    child_frontier, child_stats = enumerate_frontier(child_depth, powers_of_three(max_depth))
    parent_leaves = {leaf.residue: leaf for leaf in parent_frontier if leaf.residue > 1}
    child_leaves = {leaf.residue: leaf for leaf in child_frontier if leaf.residue > 1}
    parent_rows = {residue: analyze_prefix_start(residue, args.max_steps) for residue in sorted(parent_leaves)}

    retimed_count = 0
    pressure_unit_count = 0
    positive_pressure_count = 0
    first_layer_count = 0

    regime_counts: Counter[str] = Counter()
    layer_counts: Counter[int] = Counter()
    layer_regime_counts: Counter[str] = Counter()
    event_index_required_counts: Counter[str] = Counter()
    surplus_counts: Counter[int] = Counter()
    surplus_by_regime: dict[str, Counter[int]] = {}
    surplus_by_layer: dict[str, Counter[int]] = {}
    surplus_by_regime_layer: dict[str, Counter[int]] = {}
    min_surplus_by_regime: dict[str, int] = {}
    min_surplus_by_layer: dict[str, int] = {}
    min_surplus_by_regime_layer: dict[str, int] = {}
    credit_above_parent_counts: Counter[int] = Counter()
    lag_by_regime: Counter[str] = Counter()
    event_by_regime: Counter[str] = Counter()
    step_offset_counts: Counter[int] = Counter()
    pressure_units_per_transition: Counter[int] = Counter()

    tightest: list[dict[str, object]] = []
    nonpositive_surplus: list[dict[str, object]] = []
    non_diagonal_layer: list[dict[str, object]] = []
    missing_prior_credit: list[dict[str, object]] = []
    first_layer_misses: list[dict[str, object]] = []

    step_size = 1 << parent_depth
    for parent in sorted(parent_leaves):
        parent_row = parent_rows[parent]
        parent_required = int(parent_row["max_prefix_required"])
        for child_bit in (0, 1):
            child = parent + child_bit * step_size
            child_leaf = child_leaves.get(child)
            if child_leaf is None:
                continue
            child_row = analyze_prefix_start(child, args.max_steps)
            transition = transition_row(
                parent=parent,
                child=child,
                child_bit=child_bit,
                parent_row=parent_row,
                child_row=child_row,
                child_leaf=child_leaf,
            )
            if int(transition["required_delta"]) > 0:
                positive_pressure_count += 1
            if not (
                int(transition["required_delta"]) > 0
                and int(transition["credit_delta"]) < int(transition["required_delta"])
            ):
                continue

            retimed_count += 1
            trace = pressure_trace(child, parent_required, args.max_steps)
            pressure_units = [
                dict(event)
                for event in trace["pressure_events"]
                if int(dict(event)["required"]) > parent_required
            ]
            if not pressure_units or int(pressure_units[0]["required"]) - parent_required != 1:
                first_layer_misses.append(
                    {
                        "parent": parent,
                        "child": child,
                        "pressure_unit_count": len(pressure_units),
                        "first_required_above_parent": (
                            None if not pressure_units else int(pressure_units[0]["required"]) - parent_required
                        ),
                    }
                )
            else:
                first_layer_count += 1
            pressure_units_per_transition[len(pressure_units)] += 1

            for event_index, event in enumerate(pressure_units, start=1):
                pressure_unit_count += 1
                regime = classify_pressure_unit(event)
                record = compact_record(
                    parent=parent,
                    child=child,
                    parent_depth=parent_depth,
                    event_index=event_index,
                    event=event,
                    regime=regime,
                    transition=transition,
                )
                layer = int(record["required_above_parent"])
                surplus = int(record["surplus"])
                regime_layer = f"{regime}:{layer}"

                regime_counts[regime] += 1
                layer_counts[layer] += 1
                layer_regime_counts[f"{layer}:{regime}"] += 1
                event_index_required_counts[f"{event_index}:{layer}"] += 1
                surplus_counts[surplus] += 1
                surplus_by_regime.setdefault(regime, Counter())[surplus] += 1
                surplus_by_layer.setdefault(str(layer), Counter())[surplus] += 1
                surplus_by_regime_layer.setdefault(regime_layer, Counter())[surplus] += 1
                min_surplus_by_regime[regime] = min(surplus, min_surplus_by_regime.get(regime, surplus))
                min_surplus_by_layer[str(layer)] = min(surplus, min_surplus_by_layer.get(str(layer), surplus))
                min_surplus_by_regime_layer[regime_layer] = min(
                    surplus, min_surplus_by_regime_layer.get(regime_layer, surplus)
                )
                credit_above_parent_counts[int(record["credit_above_parent"])] += 1
                if record["lag_from_credit"] is not None:
                    lag_by_regime[f"{regime}:{record['lag_from_credit']}"] += 1
                event_by_regime[f"{regime}:{record['event']}"] += 1
                step_offset_counts[int(record["step_offset_from_parent_depth"])] += 1
                keep_smallest(tightest, record, args.top_n)

                if surplus <= 0:
                    nonpositive_surplus.append(record)
                if event_index != layer:
                    non_diagonal_layer.append(record)
                if event.get("last_credit_event") is None:
                    missing_prior_credit.append(record)

    return {
        "status": "branch-prefix-retimed-layer-margin",
        "elapsed_seconds": round_float(perf_counter() - started, 6),
        "parent_depth": parent_depth,
        "child_depth": child_depth,
        "frontiers": {
            "parent": {**parent_stats, "positive_live_count": len(parent_leaves), "depth": parent_depth},
            "child": {**child_stats, "positive_live_count": len(child_leaves), "depth": child_depth},
        },
        "positive_pressure_transition_count": positive_pressure_count,
        "retimed_transition_count": retimed_count,
        "above_parent_pressure_unit_count": pressure_unit_count,
        "first_layer_count": first_layer_count,
        "regime_counts": as_counter_dict(regime_counts),
        "layer_counts": as_counter_dict(layer_counts),
        "layer_regime_counts": as_counter_dict(layer_regime_counts),
        "event_index_required_above_parent_counts": as_counter_dict(event_index_required_counts),
        "surplus_histogram": as_counter_dict(surplus_counts),
        "surplus_by_regime": {
            regime: as_counter_dict(counter) for regime, counter in sorted(surplus_by_regime.items())
        },
        "surplus_by_layer": {
            layer: as_counter_dict(counter) for layer, counter in sorted(surplus_by_layer.items(), key=lambda x: int(x[0]))
        },
        "surplus_by_regime_layer": {
            key: as_counter_dict(counter) for key, counter in sorted(surplus_by_regime_layer.items())
        },
        "min_surplus_by_regime": as_counter_dict(Counter(min_surplus_by_regime)),
        "min_surplus_by_layer": as_counter_dict(Counter(min_surplus_by_layer)),
        "min_surplus_by_regime_layer": as_counter_dict(Counter(min_surplus_by_regime_layer)),
        "credit_above_parent_histogram": as_counter_dict(credit_above_parent_counts),
        "lag_by_regime": as_counter_dict(lag_by_regime),
        "event_by_regime": as_counter_dict(event_by_regime),
        "step_offset_histogram": as_counter_dict(step_offset_counts),
        "pressure_units_per_transition": as_counter_dict(pressure_units_per_transition),
        "pure_feature_claims": {
            "all_pressure_units_have_positive_surplus": not nonpositive_surplus,
            "all_event_indexes_equal_required_above_parent": not non_diagonal_layer,
            "all_pressure_units_have_prior_credit": not missing_prior_credit,
            "all_retimed_transitions_have_layer_one": first_layer_count == retimed_count and not first_layer_misses,
        },
        "tightest_pressure_units": tightest,
        "nonpositive_surplus_examples": nonpositive_surplus[: args.top_n],
        "non_diagonal_layer_examples": non_diagonal_layer[: args.top_n],
        "missing_prior_credit_examples": missing_prior_credit[: args.top_n],
        "first_layer_miss_examples": first_layer_misses[: args.top_n],
    }


def load_or_run_depth(args: argparse.Namespace, parent_depth: int) -> tuple[dict[str, object], bool]:
    child_depth = parent_depth + 1
    cache = Path(args.cache_template.format(parent_depth=parent_depth, child_depth=child_depth))
    if args.use_cache and cache.exists() and not args.refresh:
        return json.loads(cache.read_text(encoding="utf-8")), True
    payload = analyze_depth(args, parent_depth)
    if args.write_depth_cache:
        cache.parent.mkdir(parents=True, exist_ok=True)
        cache.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return payload, False


def merge_counter_dict(rows: list[dict[str, object]], key: str) -> Counter[str]:
    merged: Counter[str] = Counter()
    for row in rows:
        merged.update({str(k): int(v) for k, v in dict(row[key]).items()})
    return merged


def merge_nested(rows: list[dict[str, object]], key: str) -> dict[str, dict[str, int]]:
    outer: dict[str, Counter[str]] = {}
    for row in rows:
        for name, counter in dict(row[key]).items():
            outer.setdefault(str(name), Counter()).update({str(k): int(v) for k, v in dict(counter).items()})
    return {name: as_counter_dict(counter) for name, counter in sorted(outer.items())}


def min_merge(rows: list[dict[str, object]], key: str) -> dict[str, int]:
    result: dict[str, int] = {}
    for row in rows:
        for name, value in dict(row[key]).items():
            name = str(name)
            value = int(value)
            result[name] = min(value, result.get(name, value))
    return dict(sorted(result.items()))


def compact_depth(payload: dict[str, object], cached: bool) -> dict[str, object]:
    offsets = [int(key) for key in dict(payload["step_offset_histogram"])]
    return {
        "parent_depth": int(payload["parent_depth"]),
        "child_depth": int(payload["child_depth"]),
        "cached": cached,
        "retimed_transition_count": int(payload["retimed_transition_count"]),
        "above_parent_pressure_unit_count": int(payload["above_parent_pressure_unit_count"]),
        "first_layer_count": int(payload["first_layer_count"]),
        "regime_counts": payload["regime_counts"],
        "layer_counts": payload["layer_counts"],
        "min_surplus_by_layer": payload["min_surplus_by_layer"],
        "min_surplus_by_regime": payload["min_surplus_by_regime"],
        "pressure_units_per_transition": payload["pressure_units_per_transition"],
        "step_offset_min": min(offsets) if offsets else None,
        "step_offset_max": max(offsets) if offsets else None,
        "pure_feature_claims": payload["pure_feature_claims"],
    }


def run(args: argparse.Namespace) -> dict[str, object]:
    full_rows = []
    rows = []
    for depth in range(args.min_parent_depth, args.max_parent_depth + 1):
        payload, cached = load_or_run_depth(args, depth)
        full_rows.append(payload)
        rows.append(compact_depth(payload, cached))

    offsets = [
        int(value)
        for row in rows
        for value in (row["step_offset_min"], row["step_offset_max"])
        if value is not None
    ]
    claim_names = sorted({claim for row in rows for claim in dict(row["pure_feature_claims"])})

    return {
        "status": "branch-prefix-retimed-layer-margin-sweep",
        "parameters": {
            "min_parent_depth": args.min_parent_depth,
            "max_parent_depth": args.max_parent_depth,
            "max_depth": args.max_depth,
            "max_steps": args.max_steps,
            "top_n": args.top_n,
            "use_cache": args.use_cache,
            "refresh": args.refresh,
            "write_depth_cache": args.write_depth_cache,
            "cache_template": args.cache_template,
        },
        "depths": rows,
        "checks": {
            "pure_feature_claims_all_depths": {
                claim: all(bool(dict(row["pure_feature_claims"]).get(claim, False)) for row in rows)
                for claim in claim_names
            },
            "total_retimed_transitions": sum(int(row["retimed_transition_count"]) for row in rows),
            "total_above_parent_pressure_units": sum(int(row["above_parent_pressure_unit_count"]) for row in rows),
            "total_first_layer_count": sum(int(row["first_layer_count"]) for row in rows),
            "regime_counts": as_counter_dict(merge_counter_dict(full_rows, "regime_counts")),
            "layer_counts": as_counter_dict(merge_counter_dict(full_rows, "layer_counts")),
            "layer_regime_counts": as_counter_dict(merge_counter_dict(full_rows, "layer_regime_counts")),
            "event_index_required_above_parent_counts": as_counter_dict(
                merge_counter_dict(full_rows, "event_index_required_above_parent_counts")
            ),
            "surplus_histogram": as_counter_dict(merge_counter_dict(full_rows, "surplus_histogram")),
            "surplus_by_regime": merge_nested(full_rows, "surplus_by_regime"),
            "surplus_by_layer": merge_nested(full_rows, "surplus_by_layer"),
            "surplus_by_regime_layer": merge_nested(full_rows, "surplus_by_regime_layer"),
            "min_surplus_by_regime": min_merge(full_rows, "min_surplus_by_regime"),
            "min_surplus_by_layer": min_merge(full_rows, "min_surplus_by_layer"),
            "min_surplus_by_regime_layer": min_merge(full_rows, "min_surplus_by_regime_layer"),
            "credit_above_parent_histogram": as_counter_dict(
                merge_counter_dict(full_rows, "credit_above_parent_histogram")
            ),
            "pressure_units_per_transition": as_counter_dict(
                merge_counter_dict(full_rows, "pressure_units_per_transition")
            ),
            "global_step_offset_min": min(offsets) if offsets else None,
            "global_step_offset_max": max(offsets) if offsets else None,
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--min-parent-depth", type=int, default=18)
    parser.add_argument("--max-parent-depth", type=int, default=25)
    parser.add_argument("--max-depth", type=int, default=1024)
    parser.add_argument("--max-steps", type=int, default=50000)
    parser.add_argument("--top-n", type=int, default=8)
    parser.add_argument(
        "--cache-template",
        default="experiments/results/branch_prefix_retimed_layer_margin_d{parent_depth}_d{child_depth}_20260702.json",
    )
    parser.add_argument("--use-cache", action="store_true")
    parser.add_argument("--refresh", action="store_true")
    parser.add_argument("--write-depth-cache", action="store_true")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    if args.min_parent_depth < 1:
        raise SystemExit("--min-parent-depth must be positive")
    if args.max_parent_depth < args.min_parent_depth:
        raise SystemExit("--max-parent-depth must be >= --min-parent-depth")
    if args.max_steps < 1:
        raise SystemExit("--max-steps must be positive")
    if args.top_n < 1:
        raise SystemExit("--top-n must be positive")

    payload = run(args)
    text = json.dumps(payload, indent=2, sort_keys=True)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text + "\n", encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()

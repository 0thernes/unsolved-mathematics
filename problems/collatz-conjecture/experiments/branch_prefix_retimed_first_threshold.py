#!/usr/bin/env python3
"""Mine first above-parent thresholds in retimed-pressure transitions.

The signature sweep shows that every retimed-pressure child has a prepaid
one-unit first threshold. This instrument records the timing of that first
threshold relative to the parent frontier depth and to the last visible credit
event.

The output is finite theorem-discovery data, not a proof of Collatz.
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path
from time import perf_counter

sys.path.insert(0, str(Path(__file__).resolve().parent))

from branch_potential_analyzer import enumerate_frontier, powers_of_three, round_float
from branch_prefix_dominance_analyzer import analyze_prefix_start
from branch_prefix_retimed_pressure import pressure_trace, transition_row
from branch_prefix_retimed_signature import classify_pressure_unit


def as_counter_dict(counter: Counter[object]) -> dict[str, int]:
    return dict(sorted((str(key), int(value)) for key, value in counter.items()))


def int_stats(values: list[int]) -> dict[str, object]:
    if not values:
        return {"count": 0, "min": None, "max": None, "avg": None}
    return {
        "count": len(values),
        "min": min(values),
        "max": max(values),
        "avg": round_float(sum(values) / len(values)),
    }


def compact_first_record(
    *,
    parent: int,
    child: int,
    child_bit: int,
    parent_depth: int,
    event: dict[str, object],
    regime: str,
    parent_required: int,
    transition: dict[str, object],
) -> dict[str, object]:
    last = event.get("last_credit_event")
    last_event = {} if last is None else dict(last)
    align = int(last_event.get("align", 0)) if last_event else None
    lag = int(event["step"]) - int(last_event["step"]) if last_event else None
    return {
        "parent": parent,
        "child": child,
        "child_bit": child_bit,
        "event": event["event"],
        "regime": regime,
        "step": event["step"],
        "step_offset_from_parent_depth": int(event["step"]) - parent_depth,
        "state": event["state"],
        "parent_required": parent_required,
        "required": event["required"],
        "required_above_parent": int(event["required"]) - parent_required,
        "credit": event["credit"],
        "surplus": int(event["credit"]) - int(event["required"]),
        "last_credit_kind": last_event.get("kind"),
        "last_credit_align": align,
        "last_credit_step": last_event.get("step"),
        "last_credit_state": last_event.get("state"),
        "lag": lag,
        "lag_minus_align": None if lag is None or align is None else lag - align,
        "required_delta": transition["required_delta"],
        "credit_delta": transition["credit_delta"],
        "child_required": transition["child_required"],
        "child_credit": transition["child_credit"],
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

    positive_pressure_count = 0
    retimed_count = 0
    missing_first_count = 0
    first_child_bits: Counter[int] = Counter()
    first_events: Counter[str] = Counter()
    first_regimes: Counter[str] = Counter()
    first_credit_kinds: Counter[str] = Counter()
    first_credit_aligns: Counter[str] = Counter()
    first_step_offsets: Counter[int] = Counter()
    first_lags: Counter[int] = Counter()
    first_lag_minus_align: Counter[str] = Counter()
    first_required_above_parent: Counter[int] = Counter()
    first_surplus: Counter[int] = Counter()
    offset_by_regime: Counter[str] = Counter()
    lag_by_regime: Counter[str] = Counter()
    stats_by_regime: dict[str, dict[str, list[int]]] = defaultdict(lambda: defaultdict(list))
    tightest: list[dict[str, object]] = []
    largest_offset: list[dict[str, object]] = []
    largest_lag_minus_align: list[dict[str, object]] = []
    missing_credit: list[dict[str, object]] = []

    def keep_smallest(records: list[dict[str, object]], record: dict[str, object], key: str) -> None:
        records.append(record)
        records.sort(key=lambda row: (int(row[key]), int(row["child"]), int(row["step"])))
        del records[args.top_n :]

    def keep_largest(records: list[dict[str, object]], record: dict[str, object], key: str) -> None:
        records.append(record)
        records.sort(key=lambda row: (int(row[key]), int(row["child"]), int(row["step"])), reverse=True)
        del records[args.top_n :]

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
            first = None
            for event in trace["pressure_events"]:
                candidate = dict(event)
                if int(candidate["required"]) > parent_required:
                    first = candidate
                    break
            if first is None:
                missing_first_count += 1
                continue

            regime = classify_pressure_unit(first)
            record = compact_first_record(
                parent=parent,
                child=child,
                child_bit=child_bit,
                parent_depth=parent_depth,
                event=first,
                regime=regime,
                parent_required=parent_required,
                transition=transition,
            )

            first_child_bits[child_bit] += 1
            first_events[str(first["event"])] += 1
            first_regimes[regime] += 1
            first_step_offsets[int(record["step_offset_from_parent_depth"])] += 1
            first_required_above_parent[int(record["required_above_parent"])] += 1
            first_surplus[int(record["surplus"])] += 1
            offset_by_regime[f"{regime}:{record['step_offset_from_parent_depth']}"] += 1
            stats_by_regime[regime]["step_offset"].append(int(record["step_offset_from_parent_depth"]))
            stats_by_regime[regime]["surplus"].append(int(record["surplus"]))

            if record["lag"] is not None:
                first_lags[int(record["lag"])] += 1
                lag_by_regime[f"{regime}:{record['lag']}"] += 1
                stats_by_regime[regime]["lag"].append(int(record["lag"]))
            if record["lag_minus_align"] is not None:
                kind = str(record["last_credit_kind"])
                first_lag_minus_align[f"{kind}:{record['lag_minus_align']}"] += 1
                stats_by_regime[regime]["lag_minus_align"].append(int(record["lag_minus_align"]))
            if record["last_credit_kind"] is None:
                missing_credit.append(record)
            else:
                first_credit_kinds[str(record["last_credit_kind"])] += 1
                first_credit_aligns[f"{record['last_credit_kind']}:{record['last_credit_align']}"] += 1

            keep_smallest(tightest, record, "surplus")
            keep_largest(largest_offset, record, "step_offset_from_parent_depth")
            if record["lag_minus_align"] is not None:
                keep_largest(largest_lag_minus_align, record, "lag_minus_align")

    regime_stats = {
        regime: {field: int_stats(values) for field, values in sorted(fields.items())}
        for regime, fields in sorted(stats_by_regime.items())
    }
    return {
        "status": "branch-prefix-retimed-first-threshold",
        "elapsed_seconds": round_float(perf_counter() - started, 6),
        "parent_depth": parent_depth,
        "child_depth": child_depth,
        "frontiers": {
            "parent": {
                **parent_stats,
                "positive_live_count": len(parent_leaves),
                "depth": parent_depth,
            },
            "child": {
                **child_stats,
                "positive_live_count": len(child_leaves),
                "depth": child_depth,
            },
        },
        "positive_pressure_transition_count": positive_pressure_count,
        "retimed_transition_count": retimed_count,
        "missing_first_threshold_count": missing_first_count,
        "first_threshold_count": retimed_count - missing_first_count,
        "first_child_bit_counts": as_counter_dict(first_child_bits),
        "first_event_counts": as_counter_dict(first_events),
        "first_regime_counts": as_counter_dict(first_regimes),
        "first_credit_kind_counts": as_counter_dict(first_credit_kinds),
        "first_credit_align_counts": as_counter_dict(first_credit_aligns),
        "first_step_offset_histogram": as_counter_dict(first_step_offsets),
        "first_lag_histogram": as_counter_dict(first_lags),
        "first_lag_minus_align_histogram": as_counter_dict(first_lag_minus_align),
        "first_required_above_parent_histogram": as_counter_dict(first_required_above_parent),
        "first_surplus_histogram": as_counter_dict(first_surplus),
        "first_step_offset_by_regime": as_counter_dict(offset_by_regime),
        "first_lag_by_regime": as_counter_dict(lag_by_regime),
        "regime_stats": regime_stats,
        "pure_feature_claims": {
            "all_first_thresholds_present": missing_first_count == 0,
            "all_first_thresholds_upper_child": dict(first_child_bits) == {1: retimed_count},
            "all_first_thresholds_one_unit": dict(first_required_above_parent) == {1: retimed_count},
            "all_first_thresholds_have_prior_credit": not missing_credit,
            "all_first_thresholds_positive_surplus": min(first_surplus.keys(), default=1) > 0,
        },
        "tightest_first_thresholds": tightest,
        "largest_step_offsets": largest_offset,
        "largest_lag_minus_align": largest_lag_minus_align,
        "missing_credit_first_thresholds": missing_credit[: args.top_n],
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


def compact_depth(payload: dict[str, object], cached: bool) -> dict[str, object]:
    offsets = [int(key) for key in dict(payload["first_step_offset_histogram"])]
    lags = [int(key) for key in dict(payload["first_lag_histogram"])]
    lag_minus_align = [
        int(str(key).split(":", 1)[1])
        for key in dict(payload["first_lag_minus_align_histogram"])
    ]
    return {
        "parent_depth": int(payload["parent_depth"]),
        "child_depth": int(payload["child_depth"]),
        "cached": cached,
        "positive_pressure_transition_count": int(payload["positive_pressure_transition_count"]),
        "retimed_transition_count": int(payload["retimed_transition_count"]),
        "first_threshold_count": int(payload["first_threshold_count"]),
        "first_event_counts": payload["first_event_counts"],
        "first_regime_counts": payload["first_regime_counts"],
        "first_credit_kind_counts": payload["first_credit_kind_counts"],
        "first_required_above_parent_histogram": payload["first_required_above_parent_histogram"],
        "first_surplus_min": min((int(k) for k in dict(payload["first_surplus_histogram"])), default=None),
        "first_step_offset_min": min(offsets) if offsets else None,
        "first_step_offset_max": max(offsets) if offsets else None,
        "first_lag_min": min(lags) if lags else None,
        "first_lag_max": max(lags) if lags else None,
        "first_lag_minus_align_min": min(lag_minus_align) if lag_minus_align else None,
        "first_lag_minus_align_max": max(lag_minus_align) if lag_minus_align else None,
        "pure_feature_claims": payload["pure_feature_claims"],
        "regime_stats": payload["regime_stats"],
    }


def run(args: argparse.Namespace) -> dict[str, object]:
    rows = []
    for depth in range(args.min_parent_depth, args.max_parent_depth + 1):
        payload, cached = load_or_run_depth(args, depth)
        rows.append(compact_depth(payload, cached))

    claim_names = sorted(
        {
            claim
            for row in rows
            for claim in dict(row["pure_feature_claims"])
        }
    )
    combined_regimes: Counter[str] = Counter()
    combined_events: Counter[str] = Counter()
    combined_credit_kinds: Counter[str] = Counter()
    for row in rows:
        combined_regimes.update({key: int(value) for key, value in dict(row["first_regime_counts"]).items()})
        combined_events.update({key: int(value) for key, value in dict(row["first_event_counts"]).items()})
        combined_credit_kinds.update({key: int(value) for key, value in dict(row["first_credit_kind_counts"]).items()})

    return {
        "status": "branch-prefix-retimed-first-threshold-sweep",
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
            "total_first_thresholds": sum(int(row["first_threshold_count"]) for row in rows),
            "first_regime_counts": as_counter_dict(combined_regimes),
            "first_event_counts": as_counter_dict(combined_events),
            "first_credit_kind_counts": as_counter_dict(combined_credit_kinds),
            "global_first_step_offset_min": min(
                int(row["first_step_offset_min"]) for row in rows if row["first_step_offset_min"] is not None
            ),
            "global_first_step_offset_max": max(
                int(row["first_step_offset_max"]) for row in rows if row["first_step_offset_max"] is not None
            ),
            "global_first_lag_minus_align_min": min(
                int(row["first_lag_minus_align_min"]) for row in rows if row["first_lag_minus_align_min"] is not None
            ),
            "global_first_lag_minus_align_max": max(
                int(row["first_lag_minus_align_max"]) for row in rows if row["first_lag_minus_align_max"] is not None
            ),
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
        default="experiments/results/branch_prefix_retimed_first_threshold_d{parent_depth}_d{child_depth}_20260702.json",
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

#!/usr/bin/env python3
"""Audit every above-parent pressure unit in retimed lift transitions.

The first retimed-pressure audit checks the first prefix where a child needs
more prefix credit than its parent ever needed.  This script strengthens that
local check: for every retimed-pressure child, inspect every later required
credit increase above the parent threshold and ask whether the unit pressure is
already covered by visible structural credit.
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
from branch_prefix_retimed_pressure import pressure_trace, transition_row


def event_timing_class(event: dict[str, object]) -> str:
    last = event.get("last_credit_event")
    if last is None:
        return "no_prior_counted_credit"
    lag = int(event["step"]) - int(dict(last)["step"])
    kind = str(dict(last)["kind"])
    return f"same_step_{kind}" if lag == 0 else f"prior_{kind}"


def pressure_unit_record(
    *,
    parent: int,
    child: int,
    child_bit: int,
    parent_required: int,
    transition: dict[str, object],
    event_index: int,
    event: dict[str, object],
) -> dict[str, object]:
    last = event.get("last_credit_event")
    last_event = None if last is None else dict(last)
    lag = None if last_event is None else int(event["step"]) - int(last_event["step"])
    required = int(event["required"])
    credit = int(event["credit"])
    return {
        "parent": parent,
        "child": child,
        "child_bit": child_bit,
        "event_index": event_index,
        "event": event["event"],
        "step": event["step"],
        "state": event["state"],
        "odd_steps": event["odd_steps"],
        "max_excess": event["max_excess"],
        "parent_required": parent_required,
        "required": required,
        "required_above_parent": required - parent_required,
        "credit": credit,
        "surplus": credit - required,
        "timing_class": event_timing_class(event),
        "threshold_lag": lag,
        "last_credit_event": last_event,
        "required_delta": transition["required_delta"],
        "credit_delta": transition["credit_delta"],
        "delta_shortfall_after_new_credit": transition["delta_shortfall_after_new_credit"],
        "child_required": transition["child_required"],
        "child_credit": transition["child_credit"],
        "child_max_excess": transition["child_max_excess"],
    }


def run(args: argparse.Namespace) -> dict[str, object]:
    started = perf_counter()
    parent_depth = args.parent_depth
    child_depth = parent_depth + 1
    max_depth = max(args.max_depth, child_depth)

    parent_frontier, parent_stats = enumerate_frontier(parent_depth, powers_of_three(max_depth))
    child_frontier, child_stats = enumerate_frontier(child_depth, powers_of_three(max_depth))
    parent_leaves = {leaf.residue: leaf for leaf in parent_frontier if leaf.residue > 1}
    child_leaves = {leaf.residue: leaf for leaf in child_frontier if leaf.residue > 1}
    parent_rows = {residue: analyze_prefix_start(residue, args.max_steps) for residue in sorted(parent_leaves)}

    step_size = 1 << parent_depth
    positive_pressure_count = 0
    retimed_transition_count = 0
    full_pressure_certified_count = 0
    above_parent_pressure_units: list[dict[str, object]] = []
    transition_failures: list[dict[str, object]] = []
    transition_pressure_histogram: Counter[int] = Counter()
    transition_class_counts: Counter[str] = Counter()
    child_class_counts: Counter[str] = Counter()

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

            retimed_transition_count += 1
            child_class_counts[str(transition["child_class"])] += 1
            trace = pressure_trace(child, parent_required, args.max_steps)
            pressure_events = [
                dict(event)
                for event in trace["pressure_events"]
                if int(dict(event)["required"]) > parent_required
            ]
            transition_pressure_histogram[len(pressure_events)] += 1

            unit_records = [
                pressure_unit_record(
                    parent=parent,
                    child=child,
                    child_bit=child_bit,
                    parent_required=parent_required,
                    transition=transition,
                    event_index=index,
                    event=event,
                )
                for index, event in enumerate(pressure_events, start=1)
            ]
            above_parent_pressure_units.extend(unit_records)
            for record in unit_records:
                transition_class_counts[str(record["timing_class"])] += 1

            bad_units = [
                record
                for record in unit_records
                if record["last_credit_event"] is None or int(record["surplus"]) < 0
            ]
            if bad_units or int(trace["max_deficit"]) > 0:
                transition_failures.append(
                    {
                        "parent": parent,
                        "child": child,
                        "child_bit": child_bit,
                        "parent_required": parent_required,
                        "child_required": transition["child_required"],
                        "required_delta": transition["required_delta"],
                        "credit_delta": transition["credit_delta"],
                        "trace_max_deficit": trace["max_deficit"],
                        "bad_units": bad_units[: args.top_n],
                    }
                )
            else:
                full_pressure_certified_count += 1

    failure_units = [
        record
        for record in above_parent_pressure_units
        if record["last_credit_event"] is None or int(record["surplus"]) < 0
    ]
    tight_units = [record for record in above_parent_pressure_units if int(record["surplus"]) == 0]
    lag_values = [
        int(record["threshold_lag"])
        for record in above_parent_pressure_units
        if record["threshold_lag"] is not None
    ]
    required_above_values = [int(record["required_above_parent"]) for record in above_parent_pressure_units]
    surplus_values = [int(record["surplus"]) for record in above_parent_pressure_units]

    return {
        "status": "branch-prefix-pressure-units",
        "elapsed_seconds": round_float(perf_counter() - started, 6),
        "parameters": {
            key: (str(value) if isinstance(value, Path) else value)
            for key, value in vars(args).items()
        },
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
        "retimed_transition_count": retimed_transition_count,
        "full_pressure_certified_transition_count": full_pressure_certified_count,
        "transition_failure_count": len(transition_failures),
        "above_parent_pressure_unit_count": len(above_parent_pressure_units),
        "pressure_unit_failure_count": len(failure_units),
        "tight_pressure_unit_count": len(tight_units),
        "timing_class_counts": dict(sorted(transition_class_counts.items())),
        "retimed_child_class_counts": dict(sorted(child_class_counts.items())),
        "transition_above_parent_pressure_unit_histogram": dict(
            sorted((str(k), v) for k, v in transition_pressure_histogram.items())
        ),
        "required_above_parent_histogram": dict(
            sorted((str(k), v) for k, v in Counter(required_above_values).items())
        ),
        "pressure_unit_surplus_histogram": dict(
            sorted((str(k), v) for k, v in Counter(surplus_values).items())
        ),
        "threshold_lag_histogram": dict(sorted((str(k), v) for k, v in Counter(lag_values).items())),
        "min_pressure_unit_surplus": min(surplus_values, default=None),
        "max_pressure_unit_surplus": max(surplus_values, default=None),
        "max_required_above_parent": max(required_above_values, default=None),
        "max_threshold_lag": max(lag_values, default=None),
        "tightest_pressure_units": sorted(
            above_parent_pressure_units,
            key=lambda record: (
                int(record["surplus"]),
                -int(record["required_above_parent"]),
                int(record["child"]),
                int(record["step"]),
            ),
        )[: args.top_n],
        "largest_required_above_parent_units": sorted(
            above_parent_pressure_units,
            key=lambda record: (
                int(record["required_above_parent"]),
                int(record["surplus"]),
                int(record["child"]),
            ),
            reverse=True,
        )[: args.top_n],
        "largest_lag_units": sorted(
            [record for record in above_parent_pressure_units if record["threshold_lag"] is not None],
            key=lambda record: (int(record["threshold_lag"]), int(record["child"]), int(record["step"])),
            reverse=True,
        )[: args.top_n],
        "failure_units": failure_units[: args.top_n],
        "transition_failures": transition_failures[: args.top_n],
        "interpretation": (
            "Finite unit-pressure audit for the retimed-pressure hard class. "
            "Zero pressure-unit failures means every above-parent required-credit "
            "increase was already covered by visible structural credit at the "
            "moment that pressure appeared."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--parent-depth", type=int, default=25)
    parser.add_argument("--max-depth", type=int, default=1024)
    parser.add_argument("--max-steps", type=int, default=50000)
    parser.add_argument("--top-n", type=int, default=12)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--quiet", action="store_true")
    args = parser.parse_args()

    if args.parent_depth < 1:
        raise SystemExit("--parent-depth must be positive")
    if args.max_depth < args.parent_depth + 1:
        raise SystemExit("--max-depth must be at least --parent-depth + 1")
    if args.max_steps < 1:
        raise SystemExit("--max-steps must be positive")
    if args.top_n < 1:
        raise SystemExit("--top-n must be positive")

    payload = run(args)
    text = json.dumps(payload, indent=2, sort_keys=True)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text + "\n", encoding="utf-8")
    if not args.quiet:
        print(text)


if __name__ == "__main__":
    main()

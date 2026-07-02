#!/usr/bin/env python3
"""Trace retimed-pressure lift transitions.

The parent-child transition audit found live children whose required prefix
credit increases, while the child has less total structural credit than the
parent by crude total-delta accounting.  Those are not failures: every checked
child still has zero prefix deficit.  This script traces those retimed-pressure
children to identify what visible event timing keeps the prefix ledger solvent.
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path
from time import perf_counter

sys.path.insert(0, str(Path(__file__).resolve().parent))

from branch_potential_analyzer import (
    enumerate_frontier,
    min_credit_required,
    odd3_macro_info,
    powers_of_three,
    round_float,
    shortcut_step,
    update_excess,
    v2,
)
from branch_prefix_dominance_analyzer import analyze_prefix_start


def pressure_trace(start: int, parent_required: int, max_steps: int) -> dict[str, object]:
    original = int(start)
    current = original
    step = 0
    odd_steps = 0
    max_excess = 0.0
    final_excess = 0.0
    credit = 0
    previous_required = 0

    credit_events: list[dict[str, object]] = []
    pressure_events: list[dict[str, object]] = []
    last_credit_event: dict[str, object] | None = None
    first_required_above_parent: dict[str, object] | None = None
    first_positive_required: dict[str, object] | None = None
    min_surplus = 0
    max_deficit = 0

    def record_credit(kind: str, amount: int, state: int, align: int | None = None) -> None:
        nonlocal credit, last_credit_event
        credit += amount
        event = {
            "kind": kind,
            "amount": amount,
            "credit_after": credit,
            "step": step,
            "state": state,
        }
        if align is not None:
            event["align"] = align
        credit_events.append(event)
        last_credit_event = event

    def observe(event: str) -> None:
        nonlocal previous_required, first_required_above_parent, first_positive_required, min_surplus, max_deficit
        required = min_credit_required(max_excess)
        surplus = credit - required
        min_surplus = min(min_surplus, surplus)
        max_deficit = max(max_deficit, max(0, -surplus))
        if required <= previous_required:
            return

        pressure_event = {
            "event": event,
            "step": step,
            "state": current,
            "odd_steps": odd_steps,
            "max_excess": round_float(max_excess),
            "required": required,
            "credit": credit,
            "surplus": surplus,
            "last_credit_event": last_credit_event,
            "credit_event_count": len(credit_events),
        }
        pressure_events.append(pressure_event)
        if first_positive_required is None:
            first_positive_required = pressure_event
        if first_required_above_parent is None and required > parent_required:
            first_required_above_parent = pressure_event
        previous_required = required

    observe("start")
    while step < max_steps and current > 1:
        if current < original and step >= 3:
            break

        if current & 1:
            align = v2(current + 1)
            if align >= 3:
                q = (current + 1) >> align
                record_credit("high_ladder", align - 2, current, align)
                observe("enter_high_ladder")

                expected_power3 = 1
                for k in range(align):
                    current, parity = shortcut_step(current)
                    step += 1
                    odd_steps += parity
                    final_excess, max_excess = update_excess(odd_steps, step, max_excess)
                    observe("high_ladder_step")
                    expected_power3 *= 3
                    if step >= max_steps:
                        break

                while step < max_steps and current > 1 and current % 2 == 0:
                    current, parity = shortcut_step(current)
                    step += 1
                    final_excess, max_excess = update_excess(odd_steps, step, max_excess)
                    observe("post_ladder_even_step")
                    if current < original and step >= 3:
                        break
                continue

            if current % 8 == 3:
                info = odd3_macro_info(current)
                if str(info["branch"]) == "repeat_minus5_gate":
                    record_credit("low_repeat", 1, current, int(info["minus5_align"]))
                    observe("enter_low_repeat_gate")

        current, parity = shortcut_step(current)
        step += 1
        odd_steps += parity
        final_excess, max_excess = update_excess(odd_steps, step, max_excess)
        observe("ordinary_step")

    max_required = min_credit_required(max_excess)
    if first_required_above_parent is None:
        timing_class = "no_pressure_above_parent"
        threshold_lag = None
    else:
        last = first_required_above_parent["last_credit_event"]
        if last is None:
            timing_class = "no_prior_counted_credit"
            threshold_lag = None
        else:
            threshold_lag = int(first_required_above_parent["step"]) - int(last["step"])
            if threshold_lag == 0:
                timing_class = f"same_step_{last['kind']}"
            else:
                timing_class = f"prior_{last['kind']}"

    return {
        "start": original,
        "certified": current < original,
        "escape_d": step,
        "odd_steps": odd_steps,
        "max_excess": round_float(max_excess),
        "final_excess": round_float(final_excess),
        "max_required": max_required,
        "final_credit": credit,
        "min_surplus": min_surplus,
        "max_deficit": max_deficit,
        "credit_event_count": len(credit_events),
        "pressure_event_count": len(pressure_events),
        "credit_kind_counts": dict(sorted(Counter(str(event["kind"]) for event in credit_events).items())),
        "first_positive_required": first_positive_required,
        "first_required_above_parent": first_required_above_parent,
        "timing_class": timing_class,
        "threshold_lag": threshold_lag,
        "credit_events_before_parent_threshold": (
            0
            if first_required_above_parent is None
            else int(first_required_above_parent["credit_event_count"])
        ),
        "pressure_events": pressure_events,
    }


def transition_row(
    *,
    parent: int,
    child: int,
    child_bit: int,
    parent_row: dict[str, object],
    child_row: dict[str, object],
    child_leaf: object,
) -> dict[str, object]:
    required_delta = int(child_row["max_prefix_required"]) - int(parent_row["max_prefix_required"])
    credit_delta = int(child_row["combined_unit_credit"]) - int(parent_row["combined_unit_credit"])
    return {
        "parent": parent,
        "child": child,
        "child_bit": child_bit,
        "frontier_odd_count": child_leaf.odd_count,
        "frontier_image": child_leaf.image,
        "parent_required": parent_row["max_prefix_required"],
        "child_required": child_row["max_prefix_required"],
        "required_delta": required_delta,
        "parent_credit": parent_row["combined_unit_credit"],
        "child_credit": child_row["combined_unit_credit"],
        "credit_delta": credit_delta,
        "delta_shortfall_after_new_credit": max(0, required_delta - credit_delta),
        "parent_class": parent_row["class"],
        "child_class": child_row["class"],
        "child_escape_d": child_row["escape_d"],
        "child_max_excess": child_row["max_excess"],
        "child_min_prefix_surplus": child_row["min_prefix_surplus"],
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
    retimed_rows: list[dict[str, object]] = []
    all_positive_pressure_count = 0

    for parent in sorted(parent_leaves):
        parent_row = parent_rows[parent]
        for child_bit in (0, 1):
            child = parent + child_bit * step_size
            child_leaf = child_leaves.get(child)
            if child_leaf is None:
                continue
            child_row = analyze_prefix_start(child, args.max_steps)
            row = transition_row(
                parent=parent,
                child=child,
                child_bit=child_bit,
                parent_row=parent_row,
                child_row=child_row,
                child_leaf=child_leaf,
            )
            if int(row["required_delta"]) > 0:
                all_positive_pressure_count += 1
            if int(row["required_delta"]) > 0 and int(row["credit_delta"]) < int(row["required_delta"]):
                trace = pressure_trace(child, int(parent_row["max_prefix_required"]), args.max_steps)
                row["trace"] = {
                    key: value
                    for key, value in trace.items()
                    if key != "pressure_events"
                }
                row["pressure_events"] = trace["pressure_events"][: args.max_pressure_events]
                retimed_rows.append(row)

    timing_counts = Counter(str(row["trace"]["timing_class"]) for row in retimed_rows)
    threshold_lag_values = [
        int(row["trace"]["threshold_lag"])
        for row in retimed_rows
        if row["trace"]["threshold_lag"] is not None
    ]
    margin_at_threshold = []
    for row in retimed_rows:
        event = row["trace"]["first_required_above_parent"]
        if event is not None:
            margin_at_threshold.append(int(event["surplus"]))

    failures = [row for row in retimed_rows if int(row["trace"]["max_deficit"]) > 0]

    return {
        "status": "branch-prefix-retimed-pressure",
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
        "positive_pressure_transition_count": all_positive_pressure_count,
        "retimed_pressure_count": len(retimed_rows),
        "retimed_failure_count": len(failures),
        "timing_class_counts": dict(sorted(timing_counts.items())),
        "credit_kind_counts": dict(
            sorted(
                Counter(
                    kind
                    for row in retimed_rows
                    for kind, count in dict(row["trace"]["credit_kind_counts"]).items()
                    for _ in range(int(count))
                ).items()
            )
        ),
        "threshold_lag_histogram": dict(sorted((str(k), v) for k, v in Counter(threshold_lag_values).items())),
        "threshold_margin_histogram": dict(sorted((str(k), v) for k, v in Counter(margin_at_threshold).items())),
        "max_threshold_lag": max(threshold_lag_values, default=None),
        "max_threshold_margin": max(margin_at_threshold, default=None),
        "min_threshold_margin": min(margin_at_threshold, default=None),
        "max_trace_deficit": max((int(row["trace"]["max_deficit"]) for row in retimed_rows), default=0),
        "largest_delta_shortfalls": sorted(
            retimed_rows,
            key=lambda row: (
                int(row["delta_shortfall_after_new_credit"]),
                int(row["required_delta"]),
                float(row["child_max_excess"]),
                int(row["child"]),
            ),
            reverse=True,
        )[: args.top_n],
        "largest_required_deltas": sorted(
            retimed_rows,
            key=lambda row: (int(row["required_delta"]), float(row["child_max_excess"]), int(row["child"])),
            reverse=True,
        )[: args.top_n],
        "largest_threshold_lags": sorted(
            [row for row in retimed_rows if row["trace"]["threshold_lag"] is not None],
            key=lambda row: (int(row["trace"]["threshold_lag"]), int(row["child"])),
            reverse=True,
        )[: args.top_n],
        "failures": failures[: args.top_n],
        "interpretation": (
            "Finite timing audit for retimed-pressure transitions. Zero trace "
            "deficits mean every audited child had enough visible credit by "
            "the first prefix that exceeded the parent's required credit."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--parent-depth", type=int, default=25)
    parser.add_argument("--max-depth", type=int, default=1024)
    parser.add_argument("--max-steps", type=int, default=50000)
    parser.add_argument("--max-pressure-events", type=int, default=16)
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
    if args.max_pressure_events < 1:
        raise SystemExit("--max-pressure-events must be positive")
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

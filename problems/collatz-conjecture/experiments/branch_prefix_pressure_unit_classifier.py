#!/usr/bin/env python3
"""Classify symbolic features of retimed pressure units.

The pressure-unit audit verifies that every above-parent pressure event in the
retimed hard class is prepaid.  This companion mines theorem-facing features:
which lifted child bit creates the hard class, whether the pressure occurs
inside or after a high ladder, how often low-repeat credit is last, and how
wide the local residue support is.
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


MODULI = (16, 32, 64, 128, 256, 512, 1024, 4096, 65536)


def dict_counter(counter: Counter[object]) -> dict[str, int]:
    return dict(sorted((str(key), int(value)) for key, value in counter.items()))


def bounded_counter(counter: Counter[object], limit: int) -> dict[str, int]:
    return dict(sorted((str(key), int(value)) for key, value in counter.most_common(limit)))


def unit_regime(event: dict[str, object]) -> str:
    last = event.get("last_credit_event")
    if last is None:
        return "missing_credit"
    last_event = dict(last)
    kind = str(last_event["kind"])
    lag = int(event["step"]) - int(last_event["step"])
    align = int(last_event.get("align", 0))
    pressure_event = str(event["event"])
    if kind == "high_ladder":
        if pressure_event == "high_ladder_step" and lag <= align:
            return "high_inside_active_ladder"
        if lag <= align:
            return "high_inside_ladder_window"
        return "high_after_ladder_window"
    if kind == "low_repeat":
        return "low_repeat_prepaid"
    return f"other_{kind}"


def record_residue_counts(
    *,
    counters: dict[str, Counter[int]],
    prefix: str,
    value: int,
) -> None:
    for modulus in MODULI:
        counters[f"{prefix}_mod_{modulus}"][value % modulus] += 1


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
    retimed_transition_count = 0
    positive_pressure_transition_count = 0
    pressure_unit_count = 0

    transition_child_bits: Counter[int] = Counter()
    unit_child_bits: Counter[int] = Counter()
    child_classes: Counter[str] = Counter()
    pressure_events: Counter[str] = Counter()
    unit_regimes: Counter[str] = Counter()
    last_credit_kinds: Counter[str] = Counter()
    last_credit_aligns: Counter[str] = Counter()
    lag_minus_align_by_kind: Counter[str] = Counter()
    lag_by_regime: Counter[str] = Counter()
    step_offset_by_regime: Counter[str] = Counter()
    event_index_by_regime: Counter[str] = Counter()
    parent_required_hist: Counter[int] = Counter()
    child_required_hist: Counter[int] = Counter()
    required_delta_hist: Counter[int] = Counter()
    credit_delta_hist: Counter[int] = Counter()
    required_above_parent_hist: Counter[int] = Counter()
    surplus_hist: Counter[int] = Counter()
    residue_counters: dict[str, Counter[int]] = {f"{name}_mod_{m}": Counter() for name in ("child", "state", "last_credit_state") for m in MODULI}

    max_lag_minus_align: int | None = None
    min_lag_minus_align: int | None = None
    max_step_offset: int | None = None
    min_step_offset: int | None = None
    high_after_ladder_examples: list[dict[str, object]] = []
    low_repeat_examples: list[dict[str, object]] = []
    largest_lag_minus_align_units: list[dict[str, object]] = []
    tightest_units: list[dict[str, object]] = []
    missing_credit_units: list[dict[str, object]] = []
    nonpositive_surplus_units: list[dict[str, object]] = []

    def consider_extreme(records: list[dict[str, object]], record: dict[str, object], key: str, reverse: bool = True) -> None:
        records.append(record)
        records.sort(key=lambda row: (int(row[key]), int(row["child"]), int(row["step"])), reverse=reverse)
        del records[args.top_n :]

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
                positive_pressure_transition_count += 1
            if not (
                int(transition["required_delta"]) > 0
                and int(transition["credit_delta"]) < int(transition["required_delta"])
            ):
                continue

            retimed_transition_count += 1
            transition_child_bits[child_bit] += 1
            child_classes[str(transition["child_class"])] += 1
            parent_required_hist[parent_required] += 1
            child_required_hist[int(transition["child_required"])] += 1
            required_delta_hist[int(transition["required_delta"])] += 1
            credit_delta_hist[int(transition["credit_delta"])] += 1
            record_residue_counts(counters=residue_counters, prefix="child", value=child)

            trace = pressure_trace(child, parent_required, args.max_steps)
            pressure_units = [
                dict(event)
                for event in trace["pressure_events"]
                if int(dict(event)["required"]) > parent_required
            ]

            for event_index, event in enumerate(pressure_units, start=1):
                pressure_unit_count += 1
                unit_child_bits[child_bit] += 1
                pressure_event = str(event["event"])
                pressure_events[pressure_event] += 1
                regime = unit_regime(event)
                unit_regimes[regime] += 1

                required = int(event["required"])
                credit = int(event["credit"])
                required_above = required - parent_required
                surplus = credit - required
                required_above_parent_hist[required_above] += 1
                surplus_hist[surplus] += 1

                step_offset = int(event["step"]) - parent_depth
                max_step_offset = step_offset if max_step_offset is None else max(max_step_offset, step_offset)
                min_step_offset = step_offset if min_step_offset is None else min(min_step_offset, step_offset)
                step_offset_by_regime[f"{regime}:{step_offset}"] += 1
                event_index_by_regime[f"{regime}:{event_index}"] += 1
                record_residue_counts(counters=residue_counters, prefix="state", value=int(event["state"]))

                last = event.get("last_credit_event")
                if last is None:
                    missing_credit_units.append(
                        {
                            "parent": parent,
                            "child": child,
                            "child_bit": child_bit,
                            "event_index": event_index,
                            "event": pressure_event,
                            "step": event["step"],
                            "required": required,
                            "credit": credit,
                            "surplus": surplus,
                        }
                    )
                    continue

                last_event = dict(last)
                kind = str(last_event["kind"])
                align = int(last_event.get("align", 0))
                lag = int(event["step"]) - int(last_event["step"])
                lag_minus_align = lag - align
                max_lag_minus_align = (
                    lag_minus_align
                    if max_lag_minus_align is None
                    else max(max_lag_minus_align, lag_minus_align)
                )
                min_lag_minus_align = (
                    lag_minus_align
                    if min_lag_minus_align is None
                    else min(min_lag_minus_align, lag_minus_align)
                )
                last_credit_kinds[kind] += 1
                last_credit_aligns[f"{kind}:{align}"] += 1
                lag_minus_align_by_kind[f"{kind}:{lag_minus_align}"] += 1
                lag_by_regime[f"{regime}:{lag}"] += 1
                record_residue_counts(counters=residue_counters, prefix="last_credit_state", value=int(last_event["state"]))

                unit_record = {
                    "parent": parent,
                    "child": child,
                    "child_bit": child_bit,
                    "event_index": event_index,
                    "event": pressure_event,
                    "regime": regime,
                    "step": event["step"],
                    "step_offset_from_parent_depth": step_offset,
                    "state": event["state"],
                    "parent_required": parent_required,
                    "required": required,
                    "required_above_parent": required_above,
                    "credit": credit,
                    "surplus": surplus,
                    "last_credit_kind": kind,
                    "last_credit_align": align,
                    "last_credit_step": last_event["step"],
                    "last_credit_state": last_event["state"],
                    "lag": lag,
                    "lag_minus_align": lag_minus_align,
                    "required_delta": transition["required_delta"],
                    "credit_delta": transition["credit_delta"],
                    "child_required": transition["child_required"],
                    "child_credit": transition["child_credit"],
                }

                if surplus <= 0:
                    nonpositive_surplus_units.append(unit_record)
                if regime == "high_after_ladder_window" and len(high_after_ladder_examples) < args.top_n:
                    high_after_ladder_examples.append(unit_record)
                if regime == "low_repeat_prepaid" and len(low_repeat_examples) < args.top_n:
                    low_repeat_examples.append(unit_record)
                consider_extreme(largest_lag_minus_align_units, unit_record, "lag_minus_align")
                tightest_units.append(unit_record)
                tightest_units.sort(
                    key=lambda row: (
                        int(row["surplus"]),
                        -int(row["required_above_parent"]),
                        int(row["child"]),
                        int(row["step"]),
                    )
                )
                del tightest_units[args.top_n :]

    residue_summary = {
        key: {
            "occupied": len(counter),
            "top": bounded_counter(counter, args.residue_top_n),
        }
        for key, counter in sorted(residue_counters.items())
    }

    return {
        "status": "branch-prefix-pressure-unit-classifier",
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
        "positive_pressure_transition_count": positive_pressure_transition_count,
        "retimed_transition_count": retimed_transition_count,
        "pressure_unit_count": pressure_unit_count,
        "transition_child_bit_counts": dict_counter(transition_child_bits),
        "pressure_unit_child_bit_counts": dict_counter(unit_child_bits),
        "retimed_child_class_counts": dict_counter(child_classes),
        "pressure_event_counts": dict_counter(pressure_events),
        "unit_regime_counts": dict_counter(unit_regimes),
        "last_credit_kind_counts": dict_counter(last_credit_kinds),
        "last_credit_align_counts": dict_counter(last_credit_aligns),
        "lag_minus_align_by_kind": dict_counter(lag_minus_align_by_kind),
        "lag_by_regime": dict_counter(lag_by_regime),
        "step_offset_by_regime": dict_counter(step_offset_by_regime),
        "event_index_by_regime": dict_counter(event_index_by_regime),
        "parent_required_histogram": dict_counter(parent_required_hist),
        "child_required_histogram": dict_counter(child_required_hist),
        "required_delta_histogram": dict_counter(required_delta_hist),
        "credit_delta_histogram": dict_counter(credit_delta_hist),
        "required_above_parent_histogram": dict_counter(required_above_parent_hist),
        "surplus_histogram": dict_counter(surplus_hist),
        "max_lag_minus_align": max_lag_minus_align,
        "min_lag_minus_align": min_lag_minus_align,
        "max_step_offset_from_parent_depth": max_step_offset,
        "min_step_offset_from_parent_depth": min_step_offset,
        "residue_summary": residue_summary,
        "pure_feature_claims": {
            "all_retimed_transitions_are_upper_lift_child": dict(transition_child_bits) == {1: retimed_transition_count},
            "all_pressure_units_are_upper_lift_child": dict(unit_child_bits) == {1: pressure_unit_count},
            "all_retimed_children_are_high_assisted": dict(child_classes) == {"high-assisted-descent": retimed_transition_count},
            "all_pressure_units_have_prior_credit": not missing_credit_units,
            "all_pressure_units_have_positive_surplus": not nonpositive_surplus_units,
        },
        "high_after_ladder_examples": high_after_ladder_examples,
        "low_repeat_examples": low_repeat_examples,
        "largest_lag_minus_align_units": largest_lag_minus_align_units,
        "tightest_units": tightest_units,
        "missing_credit_units": missing_credit_units[: args.top_n],
        "nonpositive_surplus_units": nonpositive_surplus_units[: args.top_n],
        "interpretation": (
            "Finite symbolic classifier for the retimed pressure-unit hard class. "
            "The pure-feature claims are theorem signals only; the proof must "
            "derive them from the lifted residue bit and the high/low alignment grammar."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--parent-depth", type=int, default=25)
    parser.add_argument("--max-depth", type=int, default=1024)
    parser.add_argument("--max-steps", type=int, default=50000)
    parser.add_argument("--top-n", type=int, default=12)
    parser.add_argument("--residue-top-n", type=int, default=16)
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
    if args.residue_top_n < 1:
        raise SystemExit("--residue-top-n must be positive")

    payload = run(args)
    text = json.dumps(payload, indent=2, sort_keys=True)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text + "\n", encoding="utf-8")
    if not args.quiet:
        print(text)


if __name__ == "__main__":
    main()

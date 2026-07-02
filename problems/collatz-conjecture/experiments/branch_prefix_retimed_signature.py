#!/usr/bin/env python3
"""Mine symbolic signatures of retimed-pressure transitions.

The retimed-pressure sweep shows that above-parent pressure is one-unit and
prepaid across several exact frontier lifts. This companion asks what the hard
class looks like locally: child bit, descent class, pressure-unit regime,
last-credit timing, and low-residue bucket purity.

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
from branch_prefix_retimed_pressure import pressure_trace, transition_row


DEFAULT_MODULI = (16, 32, 64, 128, 256, 512, 1024, 4096, 65536)


def parse_moduli(raw_values: list[str] | None) -> list[int]:
    if not raw_values:
        return list(DEFAULT_MODULI)
    values: list[int] = []
    for raw in raw_values:
        for part in raw.replace(",", " ").split():
            value = int(part, 0)
            if value < 2 or value & (value - 1):
                raise SystemExit("all residue moduli must be powers of two >= 2")
            values.append(value)
    return sorted(set(values))


def as_counter_dict(counter: Counter[object]) -> dict[str, int]:
    return dict(sorted((str(key), int(value)) for key, value in counter.items()))


def top_counter(counter: Counter[object], limit: int) -> dict[str, int]:
    return dict((str(key), int(value)) for key, value in counter.most_common(limit))


def classify_pressure_unit(event: dict[str, object]) -> str:
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


def add_residue(counters: dict[str, Counter[int]], prefix: str, value: int, moduli: list[int]) -> None:
    for modulus in moduli:
        counters[f"{prefix}_mod_{modulus}"][value % modulus] += 1


def residue_purity_summary(
    *,
    total: Counter[int],
    retimed: Counter[int],
    top_n: int,
) -> dict[str, object]:
    pure_ret = []
    pure_non = []
    mixed = []
    for residue, total_count in total.items():
        retimed_count = int(retimed.get(residue, 0))
        if retimed_count == total_count:
            pure_ret.append((residue, total_count))
        elif retimed_count == 0:
            pure_non.append((residue, total_count))
        else:
            mixed.append((residue, total_count, retimed_count))

    retimed_total = sum(retimed.values())
    pure_retimed_total = sum(count for _, count in pure_ret)
    mixed_retimed_total = sum(ret for _, _, ret in mixed)
    return {
        "occupied_buckets": len(total),
        "retimed_buckets": len(retimed),
        "pure_retimed_buckets": len(pure_ret),
        "pure_nonretimed_buckets": len(pure_non),
        "mixed_buckets": len(mixed),
        "retimed_total": retimed_total,
        "retimed_in_pure_buckets": pure_retimed_total,
        "retimed_in_mixed_buckets": mixed_retimed_total,
        "retimed_pure_bucket_fraction": round_float(pure_retimed_total / retimed_total) if retimed_total else 1.0,
        "top_pure_retimed_buckets": {
            str(residue): int(count)
            for residue, count in sorted(pure_ret, key=lambda item: item[1], reverse=True)[:top_n]
        },
        "top_mixed_buckets": {
            str(residue): {
                "total": int(total_count),
                "retimed": int(retimed_count),
                "retimed_fraction": round_float(retimed_count / total_count),
            }
            for residue, total_count, retimed_count in sorted(
                mixed,
                key=lambda item: (item[2], item[2] / item[1], item[0]),
                reverse=True,
            )[:top_n]
        },
    }


def compact_unit_record(
    *,
    parent: int,
    child: int,
    child_bit: int,
    event_index: int,
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
        "event_index": event_index,
        "event": event["event"],
        "regime": regime,
        "step": event["step"],
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


def run(args: argparse.Namespace) -> dict[str, object]:
    started = perf_counter()
    moduli = parse_moduli(args.residue_moduli)
    parent_depth = args.parent_depth
    child_depth = parent_depth + 1
    max_depth = max(args.max_depth, child_depth)

    parent_frontier, parent_stats = enumerate_frontier(parent_depth, powers_of_three(max_depth))
    child_frontier, child_stats = enumerate_frontier(child_depth, powers_of_three(max_depth))
    parent_leaves = {leaf.residue: leaf for leaf in parent_frontier if leaf.residue > 1}
    child_leaves = {leaf.residue: leaf for leaf in child_frontier if leaf.residue > 1}
    parent_rows = {residue: analyze_prefix_start(residue, args.max_steps) for residue in sorted(parent_leaves)}

    all_child_residues = {modulus: Counter() for modulus in moduli}
    retimed_child_residues = {modulus: Counter() for modulus in moduli}
    residue_counters: dict[str, Counter[int]] = {
        f"{name}_mod_{modulus}": Counter()
        for name in ("retimed_child", "pressure_state", "last_credit_state")
        for modulus in moduli
    }

    positive_pressure_count = 0
    retimed_count = 0
    pressure_unit_count = 0
    first_pressure_unit_count = 0
    retimed_child_bits: Counter[int] = Counter()
    pressure_child_bits: Counter[int] = Counter()
    retimed_child_classes: Counter[str] = Counter()
    pressure_events: Counter[str] = Counter()
    pressure_regimes: Counter[str] = Counter()
    last_credit_kinds: Counter[str] = Counter()
    last_credit_aligns: Counter[str] = Counter()
    lag_minus_align_by_kind: Counter[str] = Counter()
    lag_by_regime: Counter[str] = Counter()
    event_index_by_regime: Counter[str] = Counter()
    parent_required_hist: Counter[int] = Counter()
    child_required_hist: Counter[int] = Counter()
    required_delta_hist: Counter[int] = Counter()
    credit_delta_hist: Counter[int] = Counter()
    required_above_parent_hist: Counter[int] = Counter()
    surplus_hist: Counter[int] = Counter()
    first_required_above_parent_hist: Counter[int] = Counter()
    first_surplus_hist: Counter[int] = Counter()

    missing_credit_units: list[dict[str, object]] = []
    nonpositive_surplus_units: list[dict[str, object]] = []
    high_after_ladder_examples: list[dict[str, object]] = []
    low_repeat_examples: list[dict[str, object]] = []
    tightest_units: list[dict[str, object]] = []
    largest_lag_minus_align_units: list[dict[str, object]] = []

    def keep_tight(record: dict[str, object]) -> None:
        tightest_units.append(record)
        tightest_units.sort(
            key=lambda row: (
                int(row["surplus"]),
                -int(row["required_above_parent"]),
                int(row["child"]),
                int(row["step"]),
            )
        )
        del tightest_units[args.top_n :]

    def keep_lag(record: dict[str, object]) -> None:
        if record["lag_minus_align"] is None:
            return
        largest_lag_minus_align_units.append(record)
        largest_lag_minus_align_units.sort(
            key=lambda row: (
                int(row["lag_minus_align"]),
                int(row["child"]),
                int(row["step"]),
            ),
            reverse=True,
        )
        del largest_lag_minus_align_units[args.top_n :]

    step_size = 1 << parent_depth
    for parent in sorted(parent_leaves):
        parent_row = parent_rows[parent]
        parent_required = int(parent_row["max_prefix_required"])
        for child_bit in (0, 1):
            child = parent + child_bit * step_size
            child_leaf = child_leaves.get(child)
            if child_leaf is None:
                continue
            for modulus in moduli:
                all_child_residues[modulus][child % modulus] += 1
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
            retimed_child_bits[child_bit] += 1
            retimed_child_classes[str(transition["child_class"])] += 1
            parent_required_hist[parent_required] += 1
            child_required_hist[int(transition["child_required"])] += 1
            required_delta_hist[int(transition["required_delta"])] += 1
            credit_delta_hist[int(transition["credit_delta"])] += 1
            add_residue(residue_counters, "retimed_child", child, moduli)
            for modulus in moduli:
                retimed_child_residues[modulus][child % modulus] += 1

            trace = pressure_trace(child, parent_required, args.max_steps)
            pressure_units = [
                dict(event)
                for event in trace["pressure_events"]
                if int(dict(event)["required"]) > parent_required
            ]
            if pressure_units:
                first = pressure_units[0]
                first_required_above_parent_hist[int(first["required"]) - parent_required] += 1
                first_surplus_hist[int(first["credit"]) - int(first["required"])] += 1
                first_pressure_unit_count += 1

            for event_index, event in enumerate(pressure_units, start=1):
                pressure_unit_count += 1
                pressure_child_bits[child_bit] += 1
                pressure_events[str(event["event"])] += 1
                regime = classify_pressure_unit(event)
                pressure_regimes[regime] += 1
                required = int(event["required"])
                credit = int(event["credit"])
                required_above_parent_hist[required - parent_required] += 1
                surplus_hist[credit - required] += 1
                event_index_by_regime[f"{regime}:{event_index}"] += 1
                add_residue(residue_counters, "pressure_state", int(event["state"]), moduli)

                record = compact_unit_record(
                    parent=parent,
                    child=child,
                    child_bit=child_bit,
                    event_index=event_index,
                    event=event,
                    regime=regime,
                    parent_required=parent_required,
                    transition=transition,
                )
                last = event.get("last_credit_event")
                if last is None:
                    missing_credit_units.append(record)
                else:
                    last_event = dict(last)
                    kind = str(last_event["kind"])
                    align = int(last_event.get("align", 0))
                    lag = int(event["step"]) - int(last_event["step"])
                    last_credit_kinds[kind] += 1
                    last_credit_aligns[f"{kind}:{align}"] += 1
                    lag_minus_align_by_kind[f"{kind}:{lag - align}"] += 1
                    lag_by_regime[f"{regime}:{lag}"] += 1
                    add_residue(residue_counters, "last_credit_state", int(last_event["state"]), moduli)

                if int(record["surplus"]) <= 0:
                    nonpositive_surplus_units.append(record)
                if regime == "high_after_ladder_window" and len(high_after_ladder_examples) < args.top_n:
                    high_after_ladder_examples.append(record)
                if regime == "low_repeat_prepaid" and len(low_repeat_examples) < args.top_n:
                    low_repeat_examples.append(record)
                keep_tight(record)
                keep_lag(record)

    residue_summary = {
        key: {
            "occupied": len(counter),
            "top": top_counter(counter, args.residue_top_n),
        }
        for key, counter in sorted(residue_counters.items())
    }
    residue_purity = {
        str(modulus): residue_purity_summary(
            total=all_child_residues[modulus],
            retimed=retimed_child_residues[modulus],
            top_n=args.residue_top_n,
        )
        for modulus in moduli
    }

    return {
        "status": "branch-prefix-retimed-signature",
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
        "retimed_transition_count": retimed_count,
        "first_pressure_unit_count": first_pressure_unit_count,
        "pressure_unit_count": pressure_unit_count,
        "retimed_child_bit_counts": as_counter_dict(retimed_child_bits),
        "pressure_unit_child_bit_counts": as_counter_dict(pressure_child_bits),
        "retimed_child_class_counts": as_counter_dict(retimed_child_classes),
        "pressure_event_counts": as_counter_dict(pressure_events),
        "pressure_regime_counts": as_counter_dict(pressure_regimes),
        "last_credit_kind_counts": as_counter_dict(last_credit_kinds),
        "last_credit_align_counts": as_counter_dict(last_credit_aligns),
        "lag_minus_align_by_kind": as_counter_dict(lag_minus_align_by_kind),
        "lag_by_regime": as_counter_dict(lag_by_regime),
        "event_index_by_regime": as_counter_dict(event_index_by_regime),
        "parent_required_histogram": as_counter_dict(parent_required_hist),
        "child_required_histogram": as_counter_dict(child_required_hist),
        "required_delta_histogram": as_counter_dict(required_delta_hist),
        "credit_delta_histogram": as_counter_dict(credit_delta_hist),
        "first_required_above_parent_histogram": as_counter_dict(first_required_above_parent_hist),
        "first_surplus_histogram": as_counter_dict(first_surplus_hist),
        "required_above_parent_histogram": as_counter_dict(required_above_parent_hist),
        "surplus_histogram": as_counter_dict(surplus_hist),
        "residue_summary": residue_summary,
        "retimed_child_residue_purity": residue_purity,
        "pure_feature_claims": {
            "all_retimed_transitions_are_upper_lift_child": dict(retimed_child_bits) == {1: retimed_count},
            "all_pressure_units_are_upper_lift_child": dict(pressure_child_bits) == {1: pressure_unit_count},
            "all_retimed_children_are_high_assisted": dict(retimed_child_classes) == {
                "high-assisted-descent": retimed_count
            },
            "all_retimed_transitions_have_first_pressure_unit": first_pressure_unit_count == retimed_count,
            "all_first_pressure_units_are_one_unit": dict(first_required_above_parent_hist) == {1: retimed_count},
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
            "Finite symbolic signature miner for retimed-pressure transitions. "
            "Pure-feature claims are theorem signals; residue-purity summaries "
            "test whether fixed low bits alone decide the hard class."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--parent-depth", type=int, default=25)
    parser.add_argument("--max-depth", type=int, default=1024)
    parser.add_argument("--max-steps", type=int, default=50000)
    parser.add_argument("--top-n", type=int, default=12)
    parser.add_argument("--residue-top-n", type=int, default=16)
    parser.add_argument("--residue-moduli", nargs="*")
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

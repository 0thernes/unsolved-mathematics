#!/usr/bin/env python3
"""Audit the phase separator behind terminal-6 tail pressure.

The tail congruence audit found that every post-ladder high-pressure unit has
terminal state `3^a q - 1 == 6 mod 16`, but the same terminal congruence also
appears inside active high ladders.  This companion checks the missing
separator: at the high-ladder terminal, has the relevant required-credit
threshold already been crossed?

This is a finite phase audit, not a Collatz proof.  It uses high-precision
Decimal arithmetic for the excess phase

    odd_steps - log(2)/log(3) * total_steps

and compares terminal-6 high-ladder pressure units by the sign of their
terminal threshold gap.
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from decimal import Decimal, ROUND_CEILING, getcontext
from pathlib import Path
from time import perf_counter

sys.path.insert(0, str(Path(__file__).resolve().parent))

from branch_potential_analyzer import enumerate_frontier, powers_of_three, round_float, shortcut_step, v2
from branch_prefix_dominance_analyzer import analyze_prefix_start
from branch_prefix_post_ladder_tail import reconstruct_tail
from branch_prefix_pressure_unit_classifier import unit_regime
from branch_prefix_retimed_pressure import transition_row
from branch_prefix_tail_congruence import expected_q_mod16


def dict_counter(counter: Counter[object]) -> dict[str, int]:
    return dict(sorted((str(key), int(value)) for key, value in counter.items()))


def dec_string(value: Decimal, digits: int = 30) -> str:
    quant = Decimal(1).scaleb(-digits)
    return format(value.quantize(quant), "f")


def dec_required(max_excess: Decimal) -> int:
    if max_excess < 1:
        return 0
    return int((max_excess - Decimal("0.999")).to_integral_value(rounding=ROUND_CEILING))


def required_lower_edge(required: int) -> Decimal:
    if required <= 0:
        return Decimal("-Infinity")
    if required == 1:
        return Decimal(1)
    return Decimal(required) - Decimal("0.001")


def update_decimal_excess(
    *,
    theta: Decimal,
    odd_steps: int,
    step: int,
    max_excess: Decimal,
) -> tuple[Decimal, Decimal]:
    current = Decimal(odd_steps) - theta * Decimal(step)
    return current, max(max_excess, current)


def detailed_trace(start: int, max_steps: int, theta: Decimal) -> dict[str, object]:
    original = int(start)
    current = original
    step = 0
    odd_steps = 0
    current_excess = Decimal(0)
    max_excess = Decimal(0)
    credit = 0
    previous_required = 0
    credit_id = 0

    observations: list[dict[str, object]] = []
    pressure_events: list[dict[str, object]] = []
    credit_events: list[dict[str, object]] = []
    last_credit_event: dict[str, object] | None = None

    def record_credit(kind: str, amount: int, state: int, align: int | None = None) -> None:
        nonlocal credit, credit_id, last_credit_event
        credit_id += 1
        credit += amount
        event = {
            "credit_id": credit_id,
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
        nonlocal previous_required
        required = dec_required(max_excess)
        observation = {
            "event": event,
            "step": step,
            "state": current,
            "odd_steps": odd_steps,
            "current_excess": current_excess,
            "max_excess": max_excess,
            "required": required,
            "credit": credit,
            "surplus": credit - required,
            "last_credit_event": last_credit_event,
            "credit_event_count": len(credit_events),
        }
        observations.append(observation)
        if required <= previous_required:
            return
        pressure_events.append(observation)
        previous_required = required

    observe("start")
    while step < max_steps and current > 1:
        if current < original and step >= 3:
            break

        if current & 1:
            align = v2(current + 1)
            if align >= 3:
                record_credit("high_ladder", align - 2, current, align)
                observe("enter_high_ladder")

                for _ in range(align):
                    current, parity = shortcut_step(current)
                    step += 1
                    odd_steps += parity
                    current_excess, max_excess = update_decimal_excess(
                        theta=theta,
                        odd_steps=odd_steps,
                        step=step,
                        max_excess=max_excess,
                    )
                    observe("high_ladder_step")
                    if step >= max_steps:
                        break

                while step < max_steps and current > 1 and current % 2 == 0:
                    current, parity = shortcut_step(current)
                    step += 1
                    odd_steps += parity
                    current_excess, max_excess = update_decimal_excess(
                        theta=theta,
                        odd_steps=odd_steps,
                        step=step,
                        max_excess=max_excess,
                    )
                    observe("post_ladder_even_step")
                    if current < original and step >= 3:
                        break
                continue

            if current % 8 == 3:
                macro_value = (9 * current + 5) // 8
                if current % 64 == 59 and v2(macro_value + 5) == v2(current + 5) - 3:
                    record_credit("low_repeat", 1, current, v2(current + 5))
                    observe("enter_low_repeat_gate")

        current, parity = shortcut_step(current)
        step += 1
        odd_steps += parity
        current_excess, max_excess = update_decimal_excess(
            theta=theta,
            odd_steps=odd_steps,
            step=step,
            max_excess=max_excess,
        )
        observe("ordinary_step")

    return {
        "observations": observations,
        "pressure_events": pressure_events,
        "credit_events": credit_events,
    }


def observation_by_step_state(observations: list[dict[str, object]], step: int, state: int) -> dict[str, object] | None:
    for observation in observations:
        if int(observation["step"]) == step and int(observation["state"]) == state:
            return observation
    return None


def pressure_event_key(event: dict[str, object]) -> tuple[int, int, int, str]:
    return (
        int(event["step"]),
        int(event["state"]),
        int(event["required"]),
        str(event["event"]),
    )


def serial_record(record: dict[str, object]) -> dict[str, object]:
    converted: dict[str, object] = {}
    for key, value in record.items():
        if isinstance(value, Decimal):
            converted[key] = dec_string(value)
        else:
            converted[key] = value
    return converted


def run(args: argparse.Namespace) -> dict[str, object]:
    started = perf_counter()
    getcontext().prec = args.precision
    theta = Decimal(2).ln() / Decimal(3).ln()
    eoo_gain = Decimal(2) - Decimal(3) * theta

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
    pressure_unit_count = 0
    high_ladder_pressure_unit_count = 0
    terminal6_count = 0

    regime_counts: Counter[str] = Counter()
    terminal6_regime_counts: Counter[str] = Counter()
    phase_sign_by_regime: Counter[str] = Counter()
    required_delta_by_regime: Counter[str] = Counter()
    lag_minus_align_by_regime: Counter[str] = Counter()
    terminal6_q_rule_by_regime: Counter[str] = Counter()
    event_kind_by_regime: Counter[str] = Counter()
    decimal_event_mismatches: list[dict[str, object]] = []
    reconstruction_misses: list[dict[str, object]] = []
    phase_failures: list[dict[str, object]] = []
    tail_records: list[dict[str, object]] = []
    active_terminal6_records: list[dict[str, object]] = []
    tail_gap_values: list[Decimal] = []
    active_gap_values: list[Decimal] = []
    tail_terminal_to_event_gains: list[Decimal] = []
    tail_event_margins: list[Decimal] = []
    tail_required_delta_from_terminal: Counter[int] = Counter()

    def keep(records: list[dict[str, object]], record: dict[str, object], key: str, reverse: bool = False) -> None:
        records.append(record)
        records.sort(key=lambda row: (Decimal(str(row[key])), int(row["child"]), int(row["event_step"])), reverse=reverse)
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
            if not (
                int(transition["required_delta"]) > 0
                and int(transition["credit_delta"]) < int(transition["required_delta"])
            ):
                continue

            retimed_transition_count += 1
            trace = detailed_trace(child, args.max_steps, theta)
            observations = list(trace["observations"])
            pressure_events = [
                dict(event)
                for event in trace["pressure_events"]
                if int(dict(event)["required"]) > parent_required
            ]
            pressure_unit_count += len(pressure_events)

            for event_index, event in enumerate(pressure_events, start=1):
                last = event.get("last_credit_event")
                if last is None or str(dict(last)["kind"]) != "high_ladder":
                    continue

                high_ladder_pressure_unit_count += 1
                last_event = dict(last)
                align = int(last_event["align"])
                last_credit_state = int(last_event["state"])
                terminal = int(reconstruct_tail(last_credit_state, align)["ladder_terminal"])
                terminal_step = int(last_event["step"]) + align
                terminal_observation = observation_by_step_state(observations, terminal_step, terminal)
                if terminal_observation is None:
                    reconstruction_misses.append(
                        {
                            "parent": parent,
                            "child": child,
                            "event_index": event_index,
                            "terminal_step": terminal_step,
                            "terminal": terminal,
                        }
                    )
                    continue

                regime = unit_regime(event)
                regime_counts[regime] += 1
                threshold = required_lower_edge(int(event["required"]))
                terminal_gap = threshold - Decimal(terminal_observation["max_excess"])
                event_margin = Decimal(event["max_excess"]) - threshold
                terminal_to_event_gain = Decimal(event["max_excess"]) - Decimal(terminal_observation["max_excess"])
                required_delta_from_terminal = int(event["required"]) - int(terminal_observation["required"])
                lag_minus_align = int(event["step"]) - int(last_event["step"]) - align
                q = (last_credit_state + 1) >> align
                q_mod16 = q % 16
                expected_q = expected_q_mod16(align)
                terminal_mod16 = terminal % 16
                is_tail = regime == "high_after_ladder_window"
                phase_positive = terminal_gap > 0
                sign = "positive" if phase_positive else "nonpositive"

                required_delta_by_regime[f"{regime}:{required_delta_from_terminal}"] += 1
                lag_minus_align_by_regime[f"{regime}:{lag_minus_align}"] += 1
                event_kind_by_regime[f"{regime}:{event['event']}"] += 1

                if terminal_mod16 != 6:
                    continue

                terminal6_count += 1
                terminal6_regime_counts[regime] += 1
                phase_sign_by_regime[f"{regime}:{sign}"] += 1
                terminal6_q_rule_by_regime[f"{regime}:a{align % 4}:q{q_mod16}:expected{expected_q}"] += 1

                record = {
                    "parent": parent,
                    "child": child,
                    "child_bit": child_bit,
                    "event_index": event_index,
                    "event": event["event"],
                    "event_step": int(event["step"]),
                    "event_state": int(event["state"]),
                    "regime": regime,
                    "parent_required": parent_required,
                    "event_required": int(event["required"]),
                    "event_credit": int(event["credit"]),
                    "event_surplus": int(event["surplus"]),
                    "last_credit_step": int(last_event["step"]),
                    "last_credit_state": last_credit_state,
                    "align": align,
                    "align_mod4": align % 4,
                    "q_mod16": q_mod16,
                    "expected_q_mod16": expected_q,
                    "terminal_step": terminal_step,
                    "terminal": terminal,
                    "terminal_mod16": terminal_mod16,
                    "terminal_required": int(terminal_observation["required"]),
                    "required_delta_from_terminal": required_delta_from_terminal,
                    "lag_minus_align": lag_minus_align,
                    "threshold": threshold,
                    "terminal_max_excess": Decimal(terminal_observation["max_excess"]),
                    "event_max_excess": Decimal(event["max_excess"]),
                    "terminal_gap_to_event_threshold": terminal_gap,
                    "event_margin_over_threshold": event_margin,
                    "terminal_to_event_gain": terminal_to_event_gain,
                    "eoo_gain": eoo_gain,
                    "phase_positive": phase_positive,
                    "phase_sign_matches_tail": phase_positive == is_tail,
                    "transition_required_delta": transition["required_delta"],
                    "transition_credit_delta": transition["credit_delta"],
                }
                if not bool(record["phase_sign_matches_tail"]):
                    phase_failures.append(serial_record(record))
                if is_tail:
                    tail_gap_values.append(terminal_gap)
                    tail_terminal_to_event_gains.append(terminal_to_event_gain)
                    tail_event_margins.append(event_margin)
                    tail_required_delta_from_terminal[required_delta_from_terminal] += 1
                    keep(tail_records, serial_record(record), "terminal_gap_to_event_threshold")
                else:
                    active_gap_values.append(terminal_gap)
                    keep(active_terminal6_records, serial_record(record), "terminal_gap_to_event_threshold", reverse=True)

            observed_keys = Counter(pressure_event_key(event) for event in pressure_events)
            replayed_keys = Counter(pressure_event_key(event) for event in trace["pressure_events"] if int(event["required"]) > parent_required)
            if observed_keys != replayed_keys and len(decimal_event_mismatches) < args.top_n:
                decimal_event_mismatches.append(
                    {
                        "child": child,
                        "observed": [str(key) for key in sorted(observed_keys)],
                        "replayed": [str(key) for key in sorted(replayed_keys)],
                    }
                )

    pure_claims = {
        "terminal6_phase_sign_classifies_tail": not phase_failures,
        "all_tail_terminal6_phase_positive": phase_sign_by_regime.get("high_after_ladder_window:nonpositive", 0) == 0,
        "all_active_terminal6_phase_nonpositive": all(
            not key.endswith(":positive") or key.startswith("high_after_ladder_window:")
            for key in phase_sign_by_regime
        ),
        "all_tail_terminal_gap_at_most_eoo_gain": all(Decimal(0) < gap <= eoo_gain for gap in tail_gap_values),
        "all_tail_event_margin_positive": all(margin > 0 for margin in tail_event_margins),
        "all_tail_required_delta_from_terminal_is_one": dict(tail_required_delta_from_terminal) == {1: len(tail_gap_values)},
        "no_terminal_reconstruction_misses": not reconstruction_misses,
        "decimal_replay_self_consistent": not decimal_event_mismatches,
    }

    return {
        "status": "branch-prefix-tail-phase",
        "elapsed_seconds": round_float(perf_counter() - started, 6),
        "parameters": {
            key: (str(value) if isinstance(value, Path) else value)
            for key, value in vars(args).items()
        },
        "theta_decimal": dec_string(theta),
        "eoo_gain_decimal": dec_string(eoo_gain),
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
        "retimed_transition_count": retimed_transition_count,
        "pressure_unit_count": pressure_unit_count,
        "high_ladder_pressure_unit_count": high_ladder_pressure_unit_count,
        "terminal6_high_ladder_pressure_unit_count": terminal6_count,
        "pure_claims": pure_claims,
        "regime_counts": dict_counter(regime_counts),
        "terminal6_regime_counts": dict_counter(terminal6_regime_counts),
        "phase_sign_by_regime": dict_counter(phase_sign_by_regime),
        "required_delta_from_terminal_by_regime": dict_counter(required_delta_by_regime),
        "lag_minus_align_by_regime": dict_counter(lag_minus_align_by_regime),
        "terminal6_q_rule_by_regime": dict_counter(terminal6_q_rule_by_regime),
        "event_kind_by_regime": dict_counter(event_kind_by_regime),
        "tail_phase_gap_summary": {
            "count": len(tail_gap_values),
            "min": dec_string(min(tail_gap_values), 24) if tail_gap_values else None,
            "max": dec_string(max(tail_gap_values), 24) if tail_gap_values else None,
            "eoo_gain": dec_string(eoo_gain, 24),
            "terminal_to_event_gain_min": (
                dec_string(min(tail_terminal_to_event_gains), 24) if tail_terminal_to_event_gains else None
            ),
            "terminal_to_event_gain_max": (
                dec_string(max(tail_terminal_to_event_gains), 24) if tail_terminal_to_event_gains else None
            ),
            "event_margin_min": dec_string(min(tail_event_margins), 24) if tail_event_margins else None,
            "event_margin_max": dec_string(max(tail_event_margins), 24) if tail_event_margins else None,
        },
        "active_terminal6_gap_summary": {
            "count": len(active_gap_values),
            "min": dec_string(min(active_gap_values), 24) if active_gap_values else None,
            "max": dec_string(max(active_gap_values), 24) if active_gap_values else None,
        },
        "smallest_tail_positive_gaps": tail_records,
        "closest_active_nonpositive_gaps": active_terminal6_records,
        "phase_failures": phase_failures[: args.top_n],
        "reconstruction_misses": reconstruction_misses[: args.top_n],
        "decimal_event_mismatches": decimal_event_mismatches[: args.top_n],
        "interpretation": (
            "Finite Decimal phase audit.  Among high-ladder pressure units with "
            "terminal 6 mod 16, a positive terminal gap means the target required "
            "threshold was still ahead at ladder burnout and can be crossed by "
            "the EOO tail; a nonpositive gap means the threshold was already "
            "crossed inside the active ladder."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--parent-depth", type=int, default=25)
    parser.add_argument("--max-depth", type=int, default=1024)
    parser.add_argument("--max-steps", type=int, default=50000)
    parser.add_argument("--precision", type=int, default=80)
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
    if args.precision < 40:
        raise SystemExit("--precision must be at least 40")
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

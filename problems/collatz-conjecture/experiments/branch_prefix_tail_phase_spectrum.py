#!/usr/bin/env python3
"""Compress the terminal-6 tail phase separator into max-source data.

`branch_prefix_tail_phase.py` showed that terminal-6 high-ladder pressure units
split exactly by the sign of the terminal threshold gap.  This script asks
whether that gap is a terminal-local quantity or whether it remembers an
earlier prefix maximum.

For a pressure event with required level r and threshold edge L(r), the gap is

    L(r) - max_excess_at_ladder_terminal.

If the source of `max_excess_at_ladder_terminal` is the terminal observation
itself, then the sign reduces to one integer-linear phase inequality
`constant + theta * step`; otherwise the phase lemma has to carry an earlier
prefix witness.
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from decimal import Decimal, getcontext
from pathlib import Path
from time import perf_counter

sys.path.insert(0, str(Path(__file__).resolve().parent))

from branch_potential_analyzer import enumerate_frontier, powers_of_three, round_float
from branch_prefix_dominance_analyzer import analyze_prefix_start
from branch_prefix_post_ladder_tail import reconstruct_tail
from branch_prefix_pressure_unit_classifier import unit_regime
from branch_prefix_retimed_pressure import transition_row
from branch_prefix_tail_phase import dec_string, detailed_trace, required_lower_edge


def dict_counter(counter: Counter[object]) -> dict[str, int]:
    return dict(sorted((str(key), int(value)) for key, value in counter.items()))


def bounded_counter(counter: Counter[object], limit: int) -> dict[str, int]:
    return dict(sorted((str(key), int(value)) for key, value in counter.most_common(limit)))


def observation_by_step_state(observations: list[dict[str, object]], step: int, state: int) -> dict[str, object] | None:
    for observation in observations:
        if int(observation["step"]) == step and int(observation["state"]) == state:
            return observation
    return None


def max_source_before(
    observations: list[dict[str, object]],
    *,
    terminal_step: int,
    terminal_max: Decimal,
) -> dict[str, object] | None:
    source: dict[str, object] | None = None
    for observation in observations:
        if int(observation["step"]) > terminal_step:
            break
        if Decimal(observation["current_excess"]) == terminal_max:
            source = observation
    return source


def threshold_constant(required: int, odd_steps: int) -> str:
    edge = required_lower_edge(required)
    return dec_string(edge - Decimal(odd_steps), 12)


def sign_name(value: Decimal) -> str:
    if value > 0:
        return "positive"
    if value < 0:
        return "negative"
    return "zero"


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
    terminal6_count = 0
    source_miss_count = 0

    terminal_current_is_max_by_regime: Counter[str] = Counter()
    max_source_event_by_regime: Counter[str] = Counter()
    max_source_lag_by_regime: Counter[str] = Counter()
    max_source_step_by_regime: Counter[str] = Counter()
    max_source_current_equals_terminal_by_regime: Counter[str] = Counter()
    phase_linear_form_by_regime: Counter[str] = Counter()
    gap_value_by_regime: Counter[str] = Counter()
    gap_sign_by_regime: Counter[str] = Counter()
    event_required_by_regime: Counter[str] = Counter()
    terminal_required_by_regime: Counter[str] = Counter()
    max_source_required_by_regime: Counter[str] = Counter()
    phase_failures: list[dict[str, object]] = []
    source_misses: list[dict[str, object]] = []
    representative_forms: list[dict[str, object]] = []

    def keep_representative(record: dict[str, object]) -> None:
        if len(representative_forms) < args.top_n:
            representative_forms.append(serial_record(record))

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

            for event_index, event in enumerate(pressure_events, start=1):
                last = event.get("last_credit_event")
                if last is None or str(dict(last)["kind"]) != "high_ladder":
                    continue

                last_event = dict(last)
                align = int(last_event["align"])
                last_credit_state = int(last_event["state"])
                terminal = int(reconstruct_tail(last_credit_state, align)["ladder_terminal"])
                if terminal % 16 != 6:
                    continue

                terminal6_count += 1
                terminal_step = int(last_event["step"]) + align
                terminal_observation = observation_by_step_state(observations, terminal_step, terminal)
                if terminal_observation is None:
                    source_miss_count += 1
                    if len(source_misses) < args.top_n:
                        source_misses.append(
                            {
                                "parent": parent,
                                "child": child,
                                "event_index": event_index,
                                "reason": "missing terminal observation",
                            }
                        )
                    continue

                terminal_max = Decimal(terminal_observation["max_excess"])
                source = max_source_before(
                    observations,
                    terminal_step=terminal_step,
                    terminal_max=terminal_max,
                )
                if source is None:
                    source_miss_count += 1
                    if len(source_misses) < args.top_n:
                        source_misses.append(
                            {
                                "parent": parent,
                                "child": child,
                                "event_index": event_index,
                                "reason": "missing max source",
                                "terminal_max": dec_string(terminal_max),
                            }
                        )
                    continue

                regime = unit_regime(event)
                threshold = required_lower_edge(int(event["required"]))
                gap = threshold - terminal_max
                terminal_current_is_max = Decimal(terminal_observation["current_excess"]) == terminal_max
                source_is_terminal = int(source["step"]) == terminal_step and int(source["state"]) == terminal
                source_lag = terminal_step - int(source["step"])
                constant = threshold_constant(int(event["required"]), int(source["odd_steps"]))
                linear_key = f"step={int(source['step'])};constant={constant}"
                sign = sign_name(gap)
                is_tail = regime == "high_after_ladder_window"
                sign_matches_tail = (gap > 0) == is_tail

                terminal_current_is_max_by_regime[f"{regime}:{terminal_current_is_max}"] += 1
                max_source_event_by_regime[f"{regime}:{source['event']}"] += 1
                max_source_lag_by_regime[f"{regime}:{source_lag}"] += 1
                max_source_step_by_regime[f"{regime}:{int(source['step'])}"] += 1
                max_source_current_equals_terminal_by_regime[f"{regime}:{source_is_terminal}"] += 1
                phase_linear_form_by_regime[f"{regime}:{linear_key}"] += 1
                gap_value_by_regime[f"{regime}:{dec_string(gap, 24)}"] += 1
                gap_sign_by_regime[f"{regime}:{sign}"] += 1
                event_required_by_regime[f"{regime}:{int(event['required'])}"] += 1
                terminal_required_by_regime[f"{regime}:{int(terminal_observation['required'])}"] += 1
                max_source_required_by_regime[f"{regime}:{int(source['required'])}"] += 1

                record = {
                    "parent": parent,
                    "child": child,
                    "event_index": event_index,
                    "regime": regime,
                    "event": event["event"],
                    "event_step": int(event["step"]),
                    "event_required": int(event["required"]),
                    "terminal_step": terminal_step,
                    "terminal": terminal,
                    "terminal_current_is_max": terminal_current_is_max,
                    "max_source_is_terminal": source_is_terminal,
                    "max_source_event": source["event"],
                    "max_source_step": int(source["step"]),
                    "max_source_lag_from_terminal": source_lag,
                    "max_source_odd_steps": int(source["odd_steps"]),
                    "max_source_required": int(source["required"]),
                    "phase_linear_form": linear_key,
                    "gap": gap,
                    "gap_sign": sign,
                    "sign_matches_tail": sign_matches_tail,
                    "transition_required_delta": transition["required_delta"],
                    "transition_credit_delta": transition["credit_delta"],
                }
                keep_representative(record)
                if not sign_matches_tail:
                    phase_failures.append(serial_record(record))

    pure_claims = {
        "phase_sign_still_classifies_tail": not phase_failures,
        "all_terminal6_sources_found": source_miss_count == 0,
        "terminal_current_is_always_max": dict(terminal_current_is_max_by_regime)
        == {
            "high_after_ladder_window:True": 340,
            "high_inside_active_ladder:True": 656,
        },
        "max_source_is_always_terminal": dict(max_source_current_equals_terminal_by_regime)
        == {
            "high_after_ladder_window:True": 340,
            "high_inside_active_ladder:True": 656,
        },
    }

    return {
        "status": "branch-prefix-tail-phase-spectrum",
        "elapsed_seconds": round_float(perf_counter() - started, 6),
        "parameters": {
            key: (str(value) if isinstance(value, Path) else value)
            for key, value in vars(args).items()
        },
        "theta_decimal": dec_string(theta),
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
        "terminal6_high_ladder_pressure_unit_count": terminal6_count,
        "source_miss_count": source_miss_count,
        "pure_claims": pure_claims,
        "terminal_current_is_max_by_regime": dict_counter(terminal_current_is_max_by_regime),
        "max_source_is_terminal_by_regime": dict_counter(max_source_current_equals_terminal_by_regime),
        "max_source_event_by_regime": dict_counter(max_source_event_by_regime),
        "max_source_lag_by_regime": dict_counter(max_source_lag_by_regime),
        "max_source_step_by_regime": dict_counter(max_source_step_by_regime),
        "gap_sign_by_regime": dict_counter(gap_sign_by_regime),
        "event_required_by_regime": dict_counter(event_required_by_regime),
        "terminal_required_by_regime": dict_counter(terminal_required_by_regime),
        "max_source_required_by_regime": dict_counter(max_source_required_by_regime),
        "phase_linear_form_by_regime_top": bounded_counter(phase_linear_form_by_regime, args.hist_top_n),
        "gap_value_by_regime_top": bounded_counter(gap_value_by_regime, args.hist_top_n),
        "phase_linear_form_distinct_count": len(phase_linear_form_by_regime),
        "gap_value_distinct_count": len(gap_value_by_regime),
        "representative_forms": representative_forms,
        "phase_failures": phase_failures[: args.top_n],
        "source_misses": source_misses[: args.top_n],
        "interpretation": (
            "Finite max-source spectrum for terminal-6 high-ladder pressure units. "
            "If max_source_is_always_terminal holds, the phase-tail separator is "
            "terminal-local and reduces to integer-linear inequalities of the "
            "form constant + theta * terminal_step."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--parent-depth", type=int, default=25)
    parser.add_argument("--max-depth", type=int, default=1024)
    parser.add_argument("--max-steps", type=int, default=50000)
    parser.add_argument("--precision", type=int, default=80)
    parser.add_argument("--top-n", type=int, default=12)
    parser.add_argument("--hist-top-n", type=int, default=24)
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
    if args.hist_top_n < 1:
        raise SystemExit("--hist-top-n must be positive")

    payload = run(args)
    text = json.dumps(payload, indent=2, sort_keys=True)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text + "\n", encoding="utf-8")
    if not args.quiet:
        print(text)


if __name__ == "__main__":
    main()

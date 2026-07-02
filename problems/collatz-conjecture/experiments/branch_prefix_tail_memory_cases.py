#!/usr/bin/env python3
"""Extract the six non-terminal max-source tail cases.

The phase-spectrum audit found that the terminal-6 phase separator is almost
terminal-local, except for six post-ladder tail cases whose max excess is
reached eight shortcut steps before the high-ladder terminal.  This script
extracts those cases and records their local grammar.
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

from branch_potential_analyzer import enumerate_frontier, powers_of_three, round_float, shortcut_step
from branch_prefix_dominance_analyzer import analyze_prefix_start
from branch_prefix_post_ladder_tail import parity_word, reconstruct_tail
from branch_prefix_pressure_unit_classifier import unit_regime
from branch_prefix_retimed_pressure import transition_row
from branch_prefix_tail_phase import dec_string, detailed_trace, required_lower_edge
from branch_prefix_tail_phase_spectrum import max_source_before, observation_by_step_state, threshold_constant


MODULI = (16, 32, 64, 128, 256, 512, 1024, 4096, 65536)


def dict_counter(counter: Counter[object]) -> dict[str, int]:
    return dict(sorted((str(key), int(value)) for key, value in counter.items()))


def add_residues(counter: Counter[str], name: str, value: int) -> None:
    for modulus in MODULI:
        counter[f"{name}_mod_{modulus}={value % modulus}"] += 1


def shortcut_segment(start: int, steps: int) -> dict[str, object]:
    current = start
    parities: list[int] = []
    states = [current]
    transitions: list[dict[str, object]] = []
    for index in range(1, steps + 1):
        before = current
        current, parity = shortcut_step(current)
        parities.append(parity)
        states.append(current)
        transitions.append(
            {
                "index": index,
                "before": before,
                "before_mod_64": before % 64,
                "parity": parity,
                "after": current,
                "after_mod_64": current % 64,
            }
        )
    return {
        "end": current,
        "parity_word": parity_word(parities),
        "states_mod_64": [state % 64 for state in states],
        "transitions": transitions,
    }


def serial_decimal(value: Decimal) -> str:
    return dec_string(value, 30)


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
    terminal6_tail_count = 0
    memory_tail_count = 0

    align_hist: Counter[int] = Counter()
    source_lag_hist: Counter[int] = Counter()
    source_event_hist: Counter[str] = Counter()
    source_to_terminal_word_hist: Counter[str] = Counter()
    terminal_to_event_word_hist: Counter[str] = Counter()
    source_to_terminal_states_mod64_hist: Counter[str] = Counter()
    phase_form_hist: Counter[str] = Counter()
    gap_hist: Counter[str] = Counter()
    residue_hist: Counter[str] = Counter()
    required_triple_hist: Counter[str] = Counter()
    q_mod16_hist: Counter[str] = Counter()
    records: list[dict[str, object]] = []
    misses: list[dict[str, object]] = []

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
                if unit_regime(event) != "high_after_ladder_window":
                    continue
                last = event.get("last_credit_event")
                if last is None or str(dict(last)["kind"]) != "high_ladder":
                    continue

                last_event = dict(last)
                align = int(last_event["align"])
                last_credit_state = int(last_event["state"])
                reconstructed = reconstruct_tail(last_credit_state, align)
                terminal = int(reconstructed["ladder_terminal"])
                if terminal % 16 != 6:
                    continue

                terminal6_tail_count += 1
                terminal_step = int(last_event["step"]) + align
                terminal_observation = observation_by_step_state(observations, terminal_step, terminal)
                if terminal_observation is None:
                    misses.append({"parent": parent, "child": child, "reason": "missing terminal observation"})
                    continue

                terminal_max = Decimal(terminal_observation["max_excess"])
                source = max_source_before(
                    observations,
                    terminal_step=terminal_step,
                    terminal_max=terminal_max,
                )
                if source is None:
                    misses.append({"parent": parent, "child": child, "reason": "missing max source"})
                    continue

                source_lag = terminal_step - int(source["step"])
                if source_lag == 0:
                    continue

                memory_tail_count += 1
                source_state = int(source["state"])
                source_to_terminal = shortcut_segment(source_state, source_lag)
                terminal_to_event = shortcut_segment(terminal, int(event["step"]) - terminal_step)
                threshold = required_lower_edge(int(event["required"]))
                gap = threshold - terminal_max
                terminal_current_gap = threshold - Decimal(terminal_observation["current_excess"])
                memory_drop = Decimal(source["current_excess"]) - Decimal(terminal_observation["current_excess"])
                q = (last_credit_state + 1) >> align
                phase_form = f"step={int(source['step'])};constant={threshold_constant(int(event['required']), int(source['odd_steps']))}"
                state_word = ",".join(str(value) for value in source_to_terminal["states_mod_64"])

                align_hist[align] += 1
                source_lag_hist[source_lag] += 1
                source_event_hist[str(source["event"])] += 1
                source_to_terminal_word_hist[str(source_to_terminal["parity_word"])] += 1
                terminal_to_event_word_hist[str(terminal_to_event["parity_word"])] += 1
                source_to_terminal_states_mod64_hist[state_word] += 1
                phase_form_hist[phase_form] += 1
                gap_hist[dec_string(gap, 24)] += 1
                required_triple_hist[
                    f"source={int(source['required'])};terminal={int(terminal_observation['required'])};event={int(event['required'])}"
                ] += 1
                q_mod16_hist[f"a_mod4={align % 4};q_mod16={q % 16}"] += 1
                for name, value in (
                    ("parent", parent),
                    ("child", child),
                    ("last_credit_state", last_credit_state),
                    ("source_state", source_state),
                    ("terminal", terminal),
                    ("event_state", int(event["state"])),
                ):
                    add_residues(residue_hist, name, value)

                records.append(
                    {
                        "parent": parent,
                        "child": child,
                        "child_bit": child_bit,
                        "event_index": event_index,
                        "event_step": int(event["step"]),
                        "event_state": int(event["state"]),
                        "event_required": int(event["required"]),
                        "event_credit": int(event["credit"]),
                        "event_surplus": int(event["surplus"]),
                        "last_credit_step": int(last_event["step"]),
                        "last_credit_state": last_credit_state,
                        "align": align,
                        "q": q,
                        "q_mod16": q % 16,
                        "source_step": int(source["step"]),
                        "source_state": source_state,
                        "source_event": source["event"],
                        "source_required": int(source["required"]),
                        "source_lag_to_terminal": source_lag,
                        "source_to_terminal_parity_word": source_to_terminal["parity_word"],
                        "source_to_terminal_states_mod64": source_to_terminal["states_mod_64"],
                        "terminal_step": terminal_step,
                        "terminal": terminal,
                        "terminal_mod64": terminal % 64,
                        "terminal_required": int(terminal_observation["required"]),
                        "terminal_to_event_parity_word": terminal_to_event["parity_word"],
                        "terminal_to_event_states_mod64": terminal_to_event["states_mod_64"],
                        "phase_form": phase_form,
                        "gap": serial_decimal(gap),
                        "terminal_current_gap": serial_decimal(terminal_current_gap),
                        "memory_drop": serial_decimal(memory_drop),
                        "transition_required_delta": transition["required_delta"],
                        "transition_credit_delta": transition["credit_delta"],
                    }
                )

    records.sort(key=lambda row: (int(row["source_step"]), int(row["child"])))
    pure_claims = {
        "all_memory_tail_source_lag_is_8": dict(source_lag_hist) == {8: memory_tail_count},
        "single_source_to_terminal_word": len(source_to_terminal_word_hist) == 1,
        "single_terminal_to_event_word": len(terminal_to_event_word_hist) == 1,
        "all_memory_records_positive_gap": all(Decimal(row["gap"]) > 0 for row in records),
        "all_memory_records_terminal_current_gap_positive": all(
            Decimal(row["terminal_current_gap"]) > 0 for row in records
        ),
        "all_sources_found": not misses,
    }

    return {
        "status": "branch-prefix-tail-memory-cases",
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
        "terminal6_tail_count": terminal6_tail_count,
        "memory_tail_count": memory_tail_count,
        "pure_claims": pure_claims,
        "align_histogram": dict_counter(align_hist),
        "source_lag_histogram": dict_counter(source_lag_hist),
        "source_event_histogram": dict_counter(source_event_hist),
        "source_to_terminal_word_histogram": dict_counter(source_to_terminal_word_hist),
        "terminal_to_event_word_histogram": dict_counter(terminal_to_event_word_hist),
        "source_to_terminal_states_mod64_histogram": dict_counter(source_to_terminal_states_mod64_hist),
        "phase_form_histogram": dict_counter(phase_form_hist),
        "gap_histogram": dict_counter(gap_hist),
        "required_triple_histogram": dict_counter(required_triple_hist),
        "q_mod16_histogram": dict_counter(q_mod16_hist),
        "residue_histogram": dict_counter(residue_hist),
        "records": records,
        "misses": misses[: args.top_n],
        "interpretation": (
            "Finite extractor for the six post-ladder terminal-6 cases whose "
            "terminal phase max is sourced before the ladder terminal.  These "
            "are the memory subcase left by the phase-spectrum audit."
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

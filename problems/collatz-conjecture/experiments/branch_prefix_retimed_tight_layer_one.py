#!/usr/bin/env python3
"""Extract and analyze the tight surplus-one retimed pressure units.

The layer-margin sweep shows that only layer one reaches surplus 1 in the
checked retimed hard case.  This script re-enumerates the exact lifts and
records every pressure unit with the requested surplus, then checks the
common algebraic fingerprint.

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
from branch_prefix_retimed_post_ladder_tail import as_counter_dict, parity_word, simulate_steps
from branch_prefix_retimed_pressure import pressure_trace, transition_row
from branch_prefix_retimed_signature import classify_pressure_unit


DEFAULT_RESIDUE_MODULI = (16, 32, 64, 128, 256, 512, 1024, 4096, 65536)


def post_ladder_formula(terminal: int, word: str) -> int | None:
    if word == "EOO":
        return (9 * terminal + 10) // 8
    if word == "EEO":
        return (3 * terminal + 4) // 8
    return None


def compact_record(
    *,
    parent_depth: int,
    parent: int,
    child: int,
    child_bit: int,
    event_index: int,
    event: dict[str, object],
    regime: str,
    transition: dict[str, object],
) -> dict[str, object]:
    last = dict(event["last_credit_event"])
    entry = int(last["state"])
    align = int(last["align"])
    q = (entry + 1) >> align
    lag = int(event["step"]) - int(last["step"])
    state = int(event["state"])
    terminal = (3**align) * q - 1
    terminal_state, ladder_parities = simulate_steps(entry, align)
    post_lag = max(0, lag - align)
    post_state = terminal
    post_word = ""
    if post_lag:
        post_state, post_parities = simulate_steps(terminal, post_lag)
        post_word = parity_word(post_parities)
    expected_active_state = None
    if lag <= align:
        expected_active_state = (3**lag) * (1 << (align - lag)) * q - 1
    post_formula_value = post_ladder_formula(terminal, post_word) if post_word else None

    required_above_parent = int(event["required"]) - int(transition["parent_required"])
    surplus = int(event["credit"]) - int(event["required"])
    return {
        "parent_depth": parent_depth,
        "child_depth": parent_depth + 1,
        "parent": parent,
        "child": child,
        "child_bit": child_bit,
        "event_index": event_index,
        "event": event["event"],
        "regime": regime,
        "step": event["step"],
        "step_offset_from_parent_depth": int(event["step"]) - parent_depth,
        "state": state,
        "parent_required": transition["parent_required"],
        "child_required": transition["child_required"],
        "required_delta": transition["required_delta"],
        "credit_delta": transition["credit_delta"],
        "required": event["required"],
        "required_above_parent": required_above_parent,
        "credit": event["credit"],
        "surplus": surplus,
        "credit_above_parent": int(event["credit"]) - int(transition["parent_required"]),
        "last_credit_kind": last["kind"],
        "last_credit_step": last["step"],
        "last_credit_state": entry,
        "last_credit_align": align,
        "q": q,
        "q_mod_8": q % 8,
        "q_mod_16": q % 16,
        "lag_from_credit": lag,
        "lag_minus_align": lag - align,
        "terminal": terminal,
        "terminal_matches_simulation": terminal == terminal_state,
        "ladder_word": parity_word(ladder_parities),
        "terminal_mod_16": terminal % 16,
        "terminal_mod_64": terminal % 64,
        "post_lag": post_lag,
        "post_word": post_word,
        "post_state": post_state,
        "post_formula_value": post_formula_value,
        "expected_active_state": expected_active_state,
        "active_formula_matches": expected_active_state == state if expected_active_state is not None else None,
        "post_formula_matches": post_formula_value == state if post_formula_value is not None else None,
        "parent_residues": {str(modulus): parent % modulus for modulus in DEFAULT_RESIDUE_MODULI},
        "child_residues": {str(modulus): child % modulus for modulus in DEFAULT_RESIDUE_MODULI},
        "state_residues": {str(modulus): state % modulus for modulus in DEFAULT_RESIDUE_MODULI},
        "entry_residues": {str(modulus): entry % modulus for modulus in DEFAULT_RESIDUE_MODULI},
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
    selected: list[dict[str, object]] = []

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
            for event_index, event in enumerate(pressure_units, start=1):
                pressure_unit_count += 1
                surplus = int(event["credit"]) - int(event["required"])
                layer = int(event["required"]) - parent_required
                if surplus != args.surplus:
                    continue
                if args.layer is not None and layer != args.layer:
                    continue
                regime = classify_pressure_unit(event)
                selected.append(
                    compact_record(
                        parent_depth=parent_depth,
                        parent=parent,
                        child=child,
                        child_bit=int(transition["child_bit"]),
                        event_index=event_index,
                        event=event,
                        regime=regime,
                        transition=transition,
                    )
                )

    return {
        "status": "branch-prefix-retimed-tight-layer-one-depth",
        "elapsed_seconds": round_float(perf_counter() - started, 6),
        "parent_depth": parent_depth,
        "child_depth": child_depth,
        "frontiers": {
            "parent": {**parent_stats, "positive_live_count": len(parent_leaves), "depth": parent_depth},
            "child": {**child_stats, "positive_live_count": len(child_leaves), "depth": child_depth},
        },
        "retimed_transition_count": retimed_count,
        "above_parent_pressure_unit_count": pressure_unit_count,
        "selected_count": len(selected),
        "selected": selected,
    }


def update_counts(counter: Counter[str], records: list[dict[str, object]], key: str) -> None:
    counter.update(str(record[key]) if record[key] != "" else "<active>" for record in records)


def nested_residue_counts(records: list[dict[str, object]], key: str) -> dict[str, dict[str, int]]:
    result: dict[str, Counter[str]] = {str(modulus): Counter() for modulus in DEFAULT_RESIDUE_MODULI}
    for record in records:
        residues = dict(record[key])
        for modulus, residue in residues.items():
            result[str(modulus)][str(residue)] += 1
    return {modulus: as_counter_dict(counter) for modulus, counter in result.items()}


def run(args: argparse.Namespace) -> dict[str, object]:
    rows = []
    records: list[dict[str, object]] = []
    for depth in range(args.min_parent_depth, args.max_parent_depth + 1):
        payload = analyze_depth(args, depth)
        rows.append(
            {
                "parent_depth": payload["parent_depth"],
                "child_depth": payload["child_depth"],
                "retimed_transition_count": payload["retimed_transition_count"],
                "above_parent_pressure_unit_count": payload["above_parent_pressure_unit_count"],
                "selected_count": payload["selected_count"],
            }
        )
        records.extend(list(payload["selected"]))

    counter_fields = {
        "parent_depth_counts": "parent_depth",
        "regime_counts": "regime",
        "event_counts": "event",
        "child_bit_counts": "child_bit",
        "required_counts": "required",
        "parent_required_counts": "parent_required",
        "child_required_counts": "child_required",
        "required_delta_counts": "required_delta",
        "credit_delta_counts": "credit_delta",
        "credit_counts": "credit",
        "credit_above_parent_counts": "credit_above_parent",
        "last_credit_align_counts": "last_credit_align",
        "lag_from_credit_counts": "lag_from_credit",
        "lag_minus_align_counts": "lag_minus_align",
        "step_offset_counts": "step_offset_from_parent_depth",
        "terminal_mod_16_counts": "terminal_mod_16",
        "post_word_counts": "post_word",
        "q_mod_16_counts": "q_mod_16",
    }
    counters: dict[str, Counter[str]] = {key: Counter() for key in counter_fields}
    for counter_key, record_key in counter_fields.items():
        update_counts(counters[counter_key], records, record_key)

    all_layer_one = all(int(record["required_above_parent"]) == 1 and int(record["event_index"]) == 1 for record in records)
    all_parent_required_one = all(int(record["parent_required"]) == 1 for record in records)
    all_required_delta_one = all(int(record["required_delta"]) == 1 for record in records)
    all_zero_transition_credit_delta = all(int(record["credit_delta"]) == 0 for record in records)
    all_credit_three_required_two = all(
        int(record["credit"]) == 3 and int(record["required"]) == 2 and int(record["credit_above_parent"]) == 2
        for record in records
    )
    all_align_three = all(int(record["last_credit_align"]) == 3 for record in records)
    all_high_ladder_credit = all(str(record["last_credit_kind"]) == "high_ladder" for record in records)
    all_upper_child = all(int(record["child_bit"]) == 1 for record in records)
    all_step_offset_one = all(int(record["step_offset_from_parent_depth"]) == 1 for record in records)
    active_ok = all(
        bool(record["active_formula_matches"])
        for record in records
        if str(record["regime"]) == "high_inside_active_ladder"
    )
    post_ok = all(
        str(record["post_word"]) == "EOO"
        and bool(record["post_formula_matches"])
        and int(record["terminal_mod_16"]) == 6
        for record in records
        if str(record["regime"]) == "high_after_ladder_window"
    )

    return {
        "status": "branch-prefix-retimed-tight-layer-one",
        "parameters": {
            "min_parent_depth": args.min_parent_depth,
            "max_parent_depth": args.max_parent_depth,
            "max_depth": args.max_depth,
            "max_steps": args.max_steps,
            "surplus": args.surplus,
            "layer": args.layer,
        },
        "depths": rows,
        "checks": {
            "selected_count": len(records),
            "all_selected_are_layer_one": all_layer_one,
            "all_selected_have_parent_required_1": all_parent_required_one,
            "all_selected_have_required_delta_1": all_required_delta_one,
            "all_selected_have_zero_transition_credit_delta": all_zero_transition_credit_delta,
            "all_selected_have_credit_3_required_2_credit_above_parent_2": all_credit_three_required_two,
            "all_selected_have_high_ladder_credit": all_high_ladder_credit,
            "all_selected_have_align_3": all_align_three,
            "all_selected_are_upper_child": all_upper_child,
            "all_selected_have_step_offset_1": all_step_offset_one,
            "all_active_selected_match_terminal_ladder_formula": active_ok,
            "all_post_selected_match_EOO_terminal_6_mod_16": post_ok,
        },
        "counts": {key: as_counter_dict(counter) for key, counter in counters.items()},
        "residue_counts": {
            "parent": nested_residue_counts(records, "parent_residues"),
            "child": nested_residue_counts(records, "child_residues"),
            "entry": nested_residue_counts(records, "entry_residues"),
            "state": nested_residue_counts(records, "state_residues"),
        },
        "records": records,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--min-parent-depth", type=int, default=18)
    parser.add_argument("--max-parent-depth", type=int, default=25)
    parser.add_argument("--max-depth", type=int, default=1024)
    parser.add_argument("--max-steps", type=int, default=50000)
    parser.add_argument("--surplus", type=int, default=1)
    parser.add_argument("--layer", type=int, default=1)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    if args.min_parent_depth < 1:
        raise SystemExit("--min-parent-depth must be positive")
    if args.max_parent_depth < args.min_parent_depth:
        raise SystemExit("--max-parent-depth must be >= --min-parent-depth")
    if args.max_steps < 1:
        raise SystemExit("--max-steps must be positive")
    if args.layer is not None and args.layer < 1:
        raise SystemExit("--layer must be positive when provided")

    payload = run(args)
    text = json.dumps(payload, indent=2, sort_keys=True)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text + "\n", encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()

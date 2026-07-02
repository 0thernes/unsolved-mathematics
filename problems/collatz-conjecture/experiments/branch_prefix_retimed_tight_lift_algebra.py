#!/usr/bin/env python3
"""Check the lift algebra behind tight retimed layer-one units.

The tight layer-one extractor isolates five surplus-one pressure units.  This
companion does not re-select them from the frontier.  Instead it loads those
records and verifies the parent/upper-child affine lift law around the pressure
boundary:

    T^j(child) - T^j(parent) = 3^o_j 2^(d-j),  0 <= j <= d.

The output is theorem-target evidence, not a proof of Collatz.
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from branch_potential_analyzer import THETA, min_credit_required, round_float, shortcut_step, v2
from branch_prefix_retimed_post_ladder_tail import as_counter_dict


DEFAULT_INPUT = Path("experiments/results/branch_prefix_retimed_tight_layer_one_d18_d25_20260702.json")


def parity_word(bits: list[int]) -> str:
    return "".join("O" if bit else "E" for bit in bits)


def trajectory(start: int, steps: int) -> tuple[list[int], list[int]]:
    current = start
    states = [current]
    parities: list[int] = []
    for _ in range(steps):
        current, parity = shortcut_step(current)
        parities.append(int(parity))
        states.append(current)
    return states, parities


def odd_prefix_counts(parities: list[int]) -> list[int]:
    counts = [0]
    total = 0
    for parity in parities:
        total += int(parity)
        counts.append(total)
    return counts


def required_path(parities: list[int]) -> list[dict[str, object]]:
    max_excess = 0.0
    rows: list[dict[str, object]] = []
    for step in range(len(parities) + 1):
        odd_steps = sum(parities[:step])
        excess = odd_steps - THETA * step
        max_excess = max(max_excess, excess)
        rows.append(
            {
                "step": step,
                "odd_steps": odd_steps,
                "excess": round_float(excess, 9),
                "max_excess": round_float(max_excess, 9),
                "required": min_credit_required(max_excess),
            }
        )
    return rows


def analyze_record(record: dict[str, object]) -> dict[str, object]:
    d = int(record["parent_depth"])
    pressure_step = int(record["step"])
    entry_step = int(record["last_credit_step"])
    align = int(record["last_credit_align"])
    terminal_step = entry_step + align

    parent_states, parent_parities = trajectory(int(record["parent"]), pressure_step)
    child_states, child_parities = trajectory(int(record["child"]), pressure_step)
    child_odd_prefix = odd_prefix_counts(child_parities)

    affine_failures = []
    for step in range(d + 1):
        predicted_delta = (3 ** child_odd_prefix[step]) * (1 << (d - step))
        actual_delta = child_states[step] - parent_states[step]
        if actual_delta != predicted_delta:
            affine_failures.append(
                {
                    "step": step,
                    "actual_delta": actual_delta,
                    "predicted_delta": predicted_delta,
                }
            )

    parent_required_rows = required_path(parent_parities)
    child_required_rows = required_path(child_parities)
    parent_odd_prefix = odd_prefix_counts(parent_parities)
    entry_delta = child_states[entry_step] - parent_states[entry_step]
    entry_delta_power = d - entry_step
    entry_delta_odd_factor = entry_delta >> entry_delta_power if entry_delta_power >= 0 else None
    q = int(record["q"])
    terminal = (3**align) * q - 1
    active_expected = terminal
    post_expected = None
    if str(record["post_word"]) == "EOO":
        post_expected = (9 * terminal + 10) // 8

    pressure_excess_gap = (
        float(child_required_rows[pressure_step]["excess"]) - float(parent_required_rows[pressure_step]["excess"])
    )

    return {
        "parent_depth": d,
        "parent": int(record["parent"]),
        "child": int(record["child"]),
        "regime": record["regime"],
        "pressure_step": pressure_step,
        "pressure_offset_from_depth": pressure_step - d,
        "entry_step": entry_step,
        "entry_offset_from_depth": entry_step - d,
        "terminal_step": terminal_step,
        "terminal_offset_from_depth": terminal_step - d,
        "local_word_entry_to_pressure": parity_word(child_parities[entry_step:pressure_step]),
        "boundary_parent_parity": parent_parities[d],
        "boundary_child_parity": child_parities[d],
        "boundary_pair": f"{'O' if parent_parities[d] else 'E'}->{'O' if child_parities[d] else 'E'}",
        "parities_shared_before_depth": parent_parities[:d] == child_parities[:d],
        "affine_lift_law_holds_to_depth": not affine_failures,
        "affine_failures": affine_failures,
        "parent_state_at_depth": parent_states[d],
        "child_state_at_depth": child_states[d],
        "delta_at_depth": child_states[d] - parent_states[d],
        "predicted_delta_at_depth": 3 ** child_odd_prefix[d],
        "parent_odd_count_at_depth": parent_odd_prefix[d],
        "child_odd_count_at_depth": child_odd_prefix[d],
        "parent_odd_count_at_pressure": parent_odd_prefix[pressure_step],
        "child_odd_count_at_pressure": child_odd_prefix[pressure_step],
        "parent_required_at_pressure_step": parent_required_rows[pressure_step]["required"],
        "child_required_at_pressure_step": child_required_rows[pressure_step]["required"],
        "parent_excess_at_pressure_step": parent_required_rows[pressure_step]["excess"],
        "child_excess_at_pressure_step": child_required_rows[pressure_step]["excess"],
        "pressure_excess_gap_child_minus_parent": round_float(pressure_excess_gap, 9),
        "pressure_last_step_is_depth_step": pressure_step - 1 == d,
        "pressure_last_step_parity": child_parities[pressure_step - 1],
        "parent_entry_state": parent_states[entry_step],
        "child_entry_state": child_states[entry_step],
        "entry_delta": entry_delta,
        "entry_delta_power": entry_delta_power,
        "entry_delta_odd_factor": entry_delta_odd_factor,
        "child_odd_count_at_entry": child_odd_prefix[entry_step],
        "predicted_entry_delta": (3 ** child_odd_prefix[entry_step]) * (1 << entry_delta_power),
        "parent_entry_mod_16": parent_states[entry_step] % 16,
        "child_entry_mod_16": child_states[entry_step] % 16,
        "entry_delta_mod_16": entry_delta % 16,
        "child_entry_align": v2(child_states[entry_step] + 1),
        "q": q,
        "q_mod_16": q % 16,
        "terminal": terminal,
        "terminal_matches_record": terminal == int(record["terminal"]),
        "terminal_mod_16": terminal % 16,
        "active_expected_pressure": active_expected,
        "post_expected_pressure": post_expected,
        "formula_matches_pressure_state": (
            active_expected == int(record["state"])
            if str(record["post_word"]) == ""
            else post_expected == int(record["state"])
        ),
        "pressure_state": int(record["state"]),
        "post_word": record["post_word"] if record["post_word"] else "<active>",
    }


def run(args: argparse.Namespace) -> dict[str, object]:
    payload = json.loads(args.input.read_text(encoding="utf-8"))
    records = [analyze_record(dict(record)) for record in payload["records"]]

    counters: dict[str, Counter[str]] = {
        "regime_counts": Counter(str(record["regime"]) for record in records),
        "local_word_counts": Counter(str(record["local_word_entry_to_pressure"]) for record in records),
        "entry_offset_counts": Counter(str(record["entry_offset_from_depth"]) for record in records),
        "terminal_offset_counts": Counter(str(record["terminal_offset_from_depth"]) for record in records),
        "boundary_pair_counts": Counter(str(record["boundary_pair"]) for record in records),
        "entry_delta_power_counts": Counter(str(record["entry_delta_power"]) for record in records),
        "parent_entry_mod_16_counts": Counter(str(record["parent_entry_mod_16"]) for record in records),
        "child_entry_mod_16_counts": Counter(str(record["child_entry_mod_16"]) for record in records),
        "q_mod_16_counts": Counter(str(record["q_mod_16"]) for record in records),
        "post_word_counts": Counter(str(record["post_word"]) for record in records),
    }

    checks = {
        "record_count": len(records),
        "all_affine_lift_law_holds_to_depth": all(bool(record["affine_lift_law_holds_to_depth"]) for record in records),
        "all_parities_shared_before_depth": all(bool(record["parities_shared_before_depth"]) for record in records),
        "all_boundary_parent_even_child_odd": all(str(record["boundary_pair"]) == "E->O" for record in records),
        "all_pressure_at_depth_plus_one": all(int(record["pressure_offset_from_depth"]) == 1 for record in records),
        "all_pressure_last_step_is_depth_step": all(bool(record["pressure_last_step_is_depth_step"]) for record in records),
        "all_pressure_last_steps_are_odd": all(int(record["pressure_last_step_parity"]) == 1 for record in records),
        "all_child_excess_gap_at_pressure_is_one": all(
            float(record["pressure_excess_gap_child_minus_parent"]) == 1.0 for record in records
        ),
        "all_child_entry_align_three": all(int(record["child_entry_align"]) == 3 for record in records),
        "all_child_entries_are_7_mod_16": all(int(record["child_entry_mod_16"]) == 7 for record in records),
        "all_entry_delta_matches_lift_formula": all(
            int(record["entry_delta"]) == int(record["predicted_entry_delta"]) for record in records
        ),
        "all_terminal_formulas_match": all(bool(record["terminal_matches_record"]) for record in records),
        "all_pressure_formulas_match": all(bool(record["formula_matches_pressure_state"]) for record in records),
        "all_local_words_known": all(
            str(record["local_word_entry_to_pressure"]) in ("OOO", "OOOEOO") for record in records
        ),
    }

    return {
        "status": "branch-prefix-retimed-tight-lift-algebra",
        "parameters": {
            "input": str(args.input),
            "output": str(args.output) if args.output else None,
        },
        "checks": checks,
        "counts": {key: as_counter_dict(counter) for key, counter in counters.items()},
        "records": records,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    if not args.input.exists():
        raise SystemExit(f"missing input JSON: {args.input}")

    payload = run(args)
    text = json.dumps(payload, indent=2, sort_keys=True)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text + "\n", encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()

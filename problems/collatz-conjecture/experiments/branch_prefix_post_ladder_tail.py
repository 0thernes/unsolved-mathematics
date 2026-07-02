#!/usr/bin/env python3
"""Analyze the post-ladder tail in retimed pressure units.

The pressure-unit classifier found 340 high-ladder pressure units that occur
after the active ladder window, all with lag_minus_align = 3.  This script
reconstructs the high-ladder terminal state and the three following shortcut
steps for those tail units.
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path
from time import perf_counter

sys.path.insert(0, str(Path(__file__).resolve().parent))

from branch_potential_analyzer import enumerate_frontier, powers_of_three, round_float, shortcut_step, v2
from branch_prefix_dominance_analyzer import analyze_prefix_start
from branch_prefix_pressure_unit_classifier import unit_regime
from branch_prefix_retimed_pressure import pressure_trace, transition_row


MODULI = (8, 16, 32, 64, 128, 256, 512, 1024, 4096, 65536)


def dict_counter(counter: Counter[object]) -> dict[str, int]:
    return dict(sorted((str(key), int(value)) for key, value in counter.items()))


def bounded_counter(counter: Counter[object], limit: int) -> dict[str, int]:
    return dict(sorted((str(key), int(value)) for key, value in counter.most_common(limit)))


def parity_word(parities: list[int]) -> str:
    return "".join("O" if parity else "E" for parity in parities)


def residue_summaries(counters: dict[str, Counter[int]], limit: int) -> dict[str, object]:
    return {
        key: {
            "occupied": len(counter),
            "top": bounded_counter(counter, limit),
        }
        for key, counter in sorted(counters.items())
    }


def add_residues(counters: dict[str, Counter[int]], prefix: str, value: int) -> None:
    for modulus in MODULI:
        counters[f"{prefix}_mod_{modulus}"][value % modulus] += 1


def reconstruct_tail(last_credit_state: int, align: int) -> dict[str, object]:
    q = (last_credit_state + 1) >> align
    current = last_credit_state
    ladder_parities: list[int] = []
    for _ in range(align):
        current, parity = shortcut_step(current)
        ladder_parities.append(parity)

    terminal = current
    formula_terminal = (3**align) * q - 1
    post_steps = []
    post_parities: list[int] = []
    for index in range(1, 4):
        before = current
        current, parity = shortcut_step(current)
        post_parities.append(parity)
        post_steps.append(
            {
                "index": index,
                "before": before,
                "before_mod_64": before % 64,
                "before_v2": v2(before) if before else None,
                "parity": parity,
                "after": current,
                "after_mod_64": current % 64,
                "after_v2": v2(current) if current else None,
            }
        )

    return {
        "q": q,
        "q_mod_64": q % 64,
        "ladder_parity_word": parity_word(ladder_parities),
        "ladder_terminal": terminal,
        "formula_terminal": formula_terminal,
        "terminal_formula_ok": terminal == formula_terminal,
        "terminal_v2": v2(terminal),
        "terminal_mod_64": terminal % 64,
        "post_parity_word": parity_word(post_parities),
        "post_steps": post_steps,
        "after_three_steps": current,
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
    retimed_transition_count = 0
    pressure_unit_count = 0
    tail_units: list[dict[str, object]] = []
    non_tail_units = 0
    reconstruction_failures: list[dict[str, object]] = []

    child_residue_counts: dict[str, Counter[int]] = {f"child_mod_{m}": Counter() for m in MODULI}
    last_state_residue_counts: dict[str, Counter[int]] = {f"last_credit_state_mod_{m}": Counter() for m in MODULI}
    terminal_residue_counts: dict[str, Counter[int]] = {f"terminal_mod_{m}": Counter() for m in MODULI}
    pressure_state_residue_counts: dict[str, Counter[int]] = {f"pressure_state_mod_{m}": Counter() for m in MODULI}
    q_residue_counts: dict[str, Counter[int]] = {f"q_mod_{m}": Counter() for m in MODULI}

    align_hist: Counter[int] = Counter()
    terminal_v2_hist: Counter[int] = Counter()
    post_word_hist: Counter[str] = Counter()
    pressure_event_index_hist: Counter[int] = Counter()
    parent_required_hist: Counter[int] = Counter()
    required_above_hist: Counter[int] = Counter()
    surplus_hist: Counter[int] = Counter()
    step_offset_hist: Counter[int] = Counter()
    terminal_step1_residue_pairs: Counter[str] = Counter()
    terminal_step2_residue_pairs: Counter[str] = Counter()
    terminal_step3_residue_pairs: Counter[str] = Counter()

    examples: list[dict[str, object]] = []
    tightest_tail_units: list[dict[str, object]] = []

    def keep_tight(record: dict[str, object]) -> None:
        tightest_tail_units.append(record)
        tightest_tail_units.sort(
            key=lambda row: (
                int(row["surplus"]),
                -int(row["required_above_parent"]),
                int(row["child"]),
                int(row["step"]),
            )
        )
        del tightest_tail_units[args.top_n :]

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
            trace = pressure_trace(child, parent_required, args.max_steps)
            pressure_units = [
                dict(event)
                for event in trace["pressure_events"]
                if int(dict(event)["required"]) > parent_required
            ]

            for event_index, event in enumerate(pressure_units, start=1):
                pressure_unit_count += 1
                if unit_regime(event) != "high_after_ladder_window":
                    non_tail_units += 1
                    continue

                last = dict(event["last_credit_event"])
                align = int(last["align"])
                last_credit_state = int(last["state"])
                reconstructed = reconstruct_tail(last_credit_state, align)
                expected_lag = align + 3
                actual_lag = int(event["step"]) - int(last["step"])
                record = {
                    "parent": parent,
                    "child": child,
                    "child_bit": child_bit,
                    "event_index": event_index,
                    "step": event["step"],
                    "step_offset_from_parent_depth": int(event["step"]) - parent_depth,
                    "pressure_event": event["event"],
                    "pressure_state": event["state"],
                    "parent_required": parent_required,
                    "required": event["required"],
                    "required_above_parent": int(event["required"]) - parent_required,
                    "credit": event["credit"],
                    "surplus": int(event["credit"]) - int(event["required"]),
                    "last_credit_step": last["step"],
                    "last_credit_state": last_credit_state,
                    "align": align,
                    "lag": actual_lag,
                    "lag_minus_align": actual_lag - align,
                    "expected_lag": expected_lag,
                    "lag_formula_ok": actual_lag == expected_lag,
                    "after_three_matches_pressure_state": reconstructed["after_three_steps"] == int(event["state"]),
                    **{
                        key: value
                        for key, value in reconstructed.items()
                        if key not in {"post_steps"}
                    },
                    "post_steps": reconstructed["post_steps"],
                    "required_delta": transition["required_delta"],
                    "credit_delta": transition["credit_delta"],
                    "child_required": transition["child_required"],
                    "child_credit": transition["child_credit"],
                }
                tail_units.append(record)
                keep_tight(record)

                if len(examples) < args.top_n:
                    examples.append(record)
                if not bool(record["terminal_formula_ok"]) or not bool(record["lag_formula_ok"]) or not bool(record["after_three_matches_pressure_state"]):
                    reconstruction_failures.append(record)

                add_residues(child_residue_counts, "child", child)
                add_residues(last_state_residue_counts, "last_credit_state", last_credit_state)
                add_residues(terminal_residue_counts, "terminal", int(reconstructed["ladder_terminal"]))
                add_residues(pressure_state_residue_counts, "pressure_state", int(event["state"]))
                add_residues(q_residue_counts, "q", int(reconstructed["q"]))

                align_hist[align] += 1
                terminal_v2_hist[int(reconstructed["terminal_v2"])] += 1
                post_word_hist[str(reconstructed["post_parity_word"])] += 1
                pressure_event_index_hist[event_index] += 1
                parent_required_hist[parent_required] += 1
                required_above_hist[int(event["required"]) - parent_required] += 1
                surplus_hist[int(event["credit"]) - int(event["required"])] += 1
                step_offset_hist[int(event["step"]) - parent_depth] += 1
                steps = list(reconstructed["post_steps"])
                terminal_step1_residue_pairs[f"{steps[0]['before_mod_64']}->{steps[0]['after_mod_64']}"] += 1
                terminal_step2_residue_pairs[f"{steps[1]['before_mod_64']}->{steps[1]['after_mod_64']}"] += 1
                terminal_step3_residue_pairs[f"{steps[2]['before_mod_64']}->{steps[2]['after_mod_64']}"] += 1

    pure_claims = {
        "all_tail_units_lag_align_plus_3": all(bool(row["lag_formula_ok"]) for row in tail_units),
        "all_tail_units_formula_terminal": all(bool(row["terminal_formula_ok"]) for row in tail_units),
        "all_tail_units_three_step_reconstruction": all(bool(row["after_three_matches_pressure_state"]) for row in tail_units),
        "single_post_parity_word": len(post_word_hist) == 1,
        "single_terminal_v2": len(terminal_v2_hist) == 1,
        "all_tail_units_positive_surplus": all(int(row["surplus"]) > 0 for row in tail_units),
    }

    return {
        "status": "branch-prefix-post-ladder-tail",
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
        "retimed_transition_count": retimed_transition_count,
        "pressure_unit_count": pressure_unit_count,
        "post_ladder_tail_unit_count": len(tail_units),
        "non_tail_pressure_unit_count": non_tail_units,
        "reconstruction_failure_count": len(reconstruction_failures),
        "pure_claims": pure_claims,
        "align_histogram": dict_counter(align_hist),
        "terminal_v2_histogram": dict_counter(terminal_v2_hist),
        "post_parity_word_histogram": dict_counter(post_word_hist),
        "pressure_event_index_histogram": dict_counter(pressure_event_index_hist),
        "parent_required_histogram": dict_counter(parent_required_hist),
        "required_above_parent_histogram": dict_counter(required_above_hist),
        "surplus_histogram": dict_counter(surplus_hist),
        "step_offset_histogram": dict_counter(step_offset_hist),
        "terminal_step1_mod64_pairs": dict_counter(terminal_step1_residue_pairs),
        "terminal_step2_mod64_pairs": dict_counter(terminal_step2_residue_pairs),
        "terminal_step3_mod64_pairs": dict_counter(terminal_step3_residue_pairs),
        "residue_summary": {
            **residue_summaries(child_residue_counts, args.residue_top_n),
            **residue_summaries(last_state_residue_counts, args.residue_top_n),
            **residue_summaries(terminal_residue_counts, args.residue_top_n),
            **residue_summaries(pressure_state_residue_counts, args.residue_top_n),
            **residue_summaries(q_residue_counts, args.residue_top_n),
        },
        "tightest_tail_units": tightest_tail_units,
        "examples": examples,
        "reconstruction_failures": reconstruction_failures[: args.top_n],
        "interpretation": (
            "Finite post-ladder tail analyzer.  A clean parity-word and "
            "terminal-valuation pattern would turn the lag_minus_align=3 "
            "observation into a sharper carry sublemma."
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

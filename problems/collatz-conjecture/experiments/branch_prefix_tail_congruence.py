#!/usr/bin/env python3
"""Mine congruence laws behind post-ladder tail pressure.

The post-ladder tail audit reduced the tail carry to the congruence
`3^a q - 1 == 6 mod 16`.  This companion compares that congruence against all
high-ladder pressure units in the retimed hard class and checks the equivalent
cofactor rule for the tail:

    q == 7 * (3^a)^(-1) mod 16.
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
from branch_prefix_post_ladder_tail import reconstruct_tail
from branch_prefix_pressure_unit_classifier import unit_regime
from branch_prefix_retimed_pressure import pressure_trace, transition_row


EXPECTED_Q_MOD16_FOR_TERMINAL6 = {
    0: 7,
    1: 13,
    2: 15,
    3: 5,
}


def dict_counter(counter: Counter[object]) -> dict[str, int]:
    return dict(sorted((str(key), int(value)) for key, value in counter.items()))


def expected_q_mod16(align: int) -> int:
    return EXPECTED_Q_MOD16_FOR_TERMINAL6[align % 4]


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
    high_ladder_pressure_unit_count = 0
    tail_unit_count = 0

    regime_counts: Counter[str] = Counter()
    terminal_mod16_by_regime: Counter[str] = Counter()
    terminal6_by_regime: Counter[str] = Counter()
    q_mod16_by_regime: Counter[str] = Counter()
    q_rule_by_align_mod4: Counter[str] = Counter()
    align_mod4_by_regime: Counter[str] = Counter()
    tail_q_rule_hist: Counter[str] = Counter()
    tail_child_mod16: Counter[int] = Counter()
    tail_last_state_mod16: Counter[int] = Counter()
    tail_terminal_mod64: Counter[int] = Counter()
    non_tail_terminal6_examples: list[dict[str, object]] = []
    tail_q_rule_failures: list[dict[str, object]] = []
    tail_terminal6_failures: list[dict[str, object]] = []

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
                last = event.get("last_credit_event")
                if last is None or str(dict(last)["kind"]) != "high_ladder":
                    continue

                high_ladder_pressure_unit_count += 1
                last_event = dict(last)
                align = int(last_event["align"])
                last_credit_state = int(last_event["state"])
                reconstructed = reconstruct_tail(last_credit_state, align)
                regime = unit_regime(event)
                terminal_mod16 = int(reconstructed["ladder_terminal"]) % 16
                q_mod16 = int(reconstructed["q"]) % 16
                expected_q = expected_q_mod16(align)
                record = {
                    "parent": parent,
                    "child": child,
                    "child_bit": child_bit,
                    "event_index": event_index,
                    "event": event["event"],
                    "regime": regime,
                    "step": event["step"],
                    "last_credit_step": last_event["step"],
                    "last_credit_state": last_credit_state,
                    "align": align,
                    "align_mod4": align % 4,
                    "q": reconstructed["q"],
                    "q_mod16": q_mod16,
                    "expected_q_mod16_for_terminal6": expected_q,
                    "terminal_mod16": terminal_mod16,
                    "terminal_mod64": reconstructed["ladder_terminal"] % 64,
                    "terminal_v2": reconstructed["terminal_v2"],
                    "post_parity_word": reconstructed["post_parity_word"],
                    "parent_required": parent_required,
                    "required": event["required"],
                    "required_above_parent": int(event["required"]) - parent_required,
                    "credit": event["credit"],
                    "surplus": int(event["credit"]) - int(event["required"]),
                    "required_delta": transition["required_delta"],
                    "credit_delta": transition["credit_delta"],
                }

                regime_counts[regime] += 1
                terminal_mod16_by_regime[f"{regime}:{terminal_mod16}"] += 1
                q_mod16_by_regime[f"{regime}:{q_mod16}"] += 1
                align_mod4_by_regime[f"{regime}:{align % 4}"] += 1
                q_rule_by_align_mod4[f"{align % 4}:{q_mod16}"] += 1
                if terminal_mod16 == 6:
                    terminal6_by_regime[regime] += 1
                    if regime != "high_after_ladder_window" and len(non_tail_terminal6_examples) < args.top_n:
                        non_tail_terminal6_examples.append(record)

                if regime != "high_after_ladder_window":
                    continue

                tail_unit_count += 1
                tail_q_rule_hist[f"a_mod4={align % 4}:q_mod16={q_mod16}:expected={expected_q}"] += 1
                tail_child_mod16[child % 16] += 1
                tail_last_state_mod16[last_credit_state % 16] += 1
                tail_terminal_mod64[int(reconstructed["ladder_terminal"]) % 64] += 1
                if terminal_mod16 != 6:
                    tail_terminal6_failures.append(record)
                if q_mod16 != expected_q:
                    tail_q_rule_failures.append(record)

    pure_claims = {
        "all_tail_units_terminal_mod16_is_6": not tail_terminal6_failures,
        "all_tail_units_match_q_mod16_rule": not tail_q_rule_failures,
        "terminal6_is_unique_to_tail": sum(terminal6_by_regime.values()) == tail_unit_count,
    }

    return {
        "status": "branch-prefix-tail-congruence",
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
        "high_ladder_pressure_unit_count": high_ladder_pressure_unit_count,
        "tail_unit_count": tail_unit_count,
        "pure_claims": pure_claims,
        "expected_q_mod16_for_terminal6_by_align_mod4": {
            str(key): value for key, value in EXPECTED_Q_MOD16_FOR_TERMINAL6.items()
        },
        "regime_counts": dict_counter(regime_counts),
        "terminal_mod16_by_regime": dict_counter(terminal_mod16_by_regime),
        "terminal6_by_regime": dict_counter(terminal6_by_regime),
        "q_mod16_by_regime": dict_counter(q_mod16_by_regime),
        "q_rule_by_align_mod4": dict_counter(q_rule_by_align_mod4),
        "align_mod4_by_regime": dict_counter(align_mod4_by_regime),
        "tail_q_rule_histogram": dict_counter(tail_q_rule_hist),
        "tail_child_mod16": dict_counter(tail_child_mod16),
        "tail_last_credit_state_mod16": dict_counter(tail_last_state_mod16),
        "tail_terminal_mod64": dict_counter(tail_terminal_mod64),
        "non_tail_terminal6_examples": non_tail_terminal6_examples,
        "tail_terminal6_failures": tail_terminal6_failures[: args.top_n],
        "tail_q_rule_failures": tail_q_rule_failures[: args.top_n],
        "interpretation": (
            "Finite congruence audit.  The q-mod-16 rule is equivalent to "
            "3^a q - 1 == 6 mod 16; terminal6_is_unique_to_tail says whether "
            "that congruence characterizes the post-ladder tail among high "
            "pressure units or only describes it."
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

#!/usr/bin/env python3
"""Audit the ghost full-lift class in post-ladder tail pressure units.

`branch_prefix_tail_memory_lift_solver.py` found one unobserved local ghost:

    EEOEOOOO, source == 1956 mod 16384, terminal == 6 mod 64.

This script checks the full terminal-6 post-ladder tail population.  It
distinguishes the terminal signature of the ghost bit from the stronger memory
signature in which the terminal max is sourced eight shortcut steps earlier by
the word EEOEOOOO.
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
from branch_prefix_post_ladder_tail import parity_word, reconstruct_tail
from branch_prefix_pressure_unit_classifier import unit_regime
from branch_prefix_retimed_pressure import transition_row
from branch_prefix_tail_memory_cases import shortcut_segment
from branch_prefix_tail_memory_lift_solver import BRIDGE_EXTRA_BITS, FULL_EXTRA_BITS
from branch_prefix_tail_memory_word_maps import WORDS
from branch_prefix_tail_phase import dec_string, detailed_trace, required_lower_edge
from branch_prefix_tail_phase_spectrum import max_source_before, observation_by_step_state


GHOST_WORD = "EEOEOOOO"
GHOST_SOURCE_MOD_16384 = 1956
GHOST_BRIDGE_MOD_8192 = 1956
GHOST_ALIGN = 4
GHOST_Q_MOD64 = 23
GHOST_TERMINAL_MOD64 = 6


def dict_counter(counter: Counter[object]) -> dict[str, int]:
    return dict(sorted((str(key), int(value)) for key, value in counter.items()))


def serial_decimal(value: Decimal) -> str:
    return dec_string(value, 30)


def source_word_if_small(source_state: int, lag: int) -> dict[str, object]:
    if lag <= 0 or lag > 16:
        return {"word": None, "states_mod64": None}
    segment = shortcut_segment(source_state, lag)
    return {
        "word": segment["parity_word"],
        "states_mod64": segment["states_mod_64"],
    }


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
    post_ladder_tail_count = 0
    terminal_signature_count = 0
    ghost_memory_source_count = 0

    source_lag_hist: Counter[int] = Counter()
    source_word_hist: Counter[str] = Counter()
    source_mod8192_by_word: Counter[str] = Counter()
    source_mod16384_by_word: Counter[str] = Counter()
    terminal_signature_by_lag: Counter[str] = Counter()
    q_mod64_by_align_terminal: Counter[str] = Counter()
    terminal_mod64_by_source_lag: Counter[str] = Counter()
    gap_by_source_lag: Counter[str] = Counter()
    source_event_by_lag: Counter[str] = Counter()
    post_word_hist: Counter[str] = Counter()

    terminal_signature_records: list[dict[str, object]] = []
    ghost_memory_records: list[dict[str, object]] = []
    memory_records: list[dict[str, object]] = []
    source_misses: list[dict[str, object]] = []

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

                post_ladder_tail_count += 1
                terminal_step = int(last_event["step"]) + align
                terminal_observation = observation_by_step_state(observations, terminal_step, terminal)
                if terminal_observation is None:
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
                    source_misses.append(
                        {
                            "parent": parent,
                            "child": child,
                            "event_index": event_index,
                            "reason": "missing max source",
                        }
                    )
                    continue

                source_state = int(source["state"])
                source_lag = terminal_step - int(source["step"])
                source_info = source_word_if_small(source_state, source_lag)
                source_word = source_info["word"]
                threshold = required_lower_edge(int(event["required"]))
                gap = threshold - terminal_max
                terminal_current_gap = threshold - Decimal(terminal_observation["current_excess"])
                q_mod64 = int(reconstructed["q_mod_64"])
                terminal_mod64 = terminal % 64
                source_mod8192 = source_state % (1 << (8 + BRIDGE_EXTRA_BITS))
                source_mod16384 = source_state % (1 << (8 + FULL_EXTRA_BITS))
                post_word = str(reconstructed["post_parity_word"])

                source_lag_hist[source_lag] += 1
                terminal_mod64_by_source_lag[f"lag={source_lag};terminal={terminal_mod64}"] += 1
                gap_by_source_lag[f"lag={source_lag};gap={dec_string(gap, 24)}"] += 1
                source_event_by_lag[f"lag={source_lag};event={source['event']}"] += 1
                q_mod64_by_align_terminal[f"a={align};q={q_mod64};terminal={terminal_mod64}"] += 1
                if source_word is not None:
                    source_word_hist[str(source_word)] += 1
                    source_mod8192_by_word[f"{source_word}:{source_mod8192}"] += 1
                    source_mod16384_by_word[f"{source_word}:{source_mod16384}"] += 1
                post_word_hist[post_word] += 1

                terminal_signature = (
                    align == GHOST_ALIGN
                    and q_mod64 == GHOST_Q_MOD64
                    and terminal_mod64 == GHOST_TERMINAL_MOD64
                )
                if terminal_signature:
                    terminal_signature_count += 1
                    terminal_signature_by_lag[f"lag={source_lag};word={source_word}"] += 1

                ghost_memory_source = (
                    source_lag == 8
                    and source_word == GHOST_WORD
                    and source_mod16384 == GHOST_SOURCE_MOD_16384
                )
                if ghost_memory_source:
                    ghost_memory_source_count += 1

                record = {
                    "parent": parent,
                    "child": child,
                    "child_bit": child_bit,
                    "event_index": event_index,
                    "event_step": int(event["step"]),
                    "event_required": int(event["required"]),
                    "last_credit_step": int(last_event["step"]),
                    "last_credit_state": last_credit_state,
                    "align": align,
                    "q_mod64": q_mod64,
                    "terminal_step": terminal_step,
                    "terminal": terminal,
                    "terminal_mod64": terminal_mod64,
                    "source_step": int(source["step"]),
                    "source_state": source_state,
                    "source_lag_to_terminal": source_lag,
                    "source_event": source["event"],
                    "source_word": source_word,
                    "source_states_mod64": source_info["states_mod64"],
                    "source_mod8192": source_mod8192,
                    "source_mod16384": source_mod16384,
                    "post_parity_word": post_word,
                    "gap": serial_decimal(gap),
                    "terminal_current_gap": serial_decimal(terminal_current_gap),
                    "terminal_signature": terminal_signature,
                    "ghost_memory_source": ghost_memory_source,
                    "transition_required_delta": transition["required_delta"],
                    "transition_credit_delta": transition["credit_delta"],
                }

                if source_lag != 0 and len(memory_records) < args.top_n:
                    memory_records.append(record)
                if terminal_signature and len(terminal_signature_records) < args.top_n:
                    terminal_signature_records.append(record)
                if ghost_memory_source and len(ghost_memory_records) < args.top_n:
                    ghost_memory_records.append(record)

    pure_claims = {
        "all_sources_found": not source_misses,
        "terminal_signature_occurs": terminal_signature_count > 0,
        "ghost_memory_source_absent": ghost_memory_source_count == 0,
        "all_nonterminal_sources_are_known_memory_words": all(
            key in WORDS for key in source_word_hist if key != "None"
        ),
        "all_nonterminal_sources_have_lag_8": all(int(key) in (0, 8) for key in source_lag_hist),
        "all_post_ladder_tail_words_are_eoo": dict(post_word_hist) == {"EOO": post_ladder_tail_count},
    }

    return {
        "status": "branch-prefix-tail-ghost-class",
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
        "post_ladder_tail_count": post_ladder_tail_count,
        "terminal_signature_count": terminal_signature_count,
        "ghost_memory_source_count": ghost_memory_source_count,
        "pure_claims": pure_claims,
        "source_lag_histogram": dict_counter(source_lag_hist),
        "source_word_histogram": dict_counter(source_word_hist),
        "source_mod8192_by_word": dict_counter(source_mod8192_by_word),
        "source_mod16384_by_word": dict_counter(source_mod16384_by_word),
        "terminal_signature_by_lag": dict_counter(terminal_signature_by_lag),
        "q_mod64_by_align_terminal_top": dict(
            sorted(q_mod64_by_align_terminal.items(), key=lambda item: (-item[1], item[0]))[: args.hist_top_n]
        ),
        "terminal_mod64_by_source_lag": dict_counter(terminal_mod64_by_source_lag),
        "gap_by_source_lag": dict_counter(gap_by_source_lag),
        "source_event_by_lag": dict_counter(source_event_by_lag),
        "post_word_histogram": dict_counter(post_word_hist),
        "memory_record_examples": memory_records,
        "terminal_signature_examples": terminal_signature_records,
        "ghost_memory_examples": ghost_memory_records,
        "source_misses": source_misses[: args.top_n],
        "interpretation": (
            "Ghost audit over all post-ladder tail units. If the terminal "
            "signature occurs but ghost_memory_source_count is zero, then the "
            "unobserved full lift is not a memory-tail source in this exact "
            "lift; it is absorbed by terminal-local phase accounting here."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--parent-depth", type=int, default=25)
    parser.add_argument("--max-depth", type=int, default=1024)
    parser.add_argument("--max-steps", type=int, default=50000)
    parser.add_argument("--precision", type=int, default=80)
    parser.add_argument("--top-n", type=int, default=12)
    parser.add_argument("--hist-top-n", type=int, default=32)
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

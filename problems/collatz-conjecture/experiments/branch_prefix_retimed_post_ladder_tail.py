#!/usr/bin/env python3
"""Analyze the three-step post-ladder tail in retimed first thresholds.

The first-threshold sweep shows that every post-ladder first threshold occurs
with ``lag_minus_align = 3``. This script reconstructs the preceding high
ladder and records the exact three shortcut parities after the ladder terminal.

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

from branch_potential_analyzer import (
    enumerate_frontier,
    powers_of_three,
    round_float,
    shortcut_step,
    v2,
)
from branch_prefix_dominance_analyzer import analyze_prefix_start
from branch_prefix_retimed_pressure import pressure_trace, transition_row
from branch_prefix_retimed_signature import classify_pressure_unit


DEFAULT_RESIDUE_MODULI = (16, 32, 64, 128, 256, 512, 1024, 4096, 65536)


def as_counter_dict(counter: Counter[object]) -> dict[str, int]:
    return dict(sorted((str(key), int(value)) for key, value in counter.items()))


def residue_purity_summary(
    *,
    total: Counter[int],
    positive: Counter[int],
    top_n: int,
) -> dict[str, object]:
    pure_positive = []
    pure_negative = []
    mixed = []
    for residue, total_count in total.items():
        positive_count = int(positive.get(residue, 0))
        if positive_count == total_count:
            pure_positive.append((residue, total_count))
        elif positive_count == 0:
            pure_negative.append((residue, total_count))
        else:
            mixed.append((residue, total_count, positive_count))

    positive_total = sum(positive.values())
    pure_positive_total = sum(count for _, count in pure_positive)
    mixed_positive_total = sum(pos for _, _, pos in mixed)
    return {
        "occupied_buckets": len(total),
        "post_ladder_buckets": len(positive),
        "pure_post_ladder_buckets": len(pure_positive),
        "pure_non_post_ladder_buckets": len(pure_negative),
        "mixed_buckets": len(mixed),
        "post_ladder_total": positive_total,
        "post_ladder_in_pure_buckets": pure_positive_total,
        "post_ladder_in_mixed_buckets": mixed_positive_total,
        "post_ladder_pure_bucket_fraction": (
            round_float(pure_positive_total / positive_total) if positive_total else 1.0
        ),
        "top_pure_post_ladder_buckets": {
            str(residue): int(count)
            for residue, count in sorted(pure_positive, key=lambda item: item[1], reverse=True)[:top_n]
        },
        "top_mixed_buckets": {
            str(residue): {
                "total": int(total_count),
                "post_ladder": int(positive_count),
                "post_ladder_fraction": round_float(positive_count / total_count),
            }
            for residue, total_count, positive_count in sorted(
                mixed,
                key=lambda item: (item[2], item[2] / item[1], item[0]),
                reverse=True,
            )[:top_n]
        },
    }


def simulate_steps(start: int, count: int) -> tuple[int, list[int]]:
    current = start
    parities: list[int] = []
    for _ in range(count):
        current, parity = shortcut_step(current)
        parities.append(parity)
    return current, parities


def parity_word(parities: list[int]) -> str:
    return "".join("O" if parity else "E" for parity in parities)


def post3_formula_value(terminal: int, word: str) -> int | None:
    if word == "EEO":
        return (3 * terminal + 4) // 8
    if word == "EOO":
        return (9 * terminal + 10) // 8
    return None


def expected_q_mod16_for_terminal_6(align: int) -> int:
    return {
        0: 7,
        1: 13,
        2: 15,
        3: 5,
    }[align % 4]


def compact_record(
    *,
    parent: int,
    child: int,
    parent_depth: int,
    event: dict[str, object],
    transition: dict[str, object],
    entry: int,
    align: int,
    q: int,
    terminal: int,
    word: str,
    terminal_v2: int,
) -> dict[str, object]:
    last = dict(event["last_credit_event"])
    lag = int(event["step"]) - int(last["step"])
    return {
        "parent": parent,
        "child": child,
        "step": event["step"],
        "step_offset_from_parent_depth": int(event["step"]) - parent_depth,
        "state": event["state"],
        "parent_required": transition["parent_required"],
        "child_required": transition["child_required"],
        "required_delta": transition["required_delta"],
        "credit_delta": transition["credit_delta"],
        "required": event["required"],
        "required_above_parent": int(event["required"]) - int(transition["parent_required"]),
        "credit": event["credit"],
        "surplus": int(event["credit"]) - int(event["required"]),
        "entry": entry,
        "align": align,
        "align_mod_4": align % 4,
        "q": q,
        "q_mod_8": q % 8,
        "q_mod_16": q % 16,
        "expected_q_mod_16_for_terminal_6": expected_q_mod16_for_terminal_6(align),
        "q_phase_matches_terminal_6": q % 16 == expected_q_mod16_for_terminal_6(align),
        "terminal": terminal,
        "terminal_v2": terminal_v2,
        "terminal_mod_16": terminal % 16,
        "terminal_mod_32": terminal % 32,
        "terminal_mod_64": terminal % 64,
        "post_ladder_word": word,
        "lag": lag,
        "lag_minus_align": lag - align,
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

    positive_pressure_count = 0
    retimed_count = 0
    first_threshold_count = 0
    post_ladder_count = 0
    formula_failures: list[dict[str, object]] = []
    terminal_state_failures: list[dict[str, object]] = []
    lag_failures: list[dict[str, object]] = []
    word_terminal_v2_failures: list[dict[str, object]] = []
    q_phase_failures: list[dict[str, object]] = []
    word_counts: Counter[str] = Counter()
    terminal_v2_counts: Counter[int] = Counter()
    align_counts: Counter[int] = Counter()
    align_mod_4_counts: Counter[int] = Counter()
    q_mod_8_counts: Counter[int] = Counter()
    q_mod_16_counts: Counter[int] = Counter()
    q_phase_counts: Counter[str] = Counter()
    terminal_mod_16_counts: Counter[int] = Counter()
    terminal_mod_32_counts: Counter[int] = Counter()
    terminal_mod_64_counts: Counter[int] = Counter()
    surplus_counts: Counter[int] = Counter()
    step_offset_counts: Counter[int] = Counter()
    retimed_child_residue_counts = {modulus: Counter() for modulus in DEFAULT_RESIDUE_MODULI}
    post_ladder_child_residue_counts = {modulus: Counter() for modulus in DEFAULT_RESIDUE_MODULI}
    retimed_parent_residue_counts = {modulus: Counter() for modulus in DEFAULT_RESIDUE_MODULI}
    post_ladder_parent_residue_counts = {modulus: Counter() for modulus in DEFAULT_RESIDUE_MODULI}
    tightest: list[dict[str, object]] = []
    largest_offsets: list[dict[str, object]] = []
    examples_by_word: dict[str, list[dict[str, object]]] = {}

    def keep_smallest(records: list[dict[str, object]], record: dict[str, object], key: str) -> None:
        records.append(record)
        records.sort(key=lambda row: (int(row[key]), int(row["child"]), int(row["step"])))
        del records[args.top_n :]

    def keep_largest(records: list[dict[str, object]], record: dict[str, object], key: str) -> None:
        records.append(record)
        records.sort(key=lambda row: (int(row[key]), int(row["child"]), int(row["step"])), reverse=True)
        del records[args.top_n :]

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
            if int(transition["required_delta"]) > 0:
                positive_pressure_count += 1
            if not (
                int(transition["required_delta"]) > 0
                and int(transition["credit_delta"]) < int(transition["required_delta"])
            ):
                continue

            retimed_count += 1
            trace = pressure_trace(child, parent_required, args.max_steps)
            first = None
            for event in trace["pressure_events"]:
                candidate = dict(event)
                if int(candidate["required"]) > parent_required:
                    first = candidate
                    break
            if first is None:
                continue
            first_threshold_count += 1
            regime = classify_pressure_unit(first)
            for modulus in DEFAULT_RESIDUE_MODULI:
                retimed_child_residue_counts[modulus][child % modulus] += 1
                retimed_parent_residue_counts[modulus][parent % modulus] += 1
            if regime != "high_after_ladder_window":
                continue

            post_ladder_count += 1
            for modulus in DEFAULT_RESIDUE_MODULI:
                post_ladder_child_residue_counts[modulus][child % modulus] += 1
                post_ladder_parent_residue_counts[modulus][parent % modulus] += 1
            last = dict(first["last_credit_event"])
            entry = int(last["state"])
            align = int(last["align"])
            q = (entry + 1) >> align
            terminal_expected = (3**align) * q - 1
            terminal, ladder_parities = simulate_steps(entry, align)
            post_state, post_parities = simulate_steps(terminal, 3)
            word = parity_word(post_parities)
            terminal_v2 = v2(terminal)
            record = compact_record(
                parent=parent,
                child=child,
                parent_depth=parent_depth,
                event=first,
                transition=transition,
                entry=entry,
                align=align,
                q=q,
                terminal=terminal,
                word=word,
                terminal_v2=terminal_v2,
            )

            if ladder_parities != [1] * align or terminal != terminal_expected:
                formula_failures.append(record)
            if post_state != int(first["state"]):
                terminal_state_failures.append(record)
            if int(record["lag_minus_align"]) != 3:
                lag_failures.append(record)
            formula_value = post3_formula_value(terminal, word)
            if formula_value is None or formula_value != int(first["state"]):
                formula_failures.append({**record, "post3_formula_value": formula_value})
            if not (
                (word == "EEO" and terminal_v2 == 2)
                or (word == "EOO" and terminal_v2 == 1)
            ):
                word_terminal_v2_failures.append(record)
            if not bool(record["q_phase_matches_terminal_6"]):
                q_phase_failures.append(record)

            word_counts[word] += 1
            terminal_v2_counts[terminal_v2] += 1
            align_counts[align] += 1
            align_mod_4_counts[align % 4] += 1
            q_mod_8_counts[q % 8] += 1
            q_mod_16_counts[q % 16] += 1
            q_phase_counts[f"a{align % 4}:q{q % 16}"] += 1
            terminal_mod_16_counts[terminal % 16] += 1
            terminal_mod_32_counts[terminal % 32] += 1
            terminal_mod_64_counts[terminal % 64] += 1
            surplus_counts[int(record["surplus"])] += 1
            step_offset_counts[int(record["step_offset_from_parent_depth"])] += 1
            examples_by_word.setdefault(word, [])
            if len(examples_by_word[word]) < args.top_n:
                examples_by_word[word].append(record)
            keep_smallest(tightest, record, "surplus")
            keep_largest(largest_offsets, record, "step_offset_from_parent_depth")

    return {
        "status": "branch-prefix-retimed-post-ladder-tail",
        "elapsed_seconds": round_float(perf_counter() - started, 6),
        "parent_depth": parent_depth,
        "child_depth": child_depth,
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
        "first_threshold_count": first_threshold_count,
        "post_ladder_first_threshold_count": post_ladder_count,
        "post_ladder_word_counts": as_counter_dict(word_counts),
        "terminal_v2_counts": as_counter_dict(terminal_v2_counts),
        "align_counts": as_counter_dict(align_counts),
        "align_mod_4_counts": as_counter_dict(align_mod_4_counts),
        "q_mod_8_counts": as_counter_dict(q_mod_8_counts),
        "q_mod_16_counts": as_counter_dict(q_mod_16_counts),
        "q_align_mod16_phase_counts": as_counter_dict(q_phase_counts),
        "terminal_mod_16_counts": as_counter_dict(terminal_mod_16_counts),
        "terminal_mod_32_counts": as_counter_dict(terminal_mod_32_counts),
        "terminal_mod_64_counts": as_counter_dict(terminal_mod_64_counts),
        "surplus_histogram": as_counter_dict(surplus_counts),
        "step_offset_histogram": as_counter_dict(step_offset_counts),
        "retimed_child_residue_counts": {
            str(modulus): as_counter_dict(counter)
            for modulus, counter in retimed_child_residue_counts.items()
        },
        "post_ladder_child_residue_counts": {
            str(modulus): as_counter_dict(counter)
            for modulus, counter in post_ladder_child_residue_counts.items()
        },
        "retimed_parent_residue_counts": {
            str(modulus): as_counter_dict(counter)
            for modulus, counter in retimed_parent_residue_counts.items()
        },
        "post_ladder_parent_residue_counts": {
            str(modulus): as_counter_dict(counter)
            for modulus, counter in post_ladder_parent_residue_counts.items()
        },
        "post_ladder_child_residue_purity": {
            str(modulus): residue_purity_summary(
                total=retimed_child_residue_counts[modulus],
                positive=post_ladder_child_residue_counts[modulus],
                top_n=args.top_n,
            )
            for modulus in DEFAULT_RESIDUE_MODULI
        },
        "post_ladder_parent_residue_purity": {
            str(modulus): residue_purity_summary(
                total=retimed_parent_residue_counts[modulus],
                positive=post_ladder_parent_residue_counts[modulus],
                top_n=args.top_n,
            )
            for modulus in DEFAULT_RESIDUE_MODULI
        },
        "pure_feature_claims": {
            "all_post_ladder_tails_have_lag_minus_align_3": not lag_failures,
            "all_ladder_formulas_checked": not formula_failures,
            "all_post3_states_match_threshold_state": not terminal_state_failures,
            "all_post_ladder_words_are_EEO_or_EOO": set(word_counts).issubset({"EEO", "EOO"}),
            "all_post_ladder_words_are_EOO": set(word_counts).issubset({"EOO"}),
            "all_ladder_terminals_are_6_mod_16": set(terminal_mod_16_counts).issubset({6}),
            "all_ladder_terminals_have_v2_1": set(terminal_v2_counts).issubset({1}),
            "all_q_are_5_or_7_mod_8": set(q_mod_8_counts).issubset({5, 7}),
            "all_q_align_phases_force_terminal_6_mod_16": not q_phase_failures,
            "terminal_v2_matches_word": not word_terminal_v2_failures,
        },
        "tightest_post_ladder_thresholds": tightest,
        "largest_step_offsets": largest_offsets,
        "examples_by_word": examples_by_word,
        "formula_failures": formula_failures[: args.top_n],
        "terminal_state_failures": terminal_state_failures[: args.top_n],
        "lag_failures": lag_failures[: args.top_n],
        "word_terminal_v2_failures": word_terminal_v2_failures[: args.top_n],
        "q_phase_failures": q_phase_failures[: args.top_n],
    }


def load_or_run_depth(args: argparse.Namespace, parent_depth: int) -> tuple[dict[str, object], bool]:
    child_depth = parent_depth + 1
    cache = Path(args.cache_template.format(parent_depth=parent_depth, child_depth=child_depth))
    if args.use_cache and cache.exists() and not args.refresh:
        return json.loads(cache.read_text(encoding="utf-8")), True
    payload = analyze_depth(args, parent_depth)
    if args.write_depth_cache:
        cache.parent.mkdir(parents=True, exist_ok=True)
        cache.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return payload, False


def compact_depth(payload: dict[str, object], cached: bool) -> dict[str, object]:
    offsets = [int(key) for key in dict(payload["step_offset_histogram"])]
    word_keys = set(dict(payload["post_ladder_word_counts"]))
    terminal_mod_16_keys = {int(key) for key in dict(payload["terminal_mod_16_counts"])}
    terminal_v2_keys = {int(key) for key in dict(payload["terminal_v2_counts"])}
    q_mod_8_keys = {int(key) for key in dict(payload["q_mod_8_counts"])}
    q_phase_keys = set(dict(payload.get("q_align_mod16_phase_counts", {})))
    pure_feature_claims = dict(payload["pure_feature_claims"])
    pure_feature_claims.update(
        {
            "all_post_ladder_words_are_EOO": word_keys.issubset({"EOO"}),
            "all_ladder_terminals_are_6_mod_16": terminal_mod_16_keys.issubset({6}),
            "all_ladder_terminals_have_v2_1": terminal_v2_keys.issubset({1}),
            "all_q_are_5_or_7_mod_8": q_mod_8_keys.issubset({5, 7}),
            "all_q_align_phases_force_terminal_6_mod_16": q_phase_keys.issubset(
                {"a0:q7", "a1:q13", "a2:q15", "a3:q5"}
            ),
        }
    )
    return {
        "parent_depth": int(payload["parent_depth"]),
        "child_depth": int(payload["child_depth"]),
        "cached": cached,
        "retimed_transition_count": int(payload["retimed_transition_count"]),
        "first_threshold_count": int(payload["first_threshold_count"]),
        "post_ladder_first_threshold_count": int(payload["post_ladder_first_threshold_count"]),
        "post_ladder_word_counts": payload["post_ladder_word_counts"],
        "terminal_v2_counts": payload["terminal_v2_counts"],
        "align_counts": payload["align_counts"],
        "align_mod_4_counts": payload.get("align_mod_4_counts", {}),
        "q_mod_8_counts": payload["q_mod_8_counts"],
        "q_mod_16_counts": payload["q_mod_16_counts"],
        "q_align_mod16_phase_counts": payload.get("q_align_mod16_phase_counts", {}),
        "terminal_mod_16_counts": payload["terminal_mod_16_counts"],
        "terminal_mod_32_counts": payload["terminal_mod_32_counts"],
        "terminal_mod_64_counts": payload.get("terminal_mod_64_counts", {}),
        "post_ladder_child_residue_purity": payload.get("post_ladder_child_residue_purity", {}),
        "post_ladder_parent_residue_purity": payload.get("post_ladder_parent_residue_purity", {}),
        "step_offset_min": min(offsets) if offsets else None,
        "step_offset_max": max(offsets) if offsets else None,
        "pure_feature_claims": pure_feature_claims,
    }


def run(args: argparse.Namespace) -> dict[str, object]:
    rows = []
    combined_retimed_child_residues = {modulus: Counter() for modulus in DEFAULT_RESIDUE_MODULI}
    combined_post_ladder_child_residues = {modulus: Counter() for modulus in DEFAULT_RESIDUE_MODULI}
    combined_retimed_parent_residues = {modulus: Counter() for modulus in DEFAULT_RESIDUE_MODULI}
    combined_post_ladder_parent_residues = {modulus: Counter() for modulus in DEFAULT_RESIDUE_MODULI}
    for depth in range(args.min_parent_depth, args.max_parent_depth + 1):
        payload, cached = load_or_run_depth(args, depth)
        for modulus in DEFAULT_RESIDUE_MODULI:
            key = str(modulus)
            combined_retimed_child_residues[modulus].update(
                {int(residue): int(count) for residue, count in dict(payload["retimed_child_residue_counts"][key]).items()}
            )
            combined_post_ladder_child_residues[modulus].update(
                {int(residue): int(count) for residue, count in dict(payload["post_ladder_child_residue_counts"][key]).items()}
            )
            combined_retimed_parent_residues[modulus].update(
                {int(residue): int(count) for residue, count in dict(payload["retimed_parent_residue_counts"][key]).items()}
            )
            combined_post_ladder_parent_residues[modulus].update(
                {int(residue): int(count) for residue, count in dict(payload["post_ladder_parent_residue_counts"][key]).items()}
            )
        rows.append(compact_depth(payload, cached))

    combined_words: Counter[str] = Counter()
    combined_terminal_v2: Counter[str] = Counter()
    combined_q_mod_8: Counter[str] = Counter()
    combined_q_phase: Counter[str] = Counter()
    combined_terminal_mod_16: Counter[str] = Counter()
    combined_terminal_mod_64: Counter[str] = Counter()
    claim_names = sorted(
        {
            claim
            for row in rows
            for claim in dict(row["pure_feature_claims"])
        }
    )
    for row in rows:
        combined_words.update({key: int(value) for key, value in dict(row["post_ladder_word_counts"]).items()})
        combined_terminal_v2.update({key: int(value) for key, value in dict(row["terminal_v2_counts"]).items()})
        combined_q_mod_8.update({key: int(value) for key, value in dict(row["q_mod_8_counts"]).items()})
        combined_q_phase.update({key: int(value) for key, value in dict(row["q_align_mod16_phase_counts"]).items()})
        combined_terminal_mod_16.update({key: int(value) for key, value in dict(row["terminal_mod_16_counts"]).items()})
        combined_terminal_mod_64.update({key: int(value) for key, value in dict(row["terminal_mod_64_counts"]).items()})

    offsets = [
        int(value)
        for row in rows
        for value in (row["step_offset_min"], row["step_offset_max"])
        if value is not None
    ]

    return {
        "status": "branch-prefix-retimed-post-ladder-tail-sweep",
        "parameters": {
            "min_parent_depth": args.min_parent_depth,
            "max_parent_depth": args.max_parent_depth,
            "max_depth": args.max_depth,
            "max_steps": args.max_steps,
            "top_n": args.top_n,
            "use_cache": args.use_cache,
            "refresh": args.refresh,
            "write_depth_cache": args.write_depth_cache,
            "cache_template": args.cache_template,
        },
        "depths": rows,
        "checks": {
            "pure_feature_claims_all_depths": {
                claim: all(bool(dict(row["pure_feature_claims"]).get(claim, False)) for row in rows)
                for claim in claim_names
            },
            "total_retimed_transitions": sum(int(row["retimed_transition_count"]) for row in rows),
            "total_first_thresholds": sum(int(row["first_threshold_count"]) for row in rows),
            "total_post_ladder_first_thresholds": sum(int(row["post_ladder_first_threshold_count"]) for row in rows),
            "post_ladder_word_counts": as_counter_dict(combined_words),
            "terminal_v2_counts": as_counter_dict(combined_terminal_v2),
            "q_mod_8_counts": as_counter_dict(combined_q_mod_8),
            "q_align_mod16_phase_counts": as_counter_dict(combined_q_phase),
            "terminal_mod_16_counts": as_counter_dict(combined_terminal_mod_16),
            "terminal_mod_64_counts": as_counter_dict(combined_terminal_mod_64),
            "post_ladder_child_residue_purity": {
                str(modulus): residue_purity_summary(
                    total=combined_retimed_child_residues[modulus],
                    positive=combined_post_ladder_child_residues[modulus],
                    top_n=args.top_n,
                )
                for modulus in DEFAULT_RESIDUE_MODULI
            },
            "post_ladder_parent_residue_purity": {
                str(modulus): residue_purity_summary(
                    total=combined_retimed_parent_residues[modulus],
                    positive=combined_post_ladder_parent_residues[modulus],
                    top_n=args.top_n,
                )
                for modulus in DEFAULT_RESIDUE_MODULI
            },
            "global_step_offset_min": min(offsets) if offsets else None,
            "global_step_offset_max": max(offsets) if offsets else None,
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--min-parent-depth", type=int, default=18)
    parser.add_argument("--max-parent-depth", type=int, default=25)
    parser.add_argument("--max-depth", type=int, default=1024)
    parser.add_argument("--max-steps", type=int, default=50000)
    parser.add_argument("--top-n", type=int, default=8)
    parser.add_argument(
        "--cache-template",
        default="experiments/results/branch_prefix_retimed_post_ladder_tail_d{parent_depth}_d{child_depth}_20260702.json",
    )
    parser.add_argument("--use-cache", action="store_true")
    parser.add_argument("--refresh", action="store_true")
    parser.add_argument("--write-depth-cache", action="store_true")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    if args.min_parent_depth < 1:
        raise SystemExit("--min-parent-depth must be positive")
    if args.max_parent_depth < args.min_parent_depth:
        raise SystemExit("--max-parent-depth must be >= --min-parent-depth")
    if args.max_steps < 1:
        raise SystemExit("--max-steps must be positive")
    if args.top_n < 1:
        raise SystemExit("--top-n must be positive")

    payload = run(args)
    text = json.dumps(payload, indent=2, sort_keys=True)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text + "\n", encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()

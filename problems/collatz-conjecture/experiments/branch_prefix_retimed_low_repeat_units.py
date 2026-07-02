#!/usr/bin/env python3
"""Analyze low-repeat prepaid pressure units in retimed transitions.

The retimed signature sweep leaves a small third regime: pressure units whose
last visible credit was a low ``-5 mod 64`` repeat gate.  This script
reconstructs those units and records the exact low-repeat macro algebra and
timing.

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

from branch_potential_analyzer import enumerate_frontier, odd3_macro_info, powers_of_three, round_float, shortcut_step
from branch_prefix_dominance_analyzer import analyze_prefix_start
from branch_prefix_retimed_post_ladder_tail import DEFAULT_RESIDUE_MODULI, as_counter_dict, parity_word
from branch_prefix_retimed_pressure import pressure_trace, transition_row
from branch_prefix_retimed_signature import classify_pressure_unit


def low_repeat_residue_purity_summary(
    *,
    total: Counter[int],
    low_repeat: Counter[int],
    top_n: int,
) -> dict[str, object]:
    pure_low_repeat = []
    pure_non_low_repeat = []
    mixed = []
    for residue, total_count in total.items():
        low_repeat_count = int(low_repeat.get(residue, 0))
        if low_repeat_count == total_count:
            pure_low_repeat.append((residue, total_count))
        elif low_repeat_count == 0:
            pure_non_low_repeat.append((residue, total_count))
        else:
            mixed.append((residue, total_count, low_repeat_count))

    low_repeat_total = sum(low_repeat.values())
    pure_low_repeat_total = sum(count for _, count in pure_low_repeat)
    mixed_low_repeat_total = sum(count for _, _, count in mixed)
    return {
        "occupied_buckets": len(total),
        "low_repeat_buckets": len(low_repeat),
        "pure_low_repeat_buckets": len(pure_low_repeat),
        "pure_non_low_repeat_buckets": len(pure_non_low_repeat),
        "mixed_buckets": len(mixed),
        "low_repeat_total": low_repeat_total,
        "low_repeat_in_pure_buckets": pure_low_repeat_total,
        "low_repeat_in_mixed_buckets": mixed_low_repeat_total,
        "low_repeat_pure_bucket_fraction": (
            round_float(pure_low_repeat_total / low_repeat_total) if low_repeat_total else 1.0
        ),
        "top_pure_low_repeat_buckets": {
            str(residue): int(count)
            for residue, count in sorted(pure_low_repeat, key=lambda item: item[1], reverse=True)[:top_n]
        },
        "top_mixed_buckets": {
            str(residue): {
                "total": int(total_count),
                "low_repeat": int(low_repeat_count),
                "low_repeat_fraction": round_float(low_repeat_count / total_count),
            }
            for residue, total_count, low_repeat_count in sorted(
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


def compact_record(
    *,
    parent: int,
    child: int,
    parent_depth: int,
    event_index: int,
    event: dict[str, object],
    transition: dict[str, object],
    entry: int,
    align: int,
    macro_value: int,
    macro_align_after: int,
    lag_word: str,
) -> dict[str, object]:
    last = dict(event["last_credit_event"])
    lag = int(event["step"]) - int(last["step"])
    return {
        "parent": parent,
        "child": child,
        "event_index": event_index,
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
        "entry_mod_64": entry % 64,
        "entry_mod_256": entry % 256,
        "align": align,
        "align_mod_3": align % 3,
        "macro_value": macro_value,
        "macro_align_after": macro_align_after,
        "macro_align_drop": align - macro_align_after,
        "macro_value_mod_64": macro_value % 64,
        "lag": lag,
        "lag_minus_align": lag - align,
        "lag_word": lag_word,
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
    pressure_unit_count = 0
    low_repeat_count = 0

    pressure_regimes: Counter[str] = Counter()
    event_index_counts: Counter[int] = Counter()
    event_index_required_above_parent_counts: Counter[str] = Counter()
    lag_counts: Counter[int] = Counter()
    lag_minus_align_counts: Counter[int] = Counter()
    lag_word_counts: Counter[str] = Counter()
    align_counts: Counter[int] = Counter()
    align_mod_3_counts: Counter[int] = Counter()
    entry_mod_256_counts: Counter[int] = Counter()
    macro_value_mod_64_counts: Counter[int] = Counter()
    macro_align_after_counts: Counter[int] = Counter()
    surplus_counts: Counter[int] = Counter()
    step_offset_counts: Counter[int] = Counter()

    all_pressure_state_residues = {modulus: Counter() for modulus in DEFAULT_RESIDUE_MODULI}
    low_repeat_pressure_state_residues = {modulus: Counter() for modulus in DEFAULT_RESIDUE_MODULI}

    repeat_law_failures: list[dict[str, object]] = []
    terminal_state_failures: list[dict[str, object]] = []
    entry_residue_failures: list[dict[str, object]] = []
    tightest: list[dict[str, object]] = []
    largest_offsets: list[dict[str, object]] = []
    examples_by_lag_word: dict[str, list[dict[str, object]]] = {}

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
            pressure_units = [
                dict(event)
                for event in trace["pressure_events"]
                if int(dict(event)["required"]) > parent_required
            ]
            for event_index, event in enumerate(pressure_units, start=1):
                pressure_unit_count += 1
                state = int(event["state"])
                for modulus in DEFAULT_RESIDUE_MODULI:
                    all_pressure_state_residues[modulus][state % modulus] += 1

                regime = classify_pressure_unit(event)
                pressure_regimes[regime] += 1
                if regime != "low_repeat_prepaid":
                    continue

                low_repeat_count += 1
                for modulus in DEFAULT_RESIDUE_MODULI:
                    low_repeat_pressure_state_residues[modulus][state % modulus] += 1

                last = dict(event["last_credit_event"])
                entry = int(last["state"])
                align = int(last["align"])
                info = odd3_macro_info(entry)
                macro_value = (9 * entry + 5) // 8
                macro_align_after = int(info["minus5_align_after_macro"])
                lag = int(event["step"]) - int(last["step"])
                lag_state, lag_parities = simulate_steps(entry, lag)
                lag_word = parity_word(lag_parities)
                record = compact_record(
                    parent=parent,
                    child=child,
                    parent_depth=parent_depth,
                    event_index=event_index,
                    event=event,
                    transition=transition,
                    entry=entry,
                    align=align,
                    macro_value=macro_value,
                    macro_align_after=macro_align_after,
                    lag_word=lag_word,
                )

                if entry % 64 != 59 or str(info["branch"]) != "repeat_minus5_gate":
                    entry_residue_failures.append(record)
                if not bool(info["repeat_law_ok"]) or macro_align_after != align - 3:
                    repeat_law_failures.append(record)
                if lag_state != state:
                    terminal_state_failures.append(record)

                event_index_counts[event_index] += 1
                event_index_required_above_parent_counts[
                    f"{event_index}:{record['required_above_parent']}"
                ] += 1
                lag_counts[lag] += 1
                lag_minus_align_counts[lag - align] += 1
                lag_word_counts[lag_word] += 1
                align_counts[align] += 1
                align_mod_3_counts[align % 3] += 1
                entry_mod_256_counts[entry % 256] += 1
                macro_value_mod_64_counts[macro_value % 64] += 1
                macro_align_after_counts[macro_align_after] += 1
                surplus_counts[int(record["surplus"])] += 1
                step_offset_counts[int(record["step_offset_from_parent_depth"])] += 1
                examples_by_lag_word.setdefault(lag_word, [])
                if len(examples_by_lag_word[lag_word]) < args.top_n:
                    examples_by_lag_word[lag_word].append(record)
                keep_smallest(tightest, record, "surplus")
                keep_largest(largest_offsets, record, "step_offset_from_parent_depth")

    return {
        "status": "branch-prefix-retimed-low-repeat-units",
        "elapsed_seconds": round_float(perf_counter() - started, 6),
        "parent_depth": parent_depth,
        "child_depth": child_depth,
        "frontiers": {
            "parent": {**parent_stats, "positive_live_count": len(parent_leaves), "depth": parent_depth},
            "child": {**child_stats, "positive_live_count": len(child_leaves), "depth": child_depth},
        },
        "positive_pressure_transition_count": positive_pressure_count,
        "retimed_transition_count": retimed_count,
        "above_parent_pressure_unit_count": pressure_unit_count,
        "low_repeat_pressure_unit_count": low_repeat_count,
        "pressure_regime_counts": as_counter_dict(pressure_regimes),
        "event_index_counts": as_counter_dict(event_index_counts),
        "event_index_required_above_parent_counts": as_counter_dict(event_index_required_above_parent_counts),
        "lag_counts": as_counter_dict(lag_counts),
        "lag_minus_align_counts": as_counter_dict(lag_minus_align_counts),
        "lag_word_counts": as_counter_dict(lag_word_counts),
        "align_counts": as_counter_dict(align_counts),
        "align_mod_3_counts": as_counter_dict(align_mod_3_counts),
        "entry_mod_256_counts": as_counter_dict(entry_mod_256_counts),
        "macro_value_mod_64_counts": as_counter_dict(macro_value_mod_64_counts),
        "macro_align_after_counts": as_counter_dict(macro_align_after_counts),
        "surplus_histogram": as_counter_dict(surplus_counts),
        "step_offset_histogram": as_counter_dict(step_offset_counts),
        "low_repeat_pressure_state_residue_purity": {
            str(modulus): low_repeat_residue_purity_summary(
                total=all_pressure_state_residues[modulus],
                low_repeat=low_repeat_pressure_state_residues[modulus],
                top_n=args.top_n,
            )
            for modulus in DEFAULT_RESIDUE_MODULI
        },
        "all_pressure_state_residue_counts": {
            str(modulus): as_counter_dict(counter)
            for modulus, counter in all_pressure_state_residues.items()
        },
        "low_repeat_pressure_state_residue_counts": {
            str(modulus): as_counter_dict(counter)
            for modulus, counter in low_repeat_pressure_state_residues.items()
        },
        "pure_feature_claims": {
            "all_entries_are_minus5_mod64_repeat_gates": not entry_residue_failures,
            "all_repeat_laws_checked": not repeat_law_failures,
            "all_lag_simulations_match_pressure_state": not terminal_state_failures,
        },
        "tightest_low_repeat_pressure_units": tightest,
        "largest_step_offsets": largest_offsets,
        "examples_by_lag_word": examples_by_lag_word,
        "entry_residue_failures": entry_residue_failures[: args.top_n],
        "repeat_law_failures": repeat_law_failures[: args.top_n],
        "terminal_state_failures": terminal_state_failures[: args.top_n],
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
    return {
        "parent_depth": int(payload["parent_depth"]),
        "child_depth": int(payload["child_depth"]),
        "cached": cached,
        "retimed_transition_count": int(payload["retimed_transition_count"]),
        "above_parent_pressure_unit_count": int(payload["above_parent_pressure_unit_count"]),
        "low_repeat_pressure_unit_count": int(payload["low_repeat_pressure_unit_count"]),
        "pressure_regime_counts": payload["pressure_regime_counts"],
        "event_index_counts": payload["event_index_counts"],
        "event_index_required_above_parent_counts": payload["event_index_required_above_parent_counts"],
        "lag_counts": payload["lag_counts"],
        "lag_minus_align_counts": payload["lag_minus_align_counts"],
        "lag_word_counts": payload["lag_word_counts"],
        "align_counts": payload["align_counts"],
        "align_mod_3_counts": payload["align_mod_3_counts"],
        "entry_mod_256_counts": payload["entry_mod_256_counts"],
        "macro_value_mod_64_counts": payload["macro_value_mod_64_counts"],
        "macro_align_after_counts": payload["macro_align_after_counts"],
        "step_offset_min": min(offsets) if offsets else None,
        "step_offset_max": max(offsets) if offsets else None,
        "low_repeat_pressure_state_residue_purity": payload["low_repeat_pressure_state_residue_purity"],
        "pure_feature_claims": payload["pure_feature_claims"],
    }


def update_from_counter(target: Counter[str], source: dict[str, object]) -> None:
    target.update({str(key): int(value) for key, value in source.items()})


def run(args: argparse.Namespace) -> dict[str, object]:
    rows = []
    combined_pressure_state_residues = {modulus: Counter() for modulus in DEFAULT_RESIDUE_MODULI}
    combined_low_repeat_state_residues = {modulus: Counter() for modulus in DEFAULT_RESIDUE_MODULI}

    for depth in range(args.min_parent_depth, args.max_parent_depth + 1):
        payload, cached = load_or_run_depth(args, depth)
        if not payload.get("all_pressure_state_residue_counts"):
            raise RuntimeError(f"refresh caches to combine pressure-state residue counts at depth {depth}")
        for modulus in DEFAULT_RESIDUE_MODULI:
            key = str(modulus)
            for residue, count in dict(payload["all_pressure_state_residue_counts"][key]).items():
                combined_pressure_state_residues[modulus][int(residue)] += int(count)
            for residue, count in dict(payload["low_repeat_pressure_state_residue_counts"][key]).items():
                combined_low_repeat_state_residues[modulus][int(residue)] += int(count)
        rows.append(compact_depth(payload, cached))

    combined_regimes: Counter[str] = Counter()
    combined_event_index: Counter[str] = Counter()
    combined_event_index_required: Counter[str] = Counter()
    combined_lag: Counter[str] = Counter()
    combined_lag_minus_align: Counter[str] = Counter()
    combined_lag_word: Counter[str] = Counter()
    combined_align: Counter[str] = Counter()
    combined_align_mod_3: Counter[str] = Counter()
    combined_entry_mod_256: Counter[str] = Counter()
    combined_macro_mod_64: Counter[str] = Counter()
    combined_macro_align_after: Counter[str] = Counter()
    claim_names = sorted({claim for row in rows for claim in dict(row["pure_feature_claims"])})
    for row in rows:
        update_from_counter(combined_regimes, dict(row["pressure_regime_counts"]))
        update_from_counter(combined_event_index, dict(row["event_index_counts"]))
        update_from_counter(combined_event_index_required, dict(row["event_index_required_above_parent_counts"]))
        update_from_counter(combined_lag, dict(row["lag_counts"]))
        update_from_counter(combined_lag_minus_align, dict(row["lag_minus_align_counts"]))
        update_from_counter(combined_lag_word, dict(row["lag_word_counts"]))
        update_from_counter(combined_align, dict(row["align_counts"]))
        update_from_counter(combined_align_mod_3, dict(row["align_mod_3_counts"]))
        update_from_counter(combined_entry_mod_256, dict(row["entry_mod_256_counts"]))
        update_from_counter(combined_macro_mod_64, dict(row["macro_value_mod_64_counts"]))
        update_from_counter(combined_macro_align_after, dict(row["macro_align_after_counts"]))

    offsets = [
        int(value)
        for row in rows
        for value in (row["step_offset_min"], row["step_offset_max"])
        if value is not None
    ]

    return {
        "status": "branch-prefix-retimed-low-repeat-units-sweep",
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
            "total_above_parent_pressure_units": sum(int(row["above_parent_pressure_unit_count"]) for row in rows),
            "total_low_repeat_pressure_units": sum(int(row["low_repeat_pressure_unit_count"]) for row in rows),
            "pressure_regime_counts": as_counter_dict(combined_regimes),
            "event_index_counts": as_counter_dict(combined_event_index),
            "event_index_required_above_parent_counts": as_counter_dict(combined_event_index_required),
            "lag_counts": as_counter_dict(combined_lag),
            "lag_minus_align_counts": as_counter_dict(combined_lag_minus_align),
            "lag_word_counts": as_counter_dict(combined_lag_word),
            "align_counts": as_counter_dict(combined_align),
            "align_mod_3_counts": as_counter_dict(combined_align_mod_3),
            "entry_mod_256_counts": as_counter_dict(combined_entry_mod_256),
            "macro_value_mod_64_counts": as_counter_dict(combined_macro_mod_64),
            "macro_align_after_counts": as_counter_dict(combined_macro_align_after),
            "low_repeat_pressure_state_residue_purity": {
                str(modulus): low_repeat_residue_purity_summary(
                    total=combined_pressure_state_residues[modulus],
                    low_repeat=combined_low_repeat_state_residues[modulus],
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
        default="experiments/results/branch_prefix_retimed_low_repeat_units_d{parent_depth}_d{child_depth}_20260702.json",
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

#!/usr/bin/env python3
"""Analyze active high-ladder pressure units in retimed transitions.

The retimed signature sweep splits above-parent pressure units into three
regimes.  The post-ladder and low-repeat regimes have separate algebra notes;
this script reconstructs the dominant active high-ladder regime.

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

from branch_potential_analyzer import enumerate_frontier, powers_of_three, round_float, shortcut_step, v2
from branch_prefix_dominance_analyzer import analyze_prefix_start
from branch_prefix_retimed_post_ladder_tail import DEFAULT_RESIDUE_MODULI, as_counter_dict
from branch_prefix_retimed_pressure import pressure_trace, transition_row
from branch_prefix_retimed_signature import classify_pressure_unit


def active_residue_purity_summary(
    *,
    total: Counter[int],
    active: Counter[int],
    top_n: int,
) -> dict[str, object]:
    pure_active = []
    pure_non_active = []
    mixed = []
    for residue, total_count in total.items():
        active_count = int(active.get(residue, 0))
        if active_count == total_count:
            pure_active.append((residue, total_count))
        elif active_count == 0:
            pure_non_active.append((residue, total_count))
        else:
            mixed.append((residue, total_count, active_count))

    active_total = sum(active.values())
    pure_active_total = sum(count for _, count in pure_active)
    mixed_active_total = sum(count for _, _, count in mixed)
    return {
        "occupied_buckets": len(total),
        "active_buckets": len(active),
        "pure_active_buckets": len(pure_active),
        "pure_non_active_buckets": len(pure_non_active),
        "mixed_buckets": len(mixed),
        "active_total": active_total,
        "active_in_pure_buckets": pure_active_total,
        "active_in_mixed_buckets": mixed_active_total,
        "active_pure_bucket_fraction": round_float(pure_active_total / active_total) if active_total else 1.0,
        "top_pure_active_buckets": {
            str(residue): int(count)
            for residue, count in sorted(pure_active, key=lambda item: item[1], reverse=True)[:top_n]
        },
        "top_mixed_buckets": {
            str(residue): {
                "total": int(total_count),
                "active": int(active_count),
                "active_fraction": round_float(active_count / total_count),
            }
            for residue, total_count, active_count in sorted(
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
    q: int,
    lag: int,
    expected_state: int,
    terminal: int,
    state_plus_one_v2: int,
) -> dict[str, object]:
    remaining_align = align - lag
    return {
        "parent": parent,
        "child": child,
        "event_index": event_index,
        "event": event["event"],
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
        "align": align,
        "align_mod_4": align % 4,
        "q": q,
        "q_mod_8": q % 8,
        "q_mod_16": q % 16,
        "ladder_credit": align - 2,
        "lag": lag,
        "remaining_align": remaining_align,
        "lag_minus_align": lag - align,
        "expected_state": expected_state,
        "state_plus_one_v2": state_plus_one_v2,
        "terminal": terminal,
        "terminal_mod_16": terminal % 16,
        "terminal_mod_64": terminal % 64,
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
    active_count = 0

    pressure_regimes: Counter[str] = Counter()
    event_counts: Counter[str] = Counter()
    event_index_counts: Counter[int] = Counter()
    event_index_required_above_parent_counts: Counter[str] = Counter()
    lag_counts: Counter[int] = Counter()
    lag_minus_align_counts: Counter[int] = Counter()
    remaining_align_counts: Counter[int] = Counter()
    align_counts: Counter[int] = Counter()
    align_mod_4_counts: Counter[int] = Counter()
    ladder_credit_counts: Counter[int] = Counter()
    q_mod_8_counts: Counter[int] = Counter()
    q_mod_16_counts: Counter[int] = Counter()
    terminal_mod_16_counts: Counter[int] = Counter()
    terminal_mod_64_counts: Counter[int] = Counter()
    state_plus_one_v2_counts: Counter[int] = Counter()
    event_index_lag_counts: Counter[str] = Counter()
    required_above_parent_lag_counts: Counter[str] = Counter()
    active_units_per_transition: Counter[int] = Counter()
    active_ladders_per_transition: Counter[int] = Counter()
    active_units_per_ladder: Counter[int] = Counter()
    surplus_counts: Counter[int] = Counter()
    step_offset_counts: Counter[int] = Counter()

    all_pressure_state_residues = {modulus: Counter() for modulus in DEFAULT_RESIDUE_MODULI}
    active_pressure_state_residues = {modulus: Counter() for modulus in DEFAULT_RESIDUE_MODULI}

    event_kind_failures: list[dict[str, object]] = []
    formula_failures: list[dict[str, object]] = []
    simulation_failures: list[dict[str, object]] = []
    alignment_burn_failures: list[dict[str, object]] = []
    parity_failures: list[dict[str, object]] = []
    event_index_failures: list[dict[str, object]] = []
    tightest: list[dict[str, object]] = []
    largest_offsets: list[dict[str, object]] = []
    examples_by_remaining_align: dict[str, list[dict[str, object]]] = {}

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
            transition_active_count = 0
            transition_ladder_counts: Counter[str] = Counter()
            for event_index, event in enumerate(pressure_units, start=1):
                pressure_unit_count += 1
                state = int(event["state"])
                for modulus in DEFAULT_RESIDUE_MODULI:
                    all_pressure_state_residues[modulus][state % modulus] += 1

                regime = classify_pressure_unit(event)
                pressure_regimes[regime] += 1
                if regime != "high_inside_active_ladder":
                    continue

                active_count += 1
                transition_active_count += 1
                for modulus in DEFAULT_RESIDUE_MODULI:
                    active_pressure_state_residues[modulus][state % modulus] += 1

                last = dict(event["last_credit_event"])
                entry = int(last["state"])
                align = int(last["align"])
                q = (entry + 1) >> align
                lag = int(event["step"]) - int(last["step"])
                expected_state = (3**lag) * (1 << (align - lag)) * q - 1
                terminal = (3**align) * q - 1
                state_plus_one_v2 = v2(state + 1)
                lag_state, lag_parities = simulate_steps(entry, lag)
                record = compact_record(
                    parent=parent,
                    child=child,
                    parent_depth=parent_depth,
                    event_index=event_index,
                    event=event,
                    transition=transition,
                    entry=entry,
                    align=align,
                    q=q,
                    lag=lag,
                    expected_state=expected_state,
                    terminal=terminal,
                    state_plus_one_v2=state_plus_one_v2,
                )

                if str(event["event"]) != "high_ladder_step" or str(last["kind"]) != "high_ladder":
                    event_kind_failures.append(record)
                if expected_state != state:
                    formula_failures.append(record)
                if lag_state != state:
                    simulation_failures.append(record)
                if state_plus_one_v2 != align - lag:
                    alignment_burn_failures.append(record)
                if lag_parities != [1] * lag:
                    parity_failures.append(record)
                if int(record["event_index"]) != int(record["required_above_parent"]):
                    event_index_failures.append(record)

                ladder_key = f"{last['step']}:{entry}"
                transition_ladder_counts[ladder_key] += 1
                event_counts[str(event["event"])] += 1
                event_index_counts[event_index] += 1
                event_index_required_above_parent_counts[
                    f"{event_index}:{record['required_above_parent']}"
                ] += 1
                lag_counts[lag] += 1
                lag_minus_align_counts[lag - align] += 1
                remaining_align_counts[align - lag] += 1
                align_counts[align] += 1
                align_mod_4_counts[align % 4] += 1
                ladder_credit_counts[align - 2] += 1
                q_mod_8_counts[q % 8] += 1
                q_mod_16_counts[q % 16] += 1
                terminal_mod_16_counts[terminal % 16] += 1
                terminal_mod_64_counts[terminal % 64] += 1
                state_plus_one_v2_counts[state_plus_one_v2] += 1
                event_index_lag_counts[f"{event_index}:{lag}"] += 1
                required_above_parent_lag_counts[f"{record['required_above_parent']}:{lag}"] += 1
                surplus_counts[int(record["surplus"])] += 1
                step_offset_counts[int(record["step_offset_from_parent_depth"])] += 1
                examples_by_remaining_align.setdefault(str(align - lag), [])
                if len(examples_by_remaining_align[str(align - lag)]) < args.top_n:
                    examples_by_remaining_align[str(align - lag)].append(record)
                keep_smallest(tightest, record, "surplus")
                keep_largest(largest_offsets, record, "step_offset_from_parent_depth")

            if transition_active_count:
                active_units_per_transition[transition_active_count] += 1
                active_ladders_per_transition[len(transition_ladder_counts)] += 1
                for count in transition_ladder_counts.values():
                    active_units_per_ladder[count] += 1

    return {
        "status": "branch-prefix-retimed-active-ladder-units",
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
        "active_ladder_pressure_unit_count": active_count,
        "pressure_regime_counts": as_counter_dict(pressure_regimes),
        "pressure_event_counts": as_counter_dict(event_counts),
        "event_index_counts": as_counter_dict(event_index_counts),
        "event_index_required_above_parent_counts": as_counter_dict(event_index_required_above_parent_counts),
        "lag_counts": as_counter_dict(lag_counts),
        "lag_minus_align_counts": as_counter_dict(lag_minus_align_counts),
        "remaining_align_counts": as_counter_dict(remaining_align_counts),
        "align_counts": as_counter_dict(align_counts),
        "align_mod_4_counts": as_counter_dict(align_mod_4_counts),
        "ladder_credit_counts": as_counter_dict(ladder_credit_counts),
        "q_mod_8_counts": as_counter_dict(q_mod_8_counts),
        "q_mod_16_counts": as_counter_dict(q_mod_16_counts),
        "terminal_mod_16_counts": as_counter_dict(terminal_mod_16_counts),
        "terminal_mod_64_counts": as_counter_dict(terminal_mod_64_counts),
        "state_plus_one_v2_counts": as_counter_dict(state_plus_one_v2_counts),
        "event_index_lag_counts": as_counter_dict(event_index_lag_counts),
        "required_above_parent_lag_counts": as_counter_dict(required_above_parent_lag_counts),
        "active_units_per_transition": as_counter_dict(active_units_per_transition),
        "active_ladders_per_transition": as_counter_dict(active_ladders_per_transition),
        "active_units_per_ladder": as_counter_dict(active_units_per_ladder),
        "surplus_histogram": as_counter_dict(surplus_counts),
        "step_offset_histogram": as_counter_dict(step_offset_counts),
        "active_pressure_state_residue_purity": {
            str(modulus): active_residue_purity_summary(
                total=all_pressure_state_residues[modulus],
                active=active_pressure_state_residues[modulus],
                top_n=args.top_n,
            )
            for modulus in DEFAULT_RESIDUE_MODULI
        },
        "all_pressure_state_residue_counts": {
            str(modulus): as_counter_dict(counter)
            for modulus, counter in all_pressure_state_residues.items()
        },
        "active_pressure_state_residue_counts": {
            str(modulus): as_counter_dict(counter)
            for modulus, counter in active_pressure_state_residues.items()
        },
        "pure_feature_claims": {
            "all_active_events_are_high_ladder_steps": not event_kind_failures,
            "all_active_ladder_formulas_checked": not formula_failures,
            "all_lag_simulations_match_pressure_state": not simulation_failures,
            "all_active_parities_are_odd": not parity_failures,
            "all_alignment_burns_checked": not alignment_burn_failures,
            "all_event_indexes_equal_required_above_parent": not event_index_failures,
        },
        "tightest_active_ladder_pressure_units": tightest,
        "largest_step_offsets": largest_offsets,
        "examples_by_remaining_align": examples_by_remaining_align,
        "event_kind_failures": event_kind_failures[: args.top_n],
        "formula_failures": formula_failures[: args.top_n],
        "simulation_failures": simulation_failures[: args.top_n],
        "alignment_burn_failures": alignment_burn_failures[: args.top_n],
        "parity_failures": parity_failures[: args.top_n],
        "event_index_failures": event_index_failures[: args.top_n],
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
        "active_ladder_pressure_unit_count": int(payload["active_ladder_pressure_unit_count"]),
        "pressure_regime_counts": payload["pressure_regime_counts"],
        "pressure_event_counts": payload["pressure_event_counts"],
        "event_index_counts": payload["event_index_counts"],
        "event_index_required_above_parent_counts": payload["event_index_required_above_parent_counts"],
        "lag_counts": payload["lag_counts"],
        "lag_minus_align_counts": payload["lag_minus_align_counts"],
        "remaining_align_counts": payload["remaining_align_counts"],
        "align_counts": payload["align_counts"],
        "align_mod_4_counts": payload["align_mod_4_counts"],
        "ladder_credit_counts": payload["ladder_credit_counts"],
        "q_mod_8_counts": payload["q_mod_8_counts"],
        "q_mod_16_counts": payload["q_mod_16_counts"],
        "terminal_mod_16_counts": payload["terminal_mod_16_counts"],
        "terminal_mod_64_counts": payload["terminal_mod_64_counts"],
        "state_plus_one_v2_counts": payload["state_plus_one_v2_counts"],
        "event_index_lag_counts": payload["event_index_lag_counts"],
        "required_above_parent_lag_counts": payload["required_above_parent_lag_counts"],
        "active_units_per_transition": payload["active_units_per_transition"],
        "active_ladders_per_transition": payload["active_ladders_per_transition"],
        "active_units_per_ladder": payload["active_units_per_ladder"],
        "step_offset_min": min(offsets) if offsets else None,
        "step_offset_max": max(offsets) if offsets else None,
        "active_pressure_state_residue_purity": payload["active_pressure_state_residue_purity"],
        "pure_feature_claims": payload["pure_feature_claims"],
    }


def update_from_counter(target: Counter[str], source: dict[str, object]) -> None:
    target.update({str(key): int(value) for key, value in source.items()})


def run(args: argparse.Namespace) -> dict[str, object]:
    rows = []
    combined_pressure_state_residues = {modulus: Counter() for modulus in DEFAULT_RESIDUE_MODULI}
    combined_active_state_residues = {modulus: Counter() for modulus in DEFAULT_RESIDUE_MODULI}

    for depth in range(args.min_parent_depth, args.max_parent_depth + 1):
        payload, cached = load_or_run_depth(args, depth)
        if not payload.get("all_pressure_state_residue_counts"):
            raise RuntimeError(f"refresh caches to combine pressure-state residue counts at depth {depth}")
        for modulus in DEFAULT_RESIDUE_MODULI:
            key = str(modulus)
            for residue, count in dict(payload["all_pressure_state_residue_counts"][key]).items():
                combined_pressure_state_residues[modulus][int(residue)] += int(count)
            for residue, count in dict(payload["active_pressure_state_residue_counts"][key]).items():
                combined_active_state_residues[modulus][int(residue)] += int(count)
        rows.append(compact_depth(payload, cached))

    combined_regimes: Counter[str] = Counter()
    combined_events: Counter[str] = Counter()
    combined_event_index: Counter[str] = Counter()
    combined_event_index_required: Counter[str] = Counter()
    combined_lag: Counter[str] = Counter()
    combined_lag_minus_align: Counter[str] = Counter()
    combined_remaining_align: Counter[str] = Counter()
    combined_align: Counter[str] = Counter()
    combined_align_mod_4: Counter[str] = Counter()
    combined_ladder_credit: Counter[str] = Counter()
    combined_q_mod_8: Counter[str] = Counter()
    combined_q_mod_16: Counter[str] = Counter()
    combined_terminal_mod_16: Counter[str] = Counter()
    combined_terminal_mod_64: Counter[str] = Counter()
    combined_state_plus_one_v2: Counter[str] = Counter()
    combined_event_index_lag: Counter[str] = Counter()
    combined_required_lag: Counter[str] = Counter()
    combined_units_per_transition: Counter[str] = Counter()
    combined_ladders_per_transition: Counter[str] = Counter()
    combined_units_per_ladder: Counter[str] = Counter()
    claim_names = sorted({claim for row in rows for claim in dict(row["pure_feature_claims"])})
    for row in rows:
        update_from_counter(combined_regimes, dict(row["pressure_regime_counts"]))
        update_from_counter(combined_events, dict(row["pressure_event_counts"]))
        update_from_counter(combined_event_index, dict(row["event_index_counts"]))
        update_from_counter(combined_event_index_required, dict(row["event_index_required_above_parent_counts"]))
        update_from_counter(combined_lag, dict(row["lag_counts"]))
        update_from_counter(combined_lag_minus_align, dict(row["lag_minus_align_counts"]))
        update_from_counter(combined_remaining_align, dict(row["remaining_align_counts"]))
        update_from_counter(combined_align, dict(row["align_counts"]))
        update_from_counter(combined_align_mod_4, dict(row["align_mod_4_counts"]))
        update_from_counter(combined_ladder_credit, dict(row["ladder_credit_counts"]))
        update_from_counter(combined_q_mod_8, dict(row["q_mod_8_counts"]))
        update_from_counter(combined_q_mod_16, dict(row["q_mod_16_counts"]))
        update_from_counter(combined_terminal_mod_16, dict(row["terminal_mod_16_counts"]))
        update_from_counter(combined_terminal_mod_64, dict(row["terminal_mod_64_counts"]))
        update_from_counter(combined_state_plus_one_v2, dict(row["state_plus_one_v2_counts"]))
        update_from_counter(combined_event_index_lag, dict(row["event_index_lag_counts"]))
        update_from_counter(combined_required_lag, dict(row["required_above_parent_lag_counts"]))
        update_from_counter(combined_units_per_transition, dict(row["active_units_per_transition"]))
        update_from_counter(combined_ladders_per_transition, dict(row["active_ladders_per_transition"]))
        update_from_counter(combined_units_per_ladder, dict(row["active_units_per_ladder"]))

    offsets = [
        int(value)
        for row in rows
        for value in (row["step_offset_min"], row["step_offset_max"])
        if value is not None
    ]

    return {
        "status": "branch-prefix-retimed-active-ladder-units-sweep",
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
            "total_active_ladder_pressure_units": sum(
                int(row["active_ladder_pressure_unit_count"]) for row in rows
            ),
            "pressure_regime_counts": as_counter_dict(combined_regimes),
            "pressure_event_counts": as_counter_dict(combined_events),
            "event_index_counts": as_counter_dict(combined_event_index),
            "event_index_required_above_parent_counts": as_counter_dict(combined_event_index_required),
            "lag_counts": as_counter_dict(combined_lag),
            "lag_minus_align_counts": as_counter_dict(combined_lag_minus_align),
            "remaining_align_counts": as_counter_dict(combined_remaining_align),
            "align_counts": as_counter_dict(combined_align),
            "align_mod_4_counts": as_counter_dict(combined_align_mod_4),
            "ladder_credit_counts": as_counter_dict(combined_ladder_credit),
            "q_mod_8_counts": as_counter_dict(combined_q_mod_8),
            "q_mod_16_counts": as_counter_dict(combined_q_mod_16),
            "terminal_mod_16_counts": as_counter_dict(combined_terminal_mod_16),
            "terminal_mod_64_counts": as_counter_dict(combined_terminal_mod_64),
            "state_plus_one_v2_counts": as_counter_dict(combined_state_plus_one_v2),
            "event_index_lag_counts": as_counter_dict(combined_event_index_lag),
            "required_above_parent_lag_counts": as_counter_dict(combined_required_lag),
            "active_units_per_transition": as_counter_dict(combined_units_per_transition),
            "active_ladders_per_transition": as_counter_dict(combined_ladders_per_transition),
            "active_units_per_ladder": as_counter_dict(combined_units_per_ladder),
            "active_pressure_state_residue_purity": {
                str(modulus): active_residue_purity_summary(
                    total=combined_pressure_state_residues[modulus],
                    active=combined_active_state_residues[modulus],
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
        default="experiments/results/branch_prefix_retimed_active_ladder_units_d{parent_depth}_d{child_depth}_20260702.json",
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

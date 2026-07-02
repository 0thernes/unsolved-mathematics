#!/usr/bin/env python3
"""Classify boundary types for retimed first above-parent thresholds.

The affine lift lemma proves that an upper lift shares its first d shortcut
parities with the parent and then flips parity at depth d.  This script asks
which boundary type appears in the retimed hard class and how it relates to
first-threshold surplus, step offset, and high-ladder local words.

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

from branch_potential_analyzer import enumerate_frontier, powers_of_three, round_float, shortcut_step
from branch_prefix_dominance_analyzer import analyze_prefix_start
from branch_prefix_retimed_post_ladder_tail import as_counter_dict
from branch_prefix_retimed_pressure import pressure_trace, transition_row
from branch_prefix_retimed_signature import classify_pressure_unit


def parity_word(bits: list[int]) -> str:
    return "".join("O" if bit else "E" for bit in bits)


def trajectory(start: int, steps: int) -> tuple[list[int], list[int]]:
    current = int(start)
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


def keep_smallest(records: list[dict[str, object]], record: dict[str, object], top_n: int) -> None:
    records.append(record)
    records.sort(
        key=lambda row: (
            int(row["surplus"]),
            int(row["step_offset_from_parent_depth"]),
            str(row["boundary_pair"]),
            int(row["child"]),
        )
    )
    del records[top_n:]


def compact_boundary_record(
    *,
    parent_depth: int,
    parent: int,
    child: int,
    child_bit: int,
    transition: dict[str, object],
    event: dict[str, object],
) -> dict[str, object]:
    pressure_step = int(event["step"])
    required_steps = max(parent_depth + 1, pressure_step)
    parent_states, parent_parities = trajectory(parent, required_steps)
    child_states, child_parities = trajectory(child, required_steps)
    child_odd_counts = odd_prefix_counts(child_parities)

    affine_failures = []
    for step in range(parent_depth + 1):
        predicted_delta = (3 ** child_odd_counts[step]) * (1 << (parent_depth - step))
        actual_delta = child_states[step] - parent_states[step]
        if actual_delta != predicted_delta:
            affine_failures.append({"step": step, "actual": actual_delta, "predicted": predicted_delta})

    last = event.get("last_credit_event")
    last_event = {} if last is None else dict(last)
    last_step = None if not last_event else int(last_event["step"])
    last_align = None if "align" not in last_event else int(last_event["align"])
    local_word = ""
    if last_step is not None:
        local_word = parity_word(child_parities[last_step:pressure_step])

    boundary_pair = f"{'O' if parent_parities[parent_depth] else 'E'}->{'O' if child_parities[parent_depth] else 'E'}"
    required_above_parent = int(event["required"]) - int(transition["parent_required"])
    surplus = int(event["credit"]) - int(event["required"])
    regime = classify_pressure_unit(event)
    return {
        "parent_depth": parent_depth,
        "child_depth": parent_depth + 1,
        "parent": parent,
        "child": child,
        "child_bit": child_bit,
        "boundary_pair": boundary_pair,
        "boundary_parent_state": parent_states[parent_depth],
        "boundary_child_state": child_states[parent_depth],
        "boundary_delta": child_states[parent_depth] - parent_states[parent_depth],
        "boundary_delta_power3": 3 ** child_odd_counts[parent_depth],
        "parities_shared_before_depth": parent_parities[:parent_depth] == child_parities[:parent_depth],
        "affine_lift_law_holds_to_depth": not affine_failures,
        "affine_failure_count": len(affine_failures),
        "first_event": event["event"],
        "regime": regime,
        "pressure_step": pressure_step,
        "step_offset_from_parent_depth": pressure_step - parent_depth,
        "pressure_state": event["state"],
        "parent_required": transition["parent_required"],
        "child_required": transition["child_required"],
        "required_delta": transition["required_delta"],
        "credit_delta": transition["credit_delta"],
        "required": event["required"],
        "required_above_parent": required_above_parent,
        "credit": event["credit"],
        "surplus": surplus,
        "last_credit_kind": last_event.get("kind"),
        "last_credit_step": last_step,
        "last_credit_align": last_align,
        "last_credit_state": last_event.get("state"),
        "lag_from_credit": None if last_step is None else pressure_step - last_step,
        "lag_minus_align": (
            None if last_step is None or last_align is None else pressure_step - last_step - last_align
        ),
        "local_word_from_credit_to_pressure": local_word if local_word else "<none>",
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
    first_count = 0
    positive_pressure_count = 0

    boundary_counts: Counter[str] = Counter()
    boundary_by_surplus: Counter[str] = Counter()
    boundary_by_offset: Counter[str] = Counter()
    boundary_by_regime: Counter[str] = Counter()
    offset_by_surplus: Counter[str] = Counter()
    local_word_counts: Counter[str] = Counter()
    local_word_by_surplus: Counter[str] = Counter()
    align_by_surplus: Counter[str] = Counter()
    regime_by_surplus: Counter[str] = Counter()
    surplus_counts: Counter[int] = Counter()
    offset_counts: Counter[int] = Counter()
    event_counts: Counter[str] = Counter()

    affine_failures: list[dict[str, object]] = []
    unshared_prefix_examples: list[dict[str, object]] = []
    surplus_one_examples: list[dict[str, object]] = []
    boundary_examples: list[dict[str, object]] = []
    tightest_examples: list[dict[str, object]] = []

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

            first_count += 1
            record = compact_boundary_record(
                parent_depth=parent_depth,
                parent=parent,
                child=child,
                child_bit=int(transition["child_bit"]),
                transition=transition,
                event=first,
            )

            boundary = str(record["boundary_pair"])
            surplus = int(record["surplus"])
            offset = int(record["step_offset_from_parent_depth"])
            regime = str(record["regime"])
            local_word = str(record["local_word_from_credit_to_pressure"])
            align = record["last_credit_align"]

            boundary_counts[boundary] += 1
            boundary_by_surplus[f"{surplus}:{boundary}"] += 1
            boundary_by_offset[f"{offset}:{boundary}"] += 1
            boundary_by_regime[f"{regime}:{boundary}"] += 1
            offset_by_surplus[f"{surplus}:{offset}"] += 1
            local_word_counts[local_word] += 1
            local_word_by_surplus[f"{surplus}:{local_word}"] += 1
            align_by_surplus[f"{surplus}:{align}"] += 1
            regime_by_surplus[f"{surplus}:{regime}"] += 1
            surplus_counts[surplus] += 1
            offset_counts[offset] += 1
            event_counts[str(record["first_event"])] += 1

            keep_smallest(tightest_examples, record, args.top_n)
            if surplus == 1:
                surplus_one_examples.append(record)
            if boundary not in {str(row["boundary_pair"]) for row in boundary_examples}:
                boundary_examples.append(record)
            if not bool(record["affine_lift_law_holds_to_depth"]):
                affine_failures.append(record)
            if not bool(record["parities_shared_before_depth"]):
                unshared_prefix_examples.append(record)

    return {
        "status": "branch-prefix-retimed-boundary-classifier-depth",
        "elapsed_seconds": round_float(perf_counter() - started, 6),
        "parent_depth": parent_depth,
        "child_depth": child_depth,
        "frontiers": {
            "parent": {**parent_stats, "positive_live_count": len(parent_leaves), "depth": parent_depth},
            "child": {**child_stats, "positive_live_count": len(child_leaves), "depth": child_depth},
        },
        "positive_pressure_transition_count": positive_pressure_count,
        "retimed_transition_count": retimed_count,
        "first_threshold_count": first_count,
        "boundary_counts": as_counter_dict(boundary_counts),
        "boundary_by_surplus": as_counter_dict(boundary_by_surplus),
        "boundary_by_offset": as_counter_dict(boundary_by_offset),
        "boundary_by_regime": as_counter_dict(boundary_by_regime),
        "offset_by_surplus": as_counter_dict(offset_by_surplus),
        "local_word_counts": as_counter_dict(local_word_counts),
        "local_word_by_surplus": as_counter_dict(local_word_by_surplus),
        "align_by_surplus": as_counter_dict(align_by_surplus),
        "regime_by_surplus": as_counter_dict(regime_by_surplus),
        "surplus_histogram": as_counter_dict(surplus_counts),
        "offset_histogram": as_counter_dict(offset_counts),
        "event_counts": as_counter_dict(event_counts),
        "checks": {
            "all_first_thresholds_present": first_count == retimed_count,
            "all_affine_lift_law_holds_to_depth": not affine_failures,
            "all_parities_shared_before_depth": not unshared_prefix_examples,
            "all_boundary_pairs_opposite": set(boundary_counts) <= {"E->O", "O->E"},
            "all_surplus_one_cases_are_e_to_o": all(
                str(record["boundary_pair"]) == "E->O" for record in surplus_one_examples
            ),
            "all_surplus_one_cases_offset_one": all(
                int(record["step_offset_from_parent_depth"]) == 1 for record in surplus_one_examples
            ),
            "all_surplus_one_cases_align_three": all(
                int(record["last_credit_align"]) == 3 for record in surplus_one_examples
            ),
            "all_surplus_one_cases_known_words": all(
                str(record["local_word_from_credit_to_pressure"]) in {"OOO", "OOOEOO"}
                for record in surplus_one_examples
            ),
        },
        "tightest_examples": tightest_examples,
        "surplus_one_examples": surplus_one_examples[: args.top_n],
        "boundary_examples": boundary_examples[: args.top_n],
        "affine_failure_examples": affine_failures[: args.top_n],
        "unshared_prefix_examples": unshared_prefix_examples[: args.top_n],
    }


def merge_counter(rows: list[dict[str, object]], key: str) -> dict[str, int]:
    counter: Counter[str] = Counter()
    for row in rows:
        counter.update({str(k): int(v) for k, v in dict(row[key]).items()})
    return as_counter_dict(counter)


def run(args: argparse.Namespace) -> dict[str, object]:
    rows = []
    compact_rows = []
    for depth in range(args.min_parent_depth, args.max_parent_depth + 1):
        payload = analyze_depth(args, depth)
        rows.append(payload)
        compact_rows.append(
            {
                "parent_depth": payload["parent_depth"],
                "child_depth": payload["child_depth"],
                "positive_pressure_transition_count": payload["positive_pressure_transition_count"],
                "retimed_transition_count": payload["retimed_transition_count"],
                "first_threshold_count": payload["first_threshold_count"],
                "boundary_counts": payload["boundary_counts"],
                "surplus_histogram": payload["surplus_histogram"],
                "offset_histogram": payload["offset_histogram"],
                "checks": payload["checks"],
            }
        )

    claim_names = sorted({claim for row in rows for claim in dict(row["checks"])})
    surplus_one_records = [
        record
        for row in rows
        for record in list(row["surplus_one_examples"])
    ]
    return {
        "status": "branch-prefix-retimed-boundary-classifier",
        "parameters": {
            "min_parent_depth": args.min_parent_depth,
            "max_parent_depth": args.max_parent_depth,
            "max_depth": args.max_depth,
            "max_steps": args.max_steps,
            "top_n": args.top_n,
        },
        "depths": compact_rows,
        "checks": {
            "total_retimed_transitions": sum(int(row["retimed_transition_count"]) for row in rows),
            "total_first_thresholds": sum(int(row["first_threshold_count"]) for row in rows),
            "all_depth_checks": {
                claim: all(bool(dict(row["checks"]).get(claim, False)) for row in rows)
                for claim in claim_names
            },
        },
        "counts": {
            "boundary_counts": merge_counter(rows, "boundary_counts"),
            "boundary_by_surplus": merge_counter(rows, "boundary_by_surplus"),
            "boundary_by_offset": merge_counter(rows, "boundary_by_offset"),
            "boundary_by_regime": merge_counter(rows, "boundary_by_regime"),
            "offset_by_surplus": merge_counter(rows, "offset_by_surplus"),
            "local_word_counts": merge_counter(rows, "local_word_counts"),
            "local_word_by_surplus": merge_counter(rows, "local_word_by_surplus"),
            "align_by_surplus": merge_counter(rows, "align_by_surplus"),
            "regime_by_surplus": merge_counter(rows, "regime_by_surplus"),
            "surplus_histogram": merge_counter(rows, "surplus_histogram"),
            "offset_histogram": merge_counter(rows, "offset_histogram"),
            "event_counts": merge_counter(rows, "event_counts"),
        },
        "surplus_one_examples": surplus_one_records[: args.top_n],
        "boundary_examples": [
            record
            for row in rows
            for record in list(row["boundary_examples"])
        ][: args.top_n],
        "tightest_examples": [
            record
            for row in rows
            for record in list(row["tightest_examples"])
        ][: args.top_n],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--min-parent-depth", type=int, default=18)
    parser.add_argument("--max-parent-depth", type=int, default=25)
    parser.add_argument("--max-depth", type=int, default=1024)
    parser.add_argument("--max-steps", type=int, default=50000)
    parser.add_argument("--top-n", type=int, default=12)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    if args.min_parent_depth < 1:
        raise SystemExit("--min-parent-depth must be positive")
    if args.max_parent_depth < args.min_parent_depth:
        raise SystemExit("--max-parent-depth must be >= --min-parent-depth")
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

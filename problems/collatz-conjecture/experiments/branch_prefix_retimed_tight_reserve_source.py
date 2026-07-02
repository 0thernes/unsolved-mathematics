#!/usr/bin/env python3
"""Mine the source of inherited reserve before the final align-3 entry.

The tight credit-floor identity reduces the align-3 local-grammar near-misses
to a pre-entry reserve question.  This script records the full credit-event
history before the final align-3 high-ladder entry, including the required
credit immediately before that entry.

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
    min_credit_required,
    odd3_macro_info,
    powers_of_three,
    round_float,
    shortcut_step,
    update_excess,
    v2,
)
from branch_prefix_dominance_analyzer import analyze_prefix_start
from branch_prefix_retimed_boundary_classifier import compact_boundary_record
from branch_prefix_retimed_post_ladder_tail import as_counter_dict
from branch_prefix_retimed_pressure import transition_row
from branch_prefix_retimed_tight_grammar import enrich_record, tight_local_grammar


def trace_with_credit_events(start: int, parent_required: int, max_steps: int) -> dict[str, object]:
    original = int(start)
    current = original
    step = 0
    odd_steps = 0
    max_excess = 0.0
    final_excess = 0.0
    credit = 0
    previous_required = 0

    credit_events: list[dict[str, object]] = []
    pressure_events: list[dict[str, object]] = []
    last_credit_event: dict[str, object] | None = None
    first_required_above_parent: dict[str, object] | None = None

    def record_credit(kind: str, amount: int, state: int, align: int | None = None) -> None:
        nonlocal credit, last_credit_event
        required_before = min_credit_required(max_excess)
        event = {
            "kind": kind,
            "amount": amount,
            "credit_before": credit,
            "credit_after": credit + amount,
            "required_before": required_before,
            "reserve_vs_parent_before": credit - parent_required,
            "reserve_vs_current_before": credit - required_before,
            "parent_required_minus_current_required": parent_required - required_before,
            "step": step,
            "state": state,
        }
        if align is not None:
            event["align"] = align
        credit += amount
        credit_events.append(event)
        last_credit_event = event

    def observe(event: str) -> None:
        nonlocal previous_required, first_required_above_parent
        required = min_credit_required(max_excess)
        if required <= previous_required:
            return
        pressure_event = {
            "event": event,
            "step": step,
            "state": current,
            "odd_steps": odd_steps,
            "max_excess": round_float(max_excess),
            "required": required,
            "credit": credit,
            "surplus": credit - required,
            "last_credit_event": last_credit_event,
            "credit_event_count": len(credit_events),
        }
        pressure_events.append(pressure_event)
        if first_required_above_parent is None and required > parent_required:
            first_required_above_parent = pressure_event
        previous_required = required

    observe("start")
    while step < max_steps and current > 1:
        if current < original and step >= 3:
            break

        if current & 1:
            align = v2(current + 1)
            if align >= 3:
                record_credit("high_ladder", align - 2, current, align)
                observe("enter_high_ladder")

                for _ in range(align):
                    current, parity = shortcut_step(current)
                    step += 1
                    odd_steps += parity
                    final_excess, max_excess = update_excess(odd_steps, step, max_excess)
                    observe("high_ladder_step")
                    if step >= max_steps:
                        break

                while step < max_steps and current > 1 and current % 2 == 0:
                    current, parity = shortcut_step(current)
                    step += 1
                    final_excess, max_excess = update_excess(odd_steps, step, max_excess)
                    observe("post_ladder_even_step")
                    if current < original and step >= 3:
                        break
                continue

            if current % 8 == 3:
                info = odd3_macro_info(current)
                if str(info["branch"]) == "repeat_minus5_gate":
                    record_credit("low_repeat", 1, current, int(info["minus5_align"]))
                    observe("enter_low_repeat_gate")

        current, parity = shortcut_step(current)
        step += 1
        odd_steps += parity
        final_excess, max_excess = update_excess(odd_steps, step, max_excess)
        observe("ordinary_step")

    return {
        "start": original,
        "certified": current < original,
        "escape_d": step,
        "odd_steps": odd_steps,
        "max_excess": round_float(max_excess),
        "final_excess": round_float(final_excess),
        "credit_events": credit_events,
        "pressure_events": pressure_events,
        "first_required_above_parent": first_required_above_parent,
    }


def keep_smallest(records: list[dict[str, object]], record: dict[str, object], top_n: int) -> None:
    records.append(record)
    records.sort(
        key=lambda row: (
            int(row["inherited_reserve_before_entry"]),
            int(row["parent_required_minus_entry_required"]),
            int(row["parent_depth"]),
            int(row["child"]),
        )
    )
    del records[top_n:]


def enrich_source_record(record: dict[str, object], trace: dict[str, object]) -> dict[str, object]:
    credit_events = list(trace["credit_events"])
    final_index = None
    for index, event in enumerate(credit_events):
        if int(event["step"]) == int(record["last_credit_step"]) and int(event["state"]) == int(record["last_credit_state"]):
            final_index = index
            break
    if final_index is None:
        raise ValueError("final credit event not found")

    final_event = dict(credit_events[final_index])
    previous_event = None if final_index == 0 else dict(credit_events[final_index - 1])
    prior_events = credit_events[:final_index]

    credit_before = int(final_event["credit_before"])
    entry_required = int(final_event["required_before"])
    parent_required = int(record["parent_required"])
    inherited_reserve = credit_before - parent_required
    reserve_vs_current = credit_before - entry_required
    parent_gap = parent_required - entry_required

    record = dict(record)
    record.update(
        {
            "final_credit_event_index": final_index + 1,
            "prior_credit_event_count": final_index,
            "prior_high_ladder_count": sum(1 for event in prior_events if str(event["kind"]) == "high_ladder"),
            "prior_low_repeat_count": sum(1 for event in prior_events if str(event["kind"]) == "low_repeat"),
            "entry_required_before_final_credit": entry_required,
            "inherited_reserve_before_entry": inherited_reserve,
            "reserve_vs_current_required_before_entry": reserve_vs_current,
            "parent_required_minus_entry_required": parent_gap,
            "inherited_reserve_identity_holds": inherited_reserve == reserve_vs_current - parent_gap,
            "previous_credit_kind": None if previous_event is None else previous_event["kind"],
            "previous_credit_amount": None if previous_event is None else previous_event["amount"],
            "previous_credit_align": None if previous_event is None else previous_event.get("align"),
            "previous_credit_step": None if previous_event is None else previous_event["step"],
            "previous_credit_state": None if previous_event is None else previous_event["state"],
            "previous_gap_to_entry": (
                None if previous_event is None else int(record["entry_step"]) - int(previous_event["step"])
            ),
            "previous_reserve_vs_parent_after": (
                None if previous_event is None else int(previous_event["credit_after"]) - parent_required
            ),
            "previous_reserve_vs_current_after": (
                None if previous_event is None else int(previous_event["credit_after"]) - int(previous_event["required_before"])
            ),
        }
    )
    return record


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
    local_count = 0

    counters: dict[str, Counter[str]] = {
        "inherited_reserve": Counter(),
        "reserve_vs_current_required": Counter(),
        "parent_required_minus_entry_required": Counter(),
        "entry_required": Counter(),
        "prior_credit_event_count": Counter(),
        "prior_high_ladder_count": Counter(),
        "prior_low_repeat_count": Counter(),
        "previous_credit_kind": Counter(),
        "previous_credit_amount": Counter(),
        "previous_credit_align": Counter(),
        "previous_gap_to_entry": Counter(),
        "previous_reserve_vs_parent_after": Counter(),
        "word_by_reserve": Counter(),
        "q_mod_16_by_reserve": Counter(),
    }

    source_records: list[dict[str, object]] = []
    minimal_examples: list[dict[str, object]] = []
    near_miss_examples: list[dict[str, object]] = []
    trace_mismatches: list[dict[str, object]] = []
    identity_failures: list[dict[str, object]] = []
    negative_current_reserve: list[dict[str, object]] = []
    no_prior_credit: list[dict[str, object]] = []

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
            trace = trace_with_credit_events(child, parent_required, args.max_steps)
            first = trace["first_required_above_parent"]
            if first is None:
                continue
            first = dict(first)
            first_count += 1

            record = compact_boundary_record(
                parent_depth=parent_depth,
                parent=parent,
                child=child,
                child_bit=int(transition["child_bit"]),
                transition=transition,
                event=first,
            )
            record = enrich_record(record)
            if not tight_local_grammar(record):
                continue

            local_count += 1
            record = enrich_source_record(record, trace)
            source_records.append(record)

            if int(first["step"]) != int(record["pressure_step"]) or int(first["state"]) != int(record["pressure_state"]):
                trace_mismatches.append(record)
            if not bool(record["inherited_reserve_identity_holds"]):
                identity_failures.append(record)
            if int(record["reserve_vs_current_required_before_entry"]) < 0:
                negative_current_reserve.append(record)
            if int(record["prior_credit_event_count"]) <= 0:
                no_prior_credit.append(record)

            reserve = int(record["inherited_reserve_before_entry"])
            counters["inherited_reserve"][str(reserve)] += 1
            counters["reserve_vs_current_required"][str(record["reserve_vs_current_required_before_entry"])] += 1
            counters["parent_required_minus_entry_required"][str(record["parent_required_minus_entry_required"])] += 1
            counters["entry_required"][str(record["entry_required_before_final_credit"])] += 1
            counters["prior_credit_event_count"][str(record["prior_credit_event_count"])] += 1
            counters["prior_high_ladder_count"][str(record["prior_high_ladder_count"])] += 1
            counters["prior_low_repeat_count"][str(record["prior_low_repeat_count"])] += 1
            counters["previous_credit_kind"][str(record["previous_credit_kind"])] += 1
            counters["previous_credit_amount"][str(record["previous_credit_amount"])] += 1
            counters["previous_credit_align"][str(record["previous_credit_align"])] += 1
            counters["previous_gap_to_entry"][str(record["previous_gap_to_entry"])] += 1
            counters["previous_reserve_vs_parent_after"][str(record["previous_reserve_vs_parent_after"])] += 1
            counters["word_by_reserve"][f"{reserve}:{record['local_word_from_credit_to_pressure']}"] += 1
            counters["q_mod_16_by_reserve"][f"{reserve}:{record['q_mod_16']}"] += 1

            if reserve == 1:
                keep_smallest(minimal_examples, record, args.top_n)
            else:
                keep_smallest(near_miss_examples, record, args.top_n)

    return {
        "status": "branch-prefix-retimed-tight-reserve-source-depth",
        "elapsed_seconds": round_float(perf_counter() - started, 6),
        "parent_depth": parent_depth,
        "child_depth": child_depth,
        "frontiers": {
            "parent": {**parent_stats, "positive_live_count": len(parent_leaves), "depth": parent_depth},
            "child": {**child_stats, "positive_live_count": len(child_leaves), "depth": child_depth},
        },
        "retimed_transition_count": retimed_count,
        "first_threshold_count": first_count,
        "local_grammar_count": local_count,
        "counters": {key: as_counter_dict(counter) for key, counter in counters.items()},
        "checks": {
            "all_first_thresholds_present": first_count == retimed_count,
            "all_trace_first_events_match_records": not trace_mismatches,
            "all_inherited_reserve_identities_hold": not identity_failures,
            "all_reserve_vs_current_required_nonnegative": not negative_current_reserve,
            "all_local_records_have_prior_credit": not no_prior_credit,
        },
        "minimal_examples": minimal_examples,
        "near_miss_examples": near_miss_examples,
        "trace_mismatches": trace_mismatches[: args.top_n],
        "identity_failures": identity_failures[: args.top_n],
        "negative_current_reserve_examples": negative_current_reserve[: args.top_n],
        "no_prior_credit_examples": no_prior_credit[: args.top_n],
    }


def merge_counter(rows: list[dict[str, object]], key: str) -> dict[str, int]:
    counter: Counter[str] = Counter()
    for row in rows:
        counter.update({str(k): int(v) for k, v in dict(dict(row["counters"])[key]).items()})
    return as_counter_dict(counter)


def merge_records(rows: list[dict[str, object]], key: str, top_n: int) -> list[dict[str, object]]:
    records = [record for row in rows for record in list(row[key])]
    records.sort(
        key=lambda row: (
            int(row["inherited_reserve_before_entry"]),
            int(row["parent_required_minus_entry_required"]),
            int(row["parent_depth"]),
            int(row["child"]),
        )
    )
    return records[:top_n]


def run(args: argparse.Namespace) -> dict[str, object]:
    rows = [analyze_depth(args, depth) for depth in range(args.min_parent_depth, args.max_parent_depth + 1)]
    claim_names = sorted({claim for row in rows for claim in dict(row["checks"])})
    counter_names = sorted({name for row in rows for name in dict(row["counters"])})
    return {
        "status": "branch-prefix-retimed-tight-reserve-source",
        "parameters": {
            "min_parent_depth": args.min_parent_depth,
            "max_parent_depth": args.max_parent_depth,
            "max_depth": args.max_depth,
            "max_steps": args.max_steps,
            "top_n": args.top_n,
        },
        "depths": [
            {
                "parent_depth": row["parent_depth"],
                "child_depth": row["child_depth"],
                "retimed_transition_count": row["retimed_transition_count"],
                "first_threshold_count": row["first_threshold_count"],
                "local_grammar_count": row["local_grammar_count"],
                "checks": row["checks"],
                "counters": row["counters"],
            }
            for row in rows
        ],
        "checks": {
            "total_retimed_transitions": sum(int(row["retimed_transition_count"]) for row in rows),
            "total_first_thresholds": sum(int(row["first_threshold_count"]) for row in rows),
            "total_local_grammar_records": sum(int(row["local_grammar_count"]) for row in rows),
            "all_depth_checks": {
                claim: all(bool(dict(row["checks"]).get(claim, False)) for row in rows) for claim in claim_names
            },
        },
        "counters": {name: merge_counter(rows, name) for name in counter_names},
        "minimal_examples": merge_records(rows, "minimal_examples", args.top_n),
        "near_miss_examples": merge_records(rows, "near_miss_examples", args.top_n),
        "trace_mismatches": merge_records(rows, "trace_mismatches", args.top_n),
        "identity_failures": merge_records(rows, "identity_failures", args.top_n),
        "negative_current_reserve_examples": merge_records(rows, "negative_current_reserve_examples", args.top_n),
        "no_prior_credit_examples": merge_records(rows, "no_prior_credit_examples", args.top_n),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--min-parent-depth", type=int, default=18)
    parser.add_argument("--max-parent-depth", type=int, default=25)
    parser.add_argument("--max-depth", type=int, default=1024)
    parser.add_argument("--max-steps", type=int, default=50000)
    parser.add_argument("--top-n", type=int, default=12)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--quiet", action="store_true", help="write output without printing the JSON payload")
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
    if not args.quiet:
        print(text)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Analyze the inherited-credit floor inside the retimed tight grammar.

The tight grammar selector showed that align-3 OOO/OOOEOO local grammar is
necessary but not sufficient for surplus-one first thresholds.  This script
splits the pressure surplus into:

    inherited reserve before the final align-3 credit
    plus local credit amount
    minus the new required layer.

For the checked local grammar, the final align-3 high-ladder credit amount and
the new required layer are both one.  Thus pressure surplus equals inherited
reserve.  The output verifies this identity and records the exact near-miss
reserve distribution.
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
from branch_prefix_retimed_boundary_classifier import compact_boundary_record
from branch_prefix_retimed_post_ladder_tail import as_counter_dict
from branch_prefix_retimed_pressure import pressure_trace, transition_row
from branch_prefix_retimed_tight_grammar import enrich_record, tight_local_grammar


def keep_smallest(records: list[dict[str, object]], record: dict[str, object], top_n: int) -> None:
    records.append(record)
    records.sort(
        key=lambda row: (
            int(row["inherited_reserve_before_entry"]),
            int(row["parent_depth"]),
            int(row["child"]),
        )
    )
    del records[top_n:]


def enrich_credit_floor(record: dict[str, object], event: dict[str, object]) -> dict[str, object]:
    last = dict(event["last_credit_event"])
    last_amount = int(last["amount"])
    last_credit_after = int(last["credit_after"])
    credit_before_last = last_credit_after - last_amount
    parent_required = int(record["parent_required"])
    required_above_parent = int(record["required_above_parent"])
    pressure_surplus = int(record["surplus"])
    inherited_reserve = credit_before_last - parent_required
    local_balance = last_amount - required_above_parent

    record = dict(record)
    record.update(
        {
            "last_credit_amount": last_amount,
            "last_credit_after": last_credit_after,
            "credit_before_last": credit_before_last,
            "required_above_parent": required_above_parent,
            "inherited_reserve_before_entry": inherited_reserve,
            "local_credit_minus_new_required": local_balance,
            "predicted_pressure_surplus": inherited_reserve + local_balance,
            "surplus_identity_holds": pressure_surplus == inherited_reserve + local_balance,
            "is_minimal_inherited_reserve": inherited_reserve == 1,
            "is_credit_three_edge": int(record["credit"]) == 3,
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
    minimal_reserve_count = 0
    credit_three_count = 0

    counters: dict[str, Counter[str]] = {
        "pressure_surplus": Counter(),
        "inherited_reserve": Counter(),
        "credit_before_last": Counter(),
        "parent_required": Counter(),
        "required_above_parent": Counter(),
        "last_credit_amount": Counter(),
        "local_balance": Counter(),
        "word_by_reserve": Counter(),
        "depth_by_reserve": Counter(),
        "parent_required_by_reserve": Counter(),
        "q_mod_16_by_reserve": Counter(),
        "tail_by_reserve": Counter(),
    }

    identity_failures: list[dict[str, object]] = []
    non_unit_local_balance: list[dict[str, object]] = []
    minimal_reserve_non_surplus_one: list[dict[str, object]] = []
    credit_three_non_minimal: list[dict[str, object]] = []
    minimal_examples: list[dict[str, object]] = []
    near_miss_examples: list[dict[str, object]] = []

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
            record = enrich_record(record)
            if not tight_local_grammar(record):
                continue
            local_count += 1
            record = enrich_credit_floor(record, first)

            reserve = int(record["inherited_reserve_before_entry"])
            pressure_surplus = int(record["surplus"])
            credit_before_last = int(record["credit_before_last"])
            parent_req = int(record["parent_required"])
            required_above_parent = int(record["required_above_parent"])
            last_amount = int(record["last_credit_amount"])
            local_balance = int(record["local_credit_minus_new_required"])
            word = str(record["local_word_from_credit_to_pressure"])
            tail = str(record["tail_after_ladder"])
            q_mod = str(record["q_mod_16"])

            counters["pressure_surplus"][str(pressure_surplus)] += 1
            counters["inherited_reserve"][str(reserve)] += 1
            counters["credit_before_last"][str(credit_before_last)] += 1
            counters["parent_required"][str(parent_req)] += 1
            counters["required_above_parent"][str(required_above_parent)] += 1
            counters["last_credit_amount"][str(last_amount)] += 1
            counters["local_balance"][str(local_balance)] += 1
            counters["word_by_reserve"][f"{reserve}:{word}"] += 1
            counters["depth_by_reserve"][f"{reserve}:{parent_depth}"] += 1
            counters["parent_required_by_reserve"][f"{reserve}:{parent_req}"] += 1
            counters["q_mod_16_by_reserve"][f"{reserve}:{q_mod}"] += 1
            counters["tail_by_reserve"][f"{reserve}:{tail}"] += 1

            if reserve == 1:
                minimal_reserve_count += 1
                keep_smallest(minimal_examples, record, args.top_n)
            elif reserve > 1:
                keep_smallest(near_miss_examples, record, args.top_n)

            if int(record["credit"]) == 3:
                credit_three_count += 1
            if not bool(record["surplus_identity_holds"]):
                identity_failures.append(record)
            if local_balance != 0:
                non_unit_local_balance.append(record)
            if reserve == 1 and pressure_surplus != 1:
                minimal_reserve_non_surplus_one.append(record)
            if int(record["credit"]) == 3 and reserve != 1:
                credit_three_non_minimal.append(record)

    return {
        "status": "branch-prefix-retimed-tight-credit-floor-depth",
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
        "minimal_inherited_reserve_count": minimal_reserve_count,
        "credit_three_count": credit_three_count,
        "counters": {key: as_counter_dict(counter) for key, counter in counters.items()},
        "checks": {
            "all_first_thresholds_present": first_count == retimed_count,
            "all_local_surplus_identities_hold": not identity_failures,
            "all_local_credit_amounts_match_new_required_layer": not non_unit_local_balance,
            "minimal_inherited_reserve_is_surplus_one": not minimal_reserve_non_surplus_one,
            "credit_three_implies_minimal_inherited_reserve": not credit_three_non_minimal,
            "minimal_inherited_reserve_count_equals_credit_three_count": minimal_reserve_count == credit_three_count,
        },
        "minimal_examples": minimal_examples,
        "near_miss_examples": near_miss_examples,
        "identity_failures": identity_failures[: args.top_n],
        "non_unit_local_balance_examples": non_unit_local_balance[: args.top_n],
        "minimal_reserve_non_surplus_one_examples": minimal_reserve_non_surplus_one[: args.top_n],
        "credit_three_non_minimal_examples": credit_three_non_minimal[: args.top_n],
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
        "status": "branch-prefix-retimed-tight-credit-floor",
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
                "minimal_inherited_reserve_count": row["minimal_inherited_reserve_count"],
                "credit_three_count": row["credit_three_count"],
                "checks": row["checks"],
                "counters": row["counters"],
            }
            for row in rows
        ],
        "checks": {
            "total_retimed_transitions": sum(int(row["retimed_transition_count"]) for row in rows),
            "total_first_thresholds": sum(int(row["first_threshold_count"]) for row in rows),
            "total_local_grammar_records": sum(int(row["local_grammar_count"]) for row in rows),
            "total_minimal_inherited_reserve_records": sum(
                int(row["minimal_inherited_reserve_count"]) for row in rows
            ),
            "total_credit_three_records": sum(int(row["credit_three_count"]) for row in rows),
            "all_depth_checks": {
                claim: all(bool(dict(row["checks"]).get(claim, False)) for row in rows) for claim in claim_names
            },
        },
        "counters": {name: merge_counter(rows, name) for name in counter_names},
        "minimal_examples": merge_records(rows, "minimal_examples", args.top_n),
        "near_miss_examples": merge_records(rows, "near_miss_examples", args.top_n),
        "identity_failures": merge_records(rows, "identity_failures", args.top_n),
        "non_unit_local_balance_examples": merge_records(rows, "non_unit_local_balance_examples", args.top_n),
        "minimal_reserve_non_surplus_one_examples": merge_records(
            rows, "minimal_reserve_non_surplus_one_examples", args.top_n
        ),
        "credit_three_non_minimal_examples": merge_records(rows, "credit_three_non_minimal_examples", args.top_n),
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

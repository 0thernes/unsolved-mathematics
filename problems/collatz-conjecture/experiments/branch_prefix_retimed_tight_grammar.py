#!/usr/bin/env python3
"""Classify the local grammar around tight retimed first thresholds.

Earlier retimed analyzers isolated five surplus-one first thresholds.  This
script asks a sharper falsifiable question: can local features that do not use
the surplus value itself pick out the same five records?

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
from branch_prefix_retimed_boundary_classifier import compact_boundary_record, parity_word, trajectory
from branch_prefix_retimed_post_ladder_tail import as_counter_dict
from branch_prefix_retimed_pressure import pressure_trace, transition_row


KNOWN_TIGHT_WORDS = {"OOO", "OOOEOO"}


def high_ladder_q(state: int, align: int | None) -> int | None:
    if align is None or align < 0:
        return None
    if v2(state + 1) != align:
        return None
    return (state + 1) >> align


def enrich_record(record: dict[str, object]) -> dict[str, object]:
    parent_depth = int(record["parent_depth"])
    pressure_step = int(record["pressure_step"])
    last_step = record["last_credit_step"]
    last_align = record["last_credit_align"]
    last_state = record["last_credit_state"]

    parent_states, parent_parities = trajectory(int(record["parent"]), pressure_step)
    child_states, child_parities = trajectory(int(record["child"]), pressure_step)

    entry_step = None if last_step is None else int(last_step)
    align = None if last_align is None else int(last_align)
    entry_state = None if last_state is None else int(last_state)
    q = high_ladder_q(entry_state, align) if entry_state is not None else None
    terminal_step = None if entry_step is None or align is None else entry_step + align
    terminal_state = None
    tail_after_ladder = "<none>"
    if terminal_step is not None and terminal_step <= pressure_step:
        terminal_state = child_states[terminal_step]
        tail_after_ladder = parity_word(child_parities[terminal_step:pressure_step]) or "<active>"

    expected_terminal = None
    terminal_formula_matches = None
    if q is not None and align is not None:
        expected_terminal = (3**align) * q - 1
        terminal_formula_matches = expected_terminal == terminal_state

    record = dict(record)
    record.update(
        {
            "entry_step": entry_step,
            "entry_offset_from_parent_depth": None if entry_step is None else entry_step - parent_depth,
            "boundary_index_from_entry": None if entry_step is None else parent_depth - entry_step,
            "parent_entry_state": None if entry_step is None else parent_states[entry_step],
            "child_entry_state": None if entry_step is None else child_states[entry_step],
            "parent_entry_mod_16": None if entry_step is None else parent_states[entry_step] % 16,
            "child_entry_mod_16": None if entry_step is None else child_states[entry_step] % 16,
            "child_entry_align": None if entry_state is None else v2(entry_state + 1),
            "q": q,
            "q_mod_16": None if q is None else q % 16,
            "terminal_step": terminal_step,
            "terminal_offset_from_parent_depth": None if terminal_step is None else terminal_step - parent_depth,
            "terminal_state": terminal_state,
            "terminal_mod_16": None if terminal_state is None else terminal_state % 16,
            "expected_terminal_from_entry": expected_terminal,
            "terminal_formula_matches": terminal_formula_matches,
            "tail_after_ladder": tail_after_ladder,
        }
    )
    return record


def tight_local_grammar(record: dict[str, object]) -> bool:
    """A surplus-free selector suggested by the five tight records."""

    return all(
        (
            int(record["child_bit"]) == 1,
            str(record["boundary_pair"]) == "E->O",
            int(record["step_offset_from_parent_depth"]) == 1,
            str(record["last_credit_kind"]) == "high_ladder",
            int(record["last_credit_align"]) == 3,
            str(record["local_word_from_credit_to_pressure"]) in KNOWN_TIGHT_WORDS,
            int(record["entry_offset_from_parent_depth"]) in {-5, -2},
            int(record["child_entry_mod_16"]) == 7,
            bool(record["terminal_formula_matches"]),
        )
    )


def base_required_local_grammar(record: dict[str, object]) -> bool:
    """The local grammar plus the parent base-layer requirement."""

    return tight_local_grammar(record) and int(record["parent_required"]) == 1


def credit_three_local_grammar(record: dict[str, object]) -> bool:
    """The local grammar plus the minimal observed high-ladder credit."""

    return tight_local_grammar(record) and int(record["credit"]) == 3


FILTER_CHAIN = [
    ("upper_child", lambda row: int(row["child_bit"]) == 1),
    ("boundary_E_to_O", lambda row: str(row["boundary_pair"]) == "E->O"),
    ("pressure_at_d_plus_1", lambda row: int(row["step_offset_from_parent_depth"]) == 1),
    ("last_credit_high_ladder", lambda row: str(row["last_credit_kind"]) == "high_ladder"),
    ("align_3", lambda row: int(row["last_credit_align"]) == 3),
    ("known_tight_word", lambda row: str(row["local_word_from_credit_to_pressure"]) in KNOWN_TIGHT_WORDS),
    ("entry_offset_minus_2_or_minus_5", lambda row: int(row["entry_offset_from_parent_depth"]) in {-5, -2}),
    ("child_entry_7_mod_16", lambda row: int(row["child_entry_mod_16"]) == 7),
    ("terminal_formula_matches", lambda row: bool(row["terminal_formula_matches"])),
    ("credit_3", lambda row: int(row["credit"]) == 3),
]


def keep_smallest(records: list[dict[str, object]], record: dict[str, object], top_n: int) -> None:
    records.append(record)
    records.sort(
        key=lambda row: (
            int(row["surplus"]),
            int(row["parent_depth"]),
            int(row["child"]),
            int(row["pressure_step"]),
        )
    )
    del records[top_n:]


def summarize_records(records: list[dict[str, object]]) -> dict[str, object]:
    return {
        "count": len(records),
        "surplus_histogram": as_counter_dict(Counter(str(row["surplus"]) for row in records)),
        "depth_counts": as_counter_dict(Counter(str(row["parent_depth"]) for row in records)),
        "word_counts": as_counter_dict(Counter(str(row["local_word_from_credit_to_pressure"]) for row in records)),
        "entry_offset_counts": as_counter_dict(Counter(str(row["entry_offset_from_parent_depth"]) for row in records)),
        "q_mod_16_counts": as_counter_dict(Counter(str(row["q_mod_16"]) for row in records)),
        "tail_after_ladder_counts": as_counter_dict(Counter(str(row["tail_after_ladder"]) for row in records)),
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

    records: list[dict[str, object]] = []
    retimed_count = 0
    first_count = 0
    positive_pressure_count = 0

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
            records.append(enrich_record(record))

    local_selected = [row for row in records if tight_local_grammar(row)]
    base_selected = [row for row in records if base_required_local_grammar(row)]
    credit_three_selected = [row for row in records if credit_three_local_grammar(row)]
    surplus_one = [row for row in records if int(row["surplus"]) == 1]

    chain_rows = []
    current = list(records)
    for name, predicate in FILTER_CHAIN:
        current = [row for row in current if predicate(row)]
        chain_rows.append({"filter": name, **summarize_records(current)})

    return {
        "status": "branch-prefix-retimed-tight-grammar-depth",
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
        "summaries": {
            "all_first_thresholds": summarize_records(records),
            "surplus_one": summarize_records(surplus_one),
            "tight_local_grammar": summarize_records(local_selected),
            "base_required_local_grammar": summarize_records(base_selected),
            "credit_three_local_grammar": summarize_records(credit_three_selected),
        },
        "filter_chain": chain_rows,
        "checks": {
            "all_first_thresholds_present": first_count == retimed_count,
            "tight_local_grammar_selects_all_surplus_one": {
                f"{row['parent_depth']}:{row['parent']}:{row['child']}": tight_local_grammar(row)
                for row in surplus_one
            },
            "tight_local_grammar_has_no_non_surplus_one": all(int(row["surplus"]) == 1 for row in local_selected),
            "base_required_local_grammar_selects_all_surplus_one": {
                f"{row['parent_depth']}:{row['parent']}:{row['child']}": base_required_local_grammar(row)
                for row in surplus_one
            },
            "base_required_local_grammar_has_no_non_surplus_one": all(int(row["surplus"]) == 1 for row in base_selected),
            "credit_three_local_grammar_selects_all_surplus_one": {
                f"{row['parent_depth']}:{row['parent']}:{row['child']}": credit_three_local_grammar(row)
                for row in surplus_one
            },
            "credit_three_local_grammar_has_no_non_surplus_one": all(
                int(row["surplus"]) == 1 for row in credit_three_selected
            ),
        },
        "surplus_one_examples": surplus_one[: args.top_n],
        "tight_local_grammar_examples": local_selected[: args.top_n],
        "base_required_local_grammar_examples": base_selected[: args.top_n],
        "credit_three_local_grammar_examples": credit_three_selected[: args.top_n],
        "tight_local_grammar_non_surplus_one_examples": [
            row for row in local_selected if int(row["surplus"]) != 1
        ][: args.top_n],
    }


def merge_records(rows: list[dict[str, object]], key: str) -> list[dict[str, object]]:
    return [record for row in rows for record in list(row[key])]


def merge_filter_chain(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    merged = []
    for index, (name, _) in enumerate(FILTER_CHAIN):
        # Records are intentionally not retained in filter_chain, so merge counters directly.
        counter_keys = [
            "surplus_histogram",
            "depth_counts",
            "word_counts",
            "entry_offset_counts",
            "q_mod_16_counts",
            "tail_after_ladder_counts",
        ]
        merged_row: dict[str, object] = {"filter": name}
        count = 0
        for row in rows:
            chain_row = list(row["filter_chain"])[index]
            count += int(chain_row["count"])
            for counter_key in counter_keys:
                merged_row.setdefault(counter_key, Counter())
                dict_counter = dict(chain_row[counter_key])
                assert isinstance(merged_row[counter_key], Counter)
                merged_row[counter_key].update({str(k): int(v) for k, v in dict_counter.items()})
        merged_row["count"] = count
        for counter_key in counter_keys:
            counter = merged_row[counter_key]
            assert isinstance(counter, Counter)
            merged_row[counter_key] = as_counter_dict(counter)
        merged.append(merged_row)
    return merged


def merge_summary(rows: list[dict[str, object]], summary_key: str) -> dict[str, object]:
    counter_keys = [
        "surplus_histogram",
        "depth_counts",
        "word_counts",
        "entry_offset_counts",
        "q_mod_16_counts",
        "tail_after_ladder_counts",
    ]
    merged: dict[str, object] = {"count": 0}
    for counter_key in counter_keys:
        merged[counter_key] = Counter()
    for row in rows:
        summary = dict(dict(row["summaries"])[summary_key])
        merged["count"] = int(merged["count"]) + int(summary["count"])
        for counter_key in counter_keys:
            counter = merged[counter_key]
            assert isinstance(counter, Counter)
            counter.update({str(k): int(v) for k, v in dict(summary[counter_key]).items()})
    for counter_key in counter_keys:
        counter = merged[counter_key]
        assert isinstance(counter, Counter)
        merged[counter_key] = as_counter_dict(counter)
    return merged


def run(args: argparse.Namespace) -> dict[str, object]:
    rows = [analyze_depth(args, depth) for depth in range(args.min_parent_depth, args.max_parent_depth + 1)]
    surplus_one = merge_records(rows, "surplus_one_examples")
    local_selected = merge_records(rows, "tight_local_grammar_examples")
    base_selected = merge_records(rows, "base_required_local_grammar_examples")
    credit_three_selected = merge_records(rows, "credit_three_local_grammar_examples")
    local_non_surplus = merge_records(rows, "tight_local_grammar_non_surplus_one_examples")

    local_selects_all = all(
        all(bool(value) for value in dict(dict(row["checks"])["tight_local_grammar_selects_all_surplus_one"]).values())
        for row in rows
    )
    base_selects_all = all(
        all(
            bool(value)
            for value in dict(dict(row["checks"])["base_required_local_grammar_selects_all_surplus_one"]).values()
        )
        for row in rows
    )
    credit_three_selects_all = all(
        all(
            bool(value)
            for value in dict(dict(row["checks"])["credit_three_local_grammar_selects_all_surplus_one"]).values()
        )
        for row in rows
    )

    return {
        "status": "branch-prefix-retimed-tight-grammar",
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
                "summaries": row["summaries"],
                "checks": row["checks"],
            }
            for row in rows
        ],
        "global_filter_chain": merge_filter_chain(rows),
        "global_summaries": {
            "surplus_one": merge_summary(rows, "surplus_one"),
            "tight_local_grammar": merge_summary(rows, "tight_local_grammar"),
            "base_required_local_grammar": merge_summary(rows, "base_required_local_grammar"),
            "credit_three_local_grammar": merge_summary(rows, "credit_three_local_grammar"),
        },
        "checks": {
            "total_retimed_transitions": sum(int(row["retimed_transition_count"]) for row in rows),
            "total_first_thresholds": sum(int(row["first_threshold_count"]) for row in rows),
            "all_first_thresholds_present": all(bool(dict(row["checks"])["all_first_thresholds_present"]) for row in rows),
            "tight_local_grammar_selects_all_surplus_one": local_selects_all,
            "tight_local_grammar_has_no_non_surplus_one": all(
                bool(dict(row["checks"])["tight_local_grammar_has_no_non_surplus_one"]) for row in rows
            ),
            "base_required_local_grammar_selects_all_surplus_one": base_selects_all,
            "base_required_local_grammar_has_no_non_surplus_one": all(
                bool(dict(row["checks"])["base_required_local_grammar_has_no_non_surplus_one"]) for row in rows
            ),
            "credit_three_local_grammar_selects_all_surplus_one": credit_three_selects_all,
            "credit_three_local_grammar_has_no_non_surplus_one": all(
                bool(dict(row["checks"])["credit_three_local_grammar_has_no_non_surplus_one"]) for row in rows
            ),
        },
        "surplus_one_examples": surplus_one[: args.top_n],
        "tight_local_grammar_examples": local_selected[: args.top_n],
        "base_required_local_grammar_examples": base_selected[: args.top_n],
        "credit_three_local_grammar_examples": credit_three_selected[: args.top_n],
        "tight_local_grammar_non_surplus_one_examples": local_non_surplus[: args.top_n],
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

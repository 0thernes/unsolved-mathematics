#!/usr/bin/env python3
"""Analyze the exact residue grammar behind low-alignment descent.

The alignment dichotomy says starts with `max_align < 3` descend quickly, but
it does not explain why.  This script isolates the low-alignment mechanism.

For odd `x == 3 mod 8`, three shortcut steps satisfy

    T^3(x) = (9*x + 5) / 8.

The only residue class that reproduces another odd `3 mod 8` growth state is
`x == 59 mod 64`, i.e. `x == -5 mod 64`.  On that gate,

    v2(T^3(x) + 5) = v2(x + 5) - 3.

So the local low branch has a finite "minus-five rank" unless it exits to
ordinary descent or crosses into the high-alignment branch.  This is finite
evidence plus an executable residue ledger, not a proof of Collatz.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path
from time import perf_counter

from kick_repulsion_claim_audit import (
    TRANSFER_FAILURE_STARTS,
    starts_from_frontier,
    top_rows,
    unique_preserving_order,
)
from master_kick_rejection_lemma import get_hard_records, shortcut_step, v2
from repayment_envelope_scan import parse_ints, round_float
from terminal_residue_tree_sweep_analyzer import parse_offset_set


ODD3_RESIDUES = tuple(range(3, 64, 8))


def shortcut_iterate(x: int, steps: int) -> int:
    for _ in range(steps):
        x, _ = shortcut_step(x)
    return x


def odd3_macro_info(x: int) -> dict[str, object]:
    if not (x & 1) or x % 8 != 3:
        raise ValueError("odd3_macro_info expects an odd x == 3 mod 8")
    macro_value = (9 * x + 5) // 8
    if shortcut_iterate(x, 3) != macro_value:
        raise AssertionError("T^3 identity failed")

    h = v2(x + 5)
    h_after = v2(macro_value + 5)
    residue = x % 64
    if residue == 59:
        branch = "repeat_minus5_gate"
        exit_steps = 3
        exit_value = macro_value
    elif macro_value & 1 == 0:
        branch = "even_exit"
        exit_steps = 4
        exit_value = macro_value // 2
    elif macro_value % 8 == 7:
        branch = "to_high_alignment"
        exit_steps = 3
        exit_value = macro_value
    else:
        branch = "odd15_drop_exit"
        exit_steps = 5
        exit_value = (3 * macro_value + 1) // 4

    return {
        "x": x,
        "residue_mod_64": residue,
        "minus5_align": h,
        "macro_value": macro_value,
        "macro_value_mod_8": macro_value % 8,
        "minus5_align_after_macro": h_after,
        "branch": branch,
        "exit_steps": exit_steps,
        "exit_value": exit_value,
        "exit_lt_x": exit_value < x,
        "repeat_law_ok": residue != 59 or h_after == h - 3,
        "repeat_mod3": h % 3 if residue == 59 else None,
    }


def residue_table() -> list[dict[str, object]]:
    rows = []
    for residue in ODD3_RESIDUES:
        info = odd3_macro_info(residue)
        rows.append(
            {
                "residue_mod_64": residue,
                "macro_value_mod_8": info["macro_value_mod_8"],
                "branch": info["branch"],
                "exit_steps": info["exit_steps"],
                "exit_lt_x_for_symbolic_branch": info["exit_lt_x"],
            }
        )
    return rows


def analyze_start(start: int, max_steps: int) -> dict[str, object]:
    original = int(start)
    current = original
    step = 0
    max_align = v2(original + 1) if original >= 2 else 0
    max_minus5_align = 0
    repeat_macros = 0
    repeat_mod3_counts: Counter[int] = Counter()
    odd3_branch_counts: Counter[str] = Counter()
    odd3_residue_counts: Counter[int] = Counter()
    macro_counts: Counter[str] = Counter()
    repeat_law_failures: list[dict[str, object]] = []
    repeat_mod3_2_events = 0
    first_high_step = None
    first_high_value = None
    first_high_align = None

    while step < max_steps and current > 1:
        if current < original and step >= 3:
            return {
                "start": original,
                "class": "low-descent" if max_align < 3 else "high-after-entry",
                "escape_d": step,
                "b": original.bit_length(),
                "max_align": max_align,
                "max_minus5_align": max_minus5_align,
                "repeat_macros": repeat_macros,
                "repeat_mod3_counts": dict(sorted(repeat_mod3_counts.items())),
                "repeat_mod3_2_events": repeat_mod3_2_events,
                "odd3_branch_counts": dict(sorted(odd3_branch_counts.items())),
                "odd3_residue_counts": dict(sorted(odd3_residue_counts.items())),
                "macro_counts": dict(sorted(macro_counts.items())),
                "repeat_law_failure_count": len(repeat_law_failures),
                "repeat_law_failures": repeat_law_failures[:3],
                "first_high_step": first_high_step,
                "first_high_value": first_high_value,
                "first_high_align": first_high_align,
                "steps_per_bit": round_float(step / max(1, original.bit_length())),
            }

        if current & 1:
            pre_align = v2(current + 1)
            max_align = max(max_align, pre_align)
            if pre_align >= 3:
                first_high_step = step
                first_high_value = current
                first_high_align = pre_align
                return {
                    "start": original,
                    "class": "high-entered",
                    "escape_d": step,
                    "b": original.bit_length(),
                    "max_align": max_align,
                    "max_minus5_align": max_minus5_align,
                    "repeat_macros": repeat_macros,
                    "repeat_mod3_counts": dict(sorted(repeat_mod3_counts.items())),
                    "repeat_mod3_2_events": repeat_mod3_2_events,
                    "odd3_branch_counts": dict(sorted(odd3_branch_counts.items())),
                    "odd3_residue_counts": dict(sorted(odd3_residue_counts.items())),
                    "macro_counts": dict(sorted(macro_counts.items())),
                    "repeat_law_failure_count": len(repeat_law_failures),
                    "repeat_law_failures": repeat_law_failures[:3],
                    "first_high_step": first_high_step,
                    "first_high_value": first_high_value,
                    "first_high_align": first_high_align,
                    "steps_per_bit": round_float(step / max(1, original.bit_length())),
                }

            if current % 8 in (1, 5):
                macro_counts["odd_1_or_5_drop"] += 1
            elif current % 8 == 3:
                info = odd3_macro_info(current)
                branch = str(info["branch"])
                odd3_branch_counts[branch] += 1
                odd3_residue_counts[int(info["residue_mod_64"])] += 1
                macro_counts[f"odd3_{branch}"] += 1
                max_minus5_align = max(max_minus5_align, int(info["minus5_align"]))
                if branch == "repeat_minus5_gate":
                    repeat_macros += 1
                    repeat_mod3 = int(info["repeat_mod3"])
                    repeat_mod3_counts[repeat_mod3] += 1
                    if repeat_mod3 == 2:
                        repeat_mod3_2_events += 1
                    if not bool(info["repeat_law_ok"]):
                        repeat_law_failures.append(info)
        else:
            macro_counts["even_halving"] += 1

        current, _ = shortcut_step(current)
        step += 1

    if current < original:
        return {
            "start": original,
            "class": "low-descent" if max_align < 3 else "high-after-entry",
            "escape_d": step,
            "b": original.bit_length(),
            "max_align": max_align,
            "max_minus5_align": max_minus5_align,
            "repeat_macros": repeat_macros,
            "repeat_mod3_counts": dict(sorted(repeat_mod3_counts.items())),
            "repeat_mod3_2_events": repeat_mod3_2_events,
            "odd3_branch_counts": dict(sorted(odd3_branch_counts.items())),
            "odd3_residue_counts": dict(sorted(odd3_residue_counts.items())),
            "macro_counts": dict(sorted(macro_counts.items())),
            "repeat_law_failure_count": len(repeat_law_failures),
            "repeat_law_failures": repeat_law_failures[:3],
            "first_high_step": first_high_step,
            "first_high_value": first_high_value,
            "first_high_align": first_high_align,
            "steps_per_bit": round_float(step / max(1, original.bit_length())),
        }

    return {
        "start": original,
        "class": "uncertified",
        "escape_d": step,
        "b": original.bit_length(),
        "max_align": max_align,
        "max_minus5_align": max_minus5_align,
        "repeat_macros": repeat_macros,
        "repeat_mod3_counts": dict(sorted(repeat_mod3_counts.items())),
        "repeat_mod3_2_events": repeat_mod3_2_events,
        "odd3_branch_counts": dict(sorted(odd3_branch_counts.items())),
        "odd3_residue_counts": dict(sorted(odd3_residue_counts.items())),
        "macro_counts": dict(sorted(macro_counts.items())),
        "repeat_law_failure_count": len(repeat_law_failures),
        "repeat_law_failures": repeat_law_failures[:3],
        "first_high_step": first_high_step,
        "first_high_value": first_high_value,
        "first_high_align": first_high_align,
        "steps_per_bit": round_float(step / max(1, original.bit_length())),
    }


def merge_counters(rows: list[dict[str, object]], key: str) -> dict[str, int]:
    counter: Counter[str] = Counter()
    for row in rows:
        for name, value in dict(row[key]).items():
            counter[str(name)] += int(value)
    return dict(sorted(counter.items()))


def summarize(rows: list[dict[str, object]]) -> dict[str, object]:
    if not rows:
        return {"count": 0}
    return {
        "count": len(rows),
        "escape_max": max(int(row["escape_d"]) for row in rows),
        "steps_per_bit_max": round_float(max(float(row["steps_per_bit"]) for row in rows)),
        "repeat_macros_max": max(int(row["repeat_macros"]) for row in rows),
        "max_minus5_align": max(int(row["max_minus5_align"]) for row in rows),
        "repeat_mod3_2_event_count": sum(int(row["repeat_mod3_2_events"]) for row in rows),
        "repeat_law_failure_count": sum(int(row["repeat_law_failure_count"]) for row in rows),
        "odd3_branch_counts": merge_counters(rows, "odd3_branch_counts"),
        "macro_counts": merge_counters(rows, "macro_counts"),
    }


def run(args: argparse.Namespace) -> dict[str, object]:
    started = perf_counter()
    frontier_offsets = parse_offset_set(
        args.frontier_sample_offsets,
        args.frontier_sample_stride,
        default=[
            0,
            args.frontier_sample_stride // 4,
            args.frontier_sample_stride // 2,
            (3 * args.frontier_sample_stride) // 4,
        ],
    )
    explicit_starts = parse_ints(args.starts)
    frontier_starts, frontier_meta = starts_from_frontier(
        base_depth=args.frontier_base_depth,
        max_depth=args.frontier_max_depth,
        sample_stride=args.frontier_sample_stride,
        sample_offsets=frontier_offsets,
        max_frontier=args.frontier_max_frontier,
    )

    groups = {
        "initial_scan": list(range(2, args.limit_scan + 1)),
        "hard_records": get_hard_records(),
        "transfer_failure_starts": TRANSFER_FAILURE_STARTS,
        "sampled_frontier_shadows": frontier_starts,
        "explicit_starts": explicit_starts,
    }

    rows: list[dict[str, object]] = []
    by_group: dict[str, list[dict[str, object]]] = defaultdict(list)
    by_class: dict[str, list[dict[str, object]]] = defaultdict(list)
    for group_name, starts in groups.items():
        for start in unique_preserving_order(starts):
            row = analyze_start(start, args.max_steps)
            row["group"] = group_name
            rows.append(row)
            by_group[group_name].append(row)
            by_class[str(row["class"])].append(row)

    low_rows = by_class["low-descent"]
    return {
        "status": "low-alignment-structure-analysis",
        "elapsed_seconds": round_float(perf_counter() - started, 6),
        "parameters": {
            "limit_scan": args.limit_scan,
            "max_steps": args.max_steps,
            "frontier_base_depth": args.frontier_base_depth,
            "frontier_max_depth": args.frontier_max_depth,
            "frontier_sample_stride": args.frontier_sample_stride,
            "frontier_sample_offsets": frontier_offsets,
            "frontier_max_frontier": args.frontier_max_frontier,
        },
        "residue_table": residue_table(),
        "frontier_selection": frontier_meta,
        "total_checked": len(rows),
        "class_counts": dict(sorted(Counter(str(row["class"]) for row in rows).items())),
        "group_class_counts": {
            name: dict(sorted(Counter(str(row["class"]) for row in members).items()))
            for name, members in sorted(by_group.items())
        },
        "class_summaries": {name: summarize(members) for name, members in sorted(by_class.items())},
        "low_branch_checks": {
            "repeat_law_failure_count": sum(int(row["repeat_law_failure_count"]) for row in low_rows),
            "repeat_mod3_2_event_count": sum(int(row["repeat_mod3_2_events"]) for row in low_rows),
            "odd3_to_high_event_count": sum(
                int(dict(row["odd3_branch_counts"]).get("to_high_alignment", 0)) for row in low_rows
            ),
        },
        "worst_low_by_escape": top_rows(low_rows, "escape_d", args.top_n),
        "worst_low_by_repeat_macros": top_rows(low_rows, "repeat_macros", args.top_n),
        "worst_low_by_minus5_align": top_rows(low_rows, "max_minus5_align", args.top_n),
        "first_high_entries": top_rows(by_class["high-entered"], "first_high_align", args.top_n),
        "interpretation": (
            "Low-alignment slowdowns are controlled by the exact x == -5 mod 64 "
            "repeat gate. Each local repeat lowers v2(x+5) by three; the h == 5 "
            "exit hands the local odd-3 spine to the high-alignment branch if "
            "the orbit has not already descended, while h == 3 or 4 exits into "
            "ordinary descent."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit-scan", type=int, default=1000000)
    parser.add_argument("--max-steps", type=int, default=20000)
    parser.add_argument("--frontier-base-depth", type=int, default=28)
    parser.add_argument("--frontier-max-depth", type=int, default=1024)
    parser.add_argument("--frontier-sample-stride", type=int, default=1024)
    parser.add_argument("--frontier-sample-offsets", nargs="+")
    parser.add_argument("--frontier-max-frontier", type=int)
    parser.add_argument("--starts", nargs="*")
    parser.add_argument("--top-n", type=int, default=12)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--quiet", action="store_true")
    args = parser.parse_args()

    if args.limit_scan < 2:
        raise SystemExit("--limit-scan must be >= 2")
    if args.max_steps < 1:
        raise SystemExit("--max-steps must be positive")
    if args.frontier_base_depth < 1:
        raise SystemExit("--frontier-base-depth must be positive")
    if args.frontier_max_depth < 1:
        raise SystemExit("--frontier-max-depth must be positive")
    if args.frontier_sample_stride < 1:
        raise SystemExit("--frontier-sample-stride must be positive")
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

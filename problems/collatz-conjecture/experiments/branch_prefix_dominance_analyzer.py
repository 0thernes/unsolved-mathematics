#!/usr/bin/env python3
"""Prefix-local test for the branch-potential credit ledger.

The branch-potential analyzer checks whether the total structural credit before
first descent pays the total observed excess debt.  This companion asks the
sharper localization question:

    does visible credit at event entry dominate the required excess credit at
    every prefix of the same trajectory?

Credit timing is deliberately explicit.  A high ladder pays `v2(x + 1) - 2`
as soon as the odd state `x = 2^a q - 1` is observed.  A low repeat gate pays
one unit as soon as the odd state `x == -5 mod 64` is observed.  This is not a
Collatz proof; it is a falsifiable test for a stronger potential theorem.
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path
from time import perf_counter

sys.path.insert(0, str(Path(__file__).resolve().parent))

from branch_potential_analyzer import (
    TRANSFER_FAILURE_STARTS,
    get_hard_records,
    min_credit_required,
    odd3_macro_info,
    parse_ints,
    parse_offset_set,
    round_float,
    shortcut_step,
    starts_from_frontier,
    unique_preserving_order,
    update_excess,
    v2,
)
from branch_potential_stress import (
    biased_boundary_random,
    high_ladder_spines,
    low_repeat_spines,
    near_boundaries,
    random_high_bit,
)


def observe_prefix(
    *,
    state: dict[str, object],
    event: str,
    original: int,
    current: int,
    step: int,
    odd_steps: int,
    max_excess: float,
    credit: int,
) -> None:
    required = min_credit_required(max_excess)
    surplus = credit - required
    deficit = max(0, -surplus)

    state["prefix_observation_count"] = int(state["prefix_observation_count"]) + 1
    state["max_prefix_required"] = max(int(state["max_prefix_required"]), required)
    state["min_prefix_surplus"] = min(int(state["min_prefix_surplus"]), surplus)
    state["max_prefix_deficit"] = max(int(state["max_prefix_deficit"]), deficit)

    if surplus == 0:
        state["prefix_tight_count"] = int(state["prefix_tight_count"]) + 1

    if deficit <= 0:
        return

    state["prefix_deficit_observation_count"] = int(state["prefix_deficit_observation_count"]) + 1
    if state["first_prefix_deficit"] is None:
        state["first_prefix_deficit"] = {
            "event": event,
            "step": step,
            "current": current,
            "current_over_start": round_float(current / max(1, original), 12),
            "odd_steps": odd_steps,
            "max_excess": round_float(max_excess),
            "required_credit": required,
            "available_credit": credit,
            "deficit": deficit,
        }


def analyze_prefix_start(start: int, max_steps: int) -> dict[str, object]:
    original = int(start)
    if original < 2:
        return {
            "start": original,
            "class": "trivial",
            "escape_d": 0,
            "b": 1,
            "certified": True,
            "odd_steps": 0,
            "max_excess": 0.0,
            "final_excess": 0.0,
            "min_credit_required": 0,
            "high_ladder_credit": 0,
            "low_repeat_credit": 0,
            "combined_unit_credit": 0,
            "prefix_unit_sufficient": True,
            "max_prefix_required": 0,
            "max_prefix_deficit": 0,
            "min_prefix_surplus": 0,
            "prefix_tight_count": 1,
            "prefix_observation_count": 1,
            "prefix_deficit_observation_count": 0,
            "first_prefix_deficit": None,
        }

    current = original
    step = 0
    odd_steps = 0
    max_excess = 0.0
    final_excess = 0.0
    credit = 0

    high_ladder_count = 0
    high_ladder_credit = 0
    high_alignment_counts: Counter[int] = Counter()
    high_formula_failures = 0
    high_alignment_burn_failures = 0
    max_high_align = 0
    max_even_chain = 0

    low_repeat_count = 0
    low_repeat_credit = 0
    low_repeat_law_failures = 0
    max_minus5_align = 0
    odd3_branch_counts: Counter[str] = Counter()
    macro_counts: Counter[str] = Counter()

    prefix_state: dict[str, object] = {
        "max_prefix_required": 0,
        "max_prefix_deficit": 0,
        "min_prefix_surplus": 0,
        "prefix_tight_count": 0,
        "prefix_observation_count": 0,
        "prefix_deficit_observation_count": 0,
        "first_prefix_deficit": None,
    }
    observe_prefix(
        state=prefix_state,
        event="start",
        original=original,
        current=current,
        step=step,
        odd_steps=odd_steps,
        max_excess=max_excess,
        credit=credit,
    )

    while step < max_steps and current > 1:
        if current < original and step >= 3:
            break

        if current & 1:
            align = v2(current + 1)
            if align >= 3:
                q = (current + 1) >> align
                high_ladder_count += 1
                high_ladder_credit += align - 2
                credit += align - 2
                high_alignment_counts[align] += 1
                max_high_align = max(max_high_align, align)
                observe_prefix(
                    state=prefix_state,
                    event="enter_high_ladder",
                    original=original,
                    current=current,
                    step=step,
                    odd_steps=odd_steps,
                    max_excess=max_excess,
                    credit=credit,
                )

                expected_power3 = 1
                for k in range(align):
                    expected = expected_power3 * (1 << (align - k)) * q - 1
                    if current != expected:
                        high_formula_failures += 1
                    if v2(current + 1) != align - k:
                        high_alignment_burn_failures += 1

                    current, parity = shortcut_step(current)
                    if parity != 1:
                        high_alignment_burn_failures += 1
                    step += 1
                    odd_steps += 1
                    final_excess, max_excess = update_excess(odd_steps, step, max_excess)
                    observe_prefix(
                        state=prefix_state,
                        event="high_ladder_step",
                        original=original,
                        current=current,
                        step=step,
                        odd_steps=odd_steps,
                        max_excess=max_excess,
                        credit=credit,
                    )
                    expected_power3 *= 3
                    if step >= max_steps:
                        break

                terminal_expected = expected_power3 * q - 1
                if current != terminal_expected:
                    high_formula_failures += 1

                even_chain = v2(max(1, current))
                max_even_chain = max(max_even_chain, even_chain)
                while step < max_steps and current > 1 and current % 2 == 0:
                    current, parity = shortcut_step(current)
                    if parity != 0:
                        high_alignment_burn_failures += 1
                    step += 1
                    final_excess, max_excess = update_excess(odd_steps, step, max_excess)
                    observe_prefix(
                        state=prefix_state,
                        event="post_ladder_even_step",
                        original=original,
                        current=current,
                        step=step,
                        odd_steps=odd_steps,
                        max_excess=max_excess,
                        credit=credit,
                    )
                    if current < original and step >= 3:
                        break
                continue

            if current % 8 in (1, 5):
                macro_counts["low_odd_1_or_5_drop"] += 1
            elif current % 8 == 3:
                info = odd3_macro_info(current)
                branch = str(info["branch"])
                odd3_branch_counts[branch] += 1
                macro_counts[f"low_odd3_{branch}"] += 1
                max_minus5_align = max(max_minus5_align, int(info["minus5_align"]))
                if branch == "repeat_minus5_gate":
                    low_repeat_count += 1
                    low_repeat_credit += 1
                    credit += 1
                    if not bool(info["repeat_law_ok"]):
                        low_repeat_law_failures += 1
                    observe_prefix(
                        state=prefix_state,
                        event="enter_low_repeat_gate",
                        original=original,
                        current=current,
                        step=step,
                        odd_steps=odd_steps,
                        max_excess=max_excess,
                        credit=credit,
                    )
        else:
            macro_counts["even_halving"] += 1

        current, parity = shortcut_step(current)
        step += 1
        odd_steps += parity
        final_excess, max_excess = update_excess(odd_steps, step, max_excess)
        observe_prefix(
            state=prefix_state,
            event="ordinary_step",
            original=original,
            current=current,
            step=step,
            odd_steps=odd_steps,
            max_excess=max_excess,
            credit=credit,
        )

    certified = current < original
    required = min_credit_required(max_excess)
    combined_unit_credit = high_ladder_credit + low_repeat_credit
    class_name = "uncertified"
    if certified:
        if max_high_align >= 3:
            class_name = "high-assisted-descent"
        elif low_repeat_count:
            class_name = "low-repeat-descent"
        else:
            class_name = "low-direct-descent"

    max_prefix_deficit = int(prefix_state["max_prefix_deficit"])
    return {
        "start": original,
        "class": class_name,
        "escape_d": step,
        "b": original.bit_length(),
        "certified": certified,
        "odd_steps": odd_steps,
        "steps_per_bit": round_float(step / max(1, original.bit_length())),
        "max_excess": round_float(max_excess),
        "final_excess": round_float(final_excess),
        "min_credit_required": required,
        "high_ladder_count": high_ladder_count,
        "high_ladder_credit": high_ladder_credit,
        "high_alignment_counts": dict(sorted(high_alignment_counts.items())),
        "high_formula_failure_count": high_formula_failures,
        "high_alignment_burn_failure_count": high_alignment_burn_failures,
        "max_high_align": max_high_align,
        "max_even_chain": max_even_chain,
        "low_repeat_count": low_repeat_count,
        "low_repeat_credit": low_repeat_credit,
        "low_repeat_law_failure_count": low_repeat_law_failures,
        "max_minus5_align": max_minus5_align,
        "odd3_branch_counts": dict(sorted(odd3_branch_counts.items())),
        "macro_counts": dict(sorted(macro_counts.items())),
        "combined_unit_credit": combined_unit_credit,
        "unit_credit_surplus": combined_unit_credit - required,
        "prefix_unit_sufficient": max_prefix_deficit == 0,
        "max_prefix_required": int(prefix_state["max_prefix_required"]),
        "max_prefix_deficit": max_prefix_deficit,
        "min_prefix_surplus": int(prefix_state["min_prefix_surplus"]),
        "prefix_tight_count": int(prefix_state["prefix_tight_count"]),
        "prefix_observation_count": int(prefix_state["prefix_observation_count"]),
        "prefix_deficit_observation_count": int(prefix_state["prefix_deficit_observation_count"]),
        "first_prefix_deficit": prefix_state["first_prefix_deficit"],
    }


def merge_counter(rows: list[dict[str, object]], key: str) -> dict[str, int]:
    merged: Counter[str] = Counter()
    for row in rows:
        for name, value in dict(row[key]).items():
            merged[str(name)] += int(value)
    return dict(sorted(merged.items(), key=lambda item: item[0]))


def summarize_prefix(rows: list[dict[str, object]]) -> dict[str, object]:
    if not rows:
        return {"count": 0}
    return {
        "count": len(rows),
        "certified_count": sum(1 for row in rows if row["certified"]),
        "prefix_failure_count": sum(1 for row in rows if not row["prefix_unit_sufficient"]),
        "escape_max": max(int(row["escape_d"]) for row in rows),
        "steps_per_bit_max": round_float(max(float(row["steps_per_bit"]) for row in rows)),
        "max_excess": round_float(max(float(row["max_excess"]) for row in rows)),
        "max_prefix_required": max(int(row["max_prefix_required"]) for row in rows),
        "max_prefix_deficit": max(int(row["max_prefix_deficit"]) for row in rows),
        "min_prefix_surplus": min(int(row["min_prefix_surplus"]) for row in rows),
        "high_ladder_credit_total": sum(int(row["high_ladder_credit"]) for row in rows),
        "low_repeat_credit_total": sum(int(row["low_repeat_credit"]) for row in rows),
        "high_formula_failure_count": sum(int(row["high_formula_failure_count"]) for row in rows),
        "high_alignment_burn_failure_count": sum(int(row["high_alignment_burn_failure_count"]) for row in rows),
        "low_repeat_law_failure_count": sum(int(row["low_repeat_law_failure_count"]) for row in rows),
        "macro_counts": merge_counter(rows, "macro_counts"),
    }


def baseline_groups(args: argparse.Namespace) -> tuple[dict[str, list[int]], dict[str, object]]:
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
    frontier_starts, frontier_meta = starts_from_frontier(
        base_depth=args.frontier_base_depth,
        max_depth=args.frontier_max_depth,
        sample_stride=args.frontier_sample_stride,
        sample_offsets=frontier_offsets,
        max_frontier=args.frontier_max_frontier,
    )
    return {
        "baseline/initial_scan": list(range(2, args.limit_scan + 1)),
        "baseline/hard_records": get_hard_records(),
        "baseline/transfer_failure_starts": TRANSFER_FAILURE_STARTS,
        "baseline/sampled_frontier_shadows": frontier_starts,
    }, {**frontier_meta, "sample_offsets": frontier_offsets}


def stress_groups(args: argparse.Namespace) -> tuple[dict[str, list[int]], dict[str, object]]:
    frontier_offsets = parse_offset_set(
        args.stress_frontier_sample_offsets,
        args.stress_frontier_sample_stride,
        default=[
            args.stress_frontier_sample_stride // 8,
            (3 * args.stress_frontier_sample_stride) // 8,
            (5 * args.stress_frontier_sample_stride) // 8,
            (7 * args.stress_frontier_sample_stride) // 8,
        ],
    )
    frontier_starts, frontier_meta = starts_from_frontier(
        base_depth=args.stress_frontier_base_depth,
        max_depth=args.stress_frontier_max_depth,
        sample_stride=args.stress_frontier_sample_stride,
        sample_offsets=frontier_offsets,
        max_frontier=args.stress_frontier_max_frontier,
    )
    return {
        "stress/hard_records": get_hard_records(),
        "stress/low_repeat_spines": low_repeat_spines(args.low_max_h, args.max_q),
        "stress/high_ladder_spines": high_ladder_spines(args.high_max_a, args.max_q),
        "stress/near_boundaries": near_boundaries(args.max_bits, args.boundary_width),
        "stress/random_high_bit": random_high_bit(args.random_count, args.random_min_bits, args.max_bits, args.seed),
        "stress/biased_boundary_random": biased_boundary_random(args.biased_count, args.max_bits, args.seed),
        "stress/fresh_frontier_shadows": frontier_starts,
    }, {**frontier_meta, "sample_offsets": frontier_offsets}


def build_groups(args: argparse.Namespace) -> tuple[dict[str, list[int]], dict[str, object]]:
    groups: dict[str, list[int]] = {}
    meta: dict[str, object] = {}
    if args.population in ("baseline", "combined"):
        baseline, baseline_meta = baseline_groups(args)
        groups.update(baseline)
        meta["baseline_frontier"] = baseline_meta
    if args.population in ("stress", "combined"):
        stress, stress_meta = stress_groups(args)
        groups.update(stress)
        meta["stress_frontier"] = stress_meta
    explicit = parse_ints(args.starts)
    if explicit:
        groups["explicit_starts"] = explicit
    return groups, meta


def run(args: argparse.Namespace) -> dict[str, object]:
    started = perf_counter()
    groups, frontier_meta = build_groups(args)
    rows: list[dict[str, object]] = []
    by_group: dict[str, list[dict[str, object]]] = defaultdict(list)
    by_class: dict[str, list[dict[str, object]]] = defaultdict(list)

    for group_name, starts in groups.items():
        for start in unique_preserving_order(starts):
            row = analyze_prefix_start(start, args.max_steps)
            row["group"] = group_name
            rows.append(row)
            by_group[group_name].append(row)
            by_class[str(row["class"])].append(row)

    uncertified = [row for row in rows if not row["certified"]]
    prefix_failures = [row for row in rows if not row["prefix_unit_sufficient"]]

    return {
        "status": "branch-prefix-dominance-analysis",
        "elapsed_seconds": round_float(perf_counter() - started, 6),
        "parameters": {
            key: (str(value) if isinstance(value, Path) else value)
            for key, value in vars(args).items()
        },
        "frontier_selection": frontier_meta,
        "total_checked": len(rows),
        "unique_starts_checked": len({int(row["start"]) for row in rows}),
        "class_counts": dict(sorted(Counter(str(row["class"]) for row in rows).items())),
        "group_counts": {name: len(members) for name, members in sorted(by_group.items())},
        "group_summaries": {name: summarize_prefix(members) for name, members in sorted(by_group.items())},
        "class_summaries": {name: summarize_prefix(members) for name, members in sorted(by_class.items())},
        "failure_counts": {
            "uncertified": len(uncertified),
            "prefix_unit": len(prefix_failures),
            "high_formula": sum(int(row["high_formula_failure_count"]) for row in rows),
            "high_alignment_burn": sum(int(row["high_alignment_burn_failure_count"]) for row in rows),
            "low_repeat_law": sum(int(row["low_repeat_law_failure_count"]) for row in rows),
        },
        "max_prefix_deficit": max((int(row["max_prefix_deficit"]) for row in rows), default=0),
        "min_prefix_surplus": min((int(row["min_prefix_surplus"]) for row in rows), default=0),
        "max_prefix_required": max((int(row["max_prefix_required"]) for row in rows), default=0),
        "largest_prefix_failures": sorted(
            prefix_failures,
            key=lambda row: (int(row["max_prefix_deficit"]), float(row["max_excess"]), int(row["start"])),
            reverse=True,
        )[: args.top_n],
        "tightest_prefix_surplus": sorted(
            rows,
            key=lambda row: (int(row["min_prefix_surplus"]), -float(row["max_excess"]), int(row["start"])),
        )[: args.top_n],
        "largest_excess": sorted(rows, key=lambda row: (float(row["max_excess"]), int(row["start"])), reverse=True)[
            : args.top_n
        ],
        "largest_escape": sorted(rows, key=lambda row: (int(row["escape_d"]), int(row["start"])), reverse=True)[
            : args.top_n
        ],
        "interpretation": (
            "Finite prefix-local falsification test. Credit is assigned at the "
            "entry of visible high-ladder and low-repeat events. A positive "
            "max_prefix_deficit falsifies this stronger localized theorem. "
            "Zero failures would still be evidence only, not a universal proof."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--population", choices=["baseline", "stress", "combined"], default="combined")
    parser.add_argument("--max-steps", type=int, default=50000)
    parser.add_argument("--limit-scan", type=int, default=1_000_000)
    parser.add_argument("--frontier-base-depth", type=int, default=28)
    parser.add_argument("--frontier-max-depth", type=int, default=1024)
    parser.add_argument("--frontier-sample-stride", type=int, default=1024)
    parser.add_argument("--frontier-sample-offsets", nargs="+")
    parser.add_argument("--frontier-max-frontier", type=int)
    parser.add_argument("--low-max-h", type=int, default=96)
    parser.add_argument("--high-max-a", type=int, default=96)
    parser.add_argument("--max-q", type=int, default=63)
    parser.add_argument("--max-bits", type=int, default=160)
    parser.add_argument("--boundary-width", type=int, default=63)
    parser.add_argument("--random-count", type=int, default=2000)
    parser.add_argument("--random-min-bits", type=int, default=32)
    parser.add_argument("--biased-count", type=int, default=2000)
    parser.add_argument("--seed", type=int, default=20260702)
    parser.add_argument("--stress-frontier-base-depth", type=int, default=28)
    parser.add_argument("--stress-frontier-max-depth", type=int, default=1024)
    parser.add_argument("--stress-frontier-sample-stride", type=int, default=1024)
    parser.add_argument("--stress-frontier-sample-offsets", nargs="+")
    parser.add_argument("--stress-frontier-max-frontier", type=int)
    parser.add_argument("--starts", nargs="*")
    parser.add_argument("--top-n", type=int, default=12)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--quiet", action="store_true")
    args = parser.parse_args()

    if args.max_steps < 1:
        raise SystemExit("--max-steps must be positive")
    if args.limit_scan < 1:
        raise SystemExit("--limit-scan must be positive")
    if args.frontier_base_depth < 1 or args.stress_frontier_base_depth < 1:
        raise SystemExit("frontier base depths must be positive")
    if args.frontier_max_depth < 1 or args.stress_frontier_max_depth < 1:
        raise SystemExit("frontier max depths must be positive")
    if args.frontier_sample_stride < 1 or args.stress_frontier_sample_stride < 1:
        raise SystemExit("frontier sample strides must be positive")
    if args.low_max_h < 6:
        raise SystemExit("--low-max-h must be >= 6")
    if args.high_max_a < 3:
        raise SystemExit("--high-max-a must be >= 3")
    if args.max_q < 1:
        raise SystemExit("--max-q must be positive")
    if args.max_bits < 12:
        raise SystemExit("--max-bits must be >= 12")
    if args.random_min_bits < 2 or args.random_min_bits > args.max_bits:
        raise SystemExit("--random-min-bits must be between 2 and --max-bits")
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

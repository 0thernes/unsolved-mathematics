#!/usr/bin/env python3
"""Analyze the exact high-alignment ladder behind kick/carry repulsion.

The low branch is controlled by the `-5 mod 64` repeat gate.  The high branch
has a different exact object: if an odd value is aligned to the 2-adic boundary,

    x = 2^a q - 1,    a = v2(x + 1) >= 3, q odd,

then the next `a` shortcut steps are forced:

    T^k(x) = 3^k 2^(a-k) q - 1       for 0 <= k <= a.

The first `a - 2` of those odd steps are exactly the high-alignment repulsion
events counted by the existing kick audit.  This script verifies that ladder
law and checks whether the exact ladder credit pays the observed excess debt on
the same finite population as the alignment dichotomy.
"""

from __future__ import annotations

import argparse
import json
import math
from collections import Counter, defaultdict
from pathlib import Path
from time import perf_counter

from kick_repulsion_claim_audit import (
    TRANSFER_FAILURE_STARTS,
    starts_from_frontier,
    top_rows,
    unique_preserving_order,
)
from master_kick_rejection_lemma import THETA, get_hard_records, shortcut_step, v2
from repayment_envelope_scan import parse_ints, round_float
from terminal_residue_tree_sweep_analyzer import parse_offset_set


def empty_row(original: int, class_name: str, step: int, max_align: int) -> dict[str, object]:
    return {
        "start": original,
        "class": class_name,
        "escape_d": step,
        "b": max(1, original.bit_length()),
        "steps_per_bit": round_float(step / max(1, original.bit_length())),
        "max_align": max_align,
        "max_excess": 0.0,
        "final_excess": 0.0,
        "min_repulsions_required": 0,
        "ladder_count": 0,
        "ladder_credit": 0,
        "credit_sufficient": True,
        "credit_surplus": 0,
        "max_ladder_align": 0,
        "max_even_chain_total": 0,
        "max_even_chain_used": 0,
        "ladder_alignment_counts": {},
        "ladder_even_chain_counts": {},
        "formula_failure_count": 0,
        "alignment_burn_failure_count": 0,
    }


def finish_row(
    *,
    original: int,
    class_name: str,
    step: int,
    odd_steps: int,
    max_align: int,
    max_excess: float,
    final_excess: float,
    ladder_count: int,
    ladder_credit: int,
    max_ladder_align: int,
    max_even_chain_total: int,
    max_even_chain_used: int,
    ladder_alignment_counts: Counter[int],
    ladder_even_chain_counts: Counter[int],
    formula_failures: int,
    alignment_burn_failures: int,
) -> dict[str, object]:
    if max_excess >= 1.0:
        min_req = math.ceil(max(0.0, max_excess - 0.999))
    else:
        min_req = 0
    return {
        "start": original,
        "class": class_name,
        "escape_d": step,
        "b": max(1, original.bit_length()),
        "steps_per_bit": round_float(step / max(1, original.bit_length())),
        "odd_steps": odd_steps,
        "max_align": max_align,
        "max_excess": round_float(max_excess),
        "final_excess": round_float(final_excess),
        "min_repulsions_required": min_req,
        "ladder_count": ladder_count,
        "ladder_credit": ladder_credit,
        "credit_sufficient": ladder_credit >= min_req,
        "credit_surplus": ladder_credit - min_req,
        "max_ladder_align": max_ladder_align,
        "max_even_chain_total": max_even_chain_total,
        "max_even_chain_used": max_even_chain_used,
        "ladder_alignment_counts": dict(sorted(ladder_alignment_counts.items())),
        "ladder_even_chain_counts": dict(sorted(ladder_even_chain_counts.items())),
        "formula_failure_count": formula_failures,
        "alignment_burn_failure_count": alignment_burn_failures,
    }


def analyze_start(start: int, max_steps: int) -> dict[str, object]:
    original = int(start)
    if original < 2:
        return empty_row(original, "trivial", 0, 0)

    current = original
    step = 0
    odd_steps = 0
    max_align = v2(original + 1)
    max_excess = 0.0
    final_excess = 0.0
    ladder_count = 0
    ladder_credit = 0
    max_ladder_align = 0
    max_even_chain_total = 0
    max_even_chain_used = 0
    ladder_alignment_counts: Counter[int] = Counter()
    ladder_even_chain_counts: Counter[int] = Counter()
    formula_failures = 0
    alignment_burn_failures = 0

    while step < max_steps and current > 1:
        if current < original and step >= 3:
            class_name = "high-descent" if max_ladder_align >= 3 else "low-descent"
            return finish_row(
                original=original,
                class_name=class_name,
                step=step,
                odd_steps=odd_steps,
                max_align=max_align,
                max_excess=max_excess,
                final_excess=final_excess,
                ladder_count=ladder_count,
                ladder_credit=ladder_credit,
                max_ladder_align=max_ladder_align,
                max_even_chain_total=max_even_chain_total,
                max_even_chain_used=max_even_chain_used,
                ladder_alignment_counts=ladder_alignment_counts,
                ladder_even_chain_counts=ladder_even_chain_counts,
                formula_failures=formula_failures,
                alignment_burn_failures=alignment_burn_failures,
            )

        if current & 1:
            align = v2(current + 1)
            max_align = max(max_align, align)
            if align >= 3:
                q = (current + 1) >> align
                ladder_start = current
                ladder_count += 1
                ladder_credit += align - 2
                max_ladder_align = max(max_ladder_align, align)
                ladder_alignment_counts[align] += 1
                expected_power3 = 1

                for k in range(align):
                    expected = expected_power3 * (1 << (align - k)) * q - 1
                    if current != expected:
                        formula_failures += 1
                    current_align = v2(current + 1)
                    if current_align != align - k:
                        alignment_burn_failures += 1
                    current, parity = shortcut_step(current)
                    if parity != 1:
                        alignment_burn_failures += 1
                    step += 1
                    odd_steps += 1
                    final_excess = odd_steps - THETA * step
                    max_excess = max(max_excess, final_excess)
                    expected_power3 *= 3
                    if step >= max_steps:
                        break

                terminal_expected = expected_power3 * q - 1
                if current != terminal_expected:
                    formula_failures += 1
                even_chain_total = v2(max(1, terminal_expected))
                ladder_even_chain_counts[even_chain_total] += 1
                max_even_chain_total = max(max_even_chain_total, even_chain_total)
                even_chain_used = 0
                while step < max_steps and current > 1 and current % 2 == 0:
                    current, parity = shortcut_step(current)
                    if parity != 0:
                        alignment_burn_failures += 1
                    step += 1
                    even_chain_used += 1
                    final_excess = odd_steps - THETA * step
                    max_excess = max(max_excess, final_excess)
                    if current < original and step >= 3:
                        break
                max_even_chain_used = max(max_even_chain_used, even_chain_used)
                if ladder_start == current and current > 1:
                    formula_failures += 1
                continue

        current, parity = shortcut_step(current)
        step += 1
        odd_steps += parity
        final_excess = odd_steps - THETA * step
        max_excess = max(max_excess, final_excess)

    if current < original:
        class_name = "high-descent" if max_ladder_align >= 3 else "low-descent"
    else:
        class_name = "uncertified"
    return finish_row(
        original=original,
        class_name=class_name,
        step=step,
        odd_steps=odd_steps,
        max_align=max_align,
        max_excess=max_excess,
        final_excess=final_excess,
        ladder_count=ladder_count,
        ladder_credit=ladder_credit,
        max_ladder_align=max_ladder_align,
        max_even_chain_total=max_even_chain_total,
        max_even_chain_used=max_even_chain_used,
        ladder_alignment_counts=ladder_alignment_counts,
        ladder_even_chain_counts=ladder_even_chain_counts,
        formula_failures=formula_failures,
        alignment_burn_failures=alignment_burn_failures,
    )


def merge_counter(rows: list[dict[str, object]], key: str) -> dict[str, int]:
    counter: Counter[str] = Counter()
    for row in rows:
        for name, value in dict(row[key]).items():
            counter[str(name)] += int(value)
    return dict(sorted(counter.items(), key=lambda item: int(item[0])))


def summarize(rows: list[dict[str, object]]) -> dict[str, object]:
    if not rows:
        return {"count": 0}
    return {
        "count": len(rows),
        "escape_max": max(int(row["escape_d"]) for row in rows),
        "steps_per_bit_max": round_float(max(float(row["steps_per_bit"]) for row in rows)),
        "max_align": max(int(row["max_align"]) for row in rows),
        "max_excess": round_float(max(float(row["max_excess"]) for row in rows)),
        "ladder_count_total": sum(int(row["ladder_count"]) for row in rows),
        "ladder_credit_total": sum(int(row["ladder_credit"]) for row in rows),
        "min_credit_surplus": min(int(row["credit_surplus"]) for row in rows),
        "credit_sufficient_count": sum(1 for row in rows if row["credit_sufficient"]),
        "credit_failure_count": sum(1 for row in rows if not row["credit_sufficient"]),
        "max_ladder_align": max(int(row["max_ladder_align"]) for row in rows),
        "max_even_chain_total": max(int(row["max_even_chain_total"]) for row in rows),
        "max_even_chain_used": max(int(row["max_even_chain_used"]) for row in rows),
        "formula_failure_count": sum(int(row["formula_failure_count"]) for row in rows),
        "alignment_burn_failure_count": sum(int(row["alignment_burn_failure_count"]) for row in rows),
        "ladder_alignment_counts": merge_counter(rows, "ladder_alignment_counts"),
        "ladder_even_chain_counts": merge_counter(rows, "ladder_even_chain_counts"),
    }


def high_ladder_identity_examples(max_align: int) -> list[dict[str, object]]:
    rows = []
    for align in range(3, max_align + 1):
        x = (1 << align) - 1
        q = 1
        terminal = (3**align) * q - 1
        rows.append(
            {
                "align": align,
                "x": x,
                "terminal_after_odd_ladder": terminal,
                "forced_even_chain": v2(terminal),
                "ladder_credit": align - 2,
            }
        )
    return rows


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

    high_rows = by_class["high-descent"]
    return {
        "status": "high-alignment-ladder-analysis",
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
        "identity": {
            "statement": "If x = 2^a*q - 1 with q odd and a >= 3, then T^k(x) = 3^k*2^(a-k)*q - 1 for 0 <= k <= a.",
            "repulsion_credit_per_ladder": "a - 2 high-alignment odd steps",
            "examples": high_ladder_identity_examples(args.example_max_align),
        },
        "frontier_selection": frontier_meta,
        "total_checked": len(rows),
        "class_counts": dict(sorted(Counter(str(row["class"]) for row in rows).items())),
        "group_class_counts": {
            name: dict(sorted(Counter(str(row["class"]) for row in members).items()))
            for name, members in sorted(by_group.items())
        },
        "class_summaries": {name: summarize(members) for name, members in sorted(by_class.items())},
        "high_branch_checks": {
            "credit_failure_count": sum(1 for row in high_rows if not row["credit_sufficient"]),
            "formula_failure_count": sum(int(row["formula_failure_count"]) for row in high_rows),
            "alignment_burn_failure_count": sum(int(row["alignment_burn_failure_count"]) for row in high_rows),
            "min_credit_surplus": min((int(row["credit_surplus"]) for row in high_rows), default=None),
        },
        "worst_high_by_ratio": top_rows(high_rows, "steps_per_bit", args.top_n),
        "worst_high_by_escape": top_rows(high_rows, "escape_d", args.top_n),
        "tightest_high_credit_surplus": sorted(
            high_rows,
            key=lambda row: (int(row["credit_surplus"]), -float(row["max_excess"])),
        )[: args.top_n],
        "largest_ladder_credit": top_rows(high_rows, "ladder_credit", args.top_n),
        "largest_ladder_alignment": top_rows(high_rows, "max_ladder_align", args.top_n),
        "interpretation": (
            "The high-alignment branch decomposes into exact ladders. A ladder "
            "starting at v2(x+1)=a contributes a-2 counted high-alignment "
            "repulsion credits before the forced even terminal. Finite evidence "
            "checks that this exact credit pays the max-excess debt on the "
            "same population as the kick audit."
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
    parser.add_argument("--example-max-align", type=int, default=12)
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
    if args.example_max_align < 3:
        raise SystemExit("--example-max-align must be >= 3")

    payload = run(args)
    text = json.dumps(payload, indent=2, sort_keys=True)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text + "\n", encoding="utf-8")
    if not args.quiet:
        print(text)


if __name__ == "__main__":
    main()

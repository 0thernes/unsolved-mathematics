#!/usr/bin/env python3
"""Test a combined low-rank / high-ladder structural potential.

The current Collatz proof frontier in this repo has two exact local grammars:

* low alignment: the only odd `3 mod 8` repeat gate is `x == -5 mod 64`,
  and each repeat lowers `v2(x + 5)` by exactly `3`;
* high alignment: if odd `x = 2^a q - 1`, `a >= 3`, then a forced ladder
  burns `v2(x + 1)` one bit per odd shortcut and contributes `a - 2`
  high-alignment credits.

This script tests the next bridge: whether a combined structural credit,

    high_ladder_credit + low_repeat_credit,

pays the observed excess debt on the same finite population used by the kick
audit.  It is evidence and obligation accounting, not a proof of Collatz.
"""

from __future__ import annotations

import argparse
import json
import math
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
from time import perf_counter

THETA = math.log(2) / math.log(3)

TRANSFER_FAILURE_STARTS = [
    350770415,
    396162791,
    445000795,
    475203487,
    516172255,
    386531023,
    527881499,
    409596671,
    461361359,
    471717535,
    184427291,
    228350399,
    262955455,
    194843463,
    175854063,
]


@dataclass(frozen=True)
class FrontierLeaf:
    depth: int
    residue: int
    odd_count: int
    image: int


def round_float(value: float, digits: int = 9) -> float:
    return round(float(value), digits)


def parse_ints(raw_values: list[str] | None) -> list[int]:
    if not raw_values:
        return []
    values: list[int] = []
    for raw in raw_values:
        for part in raw.replace(",", " ").split():
            values.append(int(part, 0))
    return values


def parse_offset_set(raw_offsets: list[str] | None, stride: int, default: list[int]) -> list[int]:
    if not raw_offsets:
        offsets = default
    elif any(raw.strip().lower() == "all" for raw in raw_offsets):
        offsets = list(range(stride))
    else:
        offsets = parse_ints(raw_offsets)

    bad_offsets = [offset for offset in offsets if not 0 <= offset < stride]
    if bad_offsets:
        raise SystemExit("all offsets must satisfy 0 <= offset < target stride")

    return unique_preserving_order(offsets)


def unique_preserving_order(values) -> list[int]:
    seen: set[int] = set()
    ordered: list[int] = []
    for value in values:
        value = int(value)
        if value in seen:
            continue
        seen.add(value)
        ordered.append(value)
    return ordered


def top_rows(rows: list[dict[str, object]], key: str, top_n: int) -> list[dict[str, object]]:
    return sorted(rows, key=lambda row: (row[key], row["start"]), reverse=True)[:top_n]


def v2(x: int) -> int:
    if x == 0:
        return 10**9
    count = 0
    while x % 2 == 0:
        x //= 2
        count += 1
    return count


def shortcut_step(n: int) -> tuple[int, int]:
    if n % 2 == 0:
        return n // 2, 0
    return (3 * n + 1) // 2, 1


def get_hard_records() -> list[int]:
    records = [
        27,
        703,
        10087,
        35655,
        270271,
        362343,
        381727,
        626331,
        1027431,
        1126015,
        8088063,
        13421671,
        20638335,
        26716671,
        56924955,
        63728127,
        217740015,
        2358909599867980429759,
        2416326538309822975,
    ]
    for m in [11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 35, 39, 43, 47]:
        records.append((1 << m) - 1)
    return sorted(set(records))


def odd3_macro_info(x: int) -> dict[str, object]:
    if not (x & 1) or x % 8 != 3:
        raise ValueError("odd3_macro_info expects an odd x == 3 mod 8")
    macro_value = (9 * x + 5) // 8
    h = v2(x + 5)
    h_after = v2(macro_value + 5)
    residue = x % 64
    if residue == 59:
        branch = "repeat_minus5_gate"
    elif macro_value & 1 == 0:
        branch = "even_exit"
    elif macro_value % 8 == 7:
        branch = "to_high_alignment"
    else:
        branch = "odd15_drop_exit"
    return {
        "minus5_align": h,
        "minus5_align_after_macro": h_after,
        "branch": branch,
        "repeat_law_ok": residue != 59 or h_after == h - 3,
    }


def shortcut_image(n: int) -> int:
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


def powers_of_three(max_depth: int) -> list[int]:
    powers = [1]
    for _ in range(max_depth):
        powers.append(powers[-1] * 3)
    return powers


def enumerate_frontier(base_depth: int, pow3: list[int]) -> tuple[list[FrontierLeaf], dict[str, object]]:
    live = [FrontierLeaf(depth=0, residue=0, odd_count=0, image=0)]
    certified_leaf_count = 0
    certified_units = 0

    for depth in range(base_depth):
        next_depth = depth + 1
        next_bit = 1 << depth
        next_live: list[FrontierLeaf] = []
        for leaf in live:
            for high_bit in (0, 1):
                residue = leaf.residue + (next_bit if high_bit else 0)
                image_before_next_step = leaf.image + (pow3[leaf.odd_count] if high_bit else 0)
                odd_count = leaf.odd_count + (image_before_next_step & 1)
                image = shortcut_image(image_before_next_step)
                if pow3[odd_count] < (1 << next_depth):
                    certified_leaf_count += 1
                    certified_units += 1 << (base_depth - next_depth)
                else:
                    next_live.append(FrontierLeaf(next_depth, residue, odd_count, image))
        live = next_live

    odd_histogram = Counter(leaf.odd_count for leaf in live)
    scale = 1 << base_depth
    return live, {
        "base_depth": base_depth,
        "certified_leaf_count": certified_leaf_count,
        "certified_units_mod_2^base_depth": certified_units,
        "frontier_count": len(live),
        "frontier_fraction": len(live) / scale,
        "certified_fraction": certified_units / scale,
        "frontier_odd_count_histogram": {str(k): odd_histogram[k] for k in sorted(odd_histogram)},
    }


def frontier_partitions(
    *,
    base_depth: int,
    max_depth: int,
    stride: int,
    max_frontier: int | None,
) -> tuple[dict[int, list[int]], dict[str, object]]:
    frontier, stats = enumerate_frontier(base_depth, powers_of_three(max_depth))
    leaves = sorted(frontier, key=lambda leaf: leaf.residue)
    if max_frontier is not None:
        leaves = leaves[:max_frontier]
    partitions: dict[int, list[int]] = {offset: [] for offset in range(stride)}
    for index, leaf in enumerate(leaves):
        if leaf.residue > 1:
            partitions[index % stride].append(leaf.residue)
    return partitions, {
        **stats,
        "selected_count": len(leaves),
        "sample_stride": stride,
        "sample_offset": "partitioned",
        "max_frontier": max_frontier,
    }


def starts_from_frontier(
    *,
    base_depth: int,
    max_depth: int,
    sample_stride: int,
    sample_offsets: list[int],
    max_frontier: int | None,
) -> tuple[list[int], dict[str, object]]:
    partitions, meta = frontier_partitions(
        base_depth=base_depth,
        max_depth=max_depth,
        stride=sample_stride,
        max_frontier=max_frontier,
    )
    starts: list[int] = []
    per_offset = {}
    for offset in sample_offsets:
        values = partitions[offset]
        starts.extend(values)
        per_offset[str(offset)] = len(values)
    return unique_preserving_order(starts), {**meta, "sample_offsets": sample_offsets, "per_offset_count": per_offset}


def min_credit_required(max_excess: float) -> int:
    if max_excess >= 1.0:
        return math.ceil(max(0.0, max_excess - 0.999))
    return 0


def update_excess(odd_steps: int, step: int, max_excess: float) -> tuple[float, float]:
    current_excess = odd_steps - THETA * step
    return current_excess, max(max_excess, current_excess)


def analyze_start(start: int, max_steps: int) -> dict[str, object]:
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
            "low_rank_drop_credit": 0,
            "combined_unit_credit": 0,
            "combined_rank_credit": 0,
            "unit_credit_sufficient": True,
            "rank_credit_sufficient": True,
        }

    current = original
    step = 0
    odd_steps = 0
    max_excess = 0.0
    final_excess = 0.0

    high_ladder_count = 0
    high_ladder_credit = 0
    high_alignment_counts: Counter[int] = Counter()
    high_formula_failures = 0
    high_alignment_burn_failures = 0
    max_high_align = 0
    max_even_chain = 0

    low_repeat_count = 0
    low_repeat_credit = 0
    low_rank_drop_credit = 0
    low_repeat_law_failures = 0
    max_minus5_align = 0
    odd3_branch_counts: Counter[str] = Counter()
    macro_counts: Counter[str] = Counter()

    while step < max_steps and current > 1:
        if current < original and step >= 3:
            break

        if current & 1:
            align = v2(current + 1)
            if align >= 3:
                q = (current + 1) >> align
                high_ladder_count += 1
                high_ladder_credit += align - 2
                high_alignment_counts[align] += 1
                max_high_align = max(max_high_align, align)
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
                    low_rank_drop_credit += 3
                    if not bool(info["repeat_law_ok"]):
                        low_repeat_law_failures += 1
        else:
            macro_counts["even_halving"] += 1

        current, parity = shortcut_step(current)
        step += 1
        odd_steps += parity
        final_excess, max_excess = update_excess(odd_steps, step, max_excess)

    certified = current < original
    required = min_credit_required(max_excess)
    combined_unit_credit = high_ladder_credit + low_repeat_credit
    combined_rank_credit = high_ladder_credit + low_rank_drop_credit
    class_name = "uncertified"
    if certified:
        if max_high_align >= 3:
            class_name = "high-assisted-descent"
        elif low_repeat_count:
            class_name = "low-repeat-descent"
        else:
            class_name = "low-direct-descent"

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
        "low_rank_drop_credit": low_rank_drop_credit,
        "low_repeat_law_failure_count": low_repeat_law_failures,
        "max_minus5_align": max_minus5_align,
        "odd3_branch_counts": dict(sorted(odd3_branch_counts.items())),
        "macro_counts": dict(sorted(macro_counts.items())),
        "combined_unit_credit": combined_unit_credit,
        "combined_rank_credit": combined_rank_credit,
        "unit_credit_sufficient": combined_unit_credit >= required,
        "rank_credit_sufficient": combined_rank_credit >= required,
        "unit_credit_surplus": combined_unit_credit - required,
        "rank_credit_surplus": combined_rank_credit - required,
    }


def merge_counter(rows: list[dict[str, object]], key: str) -> dict[str, int]:
    merged: Counter[str] = Counter()
    for row in rows:
        for name, value in dict(row[key]).items():
            merged[str(name)] += int(value)
    return dict(sorted(merged.items(), key=lambda item: item[0]))


def summarize(rows: list[dict[str, object]]) -> dict[str, object]:
    if not rows:
        return {"count": 0}
    return {
        "count": len(rows),
        "certified_count": sum(1 for row in rows if row["certified"]),
        "escape_max": max(int(row["escape_d"]) for row in rows),
        "steps_per_bit_max": round_float(max(float(row["steps_per_bit"]) for row in rows)),
        "max_excess": round_float(max(float(row["max_excess"]) for row in rows)),
        "min_unit_credit_surplus": min(int(row["unit_credit_surplus"]) for row in rows),
        "min_rank_credit_surplus": min(int(row["rank_credit_surplus"]) for row in rows),
        "unit_credit_failure_count": sum(1 for row in rows if not row["unit_credit_sufficient"]),
        "rank_credit_failure_count": sum(1 for row in rows if not row["rank_credit_sufficient"]),
        "high_ladder_credit_total": sum(int(row["high_ladder_credit"]) for row in rows),
        "low_repeat_credit_total": sum(int(row["low_repeat_credit"]) for row in rows),
        "low_rank_drop_credit_total": sum(int(row["low_rank_drop_credit"]) for row in rows),
        "high_formula_failure_count": sum(int(row["high_formula_failure_count"]) for row in rows),
        "high_alignment_burn_failure_count": sum(int(row["high_alignment_burn_failure_count"]) for row in rows),
        "low_repeat_law_failure_count": sum(int(row["low_repeat_law_failure_count"]) for row in rows),
        "macro_counts": merge_counter(rows, "macro_counts"),
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
        "explicit_starts": parse_ints(args.starts),
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

    unit_failures = [row for row in rows if not row["unit_credit_sufficient"]]
    rank_failures = [row for row in rows if not row["rank_credit_sufficient"]]
    uncertified = [row for row in rows if not row["certified"]]

    return {
        "status": "branch-potential-analysis",
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
        "frontier_selection": frontier_meta,
        "total_checked": len(rows),
        "class_counts": dict(sorted(Counter(str(row["class"]) for row in rows).items())),
        "group_class_counts": {
            name: dict(sorted(Counter(str(row["class"]) for row in members).items()))
            for name, members in sorted(by_group.items())
        },
        "class_summaries": {name: summarize(members) for name, members in sorted(by_class.items())},
        "global_summary": summarize(rows),
        "failure_counts": {
            "uncertified": len(uncertified),
            "unit_credit": len(unit_failures),
            "rank_credit": len(rank_failures),
        },
        "largest_unit_credit_failures": top_rows(unit_failures, "max_excess", args.top_n),
        "largest_rank_credit_failures": top_rows(rank_failures, "max_excess", args.top_n),
        "tightest_unit_surplus": sorted(rows, key=lambda row: (int(row["unit_credit_surplus"]), -float(row["max_excess"])))[: args.top_n],
        "tightest_rank_surplus": sorted(rows, key=lambda row: (int(row["rank_credit_surplus"]), -float(row["max_excess"])))[: args.top_n],
        "largest_combined_credit": top_rows(rows, "combined_unit_credit", args.top_n),
        "interpretation": (
            "Finite bridge test for the candidate global potential: exact high "
            "ladder credit plus exact low minus-five repeat credit. Unit repeat "
            "credit counts one credit per -5 mod 64 repeat; rank repeat credit "
            "counts the exact v2(x+5) drop of three bits. Any remaining failure "
            "is a concrete obstruction to this simple combined potential."
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

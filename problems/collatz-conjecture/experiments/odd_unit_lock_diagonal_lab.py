#!/usr/bin/env python3
"""Diagonal target-growth test for odd-unit locks.

Fixed finite target libraries eventually thin at high 2-adic precision.  That
is useful, but partly tautological.  The harder question is whether deeper
target spines add residue locks quickly enough to refill the odd-unit space.

This lab fixes a source-spine library, grows the target-spine library by depth,
and measures lock coverage at several precision levels.

Finite measurement only; the Collatz conjecture remains open.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from time import perf_counter

sys.path.insert(0, str(Path(__file__).resolve().parent))

from odd_unit_lock_coverage_lab import (
    build_lock_sets,
    enumerate_supercritical_cycles,
    primitive_period,
    spine,
    summarize_lock_sets,
    word_string,
)

SCRIPT_DIR = Path(__file__).resolve().parent


def parse_int_list(raw: str) -> list[int]:
    values = sorted({int(part.strip()) for part in raw.split(",") if part.strip()})
    if not values:
        raise argparse.ArgumentTypeError("expected comma-separated integers")
    return values


def primitive_cycles_between(
    cycles: list[tuple[int, ...]],
    min_depth: int,
    max_depth: int,
) -> list[tuple[int, ...]]:
    return [
        w
        for w in cycles
        if min_depth <= len(w) <= max_depth and primitive_period(w) == len(w)
    ]


def unique_target_items(cycles: list[tuple[int, ...]]) -> list[tuple[str, object]]:
    by_spine = {}
    for w in cycles:
        by_spine.setdefault(spine(w), word_string(w))
    return [(label, eta) for eta, label in sorted(by_spine.items(), key=lambda item: (len(item[1]), item[1]))]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-max-depth", type=int, default=10)
    parser.add_argument("--source-min-depth", type=int, default=3)
    parser.add_argument("--target-min-depth", type=int, default=1)
    parser.add_argument("--target-depths", type=parse_int_list, default=parse_int_list("10,12,14,15"))
    parser.add_argument("--bits", type=parse_int_list, default=parse_int_list("12,16,20"))
    parser.add_argument(
        "--output",
        type=Path,
        default=SCRIPT_DIR / "results" / "odd_unit_lock_diagonal_s10_t15_20260705.json",
    )
    args = parser.parse_args()

    start = perf_counter()
    max_target_depth = max(args.target_depths)
    cycles = enumerate_supercritical_cycles(max_target_depth)
    sources = primitive_cycles_between(cycles, args.source_min_depth, args.source_max_depth)

    rows = []
    previous_by_bit: dict[int, dict[str, float | int]] = {}
    for target_depth in args.target_depths:
        target_cycles = primitive_cycles_between(cycles, args.target_min_depth, target_depth)
        targets = unique_target_items(target_cycles)
        construction, lock_sets = build_lock_sets(sources, targets, args.bits)
        coverage = summarize_lock_sets(sources, lock_sets, args.bits)
        bit_rows = {}
        for bits in args.bits:
            row = coverage[str(bits)]
            densest = row["densest_bins"][0] if row["densest_bins"] else {}
            target_summary = {
                "target_depth": target_depth,
                "bits": bits,
                "target_spines": len(targets),
                "source_phase_target_pairs": construction["source_phase_target_pairs"],
                "max_coverage_fraction": row["max_coverage_fraction"],
                "avg_coverage_fraction_all_bins": row["avg_coverage_fraction_all_bins"],
                "avg_coverage_fraction_nonempty_bins": row[
                    "avg_coverage_fraction_nonempty_bins"
                ],
                "min_codimension_bits_nonempty": row["min_codimension_bits_nonempty"],
                "avg_codimension_bits_nonempty": row["avg_codimension_bits_nonempty"],
                "saturated_alignment_bins": row["saturated_alignment_bins"],
                "densest_distinct_lock_residues": densest.get("distinct_lock_residues"),
                "densest_source": densest.get("source"),
                "densest_source_length": densest.get("source_length"),
                "densest_alignment_class_m_mod_d": densest.get(
                    "alignment_class_m_mod_d"
                ),
            }
            prior = previous_by_bit.get(bits)
            if prior:
                old_avg = float(prior["avg_coverage_fraction_all_bins"])
                old_max = float(prior["max_coverage_fraction"])
                target_summary["avg_coverage_multiplier_from_previous_depth"] = (
                    round(target_summary["avg_coverage_fraction_all_bins"] / old_avg, 6)
                    if old_avg
                    else None
                )
                target_summary["max_coverage_multiplier_from_previous_depth"] = (
                    round(target_summary["max_coverage_fraction"] / old_max, 6)
                    if old_max
                    else None
                )
            bit_rows[str(bits)] = target_summary
            previous_by_bit[bits] = target_summary

        rows.append(
            {
                "target_depth": target_depth,
                "target_spines": len(targets),
                "source_phase_target_pairs": construction["source_phase_target_pairs"],
                "valuation_histogram": construction["valuation_histogram"],
                "coverage_by_bits": bit_rows,
            }
        )

    result = {
        "status": "finite measurement only; not a proof of Collatz",
        "parameters": {
            "source_min_depth": args.source_min_depth,
            "source_max_depth": args.source_max_depth,
            "target_min_depth": args.target_min_depth,
            "target_depths": args.target_depths,
            "bits": args.bits,
        },
        "source_counts": {
            "primitive_source_cycles": len(sources),
            "source_alignment_bins": sum(len(w) for w in sources),
        },
        "rows": rows,
        "runtime_seconds": round(perf_counter() - start, 6),
    }

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    print(f"wrote {args.output}")
    print(json.dumps(result["source_counts"], indent=2, sort_keys=True))
    for row in rows:
        parts = []
        for bits in args.bits:
            b = row["coverage_by_bits"][str(bits)]
            parts.append(
                "R={bits}:avg={avg} max={maxv}".format(
                    bits=bits,
                    avg=b["avg_coverage_fraction_all_bins"],
                    maxv=b["max_coverage_fraction"],
                )
            )
        print(f"T<={row['target_depth']} targets={row['target_spines']} " + " ".join(parts))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

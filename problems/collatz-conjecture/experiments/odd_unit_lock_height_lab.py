#!/usr/bin/env python3
"""Exact-height odd-unit lock lab.

Earlier odd-unit labs grouped source alignment by m mod d.  That is a useful
upper envelope, but a real orbit has an actual alignment height m.  If it burns
q full source periods before colliding with target phase t, then

    m = t + e + q d,     e = v2(rho_t - eta),

and the odd-unit lock uses odd-prefix a(t) + q o, not just a(t).  This lab
measures the exact-height lock union with that q-dependent power of 3 included.

Finite measurement only; the Collatz conjecture remains open.
"""

from __future__ import annotations

import argparse
import json
import math
import sys
from collections import defaultdict
from pathlib import Path
from statistics import mean
from time import perf_counter

sys.path.insert(0, str(Path(__file__).resolve().parent))

from odd_unit_lock_coverage_lab import (
    enumerate_supercritical_cycles,
    lock_residue,
    phase_data,
    primitive_period,
    spine,
    v2_fraction,
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


def build_height_lock_sets(
    sources: list[tuple[int, ...]],
    targets: list[tuple[str, object]],
    bits: list[int],
    min_height: int,
    max_height: int,
) -> tuple[dict[str, object], dict[tuple[str, int, int], set[int]]]:
    lock_sets: dict[tuple[str, int, int], set[int]] = defaultdict(set)
    phase_target_pairs = 0
    emitted_height_locks = 0
    max_seen_e = 0
    examples = []

    for source in sources:
        source_label = word_string(source)
        d = len(source)
        source_odd_count = sum(source)
        for phase in phase_data(source):
            t = int(phase["t"])
            rho_t = phase["rho"]
            odd_prefix = int(phase["odd_prefix"])
            for target_label, eta in targets:
                if rho_t == eta:
                    continue
                phase_target_pairs += 1
                e = v2_fraction(rho_t - eta)
                max_seen_e = max(max_seen_e, e)
                base_height = t + e
                if base_height > max_height:
                    continue
                first_height = base_height
                if first_height < min_height:
                    steps = (min_height - first_height + d - 1) // d
                    first_height += steps * d
                for height in range(first_height, max_height + 1, d):
                    q = (height - base_height) // d
                    total_odd_prefix = odd_prefix + q * source_odd_count
                    for bit_depth in bits:
                        residue = lock_residue(rho_t, eta, e, total_odd_prefix, bit_depth)
                        lock_sets[(source_label, height, bit_depth)].add(residue)
                    emitted_height_locks += 1
                    if len(examples) < 12:
                        examples.append(
                            {
                                "source": source_label,
                                "target": target_label,
                                "phase_t": t,
                                "valuation_e": e,
                                "height_m": height,
                                "period_burn_q": q,
                                "source_odd_count": source_odd_count,
                            }
                        )

    return (
        {
            "phase_target_pairs": phase_target_pairs,
            "emitted_height_locks": emitted_height_locks,
            "max_seen_valuation_e": max_seen_e,
            "examples": examples,
        },
        lock_sets,
    )


def summarize_by_height(
    source_labels: dict[str, int],
    lock_sets: dict[tuple[str, int, int], set[int]],
    bits: list[int],
    min_height: int,
    max_height: int,
) -> dict[str, object]:
    by_bits = {}
    densest = []

    for bit_depth in bits:
        total_odd_units = 1 << (bit_depth - 1)
        height_rows = []
        all_fractions = []
        for height in range(min_height, max_height + 1):
            counts = []
            fractions = []
            for source_label in source_labels:
                count = len(lock_sets.get((source_label, height, bit_depth), set()))
                counts.append(count)
                fraction = count / total_odd_units
                fractions.append(fraction)
                all_fractions.append(fraction)
                if count:
                    densest.append(
                        {
                            "bits": bit_depth,
                            "height_m": height,
                            "source": source_label,
                            "source_length": source_labels[source_label],
                            "distinct_lock_residues": count,
                            "coverage_fraction": round(fraction, 12),
                            "codimension_bits": round((bit_depth - 1) - math.log2(count), 6),
                            "sample_residues": sorted(
                                lock_sets[(source_label, height, bit_depth)]
                            )[:12],
                        }
                    )
            nonzero = [value for value in counts if value]
            height_rows.append(
                {
                    "height_m": height,
                    "sources": len(counts),
                    "nonzero_sources": len(nonzero),
                    "max_distinct_lock_residues": max(counts, default=0),
                    "avg_distinct_lock_residues_all_sources": round(mean(counts), 6)
                    if counts
                    else 0.0,
                    "avg_distinct_lock_residues_nonzero_sources": round(mean(nonzero), 6)
                    if nonzero
                    else 0.0,
                    "max_coverage_fraction": round(max(fractions, default=0.0), 12),
                    "avg_coverage_fraction_all_sources": round(mean(fractions), 12)
                    if fractions
                    else 0.0,
                }
            )

        by_bits[str(bit_depth)] = {
            "max_coverage_fraction": round(max(all_fractions, default=0.0), 12),
            "avg_coverage_fraction_all_source_heights": round(mean(all_fractions), 12)
            if all_fractions
            else 0.0,
            "height_rows": height_rows,
        }

    densest.sort(
        key=lambda row: (
            -row["coverage_fraction"],
            row["bits"],
            row["height_m"],
            row["source_length"],
            row["source"],
        )
    )
    return {"by_bits": by_bits, "densest_source_height_bins": densest[:20]}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-max-depth", type=int, default=10)
    parser.add_argument("--source-min-depth", type=int, default=3)
    parser.add_argument("--target-max-depth", type=int, default=16)
    parser.add_argument("--target-min-depth", type=int, default=1)
    parser.add_argument("--min-height", type=int, default=0)
    parser.add_argument("--max-height", type=int, default=48)
    parser.add_argument("--bits", type=parse_int_list, default=parse_int_list("16,20,24"))
    parser.add_argument(
        "--output",
        type=Path,
        default=SCRIPT_DIR / "results" / "odd_unit_lock_height_s10_t16_h48_20260705.json",
    )
    args = parser.parse_args()

    start = perf_counter()
    cycles = enumerate_supercritical_cycles(args.target_max_depth)
    sources = primitive_cycles_between(cycles, args.source_min_depth, args.source_max_depth)
    targets = unique_target_items(
        primitive_cycles_between(cycles, args.target_min_depth, args.target_max_depth)
    )
    source_labels = {word_string(w): len(w) for w in sources}
    construction, lock_sets = build_height_lock_sets(
        sources, targets, args.bits, args.min_height, args.max_height
    )
    summary = summarize_by_height(
        source_labels, lock_sets, args.bits, args.min_height, args.max_height
    )

    result = {
        "status": "finite measurement only; not a proof of Collatz",
        "parameters": {
            "source_min_depth": args.source_min_depth,
            "source_max_depth": args.source_max_depth,
            "target_min_depth": args.target_min_depth,
            "target_max_depth": args.target_max_depth,
            "min_height": args.min_height,
            "max_height": args.max_height,
            "bits": args.bits,
        },
        "cycle_counts": {
            "primitive_source_cycles": len(sources),
            "source_alignment_bins": sum(len(w) for w in sources),
            "unique_target_spines": len(targets),
        },
        "construction": construction,
        "height_summary": summary,
        "runtime_seconds": round(perf_counter() - start, 6),
    }

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    print(f"wrote {args.output}")
    print(json.dumps(result["cycle_counts"], indent=2, sort_keys=True))
    for bit_depth in args.bits:
        row = summary["by_bits"][str(bit_depth)]
        print(
            "R={bits}: max={max_cov} avg={avg_cov}".format(
                bits=bit_depth,
                max_cov=row["max_coverage_fraction"],
                avg_cov=row["avg_coverage_fraction_all_source_heights"],
            )
        )
    print(f"max seen valuation e: {construction['max_seen_valuation_e']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

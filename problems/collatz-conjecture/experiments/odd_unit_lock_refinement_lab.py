#!/usr/bin/env python3
"""Odd-unit lock refinement lab.

The coverage lab asks how much odd-unit space is covered at one precision R.
This lab asks whether that coverage refills when R is increased.

For a source/alignment bin, compare lock residues modulo 2^R_low and 2^R_high.
Every high-precision lock projects to a low-precision lock, so the question is
not whether low residues survive.  They should.  The question is whether each
low residue fills all 2^(R_high-R_low) possible odd lifts.  If not, higher
precision imposes fresh codimension.

Finite measurement only; the Collatz conjecture remains open.
"""

from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path
from statistics import mean
from time import perf_counter

sys.path.insert(0, str(Path(__file__).resolve().parent))

from odd_unit_lock_coverage_lab import (
    build_lock_sets,
    enumerate_supercritical_cycles,
    primitive_period,
    spine,
    word_string,
)

SCRIPT_DIR = Path(__file__).resolve().parent


def parse_bits(raw: str) -> list[int]:
    bits = sorted({int(part.strip()) for part in raw.split(",") if part.strip()})
    if len(bits) < 2 or bits[0] < 2:
        raise argparse.ArgumentTypeError("need at least two comma-separated bit depths >= 2")
    return bits


def quantiles(values: list[float]) -> dict[str, float | None]:
    if not values:
        return {"min": None, "p10": None, "median": None, "p90": None, "max": None}
    xs = sorted(values)

    def pick(frac: float) -> float:
        return xs[min(len(xs) - 1, max(0, round(frac * (len(xs) - 1))))]

    return {
        "min": round(xs[0], 6),
        "p10": round(pick(0.10), 6),
        "median": round(pick(0.50), 6),
        "p90": round(pick(0.90), 6),
        "max": round(xs[-1], 6),
    }


def linear_slope(points: list[tuple[int, float]]) -> float | None:
    if len(points) < 2:
        return None
    xs = [float(x) for x, _ in points]
    ys = [float(y) for _, y in points]
    xbar = mean(xs)
    ybar = mean(ys)
    denom = sum((x - xbar) ** 2 for x in xs)
    if denom == 0:
        return None
    return sum((x - xbar) * (y - ybar) for x, y in zip(xs, ys)) / denom


def refinement_summary(
    source_lengths: dict[str, int],
    lock_sets: dict[tuple[str, int, int], set[int]],
    bits: list[int],
) -> dict[str, object]:
    transitions: dict[str, object] = {}
    slope_rows: list[dict[str, object]] = []
    projection_leaks: list[dict[str, object]] = []

    for low, high in zip(bits, bits[1:]):
        delta = high - low
        full_lift_factor = 1 << delta
        rows: list[dict[str, object]] = []
        incremental_losses: list[float] = []
        lift_densities: list[float] = []
        branching_factors: list[float] = []

        for source, d in source_lengths.items():
            for m_class in range(d):
                low_set = lock_sets.get((source, m_class, low), set())
                high_set = lock_sets.get((source, m_class, high), set())
                if not low_set and not high_set:
                    continue
                projected_high = {residue % (1 << low) for residue in high_set}
                leaks = sorted(projected_high - low_set)
                if leaks:
                    projection_leaks.append(
                        {
                            "source": source,
                            "alignment_class_m_mod_d": m_class,
                            "low_bits": low,
                            "high_bits": high,
                            "leak_count": len(leaks),
                            "sample_leaks": leaks[:12],
                        }
                    )

                low_count = len(low_set)
                high_count = len(high_set)
                possible_lifts = low_count * full_lift_factor
                if low_count == 0 or high_count == 0:
                    continue
                branching = high_count / low_count
                lift_density = high_count / possible_lifts
                incremental_loss = math.log2(possible_lifts / high_count)
                rows.append(
                    {
                        "source": source,
                        "source_length": d,
                        "alignment_class_m_mod_d": m_class,
                        "low_lock_count": low_count,
                        "high_lock_count": high_count,
                        "full_lift_factor": full_lift_factor,
                        "observed_branching_factor": round(branching, 6),
                        "lift_density_fraction": round(lift_density, 12),
                        "incremental_codimension_bits": round(incremental_loss, 6),
                    }
                )
                branching_factors.append(branching)
                lift_densities.append(lift_density)
                incremental_losses.append(incremental_loss)

        rows.sort(
            key=lambda row: (
                row["incremental_codimension_bits"],
                row["source_length"],
                row["source"],
                row["alignment_class_m_mod_d"],
            )
        )
        transitions[f"{low}->{high}"] = {
            "bins": len(rows),
            "full_lift_factor": full_lift_factor,
            "avg_observed_branching_factor": round(mean(branching_factors), 6)
            if branching_factors
            else None,
            "avg_lift_density_fraction": round(mean(lift_densities), 12)
            if lift_densities
            else None,
            "avg_incremental_codimension_bits": round(mean(incremental_losses), 6)
            if incremental_losses
            else None,
            "incremental_codimension_quantiles": quantiles(incremental_losses),
            "weakest_incremental_loss_bins": rows[:12],
            "strongest_incremental_loss_bins": list(reversed(rows[-12:])),
        }

    for source, d in source_lengths.items():
        for m_class in range(d):
            points: list[tuple[int, float]] = []
            counts: dict[str, int] = {}
            for bit_depth in bits:
                count = len(lock_sets.get((source, m_class, bit_depth), set()))
                counts[str(bit_depth)] = count
                if count:
                    codim = (bit_depth - 1) - math.log2(count)
                    points.append((bit_depth, codim))
            slope = linear_slope(points)
            if slope is not None:
                slope_rows.append(
                    {
                        "source": source,
                        "source_length": d,
                        "alignment_class_m_mod_d": m_class,
                        "codimension_slope_bits_per_precision_bit": round(slope, 6),
                        "lock_counts_by_bits": counts,
                    }
                )

    slopes = [row["codimension_slope_bits_per_precision_bit"] for row in slope_rows]
    slope_rows.sort(
        key=lambda row: (
            row["codimension_slope_bits_per_precision_bit"],
            row["source_length"],
            row["source"],
            row["alignment_class_m_mod_d"],
        )
    )

    return {
        "transitions": transitions,
        "projection_leak_count": len(projection_leaks),
        "projection_leaks": projection_leaks[:20],
        "codimension_slope_quantiles": quantiles([float(x) for x in slopes]),
        "weakest_codimension_slope_bins": slope_rows[:12],
        "strongest_codimension_slope_bins": list(reversed(slope_rows[-12:])),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-depth", type=int, default=13)
    parser.add_argument("--min-source-depth", type=int, default=3)
    parser.add_argument("--bits", type=parse_bits, default=parse_bits("8,12,16,20"))
    parser.add_argument(
        "--output",
        type=Path,
        default=SCRIPT_DIR / "results" / "odd_unit_lock_refinement_d13_min3_20260705.json",
    )
    args = parser.parse_args()

    start = perf_counter()
    cycles = enumerate_supercritical_cycles(args.max_depth)
    sources = [
        w for w in cycles if primitive_period(w) == len(w) and len(w) >= args.min_source_depth
    ]
    targets_by_spine = {spine(w): word_string(w) for w in sources}
    targets = [(label, eta) for eta, label in sorted(targets_by_spine.items(), key=lambda item: (len(item[1]), item[1]))]
    source_lengths = {word_string(w): len(w) for w in sources}

    construction, lock_sets = build_lock_sets(sources, targets, args.bits)
    summary = refinement_summary(source_lengths, lock_sets, args.bits)

    result = {
        "status": "finite measurement only; not a proof of Collatz",
        "parameters": {
            "max_depth": args.max_depth,
            "min_source_depth": args.min_source_depth,
            "bits": args.bits,
        },
        "cycle_counts": {
            "supercritical_necklace_cycles": len(cycles),
            "primitive_source_cycles": len(sources),
            "unique_target_spines": len(targets),
            "source_alignment_bins": sum(len(w) for w in sources),
        },
        "lock_construction": construction,
        "refinement": summary,
        "runtime_seconds": round(perf_counter() - start, 6),
    }

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    print(f"wrote {args.output}")
    print(json.dumps(result["cycle_counts"], indent=2, sort_keys=True))
    for name, row in summary["transitions"].items():
        print(
            "{name}: avg_branch={branch} avg_lift_density={density} avg_loss_bits={loss}".format(
                name=name,
                branch=row["avg_observed_branching_factor"],
                density=row["avg_lift_density_fraction"],
                loss=row["avg_incremental_codimension_bits"],
            )
        )
    print(f"projection leaks: {summary['projection_leak_count']}")
    print(
        "codim slope quantiles: "
        + json.dumps(summary["codimension_slope_quantiles"], sort_keys=True)
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

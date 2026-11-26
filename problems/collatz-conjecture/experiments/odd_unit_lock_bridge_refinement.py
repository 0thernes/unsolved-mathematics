#!/usr/bin/env python3
"""Refine measured odd-unit lock bridges to higher odd-unit precision.

`odd_unit_lock_bridge_classifier.py` explains repeated R-bit bridges by exact
affine bridge geometry. This script asks whether those measured bridge
geometries survive at higher precision:

1. lift the previous R-bit unit lock to higher-precision previous-unit locks;
2. push each lifted previous unit through the same shortcut bridge;
3. test whether the resulting current unit is also a lock at the higher R.

Finite theorem-discovery data only; not a proof of Collatz.
"""

from __future__ import annotations

import argparse
import json
import sys
from fractions import Fraction
from pathlib import Path
from time import perf_counter

sys.path.insert(0, str(Path(__file__).resolve().parent))

from lib_collatz import affine_coeffs, spine
from odd_unit_lock_coverage_lab import build_lock_sets, fraction_mod_2k, v2_fraction
from odd_unit_lock_transition_lab import make_sources, make_targets, round_float

SCRIPT_DIR = Path(__file__).resolve().parent


def parse_bits(raw: str) -> list[int]:
    bits = sorted({int(part.strip()) for part in raw.split(",") if part.strip()})
    if not bits or any(bit < 2 for bit in bits):
        raise argparse.ArgumentTypeError("bits must be comma-separated integers >= 2")
    return bits


def word_tuple(label: str) -> tuple[int, ...]:
    if not label or any(ch not in "01" for ch in label):
        raise ValueError(f"not a parity-word label: {label!r}")
    return tuple(int(ch) for ch in label)


def odd_unit_bridge_image(
    *,
    source_label: str,
    target_label: str,
    previous_alignment_m: int,
    previous_unit: int,
    gap_word: str,
) -> Fraction:
    """Return F_gap(rho0 + 2^m u) - rho1."""
    gap = word_tuple(gap_word)
    three_power, affine_c = affine_coeffs(gap)
    rho0 = spine(word_tuple(source_label))
    rho1 = spine(word_tuple(target_label))
    previous_state = rho0 + (1 << previous_alignment_m) * Fraction(previous_unit)
    return Fraction(three_power, 1 << len(gap)) * previous_state + Fraction(
        affine_c, 1 << len(gap)
    ) - rho1


def classify_refinement(
    *,
    family: dict[str, object],
    base_bits: int,
    high_bits: int,
    lock_sets: dict[tuple[str, int, int], set[int]],
) -> dict[str, object]:
    previous = family["previous_lock"]
    current = family["current_lock"]
    source0 = str(previous["source"])
    source1 = str(current["source"])
    previous_alignment_m = int(previous["alignment_m"])
    previous_alignment_class = int(family["geometry_key"].split("|")[2][1:])
    previous_unit_low = int(previous["unit_residue_mod_2^R"])
    current_alignment_class_low = int(family["geometry_key"].split("|")[6][1:])
    current_unit_low = int(current["unit_residue_mod_2^R"])
    gap_word = str(family["gap_word"])

    previous_high_locks = sorted(
        residue
        for residue in lock_sets.get((source0, previous_alignment_class, high_bits), set())
        if residue % (1 << base_bits) == previous_unit_low
    )

    lifted_rows: list[dict[str, object]] = []
    refined_repeat_count = 0
    same_geometry_repeat_count = 0
    low_projection_mismatches = 0

    for previous_unit_high in previous_high_locks:
        diff = odd_unit_bridge_image(
            source_label=source0,
            target_label=source1,
            previous_alignment_m=previous_alignment_m,
            previous_unit=previous_unit_high,
            gap_word=gap_word,
        )
        current_alignment_m = v2_fraction(diff)
        current_alignment_class = current_alignment_m % len(word_tuple(source1))
        current_unit = diff / (1 << current_alignment_m)
        current_unit_high = fraction_mod_2k(current_unit, high_bits)
        current_unit_low_projection = current_unit_high % (1 << base_bits)
        current_high_locks = lock_sets.get((source1, current_alignment_class, high_bits), set())
        current_hit = current_unit_high in current_high_locks
        same_geometry = (
            current_alignment_m == int(current["alignment_m"])
            and current_alignment_class == current_alignment_class_low
            and current_unit_low_projection == current_unit_low
        )
        refined_repeat_count += int(current_hit)
        same_geometry_repeat_count += int(current_hit and same_geometry)
        low_projection_mismatches += int(current_unit_low_projection != current_unit_low)
        lifted_rows.append(
            {
                "previous_unit_residue_mod_2^R_high": previous_unit_high,
                "current_alignment_m": current_alignment_m,
                "current_alignment_class_m_mod_d": current_alignment_class,
                "current_unit_residue_mod_2^R_high": current_unit_high,
                "current_unit_projection_mod_2^R_base": current_unit_low_projection,
                "current_high_lock_hit": current_hit,
                "same_low_geometry_projection": same_geometry,
                "current_high_lock_count_for_bin": len(current_high_locks),
            }
        )

    return {
        "high_bits": high_bits,
        "previous_high_lock_lifts": len(previous_high_locks),
        "refined_repeat_lifts": refined_repeat_count,
        "same_geometry_refined_repeat_lifts": same_geometry_repeat_count,
        "low_projection_mismatches": low_projection_mismatches,
        "all_previous_lifts_die_as_repeats": len(previous_high_locks) > 0
        and refined_repeat_count == 0,
        "lift_rows": lifted_rows[:24],
    }


def run(args: argparse.Namespace) -> dict[str, object]:
    started = perf_counter()
    classifier = json.loads(args.classifier.read_text(encoding="utf-8"))
    base_bits = int(classifier["parameters"]["excess_bits"])
    high_bits = sorted({bit for bit in args.high_bits if bit > base_bits})
    if not high_bits:
        raise SystemExit("at least one --high-bits value must exceed the classifier base bits")

    sources = make_sources(args.max_depth, args.min_source_depth)
    targets = make_targets(sources)
    _meta, lock_sets = build_lock_sets(
        [source.word for source in sources],
        targets,
        [base_bits, *high_bits],
    )

    families = []
    for family in classifier["families"]:
        refinements = [
            classify_refinement(
                family=family,
                base_bits=base_bits,
                high_bits=bit,
                lock_sets=lock_sets,
            )
            for bit in high_bits
        ]
        families.append(
            {
                "source_pair": family["source_pair"],
                "geometry_key": family["geometry_key"],
                "transition_count_at_base_bits": family["transition_count"],
                "base_fresh_quotient_bits": family["bridge_algebra"]["solution"][
                    "fresh_quotient_bits"
                ],
                "refinements": refinements,
            }
        )

    all_die = all(
        refinement["all_previous_lifts_die_as_repeats"]
        for family in families
        for refinement in family["refinements"]
    )
    if all_die:
        interpretation = (
            f"For the measured R={base_bits} repeat bridges, every "
            "higher-precision previous-lock lift tested here fails to be "
            "a higher-precision next-lock hit."
        )
    else:
        interpretation = (
            f"At least one measured R={base_bits} repeat bridge survives at a "
            "tested higher precision as an algebraic lock bridge. Use the "
            "state-lift microscope to check whether the observed merged orbit "
            "state lies in the surviving lifted residue class."
        )
    projection_mismatches = sum(
        int(refinement["low_projection_mismatches"])
        for family in families
        for refinement in family["refinements"]
    )
    return {
        "status": "odd-unit-lock-bridge-refinement",
        "result": "finite bridge refinement measurement; not a proof of Collatz",
        "elapsed_seconds": round_float(perf_counter() - started, 6),
        "inputs": {
            "classifier": str(args.classifier),
        },
        "parameters": {
            "max_depth": args.max_depth,
            "min_source_depth": args.min_source_depth,
            "base_bits": base_bits,
            "high_bits": high_bits,
        },
        "summary": {
            "families_checked": len(families),
            "all_measured_base_bridges_die_as_refined_repeats": all_die,
            "low_projection_mismatches": projection_mismatches,
            "interpretation": interpretation,
        },
        "families": families,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-depth", type=int, default=13)
    parser.add_argument("--min-source-depth", type=int, default=3)
    parser.add_argument("--high-bits", type=parse_bits, default=parse_bits("20,24"))
    parser.add_argument(
        "--classifier",
        type=Path,
        default=SCRIPT_DIR
        / "results"
        / "odd_unit_lock_bridge_classifier_d13_R16_N250000_20260705.json",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=SCRIPT_DIR
        / "results"
        / "odd_unit_lock_bridge_refinement_d13_R16_to_R20_R24_N250000_20260705.json",
    )
    parser.add_argument("--quiet", action="store_true")
    args = parser.parse_args()

    if not args.classifier.exists():
        raise SystemExit(f"classifier input not found: {args.classifier}")
    result = run(args)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    if not args.quiet:
        print(f"wrote {args.output}")
        print(json.dumps(result["summary"], indent=2, sort_keys=True))
        for family in result["families"]:
            bits = ", ".join(
                f"R={row['high_bits']}: lifts={row['previous_high_lock_lifts']} repeats={row['refined_repeat_lifts']}"
                for row in family["refinements"]
            )
            print(f"{family['source_pair']} count={family['transition_count_at_base_bits']}: {bits}")
    if not result["summary"]["all_measured_base_bridges_die_as_refined_repeats"]:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

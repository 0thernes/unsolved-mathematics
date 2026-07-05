#!/usr/bin/env python3
"""State-lift microscope for repeated odd-unit lock bridges.

Bridge refinement answers a static question: if an R-bit repeat bridge is lifted
to higher precision, does some higher-precision previous lock still map to a
higher-precision next lock?

This script adds the orbit-state question.  For each higher-precision lift it
checks whether the observed merged previous/current states from the base scan
actually lie in the lifted state residue classes.  When they do not, the bridge
may survive algebraically while escaping the finite positive-start window that
merged into the lower representative state.

Finite theorem-discovery data only; not a proof of Collatz.
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from fractions import Fraction
from pathlib import Path
from time import perf_counter

sys.path.insert(0, str(Path(__file__).resolve().parent))

from lib_collatz import spine
from odd_unit_lock_bridge_refinement import odd_unit_bridge_image, word_tuple
from odd_unit_lock_coverage_lab import build_lock_sets, fraction_mod_2k, v2_fraction
from odd_unit_lock_transition_lab import make_sources, make_targets, round_float

SCRIPT_DIR = Path(__file__).resolve().parent


def parse_bits(raw: str) -> list[int]:
    bits = sorted({int(part.strip()) for part in raw.split(",") if part.strip()})
    if not bits or any(bit < 2 for bit in bits):
        raise argparse.ArgumentTypeError("bits must be comma-separated integers >= 2")
    return bits


def first_int_key(hist: dict[str, int]) -> int:
    return int(sorted(hist, key=lambda item: (-int(hist[item]), int(item)))[0])


def unit_for_state(n: int, source_label: str, alignment_m: int, bits: int) -> int:
    diff = (Fraction(n) - spine(word_tuple(source_label))) / (1 << alignment_m)
    return fraction_mod_2k(diff, bits)


def state_residue(source_label: str, alignment_m: int, unit_residue: int, bits: int) -> int:
    state = spine(word_tuple(source_label)) + (1 << alignment_m) * Fraction(unit_residue)
    return fraction_mod_2k(state, alignment_m + bits)


def classify_family_lift(
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
    previous_m = int(previous["alignment_m"])
    current_m_base = int(current["alignment_m"])
    previous_alignment_class = int(family["geometry_key"].split("|")[2][1:])
    current_alignment_class_base = int(family["geometry_key"].split("|")[6][1:])
    previous_unit_base = int(previous["unit_residue_mod_2^R"])
    current_unit_base = int(current["unit_residue_mod_2^R"])
    gap_word = str(family["gap_word"])

    observed_previous_state = first_int_key(family["previous_state_histogram"])
    observed_current_state = first_int_key(family["current_state_histogram"])
    observed_previous_unit_high = unit_for_state(
        observed_previous_state, source0, previous_m, high_bits
    )
    observed_current_unit_high = unit_for_state(
        observed_current_state, source1, current_m_base, high_bits
    )

    previous_high_locks = sorted(
        residue
        for residue in lock_sets.get((source0, previous_alignment_class, high_bits), set())
        if residue % (1 << base_bits) == previous_unit_base
    )

    rows: list[dict[str, object]] = []
    for previous_unit_high in previous_high_locks:
        diff = odd_unit_bridge_image(
            source_label=source0,
            target_label=source1,
            previous_alignment_m=previous_m,
            previous_unit=previous_unit_high,
            gap_word=gap_word,
        )
        current_m_high = v2_fraction(diff)
        current_alignment_class_high = current_m_high % len(word_tuple(source1))
        current_unit = diff / (1 << current_m_high)
        current_unit_high = fraction_mod_2k(current_unit, high_bits)
        current_high_lock_hit = current_unit_high in lock_sets.get(
            (source1, current_alignment_class_high, high_bits), set()
        )
        previous_modulus_bits = previous_m + high_bits
        current_modulus_bits = current_m_high + high_bits
        required_previous_state = state_residue(
            source0, previous_m, previous_unit_high, high_bits
        )
        required_current_state = state_residue(
            source1, current_m_high, current_unit_high, high_bits
        )
        observed_previous_residue = observed_previous_state % (1 << previous_modulus_bits)
        observed_current_residue = observed_current_state % (1 << current_modulus_bits)
        rows.append(
            {
                "previous_unit_required": previous_unit_high,
                "previous_unit_observed_state": observed_previous_unit_high,
                "previous_observed_state_matches_required_lift": (
                    observed_previous_unit_high == previous_unit_high
                ),
                "previous_required_state_residue": required_previous_state,
                "previous_observed_state_residue": observed_previous_residue,
                "previous_state_modulus_bits": previous_modulus_bits,
                "previous_state_lift_delta": (
                    required_previous_state - observed_previous_residue
                )
                % (1 << previous_modulus_bits),
                "current_alignment_m_required": current_m_high,
                "current_alignment_class_required": current_alignment_class_high,
                "current_unit_required": current_unit_high,
                "current_unit_observed_state": observed_current_unit_high,
                "current_observed_state_matches_required_lift": (
                    current_m_high == current_m_base
                    and observed_current_unit_high == current_unit_high
                ),
                "current_high_lock_hit": current_high_lock_hit,
                "current_required_state_residue": required_current_state,
                "current_observed_state_residue": observed_current_residue,
                "current_state_modulus_bits": current_modulus_bits,
                "current_state_lift_delta": (
                    required_current_state - observed_current_residue
                )
                % (1 << current_modulus_bits),
                "same_base_geometry_projection": (
                    current_m_high == current_m_base
                    and current_alignment_class_high == current_alignment_class_base
                    and current_unit_high % (1 << base_bits) == current_unit_base
                ),
            }
        )

    return {
        "high_bits": high_bits,
        "observed_previous_state": observed_previous_state,
        "observed_current_state": observed_current_state,
        "previous_high_lock_lifts": len(previous_high_locks),
        "algebraic_refined_repeat_lifts": sum(
            int(row["current_high_lock_hit"]) for row in rows
        ),
        "observed_state_repeat_lifts": sum(
            int(
                row["current_high_lock_hit"]
                and row["previous_observed_state_matches_required_lift"]
                and row["current_observed_state_matches_required_lift"]
            )
            for row in rows
        ),
        "state_escape_lifts": sum(
            int(
                row["current_high_lock_hit"]
                and (
                    not row["previous_observed_state_matches_required_lift"]
                    or not row["current_observed_state_matches_required_lift"]
                )
            )
            for row in rows
        ),
        "lift_rows": rows,
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
            classify_family_lift(
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

    algebraic_repeats_by_bits: Counter[int] = Counter()
    observed_repeats_by_bits: Counter[int] = Counter()
    state_escapes_by_bits: Counter[int] = Counter()
    for family in families:
        for refinement in family["refinements"]:
            bit = int(refinement["high_bits"])
            algebraic_repeats_by_bits[bit] += int(
                refinement["algebraic_refined_repeat_lifts"]
            )
            observed_repeats_by_bits[bit] += int(refinement["observed_state_repeat_lifts"])
            state_escapes_by_bits[bit] += int(refinement["state_escape_lifts"])

    return {
        "status": "odd-unit-lock-bridge-state-lift",
        "result": "finite bridge state-lift measurement; not a proof of Collatz",
        "elapsed_seconds": round_float(perf_counter() - started, 6),
        "inputs": {"classifier": str(args.classifier)},
        "parameters": {
            "max_depth": args.max_depth,
            "min_source_depth": args.min_source_depth,
            "base_bits": base_bits,
            "high_bits": high_bits,
        },
        "summary": {
            "families_checked": len(families),
            "algebraic_refined_repeats_by_bits": {
                str(bit): algebraic_repeats_by_bits[bit] for bit in high_bits
            },
            "observed_state_repeats_by_bits": {
                str(bit): observed_repeats_by_bits[bit] for bit in high_bits
            },
            "state_escape_lifts_by_bits": {
                str(bit): state_escapes_by_bits[bit] for bit in high_bits
            },
            "interpretation": (
                "A bridge can persist as a higher-precision residue class while "
                "the observed low representative state falls outside that class."
            ),
        },
        "families": families,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-depth", type=int, default=13)
    parser.add_argument("--min-source-depth", type=int, default=3)
    parser.add_argument("--high-bits", type=parse_bits, default=parse_bits("18,19,20,24"))
    parser.add_argument(
        "--classifier",
        type=Path,
        default=SCRIPT_DIR
        / "results"
        / "odd_unit_lock_bridge_classifier_d13_R17_N1000000_20260705.json",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=SCRIPT_DIR
        / "results"
        / "odd_unit_lock_bridge_state_lift_d13_R17_to_R18_R19_R20_R24_N1000000_20260705.json",
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
                "R={bits}: algebraic={alg} observed={obs} escapes={esc}".format(
                    bits=row["high_bits"],
                    alg=row["algebraic_refined_repeat_lifts"],
                    obs=row["observed_state_repeat_lifts"],
                    esc=row["state_escape_lifts"],
                )
                for row in family["refinements"]
            )
            print(f"{family['source_pair']} count={family['transition_count_at_base_bits']}: {bits}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

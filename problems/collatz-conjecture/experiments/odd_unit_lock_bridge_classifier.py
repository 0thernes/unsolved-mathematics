#!/usr/bin/env python3
"""Classify repeated odd-unit lock bridges by symbolic 2-adic lift cost.

The transition microscope finds rare hit-after-hit lock families along positive
shortcut orbits. This script takes those finite transition records and derives
the exact affine bridge relation:

    n' - rho_1 = (F_gap(rho_0) - rho_1) + (3^o / 2^g) * 2^m * u

where n = rho_0 + 2^m u is the previous source-cylinder visit. If the previous
R-bit unit lock fixes u modulo 2^R, the next R-bit lock may still require fresh
quotient bits. The fresh lift cost is:

    max(0, gap_steps + next_alignment_m - previous_alignment_m)

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

from lib_collatz import affine_coeffs, spine
from odd_unit_lock_coverage_lab import fraction_mod_2k, v2_fraction
from odd_unit_lock_transition_lab import round_float

SCRIPT_DIR = Path(__file__).resolve().parent


def word_tuple(label: str) -> tuple[int, ...]:
    if not label or any(ch not in "01" for ch in label):
        raise ValueError(f"not a parity-word label: {label!r}")
    return tuple(int(ch) for ch in label)


def fraction_string(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def solve_power_two_linear(unit_step: int, rhs: int, bits: int) -> dict[str, object]:
    """Solve unit_step * k = rhs (mod 2^bits)."""
    modulus = 1 << bits
    rhs %= modulus
    if unit_step == 0:
        return {
            "solvable": rhs == 0,
            "fresh_quotient_bits": 0,
            "k_residue": 0,
            "k_modulus": 1,
            "detail": "zero coefficient",
        }

    step_v2 = 0
    reduced_step = abs(unit_step)
    while reduced_step % 2 == 0:
        reduced_step //= 2
        step_v2 += 1

    forced_divisor_bits = min(step_v2, bits)
    forced_divisor = 1 << forced_divisor_bits
    if rhs % forced_divisor:
        return {
            "solvable": False,
            "fresh_quotient_bits": None,
            "k_residue": None,
            "k_modulus": None,
            "detail": "right side is not divisible by gcd(unit_step, 2^R)",
        }

    fresh_bits = bits - forced_divisor_bits
    if fresh_bits == 0:
        return {
            "solvable": True,
            "fresh_quotient_bits": 0,
            "k_residue": 0,
            "k_modulus": 1,
            "detail": "previous lock already determines next unit modulo 2^R",
        }

    reduced_modulus = 1 << fresh_bits
    odd_coeff = (unit_step >> forced_divisor_bits) % reduced_modulus
    reduced_rhs = (rhs >> forced_divisor_bits) % reduced_modulus
    k_residue = (reduced_rhs * pow(odd_coeff, -1, reduced_modulus)) % reduced_modulus
    return {
        "solvable": True,
        "fresh_quotient_bits": fresh_bits,
        "k_residue": k_residue,
        "k_modulus": reduced_modulus,
        "detail": "next lock imposes a fresh quotient congruence",
    }


def bridge_geometry_key(row: dict[str, object]) -> str:
    previous = row["previous"]
    current = row["current"]
    segment = row["shortcut_segment"]
    return "|".join(
        [
            str(previous["source"]),
            f"m{previous['alignment_m']}",
            f"a{previous['alignment_class_m_mod_d']}",
            f"u{previous['unit_residue']}",
            str(current["source"]),
            f"m{current['alignment_m']}",
            f"a{current['alignment_class_m_mod_d']}",
            f"u{current['unit_residue']}",
            f"gap{segment['parity_word']}",
        ]
    )


def bridge_rows(transitions: list[dict[str, object]]) -> list[tuple[str, dict[str, object], int]]:
    counts: Counter[str] = Counter(bridge_geometry_key(row) for row in transitions)
    first: dict[str, dict[str, object]] = {}
    for row in transitions:
        first.setdefault(bridge_geometry_key(row), row)
    return sorted(first.items(), key=lambda item: (-counts[item[0]], item[0]))


def classify_bridge(
    geometry_key: str,
    row: dict[str, object],
    count: int,
    all_rows: list[dict[str, object]],
    bits: int,
) -> dict[str, object]:
    previous = row["previous"]
    current = row["current"]
    gap_word = word_tuple(str(row["shortcut_segment"]["parity_word"]))
    gap_steps = len(gap_word)
    three_power, affine_c = affine_coeffs(gap_word)

    source_word = word_tuple(str(previous["source"]))
    target_word = word_tuple(str(current["source"]))
    rho0 = spine(source_word)
    rho1 = spine(target_word)
    bridge_rho_offset = Fraction(three_power * rho0 + affine_c, 1 << gap_steps) - rho1

    previous_m = int(previous["alignment_m"])
    current_m = int(current["alignment_m"])
    previous_unit = int(previous["unit_residue"])
    current_unit = int(current["unit_residue"])

    previous_modulus_bits = previous_m + bits
    previous_residue = fraction_mod_2k(
        rho0 + (1 << previous_m) * Fraction(previous_unit),
        previous_modulus_bits,
    )
    current_modulus_bits = current_m + bits
    current_residue = fraction_mod_2k(
        rho1 + (1 << current_m) * Fraction(current_unit),
        current_modulus_bits,
    )

    # Work in the integer state quotient coordinate
    # n = previous_residue + 2^(previous_m + R) * k. This avoids the 2-adic
    # offset ambiguity in the rational unit coordinate.
    base_current_diff = (
        Fraction(three_power * previous_residue + affine_c, 1 << gap_steps) - rho1
    )
    base_v2 = v2_fraction(base_current_diff)
    base_current_unit = base_current_diff / (1 << current_m)
    base_current_unit_residue = fraction_mod_2k(base_current_unit, bits)

    unit_step_exponent = previous_m + bits - gap_steps - current_m
    if unit_step_exponent < 0:
        raise ValueError(
            "current alignment asks for more precision than the previous lock supplies: "
            f"{geometry_key}"
        )
    unit_step = three_power * (1 << unit_step_exponent)
    rhs = (current_unit - base_current_unit_residue) % (1 << bits)
    solution = solve_power_two_linear(unit_step, rhs, bits)
    formula_fresh_bits = max(0, gap_steps + current_m - previous_m)

    lifted_previous_modulus_bits = previous_modulus_bits + int(
        solution["fresh_quotient_bits"] or 0
    )
    lifted_previous_residue = previous_residue
    if solution["solvable"] and int(solution["fresh_quotient_bits"] or 0) > 0:
        lifted_previous_residue = (
            previous_residue
            + (1 << previous_modulus_bits) * int(solution["k_residue"])
        ) % (1 << lifted_previous_modulus_bits)

    family_rows = [item for item in all_rows if bridge_geometry_key(item) == geometry_key]
    previous_states = Counter(int(item["previous"]["n"]) for item in family_rows)
    current_states = Counter(int(item["current"]["n"]) for item in family_rows)
    starts = sorted({int(item["start"]) for item in family_rows})

    return {
        "geometry_key": geometry_key,
        "lock_signature": row["signature"],
        "source_pair": row["source_pair"],
        "transition_count": count,
        "unique_previous_states": len(previous_states),
        "unique_current_states": len(current_states),
        "previous_state_histogram": {
            str(key): value for key, value in previous_states.most_common()
        },
        "current_state_histogram": {str(key): value for key, value in current_states.most_common()},
        "starts_sample": starts[:24],
        "gap_word": "".join(str(bit) for bit in gap_word),
        "gap_steps": gap_steps,
        "gap_affine": {
            "three_power": three_power,
            "c": affine_c,
            "formula": f"({three_power}*n + {affine_c}) / 2^{gap_steps}",
        },
        "previous_lock": {
            "source": previous["source"],
            "rho": fraction_string(rho0),
            "alignment_m": previous_m,
            "unit_residue_mod_2^R": previous_unit,
            "state_residue_mod_2^(m+R)": previous_residue,
            "state_modulus_bits": previous_modulus_bits,
        },
        "current_lock": {
            "source": current["source"],
            "rho": fraction_string(rho1),
            "alignment_m": current_m,
            "unit_residue_mod_2^R": current_unit,
            "state_residue_mod_2^(m+R)": current_residue,
            "state_modulus_bits": current_modulus_bits,
        },
        "bridge_algebra": {
            "F_gap_rho0_minus_rho1": fraction_string(bridge_rho_offset),
            "base_current_diff_v2_for_k0": base_v2,
            "base_current_unit_residue_mod_2^R": base_current_unit_residue,
            "unit_step_mod_2^R": unit_step % (1 << bits),
            "unit_step_v2": unit_step_exponent,
            "rhs_needed_for_current_unit": rhs,
            "fresh_bits_formula_max_0_gap_plus_next_m_minus_previous_m": formula_fresh_bits,
            "solution": solution,
            "lifted_previous_state_residue": lifted_previous_residue,
            "lifted_previous_state_modulus_bits": lifted_previous_modulus_bits,
        },
        "checks": {
            "formula_matches_solver_fresh_bits": solution["fresh_quotient_bits"]
            == formula_fresh_bits,
            "observed_previous_states_match_base_residue": all(
                int(state) % (1 << previous_modulus_bits) == previous_residue
                for state in previous_states
            ),
            "observed_previous_states_match_lifted_residue": all(
                int(state) % (1 << lifted_previous_modulus_bits) == lifted_previous_residue
                for state in previous_states
            ),
            "observed_current_states_match_current_residue": all(
                int(state) % (1 << current_modulus_bits) == current_residue
                for state in current_states
            ),
            "base_alignment_reaches_current_alignment": base_v2 >= current_m,
        },
    }


def run(args: argparse.Namespace) -> dict[str, object]:
    started = perf_counter()
    payload = json.loads(args.input.read_text(encoding="utf-8"))
    bits = int(payload["parameters"]["excess_bits"])
    transitions = payload["scan"]["transitions"]
    rows = []
    counts = Counter(bridge_geometry_key(row) for row in transitions)
    for geometry_key, row in bridge_rows(transitions):
        rows.append(classify_bridge(geometry_key, row, counts[geometry_key], transitions, bits))

    checks_passed = all(
        all(bool(value) for value in row["checks"].values()) for row in rows
    )
    fresh_hist = Counter(
        str(row["bridge_algebra"]["solution"]["fresh_quotient_bits"]) for row in rows
    )
    return {
        "status": "odd-unit-lock-bridge-classifier",
        "result": "finite symbolic classification of measured bridges; not a proof of Collatz",
        "elapsed_seconds": round_float(perf_counter() - started, 6),
        "input": str(args.input),
        "parameters": {
            "excess_bits": bits,
            "transition_records": len(transitions),
            "bridge_geometries": len(rows),
            "coarse_lock_signatures": len({str(row["signature"]) for row in transitions}),
        },
        "summary": {
            "all_checks_passed": checks_passed,
            "fresh_quotient_bits_histogram_by_signature": dict(sorted(fresh_hist.items())),
            "max_fresh_quotient_bits": max(
                int(row["bridge_algebra"]["solution"]["fresh_quotient_bits"] or 0)
                for row in rows
            )
            if rows
            else 0,
            "interpretation": (
                "Repeated locks are not one phenomenon. Some bridge families are "
                "free once the previous lock is known; others require additional "
                "quotient bits before the next lock can occur."
            ),
        },
        "families": rows,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--input",
        type=Path,
        default=SCRIPT_DIR
        / "results"
        / "odd_unit_lock_transition_microscope_d13_R16_N250000_20260705.json",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=SCRIPT_DIR
        / "results"
        / "odd_unit_lock_bridge_classifier_d13_R16_N250000_20260705.json",
    )
    parser.add_argument("--quiet", action="store_true")
    args = parser.parse_args()

    if not args.input.exists():
        raise SystemExit(f"input not found: {args.input}")
    result = run(args)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    if not args.quiet:
        print(f"wrote {args.output}")
        print(json.dumps(result["summary"], indent=2, sort_keys=True))
        for row in result["families"]:
            print(
                "{pair}: count={count} fresh_bits={fresh} unique_prev={prev}".format(
                    pair=row["source_pair"],
                    count=row["transition_count"],
                    fresh=row["bridge_algebra"]["solution"]["fresh_quotient_bits"],
                    prev=row["unique_previous_states"],
                )
            )
    if not result["summary"]["all_checks_passed"]:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

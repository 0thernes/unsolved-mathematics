#!/usr/bin/env python3
"""Classify zero-fresh odd-unit lock bridges by alignment drift.

The bridge classifier shows which repeated lock transitions require fresh
quotient bits. This follow-up focuses on the dangerous zero-fresh bridges:
do they persist for free, or do they burn alignment height?

Finite theorem-discovery data only; not a proof of Collatz.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path
from time import perf_counter

SCRIPT_DIR = Path(__file__).resolve().parent
RESULTS_DIR = SCRIPT_DIR / "results"


DEFAULT_CLASSIFIERS = [
    RESULTS_DIR / "odd_unit_lock_bridge_classifier_d13_R16_N250000_20260705.json",
    RESULTS_DIR / "odd_unit_lock_bridge_classifier_d13_R17_N1000000_20260705.json",
    RESULTS_DIR / "odd_unit_lock_bridge_classifier_d13_R18_N1000000_20260705.json",
]

DEFAULT_REFINEMENTS = [
    RESULTS_DIR / "odd_unit_lock_bridge_refinement_d13_R16_to_R20_R24_N250000_20260705.json",
    RESULTS_DIR / "odd_unit_lock_bridge_refinement_d13_R17_to_R20_R24_N1000000_20260705.json",
    RESULTS_DIR / "odd_unit_lock_bridge_refinement_d13_R18_to_R20_R24_N1000000_20260705.json",
]


def load_json(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def family_refinement_index(paths: list[Path]) -> dict[tuple[int, str], dict[str, object]]:
    index: dict[tuple[int, str], dict[str, object]] = {}
    for path in paths:
        if not path.exists():
            continue
        payload = load_json(path)
        base_bits = int(payload["parameters"]["base_bits"])
        for family in payload.get("families", []):
            refinements = family.get("refinements", [])
            index[(base_bits, str(family["geometry_key"]))] = {
                "path": str(path),
                "base_bits": base_bits,
                "high_bits": [int(row["high_bits"]) for row in refinements],
                "previous_lifts": {
                    str(row["high_bits"]): int(row["previous_high_lock_lifts"])
                    for row in refinements
                },
                "refined_repeats": {
                    str(row["high_bits"]): int(row["refined_repeat_lifts"])
                    for row in refinements
                },
                "all_die": all(
                    bool(row["all_previous_lifts_die_as_repeats"])
                    for row in refinements
                ),
            }
    return index


def classify_mechanism(
    *,
    fresh_bits: int,
    alignment_drop: int,
    transport_reserve: int,
    offset: str,
) -> str:
    if fresh_bits > 0:
        return "positive-fresh-cost"
    if alignment_drop <= 0:
        return "zero-fresh-nondescending"
    if offset == "0" and transport_reserve == 0:
        return "zero-fresh-self-spine-burn"
    if transport_reserve == 0:
        return "zero-fresh-balanced-burn"
    return "zero-fresh-reserve-burn"


def analyze_classifier(
    path: Path,
    refinement_index: dict[tuple[int, str], dict[str, object]],
) -> list[dict[str, object]]:
    payload = load_json(path)
    bits = int(payload["parameters"]["excess_bits"])
    rows: list[dict[str, object]] = []
    for family in payload.get("families", []):
        previous_m = int(family["previous_lock"]["alignment_m"])
        current_m = int(family["current_lock"]["alignment_m"])
        gap_steps = int(family["gap_steps"])
        solution = family["bridge_algebra"]["solution"]
        fresh_bits = int(solution["fresh_quotient_bits"] or 0)
        alignment_drop = previous_m - current_m
        transport_reserve = previous_m - gap_steps - current_m
        offset = str(family["bridge_algebra"]["F_gap_rho0_minus_rho1"])
        geometry_key = str(family["geometry_key"])
        refinement = refinement_index.get((bits, geometry_key))
        rows.append(
            {
                "base_bits": bits,
                "source_pair": family["source_pair"],
                "geometry_key": geometry_key,
                "transition_count": int(family["transition_count"]),
                "gap_word": family["gap_word"],
                "gap_steps": gap_steps,
                "previous_alignment_m": previous_m,
                "current_alignment_m": current_m,
                "alignment_drop_previous_minus_current": alignment_drop,
                "transport_reserve_previous_minus_gap_minus_current": transport_reserve,
                "fresh_quotient_bits": fresh_bits,
                "offset_F_gap_rho0_minus_rho1": offset,
                "offset_v2_at_observed_base": int(
                    family["bridge_algebra"]["base_current_diff_v2_for_k0"]
                ),
                "mechanism": classify_mechanism(
                    fresh_bits=fresh_bits,
                    alignment_drop=alignment_drop,
                    transport_reserve=transport_reserve,
                    offset=offset,
                ),
                "refinement": refinement,
                "checks": {
                    "fresh_formula_matches": fresh_bits
                    == max(0, gap_steps + current_m - previous_m),
                    "zero_fresh_is_alignment_descending": fresh_bits > 0
                    or alignment_drop > 0,
                    "zero_fresh_has_no_refined_repeat_when_checked": fresh_bits > 0
                    or refinement is None
                    or bool(refinement["all_die"]),
                },
            }
        )
    return rows


def run(args: argparse.Namespace) -> dict[str, object]:
    started = perf_counter()
    refinement_index = family_refinement_index(args.refinement)
    families: list[dict[str, object]] = []
    for path in args.classifier:
        if not path.exists():
            raise SystemExit(f"classifier not found: {path}")
        families.extend(analyze_classifier(path, refinement_index))

    mechanism_counts = Counter(row["mechanism"] for row in families)
    transition_counts = Counter()
    for row in families:
        transition_counts[row["mechanism"]] += int(row["transition_count"])

    zero_fresh = [row for row in families if int(row["fresh_quotient_bits"]) == 0]
    positive_fresh = [row for row in families if int(row["fresh_quotient_bits"]) > 0]
    checks = {
        "all_fresh_formulas_match": all(
            row["checks"]["fresh_formula_matches"] for row in families
        ),
        "all_zero_fresh_alignment_descends": all(
            row["alignment_drop_previous_minus_current"] > 0 for row in zero_fresh
        ),
        "all_checked_zero_fresh_refinements_die": all(
            row["refinement"] is None or bool(row["refinement"]["all_die"])
            for row in zero_fresh
        ),
        "positive_fresh_families_exist": bool(positive_fresh),
        "zero_fresh_families_exist": bool(zero_fresh),
    }
    return {
        "status": "odd-unit-lock-alignment-drop-analyzer",
        "result": "finite bridge mechanism classification; not a proof of Collatz",
        "elapsed_seconds": round(perf_counter() - started, 6),
        "inputs": {
            "classifiers": [str(path) for path in args.classifier],
            "refinements": [str(path) for path in args.refinement if path.exists()],
        },
        "summary": {
            "families": len(families),
            "transition_records": sum(int(row["transition_count"]) for row in families),
            "zero_fresh_families": len(zero_fresh),
            "zero_fresh_transition_records": sum(
                int(row["transition_count"]) for row in zero_fresh
            ),
            "positive_fresh_families": len(positive_fresh),
            "positive_fresh_transition_records": sum(
                int(row["transition_count"]) for row in positive_fresh
            ),
            "mechanism_counts": dict(sorted(mechanism_counts.items())),
            "mechanism_transition_counts": dict(sorted(transition_counts.items())),
            "max_zero_fresh_alignment_drop": max(
                (int(row["alignment_drop_previous_minus_current"]) for row in zero_fresh),
                default=0,
            ),
            "min_zero_fresh_alignment_drop": min(
                (int(row["alignment_drop_previous_minus_current"]) for row in zero_fresh),
                default=0,
            ),
            "interpretation": (
                "In the measured bridge families, every zero-fresh bridge is "
                "alignment-descending, and every checked zero-fresh bridge dies "
                "as a repeated lock under the available R=20/R=24 refinements."
            ),
        },
        "checks": checks,
        "families": families,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--classifier",
        type=Path,
        action="append",
        default=None,
        help="Bridge classifier JSON. May be provided more than once.",
    )
    parser.add_argument(
        "--refinement",
        type=Path,
        action="append",
        default=None,
        help="Bridge refinement JSON. May be provided more than once.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=RESULTS_DIR / "odd_unit_lock_alignment_drop_20260705.json",
    )
    parser.add_argument("--quiet", action="store_true")
    args = parser.parse_args()
    if args.classifier is None:
        args.classifier = DEFAULT_CLASSIFIERS
    if args.refinement is None:
        args.refinement = DEFAULT_REFINEMENTS

    result = run(args)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    if not args.quiet:
        print(f"wrote {args.output}")
        print(json.dumps(result["summary"], indent=2, sort_keys=True))
    if not all(bool(value) for value in result["checks"].values()):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Build a machine-checkable certificate for odd-unit lock bridge collapse.

This ties together three finite instruments:

* transition microscope outputs, which count hit-after-hit lock transitions;
* bridge classifier outputs, which reduce transitions to affine geometries;
* bridge refinement outputs, which test whether those geometries survive at
  higher odd-unit precision.

The certificate is deliberately narrow. It verifies the current depth-13,
odd-start windows and records the exact collapse pattern. It is theorem
discovery scaffolding, not a proof of Collatz.
"""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from pathlib import Path
from time import perf_counter

SCRIPT_DIR = Path(__file__).resolve().parent
RESULTS_DIR = SCRIPT_DIR / "results"

TRANSITION_FILES = [
    "odd_unit_lock_transition_microscope_d13_R16_N250000_20260705.json",
    "odd_unit_lock_transition_microscope_d13_R17_N250000_20260705.json",
    "odd_unit_lock_transition_microscope_d13_R18_N250000_20260705.json",
    "odd_unit_lock_transition_microscope_d13_R19_N250000_20260705.json",
    "odd_unit_lock_transition_microscope_d13_R20_N250000_20260705.json",
    "odd_unit_lock_transition_microscope_d13_R24_N250000_20260705.json",
    "odd_unit_lock_transition_microscope_d13_R17_N1000000_20260705.json",
    "odd_unit_lock_transition_microscope_d13_R18_N1000000_20260705.json",
    "odd_unit_lock_transition_microscope_d13_R19_N1000000_20260705.json",
]

CLASSIFIER_FILES = [
    "odd_unit_lock_bridge_classifier_d13_R16_N250000_20260705.json",
    "odd_unit_lock_bridge_classifier_d13_R17_N1000000_20260705.json",
    "odd_unit_lock_bridge_classifier_d13_R18_N1000000_20260705.json",
]

REFINEMENT_FILES = [
    "odd_unit_lock_bridge_refinement_d13_R16_to_R20_R24_N250000_20260705.json",
    "odd_unit_lock_bridge_refinement_d13_R17_to_R20_R24_N1000000_20260705.json",
    "odd_unit_lock_bridge_refinement_d13_R18_to_R20_R24_N1000000_20260705.json",
]

NAME_RE = re.compile(r"_R(?P<bits>\d+)_N(?P<limit>\d+)_")


def round_float(value: float, digits: int = 12) -> float:
    return round(float(value), digits)


def load_json(path: Path) -> dict[str, object]:
    if not path.exists():
        raise FileNotFoundError(path)
    return json.loads(path.read_text(encoding="utf-8"))


def display_path(path: Path) -> str:
    """Prefer repo-relative artifact labels in generated receipts."""
    try:
        return path.resolve().relative_to(SCRIPT_DIR.parent.resolve()).as_posix()
    except ValueError:
        return str(path)


def bits_limit_from_name(path: Path) -> tuple[int, int]:
    match = NAME_RE.search(path.name)
    if not match:
        raise ValueError(f"cannot parse R/N from filename: {path.name}")
    return int(match.group("bits")), int(match.group("limit"))


def transition_rows(results_dir: Path) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for name in TRANSITION_FILES:
        path = results_dir / name
        bits, limit = bits_limit_from_name(path)
        payload = load_json(path)
        scan = payload["scan"]
        transitions = scan["transitions"]
        state_bridge_hist = Counter(
            f"{row['previous']['n']}->{row['current']['n']}" for row in transitions
        )
        rows.append(
            {
                "file": display_path(path),
                "excess_bits": bits,
                "start_limit": limit,
                "odd_starts_scanned": scan["starts_scanned"],
                "source_visits": scan["total_canonical_source_visits"],
                "lock_hits": scan["total_lock_hits"],
                "previous_hit_transitions": scan["previous_hit_transitions"],
                "hit_after_hit_transitions": scan["hit_after_hit_transitions"],
                "expected_hit_after_hit_from_local_coverage": scan[
                    "expected_hit_after_hit_from_local_coverage"
                ],
                "observed_over_expected_hit_after_hit": scan[
                    "observed_over_expected_hit_after_hit"
                ],
                "same_source_repeat_count": scan["same_source_repeat_count"],
                "different_source_repeat_count": scan["different_source_repeat_count"],
                "starts_with_repeat_count": scan["starts_with_repeat_count"],
                "state_bridge_histogram": dict(
                    sorted(state_bridge_hist.items(), key=lambda item: (-item[1], item[0]))
                ),
            }
        )
    return rows


def classifier_rows(results_dir: Path) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for name in CLASSIFIER_FILES:
        path = results_dir / name
        payload = load_json(path)
        family_rows = []
        for family in payload["families"]:
            family_rows.append(
                {
                    "source_pair": family["source_pair"],
                    "transition_count": family["transition_count"],
                    "gap_word": family["gap_word"],
                    "fresh_quotient_bits": family["bridge_algebra"]["solution"][
                        "fresh_quotient_bits"
                    ],
                    "state_bridges": {
                        "previous": family["previous_state_histogram"],
                        "current": family["current_state_histogram"],
                    },
                }
            )
        rows.append(
            {
                "file": display_path(path),
                "base_bits": payload["parameters"]["excess_bits"],
                "transition_records": payload["parameters"]["transition_records"],
                "bridge_geometries": payload["parameters"]["bridge_geometries"],
                "all_checks_passed": payload["summary"]["all_checks_passed"],
                "max_fresh_quotient_bits": payload["summary"]["max_fresh_quotient_bits"],
                "fresh_quotient_bits_histogram": payload["summary"][
                    "fresh_quotient_bits_histogram_by_signature"
                ],
                "families": family_rows,
            }
        )
    return rows


def refinement_rows(results_dir: Path) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for name in REFINEMENT_FILES:
        path = results_dir / name
        payload = load_json(path)
        total_previous_lifts = 0
        total_refined_repeats = 0
        total_same_geometry_repeats = 0
        for family in payload["families"]:
            for refinement in family["refinements"]:
                total_previous_lifts += int(refinement["previous_high_lock_lifts"])
                total_refined_repeats += int(refinement["refined_repeat_lifts"])
                total_same_geometry_repeats += int(
                    refinement["same_geometry_refined_repeat_lifts"]
                )
        rows.append(
            {
                "file": display_path(path),
                "base_bits": payload["parameters"]["base_bits"],
                "high_bits": payload["parameters"]["high_bits"],
                "families_checked": payload["summary"]["families_checked"],
                "all_measured_base_bridges_die_as_refined_repeats": payload["summary"][
                    "all_measured_base_bridges_die_as_refined_repeats"
                ],
                "low_projection_mismatches": payload["summary"][
                    "low_projection_mismatches"
                ],
                "total_previous_high_lock_lifts": total_previous_lifts,
                "total_refined_repeat_lifts": total_refined_repeats,
                "total_same_geometry_refined_repeat_lifts": total_same_geometry_repeats,
            }
        )
    return rows


def row_by_key(rows: list[dict[str, object]]) -> dict[tuple[int, int], dict[str, object]]:
    return {
        (int(row["excess_bits"]), int(row["start_limit"])): row
        for row in rows
    }


def build_checks(
    transitions: list[dict[str, object]],
    classifiers: list[dict[str, object]],
    refinements: list[dict[str, object]],
) -> list[dict[str, object]]:
    by_key = row_by_key(transitions)
    checks = []
    fixed_window_bits = [16, 17, 18, 19, 20, 24]
    stress_bits = [17, 18, 19]

    checks.append(
        {
            "name": "fixed_250k_window_has_only_R16_repeat_bridges",
            "passed": by_key[(16, 250000)]["hit_after_hit_transitions"] > 0
            and all(
                by_key[(bits, 250000)]["hit_after_hit_transitions"] == 0
                for bits in fixed_window_bits
                if bits != 16
            ),
            "detail": {
                str(bits): by_key[(bits, 250000)]["hit_after_hit_transitions"]
                for bits in fixed_window_bits
            },
        }
    )
    checks.append(
        {
            "name": "million_stress_repeats_die_by_R19",
            "passed": by_key[(17, 1000000)]["hit_after_hit_transitions"] > 0
            and by_key[(18, 1000000)]["hit_after_hit_transitions"] > 0
            and by_key[(19, 1000000)]["hit_after_hit_transitions"] == 0,
            "detail": {
                str(bits): by_key[(bits, 1000000)]["hit_after_hit_transitions"]
                for bits in stress_bits
            },
        }
    )
    r17_bridges = set(by_key[(17, 1000000)]["state_bridge_histogram"])
    r18_bridges = set(by_key[(18, 1000000)]["state_bridge_histogram"])
    checks.append(
        {
            "name": "million_stress_R18_state_bridges_are_subset_of_R17",
            "passed": bool(r18_bridges) and r18_bridges <= r17_bridges,
            "detail": {
                "R17_state_bridges": sorted(r17_bridges),
                "R18_state_bridges": sorted(r18_bridges),
            },
        }
    )
    checks.append(
        {
            "name": "all_bridge_classifier_checks_pass",
            "passed": all(row["all_checks_passed"] for row in classifiers),
            "detail": {
                str(row["base_bits"]): row["all_checks_passed"] for row in classifiers
            },
        }
    )
    checks.append(
        {
            "name": "all_refined_bridge_families_die",
            "passed": all(
                row["all_measured_base_bridges_die_as_refined_repeats"]
                and row["total_refined_repeat_lifts"] == 0
                and row["total_same_geometry_refined_repeat_lifts"] == 0
                for row in refinements
            ),
            "detail": {
                str(row["base_bits"]): {
                    "high_bits": row["high_bits"],
                    "total_previous_high_lock_lifts": row[
                        "total_previous_high_lock_lifts"
                    ],
                    "total_refined_repeat_lifts": row["total_refined_repeat_lifts"],
                    "total_same_geometry_refined_repeat_lifts": row[
                        "total_same_geometry_refined_repeat_lifts"
                    ],
                }
                for row in refinements
            },
        }
    )
    checks.append(
        {
            "name": "repeat_counts_stay_below_local_coverage_expectation",
            "passed": all(
                float(row["observed_over_expected_hit_after_hit"]) <= 1.0
                for row in transitions
            ),
            "detail": {
                f"R{row['excess_bits']}_N{row['start_limit']}": row[
                    "observed_over_expected_hit_after_hit"
                ]
                for row in transitions
            },
        }
    )
    return checks


def run(results_dir: Path) -> dict[str, object]:
    started = perf_counter()
    transitions = transition_rows(results_dir)
    classifiers = classifier_rows(results_dir)
    refinements = refinement_rows(results_dir)
    checks = build_checks(transitions, classifiers, refinements)
    all_passed = all(bool(row["passed"]) for row in checks)

    by_key = row_by_key(transitions)
    r16 = by_key[(16, 250000)]
    r17_stress = by_key[(17, 1000000)]
    r18_stress = by_key[(18, 1000000)]
    r19_stress = by_key[(19, 1000000)]

    return {
        "status": "odd-unit-lock-bridge-collapse-certificate",
        "result": "finite bridge collapse certificate; not a proof of Collatz",
        "elapsed_seconds": round_float(perf_counter() - started, 6),
        "parameters": {
            "results_dir": display_path(results_dir),
            "transition_artifacts": len(TRANSITION_FILES),
            "classifier_artifacts": len(CLASSIFIER_FILES),
            "refinement_artifacts": len(REFINEMENT_FILES),
        },
        "summary": {
            "all_checks_passed": all_passed,
            "fixed_250k_R16_repeat_transitions": r16["hit_after_hit_transitions"],
            "fixed_250k_R17_to_R24_repeat_transitions": {
                str(bits): by_key[(bits, 250000)]["hit_after_hit_transitions"]
                for bits in (17, 18, 19, 20, 24)
            },
            "million_stress_repeat_transitions": {
                "17": r17_stress["hit_after_hit_transitions"],
                "18": r18_stress["hit_after_hit_transitions"],
                "19": r19_stress["hit_after_hit_transitions"],
            },
            "million_stress_R18_state_bridges": sorted(
                r18_stress["state_bridge_histogram"]
            ),
            "refinement_base_bits_checked": [
                int(row["base_bits"]) for row in refinements
            ],
            "total_refined_repeat_lifts": sum(
                int(row["total_refined_repeat_lifts"]) for row in refinements
            ),
            "interpretation": (
                "In the checked depth-13 windows, repeated odd-unit locks are a "
                "coarse-precision bridge phenomenon: R16 repeats exist, R17/R18 "
                "stress repeats compress to tiny state bridges, and all measured "
                "bridge families fail the R20/R24 refinement test."
            ),
        },
        "checks": checks,
        "transition_rows": transitions,
        "classifier_rows": classifiers,
        "refinement_rows": refinements,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--results-dir", type=Path, default=RESULTS_DIR)
    parser.add_argument(
        "--output",
        type=Path,
        default=RESULTS_DIR / "odd_unit_lock_bridge_collapse_certificate_20260705.json",
    )
    parser.add_argument("--quiet", action="store_true")
    args = parser.parse_args()

    payload = run(args.results_dir)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    if not args.quiet:
        print(f"wrote {args.output}")
        print(json.dumps(payload["summary"], indent=2, sort_keys=True))
        for check in payload["checks"]:
            print(f"{check['name']}: {'PASS' if check['passed'] else 'FAIL'}")
    return 0 if payload["summary"]["all_checks_passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())

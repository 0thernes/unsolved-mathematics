#!/usr/bin/env python3
"""WTF regression suite for Collatz proof-route candidates.

This is an adversarial smoke test for future invariants and proof sketches. It
does not try to prove the Collatz conjecture. Its job is to keep us honest by
replaying the strangest known local controls:

* Collatz quick descent/tau checks on hard-ish starts.
* The `3n-1` false sibling, whose word statistics match `3n+1` but whose
  survivor set contains positive cycle minima.
* The `5n+1` sibling as a divergence-typical control.
* Exact high-alignment ladder identities.
* Exact phase-collision identity checks and the negative result that the phase
  gate alone is too permissive.
* Mersenne shadows of the 2-adic `-1` ghost.

Passing this suite is not evidence of a proof. Failing it is strong evidence
that a proposed mechanism is too broad, sign-blind, phase-naive, or merely
finite-table-shaped.
"""

from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path
from types import SimpleNamespace
from time import perf_counter

sys.path.insert(0, str(Path(__file__).resolve().parent))

import collatz_frontier_geometry as frontier
import collatz_epsilon_lint as epsilon_lint
import collatz_sibling_control as sibling
import spine_phase_collision_lab as phase
from lib_collatz import shortcut_step


HARD_STARTS = [
    2,
    3,
    7,
    27,
    97,
    871,
    6171,
    77031,
    837799,
]


def ok(name: str, passed: bool, detail: object) -> dict[str, object]:
    return {"name": name, "passed": bool(passed), "detail": detail}


def collatz_tau_checks(starts: list[int]) -> dict[str, object]:
    rows = []
    for n in starts:
        tau, sigma = frontier.tau_sigma(n)
        rows.append(
            {
                "n": n,
                "tau": tau,
                "sigma": sigma,
                "tau_equals_sigma": tau == sigma,
                "tau_over_log2_n": round(tau / math.log2(n), 6),
            }
        )
    return {
        "starts": rows,
        "all_tau_equals_sigma": all(row["tau_equals_sigma"] for row in rows),
        "max_tau": max(row["tau"] for row in rows),
    }


def sibling_controls(limit: int, cap: int) -> dict[str, object]:
    scan_3minus = sibling.scan_payload(3, -1, limit=limit, cap=cap, tails=[10, 20, 40, 80])
    scan_3plus = sibling.scan_payload(3, 1, limit=limit, cap=cap, tails=[10, 20, 40, 80])
    scan_5plus = sibling.scan_payload(5, 1, limit=min(limit, 2000), cap=min(cap, 512), tails=[10, 20, 40, 80])
    anchors = dict(sibling.dp_rows(3, {20, 24, 28}))

    return {
        "q3_word_system_anchors": anchors,
        "q3_word_system_anchor_match": anchors == {20: 27328, 24: 286581, 28: 3524586},
        "scan_3minus": {
            "flagged": scan_3minus["flagged_frontier_residents"],
            "terras_mismatches": scan_3minus["terras_mismatches_sigma_ne_tau"],
        },
        "scan_3plus": {
            "flagged": scan_3plus["flagged_frontier_residents"],
            "terras_mismatches": scan_3plus["terras_mismatches_sigma_ne_tau"],
        },
        "scan_5plus": {
            "flagged": scan_5plus["flagged_frontier_residents"],
            "terras_mismatches": scan_5plus["terras_mismatches_sigma_ne_tau"],
        },
    }


def high_ladder_identity(max_align: int) -> dict[str, object]:
    failures = []
    rows = []
    qs = [1, 3, 5, 17]
    for align in range(3, max_align + 1):
        for q in qs:
            x = (1 << align) * q - 1
            row = {"align": align, "q": q, "start": x, "terminal": None}
            for k in range(align + 1):
                expected = (3**k) * (1 << (align - k)) * q - 1
                if x != expected:
                    failures.append({"align": align, "q": q, "k": k, "x": x, "expected": expected})
                    break
                if k < align:
                    if not x & 1:
                        failures.append({"align": align, "q": q, "k": k, "failure": "expected odd ladder step"})
                        break
                    x = shortcut_step(x)
            row["terminal"] = x
            row["terminal_even_chain"] = v2(x)
            rows.append(row)
    return {"max_align": max_align, "failures": failures, "sample_rows": rows[:12], "checked_rows": len(rows)}


def phase_collision_probe(max_depth: int, identity_trials: int) -> dict[str, object]:
    args = SimpleNamespace(
        max_depth=max_depth,
        identity_trials=identity_trials,
        seed=20260705,
        max_excess=8,
        barrier_depths="32,64,128",
        density_max_depth=512,
        density_depths="16,64,128,256,512",
    )
    payload = phase.run(args)
    unique_gate = payload["phase_gate_unique_target_spines"]
    all_gate = payload["phase_gate_all_target_cycles"]
    return {
        "identity": payload["phase_identity"],
        "library": payload["library"],
        "unique_gate_avg_allowed_fraction": unique_gate["avg_allowed_fraction_of_m_mod_source_length"],
        "all_cycle_gate_avg_allowed_fraction": all_gate["avg_allowed_fraction_of_m_mod_source_length"],
        "minus_one_to_minus_five_all_empty": payload["minus_one_to_minus_five_mersenne_lock"]["all_empty"],
        "density_firewall_counts": payload["density_firewall_counts"],
        "interpretation": payload["interpretation"],
    }


def mersenne_shadow_probe(max_j: int) -> dict[str, object]:
    js = sorted({8, 16, 24, 32, 48, 64, max_j})
    rows = []
    for j in js:
        tau = frontier.tau_of((1 << j) - 1)
        rows.append({"j": j, "tau": tau, "tau_over_j": round(tau / j, 6)})
    ratios = [row["tau_over_j"] for row in rows if row["j"] >= max(24, max_j // 2)]
    return {
        "predicted_slope": frontier.MERSENNE_SLOPE,
        "rows": rows,
        "upper_tail_mean_tau_over_j": round(sum(ratios) / len(ratios), 6),
        "upper_tail_within_wide_model_band": all(2.5 <= ratio <= 5.0 for ratio in ratios),
    }


def epsilon_lint_probe() -> dict[str, object]:
    """Run the newer sign-aware lint gate as a sub-control.

    The WTF suite is a broad regression harness; epsilon-lint is the sharper
    proof-safety gate for eps-blind claims.  Keeping both wired together makes
    a future "passed the gauntlet" statement harder to overstate.
    """

    payload = epsilon_lint.build_payload(
        depth=8,
        trace_depth=16,
        max_start=501,
        cap=2048,
        max_align=12,
    )
    scan_rows = {
        row["world"]["id"]: row
        for row in payload["bounded_scan_controls"]["summaries"]
    }
    return {
        "pass": payload["pass"],
        "hard_failures": payload["hard_failures"],
        "word_distribution_identical": payload["word_barrier"]["word_distribution_identical"],
        "odd_count_distribution_identical": payload["word_barrier"]["odd_count_distribution_identical"],
        "three_minus_flagged_count": scan_rows["sibling_3n_minus_1"]["flagged_count"],
        "five_plus_flagged_count": scan_rows["sibling_5n_plus_1"]["flagged_count"],
        "high_ladder_formula_controls_pass": payload["high_ladder_formula_controls"]["all_formula_checks_pass"],
        "low_repeat_formula_controls_pass": payload["low_repeat_formula_controls"]["all_formula_checks_pass"],
        "lint_rules": [
            {
                "probe": row["probe"],
                "status": row["status"],
                "proof_safety_rating_0_to_10": row["proof_safety_rating_0_to_10"],
            }
            for row in payload["lint_rules"]
        ],
    }


def v2(n: int) -> int:
    if n == 0:
        return 0
    count = 0
    while n % 2 == 0:
        n //= 2
        count += 1
    return count


def run(args: argparse.Namespace) -> dict[str, object]:
    started = perf_counter()
    collatz = collatz_tau_checks(HARD_STARTS)
    controls = sibling_controls(args.sibling_limit, args.sibling_cap)
    ladder = high_ladder_identity(args.max_ladder_align)
    phase_probe = phase_collision_probe(args.phase_max_depth, args.phase_identity_trials)
    mersenne = mersenne_shadow_probe(args.mersenne_max_j)
    eps_lint = epsilon_lint_probe()

    assertions = [
        ok(
            "collatz_hard_starts_tau_equals_sigma",
            collatz["all_tau_equals_sigma"],
            {"max_tau": collatz["max_tau"]},
        ),
        ok(
            "q3_word_system_matches_frontier_anchors",
            controls["q3_word_system_anchor_match"],
            controls["q3_word_system_anchors"],
        ),
        ok(
            "3n_minus_false_sibling_flags_exact_cycle_minima",
            controls["scan_3minus"]["flagged"]["samples"] == [1, 5, 17],
            controls["scan_3minus"]["flagged"],
        ),
        ok(
            "3n_plus_collatz_has_no_quick_frontier_resident",
            controls["scan_3plus"]["flagged"]["count"] == 0,
            controls["scan_3plus"]["flagged"],
        ),
        ok(
            "5n_plus_control_flags_frontier_residents",
            controls["scan_5plus"]["flagged"]["count"] > 0,
            controls["scan_5plus"]["flagged"],
        ),
        ok(
            "high_alignment_ladder_identity_clean",
            not ladder["failures"],
            {"checked_rows": ladder["checked_rows"], "failures": ladder["failures"][:5]},
        ),
        ok(
            "phase_collision_identity_clean",
            phase_probe["identity"]["failure_count"] == 0,
            phase_probe["identity"],
        ),
        ok(
            "phase_gate_too_permissive_to_be_proof",
            phase_probe["unique_gate_avg_allowed_fraction"] > 0.5,
            {
                "unique_gate_avg_allowed_fraction": phase_probe["unique_gate_avg_allowed_fraction"],
                "all_cycle_gate_avg_allowed_fraction": phase_probe["all_cycle_gate_avg_allowed_fraction"],
            },
        ),
        ok(
            "mersenne_shadow_detaches_inside_wide_model_band",
            mersenne["upper_tail_within_wide_model_band"],
            {
                "predicted_slope": mersenne["predicted_slope"],
                "upper_tail_mean_tau_over_j": mersenne["upper_tail_mean_tau_over_j"],
            },
        ),
        ok(
            "epsilon_lint_gate_passes",
            eps_lint["pass"]
            and eps_lint["word_distribution_identical"]
            and eps_lint["odd_count_distribution_identical"]
            and eps_lint["three_minus_flagged_count"] == 3
            and eps_lint["five_plus_flagged_count"] > 0
            and eps_lint["high_ladder_formula_controls_pass"]
            and eps_lint["low_repeat_formula_controls_pass"],
            eps_lint,
        ),
    ]

    return {
        "status": "collatz-wtf-regression-suite",
        "elapsed_seconds": round(perf_counter() - started, 6),
        "parameters": {
            "sibling_limit": args.sibling_limit,
            "sibling_cap": args.sibling_cap,
            "max_ladder_align": args.max_ladder_align,
            "phase_max_depth": args.phase_max_depth,
            "phase_identity_trials": args.phase_identity_trials,
            "mersenne_max_j": args.mersenne_max_j,
        },
        "all_assertions_passed": all(item["passed"] for item in assertions),
        "assertions": assertions,
        "collatz_tau_checks": collatz,
        "sibling_controls": controls,
        "high_ladder_identity": ladder,
        "phase_collision_probe": phase_probe,
        "mersenne_shadow_probe": mersenne,
        "epsilon_lint_probe": eps_lint,
        "interpretation": (
            "This suite is a falsification harness for future proof routes. "
            "Passing means a route has survived basic weirdness controls; it "
            "does not prove Collatz. Failing identifies a concrete old trap."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--sibling-limit", type=int, default=1000)
    parser.add_argument("--sibling-cap", type=int, default=2048)
    parser.add_argument("--max-ladder-align", type=int, default=16)
    parser.add_argument("--phase-max-depth", type=int, default=8)
    parser.add_argument("--phase-identity-trials", type=int, default=1500)
    parser.add_argument("--mersenne-max-j", type=int, default=96)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--quiet", action="store_true")
    args = parser.parse_args()

    if args.sibling_limit < 17:
        raise SystemExit("--sibling-limit must include the known 3n-1 cycle minimum 17")
    if args.sibling_cap < 128:
        raise SystemExit("--sibling-cap must be at least 128")
    if args.max_ladder_align < 3:
        raise SystemExit("--max-ladder-align must be at least 3")
    if args.phase_max_depth < 3:
        raise SystemExit("--phase-max-depth must be at least 3")
    if args.phase_identity_trials < 1:
        raise SystemExit("--phase-identity-trials must be positive")
    if args.mersenne_max_j < 24:
        raise SystemExit("--mersenne-max-j must be at least 24")

    payload = run(args)
    text = json.dumps(payload, indent=2, sort_keys=True)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text + "\n", encoding="utf-8")
    if not args.quiet:
        print(text)
    if not payload["all_assertions_passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()

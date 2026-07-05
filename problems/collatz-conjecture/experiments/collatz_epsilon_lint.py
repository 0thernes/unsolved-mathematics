#!/usr/bin/env python3
"""Reusable epsilon/sibling lint harness for Collatz proof sketches.

This is a guardrail, not a proof attempt.  It turns the repo's epsilon-barrier
and sibling-control discipline into a small executable gate:

* parity-word and frontier-count probes are marked epsilon-blind;
* affine-intercept and cycle-side probes are marked epsilon-sensitive;
* every future invariant should survive the false sibling worlds before it is
  promoted to theorem language.

The shortcut family is

    T_{q,eps}(n) = n / 2            if n is even
                 = (q n + eps) / 2 if n is odd,

with q odd and eps in {+1, -1}.  Collatz is (q, eps) = (3, +1).
"""

from __future__ import annotations

import argparse
import json
import math
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from lib_collatz import parity_word as collatz_parity_word


SCRIPT_DIR = Path(__file__).resolve().parent
RESULTS_DIR = SCRIPT_DIR / "results"
DEFAULT_OUT = RESULTS_DIR / "epsilon_lint.json"
RETIME_TIGHT_FILE = RESULTS_DIR / "branch_prefix_retimed_tight_layer_one_d18_d25_20260702.json"

KNOWN_CYCLE_MINIMA: dict[tuple[int, int], list[int]] = {
    (3, 1): [1],
    (3, -1): [1, 5, 17],
    (5, 1): [1, 13, 17],
}

COLLATZ_STRESS_STARTS = [1, 3, 5, 7, 27, 703, 10087, 35655, 77031, 837799]

WORLDS: list[dict[str, Any]] = [
    {
        "id": "collatz_3n_plus_1",
        "q": 3,
        "eps": 1,
        "role": "target world",
        "status": "open positive-orbit conjecture",
    },
    {
        "id": "sibling_3n_minus_1",
        "q": 3,
        "eps": -1,
        "role": "epsilon control",
        "status": "false analogue with positive cycles",
    },
    {
        "id": "sibling_5n_plus_1",
        "q": 5,
        "eps": 1,
        "role": "multiplier control",
        "status": "hostile analogue with known nontrivial cycles and long frontier residents",
    },
]


def step(q: int, eps: int, n: int) -> int:
    if q % 2 != 1 or eps not in (-1, 1):
        raise ValueError("q must be odd and eps must be +/-1")
    return (q * n + eps) // 2 if n & 1 else n // 2


def v2(n: int) -> int | None:
    if n == 0:
        return None
    n = abs(n)
    k = 0
    while n % 2 == 0:
        k += 1
        n //= 2
    return k


def parity_word(q: int, eps: int, start: int, depth: int) -> tuple[int, ...]:
    x = start
    word: list[int] = []
    for _ in range(depth):
        word.append(x & 1)
        x = step(q, eps, x)
    return tuple(word)


def affine_trace(q: int, eps: int, start: int, depth: int) -> dict[str, Any]:
    """Trace exact affine data for T^d(start).

    If the parity word has o odd steps, then

        T^d(n) = (q^o n + c_d) / 2^d.

    The coefficient q^o is epsilon-blind; the intercept c_d carries the sign
    of eps whenever an odd step has occurred.
    """

    x = start
    coeff = 1
    intercept = 0
    word: list[int] = []
    high_ladder_hits = 0
    high_ladder_sign_paired_hits = 0
    low_repeat_hits = 0
    low_repeat_sign_paired_hits = 0
    min_prefix_margin_bits: float | None = None
    odd_count = 0

    for j in range(1, depth + 1):
        if x % 64 == 59:
            low_repeat_hits += 1
        if (x + 5 * eps) % 64 == 0:
            low_repeat_sign_paired_hits += 1
        a = v2(x + 1)
        if a is not None and a >= 3:
            high_ladder_hits += 1
        signed_a = v2(x + eps)
        if signed_a is not None and signed_a >= 3:
            high_ladder_sign_paired_hits += 1

        bit = x & 1
        word.append(bit)
        if bit:
            odd_count += 1
            intercept = q * intercept + eps * (1 << (j - 1))
            coeff *= q
        x = step(q, eps, x)

        margin = odd_count * math.log2(q) - j
        min_prefix_margin_bits = margin if min_prefix_margin_bits is None else min(min_prefix_margin_bits, margin)

        denom = 1 << j
        if coeff * start + intercept != denom * x:
            raise AssertionError(
                f"affine identity failed for q={q}, eps={eps}, start={start}, depth={j}"
            )

    sign = 0 if intercept == 0 else (1 if intercept > 0 else -1)
    return {
        "q": q,
        "eps": eps,
        "start": start,
        "depth": depth,
        "end": x,
        "word": "".join(str(b) for b in word),
        "odd_steps": odd_count,
        "coefficient": coeff,
        "intercept": intercept,
        "intercept_sign": sign,
        "intercept_sign_matches_eps": odd_count == 0 or sign == eps,
        "multiplier_excess_bits": round(odd_count * math.log2(q) - depth, 9),
        "min_prefix_margin_bits": round(min_prefix_margin_bits or 0.0, 9),
        "low_repeat_gate_hits_x_mod_64_eq_59": low_repeat_hits,
        "low_repeat_sign_paired_hits_x_plus_5eps_eq_0_mod_64": low_repeat_sign_paired_hits,
        "high_ladder_hits_v2_x_plus_1_ge_3": high_ladder_hits,
        "high_ladder_sign_paired_hits_v2_x_plus_eps_ge_3": high_ladder_sign_paired_hits,
    }


def word_distribution(q: int, eps: int, depth: int) -> Counter[tuple[int, ...]]:
    return Counter(parity_word(q, eps, r, depth) for r in range(1 << depth))


def survivor_word_count(q: int, depth: int) -> int:
    """Count words whose every prefix satisfies q^o >= 2^j.

    This is deliberately word-only.  The count is therefore independent of eps
    and cannot distinguish Collatz from 3n-1.
    """

    total = 0
    for mask in range(1 << depth):
        odd_count = 0
        ok = True
        for j in range(1, depth + 1):
            if (mask >> (j - 1)) & 1:
                odd_count += 1
            if q**odd_count < (1 << j):
                ok = False
                break
        if ok:
            total += 1
    return total


def word_barrier_report(depth: int) -> dict[str, Any]:
    plus = word_distribution(3, 1, depth)
    minus = word_distribution(3, -1, depth)
    pointwise_diffs = sum(
        1
        for r in range(1 << depth)
        if parity_word(3, 1, r, depth) != parity_word(3, -1, r, depth)
    )
    odd_plus = Counter(sum(w) for w in plus)
    odd_minus = Counter(sum(w) for w in minus)
    survivor_count = survivor_word_count(3, depth)
    return {
        "depth": depth,
        "eps_plus_hits_each_word_once": set(plus.values()) == {1} and len(plus) == (1 << depth),
        "eps_minus_hits_each_word_once": set(minus.values()) == {1} and len(minus) == (1 << depth),
        "word_distribution_identical": plus == minus,
        "odd_count_distribution_identical": odd_plus == odd_minus,
        "pointwise_same_integer_word_differs": pointwise_diffs,
        "pointwise_same_integer_word_differs_fraction": pointwise_diffs / (1 << depth),
        "survivor_frontier_word_count": survivor_count,
        "survivor_frontier_fraction": survivor_count / (1 << depth),
        "lint": "Any argument using only this distribution is rejected as standalone Collatz-specific evidence.",
    }


def find_cycle(q: int, eps: int, start: int, max_steps: int = 10000) -> dict[str, Any]:
    x = start
    values = [x]
    word: list[int] = []
    for _ in range(max_steps):
        word.append(x & 1)
        x = step(q, eps, x)
        if x == start:
            break
        values.append(x)
    else:
        raise AssertionError(f"no return to {start} within {max_steps} steps for ({q},{eps})")

    d = len(word)
    o = sum(word)
    cmp = q**o - (1 << d)
    side = "above" if cmp > 0 else "below" if cmp < 0 else "on"
    sign_rule_side = "below" if eps > 0 else "above"
    return {
        "q": q,
        "eps": eps,
        "start": start,
        "length": d,
        "odd_steps": o,
        "word": "".join(str(b) for b in word),
        "elements": values,
        "q^o_minus_2^d": cmp,
        "side_of_critical_line": side,
        "positive_cycle_sign_rule_holds": side == sign_rule_side if start > 0 else None,
        "margin_bits": round(o * math.log2(q) - d, 9),
    }


def cycle_controls() -> dict[str, Any]:
    positive_cycles = [
        find_cycle(q, eps, m)
        for (q, eps), minima in KNOWN_CYCLE_MINIMA.items()
        for m in minima
    ]
    negative_conjugates = [find_cycle(3, 1, -5), find_cycle(3, 1, -17)]
    return {
        "positive_cycle_controls": positive_cycles,
        "negative_collatz_controls": negative_conjugates,
        "all_positive_cycle_sign_rules_hold": all(
            c["positive_cycle_sign_rule_holds"] for c in positive_cycles
        ),
        "lint": (
            "A proposed invariant must explain why it fails on 3n-1 positive cycles, "
            "5n+1 nontrivial cycles, and Collatz negative cycles."
        ),
    }


def stress_families() -> list[dict[str, Any]]:
    mersenne = [(1 << k) - 1 for k in (8, 12, 16, 20, 24)]
    high_ladders = [(1 << a) * q - 1 for a in (3, 4, 5, 8, 12) for q in (1, 3, 5)]
    low_repeats = [64 * m - 5 for m in (1, 3, 5, 17, 65, 257)]
    false_world_cycles = [5, 17, 13]
    return [
        {"family": "collatz_hard_record_smoke", "map": [3, 1], "starts": COLLATZ_STRESS_STARTS},
        {"family": "mersenne_shadows_2^k_minus_1", "map": [3, 1], "starts": mersenne},
        {"family": "high_ladder_states_2^a_q_minus_1", "map": [3, 1], "starts": high_ladders},
        {"family": "low_repeat_gate_x_eq_minus_5_mod_64", "map": [3, 1], "starts": low_repeats},
        {"family": "false_world_cycle_minima", "map": ["mixed"], "starts": false_world_cycles},
    ]


def stress_profile(trace_depth: int) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for n in COLLATZ_STRESS_STARTS + [(1 << k) - 1 for k in (8, 16, 24)] + [59, 187, 1019]:
        tr = affine_trace(3, 1, n, trace_depth)
        rows.append(
            {
                "start": n,
                "end_after_depth": tr["end"],
                "odd_steps": tr["odd_steps"],
                "multiplier_excess_bits": tr["multiplier_excess_bits"],
                "low_repeat_hits": tr["low_repeat_gate_hits_x_mod_64_eq_59"],
                "high_ladder_hits": tr["high_ladder_hits_v2_x_plus_1_ge_3"],
            }
        )
    return rows


def high_ladder_formula_controls(max_align: int) -> dict[str, Any]:
    """Check the sign-paired q=3 high-ladder identity.

    For eps=+1 this is the familiar x = 2^a m - 1 Mersenne shadow.
    For eps=-1 the mirror is x = 2^a m + 1.  A detector that only notices
    x+1 is therefore instrumentation for Collatz, not a sign-robust invariant.
    """

    failures: list[dict[str, Any]] = []
    samples: list[dict[str, Any]] = []
    multipliers = (1, 3, 5, 7, 11)
    for eps in (1, -1):
        for align in range(3, max_align + 1):
            for multiplier in multipliers:
                x = (1 << align) * multiplier - eps
                y = x
                ok = True
                for k in range(1, align + 1):
                    y = step(3, eps, y)
                    expected = (3**k) * (1 << (align - k)) * multiplier - eps
                    if y != expected:
                        ok = False
                        failures.append(
                            {
                                "eps": eps,
                                "align": align,
                                "multiplier": multiplier,
                                "step": k,
                                "got": y,
                                "expected": expected,
                            }
                        )
                        break
                if len(samples) < 16:
                    samples.append(
                        {
                            "eps": eps,
                            "align": align,
                            "multiplier": multiplier,
                            "start": x,
                            "terminal_after_alignment": y,
                            "formula_ok": ok,
                        }
                    )
    return {
        "max_align": max_align,
        "sample_count": 2 * max(0, max_align - 2) * len(multipliers),
        "all_formula_checks_pass": not failures,
        "failure_samples": failures[:12],
        "sample_records": samples,
        "lint": "High ladders are exact local structure, but the real family is x = 2^a*m - eps.",
    }


def low_repeat_formula_controls(max_align: int) -> dict[str, Any]:
    """Check the sign-paired OOE low-repeat gate.

    If x + 5 eps has at least six factors of two, then the OOE block gives

        T^3(x) = (9x + 5 eps) / 8
        v2(T^3(x) + 5 eps) = v2(x + 5 eps) - 3.
    """

    failures: list[dict[str, Any]] = []
    samples: list[dict[str, Any]] = []
    multipliers = (1, 3, 5, 7, 11)
    for eps in (1, -1):
        for align in range(6, max_align + 1):
            for multiplier in multipliers:
                x = (1 << align) * multiplier - 5 * eps
                y = x
                for _ in range(3):
                    y = step(3, eps, y)
                expected_y = (9 * x + 5 * eps) // 8
                expected_v2 = (v2(x + 5 * eps) or 0) - 3
                got_v2 = v2(y + 5 * eps)
                ok = y == expected_y and got_v2 == expected_v2
                if not ok:
                    failures.append(
                        {
                            "eps": eps,
                            "align": align,
                            "multiplier": multiplier,
                            "start": x,
                            "got": y,
                            "expected": expected_y,
                            "got_v2": got_v2,
                            "expected_v2": expected_v2,
                        }
                    )
                if len(samples) < 16:
                    samples.append(
                        {
                            "eps": eps,
                            "align": align,
                            "multiplier": multiplier,
                            "start": x,
                            "after_three_steps": y,
                            "v2_before": v2(x + 5 * eps),
                            "v2_after": got_v2,
                            "formula_ok": ok,
                        }
                    )
    return {
        "max_align": max_align,
        "sample_count": 2 * max(0, max_align - 5) * len(multipliers),
        "all_formula_checks_pass": not failures,
        "failure_samples": failures[:12],
        "sample_records": samples,
        "lint": "The low-repeat gate spends local 2-adic credit; it is not global descent by itself.",
    }


def scan_one(q: int, eps: int, n: int, cap: int) -> dict[str, Any]:
    """Bounded tau/sigma scan used only as a falsification smoke test."""

    x = n
    coeff = 1
    tau = None
    sigma = None
    seen: dict[int, int] = {}
    for d in range(1, cap + 1):
        if x & 1:
            coeff *= q
            x = (q * x + eps) // 2
        else:
            x //= 2
        if sigma is None and x < n:
            sigma = d
        if tau is None and coeff < (1 << d):
            tau = d
        if tau is not None and (sigma is not None or eps > 0):
            return {"n": n, "tau": tau, "sigma": sigma, "flagged": False, "reason": "finite_tau"}
        if x in seen:
            return {
                "n": n,
                "tau": tau,
                "sigma": sigma,
                "flagged": tau is None,
                "reason": "cycle_seen_before_tau" if tau is None else "cycle_after_tau",
                "cycle_entry_step": seen[x],
                "cycle_return_step": d,
            }
        seen[x] = d
    return {"n": n, "tau": tau, "sigma": sigma, "flagged": True, "reason": "cap"}


def bounded_scan_controls(max_start: int, cap: int) -> dict[str, Any]:
    summaries: list[dict[str, Any]] = []
    for world in WORLDS:
        q = int(world["q"])
        eps = int(world["eps"])
        flagged_count = 0
        flagged_samples: list[dict[str, Any]] = []
        tau_finite = 0
        sigma_finite = 0
        max_tau = {"n": None, "steps": 0}
        max_sigma = {"n": None, "steps": 0}
        for n in range(1, max_start + 1, 2):
            row = scan_one(q, eps, n, cap)
            if row["flagged"]:
                flagged_count += 1
                if len(flagged_samples) < 16:
                    flagged_samples.append(row)
            if row["tau"] is not None:
                tau_finite += 1
                if row["tau"] > max_tau["steps"]:
                    max_tau = {"n": n, "steps": row["tau"]}
            if row["sigma"] is not None:
                sigma_finite += 1
                if row["sigma"] > max_sigma["steps"]:
                    max_sigma = {"n": n, "steps": row["sigma"]}
        summaries.append(
            {
                "world": world,
                "odd_starts_scanned": (max_start + 1) // 2,
                "cap": cap,
                "tau_finite_count": tau_finite,
                "sigma_finite_count": sigma_finite,
                "flagged_count": flagged_count,
                "flagged_samples": flagged_samples,
                "max_tau": max_tau,
                "max_sigma": max_sigma,
            }
        )
    return {
        "max_start": max_start,
        "cap": cap,
        "summaries": summaries,
        "lint": "Bounded scans are not evidence of truth; they catch probes that certify false sibling worlds.",
    }


def retimed_tight_fixture_summary() -> dict[str, Any]:
    if not RETIME_TIGHT_FILE.exists():
        return {
            "available": False,
            "source": str(RETIME_TIGHT_FILE),
            "lint": "No retimed tight-layer fixture JSON found in this checkout.",
        }
    data = json.loads(RETIME_TIGHT_FILE.read_text(encoding="utf-8"))
    checks = data.get("checks", {})
    counts = data.get("counts", {})
    return {
        "available": True,
        "source": str(RETIME_TIGHT_FILE),
        "checks_subset": {
            "selected_count": checks.get("selected_count"),
            "all_selected_have_align_3": checks.get("all_selected_have_align_3"),
            "all_selected_have_required_delta_1": checks.get("all_selected_have_required_delta_1"),
            "all_selected_have_high_ladder_credit": checks.get("all_selected_have_high_ladder_credit"),
        },
        "counts_subset": {
            "regime_counts": counts.get("regime_counts"),
            "event_counts": counts.get("event_counts"),
            "terminal_mod_16_counts": counts.get("terminal_mod_16_counts"),
            "q_mod_16_counts": counts.get("q_mod_16_counts"),
        },
        "lint": "Retimed reserve cases are stress fixtures, not proof claims.",
    }


def lint_rules(depth: int) -> list[dict[str, Any]]:
    survivor_count = survivor_word_count(3, depth)
    return [
        {
            "probe": "parity_word_distribution",
            "status": "reject_as_standalone",
            "epsilon_sensitive": False,
            "proof_safety_rating_0_to_10": 1,
            "falsification_value_0_to_10": 9,
            "why": "The residue-to-word map is a bijection for eps=+1 and eps=-1; word histograms match.",
        },
        {
            "probe": "odd_density_or_multiplier_excess",
            "status": "reject_as_standalone",
            "epsilon_sensitive": False,
            "proof_safety_rating_0_to_10": 2,
            "falsification_value_0_to_10": 10,
            "why": "It is a function of the word only, so the 3n-1 false sibling inherits it unchanged.",
        },
        {
            "probe": "survivor_frontier_count",
            "status": "reject_as_standalone",
            "epsilon_sensitive": False,
            "depth": depth,
            "survivor_word_count": survivor_count,
            "proof_safety_rating_0_to_10": 2,
            "falsification_value_0_to_10": 10,
            "why": "The frontier count is word-only; it cannot separate Collatz from 3n-1.",
        },
        {
            "probe": "affine_intercept_sign",
            "status": "allowed_input",
            "epsilon_sensitive": True,
            "proof_safety_rating_0_to_10": 7,
            "falsification_value_0_to_10": 8,
            "why": "The inhomogeneous term c_d flips sign with eps and is where +1 actually enters.",
        },
        {
            "probe": "positive_cycle_side_of_critical_line",
            "status": "allowed_input",
            "epsilon_sensitive": True,
            "proof_safety_rating_0_to_10": 7,
            "falsification_value_0_to_10": 9,
            "why": "Positive cycles sit below the critical line for eps=+1 and above it for eps=-1.",
        },
        {
            "probe": "low_repeat_and_high_ladder_value_gates",
            "status": "stress_required",
            "epsilon_sensitive": "value_level_not_automatically_proof_relevant",
            "proof_safety_rating_0_to_10": 4,
            "falsification_value_0_to_10": 7,
            "why": "These local structures are useful only if tied to positivity, intercept, and infinite lift control.",
        },
    ]


def build_payload(depth: int, trace_depth: int, max_start: int, cap: int, max_align: int) -> dict[str, Any]:
    traces = [
        affine_trace(q, eps, n, min(trace_depth, 24))
        for q, eps, n in (
            (3, 1, 27),
            (3, -1, 5),
            (5, 1, 13),
            (3, 1, -5),
        )
    ]
    high_ladders = high_ladder_formula_controls(max_align)
    low_repeats = low_repeat_formula_controls(max_align)
    scans = bounded_scan_controls(max_start, cap)
    hard_failures = []
    if not high_ladders["all_formula_checks_pass"]:
        hard_failures.append("high ladder formula controls failed")
    if not low_repeats["all_formula_checks_pass"]:
        hard_failures.append("low repeat formula controls failed")
    if not cycle_controls()["all_positive_cycle_sign_rules_hold"]:
        hard_failures.append("positive cycle sign controls failed")
    return {
        "artifact": "collatz_epsilon_lint",
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "status": "lint_harness_not_proof",
        "pass": not hard_failures,
        "hard_failures": hard_failures,
        "parameters": {
            "distribution_depth": depth,
            "trace_depth": trace_depth,
            "max_start": max_start,
            "scan_cap": cap,
            "max_align": max_align,
        },
        "scope": (
            "Executable guardrail for proof sketches. It rejects epsilon-blind evidence "
            "and names the sibling/negative-cycle controls a future invariant must pass."
        ),
        "worlds": WORLDS,
        "word_barrier": word_barrier_report(depth),
        "affine_trace_witnesses": traces,
        "cycle_controls": cycle_controls(),
        "high_ladder_formula_controls": high_ladders,
        "low_repeat_formula_controls": low_repeats,
        "bounded_scan_controls": scans,
        "retimed_tight_fixture": retimed_tight_fixture_summary(),
        "stress_families": stress_families(),
        "collatz_stress_profile": stress_profile(trace_depth),
        "lint_rules": lint_rules(depth),
        "graduation_gate": [
            "Name where the +1 intercept is used.",
            "Show the claim fails on 3n-1 positive cycles for the right reason.",
            "Show the claim fails on 5n+1 nontrivial cycles or explain why the domain excludes them.",
            "Separate positive-integer evidence from negative-cycle and 2-adic ghost evidence.",
            "Provide a finite falsifier command and result path before theorem wording.",
        ],
        "does_not_claim": [
            "Collatz is solved.",
            "No divergent orbit exists.",
            "No nontrivial positive Collatz cycle exists.",
            "The listed stress probes are sufficient for a proof.",
        ],
    }


def run_selftest() -> dict[str, Any]:
    failures: list[str] = []

    if tuple(collatz_parity_word(27, 12)) != parity_word(3, 1, 27, 12):
        failures.append("lib_collatz parity word disagrees with generalized Collatz parity word")

    for q, eps, n in [(3, 1, 27), (3, -1, 5), (5, 1, 13), (3, 1, -5), (3, -1, 17)]:
        tr = affine_trace(q, eps, n, 32)
        if not tr["intercept_sign_matches_eps"]:
            failures.append(f"intercept sign mismatch for {(q, eps, n)}")

    wb = word_barrier_report(10)
    for key in (
        "eps_plus_hits_each_word_once",
        "eps_minus_hits_each_word_once",
        "word_distribution_identical",
        "odd_count_distribution_identical",
    ):
        if not wb[key]:
            failures.append(f"word barrier check failed: {key}")

    cc = cycle_controls()
    if not cc["all_positive_cycle_sign_rules_hold"]:
        failures.append("known positive cycle sign dichotomy failed")

    high = high_ladder_formula_controls(10)
    if not high["all_formula_checks_pass"]:
        failures.append("high ladder formula controls failed")

    low = low_repeat_formula_controls(10)
    if not low["all_formula_checks_pass"]:
        failures.append("low repeat formula controls failed")

    payload = build_payload(depth=8, trace_depth=12, max_start=101, cap=512, max_align=10)
    if not payload["pass"]:
        failures.extend(payload["hard_failures"])

    return {
        "selftest": "pass" if not failures else "fail",
        "failures": failures,
        "checks": {
            "lib_collatz_import": True,
            "affine_identity_and_intercept_sign": not any("intercept" in f for f in failures),
            "word_barrier_depth_10": all(wb[k] for k in (
                "eps_plus_hits_each_word_once",
                "eps_minus_hits_each_word_once",
                "word_distribution_identical",
                "odd_count_distribution_identical",
            )),
            "cycle_sign_dichotomy": cc["all_positive_cycle_sign_rules_hold"],
            "high_ladder_formula_controls": high["all_formula_checks_pass"],
            "low_repeat_formula_controls": low["all_formula_checks_pass"],
            "build_payload": payload["pass"],
        },
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)

    selftest_parser = sub.add_parser("selftest", help="run internal consistency checks")
    selftest_parser.add_argument("--json", action="store_true", help="print JSON instead of a compact status")

    run_parser = sub.add_parser("run", help="write or print the lint payload")
    run_parser.add_argument("--depth", "--distribution-depth", dest="depth", type=int, default=12, help="parity-word distribution depth")
    run_parser.add_argument("--trace-depth", "--orbit-depth", dest="trace_depth", type=int, default=40, help="stress trace depth")
    run_parser.add_argument("--max-start", type=int, default=2000, help="largest positive odd start for bounded sibling scans")
    run_parser.add_argument("--cap", type=int, default=4096, help="maximum shortcut steps per bounded scan")
    run_parser.add_argument("--max-align", type=int, default=18, help="largest 2-adic alignment checked in formula controls")
    run_parser.add_argument("--out", type=Path, default=DEFAULT_OUT, help="JSON output path")
    run_parser.add_argument("--no-write", action="store_true", help="print only; do not write --out")

    args = parser.parse_args(argv)

    if args.command == "selftest":
        result = run_selftest()
        if args.json:
            print(json.dumps(result, indent=2))
        else:
            print(result["selftest"])
            for failure in result["failures"]:
                print(f"FAIL: {failure}", file=sys.stderr)
        return 0 if result["selftest"] == "pass" else 1

    payload = build_payload(args.depth, args.trace_depth, args.max_start, args.cap, args.max_align)
    payload["argv"] = sys.argv
    if not args.no_write:
        out = args.out if args.out.is_absolute() else Path.cwd() / args.out
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
        payload["wrote"] = str(out)
    print(json.dumps(payload, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

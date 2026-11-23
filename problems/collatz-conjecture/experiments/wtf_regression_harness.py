#!/usr/bin/env python3
"""Fast regression harness for the repo's sharpest Collatz obstructions.

This is not a proof attempt.  It is a guardrail for proof attempts: before a
new idea is trusted, it should survive the exact weirdness that has already
broken simpler routes:

* the epsilon barrier for parity-word-only arguments;
* the all-odd 2-adic boundary point;
* the phase-collision normal form and its too-permissive phase gate;
* the retimed-pressure surplus-one base cases;
* the reserve-source identity behind the tight retimed local grammar.

The default run is intentionally small and fast.  Increase the depth arguments
when promoting a result from smoke test to research evidence.
"""

from __future__ import annotations

import argparse
import json
import math
import sys
from collections import Counter
from pathlib import Path
from time import perf_counter

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

from lib_collatz import classic_stats, parity_word, shortcut_stats, spine
from spine_phase_collision_lab import run as run_phase_collision
from branch_prefix_retimed_tight_layer_one import run as run_tight_layer_one
from branch_prefix_retimed_tight_reserve_source import run as run_reserve_source


def round_float(value: float, digits: int = 12) -> float:
    return round(float(value), digits)


def shortcut_eps(n: int, eps: int) -> int:
    if n & 1:
        return (3 * n + eps) // 2
    return n // 2


def parity_word_eps(n: int, depth: int, eps: int) -> tuple[int, ...]:
    word = []
    for _ in range(depth):
        word.append(n & 1)
        n = shortcut_eps(n, eps)
    return tuple(word)


def find_cycle(start: int, eps: int, cap: int = 100000) -> list[int] | None:
    seen: dict[int, int] = {}
    n = start
    for step in range(cap + 1):
        if n in seen:
            first = seen[n]
            ordered = sorted(seen.items(), key=lambda item: item[1])
            return [value for value, index in ordered if index >= first]
        seen[n] = step
        n = shortcut_eps(n, eps)
    return None


def assertion(name: str, ok: bool, details: dict[str, object] | None = None) -> dict[str, object]:
    return {"name": name, "ok": bool(ok), "details": details or {}}


def core_identity_checks(boundary_depth: int) -> tuple[list[dict[str, object]], dict[str, object]]:
    checks = []
    w_minus_five = parity_word(-5, 3)
    w_minus_seventeen = parity_word(-17, 11)
    all_odd_boundary = parity_word(-1, boundary_depth)
    checks.append(
        assertion(
            "classic orbit of 27 remains a fixed sanity anchor",
            classic_stats(27) == (111, 9232),
            {"computed": classic_stats(27), "expected": [111, 9232]},
        )
    )
    checks.append(
        assertion(
            "shortcut orbit of 27 remains a fixed sanity anchor",
            shortcut_stats(27) == (70, 41),
            {"computed": shortcut_stats(27), "expected": [70, 41]},
        )
    )
    checks.append(
        assertion(
            "all-odd 2-adic boundary survives every checked prefix",
            set(all_odd_boundary) == {1},
            {"depth": boundary_depth, "odd_prefix_count": sum(all_odd_boundary)},
        )
    )
    checks.append(
        assertion(
            "known negative spines remain exact fixed points",
            spine((1,)) == -1 and spine(w_minus_five) == -5 and spine(w_minus_seventeen) == -17,
            {
                "minus_one": str(spine((1,))),
                "minus_five": str(spine(w_minus_five)),
                "minus_seventeen": str(spine(w_minus_seventeen)),
            },
        )
    )
    summary = {
        "boundary_depth": boundary_depth,
        "minus_five_word": "".join(map(str, w_minus_five)),
        "minus_seventeen_word": "".join(map(str, w_minus_seventeen)),
    }
    return checks, summary


def epsilon_barrier_checks(depth: int, conjugacy_radius: int) -> tuple[list[dict[str, object]], dict[str, object]]:
    checks = []
    conjugacy_failures = 0
    for n in range(-conjugacy_radius, conjugacy_radius + 1):
        if n and -shortcut_eps(n, +1) != shortcut_eps(-n, -1):
            conjugacy_failures += 1

    plus_words = [parity_word_eps(n, depth, +1) for n in range(1 << depth)]
    minus_words = [parity_word_eps(n, depth, -1) for n in range(1 << depth)]
    plus_counter = Counter(plus_words)
    minus_counter = Counter(minus_words)
    pointwise_diff = sum(1 for plus, minus in zip(plus_words, minus_words) if plus != minus)
    plus_odd_counts = Counter(sum(word) for word in plus_words)
    minus_odd_counts = Counter(sum(word) for word in minus_words)
    cycle_5 = find_cycle(5, -1)
    cycle_17 = find_cycle(17, -1)

    checks.append(
        assertion(
            "epsilon conjugacy has no failures on checked interval",
            conjugacy_failures == 0,
            {"radius": conjugacy_radius, "failures": conjugacy_failures},
        )
    )
    checks.append(
        assertion(
            "both epsilon maps realize every parity word exactly once",
            set(plus_counter.values()) == {1}
            and set(minus_counter.values()) == {1}
            and len(plus_counter) == (1 << depth)
            and len(minus_counter) == (1 << depth),
            {"depth": depth, "plus_words": len(plus_counter), "minus_words": len(minus_counter)},
        )
    )
    checks.append(
        assertion(
            "odd-count distribution is epsilon-invariant",
            plus_odd_counts == minus_odd_counts,
            {"depth": depth},
        )
    )
    checks.append(
        assertion(
            "pointwise parity words mostly differ despite identical statistics",
            pointwise_diff > (1 << depth) * 0.9,
            {"depth": depth, "pointwise_diff_fraction": round_float(pointwise_diff / (1 << depth))},
        )
    )
    checks.append(
        assertion(
            "3n-1 sibling map still has positive cycles at 5 and 17",
            bool(cycle_5 and 5 in cycle_5 and cycle_17 and 17 in cycle_17),
            {"cycle_5": cycle_5, "cycle_17": cycle_17},
        )
    )
    summary = {
        "depth": depth,
        "conjugacy_radius": conjugacy_radius,
        "pointwise_diff_fraction": round_float(pointwise_diff / (1 << depth)),
        "cycle_5": cycle_5,
        "cycle_17": cycle_17,
    }
    return checks, summary


def phase_collision_checks(args: argparse.Namespace) -> tuple[list[dict[str, object]], dict[str, object]]:
    payload = run_phase_collision(
        argparse.Namespace(
            max_depth=args.phase_max_depth,
            identity_trials=args.phase_identity_trials,
            seed=args.seed,
            max_excess=args.phase_max_excess,
            barrier_depths=args.phase_barrier_depths,
            density_max_depth=args.phase_density_max_depth,
            density_depths=args.phase_density_depths,
        )
    )
    phase_identity = dict(payload["phase_identity"])
    gate = dict(payload["phase_gate_unique_target_spines"])
    checks = [
        assertion(
            "phase-collision identity has zero failures",
            int(phase_identity["failure_count"]) == 0,
            {
                "identity_checks": phase_identity["identity_checks"],
                "nonmatched_checks": phase_identity["valuation_formula_checks_nonmatched"],
            },
        ),
        assertion(
            "finite phase gate remains too permissive to be a proof",
            float(gate["avg_allowed_fraction_of_m_mod_source_length"]) > args.min_phase_gate_fraction,
            {
                "avg_allowed_fraction": gate["avg_allowed_fraction_of_m_mod_source_length"],
                "minimum_required": args.min_phase_gate_fraction,
            },
        ),
    ]
    summary = {
        "library": payload["library"],
        "phase_identity": {
            "identity_checks": phase_identity["identity_checks"],
            "valuation_formula_checks_nonmatched": phase_identity["valuation_formula_checks_nonmatched"],
            "matched_phase_cases": phase_identity["matched_phase_cases"],
            "failure_count": phase_identity["failure_count"],
        },
        "phase_gate_unique_target_spines": {
            "avg_allowed_fraction": gate["avg_allowed_fraction_of_m_mod_source_length"],
            "min_allowed_fraction": gate["min_allowed_fraction"],
            "max_allowed_fraction": gate["max_allowed_fraction"],
            "valuation_count": gate["source_phase_target_valuation_count"],
        },
        "density_firewall_counts": payload["density_firewall_counts"],
    }
    return checks, summary


def retimed_layer_checks(args: argparse.Namespace) -> tuple[list[dict[str, object]], dict[str, object]]:
    payload = run_tight_layer_one(
        argparse.Namespace(
            min_parent_depth=args.retimed_min_parent_depth,
            max_parent_depth=args.retimed_max_parent_depth,
            max_depth=args.retimed_max_depth,
            max_steps=args.retimed_max_steps,
            surplus=1,
            layer=1,
        )
    )
    checks_payload = dict(payload["checks"])
    all_named_checks = {
        key: value for key, value in checks_payload.items() if key.startswith("all_")
    }
    checks = [
        assertion(
            "retimed tight layer-one slice has selected surplus-one records",
            int(checks_payload["selected_count"]) > 0,
            {"selected_count": checks_payload["selected_count"]},
        ),
        assertion(
            "all retimed tight layer-one structural checks pass",
            all(bool(value) for value in all_named_checks.values()),
            all_named_checks,
        ),
    ]
    summary = {
        "parameters": payload["parameters"],
        "depths": payload["depths"],
        "checks": checks_payload,
        "counts": {
            "regime_counts": payload["counts"]["regime_counts"],
            "post_word_counts": payload["counts"]["post_word_counts"],
            "last_credit_align_counts": payload["counts"]["last_credit_align_counts"],
        },
    }
    return checks, summary


def reserve_source_checks(args: argparse.Namespace) -> tuple[list[dict[str, object]], dict[str, object]]:
    payload = run_reserve_source(
        argparse.Namespace(
            min_parent_depth=args.retimed_min_parent_depth,
            max_parent_depth=args.retimed_max_parent_depth,
            max_depth=args.retimed_max_depth,
            max_steps=args.retimed_max_steps,
            top_n=args.reserve_top_n,
        )
    )
    checks_payload = dict(payload["checks"])
    all_depth_checks = dict(checks_payload["all_depth_checks"])
    checks = [
        assertion(
            "reserve-source local grammar slice is nonempty",
            int(checks_payload["total_local_grammar_records"]) > 0,
            {"total_local_grammar_records": checks_payload["total_local_grammar_records"]},
        ),
        assertion(
            "reserve-source identities and prior-credit checks pass",
            all(bool(value) for value in all_depth_checks.values()),
            all_depth_checks,
        ),
    ]
    summary = {
        "parameters": payload["parameters"],
        "checks": checks_payload,
        "counters": {
            "inherited_reserve": payload["counters"]["inherited_reserve"],
            "previous_credit_kind": payload["counters"]["previous_credit_kind"],
            "word_by_reserve": payload["counters"]["word_by_reserve"],
        },
        "minimal_examples": payload["minimal_examples"],
    }
    return checks, summary


def run(args: argparse.Namespace) -> dict[str, object]:
    started = perf_counter()
    checks: list[dict[str, object]] = []
    modules: dict[str, object] = {}

    block_checks, modules["core_identities"] = core_identity_checks(args.boundary_depth)
    checks.extend(block_checks)

    block_checks, modules["epsilon_barrier"] = epsilon_barrier_checks(
        args.epsilon_depth, args.epsilon_conjugacy_radius
    )
    checks.extend(block_checks)

    block_checks, modules["phase_collision"] = phase_collision_checks(args)
    checks.extend(block_checks)

    block_checks, modules["retimed_tight_layer_one"] = retimed_layer_checks(args)
    checks.extend(block_checks)

    block_checks, modules["retimed_reserve_source"] = reserve_source_checks(args)
    checks.extend(block_checks)

    failed = [check for check in checks if not check["ok"]]
    return {
        "status": "wtf-regression-harness",
        "elapsed_seconds": round_float(perf_counter() - started, 6),
        "parameters": {
            "boundary_depth": args.boundary_depth,
            "epsilon_depth": args.epsilon_depth,
            "epsilon_conjugacy_radius": args.epsilon_conjugacy_radius,
            "phase_max_depth": args.phase_max_depth,
            "phase_identity_trials": args.phase_identity_trials,
            "phase_density_max_depth": args.phase_density_max_depth,
            "retimed_min_parent_depth": args.retimed_min_parent_depth,
            "retimed_max_parent_depth": args.retimed_max_parent_depth,
            "retimed_max_depth": args.retimed_max_depth,
            "retimed_max_steps": args.retimed_max_steps,
            "seed": args.seed,
        },
        "result": {
            "passed": not failed,
            "passed_count": len(checks) - len(failed),
            "failed_count": len(failed),
        },
        "checks": checks,
        "modules": modules,
        "interpretation": (
            "Passing this harness means the current weirdness stack is stable "
            "under a fast smoke run. It does not prove Collatz. It protects "
            "future Collatz ideas from ignoring the known obstructions."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--boundary-depth", type=int, default=64)
    parser.add_argument("--epsilon-depth", type=int, default=10)
    parser.add_argument("--epsilon-conjugacy-radius", type=int, default=2048)
    parser.add_argument("--phase-max-depth", type=int, default=8)
    parser.add_argument("--phase-identity-trials", type=int, default=512)
    parser.add_argument("--phase-max-excess", type=int, default=6)
    parser.add_argument("--phase-barrier-depths", default="32,64,128")
    parser.add_argument("--phase-density-max-depth", type=int, default=256)
    parser.add_argument("--phase-density-depths", default="16,64,128,256")
    parser.add_argument("--min-phase-gate-fraction", type=float, default=0.5)
    parser.add_argument("--retimed-min-parent-depth", type=int, default=18)
    parser.add_argument("--retimed-max-parent-depth", type=int, default=18)
    parser.add_argument("--retimed-max-depth", type=int, default=256)
    parser.add_argument("--retimed-max-steps", type=int, default=10000)
    parser.add_argument("--reserve-top-n", type=int, default=6)
    parser.add_argument("--seed", type=int, default=20260705)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--quiet", action="store_true")
    args = parser.parse_args()

    if args.boundary_depth < 1:
        raise SystemExit("--boundary-depth must be positive")
    if args.epsilon_depth < 1:
        raise SystemExit("--epsilon-depth must be positive")
    if args.phase_max_depth < 1:
        raise SystemExit("--phase-max-depth must be positive")
    if args.phase_identity_trials < 1:
        raise SystemExit("--phase-identity-trials must be positive")
    if args.retimed_min_parent_depth < 1:
        raise SystemExit("--retimed-min-parent-depth must be positive")
    if args.retimed_max_parent_depth < args.retimed_min_parent_depth:
        raise SystemExit("--retimed-max-parent-depth must be >= --retimed-min-parent-depth")
    if args.retimed_max_steps < 1:
        raise SystemExit("--retimed-max-steps must be positive")

    payload = run(args)
    text = json.dumps(payload, indent=2, sort_keys=True)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text + "\n", encoding="utf-8")
    if not args.quiet:
        print(text)
    return 0 if bool(payload["result"]["passed"]) else 1


if __name__ == "__main__":
    raise SystemExit(main())

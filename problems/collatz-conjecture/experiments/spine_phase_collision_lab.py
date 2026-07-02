#!/usr/bin/env python3
"""Exact phase-to-spine collision lab.

This lab ingests the useful part of the shared ChatGPT research notes without
turning any chat output into evidence.  It verifies the exact phase collision
identity behind post-expulsion regeneration:

    T^t(x) - eta = 3^a(t) * 2^(m-t) * u + (rho_t - eta),

where x - rho_0 = 2^m u, rho_t = T^t(rho_0), and eta is a target spine.

The lab also measures the finite phase gate

    m - t = v2(rho_t - eta),

which is necessary for high cancellation.  The measurement is a negative
result: phase matching alone leaves many source-alignment residues alive, so
any proof has to use the deeper odd-unit lock, positivity, or a new invariant.

Pure stdlib.  The conjecture remains open.
"""

from __future__ import annotations

import argparse
import json
import math
import random
import sys
from collections import Counter
from fractions import Fraction
from itertools import product
from pathlib import Path
from time import perf_counter

sys.path.insert(0, str(Path(__file__).resolve().parent))

from lib_collatz import cylinder_residue, is_supercritical, spine


def round_float(value: float, digits: int = 12) -> float:
    return round(float(value), digits)


def shortcut_step_frac(x: Fraction) -> Fraction:
    """Shortcut map on rationals with odd denominator, using 2-adic parity."""
    parity = (x.numerator * pow(x.denominator, -1, 2)) & 1
    if parity:
        return (3 * x + 1) / 2
    return x / 2


def v2_fraction(x: Fraction, cap: int = 100000) -> int:
    """2-adic valuation of a rational with odd denominator."""
    if x == 0:
        return cap
    n = abs(x.numerator)
    count = 0
    while n % 2 == 0:
        n //= 2
        count += 1
    return count


def canonical_word(w: tuple[int, ...]) -> tuple[int, ...]:
    return min(w[i:] + w[:i] for i in range(len(w)))


def primitive_period(w: tuple[int, ...]) -> int:
    d = len(w)
    for p in range(1, d + 1):
        if d % p == 0 and all(w[i] == w[i % p] for i in range(d)):
            return p
    raise AssertionError("period search failed")


def rotate_word(w: tuple[int, ...], offset: int) -> tuple[int, ...]:
    offset %= len(w)
    return w[offset:] + w[:offset]


def word_string(w: tuple[int, ...]) -> str:
    return "".join(str(bit) for bit in w)


def enumerate_supercritical_cycles(max_depth: int) -> list[tuple[int, ...]]:
    cycles: dict[tuple[int, ...], tuple[int, ...]] = {}
    for d in range(1, max_depth + 1):
        for w in product((0, 1), repeat=d):
            if is_supercritical(w):
                c = canonical_word(w)
                cycles.setdefault(c, c)
    return sorted(cycles, key=lambda w: (len(w), w))


def phase_data(w: tuple[int, ...]) -> list[dict[str, object]]:
    """rho_t and odd prefix counts for the primitive source cycle w."""
    rho = spine(w)
    phases: list[dict[str, object]] = []
    current = rho
    odd_count = 0
    phases.append({"t": 0, "rho": current, "odd_prefix": 0})
    for t, bit in enumerate(w, start=1):
        if bit:
            odd_count += 1
        current = shortcut_step_frac(current)
        phases.append({"t": t, "rho": current, "odd_prefix": odd_count})
    assert current == rho
    return phases


def verify_phase_identity(
    source_cycles: list[tuple[int, ...]],
    target_spines: list[Fraction],
    trials: int,
    seed: int,
) -> dict[str, object]:
    rng = random.Random(seed)
    failures: list[dict[str, object]] = []
    valuation_formula_checks = 0
    matched_cases = 0
    checked = 0

    for _ in range(trials):
        w = rng.choice(source_cycles)
        d = len(w)
        phases = phase_data(w)
        t = rng.randrange(0, d + 1)
        phase = phases[t]
        eta = rng.choice(target_spines)
        m = t + rng.randrange(0, max(4, d + 4))
        u = rng.randrange(-99, 100) | 1
        rho0 = phases[0]["rho"]
        rho_t = phase["rho"]
        odd_prefix = int(phase["odd_prefix"])
        x = rho0 + Fraction((1 << m) * u)

        current = x
        for _step in range(t):
            current = shortcut_step_frac(current)
        lhs = current - eta
        rhs = Fraction((3**odd_prefix) * (1 << (m - t)) * u) + (rho_t - eta)
        checked += 1
        if lhs != rhs:
            failures.append(
                {
                    "word": word_string(w),
                    "t": t,
                    "m": m,
                    "u": u,
                    "lhs": str(lhs),
                    "rhs": str(rhs),
                }
            )
            continue

        e = v2_fraction(rho_t - eta)
        a = m - t
        actual = v2_fraction(lhs)
        if a == e:
            matched_cases += 1
        else:
            valuation_formula_checks += 1
            expected = min(a, e)
            if actual != expected:
                failures.append(
                    {
                        "word": word_string(w),
                        "t": t,
                        "m": m,
                        "u": u,
                        "a": a,
                        "e": e,
                        "actual_v2": actual,
                        "expected_v2": expected,
                    }
                )

    return {
        "trials": trials,
        "identity_checks": checked,
        "valuation_formula_checks_nonmatched": valuation_formula_checks,
        "matched_phase_cases": matched_cases,
        "failure_count": len(failures),
        "failures": failures[:10],
    }


def phase_gate_stats(
    source_cycles: list[tuple[int, ...]],
    target_items: list[tuple[str, Fraction]],
) -> dict[str, object]:
    valuation_hist: Counter[int] = Counter()
    allowed_fraction_by_source_target: list[float] = []
    allowed_count_hist: Counter[int] = Counter()
    zero_separation_skips = 0
    phase_target_valuation_count = 0
    examples: list[dict[str, object]] = []

    for source in source_cycles:
        d = len(source)
        phases = phase_data(source)[:-1]
        for target_label, eta in target_items:
            allowed: set[int] = set()
            local_hist: Counter[int] = Counter()
            for phase in phases:
                t = int(phase["t"])
                rho_t = phase["rho"]
                if rho_t == eta:
                    zero_separation_skips += 1
                    continue
                e = v2_fraction(rho_t - eta)
                local_hist[e] += 1
                valuation_hist[e] += 1
                phase_target_valuation_count += 1
                allowed.add((t + e) % d)
            if allowed:
                allowed_fraction = len(allowed) / d
                allowed_fraction_by_source_target.append(allowed_fraction)
                allowed_count_hist[len(allowed)] += 1
                if len(examples) < 8:
                    examples.append(
                        {
                            "source": word_string(source),
                            "target": target_label,
                            "source_length": d,
                            "allowed_residues_mod_source_length": sorted(allowed),
                            "allowed_fraction": round_float(allowed_fraction),
                            "valuation_histogram": dict(sorted(local_hist.items())),
                        }
                    )

    avg = (
        sum(allowed_fraction_by_source_target) / len(allowed_fraction_by_source_target)
        if allowed_fraction_by_source_target
        else 0.0
    )
    return {
        "source_target_pairs_with_any_allowed_residue": len(allowed_fraction_by_source_target),
        "source_phase_target_valuation_count": phase_target_valuation_count,
        "zero_separation_skips": zero_separation_skips,
        "avg_allowed_fraction_of_m_mod_source_length": round_float(avg),
        "min_allowed_fraction": round_float(min(allowed_fraction_by_source_target, default=0.0)),
        "max_allowed_fraction": round_float(max(allowed_fraction_by_source_target, default=0.0)),
        "allowed_count_histogram": dict(sorted((str(k), v) for k, v in allowed_count_hist.items())),
        "valuation_histogram": dict(sorted((str(k), v) for k, v in valuation_hist.items())),
        "examples": examples,
    }


def mersenne_minus_one_to_minus_five(max_excess: int) -> dict[str, object]:
    rows = []
    for excess in range(3, max_excess + 1):
        modulus = 1 << excess
        order = 1 << max(0, excess - 2)
        hits = [k for k in range(order) if pow(3, k, modulus) == modulus - 1]
        rows.append(
            {
                "excess": excess,
                "modulus": modulus,
                "order_of_3_mod_2^excess": order,
                "solutions_k_mod_order": hits,
            }
        )
    return {
        "source_spine": "-1",
        "target_spine": "-5",
        "condition": "3^k == -1 mod 2^excess for pure Mersenne unit u=1",
        "all_empty": all(not row["solutions_k_mod_order"] for row in rows),
        "rows": rows,
    }


def barrier_word(length: int) -> tuple[int, ...]:
    """b_j = a_j - a_{j-1}, a_j = min c with 3^c >= 2^j."""
    bits: list[int] = []
    a_prev = 0
    a = 0
    pow3 = 1
    for j in range(1, length + 1):
        while pow3 < (1 << j):
            pow3 *= 3
            a += 1
        bits.append(a - a_prev)
        a_prev = a
    return tuple(bits)


def critical_inverse_residues(depths: list[int]) -> list[dict[str, object]]:
    rows = []
    for depth in depths:
        w = barrier_word(depth)
        residue = cylinder_residue(w)
        distance = min(residue, (1 << depth) - residue)
        rows.append(
            {
                "depth": depth,
                "prefix64": word_string(w[: min(64, depth)]),
                "residue_bit_length": residue.bit_length(),
                "nearest_integer_distance_bit_length": distance.bit_length(),
                "nearest_integer_distance_over_2^depth_log2": round_float(
                    math.log2(distance) - depth if distance else float("-inf")
                ),
            }
        )
    return rows


def barrier_counts_upto(max_depth: int) -> list[int]:
    """Exact count of words that never drop below the multiplier barrier."""
    counts = [1]
    min_ones = 0
    survivor_counts = [0] * (max_depth + 1)
    survivor_counts[0] = 1
    threshold = 0
    pow3 = 1

    for j in range(1, max_depth + 1):
        new_counts = [0] * (len(counts) + 1)
        for i, count in enumerate(counts):
            new_counts[i] += count
            new_counts[i + 1] += count
        counts = new_counts
        while pow3 < (1 << j):
            pow3 *= 3
            threshold += 1
        drop = threshold - min_ones
        if drop > 0:
            counts = counts[drop:]
            min_ones = threshold
        survivor_counts[j] = sum(counts)
    return survivor_counts


def density_firewall(max_depth: int, selected_depths: list[int]) -> list[dict[str, object]]:
    counts = barrier_counts_upto(max_depth)
    rows = []
    for depth in selected_depths:
        if depth > max_depth:
            continue
        count = counts[depth]
        log_count = math.log2(count)
        rows.append(
            {
                "depth": depth,
                "a_depth": sum(barrier_word(depth)),
                "log2_barrier_word_count": round_float(log_count),
                "log2_density": round_float(log_count - depth),
            }
        )
    return rows


def run(args: argparse.Namespace) -> dict[str, object]:
    started = perf_counter()
    cycles = enumerate_supercritical_cycles(args.max_depth)
    primitive_cycles = [w for w in cycles if primitive_period(w) == len(w)]
    target_all_cycles = [(word_string(w), spine(w)) for w in cycles]
    unique_target_spines = sorted(
        {(spine(w), word_string(w[: primitive_period(w)])) for w in cycles},
        key=lambda item: (item[0].denominator, item[0].numerator, item[1]),
    )
    target_unique = [(label, rho) for rho, label in unique_target_spines]

    identity = verify_phase_identity(
        primitive_cycles,
        [rho for _label, rho in target_unique],
        args.identity_trials,
        args.seed,
    )
    unique_gate = phase_gate_stats(primitive_cycles, target_unique)
    all_cycle_gate = phase_gate_stats(primitive_cycles, target_all_cycles)
    barrier_depths = [int(part) for part in args.barrier_depths.split(",") if part.strip()]
    density_depths = [int(part) for part in args.density_depths.split(",") if part.strip()]

    return {
        "status": "spine-phase-collision-lab",
        "elapsed_seconds": round_float(perf_counter() - started, 6),
        "parameters": {
            "max_depth": args.max_depth,
            "identity_trials": args.identity_trials,
            "seed": args.seed,
            "max_excess": args.max_excess,
            "barrier_depths": barrier_depths,
            "density_max_depth": args.density_max_depth,
            "density_depths": density_depths,
        },
        "library": {
            "supercritical_necklace_cycles": len(cycles),
            "primitive_source_cycles": len(primitive_cycles),
            "primitive_source_phase_states": sum(len(w) for w in primitive_cycles),
            "all_cycle_phase_slots": sum(len(w) for w in cycles),
            "unique_target_spines": len(target_unique),
            "target_cycles_including_nonprimitive_duplicates": len(target_all_cycles),
            "note": (
                "Nonprimitive necklaces duplicate primitive spines. The unique-spine "
                "gate is the math-clean denominator; the all-cycle gate is retained "
                "for comparison with shared-chat aggregate conventions."
            ),
        },
        "phase_identity": identity,
        "phase_gate_unique_target_spines": unique_gate,
        "phase_gate_all_target_cycles": all_cycle_gate,
        "minus_one_to_minus_five_mersenne_lock": mersenne_minus_one_to_minus_five(args.max_excess),
        "critical_boundary_inverse_residues": critical_inverse_residues(barrier_depths),
        "density_firewall_counts": density_firewall(args.density_max_depth, density_depths),
        "interpretation": (
            "The normal form is exact and the nonmatched valuation rule is verified. "
            "The finite phase gate is too permissive by itself; a proof would need "
            "the odd-unit lock, entropy/codimension domination, positivity, or a "
            "new invariant. No part of Collatz is proved."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-depth", type=int, default=12)
    parser.add_argument("--identity-trials", type=int, default=5000)
    parser.add_argument("--seed", type=int, default=20260702)
    parser.add_argument("--max-excess", type=int, default=8)
    parser.add_argument("--barrier-depths", default="64,128,256,512")
    parser.add_argument("--density-max-depth", type=int, default=4096)
    parser.add_argument("--density-depths", default="16,64,128,512,1024,2048,4096")
    parser.add_argument("--output", type=Path)
    parser.add_argument("--quiet", action="store_true")
    args = parser.parse_args()

    if args.max_depth < 1:
        raise SystemExit("--max-depth must be positive")
    if args.identity_trials < 1:
        raise SystemExit("--identity-trials must be positive")
    if args.max_excess < 3:
        raise SystemExit("--max-excess must be at least 3")
    if args.density_max_depth < 1:
        raise SystemExit("--density-max-depth must be positive")

    payload = run(args)
    text = json.dumps(payload, indent=2, sort_keys=True)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text + "\n", encoding="utf-8")
    if not args.quiet:
        print(text)


if __name__ == "__main__":
    main()

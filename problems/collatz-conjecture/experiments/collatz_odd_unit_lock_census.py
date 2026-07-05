#!/usr/bin/env python3
"""Census the odd-unit locks behind phase-collision regeneration.

The phase-collision normal form says that, after a source spine phase rho_t and
a target spine eta have matched valuation e, extra alignment requires

    3^a u == -2^-e (rho_t - eta)  (mod 2^R).

For arbitrary 2-adic odd units this is always one residue class modulo 2^R;
the useful question is how those residue classes distribute and collide across
source phases, targets, and positive finite shadows.

This is finite theorem-discovery data, not a proof of Collatz.
"""

from __future__ import annotations

import argparse
import json
import random
import sys
from collections import Counter, defaultdict
from fractions import Fraction
from pathlib import Path
from time import perf_counter

sys.path.insert(0, str(Path(__file__).resolve().parent))

from lib_collatz import cylinder_residue, spine
from spine_phase_collision_lab import (
    enumerate_supercritical_cycles,
    phase_data,
    primitive_period,
    round_float,
    shortcut_step_frac,
    v2_fraction,
    word_string,
)


def parse_int_list(text: str) -> list[int]:
    values = [int(part) for part in text.split(",") if part.strip()]
    if not values:
        raise argparse.ArgumentTypeError("expected at least one integer")
    return values


def as_counter_dict(counter: Counter[int | str], *, limit: int | None = None) -> dict[str, int]:
    items = sorted(counter.items(), key=lambda item: (-int(item[1]), str(item[0])))
    if limit is not None:
        items = items[:limit]
    return {str(key): int(value) for key, value in items}


def unit_mod_power2(x: Fraction, bits: int) -> int:
    """Return x modulo 2^bits for a rational with odd denominator."""
    if bits < 1:
        raise ValueError("bits must be positive")
    modulus = 1 << bits
    denominator = x.denominator % modulus
    if denominator % 2 == 0:
        raise ValueError(f"denominator is not a 2-adic unit: {x}")
    return (x.numerator * pow(denominator, -1, modulus)) % modulus


def odd_part_after_valuation(x: Fraction, valuation: int, bits: int) -> int:
    if valuation < 0:
        raise ValueError("expected nonnegative valuation")
    return unit_mod_power2(x / (1 << valuation), bits)


def required_unit_residue(*, odd_prefix: int, delta: Fraction, valuation: int, bits: int) -> int:
    """Residue of u modulo 2^bits required for bits of extra alignment."""
    modulus = 1 << bits
    odd_delta = odd_part_after_valuation(delta, valuation, bits)
    multiplier = pow(3, odd_prefix, modulus)
    return (-odd_delta * pow(multiplier, -1, modulus)) % modulus


def odd_residue_count(bits: int) -> int:
    return 1 << max(0, bits - 1)


def target_unique_spines(cycles: list[tuple[int, ...]]) -> list[tuple[str, Fraction]]:
    unique = sorted(
        {(spine(w), word_string(w[: primitive_period(w)])) for w in cycles},
        key=lambda item: (item[0].denominator, item[0].numerator, item[1]),
    )
    return [(label, rho) for rho, label in unique]


def build_lock_records(
    sources: list[tuple[int, ...]],
    targets: list[tuple[str, Fraction]],
    lock_bits: list[int],
    *,
    example_limit: int,
) -> dict[str, object]:
    max_bits = max(lock_bits)
    valuation_hist: Counter[int] = Counter()
    phase_residue_hist: Counter[int] = Counter()
    source_length_hist: Counter[int] = Counter()
    group_residues: dict[int, dict[tuple[str, int], Counter[int]]] = {
        bits: defaultdict(Counter) for bits in lock_bits
    }
    global_residues: dict[int, Counter[int]] = {bits: Counter() for bits in lock_bits}
    examples: list[dict[str, object]] = []
    skipped_zero_delta = 0
    total_locks = 0

    for source in sources:
        source_label = word_string(source)
        source_length = len(source)
        source_length_hist[source_length] += 1
        for phase in phase_data(source)[:-1]:
            t = int(phase["t"])
            rho_t = phase["rho"]
            odd_prefix = int(phase["odd_prefix"])
            for target_label, eta in targets:
                if rho_t == eta:
                    skipped_zero_delta += 1
                    continue
                delta = rho_t - eta
                valuation = v2_fraction(delta)
                phase_residue = (t + valuation) % source_length
                phase_residue_hist[phase_residue] += 1
                valuation_hist[valuation] += 1
                total_locks += 1

                residues_by_bits = {}
                for bits in lock_bits:
                    residue = required_unit_residue(
                        odd_prefix=odd_prefix,
                        delta=delta,
                        valuation=valuation,
                        bits=bits,
                    )
                    residues_by_bits[str(bits)] = residue
                    group_residues[bits][(source_label, phase_residue)][residue] += 1
                    global_residues[bits][residue] += 1

                if len(examples) < example_limit:
                    examples.append(
                        {
                            "source": source_label,
                            "source_length": source_length,
                            "phase_t": t,
                            "odd_prefix": odd_prefix,
                            "target": target_label,
                            "valuation_e": valuation,
                            "phase_match_m_mod_source_length": phase_residue,
                            "required_unit_residue_mod_2^R": residues_by_bits,
                        }
                    )

    by_bits = {}
    for bits in lock_bits:
        groups = group_residues[bits]
        weighted_pairs = 0
        weighted_compatible = 0
        distinct_counts = []
        max_bucket = 0
        singleton_groups = 0

        for counter in groups.values():
            total = sum(counter.values())
            if total < 2:
                continue
            distinct_counts.append(len(counter))
            if len(counter) == 1:
                singleton_groups += 1
            max_bucket = max(max_bucket, max(counter.values()))
            pairs = total * (total - 1) // 2
            compatible = sum(value * (value - 1) // 2 for value in counter.values())
            weighted_pairs += pairs
            weighted_compatible += compatible

        incompatible_fraction = (
            1.0 - (weighted_compatible / weighted_pairs) if weighted_pairs else 0.0
        )
        global_counter = global_residues[bits]
        by_bits[str(bits)] = {
            "odd_unit_residue_space_size": odd_residue_count(bits),
            "codimension_bits_beyond_oddness_per_lock": max(0, bits - 1),
            "global_distinct_required_residues": len(global_counter),
            "global_residue_coverage_fraction": round_float(
                len(global_counter) / odd_residue_count(bits)
            ),
            "top_global_required_residues": as_counter_dict(global_counter, limit=12),
            "phase_groups": len(groups),
            "phase_groups_with_pair_data": len(distinct_counts),
            "singleton_residue_phase_groups": singleton_groups,
            "max_distinct_required_residues_in_phase_group": max(distinct_counts, default=0),
            "avg_distinct_required_residues_in_phase_group": round_float(
                sum(distinct_counts) / len(distinct_counts) if distinct_counts else 0.0
            ),
            "weighted_incompatible_pair_fraction_inside_phase_groups": round_float(
                incompatible_fraction
            ),
            "max_same_residue_bucket_inside_phase_group": max_bucket,
        }

    return {
        "total_locks": total_locks,
        "skipped_zero_delta": skipped_zero_delta,
        "valuation_histogram": as_counter_dict(valuation_hist),
        "phase_residue_histogram": as_counter_dict(phase_residue_hist, limit=20),
        "source_length_histogram": as_counter_dict(source_length_hist),
        "by_lock_bits": by_bits,
        "examples": examples,
        "note": (
            "Every listed lock has exactly one odd-unit residue modulo 2^R. "
            "The census measures how those residues distribute and how often "
            "two target locks in the same source phase demand incompatible units."
        ),
    }


def verify_lock_formula(
    sources: list[tuple[int, ...]],
    targets: list[tuple[str, Fraction]],
    *,
    bits: int,
    trials: int,
    seed: int,
) -> dict[str, object]:
    rng = random.Random(seed)
    failures: list[dict[str, object]] = []
    checked = 0

    for _ in range(trials):
        source = rng.choice(sources)
        phases = phase_data(source)[:-1]
        phase = rng.choice(phases)
        rho0 = phases[0]["rho"]
        rho_t = phase["rho"]
        t = int(phase["t"])
        odd_prefix = int(phase["odd_prefix"])
        target_label, eta = rng.choice(targets)
        if rho_t == eta:
            continue
        delta = rho_t - eta
        valuation = v2_fraction(delta)
        m = t + valuation
        residue = required_unit_residue(
            odd_prefix=odd_prefix,
            delta=delta,
            valuation=valuation,
            bits=bits,
        )

        # Check one satisfying and one nearby nonsatisfying unit.
        for u_mod in (residue, residue ^ 2 if bits > 1 else residue):
            if u_mod % 2 == 0:
                u_mod ^= 1
            u = Fraction(u_mod)
            x = rho0 + Fraction((1 << m) * u)
            current = x
            for _step in range(t):
                current = shortcut_step_frac(current)
            actual_extra = v2_fraction(current - eta) - valuation
            should_satisfy = (u_mod - residue) % (1 << bits) == 0
            did_satisfy = actual_extra >= bits
            checked += 1
            if should_satisfy != did_satisfy:
                failures.append(
                    {
                        "source": word_string(source),
                        "target": target_label,
                        "t": t,
                        "valuation": valuation,
                        "bits": bits,
                        "u_mod": u_mod,
                        "required": residue,
                        "actual_extra": actual_extra,
                    }
                )
                if len(failures) >= 10:
                    break
        if len(failures) >= 10:
            break

    return {
        "trials_requested": trials,
        "checks_run": checked,
        "lock_bits": bits,
        "failure_count": len(failures),
        "failures": failures,
    }


def positive_shadow_sample(
    sources: list[tuple[int, ...]],
    targets: list[tuple[str, Fraction]],
    *,
    bits: int,
    source_limit: int,
    q_limit: int,
    example_limit: int,
) -> dict[str, object]:
    examples: list[dict[str, object]] = []
    extra_hist: Counter[int] = Counter()
    starts_checked = 0
    phase_matches = 0
    lock_hits = 0
    formula_failures: list[dict[str, object]] = []

    for source in sources[:source_limit]:
        source_label = word_string(source)
        source_length = len(source)
        phases = phase_data(source)
        rho0 = phases[0]["rho"]
        residue = cylinder_residue(source)
        step_size = 1 << source_length
        for q in range(q_limit):
            x_int = residue + q * step_size
            if x_int <= 0:
                continue
            starts_checked += 1
            source_alignment = v2_fraction(Fraction(x_int) - rho0)
            for phase in phases[:-1]:
                t = int(phase["t"])
                if source_alignment < t:
                    continue
                rho_t = phase["rho"]
                odd_prefix = int(phase["odd_prefix"])
                current = Fraction(x_int)
                for _step in range(t):
                    current = shortcut_step_frac(current)
                for target_label, eta in targets:
                    if rho_t == eta:
                        continue
                    delta = rho_t - eta
                    valuation = v2_fraction(delta)
                    if source_alignment - t != valuation:
                        continue
                    phase_matches += 1
                    actual_extra = v2_fraction(current - eta) - valuation
                    extra_hist[actual_extra] += 1
                    required = required_unit_residue(
                        odd_prefix=odd_prefix,
                        delta=delta,
                        valuation=valuation,
                        bits=bits,
                    )
                    actual_unit = unit_mod_power2(
                        (Fraction(x_int) - rho0) / (1 << source_alignment),
                        bits,
                    )
                    did_hit = actual_extra >= bits
                    residue_hit = actual_unit == required
                    if did_hit:
                        lock_hits += 1
                    if did_hit != residue_hit:
                        formula_failures.append(
                            {
                                "x": x_int,
                                "source": source_label,
                                "target": target_label,
                                "t": t,
                                "valuation": valuation,
                                "actual_extra": actual_extra,
                                "actual_unit_mod_2^R": actual_unit,
                                "required_unit_mod_2^R": required,
                            }
                        )
                    if len(examples) < example_limit:
                        examples.append(
                            {
                                "x": x_int,
                                "source": source_label,
                                "source_length": source_length,
                                "q": q,
                                "source_alignment_m": source_alignment,
                                "phase_t": t,
                                "target": target_label,
                                "valuation_e": valuation,
                                "extra_alignment_bits": actual_extra,
                                "actual_unit_mod_2^R": actual_unit,
                                "required_unit_mod_2^R": required,
                                "hits_R_bit_lock": did_hit,
                            }
                        )

    return {
        "sampled_source_cycles": min(source_limit, len(sources)),
        "q_limit_per_source": q_limit,
        "starts_checked": starts_checked,
        "phase_matches": phase_matches,
        "R_bit_lock_hits": lock_hits,
        "R_bit_lock_hit_fraction_among_phase_matches": round_float(
            lock_hits / phase_matches if phase_matches else 0.0
        ),
        "extra_alignment_histogram": as_counter_dict(extra_hist),
        "formula_failure_count": len(formula_failures),
        "formula_failures": formula_failures[:10],
        "examples": examples,
    }


def toy_locks(max_bits: int) -> dict[str, object]:
    rows = []
    rho_source = Fraction(-1)
    eta = Fraction(-5)
    delta = rho_source - eta
    valuation = v2_fraction(delta)
    for bits in range(1, max_bits + 1):
        required = required_unit_residue(
            odd_prefix=0,
            delta=delta,
            valuation=valuation,
            bits=bits,
        )
        mersenne_unit = 1 % (1 << bits)
        rows.append(
            {
                "bits": bits,
                "required_u_mod_2^bits": required,
                "mersenne_u_equals_1_hits": mersenne_unit == required,
            }
        )
    return {
        "name": "-1 spine to -5 spine at t=0",
        "valuation_e": valuation,
        "equation": "u == -1 mod 2^R",
        "rows": rows,
        "interpretation": (
            "The pure Mersenne unit u=1 gets the first forced odd bit but fails "
            "all deeper R>=2 locks for this toy transition."
        ),
    }


def run(args: argparse.Namespace) -> dict[str, object]:
    started = perf_counter()
    lock_bits = sorted(set(args.lock_bits))
    cycles = enumerate_supercritical_cycles(args.max_depth)
    sources = [w for w in cycles if primitive_period(w) == len(w)]
    targets = target_unique_spines(cycles)
    verify_bits = max(lock_bits)
    formula = verify_lock_formula(
        sources,
        targets,
        bits=verify_bits,
        trials=args.formula_trials,
        seed=args.seed,
    )
    census = build_lock_records(
        sources,
        targets,
        lock_bits,
        example_limit=args.example_limit,
    )
    shadow_sample = positive_shadow_sample(
        sources,
        targets,
        bits=verify_bits,
        source_limit=args.positive_source_limit,
        q_limit=args.positive_q_limit,
        example_limit=args.example_limit,
    )
    toys = toy_locks(verify_bits)

    return {
        "status": "odd-unit-lock-census",
        "elapsed_seconds": round_float(perf_counter() - started, 6),
        "parameters": {
            "max_depth": args.max_depth,
            "lock_bits": lock_bits,
            "formula_trials": args.formula_trials,
            "seed": args.seed,
            "positive_source_limit": args.positive_source_limit,
            "positive_q_limit": args.positive_q_limit,
            "example_limit": args.example_limit,
        },
        "library": {
            "supercritical_necklace_cycles": len(cycles),
            "primitive_source_cycles": len(sources),
            "primitive_source_phase_states": sum(len(w) for w in sources),
            "unique_target_spines": len(targets),
        },
        "formula_verification": formula,
        "lock_census": census,
        "positive_shadow_sample": shadow_sample,
        "toy_locks": toys,
        "interpretation": (
            "The phase gate is only the entry ticket. Once valuations match, "
            "each extra R-bit regeneration event chooses one odd-unit residue "
            "out of 2^(R-1). Repeated locks therefore become a compatibility "
            "and codimension problem, not a solved Collatz theorem."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-depth", type=int, default=12)
    parser.add_argument("--lock-bits", type=parse_int_list, default=parse_int_list("4,8"))
    parser.add_argument("--formula-trials", type=int, default=5000)
    parser.add_argument("--seed", type=int, default=20260705)
    parser.add_argument("--positive-source-limit", type=int, default=64)
    parser.add_argument("--positive-q-limit", type=int, default=32)
    parser.add_argument("--example-limit", type=int, default=12)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--quiet", action="store_true")
    args = parser.parse_args()

    if args.max_depth < 1:
        raise SystemExit("--max-depth must be positive")
    if any(bits < 1 for bits in args.lock_bits):
        raise SystemExit("--lock-bits values must be positive")
    if args.formula_trials < 1:
        raise SystemExit("--formula-trials must be positive")
    if args.positive_source_limit < 1 or args.positive_q_limit < 1:
        raise SystemExit("positive sampling limits must be positive")

    payload = run(args)
    text = json.dumps(payload, indent=2, sort_keys=True)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text + "\n", encoding="utf-8")
    if not args.quiet:
        print(text)


if __name__ == "__main__":
    main()

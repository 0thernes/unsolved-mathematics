#!/usr/bin/env python3
"""Finite odd-unit lock coverage lab.

This extends the phase-collision lab at the next exact choke point.  Once a
source spine phase and target spine are phase-matched, deep regeneration by R
extra 2-adic bits forces one odd-unit residue modulo 2^R:

    u == -3^(-a(t)) * 2^(-e) * (rho_t - eta)  (mod 2^R)

where e = v2(rho_t - eta).  A Collatz proof is not hiding in this script.  The
point is to measure whether the union of these target locks is sparse, saturated,
or structured for the finite supercritical spine library already used by the
repo.

Pure stdlib; exact rational arithmetic.
"""

from __future__ import annotations

import argparse
import json
import math
import sys
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import product
from pathlib import Path
from time import perf_counter

sys.path.insert(0, str(Path(__file__).resolve().parent))

from lib_collatz import cylinder_residue, is_supercritical, spine

SCRIPT_DIR = Path(__file__).resolve().parent


def shortcut_step_frac(x: Fraction) -> Fraction:
    parity = (x.numerator * pow(x.denominator, -1, 2)) & 1
    return (3 * x + 1) / 2 if parity else x / 2


def v2_fraction(x: Fraction, cap: int = 100000) -> int:
    if x == 0:
        return cap
    n = abs(x.numerator)
    count = 0
    while n % 2 == 0:
        n //= 2
        count += 1
    return count


def fraction_mod_2k(x: Fraction, k: int) -> int:
    """Return x modulo 2^k for an odd-denominator rational."""
    modulus = 1 << k
    denom = x.denominator % modulus
    return (x.numerator % modulus) * pow(denom, -1, modulus) % modulus


def canonical_word(w: tuple[int, ...]) -> tuple[int, ...]:
    return min(w[i:] + w[:i] for i in range(len(w)))


def primitive_period(w: tuple[int, ...]) -> int:
    d = len(w)
    for p in range(1, d + 1):
        if d % p == 0 and all(w[i] == w[i % p] for i in range(d)):
            return p
    raise AssertionError("period search failed")


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
    return phases[:-1]


def lock_residue(
    rho_t: Fraction,
    eta: Fraction,
    e: int,
    odd_prefix: int,
    excess_bits: int,
) -> int:
    delta = (rho_t - eta) / (1 << e)
    modulus = 1 << excess_bits
    delta_mod = fraction_mod_2k(delta, excess_bits)
    three_mod = pow(3, odd_prefix, modulus)
    return (-delta_mod * pow(three_mod, -1, modulus)) % modulus


def build_lock_sets(
    sources: list[tuple[int, ...]],
    targets: list[tuple[str, Fraction]],
    excess_bits: list[int],
) -> tuple[dict[str, object], dict[tuple[str, int, int], set[int]]]:
    lock_sets: dict[tuple[str, int, int], set[int]] = defaultdict(set)
    contribution_hist: Counter[int] = Counter()
    valuation_hist: Counter[int] = Counter()
    source_pair_count = 0
    zero_separation_skips = 0
    examples: list[dict[str, object]] = []

    for source in sources:
        source_label = word_string(source)
        d = len(source)
        for phase in phase_data(source):
            t = int(phase["t"])
            rho_t = phase["rho"]
            odd_prefix = int(phase["odd_prefix"])
            for target_label, eta in targets:
                if rho_t == eta:
                    zero_separation_skips += 1
                    continue
                e = v2_fraction(rho_t - eta)
                m_class = (t + e) % d
                valuation_hist[e] += 1
                source_pair_count += 1
                for bits in excess_bits:
                    residue = lock_residue(rho_t, eta, e, odd_prefix, bits)
                    lock_sets[(source_label, m_class, bits)].add(residue)
                    if len(examples) < 10 and bits == excess_bits[-1]:
                        examples.append(
                            {
                                "source": source_label,
                                "target": target_label,
                                "phase_t": t,
                                "source_length": d,
                                "valuation_e": e,
                                "alignment_class_m_mod_d": m_class,
                                "excess_bits": bits,
                                "required_odd_unit_residue": residue,
                            }
                        )

    for residues in lock_sets.values():
        contribution_hist[len(residues)] += 1

    meta = {
        "source_phase_target_pairs": source_pair_count,
        "zero_separation_skips": zero_separation_skips,
        "valuation_histogram": dict(sorted((str(k), v) for k, v in valuation_hist.items())),
        "lock_set_size_histogram_all_bits": dict(
            sorted((str(k), v) for k, v in contribution_hist.items())
        ),
        "examples": examples,
    }
    return meta, lock_sets


def summarize_lock_sets(
    sources: list[tuple[int, ...]],
    lock_sets: dict[tuple[str, int, int], set[int]],
    excess_bits: list[int],
) -> dict[str, object]:
    rows_by_bits: dict[str, object] = {}
    source_labels = {word_string(w): len(w) for w in sources}

    for bits in excess_bits:
        total_odd_residues = 1 << (bits - 1)
        nonempty_fractions: list[float] = []
        all_bin_fractions: list[float] = []
        codim_bits: list[float] = []
        densest: list[dict[str, object]] = []
        empty_bins = 0
        saturated_bins = 0

        for source_label, d in source_labels.items():
            for m_class in range(d):
                residues = lock_sets.get((source_label, m_class, bits), set())
                count = len(residues)
                fraction = count / total_odd_residues
                all_bin_fractions.append(fraction)
                if count == 0:
                    empty_bins += 1
                    continue
                nonempty_fractions.append(fraction)
                if count == total_odd_residues:
                    saturated_bins += 1
                codim_bits.append((bits - 1) - math.log2(count))
                densest.append(
                    {
                        "source": source_label,
                        "source_length": d,
                        "alignment_class_m_mod_d": m_class,
                        "distinct_lock_residues": count,
                        "odd_unit_space_size": total_odd_residues,
                        "coverage_fraction": round(fraction, 12),
                        "codimension_bits": round((bits - 1) - math.log2(count), 6),
                        "sample_residues": sorted(residues)[:12],
                    }
                )

        densest.sort(key=lambda row: (-row["coverage_fraction"], row["source_length"], row["source"]))
        rows_by_bits[str(bits)] = {
            "total_alignment_bins": len(all_bin_fractions),
            "nonempty_alignment_bins": len(nonempty_fractions),
            "empty_alignment_bins": empty_bins,
            "saturated_alignment_bins": saturated_bins,
            "max_coverage_fraction": round(max(all_bin_fractions, default=0.0), 12),
            "avg_coverage_fraction_all_bins": round(
                sum(all_bin_fractions) / len(all_bin_fractions), 12
            ),
            "avg_coverage_fraction_nonempty_bins": round(
                sum(nonempty_fractions) / len(nonempty_fractions), 12
            )
            if nonempty_fractions
            else 0.0,
            "min_codimension_bits_nonempty": round(min(codim_bits), 6) if codim_bits else None,
            "avg_codimension_bits_nonempty": round(sum(codim_bits) / len(codim_bits), 6)
            if codim_bits
            else None,
            "densest_bins": densest[:12],
        }

    return rows_by_bits


def positive_cylinder_probe(
    sources: list[tuple[int, ...]],
    lock_sets: dict[tuple[str, int, int], set[int]],
    excess_bits: list[int],
    limit: int,
) -> dict[str, object]:
    if limit <= 0:
        return {"enabled": False}

    by_bits = {
        bits: {"visits": 0, "hits": 0, "empty_lock_visits": 0, "examples": []}
        for bits in excess_bits
    }

    for source in sources:
        d = len(source)
        source_label = word_string(source)
        rho = spine(source)
        residue = cylinder_residue(source)
        step = 1 << d
        if residue == 0:
            first = step
        else:
            first = residue
        for n in range(first, limit + 1, step):
            diff = Fraction(n) - rho
            m = v2_fraction(diff)
            m_class = m % d
            unit = diff / (1 << m)
            for bits in excess_bits:
                stats = by_bits[bits]
                stats["visits"] += 1
                residues = lock_sets.get((source_label, m_class, bits), set())
                if not residues:
                    stats["empty_lock_visits"] += 1
                    continue
                unit_residue = fraction_mod_2k(unit, bits)
                if unit_residue in residues:
                    stats["hits"] += 1
                    if len(stats["examples"]) < 10:
                        stats["examples"].append(
                            {
                                "n": n,
                                "source": source_label,
                                "source_length": d,
                                "alignment_m": m,
                                "alignment_class_m_mod_d": m_class,
                                "excess_bits": bits,
                                "unit_residue": unit_residue,
                            }
                        )

    return {
        "enabled": True,
        "positive_limit": limit,
        "by_excess_bits": {
            str(bits): {
                **stats,
                "hit_fraction": round(stats["hits"] / stats["visits"], 12)
                if stats["visits"]
                else 0.0,
                "empty_lock_fraction": round(stats["empty_lock_visits"] / stats["visits"], 12)
                if stats["visits"]
                else 0.0,
            }
            for bits, stats in by_bits.items()
        },
    }


def parse_excess_bits(raw: str) -> list[int]:
    bits = sorted({int(part.strip()) for part in raw.split(",") if part.strip()})
    if not bits or bits[0] < 2:
        raise argparse.ArgumentTypeError("excess bits must be comma-separated integers >= 2")
    return bits


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-depth", type=int, default=12)
    parser.add_argument("--min-source-depth", type=int, default=1)
    parser.add_argument("--excess-bits", type=parse_excess_bits, default=parse_excess_bits("4,8,12,16"))
    parser.add_argument("--positive-limit", type=int, default=100000)
    parser.add_argument(
        "--output",
        type=Path,
        default=SCRIPT_DIR / "results" / "odd_unit_lock_coverage_d12_20260705.json",
    )
    parser.add_argument("--quiet", action="store_true")
    args = parser.parse_args()

    start = perf_counter()
    cycles = enumerate_supercritical_cycles(args.max_depth)
    sources = [
        w for w in cycles if primitive_period(w) == len(w) and len(w) >= args.min_source_depth
    ]
    targets_by_spine: dict[Fraction, str] = {}
    for w in sources:
        targets_by_spine.setdefault(spine(w), word_string(w))
    targets = sorted(targets_by_spine.items(), key=lambda item: (len(item[1]), item[1]))
    targets = [(label, eta) for eta, label in targets]

    meta, lock_sets = build_lock_sets(sources, targets, args.excess_bits)
    summary = summarize_lock_sets(sources, lock_sets, args.excess_bits)
    positive_probe = positive_cylinder_probe(sources, lock_sets, args.excess_bits, args.positive_limit)

    result = {
        "status": "finite measurement only; not a proof of Collatz",
        "parameters": {
            "max_depth": args.max_depth,
            "min_source_depth": args.min_source_depth,
            "excess_bits": args.excess_bits,
            "positive_limit": args.positive_limit,
        },
        "cycle_counts": {
            "supercritical_necklace_cycles": len(cycles),
            "primitive_source_cycles": len(sources),
            "unique_target_spines": len(targets),
        },
        "lock_construction": meta,
        "coverage_by_excess_bits": summary,
        "positive_cylinder_probe": positive_probe,
        "runtime_seconds": round(perf_counter() - start, 6),
    }

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    if not args.quiet:
        print(f"wrote {args.output}")
        print(json.dumps(result["cycle_counts"], indent=2, sort_keys=True))
        for bits in args.excess_bits:
            row = summary[str(bits)]
            print(
                "R={bits}: max={max_cov} avg_nonempty={avg_cov} min_codim={codim}".format(
                    bits=bits,
                    max_cov=row["max_coverage_fraction"],
                    avg_cov=row["avg_coverage_fraction_nonempty_bins"],
                    codim=row["min_codimension_bits_nonempty"],
                )
            )
        if positive_probe["enabled"]:
            for bits, row in positive_probe["by_excess_bits"].items():
                print(
                    "positive R={bits}: hits={hits}/{visits} ({frac})".format(
                        bits=bits,
                        hits=row["hits"],
                        visits=row["visits"],
                        frac=row["hit_fraction"],
                    )
                )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

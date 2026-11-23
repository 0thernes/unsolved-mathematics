#!/usr/bin/env python3
"""Classify high-valuation target tails as periodic echoes.

The target-tail lab showed that the first large v2(rho_t - eta) shelf is made
of target words that begin as long repetitions of the source phase word.  This
instrument recomputes the high-tail records and measures the exact echo defect:
periodic prefix length, primitive-breaking suffix, and e-minus-prefix relation.

Finite measurement only; the Collatz conjecture remains open.
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from fractions import Fraction
from pathlib import Path
from statistics import mean
from time import perf_counter

sys.path.insert(0, str(Path(__file__).resolve().parent))

from odd_unit_lock_coverage_lab import enumerate_supercritical_cycles, v2_fraction
from odd_unit_lock_target_tail_lab import (
    periodic_prefix_len,
    primitive_cycles_between,
    source_phases,
    unique_targets,
)

SCRIPT_DIR = Path(__file__).resolve().parent


def suffix_kind(phase_word: str, target: str, prefix: int) -> dict[str, object]:
    if prefix >= len(target):
        return {
            "suffix": "",
            "first_break": None,
            "first_expected_bit": None,
            "first_actual_bit": None,
        }
    expected = phase_word[prefix % len(phase_word)]
    actual = target[prefix]
    return {
        "suffix": target[prefix:],
        "first_break": prefix,
        "first_expected_bit": expected,
        "first_actual_bit": actual,
    }


def run(args: argparse.Namespace) -> dict[str, object]:
    started = perf_counter()
    cycles = enumerate_supercritical_cycles(max(args.source_max_depth, args.target_max_depth))
    sources = primitive_cycles_between(cycles, args.source_min_depth, args.source_max_depth)
    targets = [
        target
        for target in unique_targets(
            primitive_cycles_between(cycles, args.target_min_depth, args.target_max_depth)
        )
        if int(target["depth"]) <= args.target_cutoff
    ]
    phases = source_phases(sources)

    records: list[dict[str, object]] = []
    hist_e: Counter[int] = Counter()
    hist_prefix: Counter[int] = Counter()
    hist_e_minus_prefix: Counter[int] = Counter()
    hist_defect: Counter[int] = Counter()
    hist_phase_t: Counter[int] = Counter()
    hist_source_depth: Counter[int] = Counter()
    hist_target_depth: Counter[int] = Counter()
    hist_suffix: Counter[str] = Counter()
    pair_count = 0
    zero_separation_skips = 0

    for phase in phases:
        rho_t = phase["rho_t"]
        assert isinstance(rho_t, Fraction)
        phase_word = str(phase["phase_word"])
        for target in targets:
            eta = target["eta"]
            assert isinstance(eta, Fraction)
            if rho_t == eta:
                zero_separation_skips += 1
                continue
            pair_count += 1
            e = v2_fraction(rho_t - eta)
            if e < args.threshold:
                continue

            target_label = str(target["label"])
            prefix = periodic_prefix_len(phase_word, target_label)
            defect = len(target_label) - prefix
            suffix = suffix_kind(phase_word, target_label, prefix)
            row = {
                "valuation_e": e,
                "source": phase["source"],
                "source_depth": phase["source_depth"],
                "phase_t": phase["phase_t"],
                "phase_word": phase_word,
                "target": target_label,
                "target_depth": target["depth"],
                "periodic_prefix_len": prefix,
                "periodic_prefix_fraction": round(prefix / len(target_label), 9),
                "periodic_prefix_full_repeats": prefix // len(phase_word),
                "periodic_prefix_remainder": prefix % len(phase_word),
                "echo_defect_length": defect,
                "e_minus_periodic_prefix": e - prefix,
                **suffix,
            }
            records.append(row)
            hist_e[e] += 1
            hist_prefix[prefix] += 1
            hist_e_minus_prefix[e - prefix] += 1
            hist_defect[defect] += 1
            hist_phase_t[int(phase["phase_t"])] += 1
            hist_source_depth[int(phase["source_depth"])] += 1
            hist_target_depth[int(target["depth"])] += 1
            hist_suffix[str(suffix["suffix"])] += 1

    records.sort(
        key=lambda row: (
            -int(row["valuation_e"]),
            int(row["target_depth"]),
            str(row["source"]),
            str(row["target"]),
        )
    )
    prefix_fractions = [float(row["periodic_prefix_fraction"]) for row in records]
    prefix_ge_e = sum(
        int(int(row["periodic_prefix_len"]) >= int(row["valuation_e"])) for row in records
    )
    prefix_ge_threshold = sum(
        int(int(row["periodic_prefix_len"]) >= args.threshold) for row in records
    )
    phase_zero = hist_phase_t.get(0, 0)

    return {
        "status": "finite periodic-echo classification; not a proof of Collatz",
        "parameters": {
            "source_min_depth": args.source_min_depth,
            "source_max_depth": args.source_max_depth,
            "target_min_depth": args.target_min_depth,
            "target_max_depth": args.target_max_depth,
            "target_cutoff": args.target_cutoff,
            "threshold_e_ge": args.threshold,
        },
        "cycle_counts": {
            "primitive_source_cycles": len(sources),
            "source_phases": len(phases),
            "target_spines": len(targets),
            "source_phase_target_pairs": pair_count,
            "zero_separation_skips": zero_separation_skips,
        },
        "summary": {
            "high_tail_records": len(records),
            "phase_t_zero_records": phase_zero,
            "all_records_phase_t_zero": phase_zero == len(records),
            "periodic_prefix_ge_threshold_records": prefix_ge_threshold,
            "periodic_prefix_ge_valuation_records": prefix_ge_e,
            "min_periodic_prefix_fraction": round(min(prefix_fractions), 9)
            if prefix_fractions
            else None,
            "avg_periodic_prefix_fraction": round(mean(prefix_fractions), 9)
            if prefix_fractions
            else None,
            "max_valuation_e": max(hist_e, default=None),
        },
        "histograms": {
            "valuation_e": dict(sorted((str(k), v) for k, v in hist_e.items())),
            "periodic_prefix_len": dict(sorted((str(k), v) for k, v in hist_prefix.items())),
            "e_minus_periodic_prefix": dict(
                sorted((str(k), v) for k, v in hist_e_minus_prefix.items())
            ),
            "echo_defect_length": dict(sorted((str(k), v) for k, v in hist_defect.items())),
            "phase_t": dict(sorted((str(k), v) for k, v in hist_phase_t.items())),
            "source_depth": dict(sorted((str(k), v) for k, v in hist_source_depth.items())),
            "target_depth": dict(sorted((str(k), v) for k, v in hist_target_depth.items())),
            "suffix_after_periodic_prefix_top": {
                str(key): value for key, value in hist_suffix.most_common(24)
            },
        },
        "records": records[: args.max_records],
        "runtime_seconds": round(perf_counter() - started, 6),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-max-depth", type=int, default=10)
    parser.add_argument("--source-min-depth", type=int, default=3)
    parser.add_argument("--target-max-depth", type=int, default=22)
    parser.add_argument("--target-min-depth", type=int, default=1)
    parser.add_argument("--target-cutoff", type=int, default=22)
    parser.add_argument("--threshold", type=int, default=18)
    parser.add_argument("--max-records", type=int, default=512)
    parser.add_argument(
        "--output",
        type=Path,
        default=SCRIPT_DIR / "results" / "odd_unit_lock_periodic_echo_s10_t22_e18_20260705.json",
    )
    args = parser.parse_args()

    if args.target_cutoff > args.target_max_depth:
        parser.error("--target-cutoff must be <= --target-max-depth")

    result = run(args)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    print(f"wrote {args.output}")
    print(json.dumps(result["cycle_counts"], indent=2, sort_keys=True))
    print(json.dumps(result["summary"], indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

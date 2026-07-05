#!/usr/bin/env python3
"""Positive-orbit transition lab for odd-unit lock hits.

The coverage lab measures one source-cylinder visit at a time.  This lab asks
the next finite question: along actual positive shortcut orbits, do odd-unit
lock hits persist from one canonical source-cylinder visit to the next, or do
they behave like cumulative codimension pressure?

This is finite theorem-discovery data, not a proof of Collatz.
"""

from __future__ import annotations

import argparse
import json
import math
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from time import perf_counter

sys.path.insert(0, str(Path(__file__).resolve().parent))

from lib_collatz import cylinder_residue, shortcut_step, spine
from odd_unit_lock_coverage_lab import (
    build_lock_sets,
    enumerate_supercritical_cycles,
    fraction_mod_2k,
    primitive_period,
    v2_fraction,
    word_string,
)

SCRIPT_DIR = Path(__file__).resolve().parent


@dataclass(frozen=True)
class SourceInfo:
    label: str
    word: tuple[int, ...]
    depth: int
    residue: int
    rho: Fraction


@dataclass(frozen=True)
class Visit:
    step: int
    n: int
    source: SourceInfo
    alignment_m: int
    alignment_class: int
    unit_by_bits: dict[int, int]
    lock_count_by_bits: dict[int, int]
    coverage_by_bits: dict[int, float]
    hit_by_bits: dict[int, bool]


def parse_int_list(raw: str) -> list[int]:
    values = sorted({int(part.strip()) for part in raw.split(",") if part.strip()})
    if not values:
        raise argparse.ArgumentTypeError("expected a comma-separated integer list")
    return values


def round_float(value: float, digits: int = 12) -> float:
    return round(float(value), digits)


def make_sources(max_depth: int, min_source_depth: int) -> list[SourceInfo]:
    cycles = enumerate_supercritical_cycles(max_depth)
    primitive = [
        w for w in cycles if primitive_period(w) == len(w) and len(w) >= min_source_depth
    ]
    return [
        SourceInfo(
            label=word_string(w),
            word=w,
            depth=len(w),
            residue=cylinder_residue(w),
            rho=spine(w),
        )
        for w in primitive
    ]


def make_targets(sources: list[SourceInfo]) -> list[tuple[str, Fraction]]:
    targets_by_spine: dict[Fraction, str] = {}
    for source in sources:
        targets_by_spine.setdefault(source.rho, source.label)
    return [
        (label, eta)
        for eta, label in sorted(
            targets_by_spine.items(), key=lambda item: (len(item[1]), item[1])
        )
    ]


def make_depth_index(sources: list[SourceInfo]) -> dict[int, dict[int, SourceInfo]]:
    by_depth: dict[int, dict[int, SourceInfo]] = defaultdict(dict)
    for source in sources:
        by_depth[source.depth][source.residue] = source
    return dict(by_depth)


def deepest_source_match(n: int, by_depth: dict[int, dict[int, SourceInfo]]) -> SourceInfo | None:
    for depth in sorted(by_depth, reverse=True):
        source = by_depth[depth].get(n & ((1 << depth) - 1))
        if source is not None:
            return source
    return None


def visit_for_state(
    n: int,
    step: int,
    source: SourceInfo,
    lock_sets: dict[tuple[str, int, int], set[int]],
    excess_bits: list[int],
) -> Visit:
    diff = Fraction(n) - source.rho
    alignment_m = v2_fraction(diff)
    alignment_class = alignment_m % source.depth
    unit = diff / (1 << alignment_m)
    unit_by_bits: dict[int, int] = {}
    lock_count_by_bits: dict[int, int] = {}
    coverage_by_bits: dict[int, float] = {}
    hit_by_bits: dict[int, bool] = {}

    for bits in excess_bits:
        residues = lock_sets.get((source.label, alignment_class, bits), set())
        unit_residue = fraction_mod_2k(unit, bits)
        total_odd_units = 1 << (bits - 1)
        unit_by_bits[bits] = unit_residue
        lock_count_by_bits[bits] = len(residues)
        coverage_by_bits[bits] = len(residues) / total_odd_units
        hit_by_bits[bits] = unit_residue in residues

    return Visit(
        step=step,
        n=n,
        source=source,
        alignment_m=alignment_m,
        alignment_class=alignment_class,
        unit_by_bits=unit_by_bits,
        lock_count_by_bits=lock_count_by_bits,
        coverage_by_bits=coverage_by_bits,
        hit_by_bits=hit_by_bits,
    )


def as_counter_dict(counter: Counter[object], *, limit: int | None = None) -> dict[str, int]:
    items = sorted(counter.items(), key=lambda item: (-int(item[1]), str(item[0])))
    if limit is not None:
        items = items[:limit]
    return {str(key): int(value) for key, value in items}


def add_example(examples: list[dict[str, object]], visit: Visit, bits: int, start: int) -> None:
    if len(examples) >= 12:
        return
    examples.append(
        {
            "start": start,
            "step": visit.step,
            "n": visit.n,
            "source": visit.source.label,
            "source_depth": visit.source.depth,
            "alignment_m": visit.alignment_m,
            "alignment_class_m_mod_d": visit.alignment_class,
            "excess_bits": bits,
            "unit_residue": visit.unit_by_bits[bits],
            "lock_residue_count": visit.lock_count_by_bits[bits],
            "local_coverage_fraction": round_float(visit.coverage_by_bits[bits]),
        }
    )


def start_values(limit: int, odd_only: bool) -> range:
    if odd_only:
        return range(3, limit + 1, 2)
    return range(2, limit + 1)


def scan_positive_orbits(
    *,
    start_limit: int,
    odd_starts_only: bool,
    max_steps: int,
    by_depth: dict[int, dict[int, SourceInfo]],
    lock_sets: dict[tuple[str, int, int], set[int]],
    excess_bits: list[int],
) -> dict[str, object]:
    starts_scanned = 0
    starts_reaching_one = 0
    total_steps = 0
    source_visits = 0
    source_visit_depth_hist: Counter[int] = Counter()
    source_visit_label_hist: Counter[str] = Counter()
    transition_gap_hist: Counter[int] = Counter()
    orbit_source_visit_hist: Counter[int] = Counter()
    orbit_hit_streak_hist: dict[int, Counter[int]] = {bits: Counter() for bits in excess_bits}
    hit_examples: dict[int, list[dict[str, object]]] = {bits: [] for bits in excess_bits}
    hit_after_hit_examples: dict[int, list[dict[str, object]]] = {bits: [] for bits in excess_bits}
    longest_streak_examples: dict[int, list[dict[str, object]]] = {bits: [] for bits in excess_bits}

    per_bits: dict[int, dict[str, float | int]] = {
        bits: {
            "visits": 0,
            "hits": 0,
            "expected_hits_from_local_coverage": 0.0,
            "source_visit_transitions": 0,
            "previous_hit_transitions": 0,
            "hit_after_hit": 0,
            "expected_hit_after_hit_from_local_coverage": 0.0,
            "previous_miss_transitions": 0,
            "hit_after_miss": 0,
            "same_source_transitions": 0,
            "same_source_hit_after_hit": 0,
            "max_hit_streak": 0,
            "orbits_with_any_hit": 0,
        }
        for bits in excess_bits
    }

    for start in start_values(start_limit, odd_starts_only):
        starts_scanned += 1
        n = start
        seen: set[int] = set()
        previous_visit: Visit | None = None
        orbit_source_visits = 0
        current_streak = {bits: 0 for bits in excess_bits}
        max_streak = {bits: 0 for bits in excess_bits}
        orbit_had_hit = {bits: False for bits in excess_bits}

        for step in range(max_steps + 1):
            if n in seen:
                break
            seen.add(n)
            total_steps += 1
            source = deepest_source_match(n, by_depth)
            if source is not None:
                visit = visit_for_state(n, step, source, lock_sets, excess_bits)
                source_visits += 1
                orbit_source_visits += 1
                source_visit_depth_hist[source.depth] += 1
                source_visit_label_hist[source.label] += 1

                if previous_visit is not None:
                    transition_gap_hist[visit.step - previous_visit.step] += 1

                for bits in excess_bits:
                    row = per_bits[bits]
                    hit = visit.hit_by_bits[bits]
                    coverage = visit.coverage_by_bits[bits]
                    row["visits"] = int(row["visits"]) + 1
                    row["expected_hits_from_local_coverage"] = (
                        float(row["expected_hits_from_local_coverage"]) + coverage
                    )

                    if hit:
                        row["hits"] = int(row["hits"]) + 1
                        row["orbits_with_any_hit"] = int(row["orbits_with_any_hit"]) + (
                            0 if orbit_had_hit[bits] else 1
                        )
                        orbit_had_hit[bits] = True
                        current_streak[bits] += 1
                        max_streak[bits] = max(max_streak[bits], current_streak[bits])
                        add_example(hit_examples[bits], visit, bits, start)
                    else:
                        current_streak[bits] = 0

                    if previous_visit is not None:
                        previous_hit = previous_visit.hit_by_bits[bits]
                        row["source_visit_transitions"] = int(row["source_visit_transitions"]) + 1
                        if previous_visit.source.label == visit.source.label:
                            row["same_source_transitions"] = int(row["same_source_transitions"]) + 1
                        if previous_hit:
                            row["previous_hit_transitions"] = (
                                int(row["previous_hit_transitions"]) + 1
                            )
                            row["expected_hit_after_hit_from_local_coverage"] = (
                                float(row["expected_hit_after_hit_from_local_coverage"])
                                + coverage
                            )
                            if hit:
                                row["hit_after_hit"] = int(row["hit_after_hit"]) + 1
                                add_example(hit_after_hit_examples[bits], visit, bits, start)
                                if previous_visit.source.label == visit.source.label:
                                    row["same_source_hit_after_hit"] = (
                                        int(row["same_source_hit_after_hit"]) + 1
                                    )
                        else:
                            row["previous_miss_transitions"] = (
                                int(row["previous_miss_transitions"]) + 1
                            )
                            if hit:
                                row["hit_after_miss"] = int(row["hit_after_miss"]) + 1

                previous_visit = visit

            if n == 1:
                starts_reaching_one += 1
                break
            n = shortcut_step(n)

        orbit_source_visit_hist[orbit_source_visits] += 1
        for bits in excess_bits:
            orbit_hit_streak_hist[bits][max_streak[bits]] += 1
            row = per_bits[bits]
            row["max_hit_streak"] = max(int(row["max_hit_streak"]), max_streak[bits])
            if max_streak[bits]:
                longest_streak_examples[bits].append(
                    {
                        "start": start,
                        "max_hit_streak": max_streak[bits],
                        "source_visits_in_orbit": orbit_source_visits,
                    }
                )

    by_bits: dict[str, object] = {}
    for bits in excess_bits:
        row = per_bits[bits]
        visits = int(row["visits"])
        hits = int(row["hits"])
        expected_hits = float(row["expected_hits_from_local_coverage"])
        previous_hit = int(row["previous_hit_transitions"])
        hit_after_hit = int(row["hit_after_hit"])
        expected_after_hit = float(row["expected_hit_after_hit_from_local_coverage"])
        previous_miss = int(row["previous_miss_transitions"])
        hit_after_miss = int(row["hit_after_miss"])
        source_transitions = int(row["source_visit_transitions"])
        by_bits[str(bits)] = {
            "source_visits": visits,
            "lock_hits": hits,
            "hit_fraction": round_float(hits / visits if visits else 0.0),
            "expected_hits_from_local_coverage": round_float(expected_hits),
            "observed_over_expected_hits": round_float(
                hits / expected_hits if expected_hits else 0.0
            ),
            "source_visit_transitions": source_transitions,
            "previous_hit_transitions": previous_hit,
            "hit_after_hit": hit_after_hit,
            "hit_after_hit_fraction": round_float(
                hit_after_hit / previous_hit if previous_hit else 0.0
            ),
            "expected_hit_after_hit_from_local_coverage": round_float(expected_after_hit),
            "observed_over_expected_hit_after_hit": round_float(
                hit_after_hit / expected_after_hit if expected_after_hit else 0.0
            ),
            "previous_miss_transitions": previous_miss,
            "hit_after_miss": hit_after_miss,
            "hit_after_miss_fraction": round_float(
                hit_after_miss / previous_miss if previous_miss else 0.0
            ),
            "same_source_transitions": int(row["same_source_transitions"]),
            "same_source_hit_after_hit": int(row["same_source_hit_after_hit"]),
            "max_hit_streak": int(row["max_hit_streak"]),
            "orbits_with_any_hit": int(row["orbits_with_any_hit"]),
            "orbit_max_hit_streak_histogram": as_counter_dict(orbit_hit_streak_hist[bits]),
            "hit_examples": hit_examples[bits],
            "hit_after_hit_examples": hit_after_hit_examples[bits],
            "longest_streak_examples": sorted(
                longest_streak_examples[bits],
                key=lambda item: (-int(item["max_hit_streak"]), int(item["start"])),
            )[:12],
        }

    return {
        "starts_scanned": starts_scanned,
        "starts_reaching_one_within_cap": starts_reaching_one,
        "total_shortcut_states_examined": total_steps,
        "canonical_source_visits": source_visits,
        "source_visit_depth_histogram": as_counter_dict(source_visit_depth_hist, limit=20),
        "top_source_visit_labels": as_counter_dict(source_visit_label_hist, limit=20),
        "source_visits_per_orbit_histogram": as_counter_dict(orbit_source_visit_hist, limit=20),
        "transition_gap_histogram": as_counter_dict(transition_gap_hist, limit=20),
        "by_excess_bits": by_bits,
    }


def check_row(name: str, passed: bool, detail: object) -> dict[str, object]:
    return {"name": name, "passed": bool(passed), "detail": detail}


def build_checks(scan: dict[str, object]) -> list[dict[str, object]]:
    by_bits = scan["by_excess_bits"]
    r12 = by_bits.get("12", {})
    r16 = by_bits.get("16", {})
    return [
        check_row(
            "all_scanned_positive_starts_reach_one_within_cap",
            scan["starts_scanned"] == scan["starts_reaching_one_within_cap"],
            {
                "starts_scanned": scan["starts_scanned"],
                "starts_reaching_one_within_cap": scan["starts_reaching_one_within_cap"],
            },
        ),
        check_row(
            "r16_lock_hits_are_sparse",
            bool(r16) and float(r16["hit_fraction"]) < 0.01,
            {
                "r16_hit_fraction": r16.get("hit_fraction"),
                "r16_lock_hits": r16.get("lock_hits"),
                "r16_source_visits": r16.get("source_visits"),
            },
        ),
        check_row(
            "r16_hit_after_hit_not_excessive_against_local_coverage_baseline",
            bool(r16) and float(r16["observed_over_expected_hit_after_hit"]) <= 2.0,
            {
                "r16_hit_after_hit": r16.get("hit_after_hit"),
                "r16_previous_hit_transitions": r16.get("previous_hit_transitions"),
                "r16_observed_over_expected_hit_after_hit": r16.get(
                    "observed_over_expected_hit_after_hit"
                ),
            },
        ),
        check_row(
            "r16_max_hit_streak_at_most_two_for_current_scan",
            bool(r16) and int(r16["max_hit_streak"]) <= 2,
            {"r16_max_hit_streak": r16.get("max_hit_streak")},
        ),
        check_row(
            "r12_medium_precision_correlation_warning_present",
            bool(r12) and float(r12["observed_over_expected_hit_after_hit"]) > 2.0,
            {
                "r12_observed_over_expected_hit_after_hit": r12.get(
                    "observed_over_expected_hit_after_hit"
                ),
                "r12_max_hit_streak": r12.get("max_hit_streak"),
            },
        ),
    ]


def theorem_pressure_summary(scan: dict[str, object]) -> dict[str, object]:
    by_bits = scan["by_excess_bits"]
    r12 = by_bits.get("12", {})
    r16 = by_bits.get("16", {})
    return {
        "encouraging_signal": (
            "At R=16, lock hits are sparse and hit-after-hit transitions stay close "
            "to the local-coverage baseline in this finite scan."
        ),
        "warning_signal": (
            "At R=12, hit-after-hit transitions substantially exceed the local "
            "coverage baseline, so a proof cannot use a lazy independence argument."
        ),
        "r12_observed_over_expected_hit_after_hit": r12.get(
            "observed_over_expected_hit_after_hit"
        ),
        "r16_observed_over_expected_hit_after_hit": r16.get(
            "observed_over_expected_hit_after_hit"
        ),
        "r16_max_hit_streak": r16.get("max_hit_streak"),
        "next_microscope_target": (
            "Reconstruct the exact two-step R=16 hit-after-hit transitions and "
            "classify whether they share one dynamic mechanism or split into "
            "several finite families."
        ),
    }


def run(args: argparse.Namespace) -> dict[str, object]:
    started = perf_counter()
    excess_bits = sorted(set(args.excess_bits))
    sources = make_sources(args.max_depth, args.min_source_depth)
    targets = make_targets(sources)
    _meta, lock_sets = build_lock_sets(
        [source.word for source in sources],
        targets,
        excess_bits,
    )
    by_depth = make_depth_index(sources)
    scan = scan_positive_orbits(
        start_limit=args.start_limit,
        odd_starts_only=args.odd_starts_only,
        max_steps=args.max_steps,
        by_depth=by_depth,
        lock_sets=lock_sets,
        excess_bits=excess_bits,
    )
    checks = build_checks(scan)
    return {
        "status": "odd-unit-lock-transition-lab",
        "result": "finite measurement only; not a proof of Collatz",
        "elapsed_seconds": round_float(perf_counter() - started, 6),
        "all_checks_passed": all(row["passed"] for row in checks),
        "checks": checks,
        "parameters": {
            "max_depth": args.max_depth,
            "min_source_depth": args.min_source_depth,
            "excess_bits": excess_bits,
            "start_limit": args.start_limit,
            "odd_starts_only": args.odd_starts_only,
            "max_steps": args.max_steps,
        },
        "library": {
            "canonical_primitive_sources": len(sources),
            "unique_target_spines": len(targets),
            "max_source_depth": max((source.depth for source in sources), default=0),
            "source_depths": sorted({source.depth for source in sources}),
        },
        "scan": scan,
        "theorem_pressure_summary": theorem_pressure_summary(scan),
        "interpretation": (
            "This probes whether lock hits persist along actual positive orbits. "
            "Ratios near the local-coverage expectation support the codimension "
            "route; large hit-after-hit excess would expose a counter-pattern to "
            "explain before claiming cumulative lock loss."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-depth", type=int, default=13)
    parser.add_argument("--min-source-depth", type=int, default=3)
    parser.add_argument("--excess-bits", type=parse_int_list, default=parse_int_list("8,12,16"))
    parser.add_argument("--start-limit", type=int, default=50000)
    parser.add_argument("--max-steps", type=int, default=512)
    parser.add_argument("--odd-starts-only", action=argparse.BooleanOptionalAction, default=True)
    parser.add_argument(
        "--output",
        type=Path,
        default=SCRIPT_DIR / "results" / "odd_unit_lock_transition_d13_N50000_20260705.json",
    )
    parser.add_argument("--quiet", action="store_true")
    args = parser.parse_args()

    if args.max_depth < 1:
        raise SystemExit("--max-depth must be positive")
    if args.min_source_depth < 1:
        raise SystemExit("--min-source-depth must be positive")
    if any(bits < 2 for bits in args.excess_bits):
        raise SystemExit("--excess-bits values must be >= 2")
    if args.start_limit < 2:
        raise SystemExit("--start-limit must be >= 2")
    if args.max_steps < 1:
        raise SystemExit("--max-steps must be positive")

    result = run(args)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    if not args.quiet:
        print(f"wrote {args.output}")
        print(json.dumps(result["library"], indent=2, sort_keys=True))
        scan = result["scan"]
        print(
            "starts={starts} source_visits={visits}".format(
                starts=scan["starts_scanned"],
                visits=scan["canonical_source_visits"],
            )
        )
        for bits, row in scan["by_excess_bits"].items():
            print(
                "R={bits}: hits={hits}/{visits} ({hit_fraction}), "
                "after-hit={hah}/{prev} ({hah_fraction}), max_streak={streak}".format(
                    bits=bits,
                    hits=row["lock_hits"],
                    visits=row["source_visits"],
                    hit_fraction=row["hit_fraction"],
                    hah=row["hit_after_hit"],
                    prev=row["previous_hit_transitions"],
                    hah_fraction=row["hit_after_hit_fraction"],
                    streak=row["max_hit_streak"],
                )
            )
        print(f"checks_passed={result['all_checks_passed']}")
    if not result["all_checks_passed"]:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

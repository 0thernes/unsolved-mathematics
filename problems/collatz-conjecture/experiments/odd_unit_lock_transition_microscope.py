#!/usr/bin/env python3
"""Microscope for rare odd-unit lock hit-after-hit transitions.

`odd_unit_lock_transition_lab.py` found that R=16 lock hits along positive
orbits are sparse, and that repeat hits are rarer still. This script expands
those repeat hits into exact transition records:

* previous and current positive states;
* source spine labels and depths;
* alignment classes and odd-unit residues;
* all target-lock witnesses responsible for the hit;
* shortcut gap between the two canonical source-cylinder visits.

This is finite theorem-discovery data, not a proof of Collatz.
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter, defaultdict
from dataclasses import asdict
from fractions import Fraction
from pathlib import Path
from time import perf_counter

sys.path.insert(0, str(Path(__file__).resolve().parent))

from lib_collatz import shortcut_step, spine
from odd_unit_lock_coverage_lab import (
    enumerate_supercritical_cycles,
    lock_residue,
    phase_data,
    primitive_period,
    v2_fraction,
    word_string,
)
from odd_unit_lock_transition_lab import (
    SourceInfo,
    deepest_source_match,
    make_depth_index,
    make_sources,
    make_targets,
    visit_for_state,
)

SCRIPT_DIR = Path(__file__).resolve().parent


def round_float(value: float, digits: int = 12) -> float:
    return round(float(value), digits)


def compact_fraction(x: Fraction) -> str:
    if x.denominator == 1:
        return str(x.numerator)
    return f"{x.numerator}/{x.denominator}"


def source_words(max_depth: int, min_source_depth: int) -> list[tuple[int, ...]]:
    cycles = enumerate_supercritical_cycles(max_depth)
    return [
        w for w in cycles if primitive_period(w) == len(w) and len(w) >= min_source_depth
    ]


def build_lock_witnesses(
    words: list[tuple[int, ...]],
    bits: int,
) -> dict[tuple[str, int, int], list[dict[str, object]]]:
    """Map (source_label, alignment_class, unit_residue) to target witnesses."""
    targets_by_spine: dict[Fraction, str] = {}
    for w in words:
        targets_by_spine.setdefault(spine(w), word_string(w))
    targets = [
        (label, eta)
        for eta, label in sorted(
            targets_by_spine.items(), key=lambda item: (len(item[1]), item[1])
        )
    ]

    witnesses: dict[tuple[str, int, int], list[dict[str, object]]] = defaultdict(list)
    for w in words:
        source_label = word_string(w)
        d = len(w)
        for phase in phase_data(w):
            t = int(phase["t"])
            rho_t = phase["rho"]
            odd_prefix = int(phase["odd_prefix"])
            for target_label, eta in targets:
                if rho_t == eta:
                    continue
                e = v2_fraction(rho_t - eta)
                m_class = (t + e) % d
                residue = lock_residue(rho_t, eta, e, odd_prefix, bits)
                witnesses[(source_label, m_class, residue)].append(
                    {
                        "target": target_label,
                        "phase_t": t,
                        "valuation_e": e,
                        "odd_prefix": odd_prefix,
                        "source_phase_rho": compact_fraction(rho_t),
                        "target_eta": compact_fraction(eta),
                    }
                )
    for key in list(witnesses):
        witnesses[key].sort(
            key=lambda item: (
                len(str(item["target"])),
                str(item["target"]),
                int(item["phase_t"]),
                int(item["valuation_e"]),
            )
        )
    return dict(witnesses)


def visit_payload(visit, bits: int, witnesses: dict[tuple[str, int, int], list[dict[str, object]]]) -> dict[str, object]:
    key = (
        visit.source.label,
        visit.alignment_class,
        visit.unit_by_bits[bits],
    )
    hit_witnesses = witnesses.get(key, [])
    return {
        "step": visit.step,
        "n": visit.n,
        "source": visit.source.label,
        "source_depth": visit.source.depth,
        "source_residue": visit.source.residue,
        "source_rho": compact_fraction(visit.source.rho),
        "alignment_m": visit.alignment_m,
        "alignment_class_m_mod_d": visit.alignment_class,
        "unit_residue": visit.unit_by_bits[bits],
        "lock_residue_count_for_bin": visit.lock_count_by_bits[bits],
        "local_coverage_fraction": round_float(visit.coverage_by_bits[bits]),
        "witness_count_for_unit_residue": len(hit_witnesses),
        "witnesses": hit_witnesses[:20],
    }


def shortcut_segment(start: int, steps: int, limit: int = 32) -> dict[str, object]:
    n = start
    states = [n]
    parities: list[int] = []
    for _ in range(steps):
        parities.append(n & 1)
        n = shortcut_step(n)
        states.append(n)

    truncated = len(states) > limit
    if truncated:
        half = max(1, limit // 2)
        shown_states = states[:half] + states[-half:]
    else:
        shown_states = states

    return {
        "gap_steps": steps,
        "parity_word": "".join(str(bit) for bit in parities),
        "states": shown_states,
        "states_truncated": truncated,
        "final_state": states[-1],
    }


def transition_signature(previous, current, bits: int) -> str:
    return "|".join(
        [
            previous.source.label,
            str(previous.alignment_class),
            str(previous.unit_by_bits[bits]),
            current.source.label,
            str(current.alignment_class),
            str(current.unit_by_bits[bits]),
        ]
    )


def start_values(limit: int, odd_only: bool) -> range:
    if odd_only:
        return range(3, limit + 1, 2)
    return range(2, limit + 1)


def scan_transitions(
    *,
    start_limit: int,
    odd_starts_only: bool,
    max_steps: int,
    bits: int,
    sources: list[SourceInfo],
    witnesses: dict[tuple[str, int, int], list[dict[str, object]]],
) -> dict[str, object]:
    by_depth = make_depth_index(sources)
    transitions: list[dict[str, object]] = []
    gap_hist: Counter[int] = Counter()
    source_pair_hist: Counter[str] = Counter()
    depth_pair_hist: Counter[str] = Counter()
    alignment_pair_hist: Counter[str] = Counter()
    segment_word_hist: Counter[str] = Counter()
    shared_target_count_hist: Counter[int] = Counter()
    target_hist: Counter[str] = Counter()
    signature_hist: Counter[str] = Counter()
    same_source_count = 0
    starts_scanned = 0
    starts_reaching_one = 0
    total_states = 0
    total_hits = 0
    total_visits = 0
    previous_hit_transitions = 0
    expected_hits = 0.0
    expected_hit_after_hit = 0.0
    starts_with_repeat = set()

    # Rebuild the set-valued view needed by visit_for_state from witnesses.
    lock_sets: dict[tuple[str, int, int], set[int]] = defaultdict(set)
    for source_label, alignment_class, residue in witnesses:
        lock_sets[(source_label, alignment_class, bits)].add(residue)

    for start in start_values(start_limit, odd_starts_only):
        starts_scanned += 1
        n = start
        seen: set[int] = set()
        previous_visit = None
        for step in range(max_steps + 1):
            if n in seen:
                break
            seen.add(n)
            total_states += 1
            source = deepest_source_match(n, by_depth)
            if source is not None:
                visit = visit_for_state(n, step, source, lock_sets, [bits])
                total_visits += 1
                expected_hits += visit.coverage_by_bits[bits]
                if visit.hit_by_bits[bits]:
                    total_hits += 1
                if previous_visit is not None and previous_visit.hit_by_bits[bits]:
                    previous_hit_transitions += 1
                    expected_hit_after_hit += visit.coverage_by_bits[bits]
                    if visit.hit_by_bits[bits]:
                        gap = visit.step - previous_visit.step
                        source_pair = f"{previous_visit.source.label}->{visit.source.label}"
                        depth_pair = f"{previous_visit.source.depth}->{visit.source.depth}"
                        alignment_pair = (
                            f"{previous_visit.alignment_class}->{visit.alignment_class}"
                        )
                        signature = transition_signature(previous_visit, visit, bits)
                        previous_payload = visit_payload(previous_visit, bits, witnesses)
                        current_payload = visit_payload(visit, bits, witnesses)
                        previous_targets = {
                            str(row["target"]) for row in previous_payload["witnesses"]
                        }
                        current_targets = {str(row["target"]) for row in current_payload["witnesses"]}
                        shared_targets = sorted(previous_targets & current_targets)
                        segment = shortcut_segment(previous_visit.n, gap)
                        gap_hist[gap] += 1
                        source_pair_hist[source_pair] += 1
                        depth_pair_hist[depth_pair] += 1
                        alignment_pair_hist[alignment_pair] += 1
                        segment_word_hist[str(segment["parity_word"])] += 1
                        shared_target_count_hist[len(shared_targets)] += 1
                        target_hist.update(previous_targets)
                        target_hist.update(current_targets)
                        signature_hist[signature] += 1
                        same_source_count += int(previous_visit.source.label == visit.source.label)
                        starts_with_repeat.add(start)
                        transitions.append(
                            {
                                "start": start,
                                "gap_shortcut_steps": gap,
                                "same_source": previous_visit.source.label == visit.source.label,
                                "source_pair": source_pair,
                                "depth_pair": depth_pair,
                                "alignment_class_pair": alignment_pair,
                                "signature": signature,
                                "shared_target_count": len(shared_targets),
                                "shared_targets": shared_targets,
                                "shortcut_segment": segment,
                                "previous": previous_payload,
                                "current": current_payload,
                            }
                        )
                previous_visit = visit
            if n == 1:
                starts_reaching_one += 1
                break
            n = shortcut_step(n)

    transitions.sort(key=lambda row: (int(row["start"]), int(row["previous"]["step"])))
    return {
        "starts_scanned": starts_scanned,
        "starts_reaching_one_within_cap": starts_reaching_one,
        "total_shortcut_states_examined": total_states,
        "total_canonical_source_visits": total_visits,
        "total_lock_hits": total_hits,
        "hit_fraction": round_float(total_hits / total_visits if total_visits else 0.0),
        "expected_hits_from_local_coverage": round_float(expected_hits),
        "observed_over_expected_hits": round_float(total_hits / expected_hits if expected_hits else 0.0),
        "previous_hit_transitions": previous_hit_transitions,
        "expected_hit_after_hit_from_local_coverage": round_float(expected_hit_after_hit),
        "observed_over_expected_hit_after_hit": round_float(
            len(transitions) / expected_hit_after_hit if expected_hit_after_hit else 0.0
        ),
        "hit_after_hit_transitions": len(transitions),
        "hit_after_hit_fraction": round_float(
            len(transitions) / previous_hit_transitions if previous_hit_transitions else 0.0
        ),
        "starts_with_repeat_count": len(starts_with_repeat),
        "starts_with_repeat": sorted(starts_with_repeat),
        "same_source_repeat_count": same_source_count,
        "different_source_repeat_count": len(transitions) - same_source_count,
        "gap_histogram": dict(sorted((str(k), v) for k, v in gap_hist.items())),
        "source_pair_histogram": dict(sorted(source_pair_hist.items(), key=lambda item: (-item[1], item[0]))),
        "depth_pair_histogram": dict(sorted(depth_pair_hist.items(), key=lambda item: (-item[1], item[0]))),
        "alignment_class_pair_histogram": dict(
            sorted(alignment_pair_hist.items(), key=lambda item: (-item[1], item[0]))
        ),
        "shortcut_segment_parity_histogram": dict(
            sorted(segment_word_hist.items(), key=lambda item: (-item[1], item[0]))
        ),
        "shared_target_count_histogram": dict(
            sorted((str(k), v) for k, v in shared_target_count_hist.items())
        ),
        "top_matching_targets_across_pairs": dict(
            sorted(target_hist.items(), key=lambda item: (-item[1], item[0]))[:20]
        ),
        "signature_histogram": dict(sorted(signature_hist.items(), key=lambda item: (-item[1], item[0]))),
        "transitions": transitions,
    }


def classify(scan: dict[str, object]) -> dict[str, object]:
    transitions = scan["transitions"]
    all_different_source = all(not row["same_source"] for row in transitions)
    repeated_signatures = {
        key: value
        for key, value in scan["signature_histogram"].items()
        if int(value) > 1
    }
    return {
        "all_repeat_hits_cross_source": all_different_source,
        "repeated_signature_count": len(repeated_signatures),
        "repeated_signatures": repeated_signatures,
        "dominant_gap": max(scan["gap_histogram"].items(), key=lambda item: item[1])[0]
        if scan["gap_histogram"]
        else None,
        "dominant_source_pair": next(iter(scan["source_pair_histogram"]), None),
        "interpretation": (
            "If repeat hits all cross source labels and do not collapse to one "
            "signature, the next theorem target is a transition-family classifier, "
            "not a same-spine persistence lemma."
        ),
    }


def run(args: argparse.Namespace) -> dict[str, object]:
    started = perf_counter()
    words = source_words(args.max_depth, args.min_source_depth)
    sources = make_sources(args.max_depth, args.min_source_depth)
    witnesses = build_lock_witnesses(words, args.excess_bits)
    scan = scan_transitions(
        start_limit=args.start_limit,
        odd_starts_only=args.odd_starts_only,
        max_steps=args.max_steps,
        bits=args.excess_bits,
        sources=sources,
        witnesses=witnesses,
    )
    classification = classify(scan)
    checks = [
        {
            "name": "all_scanned_positive_starts_reach_one_within_cap",
            "passed": scan["starts_scanned"] == scan["starts_reaching_one_within_cap"],
            "detail": {
                "starts_scanned": scan["starts_scanned"],
                "starts_reaching_one_within_cap": scan["starts_reaching_one_within_cap"],
            },
        },
        {
            "name": "hit_after_hit_not_above_twice_local_coverage_baseline",
            "passed": float(scan["observed_over_expected_hit_after_hit"]) <= 2.0,
            "detail": {
                "excess_bits": args.excess_bits,
                "observed_over_expected_hit_after_hit": scan[
                    "observed_over_expected_hit_after_hit"
                ],
            },
        },
    ]
    if (
        args.max_depth == 13
        and args.min_source_depth == 3
        and args.excess_bits == 16
        and args.start_limit == 50000
        and args.odd_starts_only
        and args.max_steps == 512
    ):
        checks.extend(
            [
                {
                    "name": "default_r16_repeat_hit_count_matches_transition_lab",
                    "passed": scan["hit_after_hit_transitions"] == 12,
                    "detail": {
                        "hit_after_hit_transitions": scan["hit_after_hit_transitions"],
                        "baseline": 12,
                    },
                },
                {
                    "name": "default_r16_same_source_repeat_hits_absent",
                    "passed": scan["same_source_repeat_count"] == 0,
                    "detail": {"same_source_repeat_count": scan["same_source_repeat_count"]},
                },
            ]
        )
    return {
        "status": "odd-unit-lock-transition-microscope",
        "result": "finite measurement only; not a proof of Collatz",
        "elapsed_seconds": round_float(perf_counter() - started, 6),
        "parameters": {
            "max_depth": args.max_depth,
            "min_source_depth": args.min_source_depth,
            "excess_bits": args.excess_bits,
            "start_limit": args.start_limit,
            "odd_starts_only": args.odd_starts_only,
            "max_steps": args.max_steps,
        },
        "library": {
            "canonical_primitive_sources": len(sources),
            "source_depths": sorted({source.depth for source in sources}),
            "lock_witness_keys": len(witnesses),
        },
        "scan": scan,
        "classification": classification,
        "checks": checks,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-depth", type=int, default=13)
    parser.add_argument("--min-source-depth", type=int, default=3)
    parser.add_argument("--excess-bits", "--bits", dest="excess_bits", type=int, default=16)
    parser.add_argument("--start-limit", type=int, default=50000)
    parser.add_argument("--max-steps", type=int, default=512)
    parser.add_argument("--odd-starts-only", action=argparse.BooleanOptionalAction, default=True)
    parser.add_argument(
        "--output",
        type=Path,
        default=SCRIPT_DIR / "results" / "odd_unit_lock_transition_microscope_d13_R16_N50000_20260705.json",
    )
    parser.add_argument("--quiet", action="store_true")
    args = parser.parse_args()

    if args.max_depth < 1:
        raise SystemExit("--max-depth must be positive")
    if args.min_source_depth < 1:
        raise SystemExit("--min-source-depth must be positive")
    if args.excess_bits < 2:
        raise SystemExit("--excess-bits must be >= 2")
    if args.start_limit < 2:
        raise SystemExit("--start-limit must be >= 2")
    if args.max_steps < 1:
        raise SystemExit("--max-steps must be positive")

    payload = run(args)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    if not args.quiet:
        print(f"wrote {args.output}")
        print(json.dumps(payload["library"], indent=2, sort_keys=True))
        print(
            "repeat_hits={hits} same_source={same} starts={starts}".format(
                hits=payload["scan"]["hit_after_hit_transitions"],
                same=payload["scan"]["same_source_repeat_count"],
                starts=payload["scan"]["starts_with_repeat_count"],
            )
        )
    if not all(row["passed"] for row in payload["checks"]):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

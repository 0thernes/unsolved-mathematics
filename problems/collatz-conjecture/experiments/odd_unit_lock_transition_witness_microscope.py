#!/usr/bin/env python3
"""Witness-level microscope for rare consecutive odd-unit lock hits.

The transition lab found that R=16 lock hits almost never chain, but not never.
This script reconstructs those hit-after-hit transitions with exact witnesses:
source cylinders, alignment classes, odd-unit residues, target locks, and the
shortcut bridge between the two visits.

Finite theorem-discovery data only; not a proof of Collatz.
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter, defaultdict
from fractions import Fraction
from pathlib import Path
from time import perf_counter

sys.path.insert(0, str(Path(__file__).resolve().parent))

from lib_collatz import shortcut_step
from odd_unit_lock_coverage_lab import (
    build_lock_sets,
    lock_residue,
    phase_data,
    v2_fraction,
)
from odd_unit_lock_transition_lab import (
    SourceInfo,
    Visit,
    as_counter_dict,
    deepest_source_match,
    make_depth_index,
    make_sources,
    make_targets,
    round_float,
    start_values,
    visit_for_state,
)

SCRIPT_DIR = Path(__file__).resolve().parent


def bridge_between(prev: Visit, nxt: Visit) -> dict[str, object]:
    n = prev.n
    states = [n]
    bits: list[int] = []
    for _step in range(nxt.step - prev.step):
        bits.append(n & 1)
        n = shortcut_step(n)
        states.append(n)
    if n != nxt.n:
        raise AssertionError((prev.n, nxt.n, n, prev.step, nxt.step))
    return {
        "gap_shortcut_steps": nxt.step - prev.step,
        "parity_word_01": "".join(str(bit) for bit in bits),
        "parity_word_EO": "".join("O" if bit else "E" for bit in bits),
        "states": states,
    }


def serialize_visit(
    visit: Visit,
    bits: int,
    witness_counts: Counter[tuple[str, int, int]],
    witness_samples: dict[tuple[str, int, int], list[dict[str, object]]],
) -> dict[str, object]:
    key = (visit.source.label, visit.alignment_class, visit.unit_by_bits[bits])
    witnesses = witness_samples.get(key, [])
    targets = sorted({str(item["target"]) for item in witnesses})
    return {
        "step": visit.step,
        "n": visit.n,
        "source": visit.source.label,
        "source_depth": visit.source.depth,
        "alignment_m": visit.alignment_m,
        "alignment_class_m_mod_d": visit.alignment_class,
        "unit_residue_mod_2^R": visit.unit_by_bits[bits],
        "lock_residue_count_in_union": visit.lock_count_by_bits[bits],
        "local_coverage_fraction": round_float(visit.coverage_by_bits[bits]),
        "witness_lock_count_for_this_residue": int(witness_counts[key]),
        "witness_targets_sample": targets[:12],
        "witness_samples": witnesses[:12],
    }


def transition_signature(prev: Visit, nxt: Visit, bits: int, bridge: dict[str, object]) -> tuple[object, ...]:
    return (
        prev.n,
        prev.source.label,
        prev.alignment_class,
        prev.unit_by_bits[bits],
        nxt.n,
        nxt.source.label,
        nxt.alignment_class,
        nxt.unit_by_bits[bits],
        bridge["parity_word_01"],
    )


def build_witness_maps(
    sources: list[SourceInfo],
    targets: list[tuple[str, Fraction]],
    bits: int,
    sample_limit: int,
) -> tuple[Counter[tuple[str, int, int]], dict[tuple[str, int, int], list[dict[str, object]]]]:
    counts: Counter[tuple[str, int, int]] = Counter()
    samples: dict[tuple[str, int, int], list[dict[str, object]]] = defaultdict(list)

    for source in sources:
        for phase in phase_data(source.word):
            t = int(phase["t"])
            rho_t = phase["rho"]
            odd_prefix = int(phase["odd_prefix"])
            for target_label, eta in targets:
                if rho_t == eta:
                    continue
                e = v2_fraction(rho_t - eta)
                residue = lock_residue(rho_t, eta, e, odd_prefix, bits)
                alignment_class = (t + e) % source.depth
                key = (source.label, alignment_class, residue)
                counts[key] += 1
                if len(samples[key]) < sample_limit:
                    samples[key].append(
                        {
                            "target": target_label,
                            "source_phase_t": t,
                            "valuation_e": e,
                            "odd_prefix_a": odd_prefix,
                        }
                    )

    return counts, dict(samples)


def scan_hit_after_hit(
    *,
    sources: list[SourceInfo],
    lock_sets: dict[tuple[str, int, int], set[int]],
    bits: int,
    start_limit: int,
    odd_starts_only: bool,
    max_steps: int,
    witness_counts: Counter[tuple[str, int, int]],
    witness_samples: dict[tuple[str, int, int], list[dict[str, object]]],
) -> dict[str, object]:
    by_depth = make_depth_index(sources)
    raw_transitions: list[dict[str, object]] = []
    unique_edges: dict[tuple[object, ...], dict[str, object]] = {}
    starts_scanned = 0
    starts_reaching_one = 0
    source_visits = 0
    hit_visits = 0
    previous_hit_transitions = 0
    source_pair_hist: Counter[str] = Counter()
    bridge_word_hist: Counter[str] = Counter()
    next_state_hist: Counter[int] = Counter()
    previous_state_hist: Counter[int] = Counter()

    for start in start_values(start_limit, odd_starts_only):
        starts_scanned += 1
        n = start
        seen: set[int] = set()
        previous_visit: Visit | None = None

        for step in range(max_steps + 1):
            if n in seen:
                break
            seen.add(n)
            source = deepest_source_match(n, by_depth)
            if source is not None:
                visit = visit_for_state(n, step, source, lock_sets, [bits])
                source_visits += 1
                if visit.hit_by_bits[bits]:
                    hit_visits += 1

                if previous_visit is not None and previous_visit.hit_by_bits[bits]:
                    previous_hit_transitions += 1
                    if visit.hit_by_bits[bits]:
                        bridge = bridge_between(previous_visit, visit)
                        pair = f"{previous_visit.source.label}->{visit.source.label}"
                        source_pair_hist[pair] += 1
                        bridge_word_hist[str(bridge["parity_word_01"])] += 1
                        previous_state_hist[previous_visit.n] += 1
                        next_state_hist[visit.n] += 1

                        prev_serial = serialize_visit(
                            previous_visit, bits, witness_counts, witness_samples
                        )
                        next_serial = serialize_visit(
                            visit, bits, witness_counts, witness_samples
                        )
                        prev_targets = set(prev_serial["witness_targets_sample"])
                        next_targets = set(next_serial["witness_targets_sample"])
                        raw = {
                            "start": start,
                            "previous": prev_serial,
                            "next": next_serial,
                            "bridge": bridge,
                            "shared_witness_targets_in_samples": sorted(prev_targets & next_targets),
                        }
                        raw_transitions.append(raw)

                        sig = transition_signature(previous_visit, visit, bits, bridge)
                        if sig not in unique_edges:
                            unique_edges[sig] = {
                                "start_count": 0,
                                "starts": [],
                                "previous": prev_serial,
                                "next": next_serial,
                                "bridge": bridge,
                                "shared_witness_targets_in_samples": sorted(prev_targets & next_targets),
                            }
                        unique_edges[sig]["start_count"] = int(unique_edges[sig]["start_count"]) + 1
                        if len(unique_edges[sig]["starts"]) < 24:
                            unique_edges[sig]["starts"].append(start)

                previous_visit = visit

            if n == 1:
                starts_reaching_one += 1
                break
            n = shortcut_step(n)

    unique_list = sorted(
        unique_edges.values(),
        key=lambda item: (-int(item["start_count"]), int(item["next"]["n"])),
    )
    return {
        "starts_scanned": starts_scanned,
        "starts_reaching_one_within_cap": starts_reaching_one,
        "canonical_source_visits": source_visits,
        "R_bit_hit_visits": hit_visits,
        "previous_hit_transitions": previous_hit_transitions,
        "hit_after_hit_raw_transition_count": len(raw_transitions),
        "hit_after_hit_unique_edge_count": len(unique_list),
        "dedupe_ratio_raw_per_unique": round_float(
            len(raw_transitions) / len(unique_list) if unique_list else 0.0
        ),
        "source_pair_histogram": as_counter_dict(source_pair_hist),
        "bridge_word_histogram": as_counter_dict(bridge_word_hist),
        "previous_state_histogram": as_counter_dict(previous_state_hist),
        "next_state_histogram": as_counter_dict(next_state_hist),
        "unique_edges": unique_list,
        "raw_transitions": raw_transitions[:48],
    }


def check_row(name: str, passed: bool, detail: object) -> dict[str, object]:
    return {"name": name, "passed": bool(passed), "detail": detail}


def build_checks(args: argparse.Namespace, scan: dict[str, object]) -> list[dict[str, object]]:
    checks = [
        check_row(
            "all_scanned_positive_starts_reach_one_within_cap",
            scan["starts_scanned"] == scan["starts_reaching_one_within_cap"],
            {
                "starts_scanned": scan["starts_scanned"],
                "starts_reaching_one_within_cap": scan["starts_reaching_one_within_cap"],
            },
        ),
        check_row(
            "unique_edges_not_more_than_raw_transitions",
            scan["hit_after_hit_unique_edge_count"] <= scan["hit_after_hit_raw_transition_count"],
            {
                "raw": scan["hit_after_hit_raw_transition_count"],
                "unique": scan["hit_after_hit_unique_edge_count"],
            },
        ),
        check_row(
            "unique_edges_have_no_shared_sampled_targets",
            all(not edge["shared_witness_targets_in_samples"] for edge in scan["unique_edges"]),
            {
                "unique_edge_count": scan["hit_after_hit_unique_edge_count"],
                "shared_target_edge_count": sum(
                    1 for edge in scan["unique_edges"] if edge["shared_witness_targets_in_samples"]
                ),
            },
        ),
    ]
    if args.bits == 16 and args.start_limit == 50000:
        checks.append(
            check_row(
                "r16_n50000_collapses_to_one_state_edge",
                scan["hit_after_hit_raw_transition_count"] == 12
                and scan["hit_after_hit_unique_edge_count"] == 1,
                {
                    "raw": scan["hit_after_hit_raw_transition_count"],
                    "unique": scan["hit_after_hit_unique_edge_count"],
                    "source_pair_histogram": scan["source_pair_histogram"],
                    "bridge_word_histogram": scan["bridge_word_histogram"],
                },
            )
        )
    if args.bits >= 20:
        checks.append(
            check_row(
                "r_ge_20_has_no_hit_after_hit_transitions_in_current_window",
                scan["hit_after_hit_raw_transition_count"] == 0
                and scan["hit_after_hit_unique_edge_count"] == 0,
                {
                    "bits": args.bits,
                    "raw": scan["hit_after_hit_raw_transition_count"],
                    "unique": scan["hit_after_hit_unique_edge_count"],
                    "R_bit_hit_visits": scan["R_bit_hit_visits"],
                },
            )
        )
    return checks


def run(args: argparse.Namespace) -> dict[str, object]:
    started = perf_counter()
    sources = make_sources(args.max_depth, args.min_source_depth)
    targets = make_targets(sources)
    _meta, lock_sets = build_lock_sets(
        [source.word for source in sources],
        targets,
        [args.bits],
    )
    witness_counts, witness_samples = build_witness_maps(
        sources,
        targets,
        args.bits,
        args.witness_sample_limit,
    )
    scan = scan_hit_after_hit(
        sources=sources,
        lock_sets=lock_sets,
        bits=args.bits,
        start_limit=args.start_limit,
        odd_starts_only=args.odd_starts_only,
        max_steps=args.max_steps,
        witness_counts=witness_counts,
        witness_samples=witness_samples,
    )
    checks = build_checks(args, scan)
    return {
        "status": "odd-unit-lock-transition-witness-microscope",
        "result": "finite measurement only; not a proof of Collatz",
        "elapsed_seconds": round_float(perf_counter() - started, 6),
        "all_checks_passed": all(row["passed"] for row in checks),
        "checks": checks,
        "parameters": {
            "max_depth": args.max_depth,
            "min_source_depth": args.min_source_depth,
            "bits": args.bits,
            "start_limit": args.start_limit,
            "odd_starts_only": args.odd_starts_only,
            "max_steps": args.max_steps,
            "witness_sample_limit": args.witness_sample_limit,
        },
        "library": {
            "canonical_primitive_sources": len(sources),
            "unique_target_spines": len(targets),
            "source_depths": sorted({source.depth for source in sources}),
        },
        "scan": scan,
        "interpretation": (
            "Raw hit-after-hit counts can be misleading because positive Collatz "
            "orbits merge. Unique edge counts reveal whether the rare chained "
            "locks are many mechanisms or one shared orbit bridge."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-depth", type=int, default=13)
    parser.add_argument("--min-source-depth", type=int, default=3)
    parser.add_argument("--bits", type=int, default=16)
    parser.add_argument("--start-limit", type=int, default=50000)
    parser.add_argument("--max-steps", type=int, default=512)
    parser.add_argument("--odd-starts-only", action=argparse.BooleanOptionalAction, default=True)
    parser.add_argument("--witness-sample-limit", type=int, default=24)
    parser.add_argument(
        "--output",
        type=Path,
        default=SCRIPT_DIR / "results" / "odd_unit_lock_transition_witness_microscope_R16_N50000_20260705.json",
    )
    parser.add_argument("--quiet", action="store_true")
    args = parser.parse_args()

    if args.max_depth < 1:
        raise SystemExit("--max-depth must be positive")
    if args.min_source_depth < 1:
        raise SystemExit("--min-source-depth must be positive")
    if args.bits < 2:
        raise SystemExit("--bits must be >= 2")
    if args.start_limit < 2:
        raise SystemExit("--start-limit must be >= 2")
    if args.max_steps < 1:
        raise SystemExit("--max-steps must be positive")
    if args.witness_sample_limit < 1:
        raise SystemExit("--witness-sample-limit must be positive")

    result = run(args)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    if not args.quiet:
        print(f"wrote {args.output}")
        scan = result["scan"]
        print(
            "raw={raw} unique={unique} previous_hit_transitions={prev}".format(
                raw=scan["hit_after_hit_raw_transition_count"],
                unique=scan["hit_after_hit_unique_edge_count"],
                prev=scan["previous_hit_transitions"],
            )
        )
        for edge in scan["unique_edges"][:8]:
            print(
                "edge starts={count}: {prev_n}->{next_n} {prev_source}->{next_source} bridge={bridge}".format(
                    count=edge["start_count"],
                    prev_n=edge["previous"]["n"],
                    next_n=edge["next"]["n"],
                    prev_source=edge["previous"]["source"],
                    next_source=edge["next"]["source"],
                    bridge=edge["bridge"]["parity_word_EO"],
                )
            )
        print(f"checks_passed={result['all_checks_passed']}")
    if not result["all_checks_passed"]:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

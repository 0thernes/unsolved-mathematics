#!/usr/bin/env python3
"""Target-tail lab for odd-unit lock valuations.

The exact-height odd-unit lock lab exposed the next proof obligation: control
target spines with large e = v2(rho_t - eta).  This script measures that tail
for finite supercritical source and target libraries.

Finite measurement only; the Collatz conjecture remains open.
"""

from __future__ import annotations

import argparse
import heapq
import json
import sys
from collections import Counter
from fractions import Fraction
from pathlib import Path
from statistics import mean
from time import perf_counter

sys.path.insert(0, str(Path(__file__).resolve().parent))

from odd_unit_lock_coverage_lab import (
    enumerate_supercritical_cycles,
    phase_data,
    primitive_period,
    spine,
    v2_fraction,
    word_string,
)

SCRIPT_DIR = Path(__file__).resolve().parent


def parse_int_list(raw: str) -> list[int]:
    values = sorted({int(part.strip()) for part in raw.split(",") if part.strip()})
    if not values:
        raise argparse.ArgumentTypeError("expected comma-separated integers")
    return values


def primitive_cycles_between(
    cycles: list[tuple[int, ...]], min_depth: int, max_depth: int
) -> list[tuple[int, ...]]:
    return [
        w
        for w in cycles
        if min_depth <= len(w) <= max_depth and primitive_period(w) == len(w)
    ]


def unique_targets(cycles: list[tuple[int, ...]]) -> list[dict[str, object]]:
    by_spine: dict[Fraction, tuple[str, int]] = {}
    for w in cycles:
        label = word_string(w)
        eta = spine(w)
        previous = by_spine.get(eta)
        if previous is None or (len(label), label) < (previous[1], previous[0]):
            by_spine[eta] = (label, len(w))
    return [
        {"label": label, "depth": depth, "eta": eta}
        for eta, (label, depth) in sorted(
            by_spine.items(), key=lambda item: (item[1][1], item[1][0])
        )
    ]


def source_phases(sources: list[tuple[int, ...]]) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for source in sources:
        label = word_string(source)
        for phase in phase_data(source):
            phase_t = int(phase["t"])
            rows.append(
                {
                    "source": label,
                    "source_depth": len(source),
                    "phase_t": phase_t,
                    "phase_word": label[phase_t:] + label[:phase_t],
                    "rho_t": phase["rho"],
                }
            )
    return rows


def periodic_prefix_len(source_phase_word: str, target_word: str) -> int:
    for index, bit in enumerate(target_word):
        if bit != source_phase_word[index % len(source_phase_word)]:
            return index
    return len(target_word)


def tail_summary(
    phases: list[dict[str, object]],
    targets: list[dict[str, object]],
    thresholds: list[int],
    top_n: int,
) -> dict[str, object]:
    histogram: Counter[int] = Counter()
    tail_counts = {threshold: 0 for threshold in thresholds}
    tail_digests = {
        threshold: {
            "by_source_depth": Counter(),
            "by_target_depth": Counter(),
            "by_phase_t": Counter(),
            "periodic_prefix_ge_75pct": 0,
            "periodic_prefix_ge_90pct": 0,
            "samples": [],
        }
        for threshold in thresholds
    }
    top_heap: list[tuple[int, int, dict[str, object]]] = []
    pair_count = 0
    zero_separation_skips = 0
    e_values: list[int] = []
    serial = 0

    for phase in phases:
        rho_t = phase["rho_t"]
        assert isinstance(rho_t, Fraction)
        for target in targets:
            eta = target["eta"]
            assert isinstance(eta, Fraction)
            if rho_t == eta:
                zero_separation_skips += 1
                continue
            e = v2_fraction(rho_t - eta)
            pair_count += 1
            e_values.append(e)
            histogram[e] += 1
            phase_word = str(phase["phase_word"])
            target_label = str(target["label"])
            periodic_prefix = periodic_prefix_len(phase_word, target_label)
            periodic_prefix_fraction = periodic_prefix / len(target_label)
            witness = {
                "valuation_e": e,
                "source": phase["source"],
                "source_depth": phase["source_depth"],
                "phase_t": phase["phase_t"],
                "phase_word": phase_word,
                "target": target_label,
                "target_depth": target["depth"],
                "periodic_prefix_len": periodic_prefix,
                "periodic_prefix_fraction": round(periodic_prefix_fraction, 6),
            }
            for threshold in thresholds:
                if e >= threshold:
                    tail_counts[threshold] += 1
                    digest = tail_digests[threshold]
                    digest["by_source_depth"][int(phase["source_depth"])] += 1
                    digest["by_target_depth"][int(target["depth"])] += 1
                    digest["by_phase_t"][int(phase["phase_t"])] += 1
                    if periodic_prefix_fraction >= 0.75:
                        digest["periodic_prefix_ge_75pct"] += 1
                    if periodic_prefix_fraction >= 0.90:
                        digest["periodic_prefix_ge_90pct"] += 1
                    if len(digest["samples"]) < top_n:
                        digest["samples"].append(witness)
            if top_n > 0:
                serial += 1
                item = (e, serial, witness)
                if len(top_heap) < top_n:
                    heapq.heappush(top_heap, item)
                elif item[0] > top_heap[0][0]:
                    heapq.heapreplace(top_heap, item)

    tail_rows = []
    for threshold in thresholds:
        count = tail_counts[threshold]
        expected = pair_count / (1 << threshold) if threshold >= 0 else None
        ratio = count / expected if expected else None
        tail_rows.append(
            {
                "threshold_e_ge": threshold,
                "count": count,
                "fraction": round(count / pair_count, 15) if pair_count else 0.0,
                "geometric_expected_count": round(expected, 6) if expected is not None else None,
                "observed_over_geometric": round(ratio, 6) if ratio is not None else None,
                "digest": {
                    "by_source_depth": dict(
                        sorted(
                            (str(k), v)
                            for k, v in tail_digests[threshold]["by_source_depth"].items()
                        )
                    ),
                    "by_target_depth": dict(
                        sorted(
                            (str(k), v)
                            for k, v in tail_digests[threshold]["by_target_depth"].items()
                        )
                    ),
                    "by_phase_t": dict(
                        sorted(
                            (str(k), v)
                            for k, v in tail_digests[threshold]["by_phase_t"].items()
                        )
                    ),
                    "periodic_prefix_ge_75pct": tail_digests[threshold][
                        "periodic_prefix_ge_75pct"
                    ],
                    "periodic_prefix_ge_90pct": tail_digests[threshold][
                        "periodic_prefix_ge_90pct"
                    ],
                    "samples": tail_digests[threshold]["samples"],
                },
            }
        )

    top_witnesses = [item[2] for item in sorted(top_heap, key=lambda item: (-item[0], item[1]))]
    return {
        "target_spines": len(targets),
        "source_phase_target_pairs": pair_count,
        "zero_separation_skips": zero_separation_skips,
        "max_valuation_e": max(e_values, default=None),
        "avg_valuation_e": round(mean(e_values), 9) if e_values else 0.0,
        "valuation_histogram": dict(sorted((str(k), v) for k, v in histogram.items())),
        "tail_comparison": tail_rows,
        "top_witnesses": top_witnesses,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-max-depth", type=int, default=10)
    parser.add_argument("--source-min-depth", type=int, default=3)
    parser.add_argument("--target-max-depth", type=int, default=20)
    parser.add_argument("--target-min-depth", type=int, default=1)
    parser.add_argument("--target-cutoffs", type=parse_int_list, default=parse_int_list("12,14,16,18,20"))
    parser.add_argument("--thresholds", type=parse_int_list, default=parse_int_list("8,10,12,14,16,18,20,22,24"))
    parser.add_argument("--top-witnesses", type=int, default=16)
    parser.add_argument(
        "--output",
        type=Path,
        default=SCRIPT_DIR / "results" / "odd_unit_lock_target_tail_s10_t20_20260705.json",
    )
    args = parser.parse_args()

    if args.target_max_depth < max(args.target_cutoffs):
        parser.error("--target-max-depth must be at least the largest cutoff")

    start = perf_counter()
    cycles = enumerate_supercritical_cycles(max(args.source_max_depth, args.target_max_depth))
    sources = primitive_cycles_between(cycles, args.source_min_depth, args.source_max_depth)
    targets_all = unique_targets(
        primitive_cycles_between(cycles, args.target_min_depth, args.target_max_depth)
    )
    phases = source_phases(sources)

    by_cutoff = {}
    for cutoff in args.target_cutoffs:
        targets = [target for target in targets_all if int(target["depth"]) <= cutoff]
        by_cutoff[str(cutoff)] = tail_summary(
            phases, targets, args.thresholds, args.top_witnesses
        )

    result = {
        "status": "finite measurement only; not a proof of Collatz",
        "parameters": {
            "source_min_depth": args.source_min_depth,
            "source_max_depth": args.source_max_depth,
            "target_min_depth": args.target_min_depth,
            "target_max_depth": args.target_max_depth,
            "target_cutoffs": args.target_cutoffs,
            "thresholds": args.thresholds,
        },
        "cycle_counts": {
            "primitive_source_cycles": len(sources),
            "source_phases": len(phases),
            "unique_target_spines_total": len(targets_all),
        },
        "by_target_cutoff": by_cutoff,
        "runtime_seconds": round(perf_counter() - start, 6),
    }

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    print(f"wrote {args.output}")
    print(json.dumps(result["cycle_counts"], indent=2, sort_keys=True))
    for cutoff in args.target_cutoffs:
        row = by_cutoff[str(cutoff)]
        tail_by_threshold = {
            item["threshold_e_ge"]: item for item in row["tail_comparison"]
        }
        def fmt(threshold: int) -> str:
            item = tail_by_threshold.get(threshold)
            if not item:
                return "n/a"
            return f"{item['count']} ({item['observed_over_geometric']}x geom)"

        print(
            "target<= {cutoff}: targets={targets} max_e={max_e} "
            "tail>=12={tail12} tail>=16={tail16} tail>=20={tail20}".format(
                cutoff=cutoff,
                targets=row["target_spines"],
                max_e=row["max_valuation_e"],
                tail12=fmt(12),
                tail16=fmt(16),
                tail20=fmt(20),
            )
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

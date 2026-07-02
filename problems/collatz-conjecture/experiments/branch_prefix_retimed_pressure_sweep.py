#!/usr/bin/env python3
"""Depth sweep for retimed-pressure lift transitions.

This wraps ``branch_prefix_retimed_pressure.py`` and keeps only the fields that
matter for the proposed local lemma:

* retimed-pressure transitions have no prefix trace deficit;
* the first above-parent threshold is a one-unit required-credit increase;
* the threshold is prepaid by a visible high-ladder or low-repeat event.

The output is finite evidence, not a proof of Collatz.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from types import SimpleNamespace
from typing import Any

from branch_prefix_retimed_pressure import run as run_retimed_pressure


def load_or_run(args: argparse.Namespace, parent_depth: int) -> tuple[dict[str, Any], bool]:
    child_depth = parent_depth + 1
    cache_path = args.cache_template.format(parent_depth=parent_depth, child_depth=child_depth)
    cache = Path(cache_path)
    if args.use_cache and cache.exists() and not args.refresh:
        return json.loads(cache.read_text(encoding="utf-8")), True

    payload = run_retimed_pressure(
        SimpleNamespace(
            parent_depth=parent_depth,
            max_depth=max(args.max_depth, child_depth),
            max_steps=args.max_steps,
            max_pressure_events=args.max_pressure_events,
            top_n=args.top_n,
            output=None,
            quiet=True,
        )
    )
    if args.write_depth_cache:
        cache.parent.mkdir(parents=True, exist_ok=True)
        cache.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return payload, False


def all_thresholds_one_unit(histogram: dict[str, int], retimed_count: int) -> bool:
    if retimed_count == 0:
        return True
    return histogram == {"1": retimed_count}


def all_thresholds_prepaid(timing_counts: dict[str, int], retimed_count: int) -> bool:
    if retimed_count == 0:
        return True
    prepaid = int(timing_counts.get("prior_high_ladder", 0)) + int(timing_counts.get("prior_low_repeat", 0))
    return prepaid == retimed_count


def compact_depth(payload: dict[str, Any], cached: bool) -> dict[str, Any]:
    retimed_count = int(payload["retimed_pressure_count"])
    required_hist = {str(k): int(v) for k, v in dict(payload["threshold_required_above_parent_histogram"]).items()}
    timing_counts = {str(k): int(v) for k, v in dict(payload["timing_class_counts"]).items()}
    frontiers = dict(payload["frontiers"])
    parent = dict(frontiers["parent"])
    child = dict(frontiers["child"])
    return {
        "parent_depth": int(parent["depth"]),
        "child_depth": int(child["depth"]),
        "cached": cached,
        "parent_live_count": int(parent["positive_live_count"]),
        "child_live_count": int(child["positive_live_count"]),
        "positive_pressure_transition_count": int(payload["positive_pressure_transition_count"]),
        "retimed_pressure_count": retimed_count,
        "retimed_failure_count": int(payload["retimed_failure_count"]),
        "max_trace_deficit": int(payload["max_trace_deficit"]),
        "min_threshold_margin": payload["min_threshold_margin"],
        "max_threshold_lag": payload["max_threshold_lag"],
        "threshold_required_above_parent_histogram": required_hist,
        "threshold_event_counts": payload["threshold_event_counts"],
        "timing_class_counts": timing_counts,
        "all_thresholds_one_unit": all_thresholds_one_unit(required_hist, retimed_count),
        "all_thresholds_prepaid": all_thresholds_prepaid(timing_counts, retimed_count),
    }


def run(args: argparse.Namespace) -> dict[str, Any]:
    depths = list(range(args.min_parent_depth, args.max_parent_depth + 1))
    rows = []
    for depth in depths:
        payload, cached = load_or_run(args, depth)
        rows.append(compact_depth(payload, cached))

    positive_rows = [row for row in rows if int(row["retimed_pressure_count"]) > 0]
    margins = [int(row["min_threshold_margin"]) for row in positive_rows if row["min_threshold_margin"] is not None]
    return {
        "status": "branch-prefix-retimed-pressure-depth-sweep",
        "parameters": {
            "min_parent_depth": args.min_parent_depth,
            "max_parent_depth": args.max_parent_depth,
            "max_depth": args.max_depth,
            "max_steps": args.max_steps,
            "max_pressure_events": args.max_pressure_events,
            "top_n": args.top_n,
            "use_cache": args.use_cache,
            "refresh": args.refresh,
            "write_depth_cache": args.write_depth_cache,
            "cache_template": args.cache_template,
        },
        "depths": rows,
        "checks": {
            "all_depths_trace_safe": all(
                int(row["retimed_failure_count"]) == 0 and int(row["max_trace_deficit"]) == 0 for row in rows
            ),
            "all_depths_one_unit_thresholds": all(bool(row["all_thresholds_one_unit"]) for row in rows),
            "all_depths_prepaid_thresholds": all(bool(row["all_thresholds_prepaid"]) for row in rows),
            "minimum_positive_threshold_margin": min(margins) if margins else None,
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--min-parent-depth", type=int, default=18)
    parser.add_argument("--max-parent-depth", type=int, default=25)
    parser.add_argument("--max-depth", type=int, default=1024)
    parser.add_argument("--max-steps", type=int, default=50000)
    parser.add_argument("--max-pressure-events", type=int, default=8)
    parser.add_argument("--top-n", type=int, default=3)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--cache-template", default="experiments/results/branch_prefix_retimed_pressure_d{parent_depth}_d{child_depth}_20260702.json")
    parser.add_argument("--use-cache", action="store_true")
    parser.add_argument("--refresh", action="store_true")
    parser.add_argument("--write-depth-cache", action="store_true")
    args = parser.parse_args()

    if args.min_parent_depth < 1:
        raise SystemExit("--min-parent-depth must be positive")
    if args.max_parent_depth < args.min_parent_depth:
        raise SystemExit("--max-parent-depth must be >= --min-parent-depth")
    if args.max_steps < 1:
        raise SystemExit("--max-steps must be positive")
    if args.max_pressure_events < 1:
        raise SystemExit("--max-pressure-events must be positive")
    if args.top_n < 1:
        raise SystemExit("--top-n must be positive")

    payload = run(args)
    text = json.dumps(payload, indent=2, sort_keys=True)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text + "\n", encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Depth sweep for retimed-pressure symbolic signatures.

This wraps ``branch_prefix_retimed_signature.py`` and keeps a compact ledger of
which theorem-facing features persist across exact frontier lifts.

The result is finite evidence only, not a proof of Collatz.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from types import SimpleNamespace
from typing import Any

from branch_prefix_retimed_signature import run as run_signature


def load_or_run(args: argparse.Namespace, parent_depth: int) -> tuple[dict[str, Any], bool]:
    child_depth = parent_depth + 1
    cache_path = args.cache_template.format(parent_depth=parent_depth, child_depth=child_depth)
    cache = Path(cache_path)
    if args.use_cache and cache.exists() and not args.refresh:
        return json.loads(cache.read_text(encoding="utf-8")), True

    payload = run_signature(
        SimpleNamespace(
            parent_depth=parent_depth,
            max_depth=max(args.max_depth, child_depth),
            max_steps=args.max_steps,
            top_n=args.top_n,
            residue_top_n=args.residue_top_n,
            residue_moduli=args.residue_moduli,
            output=None,
            quiet=True,
        )
    )
    if args.write_depth_cache:
        cache.parent.mkdir(parents=True, exist_ok=True)
        cache.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return payload, False


def high_ladder_lag_values(payload: dict[str, Any]) -> list[int]:
    values = []
    for key in dict(payload["lag_minus_align_by_kind"]):
        kind, raw_value = str(key).split(":", 1)
        if kind == "high_ladder":
            values.append(int(raw_value))
    return values


def post_tail_equals_plus_three(payload: dict[str, Any]) -> bool:
    regimes = dict(payload["pressure_regime_counts"])
    tail_count = int(regimes.get("high_after_ladder_window", 0))
    if tail_count == 0:
        return True
    lag_hist = dict(payload["lag_minus_align_by_kind"])
    return int(lag_hist.get("high_ladder:3", 0)) == tail_count


def no_pure_retimed_residue_buckets(payload: dict[str, Any]) -> bool:
    return all(
        int(summary["pure_retimed_buckets"]) == 0
        for summary in dict(payload["retimed_child_residue_purity"]).values()
    )


def compact_depth(payload: dict[str, Any], cached: bool) -> dict[str, Any]:
    frontiers = dict(payload["frontiers"])
    parent = dict(frontiers["parent"])
    child = dict(frontiers["child"])
    high_lags = high_ladder_lag_values(payload)
    residue_purity = dict(payload["retimed_child_residue_purity"])
    max_modulus = max(int(modulus) for modulus in residue_purity)
    max_modulus_summary = dict(residue_purity[str(max_modulus)])
    return {
        "parent_depth": int(parent["depth"]),
        "child_depth": int(child["depth"]),
        "cached": cached,
        "parent_live_count": int(parent["positive_live_count"]),
        "child_live_count": int(child["positive_live_count"]),
        "positive_pressure_transition_count": int(payload["positive_pressure_transition_count"]),
        "retimed_transition_count": int(payload["retimed_transition_count"]),
        "first_pressure_unit_count": int(payload["first_pressure_unit_count"]),
        "pressure_unit_count": int(payload["pressure_unit_count"]),
        "pure_feature_claims": payload["pure_feature_claims"],
        "pressure_regime_counts": payload["pressure_regime_counts"],
        "pressure_event_counts": payload["pressure_event_counts"],
        "last_credit_kind_counts": payload["last_credit_kind_counts"],
        "first_required_above_parent_histogram": payload["first_required_above_parent_histogram"],
        "required_above_parent_histogram": payload["required_above_parent_histogram"],
        "high_ladder_lag_minus_align_min": min(high_lags) if high_lags else None,
        "high_ladder_lag_minus_align_max": max(high_lags) if high_lags else None,
        "post_tail_equals_high_ladder_plus_three": post_tail_equals_plus_three(payload),
        "no_pure_retimed_residue_buckets": no_pure_retimed_residue_buckets(payload),
        "max_modulus_residue_purity": {
            "modulus": max_modulus,
            "occupied_buckets": int(max_modulus_summary["occupied_buckets"]),
            "retimed_buckets": int(max_modulus_summary["retimed_buckets"]),
            "pure_retimed_buckets": int(max_modulus_summary["pure_retimed_buckets"]),
            "mixed_buckets": int(max_modulus_summary["mixed_buckets"]),
            "retimed_pure_bucket_fraction": max_modulus_summary["retimed_pure_bucket_fraction"],
        },
    }


def run(args: argparse.Namespace) -> dict[str, Any]:
    rows = []
    for depth in range(args.min_parent_depth, args.max_parent_depth + 1):
        payload, cached = load_or_run(args, depth)
        rows.append(compact_depth(payload, cached))

    pure_claim_names = sorted(
        {
            claim
            for row in rows
            for claim in dict(row["pure_feature_claims"])
        }
    )
    pure_claim_checks = {
        claim: all(bool(dict(row["pure_feature_claims"]).get(claim, False)) for row in rows)
        for claim in pure_claim_names
    }

    return {
        "status": "branch-prefix-retimed-signature-depth-sweep",
        "parameters": {
            "min_parent_depth": args.min_parent_depth,
            "max_parent_depth": args.max_parent_depth,
            "max_depth": args.max_depth,
            "max_steps": args.max_steps,
            "top_n": args.top_n,
            "residue_top_n": args.residue_top_n,
            "residue_moduli": args.residue_moduli,
            "use_cache": args.use_cache,
            "refresh": args.refresh,
            "write_depth_cache": args.write_depth_cache,
            "cache_template": args.cache_template,
        },
        "depths": rows,
        "checks": {
            "pure_feature_claims_all_depths": pure_claim_checks,
            "all_depths_post_tail_equals_high_ladder_plus_three": all(
                bool(row["post_tail_equals_high_ladder_plus_three"]) for row in rows
            ),
            "all_depths_no_pure_retimed_residue_buckets": all(
                bool(row["no_pure_retimed_residue_buckets"]) for row in rows
            ),
            "total_retimed_transitions": sum(int(row["retimed_transition_count"]) for row in rows),
            "total_pressure_units": sum(int(row["pressure_unit_count"]) for row in rows),
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--min-parent-depth", type=int, default=18)
    parser.add_argument("--max-parent-depth", type=int, default=25)
    parser.add_argument("--max-depth", type=int, default=1024)
    parser.add_argument("--max-steps", type=int, default=50000)
    parser.add_argument("--top-n", type=int, default=3)
    parser.add_argument("--residue-top-n", type=int, default=8)
    parser.add_argument("--residue-moduli", nargs="*", default=["16", "64", "256", "1024", "4096", "65536"])
    parser.add_argument(
        "--cache-template",
        default="experiments/results/branch_prefix_retimed_signature_d{parent_depth}_d{child_depth}_20260702.json",
    )
    parser.add_argument("--use-cache", action="store_true")
    parser.add_argument("--refresh", action="store_true")
    parser.add_argument("--write-depth-cache", action="store_true")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    if args.min_parent_depth < 1:
        raise SystemExit("--min-parent-depth must be positive")
    if args.max_parent_depth < args.min_parent_depth:
        raise SystemExit("--max-parent-depth must be >= --min-parent-depth")
    if args.max_steps < 1:
        raise SystemExit("--max-steps must be positive")
    if args.top_n < 1:
        raise SystemExit("--top-n must be positive")
    if args.residue_top_n < 1:
        raise SystemExit("--residue-top-n must be positive")

    payload = run(args)
    text = json.dumps(payload, indent=2, sort_keys=True)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text + "\n", encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()

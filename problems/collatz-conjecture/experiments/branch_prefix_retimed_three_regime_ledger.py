#!/usr/bin/env python3
"""Combine the three retimed pressure-regime certificates into one ledger.

The active high-ladder, post-ladder, and low-repeat analyzers each verify one
dynamic regime.  This script checks that their results cover every
above-parent pressure unit and extracts the shared event-index/layer law.

The output is finite theorem-discovery data, not a proof of Collatz.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path
from typing import Any


DEFAULT_ACTIVE = Path(
    "experiments/results/branch_prefix_retimed_active_ladder_units_sweep_d18_d25_20260702.json"
)
DEFAULT_POST = Path(
    "experiments/results/branch_prefix_retimed_post_ladder_all_units_sweep_d18_d25_20260702.json"
)
DEFAULT_LOW = Path(
    "experiments/results/branch_prefix_retimed_low_repeat_units_sweep_d18_d25_20260702.json"
)
DEFAULT_SIGNATURE = Path(
    "experiments/results/branch_prefix_retimed_signature_sweep_d18_d25_20260702.json"
)


REGIMES = {
    "active_high_ladder": {
        "source_key": "active",
        "unit_key": "active_ladder_pressure_unit_count",
        "total_key": "total_active_ladder_pressure_units",
        "signature_key": "high_inside_active_ladder",
    },
    "post_ladder": {
        "source_key": "post",
        "unit_key": "post_ladder_pressure_unit_count",
        "total_key": "total_post_ladder_pressure_units",
        "signature_key": "high_after_ladder_window",
    },
    "low_repeat": {
        "source_key": "low",
        "unit_key": "low_repeat_pressure_unit_count",
        "total_key": "total_low_repeat_pressure_units",
        "signature_key": "low_repeat_prepaid",
    },
}


def read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def counter_from_dict(raw: dict[str, Any]) -> Counter[str]:
    return Counter({str(key): int(value) for key, value in raw.items()})


def sorted_counter(counter: Counter[str]) -> dict[str, int]:
    def key_fn(item: tuple[str, int]) -> tuple[int, str]:
        key, _ = item
        try:
            return (int(key), key)
        except ValueError:
            return (10**9, key)

    return {key: int(value) for key, value in sorted(counter.items(), key=key_fn)}


def all_claims_true(payload: dict[str, Any]) -> bool:
    claims = dict(payload["checks"].get("pure_feature_claims_all_depths", {}))
    return bool(claims) and all(bool(value) for value in claims.values())


def diagonal_count(counter: dict[str, Any]) -> int:
    total = 0
    for key, value in counter.items():
        left, right = str(key).split(":", 1)
        if left == right:
            total += int(value)
    return total


def non_diagonal(counter: dict[str, Any]) -> dict[str, int]:
    bad = {}
    for key, value in counter.items():
        left, right = str(key).split(":", 1)
        if left != right:
            bad[str(key)] = int(value)
    return bad


def merge_event_index_counts(*payloads: dict[str, Any]) -> Counter[str]:
    merged: Counter[str] = Counter()
    for payload in payloads:
        merged.update(counter_from_dict(dict(payload["checks"]["event_index_counts"])))
    return merged


def merge_event_index_required_counts(*payloads: dict[str, Any]) -> Counter[str]:
    merged: Counter[str] = Counter()
    for payload in payloads:
        merged.update(counter_from_dict(dict(payload["checks"]["event_index_required_above_parent_counts"])))
    return merged


def regime_layer_matrix(payloads: dict[str, dict[str, Any]]) -> dict[str, dict[str, int]]:
    matrix: dict[str, dict[str, int]] = {}
    for regime, spec in REGIMES.items():
        payload = payloads[str(spec["source_key"])]
        matrix[regime] = sorted_counter(counter_from_dict(dict(payload["checks"]["event_index_counts"])))
    return matrix


def depth_lookup(payload: dict[str, Any]) -> dict[int, dict[str, Any]]:
    return {int(row["parent_depth"]): row for row in payload["depths"]}


def depth_rows(payloads: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    active_rows = depth_lookup(payloads["active"])
    post_rows = depth_lookup(payloads["post"])
    low_rows = depth_lookup(payloads["low"])
    rows = []
    for depth in sorted(active_rows):
        active = active_rows[depth]
        post = post_rows[depth]
        low = low_rows[depth]
        retimed = int(active["retimed_transition_count"])
        pressure = int(active["above_parent_pressure_unit_count"])
        regime_counts = {
            "active_high_ladder": int(active["active_ladder_pressure_unit_count"]),
            "post_ladder": int(post["post_ladder_pressure_unit_count"]),
            "low_repeat": int(low["low_repeat_pressure_unit_count"]),
        }
        layer_counts = Counter()
        for source_row in (active, post, low):
            layer_counts.update(counter_from_dict(dict(source_row["event_index_counts"])))
        first_layer = int(layer_counts.get("1", 0))
        rows.append(
            {
                "parent_depth": depth,
                "child_depth": int(active["child_depth"]),
                "retimed_transition_count": retimed,
                "above_parent_pressure_unit_count": pressure,
                "regime_counts": regime_counts,
                "regime_sum": sum(regime_counts.values()),
                "regime_sum_matches_pressure_units": sum(regime_counts.values()) == pressure,
                "layer_counts": sorted_counter(layer_counts),
                "layer_sum": sum(layer_counts.values()),
                "layer_sum_matches_pressure_units": sum(layer_counts.values()) == pressure,
                "first_layer_count": first_layer,
                "first_layer_equals_retimed_transitions": first_layer == retimed,
            }
        )
    return rows


def run(args: argparse.Namespace) -> dict[str, Any]:
    payloads = {
        "active": read_json(args.active),
        "post": read_json(args.post),
        "low": read_json(args.low),
        "signature": read_json(args.signature),
    }

    active = payloads["active"]
    post = payloads["post"]
    low = payloads["low"]
    signature = payloads["signature"]
    regime_counts = {
        regime: int(payloads[str(spec["source_key"])]["checks"][str(spec["total_key"])])
        for regime, spec in REGIMES.items()
    }
    layer_counts = merge_event_index_counts(active, post, low)
    layer_required_counts = merge_event_index_required_counts(active, post, low)
    rows = depth_rows(payloads)

    total_retimed_values = {
        name: int(payload["checks"]["total_retimed_transitions"])
        for name, payload in payloads.items()
    }
    pressure_total_values = {
        "active": int(active["checks"]["total_above_parent_pressure_units"]),
        "post": int(post["checks"]["total_above_parent_pressure_units"]),
        "low": int(low["checks"]["total_above_parent_pressure_units"]),
        "signature": int(signature["checks"]["total_pressure_units"]),
    }
    pressure_total = int(active["checks"]["total_above_parent_pressure_units"])
    retimed_total = int(active["checks"]["total_retimed_transitions"])
    signature_regimes = dict(active["checks"]["pressure_regime_counts"])
    expected_signature_regimes = {
        str(spec["signature_key"]): regime_counts[regime]
        for regime, spec in REGIMES.items()
    }
    non_diagonal_layers = non_diagonal(dict(layer_required_counts))

    return {
        "status": "branch-prefix-retimed-three-regime-ledger",
        "source_files": {
            "active": str(args.active),
            "post": str(args.post),
            "low": str(args.low),
            "signature": str(args.signature),
        },
        "source_statuses": {name: payload["status"] for name, payload in payloads.items()},
        "totals": {
            "retimed_transition_count": retimed_total,
            "above_parent_pressure_unit_count": pressure_total,
            "regime_counts": regime_counts,
            "regime_sum": sum(regime_counts.values()),
            "layer_counts": sorted_counter(layer_counts),
            "layer_sum": sum(layer_counts.values()),
            "regime_layer_matrix": regime_layer_matrix(payloads),
            "event_index_required_above_parent_counts": sorted_counter(layer_required_counts),
        },
        "checks": {
            "all_sources_agree_on_retimed_transition_count": len(set(total_retimed_values.values())) == 1,
            "all_sources_agree_on_pressure_unit_count": len(set(pressure_total_values.values())) == 1,
            "regime_sum_matches_pressure_units": sum(regime_counts.values()) == pressure_total,
            "layer_sum_matches_pressure_units": sum(layer_counts.values()) == pressure_total,
            "first_layer_equals_retimed_transitions": int(layer_counts.get("1", 0)) == retimed_total,
            "all_event_index_required_pairs_are_diagonal": not non_diagonal_layers,
            "diagonal_event_index_required_count": diagonal_count(dict(layer_required_counts)),
            "signature_regime_counts_match_component_totals": signature_regimes == expected_signature_regimes,
            "all_component_algebra_claims_true": all(
                all_claims_true(payloads[name]) for name in ("active", "post", "low")
            ),
            "signature_dynamic_claims_true": all_claims_true(signature),
            "all_depths_regime_sum_matches_pressure_units": all(
                bool(row["regime_sum_matches_pressure_units"]) for row in rows
            ),
            "all_depths_layer_sum_matches_pressure_units": all(
                bool(row["layer_sum_matches_pressure_units"]) for row in rows
            ),
            "all_depths_first_layer_equals_retimed_transitions": all(
                bool(row["first_layer_equals_retimed_transitions"]) for row in rows
            ),
            "non_diagonal_event_index_required_pairs": non_diagonal_layers,
            "retimed_transition_counts_by_source": total_retimed_values,
            "pressure_unit_counts_by_source": pressure_total_values,
        },
        "depths": rows,
        "theorem_target": {
            "informal": (
                "Every retimed above-parent pressure unit lies in exactly one dynamic regime; "
                "its event index equals its required-credit level above the parent; and layer 1 "
                "appears exactly once per retimed transition."
            ),
            "regime_formulas": {
                "active_high_ladder": "x=2^a q-1, state=3^k 2^(a-k) q-1, word O^k",
                "post_ladder": "y=3^a q-1, y==6 mod 16, state=EOO(y)=(9y+10)/8",
                "low_repeat": "x==-5 mod 64, state is OO(x) or OOEOO(x)",
            },
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--active", type=Path, default=DEFAULT_ACTIVE)
    parser.add_argument("--post", type=Path, default=DEFAULT_POST)
    parser.add_argument("--low", type=Path, default=DEFAULT_LOW)
    parser.add_argument("--signature", type=Path, default=DEFAULT_SIGNATURE)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    payload = run(args)
    text = json.dumps(payload, indent=2, sort_keys=True)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text + "\n", encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Scan positive integers for their first usable descent-certificate depth.

This complements collatz_survivor_dp.py.  The DP counts persistent 2-adic
boundary shadows; this scanner asks how quickly ordinary positive integers
escape those shadows and acquire a usable residue certificate.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter
from time import perf_counter

from collatz_residue_lab import affine_for_low_bits, descent_threshold, shortcut


def certificate_for_start(start: int, max_depth: int, pow3: list[int]) -> dict[str, int | bool | None]:
    if start == 1:
        return {
            "certified": True,
            "depth": 0,
            "residue": 1,
            "quotient": 0,
            "odd_count": 0,
            "image": 1,
            "q_threshold": 0,
            "shortcut_steps_until_below_start": 0,
            "trivial_cycle_entry": True,
        }

    for depth in range(1, max_depth + 1):
        residue = start & ((1 << depth) - 1)
        quotient = start >> depth
        cert = descent_threshold(depth, residue, pow3)
        if cert is None:
            continue
        odd_count, image, threshold = cert
        if quotient >= threshold:
            return {
                "certified": True,
                "depth": depth,
                "residue": residue,
                "quotient": quotient,
                "odd_count": odd_count,
                "image": image,
                "q_threshold": threshold,
                "shortcut_steps_until_below_start": depth,
                "trivial_cycle_entry": False,
            }

    return {
        "certified": False,
        "depth": None,
        "residue": start & ((1 << max_depth) - 1),
        "quotient": start >> max_depth,
        "odd_count": None,
        "image": None,
        "q_threshold": None,
        "shortcut_steps_until_below_start": None,
        "trivial_cycle_entry": False,
    }


def total_stopping_profile(start: int, step_limit: int) -> dict[str, int | bool]:
    if start == 1:
        return {
            "reached_one": True,
            "total_shortcut_steps": 0,
            "first_below_start_step": 0,
            "max_seen": 1,
        }

    x = start
    max_seen = x
    below_at = 0 if start <= 1 else -1
    for step in range(1, step_limit + 1):
        x = shortcut(x)
        if x > max_seen:
            max_seen = x
        if below_at < 0 and x < start:
            below_at = step
        if x == 1:
            return {
                "reached_one": True,
                "total_shortcut_steps": step,
                "first_below_start_step": below_at,
                "max_seen": max_seen,
            }
    return {
        "reached_one": False,
        "total_shortcut_steps": step_limit,
        "first_below_start_step": below_at,
        "max_seen": max_seen,
    }


def scan(limit: int, max_depth: int, top_n: int, step_limit: int) -> dict[str, object]:
    pow3 = [1]
    for _ in range(max_depth):
        pow3.append(pow3[-1] * 3)

    started = perf_counter()
    depth_histogram: Counter[int] = Counter()
    parity_length_histogram: Counter[int] = Counter()
    uncertified: list[int] = []
    records: list[dict[str, int | bool | None]] = []
    record_setters: list[dict[str, int | bool | None]] = []
    worst_depth = -1

    for start in range(1, limit + 1):
        cert = certificate_for_start(start, max_depth, pow3)
        if not cert["certified"]:
            uncertified.append(start)
            continue

        depth = int(cert["depth"])
        depth_histogram[depth] += 1
        parity_length_histogram[start.bit_length()] += 1
        profile = total_stopping_profile(start, step_limit)
        row = {"start": start, **cert, **profile}
        records.append(row)
        records = sorted(records, key=lambda item: (int(item["depth"]), int(item["start"])), reverse=True)[:top_n]
        if depth > worst_depth:
            worst_depth = depth
            record_setters.append(row)

    elapsed = perf_counter() - started
    certified = limit - len(uncertified)
    return {
        "limit": limit,
        "max_depth": max_depth,
        "step_limit": step_limit,
        "elapsed_seconds": round(elapsed, 6),
        "certified_count": certified,
        "uncertified_count": len(uncertified),
        "uncertified_samples": uncertified[:top_n],
        "max_certificate_depth": worst_depth,
        "depth_histogram": {str(k): depth_histogram[k] for k in sorted(depth_histogram)},
        "bit_length_histogram": {str(k): parity_length_histogram[k] for k in sorted(parity_length_histogram)},
        "top_certificate_depth_records": sorted(records, key=lambda row: (int(row["depth"]), int(row["start"]))),
        "certificate_depth_record_setters": record_setters,
        "interpretation": (
            "A certified start has an explicit residue-cylinder proof that the start itself drops "
            "below its initial value. This is finite evidence, not a global proof."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=10000, help="scan starts 1..limit")
    parser.add_argument("--max-depth", type=int, default=512, help="maximum certificate depth to search")
    parser.add_argument("--top-n", type=int, default=12, help="number of worst records / samples to report")
    parser.add_argument("--step-limit", type=int, default=10000, help="step cap for profile metadata")
    args = parser.parse_args()

    if args.limit < 1:
        raise SystemExit("--limit must be at least 1")
    if args.max_depth < 1:
        raise SystemExit("--max-depth must be at least 1")

    print(json.dumps(scan(args.limit, args.max_depth, args.top_n, args.step_limit), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

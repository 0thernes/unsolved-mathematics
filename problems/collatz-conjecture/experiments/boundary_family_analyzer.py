#!/usr/bin/env python3
"""Analyze finite positive shadows of the all-odd 2-adic boundary path.

The infinite all-odd parity path is the 2-adic fixed point -1.  Positive
integers can shadow it for only finitely many low bits.  The most direct
finite shadows are Mersenne starts n = 2^m - 1, which take m consecutive odd
shortcut steps:

    T^m(2^m - 1) = 3^m - 1.

This script measures how those finite shadows escape into ordinary descent
certificates and compares them with certificate-depth record setters.
"""

from __future__ import annotations

import argparse
import json
import math

from certificate_depth_scan import certificate_for_start, total_stopping_profile


RECORD_SETTERS_THROUGH_1M = [
    1,
    2,
    3,
    7,
    27,
    703,
    10087,
    35655,
    270271,
    362343,
    381727,
    626331,
]

BARINA_PATH_RECORD = 2_358_909_599_867_980_429_759


def ctz(n: int) -> int:
    if n == 0:
        raise ValueError("ctz(0) is undefined")
    return (n & -n).bit_length() - 1


def pow3_table(max_depth: int) -> list[int]:
    pow3 = [1]
    for _ in range(max_depth):
        pow3.append(pow3[-1] * 3)
    return pow3


def mersenne_row(m: int, max_depth: int, pow3: list[int], step_limit: int) -> dict[str, int | float | bool | None]:
    start = (1 << m) - 1
    after_all_odd = pow(3, m) - 1
    even_drain = ctz(after_all_odd)
    after_even_drain = after_all_odd >> even_drain
    cert = certificate_for_start(start, max_depth, pow3)
    profile = total_stopping_profile(start, step_limit)
    return {
        "m": m,
        "start": start,
        "start_bit_length": start.bit_length(),
        "all_odd_prefix_length": m,
        "after_all_odd": after_all_odd,
        "v2_3^m_minus_1": even_drain,
        "after_even_drain": after_even_drain,
        "log2_peak_after_all_odd_over_start": math.log2(after_all_odd / start),
        "certificate_depth": cert["depth"],
        "certificate_odd_count": cert["odd_count"],
        "certificate_q_threshold": cert["q_threshold"],
        "certified": cert["certified"],
        **profile,
    }


def start_row(start: int, max_depth: int, pow3: list[int], step_limit: int) -> dict[str, int | bool | None]:
    cert = certificate_for_start(start, max_depth, pow3)
    profile = total_stopping_profile(start, step_limit)
    return {
        "start": start,
        "bit_length": start.bit_length(),
        "trailing_one_bits": ctz(start + 1),
        "certificate_depth": cert["depth"],
        "certificate_odd_count": cert["odd_count"],
        "certificate_q_threshold": cert["q_threshold"],
        "certified": cert["certified"],
        **profile,
    }


def analyze(max_m: int, max_depth: int, step_limit: int) -> dict[str, object]:
    pow3 = pow3_table(max_depth)

    mersenne_rows = [mersenne_row(m, max_depth, pow3, step_limit) for m in range(1, max_m + 1)]
    mersenne_records: list[dict[str, int | float | bool | None]] = []
    best_depth = -1
    for row in mersenne_rows:
        depth = row["certificate_depth"]
        if isinstance(depth, int) and depth > best_depth:
            best_depth = depth
            mersenne_records.append(row)

    named_starts = RECORD_SETTERS_THROUGH_1M + [BARINA_PATH_RECORD]
    named_rows = [start_row(start, max_depth, pow3, step_limit) for start in named_starts]

    return {
        "max_m": max_m,
        "max_depth": max_depth,
        "step_limit": step_limit,
        "identity_checked": "T^m(2^m - 1) = 3^m - 1 for the shortcut map",
        "mersenne_record_setters_by_certificate_depth": mersenne_records,
        "mersenne_tail_samples": mersenne_rows[-min(12, len(mersenne_rows)):],
        "known_hard_start_rows": named_rows,
        "interpretation": (
            "Mersenne starts are finite positive shadows of the 2-adic point -1. "
            "They can shadow the all-odd path for exactly m steps, then must leave it. "
            "The remaining proof problem is to uniformly bound this escape-to-certificate behavior."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-m", type=int, default=96, help="largest Mersenne exponent to analyze")
    parser.add_argument("--max-depth", type=int, default=4096, help="maximum certificate depth")
    parser.add_argument("--step-limit", type=int, default=20000, help="step cap for profile metadata")
    args = parser.parse_args()

    if args.max_m < 1:
        raise SystemExit("--max-m must be at least 1")
    if args.max_depth < 1:
        raise SystemExit("--max-depth must be at least 1")

    print(json.dumps(analyze(args.max_m, args.max_depth, args.step_limit), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

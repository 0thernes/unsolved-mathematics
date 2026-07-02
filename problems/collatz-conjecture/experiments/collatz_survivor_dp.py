#!/usr/bin/env python3
"""Exact survivor counts for the residue-certificate frontier.

The descent miner in collatz_residue_lab.py certifies a residue-prefix as soon as
the first d shortcut steps have multiplier 3^o smaller than the starting modulus
2^d.  Certification therefore depends only on the parity-prefix odd count o:

    certified at depth d  <=>  3^o < 2^d.

This dynamic program counts, without enumerating residues, how many parity
prefixes survive that test through each depth.  It is an exact shadow of the
frontier size in the residue miner.
"""

from __future__ import annotations

import argparse
import json
import math


def survivor_rows(max_depth: int, report_every: int, include_histogram: bool) -> list[dict[str, object]]:
    states: dict[int, int] = {0: 1}
    pow3 = [1]
    rows: list[dict[str, object]] = []

    for depth in range(1, max_depth + 1):
        pow3.append(pow3[-1] * 3)
        next_states: dict[int, int] = {}
        boundary = 1 << depth

        for odd_count, count in states.items():
            for child_odd_count in (odd_count, odd_count + 1):
                if pow3[child_odd_count] >= boundary:
                    next_states[child_odd_count] = next_states.get(child_odd_count, 0) + count

        states = next_states
        if depth == 1 or depth == max_depth or depth % report_every == 0:
            survivors = sum(states.values())
            total = 1 << depth
            fraction = survivors / total
            min_odd = min(states) if states else None
            max_odd = max(states) if states else None
            row: dict[str, object] = {
                "depth": depth,
                "survivors": survivors,
                "total_prefixes": total,
                "fraction": fraction,
                "log2_survivors": math.log2(survivors) if survivors else float("-inf"),
                "log2_fraction": math.log2(fraction) if fraction else float("-inf"),
                "min_odd_count": min_odd,
                "max_odd_count": max_odd,
            }
            if include_histogram:
                row["odd_count_histogram"] = {str(k): states[k] for k in sorted(states)}
            rows.append(row)

    return rows


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-depth", type=int, default=128, help="maximum prefix depth")
    parser.add_argument("--report-every", type=int, default=8, help="report every N depths")
    parser.add_argument("--include-histogram", action="store_true", help="include exact odd-count histograms")
    args = parser.parse_args()

    if args.max_depth < 1:
        raise SystemExit("--max-depth must be at least 1")
    if args.report_every < 1:
        raise SystemExit("--report-every must be at least 1")

    payload = {
        "max_depth": args.max_depth,
        "report_every": args.report_every,
        "survival_rule": "keep parity prefixes whose every reported/live prefix satisfies 3^odd_count >= 2^depth",
        "interpretation": (
            "These counts match the open frontier of collatz_residue_lab.py. "
            "The frontier is exponentially thin but nonempty at every finite depth; "
            "the all-odd path corresponds to the 2-adic fixed point -1."
        ),
        "rows": survivor_rows(args.max_depth, args.report_every, args.include_histogram),
    }
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

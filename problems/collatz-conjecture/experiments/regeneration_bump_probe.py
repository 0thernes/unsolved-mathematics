#!/usr/bin/env python3
"""
Bump probe: classify the unexplained j = 6-7 excess in the -5 family's
fresh-jump histogram (REGENERATION-EVENTS.md follow-up).

Hypothesis to test: v2(x+5) >= 6 is exactly the x ≡ 59 mod 64 repeat gate of
LOW-ALIGNMENT-STRUCTURE.md, so the bump may be repeat-gate regeneration.
For every -5-family fresh event with jump j in 5..10, record the firing
state's residue mod 4096, its parity/phase (which of x+5 / x+7 / x+10 is
deep), and whether the PREVIOUS state sat on the 59 mod 64 gate.

Run: python experiments/regeneration_bump_probe.py [--starts 2000000]
"""

from __future__ import annotations

import argparse
import json
from collections import Counter


def v2p(t: int) -> int:
    return ((t & -t).bit_length() - 1) if t else 0


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--starts", type=int, default=2_000_000)
    p.add_argument("--out", type=str,
                   default="experiments/results/regeneration_bump_probe.json")
    args = p.parse_args()

    by_j_phase = Counter()          # (j, phase) -> count
    by_j_res = {}                   # j -> Counter of state mod 4096
    prev_gate = Counter()           # (j, prev_state ≡ 59 mod 64?) -> count
    prev_res = {}                   # j -> Counter of PREVIOUS state mod 64
    for j in range(5, 11):
        by_j_res[j] = Counter()
        prev_res[j] = Counter()

    n = 1
    for _ in range(args.starts):
        n += 2
        cur = n
        if cur & 1:
            a, b = v2p(cur + 5), v2p(cur + 7)
            prev_a5 = a if a > b else b
        else:
            prev_a5 = v2p(cur + 10)
        prev_state = cur
        while cur > 1:
            cur = (3 * cur + 1) >> 1 if cur & 1 else cur >> 1
            if cur & 1:
                x5, x7 = v2p(cur + 5), v2p(cur + 7)
                a5 = x5 if x5 > x7 else x7
                phase = "+5" if x5 >= x7 else "+7"
            else:
                a5 = v2p(cur + 10)
                phase = "+10"
            inh = prev_a5 - 1 if prev_a5 > 1 else 0
            if a5 > inh:
                j = a5 - inh
                if 5 <= j <= 10:
                    by_j_phase[(j, phase)] += 1
                    by_j_res[j][cur % 4096] += 1
                    prev_gate[(j, prev_state % 64 == 59)] += 1
                    prev_res[j][prev_state % 64] += 1
            prev_a5 = a5
            prev_state = cur

    out = {
        "starts": args.starts,
        "by_j_phase": {f"{j}|{ph}": c for (j, ph), c in
                       sorted(by_j_phase.items())},
        "top_state_residues_mod4096": {
            str(j): by_j_res[j].most_common(12) for j in range(5, 11)},
        "prev_state_on_59mod64_gate": {
            f"{j}|{g}": c for (j, g), c in sorted(prev_gate.items())},
        "top_prev_residues_mod64": {
            str(j): prev_res[j].most_common(8) for j in range(5, 11)},
    }
    with open(args.out, "w") as f:
        json.dump(out, f, indent=2)
    print(json.dumps(out["by_j_phase"], indent=1))
    print("prev on gate:", out["prev_state_on_59mod64_gate"])
    print(f"Wrote {args.out}")


if __name__ == "__main__":
    main()

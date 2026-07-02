#!/usr/bin/env python3
"""
CHAITIN SURPRISE COUNTER — Proxy for Kolmogorov cost of staying supercritical.

For positive n, the "program" is its bits (size ~b).
To realize an itinerary that stays in S, at every repulsion/alignment the dynamics "surprises" with carry flips that deviate from the pure cylinder word.

Each surprise has a description cost: roughly the number of bits that had to be 'corrected' (carry length or delta in next parities).

If cumulative surprise cost exceeds b + O(1) before termination, then no finite program of size b can have produced an infinite S-itinerary.

This is runnable proxy for the rigidity.

Run on hard seeds and frontier lifts.
"""

import argparse
import json
import math
from collections import defaultdict

def shortcut_parity(n):
    if n % 2 == 0:
        return n // 2, 0
    return (3 * n + 1) // 2, 1

def compute_surprise_cost(n, max_steps=10000):
    """Run orbit, at each near-alignment (high v2(n+1)) on odd, measure deviation cost."""
    orig = n
    b = n.bit_length()
    current = n
    total_surprise = 0.0
    surprises = []
    d = 0
    o = 0
    alignments = []

    while current > 1 and d < max_steps:
        # measure alignment to boundary
        align = 0
        tmp = current + 1
        while tmp % 2 == 0 and align < 64:
            tmp //= 2
            align += 1
        alignments.append(align)

        prev = current
        current, is_odd = shortcut_parity(current)
        d += 1
        if is_odd:
            o += 1

        if is_odd and align >= 3:
            # surprise proxy: how much did the post-alignment differ from "pure continuation"
            # Pure continuation for boundary would keep high alignment.
            post_align = 0
            tmp2 = current + 1
            while tmp2 % 2 == 0 and post_align < 64:
                tmp2 //= 2
                post_align += 1

            # cost: the 'lost' alignment bits + any extra flips
            lost = max(0, align - post_align)
            flip_cost = abs(align - post_align)
            surprise = lost + flip_cost * 0.5   # heuristic bits of description needed to 'force' this deviation
            total_surprise += surprise

            if surprise > 0.5:
                surprises.append({
                    "d": d,
                    "pre_align": align,
                    "post_align": post_align,
                    "surprise": surprise,
                    "current": prev
                })

        if current < orig:
            break

    return {
        "start": n,
        "bitlen": b,
        "steps": d,
        "odds": o,
        "total_surprise": total_surprise,
        "surprise_per_bit": total_surprise / max(1, b),
        "num_surprises": len(surprises),
        "first_surprise_d": surprises[0]["d"] if surprises else None,
        "max_surprise_event": max((s["surprise"] for s in surprises), default=0),
        "exceeds_budget": total_surprise > b + 10,  # loose +O(1)
        "sample_surprises": surprises[:5]
    }

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--starts", default="27,703,35655,626331,2358909599867980429759")
    ap.add_argument("--max-steps", type=int, default=4096)
    ap.add_argument("--json-out", default="results/chaitin_surprise.json")
    args = ap.parse_args()

    starts = [int(x.strip()) for x in args.starts.split(",")]
    results = []
    for s in starts:
        res = compute_surprise_cost(s, args.max_steps)
        results.append(res)
        print(f"n={s} b={res['bitlen']} surprise={res['total_surprise']:.2f} /b={res['surprise_per_bit']:.3f} exceeds={res['exceeds_budget']} surprises={res['num_surprises']}")

    with open(args.json_out, "w") as f:
        json.dump({"results": results, "note": "Chaitin proxy: cumulative surprise (lost alignment bits at kicks) as description cost. Finite b cannot pay for infinite S."}, f, indent=2)
    print("Wrote", args.json_out)

if __name__ == "__main__":
    main()

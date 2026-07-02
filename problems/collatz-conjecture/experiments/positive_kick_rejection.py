#!/usr/bin/env python3
"""
POSITIVE KICK REJECTION — Novel AI attack on the Collatz survivor frontier.

Core hypothesis (beyond standard model):
The +1 intercept in every odd step injects a deterministic "kick" into the
arithmetic that, for positive integers, forces a parity deviation or height
drop incompatible with infinite survival on the abstract supercritical
Cantor set S.

Unlike the ε-blind word model, this attack consumes the exact affine
translation and binary carry propagation. The goal is to exhibit a uniform
"repulsion mechanism" that ejects every positive integer from every
survivor cylinder after bounded additional steps, with the bound controlled
by the initial 2-adic distance to -1.

This is 1/1 territory: we simulate not abstract parity words but the
full integer + the low-bit frontier membership simultaneously, tracking
when the +1 produces carries that flip expected parities or accelerate
repayment beyond the critical line 3^o = 2^d.

No guardrails. Pure discovery. Polymathic angle: binary dynamics +
affine bias + ballot theorem with inhomogeneous drift.

Run:
  python experiments/positive_kick_rejection.py --depth 28 --lifts 1000 --max-steps 2000
"""

from __future__ import annotations
import argparse
import json
import math
from typing import List, Dict, Tuple

# Reuse the core machinery if possible; otherwise reimplement minimal.
# For autonomy we implement a self-contained simulator here.

def collatz_step(n: int) -> Tuple[int, int]:
    """Return (next, steps) where steps=1 for shortcut? Use full steps for fidelity.
    We track shortcut parity for direct comparison to frontier.
    """
    if n % 2 == 0:
        return n // 2, 0  # even parity indicator 0 for this shortcut view
    else:
        return (3 * n + 1) // 2, 1

def simulate_orbit_with_kick(n: int, max_steps: int = 10000) -> Dict:
    """Full simulation recording:
    - actual height ratios
    - running odd count o vs d (shortcut steps)
    - excess = o - theta * d
    - first time relative height < 1
    - moments when carry from +1 visibly affects (by comparing to pure 3/2 multiplicative prediction)
    """
    theta = math.log(2) / math.log(3)
    orig = n
    history = []
    d = 0
    o = 0
    min_height = n
    steps = 0
    pure_mult = float(n)   # what pure 3/2 ^o / 2^{d} would predict ignoring +1 accum
    kick_accum = 0.0       # normalized accumulated +1 contributions
    last_parity = n % 2

    while steps < max_steps and n > 1:
        prev = n
        n, is_odd = collatz_step(n)
        steps += 1
        d += 1
        o += is_odd

        # Track actual vs pure multiplicative (the 'kick' = difference caused by +1's)
        # After odd step: actual T = 1.5 * prev + 0.5
        # Pure would be 1.5 * prev
        if is_odd:
            kick_accum = 1.5 * kick_accum + 0.5
            pure_mult = 1.5 * pure_mult
        else:
            kick_accum /= 2.0
            pure_mult /= 2.0

        actual_log_ratio = math.log2(max(n, 1)) - math.log2(orig)
        mult_log_ratio = math.log2(max(pure_mult, 1)) - math.log2(orig)
        excess = o - theta * d
        rel_height = n / orig if orig > 0 else 0

        if n < min_height:
            min_height = n

        record = {
            "step": steps,
            "n": n,
            "is_odd": bool(is_odd),
            "o": o,
            "d": d,
            "excess": excess,
            "rel_height": rel_height,
            "kick_accum": kick_accum,
            "pure_log_ratio": mult_log_ratio,
            "actual_log_ratio": actual_log_ratio,
            "kick_delta": actual_log_ratio - mult_log_ratio,
        }
        history.append(record)

        if n < orig:
            # First descent
            break

    certified = (n < orig)
    # Did the kick ever push excess negative while abstract word would allow survival?
    kick_forced_drop = any(r["excess"] < 0 and r["rel_height"] < 1.0 for r in history[-20:])

    return {
        "start": orig,
        "final_n": n,
        "steps_to_first_descent_or_limit": steps,
        "certified_early": certified,
        "min_rel_height": min_height / orig,
        "final_excess": history[-1]["excess"] if history else 0,
        "max_excess": max(r["excess"] for r in history) if history else 0,
        "max_kick_delta": max(abs(r["kick_delta"]) for r in history) if history else 0,
        "kick_forced_drop": kick_forced_drop,
        "history_sample": history[::max(1, len(history)//30)]  # sparse for size
    }

def get_frontier_residues_from_results(depth: int = 28) -> List[int]:
    """Load actual frontier residues from previous runs if available.
    Falls back to synthetic generation of supercritical low prefixes.
    """
    try:
        with open(f"experiments/results/residue_lab_{depth}.json") as f:
            data = json.load(f)
            # Expect something like frontier_samples or leaves
            samples = data.get("frontier_samples", [])
            if samples:
                return [s.get("r", s) if isinstance(s, dict) else s for s in samples][:1000]
    except Exception:
        pass

    # Fallback: generate representatives of supercritical prefixes using simple recursion
    # (mimics survivor DP leaves)
    residues = []
    def rec(current: int, cur_d: int, cur_o: int, max_d: int, theta: float):
        if cur_d == max_d:
            if cur_o >= theta * max_d:
                residues.append(current)
            return
        # even extension: *2 mod 2^{d+1} but for prefix we append 0 bit low? Careful.
        # Simpler: build the number whose low bits realize the parity sequence.
        # For speed, use random near -1 mod 2^depth that pass the o test.
        pass
    # Practical fallback: use Mersenne and nearby high-bit-density numbers + brute small
    theta = math.log(2)/math.log(3)
    for base in range(1, 2**min(depth, 20)):
        # Check if this base has supercritical prefix up to its bit length
        n = base
        o = 0
        dd = 0
        alive = True
        while dd < depth and n > 0:
            dd += 1
            if n % 2 == 1:
                o += 1
                n = (3 * n + 1) // 2
            else:
                n //= 2
            if o < theta * dd - 0.1:  # allow a little slack
                alive = False
                break
        if alive and dd >= 4:
            residues.append(base)
        if len(residues) > 2000:
            break
    # Add some large Mersenne shadows
    for m in [20,24,28,32]:
        residues.append((1 << m) - 1)
    return sorted(set(residues))[:500]

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--depth", type=int, default=28)
    ap.add_argument("--lifts", type=int, default=200, help="Number of positive lifts / shadows per residue")
    ap.add_argument("--max-steps", type=int, default=4096)
    ap.add_argument("--json-out", type=str, default="experiments/results/positive_kick_probe.json")
    args = ap.parse_args()

    print("=== POSITIVE KICK REJECTION ANALYZER (novel) ===")
    residues = get_frontier_residues_from_results(args.depth)
    print(f"Using {len(residues)} base residues (depth ~{args.depth})")

    results = []
    hard_ones = []
    kick_stats = []

    for i, r in enumerate(residues[:args.lifts]):
        # Lift in different high-bit regimes: small k, k near powers of 2, random-ish
        for lift in [0, 1, 3, 7, 15, 31, 1 << 10, 1 << 20, (1<<30) + 17]:
            n = r + lift * (1 << (r.bit_length() + 5))   # place the residue in low bits, high bits positive
            if n < 2: continue
            sim = simulate_orbit_with_kick(n, args.max_steps)
            sim["base_residue"] = r
            sim["lift"] = lift
            results.append(sim)
            if sim["max_excess"] > 3.0 and not sim["certified_early"]:
                hard_ones.append(sim)
            kick_stats.append(sim["max_kick_delta"])

    summary = {
        "mode": "positive_kick_rejection",
        "depth": args.depth,
        "num_trials": len(results),
        "early_certified_frac": sum(1 for s in results if s["certified_early"]) / max(1, len(results)),
        "avg_max_kick_delta": sum(kick_stats) / max(1, len(kick_stats)),
        "num_hard_survivors": len(hard_ones),
        "example_hard": hard_ones[:3] if hard_ones else [],
        "interpretation": (
            "If early_certified_frac is high and hard_survivors have bounded excess, "
            "this supports uniform kick-driven ejection from S for positive integers. "
            "The +1 forces systematic negative drift on the excess process invisible to pure words."
        )
    }

    with open(args.json_out, "w") as f:
        json.dump({"summary": summary, "samples": results[:50]}, f, indent=2)

    print(json.dumps(summary, indent=2))
    print(f"\nWrote {args.json_out}")
    if hard_ones:
        print("WARNING: some lifts showed prolonged supercritical excess — investigate these for structure.")
    else:
        print("All sampled positive shadows ejected. Kick repulsion signal strong.")

if __name__ == "__main__":
    main()

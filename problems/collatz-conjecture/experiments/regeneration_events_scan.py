#!/usr/bin/env python3
"""
Per-event alignment-regeneration scan (SPINE-LADDER follow-up, loop iteration 1).

The SPINE-LADDER regeneration data was state-weighted, so decay-chain states
inherited from one deep-alignment event inflated the tails (code-referee
caveat). This instrument counts EVENTS: fresh bits of spine alignment acquired
beyond what the ladder's deterministic 1-bit-per-step decay inherits.

Alignment-to-cycle (phase-correct, decays exactly 1 per shortcut step while
riding, by the Spine Ladder Lemma applied to rotations):
  -1 spine:   a(x) = v2(x+1)                      (odd states only)
  -5 cycle:   a(x) = v2(x+5) or v2(x+7) if x odd; v2(x+10) if x even
              (members -5, -7 odd; -10 even; at most one is nonzero > 2
               since the cycle points are 2-adically separated)

Event at state t (per spine family): fresh_t = a_t - max(a_{t-1} - 1, 0) > 0.
fresh_t is exactly the number of regenerated low bits. IID coin model:
P(fresh >= j) ~ 2^-j per state. A provable finite-window tail bound on fresh
bits is the theorem target; this measures the empirical law at scale.

Outputs: per-spine jump-size histograms (events, not states), per-orbit total
fresh bits vs bit-length of start, maxima with witnesses, model comparison.

Run: python experiments/regeneration_events_scan.py [--starts 10000000]
"""

from __future__ import annotations

import argparse
import json
import math
import sys
import time


def v2p(t: int) -> int:
    """2-adic valuation of positive t via bit trick."""
    return ((t & -t).bit_length() - 1) if t else 0


def scan(num_starts: int, max_steps: int = 100_000,
         progress_every: int = 500_000) -> dict:
    hist1 = [0] * 64          # -1 spine: fresh-jump-size histogram (events)
    hist5 = [0] * 64          # -5 cycle: fresh-jump-size histogram (events)
    orbit_fresh1_hist = [0] * 256   # per-orbit total fresh bits, -1 spine
    orbit_fresh5_hist = [0] * 256
    max_jump1 = max_jump5 = 0
    arg_jump1 = arg_jump5 = 0
    max_total1 = max_total5 = 0
    arg_total1 = arg_total5 = 0
    total_states = 0
    total_orbits = 0
    worst_ratio1 = (0.0, 0)   # per-orbit fresh1 / bitlen(n)

    t0 = time.time()
    n = 1
    for i in range(num_starts):
        n += 2  # odd starts 3, 5, 7, ...
        cur = n
        prev_a1 = v2p(n + 1) if n & 1 else 0     # seed alignments (excluded
        if n & 1:                                # from fresh-bit accounting
            pa5 = v2p(n + 5)
            pb5 = v2p(n + 7)
            prev_a5 = pa5 if pa5 > pb5 else pb5
        else:
            prev_a5 = v2p(n + 10)
        f1 = f5 = 0
        steps = 0
        while cur > 1 and steps < max_steps:
            if cur & 1:
                cur = (3 * cur + 1) >> 1
            else:
                cur >>= 1
            steps += 1
            if cur & 1:
                a1 = v2p(cur + 1)
                x5 = v2p(cur + 5)
                y5 = v2p(cur + 7)
                a5 = x5 if x5 > y5 else y5
            else:
                a1 = 0
                a5 = v2p(cur + 10)
            inh1 = prev_a1 - 1 if prev_a1 > 1 else 0
            inh5 = prev_a5 - 1 if prev_a5 > 1 else 0
            if a1 > inh1:
                j = a1 - inh1
                hist1[j if j < 64 else 63] += 1
                f1 += j
                if j > max_jump1:
                    max_jump1, arg_jump1 = j, n
            if a5 > inh5:
                j = a5 - inh5
                hist5[j if j < 64 else 63] += 1
                f5 += j
                if j > max_jump5:
                    max_jump5, arg_jump5 = j, n
            prev_a1, prev_a5 = a1, a5
        total_states += steps
        total_orbits += 1
        orbit_fresh1_hist[f1 if f1 < 256 else 255] += 1
        orbit_fresh5_hist[f5 if f5 < 256 else 255] += 1
        if f1 > max_total1:
            max_total1, arg_total1 = f1, n
        if f5 > max_total5:
            max_total5, arg_total5 = f5, n
        r = f1 / n.bit_length()
        if r > worst_ratio1[0]:
            worst_ratio1 = (r, n)
        if (i + 1) % progress_every == 0:
            el = time.time() - t0
            print(f"[{i+1}/{num_starts}] {el:.0f}s  states={total_states}  "
                  f"maxjump(-1)={max_jump1}@{arg_jump1}  "
                  f"maxjump(-5)={max_jump5}@{arg_jump5}", flush=True)

    # model comparison: per-state P(fresh >= j) vs 2^-j
    ev1 = sum(hist1)
    ev5 = sum(hist5)
    tail_model = {}
    for j in (4, 8, 12, 16, 20):
        ge1 = sum(hist1[j:])
        ge5 = sum(hist5[j:])
        tail_model[str(j)] = {
            "minus1_P_state": ge1 / max(1, total_states),
            "minus5_P_state": ge5 / max(1, total_states),
            "iid_2^-j": 2.0 ** -j,
        }
    return {
        "num_starts": num_starts,
        "total_states": total_states,
        "events_minus1": ev1,
        "events_minus5": ev5,
        "events_per_state": {"minus1": ev1 / max(1, total_states),
                             "minus5": ev5 / max(1, total_states)},
        "jump_hist_minus1": hist1,
        "jump_hist_minus5": hist5,
        "max_single_jump": {"minus1": [max_jump1, arg_jump1],
                            "minus5": [max_jump5, arg_jump5]},
        "max_orbit_total_fresh": {"minus1": [max_total1, arg_total1],
                                  "minus5": [max_total5, arg_total5]},
        "worst_fresh1_per_bit": {"ratio": worst_ratio1[0],
                                 "start": worst_ratio1[1]},
        "orbit_fresh_hist_minus1": orbit_fresh1_hist,
        "orbit_fresh_hist_minus5": orbit_fresh5_hist,
        "tail_vs_iid": tail_model,
        "elapsed_s": round(time.time() - t0, 1),
    }


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--starts", type=int, default=10_000_000)
    p.add_argument("--out", type=str,
                   default="experiments/results/regeneration_events_scan.json")
    args = p.parse_args()
    print(f"Per-event regeneration scan: {args.starts} odd starts", flush=True)
    res = scan(args.starts)
    with open(args.out, "w") as f:
        json.dump(res, f, indent=2)
    print("SUMMARY", flush=True)
    print(json.dumps({k: res[k] for k in
                      ("num_starts", "total_states", "events_per_state",
                       "max_single_jump", "max_orbit_total_fresh",
                       "worst_fresh1_per_bit", "tail_vs_iid")}, indent=2))
    print(f"Wrote {args.out}", flush=True)


if __name__ == "__main__":
    main()

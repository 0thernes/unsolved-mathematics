#!/usr/bin/env python3
"""
Haar-measure baseline for the fresh-jump law (bump follow-up).

The 2^-j coin baseline in REGENERATION-EVENTS.md is phase-blind, but fresh_t
compares alignments of CONSECUTIVE states, which are deterministically coupled
by T. The correct null model is the one-step fresh law under the uniform
(Haar) measure on Z_2, which T preserves: sample x uniform mod 2^128, apply
one shortcut step, compute fresh for the -5 family exactly as the orbit scan
does, histogram by (j, phase). No orbits, no start-set bias, no correlations
beyond the single transition - this is the exact model the orbit statistics
should be compared against. If this reproduces the j=6-7 bump, the bump is a
property of the map's local transition structure (model artifact of the naive
baseline), not of positive-integer orbits.

Run: python experiments/model_baseline_probe.py [--samples 100000000]
"""

from __future__ import annotations

import argparse
import json
import random


def v2p(t: int) -> int:
    return ((t & -t).bit_length() - 1) if t else 0


def a5_phase(x: int):
    if x & 1:
        a, b = v2p(x + 5), v2p(x + 7)
        return (a, "+5") if a >= b else (b, "+7")
    return v2p(x + 10), "+10"


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--samples", type=int, default=100_000_000)
    p.add_argument("--seed", type=int, default=20260702)
    p.add_argument("--out", type=str,
                   default="experiments/results/model_baseline_probe.json")
    args = p.parse_args()
    rng = random.Random(args.seed)

    hist = [0] * 64                 # fresh-jump sizes, one-step Haar model
    phase_hist = {}                 # (j,phase) for j in 1..12
    events = 0
    for i in range(args.samples):
        x = rng.getrandbits(128)
        a_prev, _ = a5_phase(x)
        y = (3 * x + 1) >> 1 if x & 1 else x >> 1
        a_new, ph = a5_phase(y)
        inh = a_prev - 1 if a_prev > 1 else 0
        if a_new > inh:
            j = a_new - inh
            hist[j if j < 64 else 63] += 1
            events += 1
            if 1 <= j <= 12:
                phase_hist[f"{j}|{ph}"] = phase_hist.get(f"{j}|{ph}", 0) + 1
        if (i + 1) % 20_000_000 == 0:
            print(f"[{i+1}/{args.samples}]", flush=True)

    tails = {}
    for j in range(1, 13):
        ge = sum(hist[j:])
        tails[str(j)] = {"P": ge / args.samples,
                         "ratio_to_2^-j": (ge / args.samples) * (2 ** j)}
    out = {"samples": args.samples, "events_per_state": events / args.samples,
           "jump_hist": hist[:20], "tails": tails,
           "phase_hist": dict(sorted(phase_hist.items()))}
    with open(args.out, "w") as f:
        json.dump(out, f, indent=2)
    print(json.dumps({"events_per_state": out["events_per_state"],
                      "tails": tails}, indent=1))
    print(f"Wrote {args.out}")


if __name__ == "__main__":
    main()

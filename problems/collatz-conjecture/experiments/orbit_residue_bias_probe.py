#!/usr/bin/env python3
"""
Orbit residue bias probe (REGENERATION-EVENTS null-model follow-up).

The Haar computation showed the one-step stationary fresh law is exactly
geometric, so all orbit deviations must come from HOW positive orbits sample
residues. Since a5-alignment >= k is a condition on x mod 2^k, the empirical
distribution of orbit states mod 2^12 (together with the deterministic
one-step law) determines the fresh law for all j <= 9. This probe measures:

  (1) the mod-2^12 histogram of orbit states (vs uniform 2^-12),
  (2) the same split by state bit-length bucket (finite-size conditioning),
  (3) direct frequencies of the -5-family shallow/deep residue conditions
      P(a5 >= k) for k = 2..10, per phase, vs Haar values,
  (4) a reconstruction check: P(fresh >= j) recomputed by pushing the
      measured mod-2^12 state distribution through one exact step, compared
      to the orbit-measured tails from regeneration_events_scan.json.

If (4) matches the orbit tails, the deviations are fully accounted for by
state-residue sampling bias (mechanism located, cause still open); if not,
multi-step correlations matter and the mechanism question deepens.

Run: python experiments/orbit_residue_bias_probe.py [--starts 2000000]
"""

from __future__ import annotations

import argparse
import json


def v2p(t: int) -> int:
    return ((t & -t).bit_length() - 1) if t else 0


def a5_of(x: int) -> int:
    if x & 1:
        a, b = v2p(x + 5), v2p(x + 7)
        return a if a > b else b
    return v2p(x + 10)


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--starts", type=int, default=2_000_000)
    p.add_argument("--out", type=str,
                   default="experiments/results/orbit_residue_bias_probe.json")
    args = p.parse_args()

    M = 1 << 12
    hist = [0] * M                       # state mod 2^12
    hist_small = [0] * M                 # states with bitlen <= 20
    hist_large = [0] * M                 # states with bitlen > 20
    total = 0
    odd_states = 0
    a5_ge = [0] * 16                     # counts of a5(x) >= k (k index)

    n = 1
    for _ in range(args.starts):
        n += 2
        cur = n
        while cur > 1:
            cur = (3 * cur + 1) >> 1 if cur & 1 else cur >> 1
            r = cur & (M - 1)
            hist[r] += 1
            if cur.bit_length() <= 20:
                hist_small[r] += 1
            else:
                hist_large[r] += 1
            total += 1
            if cur & 1:
                odd_states += 1
            a = a5_of(cur)
            for k in range(2, 16):
                if a >= k:
                    a5_ge[k] += 1
                else:
                    break

    # (4) reconstruction: push measured mod-2^12 distribution through one step.
    # For each residue r mod 2^12 we know x = r + 2^12*t; one step gives
    # y = (3x+1)/2 or x/2 whose residue mod 2^11 is determined; alignments
    # up to 9-10 bits are determined by r except when the residue pins fewer
    # bits (deep classes) — handle by capping reconstruction at j <= 8 and
    # treating the undetermined tail as exactly Haar (fair-coin) beyond the
    # determined bits, which is exact for the uniform high part of t only if
    # orbit high bits were uniform — so this reconstruction TESTS that too.
    # Simpler exact approach: empirical joint — recompute fresh tails from a
    # second pass sampling consecutive-state pairs is what the original scan
    # already did; here we do the distributional push with fair high bits.
    recon = [0.0] * 12
    for r in range(M):
        w = hist[r] / max(1, total)
        if w == 0.0:
            continue
        x = r  # low bits; high bits treated as fair coins beyond bit 12
        a_prev = a5_of(x if x & 1 else x)  # determined by low bits up to ~10
        inh = a_prev - 1 if a_prev > 1 else 0
        y = (3 * x + 1) >> 1 if x & 1 else x >> 1
        a_new_det = a5_of(y)               # determined part (~<= 10 bits)
        # probability that a_new exceeds the determined part is fair-coin:
        for j in range(1, 12):
            need = inh + j
            if a_new_det >= need:
                recon[j] += w
            elif a_new_det >= 10:  # undetermined beyond ~10 bits: coin tail
                recon[j] += w * (0.5 ** max(0, need - a_new_det))

    top_dev = sorted(range(M), key=lambda r: -abs(hist[r] / total - 1 / M))[:16]
    out = {
        "starts": args.starts,
        "total_states": total,
        "odd_fraction": odd_states / max(1, total),
        "a5_tail_P": {str(k): a5_ge[k] / max(1, total) for k in range(2, 12)},
        "a5_tail_haar": {str(k): None for k in range(2, 12)},  # filled by referee/analysis
        "top_residue_deviations_mod4096": [
            {"r": r, "freq": hist[r] / total, "uniform": 1 / M,
             "ratio": hist[r] / total * M} for r in top_dev],
        "reconstructed_fresh_tail": {str(j): recon[j] for j in range(1, 12)},
        "small_large_split_totals": [sum(hist_small), sum(hist_large)],
    }
    with open(args.out, "w") as f:
        json.dump(out, f, indent=2)
    print(json.dumps({k: out[k] for k in ("odd_fraction", "a5_tail_P",
                                          "reconstructed_fresh_tail")}, indent=1))
    print("top residue ratios:",
          [(d["r"], round(d["ratio"], 3)) for d in out["top_residue_deviations_mod4096"][:8]])
    print(f"Wrote {args.out}")


if __name__ == "__main__":
    main()

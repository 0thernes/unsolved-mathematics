#!/usr/bin/env python3
"""
stochastic_model_check.py — Empirical check of the Collatz stochastic model.

Companion to collatz_residue_lab.py / collatz_survivor_dp.py (residue-descent
certificates). This instrument tests the OTHER pillar of the heuristic case:
that integer trajectories statistically match the Lagarias–Weiss random-walk
model. It is verification/exploration, not proof, and cannot become one:
distributional agreement says nothing about the measure-zero exceptional set.

Conventions. Shortcut (Terras) map:
    T(n) = n/2         if n even
    T(n) = (3n+1)/2    if n odd
Each shortcut step performs exactly one halving. The model treats the parity
bits of a trajectory as i.i.d. fair coins, so per shortcut step the expected
log-multiplier is
    mu = (1/2)ln(3/2) + (1/2)ln(1/2) = (1/2)ln(3/4) ~ -0.14384,
predicting mean total stopping time  sigma_inf(n) ~ ln(n)/|mu| = 6.9522 ln n
and odd-step fraction -> 1/2 along complete trajectories.

For the DESCENT time (first k with T^k(n) < n) the model prediction is exact,
not heuristic: the first k parity bits of n's trajectory are determined by
n mod 2^k and are equidistributed (Terras 1976). So the empirical descent-time
distribution must match the exact count of parity prefixes first crossing
3^o < 2^k at depth k, divided by 2^k. Any mismatch would be a bug, not a
discovery; the interesting quantities are the ones the model does NOT fix
exactly (total stopping time, records).

Checks performed:
  1. self-test: known trajectory facts (27: 111 classic steps, peak 9232,
     70 shortcut steps of which 41 odd).
  2. total stopping time: mean sigma_inf(n)/ln(n) over [2, N], vs 6.9522.
  3. odd fraction: odd shortcut steps / all shortcut steps, vs 1/2.
  4. descent-time distribution for k <= DEPTH, empirical vs exact prefix count
     (independent DP; no code shared with collatz_survivor_dp.py).
  5. path records: n whose classic-trajectory peak exceeds that of all smaller n.
  6. gamma records: n setting a new record for gamma(n) = sigma_inf(n)/ln(n)
     (shortcut steps). Lagarias–Weiss (Ann. Appl. Prob. 2 (1992) 229–261)
     predict limsup gamma(n) = gamma_BP ~ 41.677647, attained along
     trajectories with odd-step ("ones") ratio ~ 0.609091; note
     1/(ln 2 - 0.609091*ln 3) ~ 41.68. Records reachable at small N sit far
     below the predicted limsup — the extreme tail is the least-tested part
     of the model, and exactly where any counterexample would have to live.

Usage:
    python stochastic_model_check.py --limit 1000000 --depth 24
Output: JSON to stdout.
"""
from __future__ import annotations

import argparse
import json
import math
import sys


def collatz_steps_and_peak(n: int) -> tuple[int, int]:
    """Total steps and trajectory peak under the classic map (3n+1, n/2)."""
    steps, peak = 0, n
    while n != 1:
        n = 3 * n + 1 if n & 1 else n >> 1
        steps += 1
        if n > peak:
            peak = n
    return steps, peak


def shortcut_profile(n: int) -> tuple[int, int]:
    """(total shortcut steps, odd shortcut steps) to reach 1."""
    total = odd = 0
    while n != 1:
        if n & 1:
            n = (3 * n + 1) >> 1
            odd += 1
        else:
            n >>= 1
        total += 1
    return total, odd


def exact_descent_distribution(depth: int) -> list[float]:
    """Model (= exact, by Terras equidistribution) P[descent time = k].

    DP over parity prefixes: a prefix of length k with o odd steps first
    forces descent at k when 3^o < 2^k and 3^{o'} >= 2^{k'} for every proper
    prefix. Track surviving (not-yet-descended) prefix counts by odd count.
    """
    probs: list[float] = [0.0] * (depth + 1)  # probs[k] for k >= 1
    survivors = {0: 1}  # odd_count -> count of surviving prefixes (empty prefix)
    for k in range(1, depth + 1):
        nxt: dict[int, int] = {}
        crossed = 0
        for o, cnt in survivors.items():
            for bit in (0, 1):  # even / odd next step
                oo = o + bit
                if 3**oo < 2**k:
                    crossed += cnt
                else:
                    nxt[oo] = nxt.get(oo, 0) + cnt
        probs[k] = crossed / 2**k
        survivors = nxt
    return probs


def run(limit: int, depth: int) -> dict:
    ln = math.log
    mu_model = 0.5 * ln(0.75)
    c_model = 1.0 / abs(mu_model)

    # -- self-test ----------------------------------------------------------
    assert collatz_steps_and_peak(27) == (111, 9232), "self-test failed (classic)"
    assert shortcut_profile(27) == (70, 41), "self-test failed (shortcut)"

    # -- single memoized pass over [2, limit] --------------------------------
    # For each n, walk the shortcut map until the value drops below n. The
    # step count at first descent IS the descent time; totals/peaks compose
    # with the cached values of the smaller landing point.
    total_c = [0] * (limit + 1)   # total shortcut steps to 1
    odd_c = [0] * (limit + 1)     # odd shortcut steps to 1
    peak_c = [0] * (limit + 1)    # classic-map trajectory peak
    peak_c[1] = 1

    emp_counts = [0] * (depth + 1)
    emp_undecided = 0
    sum_ratio = 0.0
    grand_total = grand_odd = 0
    records: list[dict] = []
    best_peak = 0
    gamma_records: list[dict] = []
    best_gamma = 0.0

    for n in range(2, limit + 1):
        v, steps, odds, cpeak = n, 0, 0, n
        while v >= n:
            if v & 1:
                up = 3 * v + 1          # classic intermediate (even)
                if up > cpeak:
                    cpeak = up
                v = up >> 1
                odds += 1
            else:
                v >>= 1
            steps += 1
        # v < n: descent achieved at `steps`
        if steps <= depth:
            emp_counts[steps] += 1
        else:
            emp_undecided += 1
        total_c[n] = steps + total_c[v]
        odd_c[n] = odds + odd_c[v]
        peak_c[n] = cpeak if cpeak > peak_c[v] else peak_c[v]

        sum_ratio += total_c[n] / ln(n)
        grand_total += total_c[n]
        grand_odd += odd_c[n]
        if peak_c[n] > best_peak:
            best_peak = peak_c[n]
            records.append({"n": n, "classic_peak": best_peak})
        g = total_c[n] / ln(n)
        if g > best_gamma:
            best_gamma = g
            gamma_records.append({
                "n": n,
                "sigma_inf_shortcut": total_c[n],
                "gamma": round(g, 4),
                "ones_ratio": round(odd_c[n] / total_c[n], 4),
            })

    n_emp = limit - 1
    model = exact_descent_distribution(depth)
    max_abs_dev = max(
        abs(emp_counts[k] / n_emp - model[k]) for k in range(1, depth + 1)
    )

    return {
        "limit": limit,
        "self_test": "passed (n=27: 111 classic steps, peak 9232, 70 shortcut steps / 41 odd)",
        "total_stopping_time_constant": {
            "measured_mean_sigma_over_ln_n": sum_ratio / n_emp,
            "model": c_model,
            "note": "model constant 2/ln(4/3); slow convergence in n is expected",
        },
        "odd_step_fraction": {
            "measured": grand_odd / grand_total,
            "model_asymptotic": 0.5,
            "note": "finite-size bias below 1/2 expected: completed descents carry an excess of halvings",
        },
        "descent_time_distribution": {
            "depth": depth,
            "max_abs_deviation_from_exact_model": max_abs_dev,
            "undecided_within_depth_fraction": emp_undecided / n_emp,
            "model_undecided_fraction": 1.0 - sum(model[1:]),
            "note": "agreement is Terras' equidistribution theorem; serves as implementation cross-check",
        },
        "path_records_classic_map": records[-12:],
        "gamma_records_shortcut_map": {
            "model_mean_gamma": c_model,
            "model_limsup_gamma_lagarias_weiss": 41.677647,
            "model_record_ones_ratio": 0.609091,
            "records": gamma_records[-10:],
            "note": "records reachable at this N sit far below the predicted limsup; the extreme tail is the least-tested regime of the model",
        },
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=1_000_000)
    ap.add_argument("--depth", type=int, default=24)
    args = ap.parse_args()
    json.dump(run(args.limit, args.depth), sys.stdout, indent=2)
    print()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

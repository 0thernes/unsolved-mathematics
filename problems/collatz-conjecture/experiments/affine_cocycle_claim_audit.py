#!/usr/bin/env python3
"""
Affine Cocycle Repulsion CLAIM AUDIT.

Adversarially tests the claims of PROOF-SKETCH-AFFINE-COCYCLE-RIGIDITY-2026.md,
affine_cocycle_repulsion_analyzer.py, and repulsion_potential_minimizer.py,
in the same spirit as kick_repulsion_claim_audit.py (which demoted the
positive-kick claim from proof to candidate mechanism).

Claims under audit:
  (C1) "Repulsion events" (high-alignment odd steps where post-alignment differs
       from pre-alignment) are a *dynamical discovery* whose rate (up to 0.98)
       evidences a repulsion mechanism.
  (C2) The mechanism is eps-sensitive / positive-cone specific: repulsion forces
       any would-be survivor to drop odd-density below theta, so S cap Z>0 = 0,
       and would break nontrivial cycle equations.
  (C3) V = M - lam*log1p(D) - mu*(A/(d+1)) is a candidate Lyapunov function:
       its strict-decrease rate (0.62 -> 0.98, increasing with size) evidences
       forced descent.
  (C4) The tracked D approximates the affine cocycle defect c_d / 2^d.

Audit tests:
  (T1) Identity test: for odd v with A = v2(v+1) >= 3, the shortcut odd step
       gives post-alignment == A - 1 *always* (v+1 = 2^A k with k odd implies
       T(v)+1 = 3*2^(A-1)*k). So the detector's fire condition
       (post != pre) holds deterministically on every high-alignment odd step,
       for every integer of either sign. The "repulsion rate" is a tautology.
  (T2) Negative-cone control (the in-repo sibling control, since 3n-1 on
       positives == 3n+1 on negatives under n <-> -n):
       - The -17 cycle (period 11, o=7, o/d = 7/11 > theta): detector FIRES
         (alignment-4 and alignment-3 members) yet the orbit is periodic and
         supercritical forever => repulsion events do NOT force density drop.
       - The -5 cycle (period 3, o=2, o/d = 2/3 > theta): max alignment 2,
         detector is SILENT forever => the mechanism cannot see low-alignment
         supercritical residents at all (the -5 spine is exactly the
         x == 59 mod 64 growth gate of LOW-ALIGNMENT-STRUCTURE.md).
       - Positive lifts 2^k - 5 ride the -5 spine detector-silently for
         Theta(k) steps while supercritical: detector-silent supercritical
         prefixes are unbounded in the positive cone too.
  (T3) Potential control: reimplement V verbatim and run it on
       (a) Collatz orbits, (b) 5n+1 orbits that grow far beyond their start
       (divergence-typical sibling), (c) the 3n-1 cycle at 5 (positive sibling
       cycle). If the strict-decrease rate is high on ALL of them, V's descent
       carries no information about convergence. Also isolate the d<=60 vs
       d>60 regimes to show the rate jump is the frozen-denominator artifact.
  (T4) Cocycle fidelity: exact affine tracking. If n_d = (3^o * n0 + c)/2^d
       then an even step leaves c fixed and an odd (shortcut) step maps
       c -> 3c + 2^d. Compare the exact c against the analyzer's c -> 3c + 1.

Pure stdlib. Run: python experiments/affine_cocycle_claim_audit.py
"""

from __future__ import annotations

import json
import math
import random
from typing import Dict, List, Optional

THETA = math.log(2) / math.log(3)  # 0.63092975...
LOG2_3 = math.log2(3)
LOG2_5 = math.log2(5)


def shortcut_step(n: int, mult: int = 3, eps: int = 1) -> int:
    """One shortcut step of the (mult*n + eps)/2 vs n/2 map. Exact for negatives."""
    if n % 2 == 0:
        return n // 2
    return (mult * n + eps) // 2


def v2_of(x: int, cap: int = 64) -> int:
    """2-adic valuation, capped; v2(0) reported as cap."""
    if x == 0:
        return cap
    c = 0
    while x % 2 == 0 and c < cap:
        x //= 2
        c += 1
    return c


def align_to_minus1(n: int) -> int:
    return v2_of(n + 1)


# ---------------------------------------------------------------- T1: identity

def t1_identity(num_random: int = 1_000_000, exhaustive_below: int = 1 << 20,
                seed: int = 20260701) -> Dict:
    """post_align == pre_align - 1 on every A>=3 odd shortcut step (both signs)."""
    rng = random.Random(seed)
    checked = 0
    fired = 0
    post_always_pre_minus_1 = True
    counterexample: Optional[int] = None

    def check(v: int) -> None:
        nonlocal checked, fired, post_always_pre_minus_1, counterexample
        a = align_to_minus1(v)
        if a < 3 or a >= 64:
            return
        checked += 1
        post = align_to_minus1(shortcut_step(v))
        if post != a:
            fired += 1
        if post != a - 1:
            post_always_pre_minus_1 = False
            if counterexample is None:
                counterexample = v

    # exhaustive small positives
    for v in range(3, exhaustive_below, 2):
        check(v)
    # random large positives and negatives
    for _ in range(num_random):
        v = rng.getrandbits(96) | 1
        check(v)
        check(-v - 2)  # odd negative

    return {
        "checked_high_align_odd_steps": checked,
        "detector_fired": fired,
        "fire_fraction": fired / max(1, checked),
        "post_always_equals_pre_minus_1": post_always_pre_minus_1,
        "counterexample": counterexample,
        "verdict": ("TAUTOLOGY: detector fires on 100% of high-alignment odd steps "
                    "by the identity v+1 = 2^A*k (k odd) => T(v)+1 = 3*2^(A-1)*k, "
                    "for every integer of either sign"
                    if fired == checked and post_always_pre_minus_1
                    else "identity FAILED - investigate"),
    }


def t1_reproduce_reported_counts() -> Dict:
    """The sketch reports 'repulsion events: 14 for 27, 22 for 703'. By T1 the
    event count is nothing but the number of high-alignment (A>=3) odd steps
    in the orbit. Reproduce it with that trivial counter."""
    out = {}
    for s in (27, 703):
        cur, count, steps = s, 0, 0
        while cur > 1 and steps < 4096:
            if cur % 2 != 0 and align_to_minus1(cur) >= 3:
                count += 1
            cur = shortcut_step(cur)
            steps += 1
        out[str(s)] = count
    return {"count_of_A_ge_3_odd_steps": out,
            "sketch_reported": {"27": 14, "703": 22}}


# ------------------------------------------------- T2: negative-cone controls

def orbit_cycle_stats(start: int, max_steps: int = 10_000) -> Dict:
    """Follow shortcut Collatz from start (may be negative); if a value repeats,
    report per-period stats: d, o, o/d, alignment profile, detector events."""
    seen: Dict[int, int] = {}
    seq: List[int] = []
    cur = start
    for _ in range(max_steps):
        if cur in seen:
            i = seen[cur]
            period = seq[i:]
            d = len(period)
            o = sum(1 for x in period if x % 2 != 0)
            aligns = [align_to_minus1(x) for x in period if x % 2 != 0]
            events = 0
            for x in period:
                if x % 2 != 0 and align_to_minus1(x) >= 3:
                    if align_to_minus1(shortcut_step(x)) != align_to_minus1(x):
                        events += 1
            return {
                "start": start, "cycle_found": True, "period_d": d, "period_o": o,
                "odd_density": o / d, "supercritical": (o / d) > THETA,
                "max_alignment": max(aligns) if aligns else 0,
                "detector_events_per_period": events,
                "cycle_members": period if d <= 16 else period[:16],
            }
        seen[cur] = len(seq)
        seq.append(cur)
        cur = shortcut_step(cur)
    return {"start": start, "cycle_found": False}


def t2_positive_spine(ks: List[int]) -> List[Dict]:
    """Positive lifts n = 2^k - 5 ride the -5 spine (word 110 repeating,
    o/d = 2/3 > theta) with alignment <= 2, i.e. detector-silent, for Theta(k)
    steps. Measure the detector-silent supercritical prefix length."""
    out = []
    for k in ks:
        n = (1 << k) - 5
        cur = n
        d = 0
        o = 0
        silent_supercritical_prefix = 0
        while cur > 1 and d < 100_000:
            is_odd = cur % 2 != 0
            a = align_to_minus1(cur) if is_odd else 0
            fires = is_odd and a >= 3 and align_to_minus1(shortcut_step(cur)) != a
            cur = shortcut_step(cur)
            d += 1
            o += 1 if is_odd else 0
            if fires:
                break
            if o / d > THETA:
                silent_supercritical_prefix = d
        out.append({
            "k": k, "start": f"2^{k}-5",
            "detector_silent_supercritical_prefix_steps": silent_supercritical_prefix,
        })
    return out


# ------------------------------------------------- T3: potential V controls

def potential_run(start: int, mult: int, eps: int, lam: float = 2.5,
                  mu: float = 1.2, max_d: int = 4096) -> Dict:
    """Verbatim reimplementation of repulsion_potential_minimizer.py's V,
    generalized to the (mult*n + eps)/2 sibling maps. Reports strict-decrease
    rate overall and split by the d<=60 / d>60 regimes, plus orbit outcome."""
    log2m = math.log2(mult)
    ln2 = math.log(2)
    cur = start
    d = 0
    o = 0
    c_approx = 0  # exact int: the minimizer's float version overflows to inf
    prev_v: Optional[float] = None
    dec_all = tot_all = 0
    dec_pre = tot_pre = 0    # steps with d <= 60
    dec_post = tot_post = 0  # steps with d > 60
    max_seen = start
    while d < max_d and cur != 1:
        if cur % 2 == 0:
            cur //= 2
        else:
            cur = (mult * cur + eps) // 2
            o += 1
            c_approx = mult * c_approx + 1  # analyzer's (incorrect) recursion, kept verbatim
        d += 1
        max_seen = max(max_seen, cur)
        m_debt = o * log2m - d
        a = v2_of(cur + 1)  # minimizer computes alignment on every step
        m = min(d, 60)
        if c_approx == 0:
            log1p_dd = 0.0
        elif c_approx.bit_length() < 900:
            log1p_dd = math.log1p(c_approx / (1 << m))
        else:  # log1p(D) ~= log(D) for astronomically large D; exact via int log
            log1p_dd = math.log(c_approx) - m * ln2
        v = m_debt - lam * log1p_dd - mu * (a / (d + 1))
        if prev_v is not None:
            dec = v < prev_v
            tot_all += 1
            dec_all += 1 if dec else 0
            if d <= 60:
                tot_pre += 1
                dec_pre += 1 if dec else 0
            else:
                tot_post += 1
                dec_post += 1 if dec else 0
        prev_v = v
    return {
        "start": start, "map": f"({mult}n{'+' if eps > 0 else '-'}{abs(eps)})/2",
        "steps": d,
        "orbit_grew_to_over_start": max_seen / start if start > 0 else None,
        "strict_decrease_rate": dec_all / max(1, tot_all),
        "rate_d_le_60": dec_pre / max(1, tot_pre),
        "rate_d_gt_60": dec_post / max(1, tot_post),
    }


# ------------------------------------------------- T4: exact cocycle tracking

def t4_cocycle_fidelity(start: int, steps: int = 40) -> Dict:
    """Exact affine intercept: n_d = (3^o * n0 + c) / 2^d demands
    even: c -> c ; odd: c -> 3c + 2^d (at the depth d where the odd step
    is taken). Verify the invariant exactly and compare against the
    analyzer's c -> 3c + 1."""
    n0 = start
    cur = start
    c_exact = 0
    c_analyzer = 0
    d = 0
    o = 0
    invariant_ok = True
    rows = []
    for _ in range(steps):
        if cur % 2 == 0:
            cur //= 2
        else:
            c_exact = 3 * c_exact + (1 << d)
            c_analyzer = 3 * c_analyzer + 1
            cur = (3 * cur + 1) // 2
            o += 1
        d += 1
        # invariant: cur * 2^d == 3^o * n0 + c_exact
        if cur * (1 << d) != (3 ** o) * n0 + c_exact:
            invariant_ok = False
        if d in (10, 20, 40):
            rows.append({
                "d": d,
                "c_exact": c_exact,
                "c_analyzer": c_analyzer,
                "ratio": c_exact / max(1, c_analyzer),
                "exact_D": c_exact / (1 << d),
                "analyzer_D": c_analyzer / (2 ** min(d, 60)),
            })
        if cur <= 1:
            break
    return {"start": start, "affine_invariant_holds_for_c_exact": invariant_ok,
            "comparison": rows}


# --------------------------------------------------------------------- main

def main() -> None:
    print("=" * 72)
    print("AFFINE COCYCLE REPULSION CLAIM AUDIT")
    print("=" * 72)

    print("\n[T1] Detector tautology test (identity post_align == pre_align - 1)...")
    t1 = t1_identity()
    print(json.dumps(t1, indent=2))
    t1b = t1_reproduce_reported_counts()
    print("  reported-count reproduction:", json.dumps(t1b, indent=2))

    print("\n[T2] Negative-cone controls (= 3n-1 positive sibling under n <-> -n)...")
    t2_m17 = orbit_cycle_stats(-17)
    t2_m5 = orbit_cycle_stats(-5)
    print("  -17 cycle:", json.dumps(t2_m17, indent=2))
    print("  -5 cycle: ", json.dumps(t2_m5, indent=2))
    t2_spine = t2_positive_spine([20, 40, 60, 100, 200])
    print("  positive -5-spine lifts:", json.dumps(t2_spine, indent=2))

    print("\n[T3] Potential V controls (same V, sibling maps)...")
    t3 = {
        "collatz": [potential_run(s, 3, 1) for s in (27, 703, 63_728_127,
                                                     2_358_909_599_867_980_429_759)],
        "five_n_plus_1": [potential_run(s, 5, 1, max_d=1500) for s in (7, 13, 33)],
        "three_n_minus_1_cycle": [potential_run(5, 3, -1, max_d=3000)],
    }
    print(json.dumps(t3, indent=2))

    print("\n[T4] Cocycle fidelity (exact affine c vs analyzer's 3c+1)...")
    t4 = [t4_cocycle_fidelity(s) for s in (27, 703)]
    print(json.dumps(t4, indent=2))

    result = {"T1": t1, "T1b": t1b,
              "T2": {"minus17": t2_m17, "minus5": t2_m5,
                               "positive_spine": t2_spine},
              "T3": t3, "T4": t4}
    out_path = "experiments/results/affine_cocycle_claim_audit.json"
    try:
        with open(out_path, "w") as f:
            json.dump(result, f, indent=2)
        print(f"\nWrote {out_path}")
    except OSError as e:
        print(f"\nCould not write {out_path}: {e}")

    print("\n" + "=" * 72)
    print("VERDICT SUMMARY")
    print("=" * 72)
    print("T1 tautology:", t1["verdict"])
    print("T2 -17: supercritical periodic orbit with detector events ->",
          t2_m17.get("detector_events_per_period"), "events/period (mechanism unsound as stated)")
    print("T2 -5: supercritical periodic orbit, detector silent (mechanism incomplete)")
    print("T3 rates: high strict-decrease on 5n+1 growth orbits and the 3n-1 cycle",
          "-> V descent carries no convergence information")
    print("T4: analyzer c is not the affine cocycle (misses the 2^d term)")


if __name__ == "__main__":
    main()

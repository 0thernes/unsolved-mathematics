#!/usr/bin/env python3
"""
Spine Ladder Lab.

Unifies the -1 identity (AFFINE-COCYCLE-CLAIM-AUDIT: T(v)+1 = 3(v+1)/2) and the
-5 repeat-gate law (LOW-ALIGNMENT-STRUCTURE: T^3(x)+5 = 9(x+5)/8) into one exact
lemma, verifies it exhaustively over all supercritical periodic words of length
<= 12, and measures the one quantity the lemma does NOT control (alignment
regeneration after spine exit) as honest data.

SPINE LADDER LEMMA.
Let w be a parity word of length d with o odd letters, realized by the unique
residue r_w mod 2^d (x follows w for its first d shortcut steps iff
x ≡ r_w mod 2^d). Running T^d on the cylinder is exact-affine:
    T^d(x) = (3^o x + c(w)) / 2^d,   c(w) from c -> 3c + 2^(depth) at odd steps.
Let rho_w = c(w) / (2^d - 3^o)  (well-defined in Z_2: the denominator is odd).
Then F_w(rho_w) = rho_w, rho_w ≡ r_w mod 2^d, and for every x ≡ r_w mod 2^d:

    T^d(x) - rho_w = (3^o / 2^d) * (x - rho_w).

Consequences:
  (L1) v2(T^d(x) - rho) = v2(x - rho) - d      [ladder: d bits burned per block]
  (L2) |T^d(x) - rho| = (3^o/2^d) |x - rho|    [supercritical => distance grows]
  (L3) If w is supercritical (3^o > 2^d) then rho_w <= -1: c(w) > 0 and
       2^d - 3^o < 0, so rho_w is a NEGATIVE rational. Positive integers are
       therefore never spine points; they can only visit spine cylinders
       transiently, for ~v2(x - rho) steps, while their value is multiplied by
       (3^o/2^d)^(blocks).
  (L4) The ladder is sign-blind (holds verbatim for negative x), so no argument
       consuming only ladder/alignment data can separate the positive cone —
       the spine-ladder generalization of the audit's F1/F2 barrier.

What the lemma does NOT control (the open seam, measured below): after a
positive orbit exits a spine cylinder, the alignment it regenerates to any
spine is v2 of an explicit affine expression in 3^j*(x - rho) — i.e., the
divergence half reduces to 2-adic digit control of powers of 3, which is
exactly the hard wall, now stated as an exact local law instead of a heuristic.

Pure stdlib. Run: python experiments/spine_ladder_lab.py
"""

from __future__ import annotations

import json
import math
import random
from fractions import Fraction
from typing import Dict, List, Optional, Tuple

THETA = math.log(2) / math.log(3)


def shortcut_step_frac(x: Fraction) -> Tuple[Fraction, int]:
    """Shortcut T on rationals with odd denominator; parity = parity of the
    2-adic reduction (numerator*inverse(denominator) mod 2)."""
    num, den = x.numerator, x.denominator
    assert den % 2 == 1
    parity = (num * pow(den, -1, 2)) % 2  # den odd => invertible mod 2
    if parity == 0:
        return x / 2, 0
    return (3 * x + 1) / 2, 1


def v2_frac(x: Fraction, cap: int = 4096) -> int:
    """2-adic valuation of a rational with odd denominator (v2 = v2(numerator))."""
    if x == 0:
        return cap
    num = abs(x.numerator)
    c = 0
    while num % 2 == 0 and c < cap:
        num //= 2
        c += 1
    return c


def word_data(w: str) -> Dict:
    """For parity word w: exact affine data (3^o, c), cylinder residue r_w,
    and spine point rho_w."""
    d = len(w)
    o = w.count("1")
    # exact affine: value*2^d = 3^o * x + c along the word
    c = 0
    oo = 0
    for depth, bit in enumerate(w):
        if bit == "1":
            c = 3 * c + (1 << depth)
            oo += 1
    assert oo == o
    # cylinder residue: unique r mod 2^d whose first d parities equal w,
    # built by 2-adic lifting on the exact affine chain value_i = (3^oo x + cc)/2^i:
    # parity constraint at step i is 3^oo * x + cc ≡ w_i * 2^i (mod 2^{i+1});
    # adding 2^i to x flips that residue by odd*2^i, so each bit is forced.
    r = 0
    cc = 0
    oo2 = 0
    for i, bit in enumerate(w):
        b = int(bit)
        mod = 1 << (i + 1)
        lhs = (pow(3, oo2, mod) * r + cc) % mod
        if lhs != (b << i) % mod:
            r += 1 << i
        if b:
            cc = 3 * cc + (1 << i)
            oo2 += 1
    rho = Fraction(c, (1 << d) - 3 ** o)
    return {"w": w, "d": d, "o": o, "c": c, "r": r, "rho": rho}


def canonical_necklace(w: str) -> str:
    return min(w[i:] + w[:i] for i in range(len(w)))


def enumerate_supercritical_words(max_d: int = 12) -> List[Dict]:
    """All parity words w (1 <= |w| <= max_d) that are supercritical
    (3^o > 2^d) as periodic blocks; dedupe nothing here (each rotation is its
    own spine), but tag the necklace class."""
    out = []
    for d in range(1, max_d + 1):
        for m in range(1 << d):
            w = format(m, f"0{d}b")
            o = w.count("1")
            if 3 ** o > (1 << d):
                out.append(w)
    return out


def verify_lemma(max_d: int = 12, samples_per_word: int = 20,
                 seed: int = 20260701) -> Dict:
    """Exhaustive verification of the lemma over all supercritical words
    d <= max_d: fixed point, cylinder membership, exact ladder on random
    integers of both signs, v2 drop, distance growth, rho <= -1."""
    rng = random.Random(seed)
    words = enumerate_supercritical_words(max_d)
    necklaces = {}
    integer_spines = []
    failures = []
    checked_ladder = 0
    for w in words:
        info = word_data(w)
        d, o, c, r, rho = info["d"], info["o"], info["c"], info["r"], info["rho"]
        nk = canonical_necklace(w)
        necklaces.setdefault(nk, 0)
        necklaces[nk] += 1
        # (i) fixed point: F_w(rho) == rho
        if (3 ** o * rho + c) / (1 << d) != rho:
            failures.append((w, "fixed-point"))
            continue
        # (ii) rho is in the cylinder: rho ≡ r mod 2^d (2-adically)
        rho_mod = (rho.numerator * pow(rho.denominator, -1, 1 << d)) % (1 << d)
        if r is None or rho_mod != r:
            failures.append((w, f"cylinder r={r} rho_mod={rho_mod}"))
            continue
        # (iii) supercritical => rho <= -1 and c > 0
        if not (c > 0 and rho <= -1):
            failures.append((w, f"positivity c={c} rho={rho}"))
            continue
        if rho == Fraction(-1) or rho.denominator == 1:
            integer_spines.append((w, int(rho)))
        # (iv) exact ladder on random integers of both signs in the cylinder
        for _ in range(samples_per_word):
            q = rng.randrange(-(1 << 40), (1 << 40))
            x = r + q * (1 << d)
            xf = Fraction(x)
            # run d shortcut steps, checking the word is actually followed
            cur, followed = xf, True
            for bit in w:
                cur, par = shortcut_step_frac(cur)
                if par != int(bit):
                    followed = False
                    break
            if not followed:
                failures.append((w, f"cylinder-sim x={x}"))
                continue
            lhs = cur - rho
            rhs = Fraction(3 ** o, 1 << d) * (xf - rho)
            if lhs != rhs:
                failures.append((w, f"ladder x={x}"))
                continue
            if x != rho and v2_frac(lhs) != v2_frac(xf - rho) - d:
                failures.append((w, f"v2-drop x={x}"))
                continue
            checked_ladder += 1
    return {
        "max_d": max_d,
        "supercritical_words": len(words),
        "necklace_classes": len(necklaces),
        "ladder_checks": checked_ladder,
        "failures": failures[:10],
        "num_failures": len(failures),
        "integer_spines_found": sorted({v for _, v in integer_spines}),
        "all_rho_le_minus1": not any(f[1].startswith("positivity") for f in failures),
    }


def expulsion_demo(seed: int = 7) -> List[Dict]:
    """(L1)+(L2) in action: positive lifts x = rho + 2^m (deep in the cylinder)
    burn their alignment in ~m steps while the distance to the spine grows by
    exactly (3^o/2^d) per block. Demonstrated on the three integer spines."""
    demos = []
    # -17 cycle members: -17,-25,-37,-55,-82,-41,-61,-91,-136,-68,-34
    # parities:            1   1   1   1   0   1   1   1    0   0   0
    for w, rho_int in (("1", -1), ("110", -5), ("11110111000", -17)):
        info = word_data(w)
        d, o = info["d"], info["o"]
        rho = Fraction(rho_int)
        for m in (24, 48, 96):
            x = rho_int + (1 << m)  # v2(x - rho) = m exactly
            xf = Fraction(x)
            blocks = 0
            cur = xf
            ok = True
            while v2_frac(cur - rho) >= d:
                for bit in w:
                    cur, par = shortcut_step_frac(cur)
                    if par != int(bit):
                        ok = False
                        break
                if not ok:
                    break
                blocks += 1
            expect_blocks = m // d
            growth_exact = (abs(cur - rho) ==
                            Fraction(3 ** o, 1 << d) ** blocks * abs(xf - rho))
            demos.append({
                "spine": rho_int, "word": w, "m": m,
                "blocks_ridden": blocks, "predicted": expect_blocks,
                "match": blocks == expect_blocks and ok and growth_exact,
                "distance_growth_exact": growth_exact,
                "growth_factor": float(Fraction(3 ** o, 1 << d) ** blocks),
            })
    return demos


def regeneration_scan(n_max: int = 100_000, max_steps: int = 5000) -> Dict:
    """The OPEN quantity: after leaving its seed alignment, how much alignment
    to the integer spines (-1, -5, -17) does a positive orbit regenerate?
    The lemma bounds nothing here; the 2-adic measure model predicts
    P(regen >= m) ~ 2^-m. Report the tail and the max, as calibration data."""
    spines = (1, 5, 17)  # measure v2(x + s)
    max_regen = {s: 0 for s in spines}
    argmax = {s: 0 for s in spines}
    tail_counts = {s: [0] * 40 for s in spines}
    orbits = 0
    for n in range(3, n_max + 1, 2):
        orbits += 1
        cur = n
        steps = 0
        first = True
        while cur > 1 and steps < max_steps:
            if not first:  # exclude the seed's own alignment
                for s in spines:
                    t = cur + s
                    a = 0
                    while t % 2 == 0 and a < 39:
                        t //= 2
                        a += 1
                    if a > max_regen[s]:
                        max_regen[s] = a
                        argmax[s] = n
                    tail_counts[s][a] += 1
            first = False
            cur = (3 * cur + 1) // 2 if cur % 2 else cur // 2
            steps += 1
    # geometric-tail check at a few levels
    total_states = {s: sum(tail_counts[s]) for s in spines}
    tails = {s: {m: sum(tail_counts[s][m:]) / max(1, total_states[s])
                 for m in (8, 12, 16, 20)} for s in spines}
    return {
        "odd_starts": orbits,
        "max_regenerated_alignment": max_regen,
        "achieved_by_start": argmax,
        "tail_P_ge_m": {str(s): {str(m): t for m, t in tails[s].items()}
                        for s in spines},
        "geometric_prediction_2^-m": {"8": 2 ** -8, "12": 2 ** -12,
                                      "16": 2 ** -16, "20": 2 ** -20},
        "note": ("bit-length of scan bound is ~17, so seed-independent "
                 "regeneration beyond ~17+log2(orbit length) would be anomalous; "
                 "the lemma provides no bound here - this is the open seam"),
    }


def main() -> None:
    print("=" * 72)
    print("SPINE LADDER LAB")
    print("=" * 72)

    print("\n[1] Lemma verification over all supercritical words, d <= 12...")
    lemma = verify_lemma()
    print(json.dumps(lemma, indent=2, default=str))

    print("\n[2] Expulsion bookkeeping on the integer spines (-1, -5, -17)...")
    demo = expulsion_demo()
    print(json.dumps(demo, indent=2))

    print("\n[3] Alignment regeneration scan (the open, uncontrolled quantity)...")
    regen = regeneration_scan()
    print(json.dumps(regen, indent=2))

    out = {"lemma": {k: (v if k != "failures" else [str(f) for f in v])
                     for k, v in lemma.items()},
           "expulsion": demo, "regeneration": regen}
    path = "experiments/results/spine_ladder_lab.json"
    with open(path, "w") as f:
        json.dump(out, f, indent=2, default=str)
    print(f"\nWrote {path}")

    print("\nSUMMARY")
    print(f"  words checked: {lemma['supercritical_words']} "
          f"({lemma['necklace_classes']} necklace classes), "
          f"ladder checks: {lemma['ladder_checks']}, "
          f"failures: {lemma['num_failures']}")
    print(f"  integer spines found (d<=12): {lemma['integer_spines_found']}")
    print(f"  all supercritical rho <= -1: {lemma['all_rho_le_minus1']}")
    print(f"  expulsion predictions matched: {all(x['match'] for x in demo)}")
    print(f"  max regenerated alignment: {regen['max_regenerated_alignment']}")


if __name__ == "__main__":
    main()

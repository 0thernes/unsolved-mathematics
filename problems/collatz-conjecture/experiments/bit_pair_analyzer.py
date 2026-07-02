#!/usr/bin/env python3
"""Bit-pair structure analyzer: investigate the pairing symmetry in survivor bits.

The modular constraint analysis revealed that survivor residue bits come in
pairs with identical entropy: bits (2,3), (4,5), etc. This instrument
investigates the algebraic origin of this pairing.

Key questions:
1. Are paired bits perfectly correlated, or just identically distributed?
2. Does the pairing persist across depths?
3. Is there a 2-adic symmetry (e.g., r -> some_function(r)) that exchanges
   paired bits?
4. Can we derive the pairing from the algebraic formula r = -c(w) * 3^{-o} mod 2^d?
"""

from __future__ import annotations

import json
import math
from collections import Counter
from time import perf_counter


def shortcut(n: int) -> int:
    return (3 * n + 1) // 2 if n & 1 else n // 2


def enumerate_survivor_residues(depth: int) -> list[int]:
    pow3 = [1]
    for _ in range(depth):
        pow3.append(pow3[-1] * 3)
    live = [0]
    live_odd = [0]
    live_img = [0]
    for d in range(depth):
        nd = d + 1
        bit = 1 << d
        next_live = []
        next_odd = []
        next_img = []
        for r, oc, img in zip(live, live_odd, live_img):
            for hb in (0, 1):
                nr = r + (bit if hb else 0)
                img_before = img + (pow3[oc] if hb else 0)
                is_odd = img_before & 1
                noc = oc + is_odd
                nimg = shortcut(img_before)
                if pow3[noc] >= (1 << nd):
                    next_live.append(nr)
                    next_odd.append(noc)
                    next_img.append(nimg)
        live = next_live
        live_odd = next_odd
        live_img = next_img
    return sorted(live)


def bit_pair_correlations(residues: list[int], depth: int) -> dict[str, object]:
    """Compute the joint distribution and correlation of each pair of adjacent bits."""
    n = len(residues)
    if n == 0:
        return {}
    pairs = []
    for j in range(0, depth - 1):
        # Bits j and j+1
        joint = Counter()
        for r in residues:
            b_j = (r >> j) & 1
            b_j1 = (r >> (j + 1)) & 1
            joint[(b_j, b_j1)] += 1
        # Marginals
        p00 = joint.get((0, 0), 0) / n
        p01 = joint.get((0, 1), 0) / n
        p10 = joint.get((1, 0), 0) / n
        p11 = joint.get((1, 1), 0) / n
        p_j1 = p10 + p11  # P(bit j = 1)
        p_j1_1 = p01 + p11  # P(bit j+1 = 1)
        # Correlation
        if p_j1 > 0 and p_j1_1 > 0 and p_j1 < 1 and p_j1_1 < 1:
            cov = p11 - p_j1 * p_j1_1
            var_j = p_j1 * (1 - p_j1)
            var_j1 = p_j1_1 * (1 - p_j1_1)
            corr = cov / (var_j ** 0.5 * var_j1 ** 0.5) if var_j > 0 and var_j1 > 0 else 0.0
        else:
            corr = 0.0
        # Test if marginals are equal
        marginals_equal = abs(p_j1 - p_j1_1) < 1e-10
        pairs.append({
            "bit_pair": (j, j + 1),
            "p00": p00, "p01": p01, "p10": p10, "p11": p11,
            "p_bit_j_1": p_j1,
            "p_bit_j1_1": p_j1_1,
            "marginals_equal": marginals_equal,
            "correlation": corr,
            "identical_distribution": abs(p_j1 - p_j1_1) < 1e-6,
        })
    return {"pairs": pairs}


def bit_pair_xor_analysis(residues: list[int], depth: int) -> dict[str, object]:
    """Analyze the XOR of adjacent bit pairs.

    If bits j and j+1 are always equal, XOR = 0 always.
    If they're independent, XOR has entropy 1.
    """
    n = len(residues)
    if n == 0:
        return {}
    xor_entropies = []
    for j in range(0, depth - 1):
        xor_ones = sum(((r >> j) & 1) ^ ((r >> (j + 1)) & 1) for r in residues)
        p_xor1 = xor_ones / n
        if p_xor1 == 0 or p_xor1 == 1:
            h = 0.0
        else:
            h = -p_xor1 * math.log2(p_xor1) - (1 - p_xor1) * math.log2(1 - p_xor1)
        xor_entropies.append({"bit_pair": (j, j + 1), "xor_entropy": h, "p_xor1": p_xor1})
    return {"xor_entropies": xor_entropies}


def two_adic_symmetry_check(residues: list[int], depth: int) -> dict[str, object]:
    """Check if the survivor set has a 2-adic symmetry.

    Test: is the map r -> r XOR 0b1100 (flipping bits 2 and 3) a bijection
    on the survivor set? If so, this explains the bit 2,3 pairing.

    Also test: r -> (r * 3) mod 2^d (2-adic multiplication by 3)
    """
    n = len(residues)
    mod = 1 << depth
    if n == 0:
        return {}

    residue_set = set(residues)

    # Test bit-flip symmetries for each pair
    symmetries = {}
    for j in range(2, min(depth, 10)):
        flip_mask = 1 << j
        flipped = set(r ^ flip_mask for r in residues)
        overlap = len(flipped & residue_set)
        symmetries[f"flip_bit_{j}"] = {
            "overlap": overlap,
            "total": n,
            "is_symmetry": overlap == n,
        }

    # Test multiplication by 3 mod 2^d
    multiplied = set((r * 3) % mod for r in residues)
    overlap_mult3 = len(multiplied & residue_set)
    # Test multiplication by 3^{-1} mod 2^d
    inv3 = pow(3, -1, mod)
    multiplied_inv = set((r * inv3) % mod for r in residues)
    overlap_inv3 = len(multiplied_inv & residue_set)

    # Test r -> r + 4 mod 2^d (shift by the fixed-bit width)
    shifted = set((r + 4) % mod for r in residues)
    overlap_shift4 = len(shifted & residue_set)

    return {
        "bit_flip_symmetries": symmetries,
        "mult_by_3": {"overlap": overlap_mult3, "is_symmetry": overlap_mult3 == n},
        "mult_by_3_inv": {"overlap": overlap_inv3, "is_symmetry": overlap_inv3 == n},
        "shift_by_4": {"overlap": overlap_shift4, "is_symmetry": overlap_shift4 == n},
    }


def residue_to_word(residue: int, depth: int) -> list[int]:
    """Compute the parity word of a residue."""
    x = residue
    word = []
    for _ in range(depth):
        word.append(x & 1)
        x = shortcut(x)
    return word


def word_to_residue(word: list[int], depth: int) -> int:
    """Compute the residue from a parity word using the algebraic formula.

    r = -c(w) * 3^{-o} mod 2^d
    """
    mod = 1 << depth
    # Compute intercept c(w) and odd count o
    # c evolves: c -> c (even step), c -> 3c + 2^j (odd step at position j)
    c = 0
    o = 0
    for j in range(depth):
        if word[j] == 1:  # odd step
            c = 3 * c + (1 << j)
            o += 1
        # even step: c unchanged
    inv3o = pow(3, -o, mod) if o > 0 else 1
    r = (-c * inv3o) % mod
    return r


def verify_bijection(depth: int, residues: list[int]) -> dict[str, object]:
    """Verify the word-to-residue bijection."""
    mod = 1 << depth
    # Map each residue to its word and back
    mismatches = 0
    for r in residues:
        w = residue_to_word(r, depth)
        r2 = word_to_residue(w, depth)
        if r2 != r:
            mismatches += 1
    # Map each survivor word to a residue and check it's in the survivor set
    residue_set = set(residues)
    word_survivors_mapped = 0
    word_survivors_in_set = 0
    # Generate all survivor words (same DP but in word space)
    # Actually, the survivor condition in word space is:
    # 3^{o(j)} >= 2^j for all j <= d, where o(j) = sum of first j bits
    survivor_words = []
    for w in range(1 << depth):
        bits = [(w >> j) & 1 for j in range(depth)]
        o = 0
        survives = True
        for j in range(depth):
            o += bits[j]
            if pow(3, o) < (1 << (j + 1)):
                survives = False
                break
        if survives:
            survivor_words.append(bits)
            r = word_to_residue(bits, depth)
            word_survivors_mapped += 1
            if r in residue_set:
                word_survivors_in_set += 1

    return {
        "depth": depth,
        "residue_count": len(residues),
        "word_survivor_count": len(survivor_words),
        "round_trip_mismatches": mismatches,
        "words_mapped_to_survivors": word_survivors_in_set,
        "bijection_verified": (mismatches == 0 and
                                word_survivors_mapped == len(residues) and
                                word_survivors_in_set == len(residues)),
    }


def analyze_depth(depth: int) -> dict[str, object]:
    t0 = perf_counter()
    residues = enumerate_survivor_residues(depth)
    n = len(residues)
    if n == 0:
        return {"depth": depth, "error": "no survivors"}

    pairs = bit_pair_correlations(residues, depth)
    xor = bit_pair_xor_analysis(residues, depth)
    symmetry = two_adic_symmetry_check(residues, depth) if depth <= 24 else {}
    bijection = verify_bijection(depth, residues) if depth <= 18 else {}

    t_total = perf_counter() - t0

    return {
        "depth": depth,
        "survivor_count": n,
        "time_s": round(t_total, 4),
        "bit_pair_correlations": pairs,
        "xor_analysis": xor,
        "symmetry_check": symmetry,
        "bijection_check": bijection,
    }


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Bit-pair structure analyzer")
    parser.add_argument("--depths", type=str, default="14,16,18,20,22,24")
    parser.add_argument("--json-out", type=str, default=None)
    args = parser.parse_args()

    depths = [int(x) for x in args.depths.split(",")]
    results = []

    for d in depths:
        r = analyze_depth(d)
        results.append(r)
        n = r["survivor_count"]

        print(f"\n=== Depth {d} (S={n}) ===")

        # Bit pair correlations
        pairs = r["bit_pair_correlations"]["pairs"]
        print("Bit pair correlations (first 10):")
        for p in pairs[:10]:
            eq = "=" if p["identical_distribution"] else "!="
            print(f"  bits ({p['bit_pair'][0]:>2d},{p['bit_pair'][1]:>2d}): "
                  f"p1={p['p_bit_j_1']:.4f} {eq} p1={p['p_bit_j1_1']:.4f} "
                  f"corr={p['correlation']:.4f} "
                  f"joint=({p['p00']:.3f},{p['p01']:.3f},{p['p10']:.3f},{p['p11']:.3f})")

        # XOR analysis
        xors = r["xor_analysis"]["xor_entropies"]
        print("XOR entropies (first 10):")
        for x in xors[:10]:
            print(f"  pair ({x['bit_pair'][0]:>2d},{x['bit_pair'][1]:>2d}): "
                  f"H_xor={x['xor_entropy']:.4f} p_xor1={x['p_xor1']:.4f}")

        # Symmetry check
        if r.get("symmetry_check"):
            sym = r["symmetry_check"]
            for name, info in sym.get("bit_flip_symmetries", {}).items():
                if info["is_symmetry"]:
                    print(f"  SYMMETRY: {name} (overlap={info['overlap']}/{info['total']})")
            for name in ["mult_by_3", "mult_by_3_inv", "shift_by_4"]:
                if name in sym:
                    info = sym[name]
                    tag = "SYMMETRY" if info["is_symmetry"] else "no"
                    print(f"  {name}: {tag} (overlap={info['overlap']}/{n})")

        # Bijection check
        if r.get("bijection_check"):
            bj = r["bijection_check"]
            print(f"  Bijection: {bj['bijection_verified']} "
                  f"(residues={bj['residue_count']}, words={bj['word_survivor_count']}, "
                  f"mismatches={bj['round_trip_mismatches']})")

    if args.json_out:
        with open(args.json_out, "w") as f:
            json.dump(results, f, indent=2, default=str)
        print(f"\nResults written to {args.json_out}")


if __name__ == "__main__":
    main()

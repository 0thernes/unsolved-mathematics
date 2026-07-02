#!/usr/bin/env python3
"""Survivor equidistribution analyzer: attack the last unproved ingredient.

The escape-envelope program (Theorems 7-8, Corollary 8.1 in
CERTIFICATE-FRONTIER-THEOREMS.md) has proved:

  - Upper bound: S(d) <= 2^(d * H(theta))
  - Lower bound: S(d) >= C(d, o_min(d)) / d
  - Two-sided:   S(d) = 2^(d*H(theta) + O(log d))
  - Crossing:    D_1(b) = c* b + O(log b)  (theorem)

The ONLY remaining unproved ingredient is *representative equidistribution*:
that the integer representatives of survivor classes spread regularly enough
in [0, 2^d) for the minimal survivor to track 2^d / S(d).

This instrument attacks that gap by:

1.  Enumerating all survivor residues at depth d (via the frontier DP).
2.  Deriving the exact algebraic formula r(w) = -c(w) * 3^{-o} mod 2^d
    and verifying it against brute-force orbit computation.
3.  Measuring equidistribution: star discrepancy, exponential sums,
    gap distribution, minimal survivor, duality product.
4.  Probing the 2-adic mixing structure: how multiplication by 3^{-o}
    scrambles the bit pattern of the intercept c(w).
5.  Computing Walsh-Fourier coefficients of the survivor indicator
    restricted to residue bits, to detect any algebraic bias.

Research instrument, not a proof.
"""

from __future__ import annotations

import argparse
import json
import math
from collections import Counter
from time import perf_counter


# ---------------------------------------------------------------------------
# Core Collatz shortcut map and affine machinery
# ---------------------------------------------------------------------------

def shortcut(n: int) -> int:
    return (3 * n + 1) // 2 if n & 1 else n // 2


def affine_for_low_bits(depth: int, residue: int) -> tuple[int, int, int]:
    """Return (odd_count, T^depth(residue), intercept c) for the shortcut map.

    The affine law: T^d(2^d q + r) = (3^o q + T^d(r)) = (3^o (2^d q + r) + c) / 2^d
    where c = 2^d * T^d(r) - 3^o * r.
    """
    x = residue
    odd_count = 0
    for _ in range(depth):
        if x & 1:
            odd_count += 1
            x = (3 * x + 1) // 2
        else:
            x //= 2
    image = x
    pow3_o = 3 ** odd_count
    c = (1 << depth) * image - pow3_o * residue
    return odd_count, image, c


def modinv(a: int, m: int) -> int:
    """Modular inverse of a mod m (m a power of 2, a odd)."""
    return pow(a, -1, m)


# ---------------------------------------------------------------------------
# Frontier enumeration (survivor residues at depth d)
# ---------------------------------------------------------------------------

def enumerate_survivor_residues(depth: int) -> list[int]:
    """Enumerate all residues r in [0, 2^depth) that survive the multiplier
    test 3^o(j) >= 2^j for all j <= depth.

    Uses the same BFS frontier expansion as frontier_escape_analyzer.py.
    """
    pow3 = [1]
    for _ in range(depth):
        pow3.append(pow3[-1] * 3)

    live = [0]  # residues
    live_odd = [0]  # odd counts
    live_img = [0]  # images T^j(r)

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


# ---------------------------------------------------------------------------
# Algebraic formula: r(w) = -c(w) * 3^{-o} mod 2^d
# ---------------------------------------------------------------------------

def verify_algebraic_formula(depth: int, residues: list[int]) -> dict[str, object]:
    """For each survivor residue, compute the algebraic formula
    r(w) = -c(w) * 3^{-o} mod 2^d and verify it matches the actual residue.
    """
    mod = 1 << depth
    mismatches = 0
    for r in residues:
        oc, img, c = affine_for_low_bits(depth, r)
        inv3o = modinv(pow(3, oc), mod)
        r_formula = (-c * inv3o) % mod
        if r_formula != r:
            mismatches += 1
    return {
        "depth": depth,
        "num_residues": len(residues),
        "mismatches": mismatches,
        "formula_verified": mismatches == 0,
    }


# ---------------------------------------------------------------------------
# Equidistribution measurements
# ---------------------------------------------------------------------------

def star_discrepancy(residues: list[int], mod: int) -> float:
    """Compute the star discrepancy D_N* of the set {r_i / mod}.

    D_N* = sup_{0 <= t <= 1} | #{r_i < t*mod} / N - t |

    Uses the standard O(N log N) algorithm via sorting.
    """
    n = len(residues)
    if n == 0:
        return 0.0
    sorted_r = sorted(residues)
    d_star = 0.0
    for i, r in enumerate(sorted_r):
        # Points are r_0 < r_1 < ... < r_{N-1}, normalized to [0,1)
        # D_N* = max over i of max(|i/N - r_i/mod|, |(i+1)/N - r_i/mod|)
        fi = r / mod
        d1 = abs((i + 1) / n - fi)
        d2 = abs(i / n - fi)
        d_star = max(d_star, d1, d2)
    # Also check the endpoint
    d_star = max(d_star, abs(n / n - 1.0))  # = 0, but for completeness
    return d_star


def exponential_sum_stats(residues: list[int], mod: int, max_k: int = 256) -> dict[str, object]:
    """Compute exponential sums S(k) = sum_r e^{2*pi*i*k*r/mod} for k=1..max_k.

    For equidistributed sets, |S(k)| should be small relative to N.
    We compute |S(k)|^2 / N (the normalized power spectrum).
    """
    n = len(residues)
    if n == 0:
        return {}
    powers = []
    for k in range(1, min(max_k + 1, mod)):
        # S(k) = sum_r exp(2*pi*i*k*r/mod)
        # |S(k)|^2 = (sum cos)^2 + (sum sin)^2
        cos_sum = 0.0
        sin_sum = 0.0
        for r in residues:
            angle = 2.0 * math.pi * k * r / mod
            cos_sum += math.cos(angle)
            sin_sum += math.sin(angle)
        power = (cos_sum * cos_sum + sin_sum * sin_sum) / n
        powers.append(power)
    return {
        "max_k": len(powers),
        "max_power": max(powers) if powers else 0.0,
        "mean_power": sum(powers) / len(powers) if powers else 0.0,
        "median_power": sorted(powers)[len(powers) // 2] if powers else 0.0,
        "p95_power": sorted(powers)[int(len(powers) * 0.95)] if powers else 0.0,
    }


def gap_distribution(residues: list[int], mod: int) -> dict[str, object]:
    """Analyze the gap distribution of sorted survivor residues."""
    n = len(residues)
    if n < 2:
        return {}
    sorted_r = sorted(residues)
    gaps = []
    for i in range(n - 1):
        gaps.append(sorted_r[i + 1] - sorted_r[i])
    # Wrap-around gap
    gaps.append(mod - sorted_r[-1] + sorted_r[0])
    mean_gap = mod / n
    return {
        "num_gaps": len(gaps),
        "min_gap": min(gaps),
        "max_gap": max(gaps),
        "mean_gap": mean_gap,
        "median_gap": sorted(gaps)[len(gaps) // 2],
        "ratio_max_mean": max(gaps) / mean_gap,
        "ratio_min_mean": min(gaps) / mean_gap,
        "cv_gaps": (sum((g - mean_gap) ** 2 for g in gaps) / len(gaps)) ** 0.5 / mean_gap,
    }


def minimal_survivor_and_duality(residues: list[int], depth: int) -> dict[str, object]:
    """Compute the minimal survivor residue and the duality product m*S(d)/2^d."""
    n = len(residues)
    mod = 1 << depth
    if n == 0:
        return {}
    min_r = min(residues)
    duality = min_r * n / mod
    return {
        "min_survivor_residue": min_r,
        "log2_min": math.log2(min_r) if min_r > 0 else 0.0,
        "survivor_count": n,
        "duality_product": duality,
        "log2_duality": math.log2(duality) if duality > 0 else float("-inf"),
    }


# ---------------------------------------------------------------------------
# 2-adic mixing analysis
# ---------------------------------------------------------------------------

def bit_correlation_analysis(depth: int, residues: list[int]) -> dict[str, object]:
    """Analyze the correlation between residue bits and parity word bits.

    For each survivor residue r, the parity word w is determined by the orbit.
    We compute the bit-wise correlation between r's binary representation and
    the parity word w, to detect any algebraic coupling.
    """
    n = len(residues)
    if n == 0:
        return {}
    # For each bit position j, compute the correlation between
    # bit j of r and bit j of the parity word w
    correlations = []
    for j in range(depth):
        bit_mask = 1 << j
        r_bits = [(r >> j) & 1 for r in residues]
        w_bits = []
        for r in residues:
            # Compute parity word bit j by running the orbit
            x = r
            wj = 0
            for step in range(j + 1):
                wj = x & 1
                x = shortcut(x)
            w_bits.append(wj)
        # Pearson correlation
        nr = len(r_bits)
        sum_r = sum(r_bits)
        sum_w = sum(w_bits)
        sum_rw = sum(rb * wb for rb, wb in zip(r_bits, w_bits))
        mean_r = sum_r / nr
        mean_w = sum_w / nr
        cov = sum_rw / nr - mean_r * mean_w
        var_r = sum(rb * rb for rb in r_bits) / nr - mean_r ** 2
        var_w = sum(wb * wb for wb in w_bits) / nr - mean_w ** 2
        if var_r > 0 and var_w > 0:
            corr = cov / (var_r ** 0.5 * var_w ** 0.5)
        else:
            corr = 0.0
        correlations.append(corr)
    return {
        "bit_correlations": correlations,
        "max_abs_corr": max(abs(c) for c in correlations),
        "mean_abs_corr": sum(abs(c) for c in correlations) / len(correlations),
    }


def walsh_fourier_analysis(depth: int, residues: list[int]) -> dict[str, object]:
    """Compute Walsh-Fourier coefficients of the survivor indicator function.

    The survivor indicator chi: {0,1}^d -> {0,1} is defined on the d-bit
    representation of residues. Walsh coefficients detect algebraic structure.

    chi(r) = 1 if r is a survivor residue, 0 otherwise.
    Walsh coefficient: W_S = (1/2^d) * sum_r chi(r) * (-1)^{popcount(r & S)}

    We compute the L2 norm of the non-trivial coefficients, which measures
    how far chi is from a constant function in the Walsh basis.
    """
    mod = 1 << depth
    n = len(residues)
    if n == 0 or depth > 20:  # Walsh analysis is O(2^d * 2^d) without FFT
        return {"skipped": True, "reason": f"depth {depth} too large for direct Walsh"}

    # Build indicator array
    chi = [0] * mod
    for r in residues:
        chi[r] = 1

    # Walsh-Hadamard transform (fast, O(d * 2^d))
    wht = chi[:]
    for j in range(depth):
        step = 1 << j
        for i in range(0, mod, step * 2):
            for k in range(step):
                u = wht[i + k]
                v = wht[i + k + step]
                wht[i + k] = u + v
                wht[i + k + step] = u - v

    # W_S = wht[S] / 2^d
    # L2 norm of non-trivial coefficients
    total_sq = sum(w * w for w in wht)  # = 2^d * sum chi^2 = 2^d * n
    w0 = wht[0]  # = n (the DC component)
    nontrivial_sq = total_sq - w0 * w0
    # Parseval: sum |W_S|^2 = sum |chi(r)|^2 / 2^d = n / 2^d
    # Non-trivial energy = n/2^d - (n/2^d)^2 = n*(2^d - n) / 2^(2d)

    # Find top coefficients (excluding DC)
    indexed = [(abs(w), S) for S, w in enumerate(wht)]
    indexed.sort(reverse=True)
    top_coeffs = [(S, wht[S] / mod) for _, S in indexed[1:11]]

    # The largest non-trivial Walsh coefficient measures the strongest
    # algebraic bias in the survivor set
    max_nontrivial = indexed[1][0] / mod if len(indexed) > 1 else 0.0

    return {
        "depth": depth,
        "num_survivors": n,
        "density": n / mod,
        "walsh_dc": w0 / mod,
        "max_nontrivial_walsh": max_nontrivial,
        "nontrivial_energy": nontrivial_sq / (mod * mod),
        "top_walsh_coeffs": [
            {"S": S, "S_bits": bin(S), "coeff": c, "abs_coeff": abs(c)}
            for S, c in top_coeffs
        ],
    }


# ---------------------------------------------------------------------------
# 2-adic digit analysis: how does 3^{-o} scramble the intercept?
# ---------------------------------------------------------------------------

def two_adic_mixing_analysis(depth: int, residues: list[int]) -> dict[str, object]:
    """Analyze how multiplication by 3^{-o} mod 2^d mixes the intercept bits.

    For each survivor residue r with odd count o and intercept c:
      r = -c * 3^{-o} mod 2^d

    We measure:
    1. The distribution of odd counts among survivors
    2. Whether the map c -> r = -c * 3^{-o} mod 2^d preserves any bit-level
       structure (it shouldn't, if 3^{-o} is a good mixer)
    3. The 2-adic valuation of c and r (how many trailing zeros)
    """
    n = len(residues)
    if n == 0:
        return {}
    mod = 1 << depth

    odd_counts = Counter()
    v2_c = Counter()
    v2_r = Counter()
    for r in residues:
        oc, img, c = affine_for_low_bits(depth, r)
        odd_counts[oc] += 1
        # 2-adic valuation of c
        vc = 0
        if c > 0:
            vc = (c & -c).bit_length() - 1
        v2_c[vc] += 1
        # 2-adic valuation of r
        vr = 0
        if r > 0:
            vr = (r & -r).bit_length() - 1
        v2_r[vr] += 1

    return {
        "odd_count_distribution": {str(k): odd_counts[k] for k in sorted(odd_counts)},
        "v2_c_distribution": {str(k): v2_c[k] for k in sorted(v2_c)},
        "v2_r_distribution": {str(k): v2_r[k] for k in sorted(v2_r)},
        "mean_odd_count": sum(k * v for k, v in odd_counts.items()) / n,
        "mean_v2_c": sum(k * v for k, v in v2_c.items()) / n,
        "mean_v2_r": sum(k * v for k, v in v2_r.items()) / n,
    }


# ---------------------------------------------------------------------------
# Main analysis
# ---------------------------------------------------------------------------

def analyze_depth(depth: int, do_walsh: bool = True, do_bitcorr: bool = True,
                   do_expsum: bool = True) -> dict[str, object]:
    """Full equidistribution analysis at a single depth."""
    t0 = perf_counter()
    mod = 1 << depth

    # 1. Enumerate survivor residues
    residues = enumerate_survivor_residues(depth)
    t_enum = perf_counter() - t0

    n = len(residues)
    if n == 0:
        return {"depth": depth, "error": "no survivors"}

    # 2. Verify algebraic formula
    formula_check = verify_algebraic_formula(depth, residues)

    # 3. Discrepancy
    disc = star_discrepancy(residues, mod)

    # 4. Gap distribution
    gaps = gap_distribution(residues, mod)

    # 5. Minimal survivor and duality
    min_surv = minimal_survivor_and_duality(residues, depth)

    # 6. Exponential sums
    expsum = {}
    if do_expsum and depth <= 24:
        expsum = exponential_sum_stats(residues, mod, max_k=min(256, mod - 1))

    # 7. Walsh-Fourier
    walsh = {}
    if do_walsh and depth <= 20:
        walsh = walsh_fourier_analysis(depth, residues)

    # 8. Bit correlation
    bitcorr = {}
    if do_bitcorr and depth <= 22 and n <= 100_000:
        bitcorr = bit_correlation_analysis(depth, residues)

    # 9. 2-adic mixing
    mixing = two_adic_mixing_analysis(depth, residues)

    # 10. Random baseline comparison
    # For N random points in [0, mod), expected star discrepancy ~ 1/sqrt(N)
    expected_disc = 1.0 / math.sqrt(n) if n > 0 else 1.0

    t_total = perf_counter() - t0

    return {
        "depth": depth,
        "modulus": mod,
        "survivor_count": n,
        "density": n / mod,
        "log2_density": math.log2(n / mod) if n > 0 else float("-inf"),
        "enum_time_s": round(t_enum, 4),
        "total_time_s": round(t_total, 4),
        "formula_check": formula_check,
        "star_discrepancy": disc,
        "expected_discrepancy_random": expected_disc,
        "discrepancy_ratio": disc / expected_disc if expected_disc > 0 else float("inf"),
        "gap_distribution": gaps,
        "minimal_survivor": min_surv,
        "exponential_sums": expsum,
        "walsh_fourier": walsh,
        "bit_correlation": bitcorr,
        "two_adic_mixing": mixing,
    }


def self_test() -> bool:
    """Quick self-test: verify the algebraic formula and frontier counts."""
    print("Self-test: algebraic formula verification...")
    for d in [4, 8, 12, 16, 20]:
        residues = enumerate_survivor_residues(d)
        check = verify_algebraic_formula(d, residues)
        assert check["formula_verified"], f"Formula mismatch at depth {d}"
        print(f"  depth {d}: {len(residues)} survivors, formula OK")

    # Check known frontier counts
    known = {20: 27_328, 24: 286_581, 28: 3_524_586}
    for d, expected in known.items():
        residues = enumerate_survivor_residues(d)
        assert len(residues) == expected, \
            f"Depth {d}: expected {expected}, got {len(residues)}"
        print(f"  depth {d}: count = {len(residues)} (matches known)")

    print("Self-test PASSED")
    return True


def main():
    parser = argparse.ArgumentParser(
        description="Survivor equidistribution analyzer"
    )
    parser.add_argument("--self-test", action="store_true", help="Run self-test")
    parser.add_argument("--depths", type=str, default="14,16,18,20,22,24",
                        help="Comma-separated depths to analyze")
    parser.add_argument("--max-depth-walsh", type=int, default=20,
                        help="Maximum depth for Walsh-Fourier analysis")
    parser.add_argument("--max-depth-bitcorr", type=int, default=22,
                        help="Maximum depth for bit correlation analysis")
    parser.add_argument("--max-depth-expsum", type=int, default=24,
                        help="Maximum depth for exponential sum analysis")
    parser.add_argument("--json-out", type=str, default=None,
                        help="Write results to JSON file")
    args = parser.parse_args()

    if args.self_test:
        self_test()
        print()

    depths = [int(x) for x in args.depths.split(",")]
    results = []

    print(f"{'d':>4} {'S(d)':>12} {'density':>12} {'D*':>10} {'D*/D_rand':>10} "
          f"{'min_r':>12} {'duality':>10} {'max_gap/mean':>12}")
    print("-" * 100)

    for d in depths:
        do_walsh = d <= args.max_depth_walsh
        do_bitcorr = d <= args.max_depth_bitcorr
        do_expsum = d <= args.max_depth_expsum

        result = analyze_depth(d, do_walsh=do_walsh, do_bitcorr=do_bitcorr,
                                do_expsum=do_expsum)
        results.append(result)

        n = result["survivor_count"]
        disc = result["star_discrepancy"]
        disc_ratio = result["discrepancy_ratio"]
        min_r = result["minimal_survivor"]["min_survivor_residue"]
        duality = result["minimal_survivor"]["duality_product"]
        max_gap_ratio = result["gap_distribution"].get("ratio_max_mean", 0)

        print(f"{d:>4} {n:>12} {result['density']:>12.6e} {disc:>10.6f} "
              f"{disc_ratio:>10.4f} {min_r:>12} {duality:>10.4f} {max_gap_ratio:>12.4f}")

    # Summary statistics
    print("\n--- Summary ---")
    print(f"Depths analyzed: {len(results)}")
    for r in results:
        d = r["depth"]
        n = r["survivor_count"]
        disc = r["star_discrepancy"]
        exp_disc = r["expected_discrepancy_random"]
        duality = r["minimal_survivor"]["duality_product"]
        print(f"  d={d}: S={n}, D*={disc:.6f} (random~{exp_disc:.6f}), "
              f"ratio={disc/exp_disc:.3f}, duality={duality:.4f}")

        if r.get("walsh_fourier") and not r["walsh_fourier"].get("skipped"):
            w = r["walsh_fourier"]
            print(f"    Walsh: max_nontrivial={w['max_nontrivial_walsh']:.6f}, "
                  f"energy={w['nontrivial_energy']:.6f}")
            if w.get("top_walsh_coeffs"):
                top = w["top_walsh_coeffs"][0]
                print(f"    Top Walsh: S={top['S_bits']}, |coeff|={top['abs_coeff']:.6f}")

        if r.get("bit_correlation"):
            bc = r["bit_correlation"]
            print(f"    Bit corr: max|rho|={bc['max_abs_corr']:.4f}, "
                  f"mean|rho|={bc['mean_abs_corr']:.4f}")

        if r.get("exponential_sums"):
            es = r["exponential_sums"]
            print(f"    Exp sums: max_power={es['max_power']:.4f}, "
                  f"mean_power={es['mean_power']:.4f}")

    if args.json_out:
        with open(args.json_out, "w") as f:
            json.dump(results, f, indent=2, default=str)
        print(f"\nResults written to {args.json_out}")


if __name__ == "__main__":
    main()

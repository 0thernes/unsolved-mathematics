#!/usr/bin/env python3
"""Modular constraint analyzer: determine which low bits are fixed for survivors.

Key insight from the Walsh analysis: the dominant Walsh coefficients of the
survivor indicator are at masks corresponding to the lowest bits, with
magnitudes equal to the density. This means ALL survivors share the same
values for those bits — a modular constraint.

This instrument:
1. Determines exactly which low bits are fixed for all survivors at depth d.
2. Measures the conditional discrepancy after removing fixed bits.
3. Studies the "free" bit distribution.
4. Derives the exact modular constraint set at each depth.

This is the key attack on the representative equidistribution gap.
"""

from __future__ import annotations

import json
import math
from collections import Counter
from time import perf_counter


def shortcut(n: int) -> int:
    return (3 * n + 1) // 2 if n & 1 else n // 2


def enumerate_survivor_residues(depth: int) -> list[int]:
    """Enumerate all survivor residues at depth d."""
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


def find_fixed_bits(residues: list[int], depth: int) -> dict[str, object]:
    """Determine which bit positions have the same value across ALL survivors."""
    if not residues:
        return {}
    fixed_bits = {}
    fixed_mask = 0
    fixed_value = 0
    for j in range(depth):
        bit_mask = 1 << j
        vals = set((r >> j) & 1 for r in residues)
        if len(vals) == 1:
            v = vals.pop()
            fixed_bits[j] = v
            fixed_mask |= bit_mask
            fixed_value |= (v << j)
        else:
            break  # bits are determined from low to high
    return {
        "num_fixed_bits": len(fixed_bits),
        "fixed_bit_positions": list(fixed_bits.keys()),
        "fixed_bit_values": fixed_bits,
        "fixed_mask": fixed_mask,
        "fixed_value": fixed_value,
        "modulus_constraint": fixed_value,
        "modulus": 1 << len(fixed_bits),
    }


def conditional_discrepancy(residues: list[int], depth: int, num_fixed: int) -> dict[str, object]:
    """Measure discrepancy after stripping the fixed low bits.

    Map each residue r to r >> num_fixed (removing the determined low bits),
    then measure equidistribution in [0, 2^(depth - num_fixed)).
    """
    if not residues or num_fixed >= depth:
        return {}
    stripped = sorted(r >> num_fixed for r in residues)
    n = len(stripped)
    mod = 1 << (depth - num_fixed)

    # Star discrepancy
    d_star = 0.0
    for i, s in enumerate(stripped):
        fi = s / mod
        d1 = abs((i + 1) / n - fi)
        d2 = abs(i / n - fi)
        d_star = max(d_star, d1, d2)

    expected_random = 1.0 / math.sqrt(n) if n > 0 else 1.0

    # Gap distribution
    gaps = []
    for i in range(n - 1):
        gaps.append(stripped[i + 1] - stripped[i])
    gaps.append(mod - stripped[-1] + stripped[0])
    mean_gap = mod / n

    return {
        "effective_depth": depth - num_fixed,
        "effective_modulus": mod,
        "num_survivors": n,
        "star_discrepancy": d_star,
        "expected_random": expected_random,
        "discrepancy_ratio": d_star / expected_random if expected_random > 0 else float("inf"),
        "mean_gap": mean_gap,
        "max_gap": max(gaps) if gaps else 0,
        "min_gap": min(gaps) if gaps else 0,
        "gap_cv": (sum((g - mean_gap) ** 2 for g in gaps) / len(gaps)) ** 0.5 / mean_gap if gaps else 0,
    }


def bit_entropy_analysis(residues: list[int], depth: int) -> dict[str, object]:
    """Measure the entropy of each bit position across survivors.

    For a perfectly equidistributed set, each bit should have entropy ~1
    (equal 0s and 1s). Fixed bits have entropy 0.
    """
    n = len(residues)
    if n == 0:
        return {}
    bit_entropies = []
    for j in range(depth):
        ones = sum((r >> j) & 1 for r in residues)
        p1 = ones / n
        if p1 == 0 or p1 == 1:
            h = 0.0
        else:
            h = -p1 * math.log2(p1) - (1 - p1) * math.log2(1 - p1)
        bit_entropies.append({"bit": j, "entropy": h, "p1": p1})
    return {
        "bit_entropies": bit_entropies,
        "min_entropy": min(b["entropy"] for b in bit_entropies),
        "mean_entropy": sum(b["entropy"] for b in bit_entropies) / len(bit_entropies),
        "num_zero_entropy_bits": sum(1 for b in bit_entropies if b["entropy"] == 0),
    }


def block_discrepancy(residues: list[int], depth: int, block_size: int) -> dict[str, object]:
    """Measure discrepancy within blocks of size 2^block_size.

    Partitions [0, 2^depth) into blocks of size 2^block_size and measures
    how uniformly survivors are distributed across blocks.
    """
    n = len(residues)
    if n == 0 or block_size >= depth:
        return {}
    num_blocks = 1 << (depth - block_size)
    block_counts = Counter(r >> block_size for r in residues)
    # Chi-squared statistic
    expected = n / num_blocks
    chi2 = sum((block_counts.get(b, 0) - expected) ** 2 / expected for b in range(num_blocks))
    # Coefficient of variation
    counts = [block_counts.get(b, 0) for b in range(num_blocks)]
    mean_c = sum(counts) / num_blocks
    std_c = (sum((c - mean_c) ** 2 for c in counts) / num_blocks) ** 0.5
    return {
        "block_size": block_size,
        "num_blocks": num_blocks,
        "expected_per_block": expected,
        "chi2": chi2,
        "chi2_per_block": chi2 / num_blocks,
        "cv_block_counts": std_c / mean_c if mean_c > 0 else 0,
        "min_block_count": min(counts),
        "max_block_count": max(counts),
        "empty_blocks": sum(1 for c in counts if c == 0),
    }


def analyze_depth(depth: int) -> dict[str, object]:
    """Full modular constraint analysis at a single depth."""
    t0 = perf_counter()
    residues = enumerate_survivor_residues(depth)
    n = len(residues)
    mod = 1 << depth

    if n == 0:
        return {"depth": depth, "error": "no survivors"}

    # 1. Find fixed bits
    fixed = find_fixed_bits(residues, depth)
    num_fixed = fixed["num_fixed_bits"]

    # 2. Conditional discrepancy
    cond_disc = conditional_discrepancy(residues, depth, num_fixed)

    # 3. Bit entropy
    bit_ent = bit_entropy_analysis(residues, depth)

    # 4. Block discrepancy at various scales
    blocks = {}
    for bs in [4, 8, 12, 16]:
        if bs < depth:
            blocks[bs] = block_discrepancy(residues, depth, bs)

    # 5. Raw discrepancy (for comparison)
    sorted_r = sorted(residues)
    raw_disc = 0.0
    for i, r in enumerate(sorted_r):
        fi = r / mod
        d1 = abs((i + 1) / n - fi)
        d2 = abs(i / n - fi)
        raw_disc = max(raw_disc, d1, d2)

    t_total = perf_counter() - t0

    return {
        "depth": depth,
        "survivor_count": n,
        "density": n / mod,
        "time_s": round(t_total, 4),
        "fixed_bits": fixed,
        "raw_discrepancy": raw_disc,
        "raw_discrepancy_ratio": raw_disc / (1.0 / math.sqrt(n)),
        "conditional_discrepancy": cond_disc,
        "bit_entropy": bit_ent,
        "block_discrepancy": blocks,
    }


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Modular constraint analyzer")
    parser.add_argument("--depths", type=str, default="14,16,18,20,22,24,26,28")
    parser.add_argument("--json-out", type=str, default=None)
    args = parser.parse_args()

    depths = [int(x) for x in args.depths.split(",")]
    results = []

    print(f"{'d':>4} {'S(d)':>10} {'fixed':>6} {'mod_val':>10} {'raw_D*':>10} "
          f"{'cond_D*':>10} {'cond_ratio':>10} {'mean_H':>8} {'zero_H':>6}")
    print("-" * 90)

    for d in depths:
        r = analyze_depth(d)
        results.append(r)

        fb = r["fixed_bits"]
        cd = r.get("conditional_discrepancy", {})
        be = r["bit_entropy"]

        print(f"{d:>4} {r['survivor_count']:>10} {fb['num_fixed_bits']:>6} "
              f"{fb['modulus_constraint']:>10} {r['raw_discrepancy']:>10.6f} "
              f"{cd.get('star_discrepancy', 0):>10.6f} "
              f"{cd.get('discrepancy_ratio', 0):>10.4f} "
              f"{be['mean_entropy']:>8.4f} {be['num_zero_entropy_bits']:>6}")

    # Detailed bit entropy for the deepest depth
    print("\n--- Bit entropy at deepest depth ---")
    if results:
        be = results[-1]["bit_entropy"]
        for b in be["bit_entropies"]:
            bar = "#" * int(b["entropy"] * 20)
            print(f"  bit {b['bit']:>3d}: H={b['entropy']:.4f} p1={b['p1']:.4f} {bar}")

    # Block discrepancy detail
    print("\n--- Block discrepancy at deepest depth ---")
    if results:
        for bs, bd in results[-1].get("block_discrepancy", {}).items():
            print(f"  block_size={bs:>3d}: blocks={bd['num_blocks']:>8d} "
                  f"chi2/block={bd['chi2_per_block']:.4f} "
                  f"cv={bd['cv_block_counts']:.4f} "
                  f"empty={bd['empty_blocks']:>6d} "
                  f"min={bd['min_block_count']:>6d} max={bd['max_block_count']:>6d}")

    if args.json_out:
        with open(args.json_out, "w") as f:
            json.dump(results, f, indent=2, default=str)
        print(f"\nResults written to {args.json_out}")


if __name__ == "__main__":
    main()

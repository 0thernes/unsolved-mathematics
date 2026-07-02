#!/usr/bin/env python3
"""Local bit constraint analyzer: derive the complete set of local constraints
on survivor residue bits from the survivor condition.

The survivor condition 3^{o(j)} >= 2^j for all j <= d creates local constraints
on consecutive bits of the residue r. This instrument:

1. Derives all local constraints (forbidden bit patterns) at each depth.
2. Measures the conditional discrepancy after removing all constrained bits.
3. Tracks how the constraint set grows with depth.
4. Tests whether the constraints are purely local (involving only adjacent bits)
   or have longer-range structure.

Key proved facts:
- bits 0,1 = 11 (all survivors ≡ 3 mod 4)
- (bit2, bit3) ≠ (0,0) [from depth-4 condition]
- (bit3, bit4) ≠ (0,1) [from depth-5 condition]

The goal is to find ALL such constraints and show that after conditioning,
the remaining bits are equidistributed — which would prove representative
equidistribution.
"""

from __future__ import annotations

import json
import math
from collections import Counter
from itertools import product
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


def find_all_local_constraints(residues: list[int], depth: int,
                                max_window: int = 4) -> dict[str, object]:
    """Find all forbidden bit patterns in windows of size 1 to max_window.

    For each window size w and each starting bit position j, check which
    of the 2^w possible bit patterns never occur among survivors.
    """
    n = len(residues)
    if n == 0:
        return {}

    constraints = []
    for w in range(1, max_window + 1):
        for j in range(depth - w + 1):
            # Count occurrences of each pattern
            pattern_counts = Counter()
            for r in residues:
                pattern = (r >> j) & ((1 << w) - 1)
                pattern_counts[pattern] += 1

            forbidden = []
            for p in range(1 << w):
                if pattern_counts.get(p, 0) == 0:
                    forbidden.append(p)

            if forbidden:
                constraints.append({
                    "window_size": w,
                    "start_bit": j,
                    "bits": list(range(j, j + w)),
                    "forbidden_patterns": forbidden,
                    "num_forbidden": len(forbidden),
                    "num_allowed": (1 << w) - len(forbidden),
                    "fraction_forbidden": len(forbidden) / (1 << w),
                })

    return {
        "depth": depth,
        "num_constraints": len(constraints),
        "constraints": constraints,
    }


def conditional_discrepancy_after_constraints(
    residues: list[int], depth: int, constraints: list[dict]
) -> dict[str, object]:
    """Measure discrepancy after conditioning on all local constraints.

    Instead of just removing fixed bits, we compute the "effective freedom"
    by counting how many bit patterns are actually realized.
    """
    n = len(residues)
    mod = 1 << depth
    if n == 0:
        return {}

    # For each bit position, compute the entropy
    bit_entropies = []
    for j in range(depth):
        ones = sum((r >> j) & 1 for r in residues)
        p1 = ones / n
        if p1 == 0 or p1 == 1:
            h = 0.0
        else:
            h = -p1 * math.log2(p1) - (1 - p1) * math.log2(1 - p1)
        bit_entropies.append(h)

    # Total entropy (sum of individual bit entropies — upper bound on joint entropy)
    total_entropy = sum(bit_entropies)

    # Find the "effective free dimension" — the number of bits with entropy > 0
    # minus the entropy loss from constraints
    free_bits = [j for j in range(depth) if bit_entropies[j] > 0]
    fixed_bits = [j for j in range(depth) if bit_entropies[j] == 0]

    # Measure discrepancy on the "free" bits only
    if not free_bits:
        return {"effective_dimension": 0}

    # Map residues to their free-bit representation
    free_mask = sum(1 << j for j in free_bits)
    free_mapped = sorted((r & free_mask) for r in residues)

    # The effective space has dimension = number of free bits,
    # but the actual number of distinct values may be less due to constraints
    distinct_vals = len(set(free_mapped))

    # Star discrepancy on the free-bit space
    # We need to map to a contiguous space for discrepancy measurement
    # Use the rank-based approach
    sorted_free = sorted(set(free_mapped))
    rank_map = {v: i for i, v in enumerate(sorted_free)}

    # Map each residue to its rank
    ranks = sorted(rank_map[r & free_mask] for r in residues)
    n_distinct = len(sorted_free)

    d_star = 0.0
    for i, rk in enumerate(ranks):
        fi = (rk + 0.5) / n_distinct
        d1 = abs((i + 1) / n - fi)
        d2 = abs(i / n - fi)
        d_star = max(d_star, d1, d2)

    expected_random = 1.0 / math.sqrt(n) if n > 0 else 1.0

    return {
        "num_free_bits": len(free_bits),
        "num_fixed_bits": len(fixed_bits),
        "fixed_bit_positions": fixed_bits,
        "free_bit_positions": free_bits,
        "distinct_free_values": distinct_vals,
        "effective_dimension": total_entropy,
        "free_discrepancy": d_star,
        "expected_random": expected_random,
        "discrepancy_ratio": d_star / expected_random if expected_random > 0 else 0,
    }


def constraint_growth_analysis(depths: list[int]) -> list[dict]:
    """Track how the constraint set grows with depth."""
    results = []
    for d in depths:
        residues = enumerate_survivor_residues(d)
        if not residues:
            continue
        constraints = find_all_local_constraints(residues, d, max_window=3)

        # Count constraints by window size
        by_window = {}
        for c in constraints["constraints"]:
            w = c["window_size"]
            if w not in by_window:
                by_window[w] = 0
            by_window[w] += c["num_forbidden"]

        # Bit entropy
        n = len(residues)
        bit_ent = []
        for j in range(d):
            ones = sum((r >> j) & 1 for r in residues)
            p1 = ones / n
            if p1 == 0 or p1 == 1:
                h = 0.0
            else:
                h = -p1 * math.log2(p1) - (1 - p1) * math.log2(1 - p1)
            bit_ent.append(h)

        num_fixed = sum(1 for h in bit_ent if h == 0)
        total_entropy = sum(bit_ent)

        results.append({
            "depth": d,
            "survivor_count": n,
            "num_constraints": constraints["num_constraints"],
            "total_forbidden_patterns": sum(by_window.values()),
            "forbidden_by_window": by_window,
            "num_fixed_bits": num_fixed,
            "total_bit_entropy": total_entropy,
            "effective_dimension": total_entropy,
            "entropy_per_bit": total_entropy / d if d > 0 else 0,
        })
    return results


def analyze_depth(depth: int, max_window: int = 3) -> dict[str, object]:
    """Full constraint analysis at a single depth."""
    t0 = perf_counter()
    residues = enumerate_survivor_residues(depth)
    n = len(residues)
    if n == 0:
        return {"depth": depth, "error": "no survivors"}

    constraints = find_all_local_constraints(residues, depth, max_window)
    cond = conditional_discrepancy_after_constraints(
        residues, depth, constraints["constraints"]
    )

    t_total = perf_counter() - t0

    return {
        "depth": depth,
        "survivor_count": n,
        "time_s": round(t_total, 4),
        "constraints": constraints,
        "conditional_analysis": cond,
    }


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Local bit constraint analyzer")
    parser.add_argument("--depths", type=str, default="14,16,18,20,22,24,26,28")
    parser.add_argument("--max-window", type=int, default=3)
    parser.add_argument("--json-out", type=str, default=None)
    parser.add_argument("--growth-only", action="store_true")
    args = parser.parse_args()

    depths = [int(x) for x in args.depths.split(",")]

    if args.growth_only:
        results = constraint_growth_analysis(depths)
        print(f"{'d':>4} {'S(d)':>10} {'constraints':>12} {'forbidden':>10} "
              f"{'fixed':>6} {'total_H':>8} {'H/bit':>8}")
        print("-" * 70)
        for r in results:
            print(f"{r['depth']:>4} {r['survivor_count']:>10} "
                  f"{r['num_constraints']:>12} {r['total_forbidden_patterns']:>10} "
                  f"{r['num_fixed_bits']:>6} {r['total_bit_entropy']:>8.4f} "
                  f"{r['entropy_per_bit']:>8.4f}")
            print(f"     forbidden by window: {r['forbidden_by_window']}")
        if args.json_out:
            with open(args.json_out, "w") as f:
                json.dump(results, f, indent=2, default=str)
        return

    results = []
    for d in depths:
        r = analyze_depth(d, args.max_window)
        results.append(r)

        print(f"\n=== Depth {d} (S={r['survivor_count']}) ===")

        # Print constraints
        constraints = r["constraints"]["constraints"]
        print(f"Total constraints: {r['constraints']['num_constraints']}")

        # Group by window size
        by_w = {}
        for c in constraints:
            w = c["window_size"]
            if w not in by_w:
                by_w[w] = []
            by_w[w].append(c)

        for w in sorted(by_w.keys()):
            print(f"\n  Window size {w} ({len(by_w[w])} constraints):")
            for c in by_w[w]:
                forbidden_strs = [bin(p) for p in c["forbidden_patterns"]]
                print(f"    bits {c['bits']}: {c['num_forbidden']} forbidden "
                      f"({forbidden_strs}), {c['num_allowed']} allowed")

        # Conditional analysis
        cond = r["conditional_analysis"]
        print(f"\n  Conditional: free_bits={cond['num_free_bits']}, "
              f"fixed={cond['num_fixed_bits']}, "
              f"distinct={cond['distinct_free_values']}, "
              f"eff_dim={cond['effective_dimension']:.4f}, "
              f"D*={cond['free_discrepancy']:.6f}, "
              f"ratio={cond['discrepancy_ratio']:.4f}")

    if args.json_out:
        with open(args.json_out, "w") as f:
            json.dump(results, f, indent=2, default=str)
        print(f"\nResults written to {args.json_out}")


if __name__ == "__main__":
    main()

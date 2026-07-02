#!/usr/bin/env python3
"""
Repulsion Potential Minimizer — escalation beyond cocycle.

Defines a new "defect potential" combining:
- Multiplier debt M = o * log2(3) - d
- Normalized cocycle defect D = c / 2^d  (positive injection)
- Boundary alignment A (bits close to -1)
- Repulsion "velocity" from observed carry flips

Hypothesis (new): On positive integers, V = M + lambda * max(0, -log(1 + D)) + mu * (A / d)  or similar is "repelled" downward at a rate > entropy deficit, forcing crossing to certified (M <0) in bounded steps.

This constructs an explicit (computable) Lyapunov-like function for the positive cone.

Searches for parameters lambda, mu that make V strictly decrease on actual orbits until descent.
"""

from __future__ import annotations
import argparse
import json
import math
from typing import List, Dict

def compute_orbit_with_cocycle(n: int, max_d: int = 4096):
    """Run full shortcut orbit, tracking approximate cocycle state."""
    steps = []
    current = n
    d = 0
    o = 0
    # Approximate accumulated c: we simulate the additive separately
    # For rigor we would need full affine, but for search use running image vs multiplier
    c_approx = 0.0   # normalized later
    while current > 1 and d < max_d:
        if current % 2 == 0:
            current //= 2
            parity = 0
        else:
            current = (3 * current + 1) // 2
            parity = 1
            o += 1
            c_approx = 3 * c_approx + 1   # rough
        d += 1
        m_debt = o * math.log2(3) - d
        # alignment to -1
        align = 0
        t = current + 1
        while t % 2 == 0 and align < 60:
            t //= 2
            align += 1
        D = abs(c_approx) / (2 ** min(d, 60)) if d > 0 else 0
        steps.append({
            "d": d, "n": current, "o": o, "M": m_debt,
            "align": align, "D": D, "parity": parity
        })
    return steps

def potential(M: float, D: float, A: int, d: int, lam: float = 1.0, mu: float = 0.5) -> float:
    """Candidate Lyapunov / defect potential. Tune lam, mu."""
    # M is the expanding debt; we want it driven negative
    # High D (defect) and high A should accelerate descent
    defect_term = lam * math.log1p(D)   # positive defect contributes "push down"
    align_term = mu * (A / (d + 1))     # alignment amplifies repulsion
    return M - defect_term - align_term

def analyze_potential(start: int, lam=1.0, mu=0.5, max_d=2048):
    orbit = compute_orbit_with_cocycle(start, max_d)
    Vs = []
    deltas = []
    prev_V = None
    for s in orbit:
        V = potential(s["M"], s["D"], s["align"], s["d"], lam, mu)
        Vs.append(V)
        if prev_V is not None:
            deltas.append(V - prev_V)
        prev_V = V
    min_V = min(Vs) if Vs else 0
    final_M = orbit[-1]["M"] if orbit else 0
    # Count strict decreases
    strict_dec = sum(1 for dd in deltas if dd < 0)
    return {
        "start": start,
        "steps": len(orbit),
        "final_M": final_M,
        "min_V": min_V,
        "strict_dec_count": strict_dec,
        "avg_delta": sum(deltas)/len(deltas) if deltas else 0,
        "repulsion_rate": strict_dec / max(1, len(deltas))
    }

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--starts", default="27,703,35655,2358909599867980429759")
    p.add_argument("--lam", type=float, default=2.5)
    p.add_argument("--mu", type=float, default=1.2)
    p.add_argument("--json-out", default="experiments/results/repulsion_potential_round2.json")
    args = p.parse_args()

    starts = [int(x) for x in args.starts.split(",")]
    out = []
    for s in starts:
        res = analyze_potential(s, args.lam, args.mu)
        out.append(res)
        print(f"Start {s}: steps={res['steps']} finalM={res['final_M']:.2f} minV={res['min_V']:.2f} rate={res['repulsion_rate']:.3f}")

    with open(args.json_out, "w") as f:
        json.dump({"lam": args.lam, "mu": args.mu, "results": out, "note": "Potential V = M - lam*log(1+D) - mu*(A/d) on positives. Search for params making avg_delta <0 and final_M <<0."}, f)
    print("Wrote potential data.")

if __name__ == "__main__":
    main()

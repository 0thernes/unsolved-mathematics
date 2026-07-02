#!/usr/bin/env python3
"""
cycle_bound_lab.py — Cycle-side instrument: derive a lower bound on the odd
length of any nontrivial Collatz cycle from the verified convergence bound,
via continued fractions of log2(3).

This is the classical Eliahou-style argument, reproduced with explicit,
auditable arithmetic. It is intentionally cruder than the Simons–de Weger /
Hercher m-cycle machinery; the point is that the repo can *derive* the
magnitude of the modern cycle floor from first principles instead of only
citing it. It proves nothing new.

## The mathematics

Shortcut map T(n) = n/2 (even), (3n+1)/2 (odd). Suppose a nontrivial cycle
has k odd steps, l total steps, and minimum element n_min. Each odd step
multiplies by (3/2)(1 + 1/(3n)); each even step by 1/2. Going once around:

    1 = (3^k / 2^l) * prod_{odd steps} (1 + 1/(3 n_i))

so, since every n_i >= n_min,

    0 < l - k*theta <= k * log2(1 + 1/(3 n_min)) =: k*delta,   theta = log2(3).

(The left inequality is strict: the product is > 1. Self-test: the trivial
cycle 1 -> 2 -> 1 has k=1, l=2, and 2^2/3^1 = 4/3 = 1 + 1/(3*1) exactly.)

Thus l is the integer just above k*theta and the distance from k*theta up to
that integer is at most k*delta. Continued-fraction best approximation gives,
for any k < q_{j+1} (q_j = convergent denominators of theta):

    ||k*theta|| >= ||q_j*theta|| > 1/(q_j + q_{j+1})

so a cycle with k < q_{j+1} needs  k > T_j := 1/(delta*(q_j + q_{j+1})).
Laddering over j yields an unconditional lower bound k_min once T_j < q_{j+1}.

With n_min = 2^71 (Barina 2025, all n < 2^71 converge, so every element of a
nontrivial cycle exceeds 2^71), delta ~ 2.04e-22 and k_min lands at the
~1e11 scale — the same magnitude as Hercher's published floor of
1.375e11 odd terms (his sharper machinery beats the crude bound; magnitude
agreement is the check).

## Precision honesty

theta's continued fraction is computed twice (at working precisions P and
2P via the decimal module) and only the agreeing prefix of terms is used;
the ladder additionally re-verifies each convergent inequality
|q_j*theta - p_j| < 1/q_{j+1} numerically at the higher precision. All
reported convergents are cross-checked against the classical prefix
19/12, 65/41, 84/53, 485/306, 1054/665, 24727/15601 (music-theory
convergents of the octave/fifth ratio).

Usage:
    python cycle_bound_lab.py                 # n_min = 2^71
    python cycle_bound_lab.py --log2-nmin 68  # reproduce the older bound
"""
from __future__ import annotations

import argparse
import json
import sys
from decimal import Decimal, getcontext


def cf_terms_of_log2_3(prec: int, max_terms: int = 60) -> list[int]:
    """Continued-fraction terms of log2(3) at the given decimal precision."""
    getcontext().prec = prec
    x = Decimal(3).ln() / Decimal(2).ln()
    terms: list[int] = []
    for _ in range(max_terms):
        a = int(x)
        terms.append(a)
        frac = x - a
        if frac == 0:
            break
        x = 1 / frac
    return terms


def trusted_cf_terms(prec: int) -> list[int]:
    """CF terms that agree between precision prec and 2*prec (drop last two
    agreeing terms as an extra safety margin)."""
    lo = cf_terms_of_log2_3(prec)
    hi = cf_terms_of_log2_3(2 * prec)
    agree: list[int] = []
    for a, b in zip(lo, hi):
        if a != b:
            break
        agree.append(a)
    return agree[:-2] if len(agree) > 2 else agree


def convergents(terms: list[int]) -> list[tuple[int, int]]:
    """(p_j, q_j) convergents from CF terms."""
    out: list[tuple[int, int]] = []
    p0, q0, p1, q1 = 1, 0, terms[0], 1
    out.append((p1, q1))
    for a in terms[1:]:
        p0, q0, p1, q1 = p1, q1, a * p1 + p0, a * q1 + q0
        out.append((p1, q1))
    return out


def run(log2_nmin: int, prec: int) -> dict:
    terms = trusted_cf_terms(prec)
    convs = convergents(terms)

    # classical prefix self-test
    known_denoms = [12, 41, 53, 306, 665, 15601]
    got_denoms = [q for _, q in convs]
    assert all(d in got_denoms for d in known_denoms), (
        "convergent self-test failed: " + str(got_denoms[:12])
    )

    getcontext().prec = 2 * prec
    theta = Decimal(3).ln() / Decimal(2).ln()
    # numeric re-verification of the convergent quality used by the ladder
    for j in range(len(convs) - 1):
        p, q = convs[j]
        q_next = convs[j + 1][1]
        assert abs(q * theta - p) < Decimal(1) / Decimal(q_next), (
            f"convergent {j} failed quality check"
        )

    n_min = Decimal(2) ** log2_nmin
    # delta = log2(1 + 1/(3 n_min))
    delta = (1 + 1 / (3 * n_min)).ln() / Decimal(2).ln()

    ladder = []
    k_min = None
    lower = 1  # running lower bound on k
    for j in range(len(convs) - 1):
        q_j = convs[j][1]
        q_next = convs[j + 1][1]
        t_j = 1 / (delta * (q_j + q_next))
        step = {
            "j": j,
            "q_j": q_j,
            "q_j+1": q_next,
            "T_j": float(t_j),
            "conclusion": None,
        }
        if t_j >= q_next:
            lower = q_next
            step["conclusion"] = f"no cycle with k < {q_next}"
            ladder.append(step)
            continue
        k_min = max(lower, int(t_j) + 1)
        step["conclusion"] = f"binding: k >= max({lower}, {int(t_j) + 1})"
        ladder.append(step)
        break

    assert k_min is not None, "ladder did not terminate within trusted terms"
    l_min = int(k_min * theta) + 1  # total shortcut steps ~ ceil(k*theta)

    return {
        "verified_convergence_bound": f"2^{log2_nmin}",
        "delta_log2(1+1/(3*n_min))": float(delta),
        "cf_terms_used": terms[: len(convs)],
        "ladder": ladder[-4:],
        "result": {
            "min_odd_steps_in_nontrivial_cycle": k_min,
            "min_total_shortcut_steps": l_min,
            "min_total_classic_steps": l_min + k_min,
        },
        "published_comparison": {
            "hercher_2023_with_2^71": 1.375e11,
            "note": "crude Eliahou-style bound; magnitude agreement with the sharper published floor is the check",
        },
        "honesty": "unconditional given the verified bound; proves nothing new; a finite bound can never exclude the infinite family of possible cycle lengths",
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--log2-nmin", type=int, default=71,
                    help="verified convergence exponent: all n < 2^this converge")
    ap.add_argument("--prec", type=int, default=150)
    args = ap.parse_args()
    json.dump(run(args.log2_nmin, args.prec), sys.stdout, indent=2)
    print()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

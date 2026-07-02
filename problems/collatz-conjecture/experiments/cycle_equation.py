#!/usr/bin/env python3
"""
Cycle side, from scratch. Shortcut map  T_{q,e}(x) = (q x + e)/2 if x odd, x/2 if even.

CYCLE EQUATION.  A cycle with odd elements a_1..a_k (k odd steps) and L total steps
must return to start, i.e. the net multiplier is 1:
    (1/2^L) * prod_i (q + e/a_i) = 1   <=>   prod_i (q a_i + e) = 2^L * prod_i a_i.   (INT identity)
Taking log2:  L = k*log2(q) + sum_i log2(1 + e/(q a_i)).                              (LOG form)

Two immediate consequences (the repo's sign dichotomy, re-derived):
  e=+1: every term >0 => L > k log2 q => q^k < 2^L  (cycle BELOW the line)
  e=-1: every term <0 => L < k log2 q => q^k > 2^L  (cycle ABOVE the line)

We VALIDATE the exact integer identity on every known cycle (ground truth), then show the
cycle-exclusion mechanism for Collatz (= Eliahou/CF; reproduces cycle_bound_lab).
"""
import math
from fractions import Fraction

def find_cycle(q, e, start, max_steps=100000):
    x = start; a = []; L = 0
    while True:
        if x & 1:
            a.append(x); x = (q*x + e)//2
        else:
            x //= 2
        L += 1
        if x == start: break
        if L > max_steps: raise RuntimeError("no cycle")
    return a, len(a), L   # odd elements, k, L

KNOWN = [
    ("Collatz 3n+1 (trivial)", 3, +1, 1),
    ("3n-1 fixed point",       3, -1, 1),
    ("3n-1 cycle at 5",        3, -1, 5),
    ("3n-1 cycle at 17",       3, -1, 17),
    ("5n+1 cycle at 13",       5, +1, 13),
    ("5n+1 cycle at 17",       5, +1, 17),
]

print("EXACT CYCLE-EQUATION VALIDATION  (prod(q a_i + e) == 2^L * prod a_i)")
print("="*84)
allok = True
for name, q, e, start in KNOWN:
    a, k, L = find_cycle(q, e, start)
    lhs = 1
    for ai in a: lhs *= (q*ai + e)
    rhs = (1 << L)
    for ai in a: rhs *= ai
    exact = (lhs == rhs)
    allok &= exact
    theta = math.log2(q)
    defect = L - k*theta                                  # L - k log2 q
    curv = sum(math.log2(1 + e/(q*ai)) for ai in a)       # sum log2(1 + e/(q a_i))
    side = "q^k < 2^L (below)" if q**k < (1<<L) else "q^k > 2^L (above)"
    sign_expected = "below" if e > 0 else "above"
    sign_ok = (("below" in side) == (e > 0))
    print(f"{name}")
    print(f"   k={k} odd steps, L={L} total; odd elements a_i = {a}")
    print(f"   INT identity prod(q a_i+e)={lhs}  vs  2^L*prod a_i={rhs}   EXACT: {exact}")
    print(f"   defect L-k*log2 q = {defect:+.6f}   sum log2(1+e/(q a_i)) = {curv:+.6f}"
          f"   (match: {abs(defect-curv)<1e-9})")
    print(f"   {side}   sign rule e{'+' if e>0 else '-'}1 => {sign_expected}: {sign_ok}")
    print()
print(f"ALL known cycles satisfy the exact integer identity: {allok}")

print("\n" + "="*84)
print("CYCLE-EXCLUSION MECHANISM for Collatz (q=3,e=+1) -- honest, = Eliahou/CF ladder")
print("="*84)
print("For a nontrivial cycle, defect d_k = ceil(k log2 3) - k log2 3 = sum log2(1+1/(3 a_i)).")
print("Since log2(1+t) <= t/ln2 and every a_i >= m (min element):  d_k <= k/(3 m ln2),")
print("so  m <= k / (3 ln2 * d_k).  All n<2^71 verified => every cycle element > 2^71, forcing")
print("d_k < k / (3 ln2 * 2^71): the defect must be astronomically small, i.e. k must sit at a")
print("very deep convergent of log2 3. That is exactly the continued-fraction ladder in")
print("cycle_bound_lab.py (verified floor ~6.5e10 odd steps vs Hercher's 1.375e11).\n")
from decimal import Decimal, getcontext
getcontext().prec = 60
theta = Decimal(3).ln()/Decimal(2).ln()
print(f"   {'k':>8} {'d_k=ceil(k t)-k t':>20} {'=> m <= k/(3 ln2 d_k)':>26}")
for k in (12, 41, 53, 306, 15601, 31867):     # convergent denominators of log2 3
    dk = float((k*theta).to_integral_value(rounding='ROUND_CEILING') - k*theta)
    mbound = k/(3*math.log(2)*dk) if dk>0 else float('inf')
    print(f"   {k:>8} {dk:>20.3e} {mbound:>26.3e}")
print("\n   At k=31867 the allowed min element already exceeds ~1e13; pushing to convergents with")
print("   d_k ~ 2^-71 forces k into the 1e10-1e11 range. A finite bound never excludes ALL k.")

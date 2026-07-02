"""
spine_regen_kernel.py -- the alignment-regeneration kernel of SPINE-LADDER.md.

SPINE-LADDER isolates the open target: after a positive integer is expelled from a
spine cylinder, its regenerated 2-adic alignment is v2 of an affine expression in
3^j-multiples. This instrument resolves the PURE-spine case exactly and names the
residual wall. No proof of Collatz; a structural localization.
"""
import json
from collections import Counter

def v2(n):
    c = 0
    while n % 2 == 0:
        n //= 2; c += 1
    return c

def order3(k):                       # multiplicative order of 3 mod 2^k
    m = 1 << k; x = 3 % m; e = 1
    while x != 1:
        x = (x * 3) % m; e += 1
    return e

out = {}

# (1) structure: 3 generates the index-2 subgroup of (Z/2^k)^*  (order 2^{k-2})
out["order_3_mod_2^k_equals_2^(k-2)"] = all(order3(k) == (1 << (k - 2)) for k in range(3, 20))

# (2) pure-spine regeneration solved exactly by Lifting-the-Exponent
p = 1; viol = 0
for j in range(1, 4001):
    p *= 3
    ok = (v2(p - 1) == (1 if j % 2 else 2 + v2(j))) and (v2(p + 1) == (2 if j % 2 else 1))
    viol += (not ok)
out["LTE_formula_violations_j_le_4000"] = viol

# (3) the regenerated-alignment distribution on the pure spine is explicit & geometric
p = 1; dist = Counter()
for j in range(1, 4001):
    p *= 3
    if j % 2 == 0:
        dist[v2(p - 1)] += 1
out["v2(3^j-1)_over_even_j_distribution"] = dict(sorted(dist.items())[:8])

out["localization"] = (
    "Pure spine (odd multiplier q=1: the -1 and -5 fixed points) is FULLY solved: "
    "v2(3^j-1)=2+v2(j) (even j) / 1 (odd j); v2(3^j+1)=2 (odd) / 1 (even) -- a clean "
    "geometric law. The residual wall is the coupled case: a positive orbit regenerates "
    "v2(3^j*q +/- c) with (j,q,c) DYNAMICALLY coupled, i.e. a measure-zero subsequence of "
    "the index-2 subgroup <3> mod 2^k. Controlling it pointwise is an effective "
    "equidistribution/discrepancy statement for that dynamically-selected subsequence -- "
    "the same measure-1 vs measure-0 wall named in EPSILON-BARRIER.md and DIVERGENCE-DRIFT.md, "
    "now in its sharpest concrete form, and tied again to the Diophantine object log2(3)."
)
print(json.dumps(out, indent=2))
with open("results/spine_regen_kernel.json", "w") as f:
    json.dump(out, f, indent=2)

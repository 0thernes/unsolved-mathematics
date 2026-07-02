"""
equidistribution_kernel.py -- the spine-regeneration crux is 2-adic distribution
of powers of 3 (Furstenberg / Erdos territory). Structural facts, all verified.
"""
import json, random

def v2(n):
    c = 0
    while n % 2 == 0:
        n //= 2; c += 1
    return c

def subgroup3(k):
    m = 1 << k; s = set(); x = 1
    while True:
        s.add(x); x = (x * 3) % m
        if x == 1:
            break
    return s

out = {}

# (1) <3> mod 2^k = { x : x ==1 or 3 mod 8 }, index 2 in (Z/2^k)^*
coset_ok = True
for k in range(4, 15):
    m = 1 << k
    coset_ok &= (subgroup3(k) == {x for x in range(1, m, 2) if x % 8 in (1, 3)}
                 and len(subgroup3(k)) == (1 << (k - 2)))
out["subgroup3_is_1_3_mod_8_index_2"] = coset_ok
out["minus1_boundary_residue_mod_8"] = (-1) % 8            # = 7, complementary coset
out["minus1_is_power_of_3_residue"] = (7 % 8) in (1, 3)     # False

# (2) alignment cap: v2(3^j - m) <= 2 for m in the complementary coset (m==5,7 mod 8)
rng = random.Random(7); capped = True; hi = 0
for _ in range(200000):
    j = rng.randint(1, 400); m = rng.randrange(1, 1 << 20, 2)
    if m % 8 in (5, 7):
        val = v2(3 ** j - m); hi = max(hi, val)
        capped &= (val <= 2)
out["v2_3j_minus_m_capped_at_2_for_complementary_coset"] = capped
out["max_seen"] = hi

out["reading"] = (
    "Supercritical survival needs sustained high alignment v2>=3, which (by (2)) is "
    "possible ONLY toward power-of-3 residues m==1,3 mod 8. So a divergent/cycling "
    "positive orbit would have to keep hitting <3> mod 2^k with growing 2-adic precision "
    "-- an EFFECTIVE EQUIDISTRIBUTION statement for {3^j} in Z_2. That is exactly the "
    "subject of recognized-open problems: Furstenberg's x2-x3 rigidity, and Erdos's "
    "questions on the base-2 digits / 2-adic distribution of 3^n. No pointwise/effective "
    "control is known. The Collatz spine kernel is a concrete instance of that class -- "
    "which is why elementary or purely-computational attacks (human or AI) do not close it: "
    "the obstruction is a genuine open problem, not a missing trick. No proof claim."
)
print(json.dumps(out, indent=2))
with open("results/equidistribution_kernel.json", "w") as f:
    json.dump(out, f, indent=2)

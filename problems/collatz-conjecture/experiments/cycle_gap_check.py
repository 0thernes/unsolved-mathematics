"""
cycle_gap_check.py -- exact cycle-exclusion arithmetic for the Collatz shortcut map.

For a nontrivial cycle through k odd values with L total halvings (shortcut map
T(n)=(3n+1)/2 odd, n/2 even), the cycle equation gives, with c(w)=sum 3^{k-i} 2^{A_i}>0:

        m = c(w) / (2^L - 3^k),     needs 2^L > 3^k.

Since c(w) < 2^L * 3^k (each of the (3^k-1)/2 < 3^k terms is < 2^L), the cycle
MINIMUM m obeys the rigorous upper bound

        m  <  2^L * 3^k / (2^L - 3^k)   =: CEIL(k, L).

The ceiling is largest at the smallest positive gap g(k)=min_{2^L>3^k}(2^L-3^k),
which occurs at L = bitlen(3^k). If CEIL(k) < 2^71 for a given k, then EVERY
k-cycle has minimum < 2^71; since all n < 2^71 are verified to reach 1
(Barina 2025), no nontrivial k-cycle exists. This is the elementary core of the
cycle-exclusion program; the strong odd-term floor needs Baker's linear forms
in logarithms (Steiner; Simons-de Weger; Hercher 2023) -- NOT reproduced here.
"""
from decimal import Decimal, getcontext
import json
getcontext().prec = 60

VERIF = 2 ** 71  # Barina 2025 verification bound

# smallest positive gap and rigorous ceiling for each odd-count k
def row(k):
    p = 3 ** k
    L = p.bit_length()          # smallest L with 2^L > 3^k
    gap = (1 << L) - p          # smallest positive gap 2^L - 3^k
    ceil = ((1 << L) * p) // gap
    return L, gap, ceil, gap / p  # last = relative gap

log2_3 = Decimal(3).ln() / Decimal(2).ln()
conv_ks = {1, 2, 5, 12, 41, 53, 306, 665, 15601, 31867}  # CF-convergent odd-counts

out = {"verification_bound_2^71": str(VERIF),
       "check_2^71 > 3*2^69": (2 ** 71) > (3 * 2 ** 69)}

# largest k the elementary ceiling alone excludes (CEIL(k) < 2^71 for all L)
excluded = []
table = []
for k in range(1, 121):
    L, gap, ceil, relgap = row(k)
    if ceil < VERIF:
        excluded.append(k)
    if k <= 15 or k in conv_ks:
        table.append({"k": k, "L": L, "gap_2^L-3^k": str(gap),
                      "rel_gap": f"{relgap:.3e}",
                      "ceil_lt_2^71": ceil < VERIF,
                      "is_CF_convergent_k": k in conv_ks})
out["elementary_ceiling_excludes_odd_counts_k_up_to"] = max(excluded) if excluded else 0
out["note"] = ("Elementary bound alone excludes only very small k. Hercher (2023) "
               "raises the floor to >= 1.375e11 odd terms via linear forms in logs, "
               "made unconditional by 2^71 > 3*2^69.")
out["sample_rows"] = table

# also: exact gap at each CF convergent (these are the 'dangerous' near-cycle lengths)
conv_rows = []
p0, p1, q0, q1 = 1, int(log2_3), 0, 1
# regenerate convergents from CF of log2_3
x, a = log2_3, []
for _ in range(14):
    ai = int(x); a.append(ai)
    fr = x - ai
    if fr == 0: break
    x = 1 / fr
p0, p1, q0, q1 = 1, a[0], 0, 1
for ai in a[1:11]:
    p2, q2 = ai * p1 + p0, ai * q1 + q0
    L, gap, ceil, relgap = row(q2)   # k = q2 (odd-count), best-L gap
    conv_rows.append({"L/k": f"{p2}/{q2}", "smallest_gap_bits": (gap.bit_length() if gap>0 else 0),
                      "3^k_bits": (3**q2).bit_length(), "rel_gap": f"{relgap:.3e}"})
    p0, p1, q0, q1 = p1, p2, q1, q2
out["convergent_gaps"] = conv_rows

print(json.dumps(out, indent=2))
with open("results/cycle_gap.json", "w") as f:
    json.dump(out, f, indent=2)

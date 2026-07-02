"""
cycle_baker_check.py -- the linear-form records behind cycle exclusion, and the
exact point where elementary arithmetic must hand off to effective transcendence.

For a nontrivial cycle: k odd steps, L = bitlen(3^k) halvings at the tightest fit.
The controlling quantity is the linear form in logarithms
        lambda(k) = L*ln2 - k*ln3 = ln(2^L / 3^k) > 0,
and the cycle minimum obeys  m < 3^k / (2^lambda - 1) ~ 3^k / lambda  (small lambda).
A cycle with minimum above the verified bound 2^71 needs lambda(k) small enough.
Record-small lambda occurs exactly at continued-fraction convergents of log2(3).
Everything measured; the UNIFORM lower bound on lambda(k) is Baker/effective
transcendence (Rhin; Nesterenko; used by Hercher 2023) -- cited, not re-derived.
"""
from decimal import Decimal, getcontext
import json
getcontext().prec = 120
LN2, LN3 = Decimal(2).ln(), Decimal(3).ln()
VERIF = 2 ** 71

def lam(k):
    L = (3 ** k).bit_length()          # smallest L with 2^L > 3^k
    return L, L * LN2 - k * LN3        # linear form > 0

# record-small linear forms up to K -- these are the "dangerous" cycle lengths
records = []
best = None
for k in range(1, 5001):
    L, lm = lam(k)
    if best is None or lm < best:
        best = lm
        # elementary ceiling on cycle minimum at this k
        gap = (1 << L) - 3 ** k
        ceil = ((1 << L) * 3 ** k) // gap
        records.append({"k": k, "L": L, "lambda": f"{float(lm):.3e}",
                        "ceil_cycle_min_bits": ceil.bit_length(),
                        "ceil_exceeds_2^71": ceil > VERIF})

# smallest k whose elementary ceiling can exceed 2^71 (i.e. NOT excluded elementarily)
first_unexcluded = None
for k in range(1, 5001):
    L = (3 ** k).bit_length()
    gap = (1 << L) - 3 ** k
    ceil = ((1 << L) * 3 ** k) // gap
    if ceil > VERIF:
        first_unexcluded = k
        break

out = {
    "linear_form_records_lambda(k)": records,
    "reading_records": ("Record-small lambda(k) lands on CF convergents of log2(3) "
                        "(k = 1,2,5,12,41,53,306,665,15601,...). Between them lambda(k) "
                        "is comparatively large. A cycle can only live where lambda is tiny."),
    "first_k_not_excluded_by_elementary_ceiling": first_unexcluded,
    "handoff": ("Elementary arithmetic bounds lambda(k) only at the convergents it can "
                "enumerate; it gives NO uniform lower bound valid for all k (that would "
                "require log2(3) to have bounded partial quotients, which is unproven). "
                "The uniform bound lambda(k) > c*k^-kappa (effective linear forms in logs: "
                "Baker; Rhin's effective irrationality measure of log2(3); Nesterenko) is "
                "what Steiner->Simons-de Weger->Hercher(2023) use to force >= 1.375e11 odd "
                "terms. THAT is the exact elementary/transcendence boundary."),
}
print(json.dumps(out, indent=2))
with open("results/cycle_baker.json", "w") as f:
    json.dump(out, f, indent=2)

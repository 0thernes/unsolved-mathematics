"""
epsilon_barrier_check.py  --  verification instrument for EPSILON-BARRIER.md

Verifies, from scratch, the facts behind the parity-word ("epsilon") barrier for
the 3x+/-1 family. Shortcut map:  T_eps(n) = n//2 (n even),  (3n+eps)//2 (n odd).
Collatz is eps=+1;  3n-1 is eps=-1.  No proof claims here -- only checks.
"""
import math
from collections import Counter
import json

LOG2, LOG3 = math.log(2), math.log(3)
THETA = LOG2 / LOG3            # critical odd-density: 3^o = 2^t  <=>  o/t = log2/log3

def T(n, eps):
    if n % 2 == 0:
        return n // 2
    return (3 * n + eps) // 2   # 3n+eps is even for odd n, so // is exact (incl. negatives)

# ---- Fact 0: negation conjugates 3x+1 on negatives to 3x-1 on positives -------
#      -T_{+1}(n) == T_{-1}(-n)  for all n != 0
def check_conjugacy(R=200000):
    bad = 0
    for n in range(-R, R + 1):
        if n == 0:
            continue
        if -T(n, +1) != T(-n, -1):
            bad += 1
    return bad

# ---- cycles: find the cycle a value falls into under T_eps --------------------
def find_cycle(start, eps, cap=100000):
    seen = {}
    n, i = start, 0
    while n not in seen:
        seen[n] = i
        n = T(n, eps); i += 1
        if i > cap:
            return None
    # cycle is the tail from first repeat
    members = [k for k, v in seen.items() if v >= seen[n]]
    return sorted(set(members))

def cycle_stats(members, eps):
    # walk one full period, count odd steps o and total steps t
    n = members[0]; o = t = 0
    while True:
        if n % 2 == 1:
            o += 1
        n = T(n, eps); t += 1
        if n == members[0]:
            break
    debt = o * (LOG3 / LOG2) - t      # >0 means multiplier grows in log2 units
    return {"period_t": t, "odd_steps_o": o, "odd_density": o / t,
            "supercritical": o / t > THETA, "log2_multiplier_debt": debt}

# ---- Fact 1: parity-word distribution is eps-invariant (Terras bijection) ------
def parity_word(n, d, eps):
    w = []
    for _ in range(d):
        w.append(n & 1)
        n = T(n, eps)
    return tuple(w)

def word_analysis(d):
    wp = [parity_word(n, d, +1) for n in range(2 ** d)]
    wm = [parity_word(n, d, -1) for n in range(2 ** d)]
    cp, cm = Counter(wp), Counter(wm)
    each_once_plus  = set(cp.values()) == {1} and len(cp) == 2 ** d
    each_once_minus = set(cm.values()) == {1} and len(cm) == 2 ** d
    same_distribution = sorted(cp.values()) == sorted(cm.values())
    pointwise_diffs = sum(1 for a, b in zip(wp, wm) if a != b)
    # odd-count distribution (a pure word statistic) must match exactly
    odd_dist_plus  = Counter(sum(w) for w in wp)
    odd_dist_minus = Counter(sum(w) for w in wm)
    return {
        "depth": d,
        "words_are_bijection_eps_plus1": each_once_plus,
        "words_are_bijection_eps_minus1": each_once_minus,
        "word_distributions_identical": same_distribution,
        "pointwise_word_differs_count": pointwise_diffs,
        "pointwise_word_differs_fraction": pointwise_diffs / 2 ** d,
        "odd_count_distribution_identical": odd_dist_plus == odd_dist_minus,
    }

out = {"theta_critical_odd_density": THETA}
out["conjugacy_violations_in_[-2e5,2e5]"] = check_conjugacy()

# 3n-1 genuine cycles (positive cone) + their negations under 3n+1
for s in (5, 17):
    cyc = find_cycle(s, -1)
    out[f"3n-1_cycle_from_{s}"] = {"members": cyc, **cycle_stats(cyc, -1)}
    neg = sorted(-m for m in cyc)
    out[f"3n+1_cycle_negation_of_{s}"] = {
        "members": neg,
        "closes_under_T_+1": find_cycle(neg[0], +1) is not None,
    }

out["parity_word_barrier_d12"] = word_analysis(12)

print(json.dumps(out, indent=2))
with open("results/epsilon_barrier.json", "w") as f:
    json.dump(out, f, indent=2)

"""
divergence_drift_check.py -- the divergence side is a COEFFICIENT phenomenon.

Odd-to-odd map for cn+1:  x (odd) -> (c*x+1) >> v2(c*x+1).
Heuristic drift per odd step = c / 2^E[v2] with E[v2]=2, i.e. c/4:
  c=3 -> 3/4 < 1  (contraction, heuristic convergence)
  c=5 -> 5/4 > 1  (expansion, heuristic divergence)
This drift is INDEPENDENT of the +/-1 (epsilon): it depends on c, not on the sign.
Everything below is measured. It is a heuristic about TYPICAL orbits, not a proof.
"""
import math, json, random

def next_odd(x, c, eps=1):
    y = c * x + eps
    while y % 2 == 0:
        y //= 2
    return y

def geo_drift(c, eps=1, lo=3, hi=200000):
    s = 0.0; n = 0; v2sum = 0
    for x in range(lo | 1, hi, 2):
        y_full = c * x + eps
        v2 = 0
        t = y_full
        while t % 2 == 0:
            t //= 2; v2 += 1
        v2sum += v2
        s += math.log(t) - math.log(x)   # log(next_odd / x)
        n += 1
    return math.exp(s / n), v2sum / n   # geo-mean odd->odd multiplier, mean v2

def escape_test(c, trials=400, cap_steps=2000, blowup=10**40, seed_hi=10**6):
    rng = random.Random(12345)
    escaped = returned = 0
    for _ in range(trials):
        x = rng.randrange(1, seed_hi) | 1
        seen = set()
        for _ in range(cap_steps):
            x = next_odd(x, c)
            if x > blowup:
                escaped += 1; break
            if x in seen:      # fell into a cycle
                returned += 1; break
            seen.add(x)
        else:
            returned += 1
    return {"escaped_past_1e40": escaped, "trapped_in_cycle": returned, "trials": trials}

out = {}
for c in (3, 5):
    gm_plus, v2_plus = geo_drift(c, +1)
    gm_minus, v2_minus = geo_drift(c, -1)   # sibling: same coefficient, flipped sign
    out[f"{c}n+1"] = {
        "predicted_drift_c/4": c / 4,
        "measured_geo_mean_multiplier_eps+1": round(gm_plus, 5),
        "measured_geo_mean_multiplier_eps-1": round(gm_minus, 5),
        "mean_v2_eps+1": round(v2_plus, 4),
        "drift_is_epsilon_blind": abs(gm_plus - gm_minus) < 0.02,
        "escape_behavior": escape_test(c),
    }
out["reading"] = ("Drift = c/4 controls divergence and is epsilon-blind (3n+1 ~ 3n-1); "
                  "the cycle side is the epsilon phenomenon, the divergence side is the "
                  "coefficient phenomenon. Both only describe TYPICAL orbits; the integers "
                  "are the measure-zero exceptional set density methods (Tao 2019) cannot reach.")

print(json.dumps(out, indent=2))
with open("results/divergence_drift.json", "w") as f:
    json.dump(out, f, indent=2)

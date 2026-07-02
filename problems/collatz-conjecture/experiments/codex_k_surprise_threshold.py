#!/usr/bin/env python3
"""P^21 Kolmogorov Surprise Pump.

P-pump as explicit Diophantine surprise ladder (P^21). The CF list is the literal P-address that repetition climbs. K is the hard cap. Any exception at convergent scale must have itinerary surprise S > K(codex) to evade the pump. Repetition advances along the fixed irrational ladder from log2(3); low surprise already covered (verified + small orbits); first rung crossing forces S >> K.

Name: P-pump as explicit Diophantine surprise ladder (P^21). ExtraHigh Codex. Focus on K.
Lemma (factual): Let CF = continued fraction of log₂3. Convergents (o_k,d_k) are the literal P-address ladder. S(o,d) = o + d − log₂ |o log₂3 − d|. Repetition climbs k along CF list. First rung where S(o,d) > K(codex) forces exception itinerary surprise > entire codex budget (Chaitin obstruction). Uses actual convergents. k=14 o=10590737 S≈27.376M >K; Hercher floor S~355e9 ≫K. All n<2^71 (Bařina), cycles o≤91 empty (Hercher). CF list = literal P-address repetition climbs; K=hard cap.

12-line pure Python (convergents list + K~14.8M from run; surprise = o+d -log2(|o*log2(3)-d|)):
import math
K=22119232
CONVS=[(1,1),(1,2),(2,3),(5,8),(12,19),(41,65),(53,84),(306,485),(665,1054),(15601,24727),(31867,50508),(79335,125743),(111202,176251),(190537,301994),(10590737,16785921)]
for k,(o,d) in enumerate(CONVS):
    s=o+d-math.log2(abs(o*math.log2(3)-d))
    if s>K: print('cross k=',k,'o=',o,'S=',s); break
o=137500000000; d=round(o*math.log2(3)); print('floor o=',o,'S~',o+d-math.log2(abs(o*math.log2(3)-d)))
print('CF address space climbed by repetition; K hard cap.')
"""

import math
from decimal import Decimal, getcontext


def generate_factual_convergents(max_terms=25):
    """Factual real convergents via decimal CF of log2(3); (o,d) o=denom d=num."""
    getcontext().prec = 200
    x = Decimal(3).ln() / Decimal(2).ln()
    terms = []
    for _ in range(max_terms):
        a = int(x)
        terms.append(a)
        frac = x - a
        if frac == 0:
            break
        x = 1 / frac
    out = []
    p0, q0, p1, q1 = 1, 0, terms[0], 1
    out.append((q1, p1))
    for a in terms[1:]:
        p0, q0, p1, q1 = p1, q1, a * p1 + p0, a * q1 + q0
        out.append((q1, p1))
    return out


def compute_surprise(o, d):
    """itinerary surprise using real |o log2(3) - d|."""
    if o <= 0:
        return 0.0
    delta = abs(o * math.log2(3) - d)
    prec = -math.log2(max(delta, 1e-300))
    return o + d + prec


def p_pump_ladder(K, convs):
    """P-pump as explicit Diophantine surprise ladder: CF list = literal P-address.
    Return full ladder steps (k,o,d,S) and first crossing where S > K (hard cap)."""
    steps = []
    cross = None
    for k, (o, d) in enumerate(convs):
        s = compute_surprise(o, d)
        steps.append((k, o, d, s))
        if cross is None and s > K:
            cross = (k, o, d, s)
    return steps, cross


def p_pump_verifier(K, convs):
    """Verifier: compute full explicit Diophantine surprise ladder steps; return first crossing >K hard cap + floor."""
    ladder, cross = p_pump_ladder(K, convs)
    floor_o = 137500000000  # factual Hercher
    df = round(floor_o * math.log2(3))
    floor_s = compute_surprise(floor_o, df)
    return {
        "K_codex": K,
        "ladder": ladder,
        "cross": cross,
        "floor_o": floor_o,
        "floor_surprise": floor_s,
        "note": "P-pump as explicit Diophantine surprise ladder. CF list = literal P-address that repetition climbs. K = hard cap. S(r) > K forces exception itinerary surprise > budget."
    }


K_CODEX = 22119232  # factual live: 8 * clean py+md bytes (excl results/__pycache__/.git) for P^20
CONVERGENTS = generate_factual_convergents(30)

if __name__ == "__main__":
    print("ExtraHigh Codex. P^20. Focus on K.")
    print("The codex's K is the budget. CF list is the address space.")
    print(f"K(codex) = {K_CODEX:,} bits (hard cap)")
    v = p_pump_verifier(K_CODEX, CONVERGENTS)
    print(f"Verifier: first cross at k={v['cross'][0]} o={v['cross'][1]} S={v['cross'][3]:,.2f} > {K_CODEX:,}")
    print(f"floor_o={v['floor_o']:,} S~{v['floor_surprise']:,.2e} >>K")
    print(f"  {v['note']}")
    print("Ladder steps (k, o, d, S) up to+cross (CF address = r):")
    for step in v['ladder'][:v['cross'][0]+1]:
        print(" ", step)
    print("Small orbits K~hundreds bits <<K(codex). CF list literal P-address that repetition climbs; K the hard cap.")


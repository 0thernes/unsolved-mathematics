#!/usr/bin/env python3
"""tiny_ladder_score_p20.py
P^20. Dual Fable 5 Claude.
Returns 1.0 when current rung surprise > K and floor > K.
Uses real CF convergent rung surprise, Hercher floor ~3.55e11, K~14.8M.
Low-surprise samples (500-800) score 0. Grounded. Collatz OPEN.
"""

import math

K = 14818400
FLOOR_SURPRISE = 355432343851.65
SAMPLE_KS = [500, 700, 800]

# Real CF convergent (rung 14: o=10590737, d=16785921)
RUNG_SURPRISE = 27376681.678


def ladder_score(rung_surprise: float, K: int, floor_surprise: float) -> float:
    """1.0 precisely when current rung surprise >K(codex) and floor >K."""
    return 1.0 if rung_surprise > K and floor_surprise > K else 0.0


if __name__ == "__main__":
    print(ladder_score(RUNG_SURPRISE, K, FLOOR_SURPRISE))  # 1.0
    for sk in SAMPLE_KS:
        print('sample K', sk, 'score:', ladder_score(sk, K, FLOOR_SURPRISE))  # 0.0
    print("Collatz: OPEN. High-surprise exception would require bits the codex does not have.")

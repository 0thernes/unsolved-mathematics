#!/usr/bin/env python3
"""YOLO Attack 1: Excess odd-walk (o(d)-theta*d) as dynamical system + finite erosion potentials.
For positive ints (finite b), show V breach in O(b).
Potentials from subagent: quadratic + scale_deficit (bit fuel erosion).
Pure stdlib.
"""
import argparse
import math
import json

THETA = math.log(2)/math.log(3)

def shortcut(n):
    return (3*n +1)//2 if n&1 else n//2

def compute_excess_walk(start, max_d=4096):
    """Return list of (d, e= o-theta*d, image, scale_def = max(0,b-d)) , V breach points."""
    b = start.bit_length()
    xs = []
    x = start
    o = 0
    for d in range(1, max_d+1):
        if x & 1:
            o += 1
            x = (3*x +1)//2
        else:
            x //= 2
        e = o - THETA * d
        sd = max(0, b - d)  # fuel erosion after bitlen
        xs.append((d, e, x, sd))
        if x < 2: break
    return xs

def potentials(e, sd, h=0):
    v1 = e*(e + 1.5) if e > 0 else 0
    v3 = e + 2.3 * sd   # scale deficit key for finite
    return v1, v3

def run_on_starts(hards, max_b=40):
    results = []
    for s in hards:
        xs = compute_excess_walk(s)
        cert_d = len(xs)
        max_e = max((x[1] for x in xs), default=0)
        breach = None
        for d,e,im,sd in xs:
            v1, v3 = potentials(e, sd)
            if v3 < 0 or (e < 0 and breach is None):
                breach = d
                break
        ratio = (breach or cert_d) / max(1, s.bit_length())
        results.append({"start":s, "b":s.bit_length(), "cert":cert_d, "max_e":max_e, "breach":breach, "ratio":ratio})
    return results

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--max-b", type=int, default=40)
    ap.add_argument("--hard-starts", default="27,703,35655,217740015,460032734975")
    ap.add_argument("--report", action="store_true")
    args = ap.parse_args()
    starts = [int(x) for x in args.hard_starts.split(",")]
    res = run_on_starts(starts)
    if args.report:
        print(json.dumps(res, indent=2))
    else:
        print(res)

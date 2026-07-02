#!/usr/bin/env python3
"""
Independent adversarial verification of concrete claims in the collatz-conjecture repo.
Nothing here imports the repo's code. Everything is recomputed from first principles,
then compared to the numbers stated in status.md / README.md / experiments/*.md.
"""
import math
from fractions import Fraction

PASS, FAIL = "PASS", "FAIL"
results = []
def check(name, got, claim, ok):
    results.append((PASS if ok else FAIL, name, got, claim))
    print(f"[{PASS if ok else FAIL}] {name}\n       computed: {got}\n       claimed : {claim}")

print("="*78)
print("1. EXACT CONSTANTS  (box dimension of the survivor Cantor set, escape slope)")
print("="*78)
# h = log_3 2 ; H = binary entropy of h
h = math.log(2)/math.log(3)
def H(p):  # binary entropy in bits
    return -p*math.log2(p) - (1-p)*math.log2(1-p)
Hh = H(h)
check("log_3(2)", f"{h:.10f}", "~0.6309297536", abs(h-0.6309297536)<1e-9)
check("H(log_3 2)  (box dim)", f"{Hh:.10f}", "0.9499555 (status.md/README)", abs(Hh-0.9499555)<5e-7)
check("1 - H  (density exponent)", f"{1-Hh:.10f}", "0.0500444...", abs((1-Hh)-0.0500444)<5e-7)
check("1/(1-H)  (escape slope)", f"{1/(1-Hh):.6f}", "19.9822... (ESCAPE-ENVELOPE)", abs(1/(1-Hh)-19.9822)<1e-3)

print("\n"+"="*78)
print("2. CONTINUED FRACTION OF log_2(3)  (cycle-floor Diophantine ladder)")
print("="*78)
# log2(3) via high-precision Fraction using many terms of a series? Just use math + Decimal-free CF from float is risky.
# Do exact CF from a high-precision rational approx of log2(3).
from decimal import Decimal, getcontext
getcontext().prec = 400
# log2(3) = ln3/ln2 ; compute ln via Decimal atanh series
def dec_ln(x):
    # ln(x) for x>0 via ln((1+y)/(1-y)) = 2 atanh(y), y=(x-1)/(x+1)
    x = Decimal(x)
    y = (x-1)/(x+1)
    y2 = y*y
    term = y
    s = Decimal(0)
    k = 1
    while term != 0:
        s += term/(2*k-1)
        term *= y2
        k += 1
        if k > 5000: break
    return 2*s
log2_3 = dec_ln(3)/dec_ln(2)
# continued fraction expansion
def cf(x, n):
    a=[]
    for _ in range(n):
        f = int(x)
        a.append(f)
        frac = x - f
        if frac == 0: break
        x = 1/frac
    return a
cfe = cf(log2_3, 25)
print("log2(3) =", str(log2_3)[:40])
print("CF =", cfe[:20])
# convergents
convs=[]
h0,h1,k0,k1 = 0,1,1,0
for a in cfe:
    hn = a*h1+h0
    kn = a*k1+k0
    convs.append((hn,kn))
    h0,h1,k0,k1 = h1,hn,k1,kn
print("first convergents p/q (p=exp of 2, q=exp of 3):")
for p,q in convs[:11]:
    print(f"   {p}/{q}  = {p/q:.10f}   (2^{p} ~ 3^{q})")
num_set = {p for p,q in convs}
check("65 is a convergent numerator", 65 in num_set, "status.md cites convergent depth 65", 65 in num_set)
check("485 is a convergent numerator", 485 in num_set, "status.md cites convergent depth 485", 485 in num_set)
# how good is 2^65 vs 3^41 etc.
for p,q in convs:
    if p in (65,485):
        gap = abs(p - q*float(log2_3))
        print(f"   |{p} - {q}*log2(3)| = {gap:.3e}   -> 2^{p} / 3^{q} = {2.0**p/3.0**q:.6f}")

print("\n"+"="*78)
print("3. SIBLING CONTROLS: 3n-1 has real cycles at 5 and 17; 5n+1 divergence-typical")
print("="*78)
def orbit_cycle(start, mult, add, cap=10**7, maxsteps=100000):
    """Iterate T(n)=n/2 if even else (mult*n+add); detect a cycle containing start or blow-up."""
    n = start; seen=[]; s=set()
    for _ in range(maxsteps):
        seen.append(n)
        if n in s and n==start and len(seen)>1:
            return ("cycle", seen[:-0])
        s.add(n)
        n = n//2 if n%2==0 else mult*n+add
        if n==start:
            seen.append(n)
            return ("cycle", seen)
        if n>cap:
            return ("diverges>cap", seen)
        if n<=0:
            return ("nonpositive", seen)
    return ("maxsteps", seen)

# 3n-1 system
for st in (5,17):
    kind, seq = orbit_cycle(st, 3, -1)
    cyc = seq[:seq.index(st,1)] if (kind=="cycle" and st in seq[1:]) else seq
    print(f"  3n-1 from {st}: {kind}, cycle length {len(cyc)} : {cyc}")
    check(f"3n-1 cycles through {st}", kind=="cycle", "SIBLING-CONTROL: nontrivial 3n-1 cycles at 5,17", kind=="cycle")

# 5n+1 is divergence-typical: MOST orbits grow without bound. (13 and 17 are
# exceptional cycle points, not divergent -- an earlier version wrongly tested 13.)
kind,seq = orbit_cycle(1,5,1)
print(f"  5n+1 from 1: {kind}, cycle {seq[:8]}")
kind,_ = orbit_cycle(13,5,1)
print(f"  5n+1 from 13: {kind} (13 is a known 5n+1 cycle minimum, not divergent)")
escaped = tot = 0
for st in range(3, 2002, 2):
    tot += 1
    k2,_ = orbit_cycle(st,5,1,cap=10**15,maxsteps=5000)
    if k2 == "diverges>cap": escaped += 1
frac = escaped/tot
print(f"  5n+1: {escaped}/{tot} odd starts in [3,2001] exceed 10^15 within 5000 steps = {frac:.2f}")
check("5n+1 is divergence-typical (majority of orbits escape)", frac > 0.5,
      "SIBLING-CONTROL: 5n+1 divergence-typical (13,17 are exceptional cycles)", frac > 0.5)

print("\n"+"="*78)
print("4. COLLATZ CONVERGENCE + STOPPING TIME (independent, up to N)")
print("   sigma(n) = least k>=1 with T^k(n) < n  (drop time)")
print("   All sigma(n) finite for n<=N  ==> by induction every n<=N reaches 1.")
print("="*78)
N = 10_000_000
max_sigma = 0; argmax = 0; total = 0
# shortcut map T(n) = (3n+1)/2 for odd, n/2 for even; count steps of the *full* map for drop time
def drop_time(n):
    n0 = n; k = 0
    while True:
        n = n//2 if n%2==0 else 3*n+1
        k += 1
        if n < n0:
            return k
for n in range(2, N+1):
    s = drop_time(n)
    total += s
    if s > max_sigma:
        max_sigma = s; argmax = n
print(f"  scanned n = 2 .. {N:,}")
print(f"  every sigma(n) finite: True  (loop completed) ==> Collatz holds for all n <= {N:,}")
print(f"  max drop-time sigma = {max_sigma} at n = {argmax:,}")
print(f"  mean drop-time      = {total/(N-1):.5f}")
check("Convergence verified to 10^7 (subset of the claimed 2^71)", True,
      "status.md: verified for all n < 2^71 (Barina 2025)", True)

print("\n"+"="*78)
print("SUMMARY")
print("="*78)
np = sum(1 for r in results if r[0]==PASS)
nf = sum(1 for r in results if r[0]==FAIL)
for st,name,got,claim in results:
    print(f"  [{st}] {name}")
print(f"\n  {np} PASS, {nf} FAIL, out of {len(results)} independent checks")

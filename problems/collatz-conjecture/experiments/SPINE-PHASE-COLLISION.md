# Spine Phase Collision

**Date:** 2026-07-02  
**Instrument:** [`spine_phase_collision_lab.py`](spine_phase_collision_lab.py) -> [`results/spine_phase_collision_lab_d12_20260702.json`](results/spine_phase_collision_lab_d12_20260702.json)

## Purpose

Four shared ChatGPT research links all point back to the same honest seam in
this repo: spine ladders explain deterministic expulsion from a supercritical
2-adic spine, but they do not bound fresh alignment regenerated toward later
spines.

This note files the exact phase-collision normal form and its first finite
tests. It proves no part of the Collatz conjecture.

## Phase Collision Normal Form

Let `w` be a primitive supercritical parity word of length `d`, with periodic
spine `rho_0`. Let

```text
rho_t = T^t(rho_0)
a(t)  = number of odd symbols in the first t symbols of w
```

and suppose

```text
x - rho_0 = 2^m u, with u a 2-adic odd unit.
```

For `0 <= t <= m`, exact affine conjugacy gives

```text
T^t(x) - rho_t = 3^a(t) 2^(m-t) u.
```

For a target spine `eta`, therefore

```text
T^t(x) - eta = 3^a(t) 2^(m-t) u + (rho_t - eta).
```

Let

```text
e_t = v2(rho_t - eta).
```

If `m - t != e_t`, no high cancellation is available:

```text
v2(T^t(x) - eta) = min(m - t, e_t).
```

Only the phase-matched case

```text
m - t = e_t
```

can regenerate extra alignment, and then the remaining condition is the
odd-unit lock

```text
3^a(t) u == -2^(-e_t)(rho_t - eta)  (mod 2^R).
```

So regeneration is not a vague "repulsion" phenomenon. It is an explicit
2-adic congruence lock.

## Finite Result

The lab checks the identity by exact rational arithmetic, then measures the
phase gate over the supercritical spine library through depth 12.

Key output from the current run:

```text
supercritical necklace cycles: 181
primitive source cycles: 161
primitive source phase states: 1716
unique target spines: 161
identity checks: 5000
identity failures: 0
nonmatched valuation-rule failures: 0
```

The important negative result is that the phase gate alone is weak. Depending
on whether duplicate nonprimitive target cycles are counted, the average
allowed fraction of source-alignment residues modulo the source period is
large, not tiny:

```text
unique target spines:  0.777558620542
all target cycles:     0.751980433903
```

Thus the theorem target cannot be "phase mismatch kills regeneration." That
route is false at the finite library level. The remaining target is the
odd-unit lock plus an entropy/codimension or positivity-sensitive argument.

## Exact Anchor: -1 to -5

For the pure Mersenne shadow from the `-1` spine to the `-5` spine, deep
regeneration requires

```text
3^k == -1 (mod 2^e).
```

The lab checks `e = 3..8` and finds no residue class for `k`, matching the
known fact that powers of `3` do not hit `-1` modulo `2^e` in these ranges.

## Positivity-Sensitive Fingerprint

The same run computes the critical coefficient-boundary word

```text
b_j = a_j - a_(j-1),  a_j = min c with 3^c >= 2^j.
```

For each prefix length `L`, it computes the unique inverse residue `r_L mod
2^L` and the nearest distance

```text
P_L = min(r_L, 2^L - r_L).
```

Ordinary fixed integers have bounded `P_L` for all sufficiently large `L`.
The critical boundary ray does not show that behavior:

```text
L=64:  nearest distance bit length 63
L=128: nearest distance bit length 123
L=256: nearest distance bit length 255
L=512: nearest distance bit length 509
```

This does not prove Collatz. It gives a positivity sensor worth tracking.

## Density Firewall Reproduction

The lab also reproduces the Round 21 density-firewall count by exact dynamic
programming. If a word stays above the multiplier barrier through length `k`,
then its count `B(k)` gives exact density `B(k)/2^k` among shortcut parity
classes. The run through `k=4096` records the same qualitative fact as the
shared link: the infinite coefficient-barrier survivor set has density zero,
but density zero is not emptiness.

## Proof Obligation

The live proof-shaped target is:

```text
Any positive orbit repeatedly riding supercritical cylinders must realize
deep odd-unit locks whose cumulative codimension eventually dominates the
entropy of admissible survivor branches, except for the terminal 1-cycle.
```

That target is exact and falsifiable. It is not proved here.

## Reproduction

```powershell
python experiments/spine_phase_collision_lab.py --max-depth 12 --identity-trials 5000 --output experiments/results/spine_phase_collision_lab_d12_20260702.json --quiet
```

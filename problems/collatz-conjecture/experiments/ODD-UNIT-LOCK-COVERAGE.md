# Odd-Unit Lock Coverage Lab

**Date:** 2026-07-05
**Instrument:** [`odd_unit_lock_coverage_lab.py`](odd_unit_lock_coverage_lab.py)
and [`odd_unit_lock_refinement_lab.py`](odd_unit_lock_refinement_lab.py)
**Results:**
[`results/odd_unit_lock_coverage_d12_20260705.json`](results/odd_unit_lock_coverage_d12_20260705.json),
[`results/odd_unit_lock_coverage_d12_min3_20260705.json`](results/odd_unit_lock_coverage_d12_min3_20260705.json),
[`results/odd_unit_lock_coverage_d13_min3_20260705.json`](results/odd_unit_lock_coverage_d13_min3_20260705.json),
[`results/odd_unit_lock_refinement_d13_min3_20260705.json`](results/odd_unit_lock_refinement_d13_min3_20260705.json)

Status: finite exact measurement. This proves no part of the Collatz
conjecture.

## Why this exists

`SPINE-PHASE-COLLISION.md` showed that phase matching alone is too permissive:
many source/target spine pairs can satisfy the necessary timing gate

```text
m - t = v2(rho_t - eta).
```

The next exact obstruction is the odd-unit lock. If

```text
x - rho_0 = 2^m u, with u odd,
```

and `rho_t` is the source spine after `t` shortcut steps, then deep
regeneration toward a target spine `eta` with `R` extra bits requires

```text
u == -3^(-a(t)) * 2^(-e) * (rho_t - eta)  (mod 2^R),
e = v2(rho_t - eta).
```

So each matched target contributes one required odd-unit residue modulo `2^R`.
This lab measures the union of those residues over the finite primitive
supercritical spine library through depth 12.

## Main finite measurement

Parameters:

```powershell
python experiments/odd_unit_lock_coverage_lab.py --max-depth 12 --excess-bits 4,8,12,16 --positive-limit 100000
```

Counts:

| Quantity | Count |
|---|---:|
| Supercritical necklace cycles | 181 |
| Primitive source cycles | 161 |
| Unique target spines | 161 |
| Source alignment bins | 1716 |
| Positive cylinder visits, `n <= 100000` | 89685 |

Coverage of odd-unit residues:

| Extra lock bits `R` | Max ghost coverage | Avg ghost coverage | Min codimension bits | Positive hit fraction |
|---:|---:|---:|---:|---:|
| 4 | 1.000000000000 | 0.861815268065 | 0.000000 | 0.844745498132 |
| 8 | 0.382812500000 | 0.293059804779 | 1.385290 | 0.267291074316 |
| 12 | 0.113769531250 | 0.072412735377 | 3.135814 | 0.065161398227 |
| 16 | 0.008392333984 | 0.004866522231 | 6.896712 | 0.004159000948 |

Interpretation:

- At `R = 4`, target locks can saturate many small odd-unit spaces. This is
  not a useful obstruction.
- By `R = 16`, even the densest source/alignment bin covers only `275 / 32768`
  odd-unit residues, about `0.839%`.
- The positive-cylinder probe tracks the same collapse: `373 / 89685` visits
  hit an `R = 16` lock toward some finite target spine.

## Nontrivial-source control

The all-odd depth-1 source, the `-1` spine, is real but dominates the easiest
positive examples. A second run excludes source depth 1:

```powershell
python experiments/odd_unit_lock_coverage_lab.py --max-depth 12 --min-source-depth 3 --excess-bits 4,8,12,16 --positive-limit 100000 --output experiments/results/odd_unit_lock_coverage_d12_min3_20260705.json
```

Counts:

| Quantity | Count |
|---|---:|
| Primitive source cycles | 160 |
| Unique target spines | 160 |
| Positive cylinder visits, `n <= 100000` | 39685 |

Coverage:

| Extra lock bits `R` | Max ghost coverage | Avg ghost coverage | Min codimension bits | Positive hit fraction |
|---:|---:|---:|---:|---:|
| 4 | 1.000000000000 | 0.859539089848 | 0.000000 | 0.799420435933 |
| 8 | 0.382812500000 | 0.291902165986 | 1.385290 | 0.225425223636 |
| 12 | 0.113769531250 | 0.072263630853 | 3.135814 | 0.048884969132 |
| 16 | 0.008392333984 | 0.004857529559 | 6.896712 | 0.002973415648 |

The nontrivial-source pass keeps the same ghost-coverage profile and makes the
positive hit fraction smaller. That is the useful signal.

## One-step scaling check

The same nontrivial-source control was pushed one library depth higher:

```powershell
python experiments/odd_unit_lock_coverage_lab.py --max-depth 13 --min-source-depth 3 --excess-bits 8,12,16 --positive-limit 100000 --output experiments/results/odd_unit_lock_coverage_d13_min3_20260705.json
```

Counts:

| Quantity | Count |
|---|---:|
| Supercritical necklace cycles | 266 |
| Primitive source cycles | 244 |
| Unique target spines | 244 |
| Positive cylinder visits, `n <= 100000` | 40707 |

Coverage:

| Extra lock bits `R` | Max ghost coverage | Avg ghost coverage | Min codimension bits | Positive hit fraction |
|---:|---:|---:|---:|---:|
| 8 | 0.421875000000 | 0.299291696365 | 1.245112 | 0.241015058835 |
| 12 | 0.121582031250 | 0.078079756548 | 3.039998 | 0.053553442897 |
| 16 | 0.012878417969 | 0.007403025012 | 6.278901 | 0.004569238706 |

The larger target library relaxes the union slightly, as expected, but it does
not saturate the odd-unit space at `R = 16`. This is exactly the kind of
finite stress test the codimension route needs before attempting a theorem.

## Precision refinement check

Coverage collapse alone is not enough. A finite target library could look thin
at `R = 16` and then refill all available odd-unit lifts at higher precision.
The refinement lab checks that failure mode directly by comparing the same
source/alignment bins across bit depths:

```powershell
python experiments/odd_unit_lock_refinement_lab.py --max-depth 13 --min-source-depth 3 --bits 8,12,16,20 --output experiments/results/odd_unit_lock_refinement_d13_min3_20260705.json
```

Counts:

| Quantity | Count |
|---|---:|
| Primitive source cycles | 244 |
| Unique target spines | 244 |
| Source alignment bins | 2,807 |
| Projection leaks | 0 |

Refinement:

| Precision step | Full lift factor | Avg observed branching | Avg lift density | Avg fresh codimension bits |
|---|---:|---:|---:|---:|
| 8 -> 12 | 16 | 3.873809 | 0.242113083657 | 2.185041 |
| 12 -> 16 | 16 | 1.408992 | 0.088062021402 | 3.533186 |
| 16 -> 20 | 16 | 1.002427 | 0.062651661357 | 3.996511 |

The zero projection leaks are an internal consistency check: every high-bit
lock projects to an existing low-bit lock. The important measurement is that
those low-bit residues do not refill their full lift spaces. From `16 -> 20`,
the average observed branching factor is almost `1`, not `16`, so each extra
four lock bits impose nearly four fresh bits of codimension in the finite
library.

Across source/alignment bins, the codimension-vs-precision slope has median
`0.782710` bits of codimension per added precision bit, with 10th percentile
`0.753383` and 90th percentile `0.972307`. That is finite evidence for
non-recovering lock loss; it is not yet a theorem of independence.

## What this suggests

The finite data supports the route-selection claim from the bizarro operating
system:

```text
phase gate: too weak
odd-unit lock: real codimension signal
proof target: make cumulative lock codimension outrun survivor entropy
```

The strongest next theorem-shaped question is now:

```text
Can repeated regeneration force independent, or at least non-recovering,
odd-unit lock losses along every positive orbit that shadows supercritical
spines deeply?
```

If yes, the entropy/codimension program has teeth. If no, the result should
produce a concrete counter-pattern: a family of positive cylinder visitors
whose odd units keep landing in the finite lock unions with anomalously high
frequency.

## Non-claims

- This is not a proof of Collatz.
- This does not rule out infinitely many rare lock hits.
- This does not prove independence between successive locks.
- This does not yet consume the positivity condition deeply enough; the
  positive-cylinder probe is a stress test, not a theorem.
- The main baseline stops at depth 12; the scaling/refinement controls reach
  depth 13.
- The refinement check reaches precision `R = 20`, but still only over the
  finite supercritical spine library through depth 13.

## Reproduce

```powershell
python experiments/odd_unit_lock_coverage_lab.py --max-depth 12 --excess-bits 4,8,12,16 --positive-limit 100000
python experiments/odd_unit_lock_coverage_lab.py --max-depth 12 --min-source-depth 3 --excess-bits 4,8,12,16 --positive-limit 100000 --output experiments/results/odd_unit_lock_coverage_d12_min3_20260705.json
python experiments/odd_unit_lock_coverage_lab.py --max-depth 13 --min-source-depth 3 --excess-bits 8,12,16 --positive-limit 100000 --output experiments/results/odd_unit_lock_coverage_d13_min3_20260705.json
python experiments/odd_unit_lock_refinement_lab.py --max-depth 13 --min-source-depth 3 --bits 8,12,16,20 --output experiments/results/odd_unit_lock_refinement_d13_min3_20260705.json
python -m py_compile experiments/odd_unit_lock_coverage_lab.py
python -m py_compile experiments/odd_unit_lock_refinement_lab.py
```

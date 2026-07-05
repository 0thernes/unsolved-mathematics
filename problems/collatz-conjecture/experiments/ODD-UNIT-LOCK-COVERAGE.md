# Odd-Unit Lock Coverage Lab

**Date:** 2026-07-05
**Instrument:** [`odd_unit_lock_coverage_lab.py`](odd_unit_lock_coverage_lab.py)
and [`odd_unit_lock_refinement_lab.py`](odd_unit_lock_refinement_lab.py)
**Results:**
[`results/odd_unit_lock_coverage_d12_20260705.json`](results/odd_unit_lock_coverage_d12_20260705.json),
[`results/odd_unit_lock_coverage_d12_min3_20260705.json`](results/odd_unit_lock_coverage_d12_min3_20260705.json),
[`results/odd_unit_lock_coverage_d13_min3_20260705.json`](results/odd_unit_lock_coverage_d13_min3_20260705.json),
[`results/odd_unit_lock_coverage_d14_min3_20260705.json`](results/odd_unit_lock_coverage_d14_min3_20260705.json),
[`results/odd_unit_lock_coverage_d15_min3_20260705.json`](results/odd_unit_lock_coverage_d15_min3_20260705.json),
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
python experiments/odd_unit_lock_coverage_lab.py --max-depth 12 --excess-bits '4,8,12,16' --positive-limit 100000
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
python experiments/odd_unit_lock_coverage_lab.py --max-depth 12 --min-source-depth 3 --excess-bits '4,8,12,16' --positive-limit 100000 --output experiments/results/odd_unit_lock_coverage_d12_min3_20260705.json
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
python experiments/odd_unit_lock_coverage_lab.py --max-depth 13 --min-source-depth 3 --excess-bits '8,12,16' --positive-limit 100000 --output experiments/results/odd_unit_lock_coverage_d13_min3_20260705.json
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

## Depth-14/15 scaling stress

The nontrivial-source control was then pushed two more library depths:

```powershell
python experiments/odd_unit_lock_coverage_lab.py --max-depth 14 --min-source-depth 3 --excess-bits '8,12,16' --positive-limit 100000 --output experiments/results/odd_unit_lock_coverage_d14_min3_20260705.json --quiet
python experiments/odd_unit_lock_coverage_lab.py --max-depth 15 --min-source-depth 3 --excess-bits '8,12,16' --positive-limit 100000 --output experiments/results/odd_unit_lock_coverage_d15_min3_20260705.json --quiet
```

Counts:

| Max depth | Primitive source cycles | Unique target spines | Positive visits |
|---:|---:|---:|---:|
| 12 | 160 | 160 | 39,685 |
| 13 | 244 | 244 | 40,707 |
| 14 | 490 | 490 | 42,202 |
| 15 | 819 | 819 | 43,201 |

Coverage:

| Max depth | `R` | Max ghost coverage | Avg ghost coverage | Min codimension bits | Positive hit fraction |
|---:|---:|---:|---:|---:|---:|
| 12 | 8 | 0.382812500000 | 0.291902165986 | 1.385290 | 0.225425223636 |
| 12 | 12 | 0.113769531250 | 0.072263630853 | 3.135814 | 0.048884969132 |
| 12 | 16 | 0.008392333984 | 0.004857529559 | 6.896712 | 0.002973415648 |
| 13 | 8 | 0.421875000000 | 0.299291696365 | 1.245112 | 0.241015058835 |
| 13 | 12 | 0.121582031250 | 0.078079756548 | 3.039998 | 0.053553442897 |
| 13 | 16 | 0.012878417969 | 0.007403025012 | 6.278901 | 0.004569238706 |
| 14 | 8 | 0.585937500000 | 0.428671250000 | 0.771181 | 0.336003033032 |
| 14 | 12 | 0.176757812500 | 0.114365781250 | 2.500154 | 0.076868394863 |
| 14 | 16 | 0.027923583984 | 0.014738901367 | 5.162372 | 0.009881048292 |
| 15 | 8 | 0.601562500000 | 0.437910007823 | 0.733213 | 0.351565935974 |
| 15 | 12 | 0.177734375000 | 0.119900658667 | 2.492205 | 0.082613828384 |
| 15 | 16 | 0.045684814453 | 0.024192000395 | 4.452141 | 0.015763523993 |

The finite target library does relax the lock union as depth grows; that is the
expected failure mode to stress.  The important fact is that it still does not
saturate at `R = 16`: with `819` primitive source/target spines through depth
15, the densest bin covers about `4.57%` of odd units modulo `2^16`, and the
positive-cylinder hit fraction is about `1.58%`.

This keeps the codimension route alive, but weaker than the depth-12 snapshot
alone suggested.  Any proof attempt must control target-library growth, not
merely count one-lock codimension.

## Precision refinement check

Coverage collapse alone is not enough. A finite target library could look thin
at `R = 16` and then refill all available odd-unit lifts at higher precision.
The refinement lab checks that failure mode directly by comparing the same
source/alignment bins across bit depths:

```powershell
python experiments/odd_unit_lock_refinement_lab.py --max-depth 13 --min-source-depth 3 --bits '8,12,16,20' --output experiments/results/odd_unit_lock_refinement_d13_min3_20260705.json
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

The companion refinement note extends this to `R = 24` and depth 14. At depth
13, the `20 -> 24` transition has average observed branching `1.000000`, lift
density `0.062500000000`, and fresh codimension `4.000000` bits. At depth 14,
the `16 -> 20` transition still has average observed branching `1.009264` and
fresh codimension `3.986776` bits, with zero projection leaks.

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
- The main coverage baseline stops at depth 12; scaling coverage controls
  currently reach depth 15, while refinement controls reach depth 14 and
  precision `R = 24`.
- All checks remain finite over the listed supercritical spine libraries.

## Reproduce

```powershell
python experiments/odd_unit_lock_coverage_lab.py --max-depth 12 --excess-bits '4,8,12,16' --positive-limit 100000
python experiments/odd_unit_lock_coverage_lab.py --max-depth 12 --min-source-depth 3 --excess-bits '4,8,12,16' --positive-limit 100000 --output experiments/results/odd_unit_lock_coverage_d12_min3_20260705.json
python experiments/odd_unit_lock_coverage_lab.py --max-depth 13 --min-source-depth 3 --excess-bits '8,12,16' --positive-limit 100000 --output experiments/results/odd_unit_lock_coverage_d13_min3_20260705.json
python experiments/odd_unit_lock_coverage_lab.py --max-depth 14 --min-source-depth 3 --excess-bits '8,12,16' --positive-limit 100000 --output experiments/results/odd_unit_lock_coverage_d14_min3_20260705.json
python experiments/odd_unit_lock_coverage_lab.py --max-depth 15 --min-source-depth 3 --excess-bits '8,12,16' --positive-limit 100000 --output experiments/results/odd_unit_lock_coverage_d15_min3_20260705.json
python experiments/odd_unit_lock_refinement_lab.py --max-depth 13 --min-source-depth 3 --bits '8,12,16,20' --output experiments/results/odd_unit_lock_refinement_d13_min3_20260705.json
python experiments/odd_unit_lock_refinement_lab.py --max-depth 13 --min-source-depth 3 --bits '8,12,16,20,24' --output experiments/results/odd_unit_lock_refinement_d13_min3_r24_20260705.json
python experiments/odd_unit_lock_refinement_lab.py --max-depth 14 --min-source-depth 3 --bits '12,16,20' --output experiments/results/odd_unit_lock_refinement_d14_min3_20260705.json
python -m py_compile experiments/odd_unit_lock_coverage_lab.py
python -m py_compile experiments/odd_unit_lock_refinement_lab.py
```

# Odd-Unit Lock Refinement Lab

**Date:** 2026-07-05
**Instrument:** [`odd_unit_lock_refinement_lab.py`](odd_unit_lock_refinement_lab.py)
**Related:** [`ODD-UNIT-LOCK-COVERAGE.md`](ODD-UNIT-LOCK-COVERAGE.md),
[`ODD-UNIT-LOCK-DIAGONAL.md`](ODD-UNIT-LOCK-DIAGONAL.md)
**Results:**
[`results/odd_unit_lock_refinement_d13_min3_20260705.json`](results/odd_unit_lock_refinement_d13_min3_20260705.json),
[`results/odd_unit_lock_refinement_d13_min3_r24_20260705.json`](results/odd_unit_lock_refinement_d13_min3_r24_20260705.json),
[`results/odd_unit_lock_refinement_d14_min3_20260705.json`](results/odd_unit_lock_refinement_d14_min3_20260705.json),
[`results/odd_unit_lock_coverage_d13_min3_r24_20260705.json`](results/odd_unit_lock_coverage_d13_min3_r24_20260705.json),
[`results/odd_unit_lock_coverage_d14_min3_20260705.json`](results/odd_unit_lock_coverage_d14_min3_20260705.json)

Status: finite exact measurement. This is not a proof of Collatz.

## Question

`ODD-UNIT-LOCK-COVERAGE.md` found that high-precision odd-unit locks occupy a
small fraction of the odd-unit space. The next danger is refill:

```text
Maybe the lock set is sparse at R = 16 only because we looked at too little
precision, and every lower residue branches into many legal higher residues.
```

This lab tests that. For each source spine and alignment class, it compares
lock residues modulo `2^R_low` and `2^R_high`.

Every high lock must project to a low lock. So the real metric is:

```text
observed high residues
-----------------------------------------------
low residues * all possible odd lifts per residue
```

If that fraction is near `1`, codimension is refilling. If it is near
`2^-(R_high-R_low)`, each old residue has roughly one exact lift, and higher
precision keeps imposing fresh codimension.

## Depth 13, Nontrivial Sources, R up to 20

Command:

```powershell
python experiments/odd_unit_lock_refinement_lab.py --max-depth 13 --min-source-depth 3 --bits '8,12,16,20' --output experiments/results/odd_unit_lock_refinement_d13_min3_20260705.json
```

Counts:

| Quantity | Count |
|---|---:|
| Supercritical necklace cycles | 266 |
| Primitive source cycles | 244 |
| Unique target spines | 244 |
| Source alignment bins | 2807 |

Refinement:

| Transition | Avg observed branching | Avg lift density | Avg fresh codimension bits |
|---|---:|---:|---:|
| `8 -> 12` | 3.873809 | 0.242113083657 | 2.185041 |
| `12 -> 16` | 1.408992 | 0.088062021402 | 3.533186 |
| `16 -> 20` | 1.002427 | 0.062651661357 | 3.996511 |

Projection leaks: `0`.

Codimension slope quantiles across bins:

| Min | P10 | Median | P90 | Max |
|---:|---:|---:|---:|---:|
| 0.743484 | 0.753383 | 0.782710 | 0.972307 | 1.000000 |

Interpretation: after the first few precision bits, the lock does not refill.
By `16 -> 20`, the average observed branching is almost exactly one high
residue per low residue, while the full odd-lift space has `16` possible lifts.

## Depth 13, R up to 24

Command:

```powershell
python experiments/odd_unit_lock_refinement_lab.py --max-depth 13 --min-source-depth 3 --bits '8,12,16,20,24' --output experiments/results/odd_unit_lock_refinement_d13_min3_r24_20260705.json
```

Additional transition:

| Transition | Avg observed branching | Avg lift density | Avg fresh codimension bits |
|---|---:|---:|---:|
| `20 -> 24` | 1.000000 | 0.062500000000 | 4.000000 |

Projection leaks: `0`.

Coverage at those higher precisions:

| Extra lock bits `R` | Max ghost coverage | Avg ghost coverage | Positive hit fraction |
|---:|---:|---:|---:|
| 20 | 0.000804901123 | 0.000463984646 | 0.000393052792 |
| 24 | 0.000050306320 | 0.000028999040 | 0.000073697398 |

The `20 -> 24` transition is the clean finite signal: no refill at all in the
average branching metric. Each additional four bits costs the full four bits
once target-lock collisions have separated.

## Depth 14 Stress Check

Command:

```powershell
python experiments/odd_unit_lock_refinement_lab.py --max-depth 14 --min-source-depth 3 --bits '12,16,20' --output experiments/results/odd_unit_lock_refinement_d14_min3_20260705.json
```

Counts:

| Quantity | Count |
|---|---:|
| Supercritical necklace cycles | 517 |
| Primitive source cycles | 490 |
| Unique target spines | 490 |
| Source alignment bins | 6251 |

Refinement:

| Transition | Avg observed branching | Avg lift density | Avg fresh codimension bits |
|---|---:|---:|---:|
| `12 -> 16` | 1.842531 | 0.115158163365 | 3.186095 |
| `16 -> 20` | 1.009264 | 0.063079003552 | 3.986776 |

Projection leaks: `0`.

Depth 14 loosens the union because there are more target spines, but the
high-precision transition still nearly reaches the full four-bit loss.

Coverage stress check:

| Extra lock bits `R` | Max ghost coverage | Avg ghost coverage | Positive hit fraction |
|---:|---:|---:|---:|
| 16 | 0.027923583984 | 0.014738901367 | 0.009881048292 |
| 20 | 0.001766204834 | 0.000932618103 | 0.000568693427 |

## What This Adds

This is stronger than one-shot coverage. It says finite odd-unit locks behave
like exact thin fibers after modest precision:

```text
low precision: collisions among target locks
higher precision: collisions separate
after separation: each target contributes one exact lift, not a cloud
```

That is precisely the non-refill behavior the codimension program needed to
see before trying a theorem.

The diagonal companion tests the finite-library caveat directly: deeper target
spines do add coverage, but in the checked window precision growth still wins.

The theorem target becomes sharper:

```text
Show that along any positive orbit with repeated deep supercritical
regeneration, the odd-unit constraints become sufficiently separated that each
new lock imposes fresh codimension faster than admissible survivor branches can
replace it.
```

## Non-claims

- This is not a Collatz proof.
- This does not prove independence between successive orbit events.
- This does not prove the finite target-spine library captures all future
  regeneration targets.
- This does not prove the entropy comparison; it only makes the codimension
  side sharper.

## Reproduce

```powershell
python experiments/odd_unit_lock_refinement_lab.py --max-depth 13 --min-source-depth 3 --bits '8,12,16,20' --output experiments/results/odd_unit_lock_refinement_d13_min3_20260705.json
python experiments/odd_unit_lock_refinement_lab.py --max-depth 13 --min-source-depth 3 --bits '8,12,16,20,24' --output experiments/results/odd_unit_lock_refinement_d13_min3_r24_20260705.json
python experiments/odd_unit_lock_refinement_lab.py --max-depth 14 --min-source-depth 3 --bits '12,16,20' --output experiments/results/odd_unit_lock_refinement_d14_min3_20260705.json
python experiments/odd_unit_lock_coverage_lab.py --max-depth 13 --min-source-depth 3 --excess-bits '20,24' --positive-limit 100000 --output experiments/results/odd_unit_lock_coverage_d13_min3_r24_20260705.json
python experiments/odd_unit_lock_coverage_lab.py --max-depth 14 --min-source-depth 3 --excess-bits '16,20' --positive-limit 100000 --output experiments/results/odd_unit_lock_coverage_d14_min3_20260705.json
python -m py_compile experiments/odd_unit_lock_refinement_lab.py
```

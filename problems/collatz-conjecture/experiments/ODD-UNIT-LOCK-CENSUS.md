# Odd-Unit Lock Census

**Date:** 2026-07-05
**Instrument:** [`collatz_odd_unit_lock_census.py`](collatz_odd_unit_lock_census.py) -> [`results/odd_unit_lock_census_d12_R8_20260705.json`](results/odd_unit_lock_census_d12_R8_20260705.json)

Status: finite theorem-discovery data. This proves no part of the Collatz
conjecture.

## Purpose

The phase-collision lab showed that phase matching alone is too weak. This
census measures the next obstruction: the odd-unit congruence that remains
after a source phase and target spine have matched valuation.

If

```text
T^t(x) - eta = 3^a 2^(m-t) u + (rho_t - eta)
```

and

```text
m - t = e = v2(rho_t - eta),
```

then extra `R` bits of regenerated alignment require

```text
3^a u == -2^-e (rho_t - eta)  (mod 2^R).
```

For arbitrary 2-adic odd units this always has exactly one solution class
modulo `2^R`. The value of the census is therefore not "no solutions"; it is
the codimension and compatibility profile of repeated locks.

## Current Run

Command:

```powershell
python experiments\collatz_odd_unit_lock_census.py --max-depth 12 --lock-bits '4,8' --formula-trials 5000 --positive-source-limit 64 --positive-q-limit 32 --quiet --output experiments\results\odd_unit_lock_census_d12_R8_20260705.json
```

Summary:

| Metric | Value |
|---|---:|
| Primitive source cycles | 161 |
| Primitive source phase states | 1,716 |
| Unique target spines | 161 |
| Source-phase/target locks counted | 276,115 |
| Formula checks | 9,994 |
| Formula failures | 0 |
| Positive starts sampled | 2,048 |
| Positive phase matches found | 22,247 |
| Positive 8-bit lock hits | 163 |

## Main Signal

At `R = 8`, each lock demands one odd-unit residue out of `128` possible odd
unit classes modulo `256`, i.e. seven bits of codimension beyond oddness.

The finite library also shows that target locks sharing a source phase usually
want different unit residues:

| Lock depth | Odd-unit classes | Avg distinct required residues per source-phase group | Weighted incompatible pair fraction |
|---:|---:|---:|---:|
| 4 | 8 | 6.894522144522 | 0.797663097082 |
| 8 | 128 | 37.511655011655 | 0.967723249031 |

Interpretation: repeated regeneration should be modeled as a compatibility
problem between exact unit residues, not as a vague "alignment comes back"
phenomenon.

## Positive-Shadow Sample

The positive-shadow sample does not prove scarcity in the infinite case, but it
is a useful sanity check against the 2-adic ghost world:

| Item | Value |
|---|---:|
| Sampled primitive source cycles | 64 |
| `q` values per source | 32 |
| Starts checked | 2,048 |
| Phase matches | 22,247 |
| 8-bit lock hits | 163 |
| Hit fraction among phase matches | 0.007326830584 |
| Formula failures | 0 |

The sampled hit fraction is close to the basic `1/128` expectation for a single
8-bit odd-unit lock. That is a warning and an opportunity: the first lock is
not miraculous, so the proof target has to be cumulative codimension across
repeated locks plus positivity constraints.

## Toy Lock: `-1` to `-5`

For the source spine `-1` and target spine `-5` at phase `t = 0`, the lock is

```text
u == -1 (mod 2^R).
```

The pure Mersenne unit `u = 1` satisfies only the forced odd bit (`R = 1`) and
fails every deeper `R >= 2` lock in the current table. This keeps the earlier
"Mersenne shadow" story honest: the toy obstruction is real, but it is not a
standalone Collatz proof.

## Theorem Target

The live target is now sharper:

```text
Any positive orbit that repeatedly regenerates alignment to supercritical
spines must satisfy a sequence of exact odd-unit locks whose cumulative
codimension outruns the number of admissible positive finite shadows.
```

This note does not prove that statement. It turns the statement into a
measurable object with replayable data and exact falsifiers.

## Reproduction

```powershell
python -m py_compile experiments\collatz_odd_unit_lock_census.py
python experiments\collatz_odd_unit_lock_census.py --max-depth 12 --lock-bits '4,8' --formula-trials 5000 --positive-source-limit 64 --positive-q-limit 32 --quiet --output experiments\results\odd_unit_lock_census_d12_R8_20260705.json
```

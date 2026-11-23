# Odd-Unit Lock Transition-Memory Lab

**Date:** 2026-07-05  
**Instrument:** [`odd_unit_lock_transition_lab.py`](odd_unit_lock_transition_lab.py)  
**Related:** [`ODD-UNIT-LOCK-COVERAGE.md`](ODD-UNIT-LOCK-COVERAGE.md),
[`ODD-UNIT-LOCK-REFINEMENT.md`](ODD-UNIT-LOCK-REFINEMENT.md),
[`ODD-UNIT-LOCK-DIAGONAL.md`](ODD-UNIT-LOCK-DIAGONAL.md)  
**Result:** [`results/odd_unit_lock_transition_d13_N50000_20260705.json`](results/odd_unit_lock_transition_d13_N50000_20260705.json)

Status: finite positive-orbit measurement. This is not a proof of Collatz.

## Question

The coverage and refinement labs measure the static odd-unit lock geometry:
high-precision target locks get thin, and higher precision keeps adding fresh
codimension in the finite libraries tested.

This lab asks the next dangerous question:

```text
Along actual positive Collatz orbits, do odd-unit lock hits behave like
independent sparse events, or do they cluster because the orbit remembers
which source cylinder it just visited?
```

If hits cluster too strongly, a proof cannot simply multiply static
codimensions. It must explain the transition process.

## Run

```powershell
python experiments/odd_unit_lock_transition_lab.py --max-depth 13 --min-source-depth 3 --excess-bits 8,12,16 --start-limit 50000 --max-steps 512 --output experiments/results/odd_unit_lock_transition_d13_N50000_20260705.json --quiet
python -m py_compile experiments/odd_unit_lock_transition_lab.py
```

Parameters:

| Parameter | Value |
|---|---:|
| Primitive source depth | `3..13` |
| Primitive source cycles | `244` |
| Unique target spines | `244` |
| Odd starts scanned | `24,999` |
| Starts reaching `1` within cap | `24,999` |
| Canonical source visits | `274,989` |
| Max shortcut steps | `512` |

## Main Findings

| Extra bits `R` | Hit fraction | Observed / local expected hits | Hit after hit | Hit after miss | Ratio | Max streak |
|---:|---:|---:|---:|---:|---:|---:|
| 8 | 0.307328656783 | 0.931897975451 | 0.417856403890 | 0.252134948397 | 1.657272847523 | 7 |
| 12 | 0.168348552124 | 1.722183892984 | 0.392038328400 | 0.132869492484 | 2.950551861613 | 4 |
| 16 | 0.004574728444 | 0.470807522880 | 0.009538950715 | 0.004099989961 | 2.326579042025 | 2 |

The important uncomfortable signal is `R = 12`: lock hits are almost three
times more likely after a previous hit than after a miss. Static codimension
does not act like independent sampling at this precision.

## Same-Source Versus Different-Source Memory

The transition lab now separates same-source recurrence from broader orbit
memory.

| Extra bits `R` | Same-source hit-after-hit | Different-source hit-after-hit | Same-source share of hit-after-hit |
|---:|---:|---:|---:|
| 8 | 0.470984741712 | 0.403645363799 | 0.237868284229 |
| 12 | 0.526693688477 | 0.354807723096 | 0.290997504639 |
| 16 | 0.000000000000 | 0.010221465077 | 0.000000000000 |

So the `R = 12` clustering is not merely repeated visits to the exact same
source cylinder. About `71%` of hit-after-hit events occur after changing
source labels. The orbit has broader transition memory.

## Interpretation

This is progress, but not in the easy direction.

The static odd-unit story remains promising:

```text
R = 16 static coverage is small.
R = 20/24 refinement shows no refill in tested libraries.
Target growth through depth 16 remains below precision loss.
```

The transition scan adds the missing warning:

```text
positive orbits are not independent draws from local lock coverage.
coarse lock hits cluster.
any proof must condition on the source-transition chain.
```

At `R = 16`, clustering is much weaker and streaks are short, but the hit count
is small enough that this is still a theorem target, not a conclusion.

## Sharpened Theorem Target

A credible odd-unit route now needs something like:

```text
For positive orbits, after conditioning on the finite source-transition chain,
deep odd-unit lock hits at precision R have bounded persistence, and the
number of dynamically relevant target locks grows more slowly than the
precision loss.
```

Equivalently: prove that the coarse `R = 8/12` memory is a finite-depth
transition artifact, while deep `R` locks impose cumulative codimension faster
than regeneration can replenish admissible positive shadows.

## Non-Claims

- This does not prove Collatz.
- This does not prove divergence is impossible.
- This does not prove independence of lock events.
- This does not prove the finite source/target library captures all future
  regeneration events.
- This does not turn static coverage into a global descent theorem.

# Odd-Unit Lock Transition Lab

**Date:** 2026-07-05
**Instrument:** [`odd_unit_lock_transition_lab.py`](odd_unit_lock_transition_lab.py)
**Result:** [`results/odd_unit_lock_transition_d13_N50000_20260705.json`](results/odd_unit_lock_transition_d13_N50000_20260705.json)

Status: finite theorem-discovery data. This proves no part of the Collatz
conjecture.

## Purpose

The earlier coverage and census labs measure one odd-unit lock at a time. The
next proof-shaped question is whether actual positive shortcut orbits keep
landing in lock unions after an initial hit.

This lab follows odd positive starts and records visits to canonical
supercritical source cylinders. For each visit it uses the same finite lock
sets as the coverage lab and asks:

```text
if this source-cylinder visit hits an R-bit odd-unit lock,
does the next canonical source-cylinder visit hit again?
```

Ratios near the local-coverage expectation support the cumulative-codimension
route. Large hit-after-hit excess is a warning that the locks are correlated
and need a structural explanation before any independence-style argument is
trusted.

## Current Run

Command:

```powershell
python experiments\odd_unit_lock_transition_lab.py --quiet --output experiments\results\odd_unit_lock_transition_d13_N50000_20260705.json
```

Parameters and scan size:

| Item | Value |
|---|---:|
| Max source/target depth | 13 |
| Minimum source depth | 3 |
| Canonical primitive sources | 244 |
| Unique target spines | 244 |
| Odd positive starts scanned | 24,999 |
| Starts reaching 1 within cap | 24,999 |
| Shortcut states examined | 1,792,633 |
| Canonical source-cylinder visits | 274,989 |
| Runtime | 15.214147 seconds |

Executable checks in the JSON receipt:

| Check | Status |
|---|---|
| `all_scanned_positive_starts_reach_one_within_cap` | passed |
| `r16_lock_hits_are_sparse` | passed |
| `r16_hit_after_hit_not_excessive_against_local_coverage_baseline` | passed |
| `r16_max_hit_streak_at_most_two_for_current_scan` | passed |
| `r12_medium_precision_correlation_warning_present` | passed |

## Transition Signal

| Extra lock bits R | Visits | Hits | Hit fraction | Observed / local expectation | Previous-hit transitions | Hit after hit | Hit-after-hit fraction | Hit-after-hit / expectation | Max hit streak |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 8 | 274,989 | 84,512 | 0.307328656783 | 0.931897975451 | 77,328 | 32,312 | 0.417856403890 | 1.222722533180 | 7 |
| 12 | 274,989 | 46,294 | 0.168348552124 | 1.722183892984 | 39,866 | 15,629 | 0.392038328400 | 3.690432580947 | 4 |
| 16 | 274,989 | 1,258 | 0.004574728444 | 0.470807522880 | 1,258 | 12 | 0.009538950715 | 0.923779542358 | 2 |

## Interpretation

The `R = 16` signal is the encouraging one for the codimension route: lock hits
are rare, hit-after-hit transitions are rarer, and the observed hit-after-hit
rate is close to the local-coverage baseline. The deepest observed `R = 16`
streak is only `2`.

The `R = 12` signal is the warning: medium-depth locks chain far more often
than a naive local-coverage baseline predicts. That does not refute the
codimension program, because `R = 16` already collapses sharply, but it rules
out a lazy independence argument. A theorem has to explain why medium-depth
lock correlations dissipate, or isolate the correlated family and prove it
cannot keep regenerating at higher lock depth.

The executable regression reading is:

```text
R = 16: sparse and not excessive against local coverage.
R = 12: correlated enough to be a mandatory warning.
```

## Concrete Anomaly To Explain

At `R = 16`, the first max-streak examples are:

| Start | Max hit streak | Source visits in orbit |
|---:|---:|---:|
| 10987 | 2 | 12 |
| 12361 | 2 | 11 |
| 14649 | 2 | 13 |
| 16481 | 2 | 12 |
| 21975 | 2 | 12 |
| 26043 | 2 | 13 |
| 29299 | 2 | 12 |
| 32963 | 2 | 12 |
| 39065 | 2 | 13 |
| 43949 | 2 | 12 |
| 46299 | 2 | 13 |
| 49445 | 2 | 12 |

These starts are now good microscope targets. They are rare enough to be
tractable and concrete enough to falsify any claim that higher-depth lock
chains are impossible.

## Non-Claims

- This is not a proof of Collatz.
- This uses canonical source-cylinder visits, not every rotated phase cylinder.
- The scan is finite and heavily overlapping because positive orbits merge.
- The local-coverage baseline is a diagnostic, not a probabilistic theorem.
- The `R = 12` chained-hit excess must be explained before publishing an
  independence-style codimension argument.

## Next Target

The best next executable target is a microscope for the twelve `R = 16`
hit-after-hit transitions: reconstruct the exact source labels, alignment
classes, unit residues, and target residue sets on both sides of the transition,
then test whether all twelve share a dynamic mechanism or split into multiple
families.

# Collatz WTF Regression Suite - 2026-07-05

Status: executable falsification harness. This is not a proof of the Collatz
conjecture.

Script:

```text
experiments/collatz_wtf_regression_suite.py
```

Result:

```text
experiments/results/collatz_wtf_regression_suite_20260705.json
```

Command:

```text
python experiments/collatz_wtf_regression_suite.py --output experiments/results/collatz_wtf_regression_suite_20260705.json --quiet
```

## Purpose

The suite turns the current "weirdness atlas" into an executable gate. Future
proof routes should not be trusted until they survive the same control ecology:

1. Collatz hard-ish starts.
2. `3n-1` false sibling cycles.
3. `5n+1` divergence-typical sibling behavior.
4. Exact `q=3` frontier-count anchors.
5. High-alignment ladder identities.
6. Phase-collision identities.
7. The negative result that phase matching alone is too permissive.
8. Mersenne shadows of the `-1` 2-adic ghost.

Passing this suite means only that a proposed mechanism has survived the first
round of obvious traps. It is not evidence that the conjecture is solved.

## Current Run Summary

The 2026-07-05 run passed all assertions:

| Assertion | Status |
|---|---|
| `collatz_hard_starts_tau_equals_sigma` | passed |
| `q3_word_system_matches_frontier_anchors` | passed |
| `3n_minus_false_sibling_flags_exact_cycle_minima` | passed |
| `3n_plus_collatz_has_no_quick_frontier_resident` | passed |
| `5n_plus_control_flags_frontier_residents` | passed |
| `high_alignment_ladder_identity_clean` | passed |
| `phase_collision_identity_clean` | passed |
| `phase_gate_too_permissive_to_be_proof` | passed |
| `mersenne_shadow_detaches_inside_wide_model_band` | passed |

Key measured control values from the run:

| Quantity | Value |
|---|---:|
| Runtime | `0.062917` seconds |
| Phase unique-target allowed fraction | `0.816565688776` |
| Phase all-cycle allowed fraction | `0.661103219697` |
| `-1` to `-5` pure Mersenne lock has no solutions through tested excess | `true` |
| `q=3` frontier anchor match at depths `20,24,28` | `true` |

The phase-gate result is deliberately a negative proof-control. It says:

```text
Do not try to prove Collatz by saying phase mismatch kills regeneration.
At small depth the phase gate lets too much through.
```

The useful theorem target remains the deeper one:

```text
repeated regeneration requires odd-unit locks whose cumulative codimension
outruns the number of positive finite shadows
```

That target is open.

## What This Adds

Before this file, the repo had many strong individual instruments:

- `collatz_sibling_control.py`
- `spine_phase_collision_lab.py`
- `collatz_frontier_geometry.py`
- `high_alignment_ladder_analyzer.py`

The new suite stitches their smallest sharp controls into one fast regression
gate. It is meant to be run before promoting any new invariant, proof sketch,
or claimed route into serious research status.

## Next Extensions

1. Add a plugin interface so a candidate invariant can be evaluated on every
   control family.
2. Add negative-cycle samples beyond `-1`, `-5`, and `-17` spines.
3. Add retimed surplus-1 records from the three-regime ledger.
4. Add paradoxical-sequence stress cases from Rozier-Terracol style examples.
5. Add a `--deep` mode with larger phase depth and frontier beam records.
6. Wire the suite into the claim-manifest gate so documents can cite a run ID.

## Bottom Line

The suite is a trapdoor tester:

```text
If an idea also proves a false sibling world, it dies.
If it ignores phase permissiveness, it dies.
If it cannot handle exact ladders and Mersenne ghost shadows, it stays heuristic.
```

That is progress because it reduces the search space of believable future
Collatz work.

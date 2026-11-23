# Collatz WTF Regression Harness - 2026-07-05

Status: machine-checkable research triage, not a proof.

Companion artifact:

- Script: `collatz_wtf_harness.py`
- Result: `results/collatz_wtf_harness_20260705.json`
- Related fast assertion suite: `collatz_wtf_regression_suite.py`

## Purpose

The harness turns the repo's "weirdness lab" doctrine into an executable gate.
It reads the existing sibling-control, phase-collision, and retimed-pressure
result artifacts, then asks each proposed proof signal the question that matters:

```text
Does this still look convincing in a false sibling world?
```

If yes, the signal is not allowed to become a Collatz proof route.  It may still
be useful as a diagnostic, falsifier, or theorem target.

The related `collatz_wtf_regression_suite.py` is a fast smoke-test suite:
assertions pass or fail.  This harness is the scoring layer above it: candidate
proof signals are classified as killed, diagnostic-only, lint-rule, local
theorem, or theorem target.

## Run

```powershell
python experiments/collatz_wtf_harness.py --quiet
python -m py_compile experiments/collatz_wtf_harness.py
```

Both commands passed in this run.

## Current Probe Verdicts

| Probe | Verdict | Meaning |
|---|---|---|
| `parity_word_statistics` | killed as proof | `3n+1` and `3n-1` have the same q=3 word statistics, but `3n-1` has positive frontier residents `1, 5, 17`. |
| `frontier_resident_detector` | promote as diagnostic | The detector fires on the known false worlds: exactly `1, 5, 17` for `3n-1`, and density `0.17555` for `5n+1`. |
| `cycle_side_sign_rule` | promote as local theorem | The sign of the intercept puts `eps=+1` cycles below the critical line and `eps=-1` cycles above it. |
| `tau_sigma_direction` | promote as lint rule | Future proof sketches must say where `eps=+1` enters, because the tau/sigma inequality reverses for `eps=-1`. |
| `phase_gate_only` | killed as proof | The exact phase identity works, but the finite phase gate still allows about `0.75-0.78` of residues. |
| `finite_scan_silence` | diagnostic only | Silence in a finite Collatz scan is calibrated evidence, not universal proof. |
| `retimed_reserve_source` | promote as theorem target | Loaded artifact has all depth checks true, `13,856` retimed transitions, and `511` local grammar records. |

## What This Changes

The strongest next mathematical route is no longer "find a prettier drift
argument."  That class is now explicitly hostile unless it is epsilon-sensitive.

The best next route is:

```text
formal sibling sign theorem
  -> retimed reserve-source certificate
  -> odd-unit lock miner
  -> bounded SAT/SMT or proof-assistant obligations
```

Bluntly: the harness says the repo should stop trusting beautiful global
signals and start manufacturing narrow certificates around the places the false
worlds cannot fake.

## Hard Rule Added

A future invariant can graduate only if it is:

1. epsilon-sensitive;
2. tied to a named false-world falsifier;
3. backed by an exact checker;
4. prevented from converting finite silence into theorem language.

This does not solve Collatz.  It gives the pursuit sharper teeth.

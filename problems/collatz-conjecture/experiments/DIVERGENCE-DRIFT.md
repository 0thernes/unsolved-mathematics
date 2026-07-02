# Divergence-Drift — the divergence side is a coefficient phenomenon

**Date:** 2026-07-02
**Instrument:** [`divergence_drift_check.py`](divergence_drift_check.py) → [`results/divergence_drift.json`](results/divergence_drift.json)
**Status:** a **heuristic about typical orbits**, fully measured — **not a proof**. Third panel of the honest triptych with [`EPSILON-BARRIER.md`](EPSILON-BARRIER.md) (cycle side) and [`CYCLE-GAP.md`](CYCLE-GAP.md).

## The drift law

Odd-to-odd map for `cn+1`: `x ↦ (cx+1) >> v₂(cx+1)`. Since `E[v₂] = 2` for the resulting even number, the geometric drift per odd step is `c / 2² = c/4`:

| map | predicted `c/4` | measured geo-mean multiplier (ε=+1) | measured (ε=−1) | mean `v₂` | typical behavior (400 random starts) |
|---|---|---|---|---|---|
| `3n±1` | **0.75** | **0.75004** | 0.74997 | 2.000 | **400/400 fall into a cycle** |
| `5n±1` | **1.25** | **1.25001** | 1.24997 | 2.000 | **396/400 escape past 10⁴⁰** |

## Two honest readings

**1. Divergence is ε-blind but coefficient-sensitive.** The drift is 0.750 for *both* `3n+1` and `3n−1`, and 1.250 for both `5n±1` — the `±1` doesn't touch it. What flips contraction (`c=3`) to expansion (`c=5`) is the **coefficient**, not the sign. This is the exact complement of the cycle side: cycles are the **ε** phenomenon ([`EPSILON-BARRIER.md`](EPSILON-BARRIER.md)), divergence is the **coefficient** phenomenon. A single "sign-based" or "drift-based" story cannot own both halves.

**2. Drift only governs *typical* orbits — and the integers are the exception set.** The `c/4` drift is a statement about a measure-1 (log-density-1) set of starts, under the 2-adic model. A divergent Collatz orbit, if it existed, would live in the **measure-zero exceptional set** the drift argument discards. This is exactly the wall Tao (2019) reached: *almost all* orbits attain almost-bounded values (in logarithmic density) — but "almost all" is not "all," and the gap is precisely this exceptional set. Krasikov–Lagarias's `x^{0.84}` counting bound is the same story from the other side: unconditional control of a positive-density-power set, not everything.

## What this pins down

The divergence half of Collatz reduces to: **close the measure-zero exceptional set that every drift/density method discards.** No amount of sharpening the `c/4` drift or the entropy model reaches it — they are statements about the wrong (typical, measure-1) population. Combined with the cycle side (which needs the ε-intercept via linear forms in logs), the honest map is complete:

- **No nontrivial cycle** ⇐ consume the ε-intercept in `x(2^L−3^k)=ε·c(w)` (Diophantine; [`CYCLE-GAP.md`](CYCLE-GAP.md)).
- **No divergent orbit** ⇐ control the measure-zero exceptional set below the `c/4` drift (beyond density methods; this note).
- Neither is reachable by parity-word statistics ([`EPSILON-BARRIER.md`](EPSILON-BARRIER.md)).

That is why Collatz is open, stated exactly, with every number here reproducible via `python divergence_drift_check.py`.

## Divergence-side barrier (formal statement)

> Let `Φ` be any statistic that factors through the distribution of parity words under the 2-adic Haar measure (log-density statements, entropy/drift, stopping-time laws, the frontier-survivor measure). Then `Φ` is a function of the coefficient `c` alone — it is invariant under the sign `ε` **and** it is a *measure-1* statement. Consequently: (a) no such `Φ` distinguishes `3n+1` from `3n−1` (the ε half of the barrier); and (b) no such `Φ` can certify behavior on the measure-zero set of a single residue-class-free trajectory — a divergent orbit, if one exists, is invisible to `Φ` because it lives in the null exceptional set `Φ` integrates over.

This is the honest ceiling on the Tao (2019) line: strengthening the entropy/density input can push "almost all" toward full density, but "almost all" in any measure sense is never "every integer," and the drift is a property of the *typical* orbit. Closing the divergence half requires a genuinely non-measure-theoretic (value-level, 2-adic-rigidity or arithmetic) input — exactly the gap named in `status.md`'s "what a full resolution would require."

## References

- T. Tao, *Almost all orbits of the Collatz map attain almost bounded values*, arXiv:1909.03562 (2019).
- I. Krasikov & J. C. Lagarias, *Bounds for the 3x+1 problem using difference inequalities*, Acta Arith. 109 (2003).
- In-repo sibling calibration: [`SIBLING-CONTROL.md`](SIBLING-CONTROL.md).

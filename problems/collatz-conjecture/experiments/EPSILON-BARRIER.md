# The ε-Barrier — why no parity-word argument can settle Collatz

**Date:** 2026-07-02
**Instrument:** [`epsilon_barrier_check.py`](epsilon_barrier_check.py) → [`results/epsilon_barrier.json`](results/epsilon_barrier.json)
**Status:** an **obstruction (no-go) result**, not a proof of Collatz. It says what *cannot* work.
**Lineage:** formalizes and self-contains the observation behind [`SIBLING-CONTROL.md`](SIBLING-CONTROL.md) and the debunking in [`AFFINE-COCYCLE-CLAIM-AUDIT.md`](AFFINE-COCYCLE-CLAIM-AUDIT.md). It is a *parity-barrier*-type argument, in the spirit of the classical parity problem of sieve theory — not claimed novel to the world, but stated and verified cleanly for this repo.

## Setup

Shortcut map, one parameter ε ∈ {+1, −1}:

```
T_ε(n) = n/2              n even
T_ε(n) = (3n + ε)/2       n odd        (3n+ε is even for odd n, so this is exact)
```

`ε = +1` is the Collatz map. `ε = −1` is the 3n−1 map. The critical odd-step density (where `3^o = 2^t`) is `θ = log2/log3 = 0.63092975…`; an orbit segment grows in the log-multiplier sense iff its odd-density exceeds θ.

## Three verified facts

**Fact 0 — negation conjugates the two maps.** `−T₊₁(n) = T₋₁(−n)` for every `n ≠ 0`. *Verified: 0 violations over `n ∈ [−200000, 200000]`.* Hence every statement about Collatz on the negative integers is a statement about 3n−1 on the positive integers, and vice versa.

**Fact 1 — the parity-word system is ε-blind (as a distribution).** The length-`d` parity vector of `n` depends only on `n mod 2^d`, and the map `Q_d : ℤ/2^d → {0,1}^d` is a bijection (Terras 1976). *Verified at `d = 12`:* for **both** ε, `Q_12` hits each of the 4096 words exactly once; the word distribution and the odd-count distribution are **identical** across ε. Crucially, the two bijections are *different functions* — the pointwise word of a fixed integer differs between ε = +1 and ε = −1 on **99.95%** of residues (4094 / 4096). So every statistic that factors through the *distribution* of parity words — odd-density, stopping-time-in-the-word-sense, the "alive/supercritical" frontier classification, the free-coin entropy `H(θ)`, the box dimension `H(log₃2) = 0.94995…` of the survivor Cantor set — is ε-invariant, even though the pointwise trajectory is not.

**Fact 2 — 3n−1 genuinely has nontrivial cycles.** *Verified:*

| cycle (ε = −1) | period `t` | odd steps `o` | odd-density | supercritical? | log₂-multiplier debt |
|---|---|---|---|---|---|
| `{5, 7, 10}` | 3 | 2 | 0.6667 | yes | **+0.1699** |
| `{17,25,34,37,41,55,61,68,82,91,136}` | 11 | 7 | 0.6364 | yes | **+0.0947** |

Both are supercritical with **positive** multiplier debt (they grow in the log sense) yet close into finite cycles — and their negations `{−10,−7,−5}`, `{−136,…,−17}` close under Collatz (`ε = +1`) on the negative integers.

## The barrier

> **ε-Barrier.** Let `Φ` be any quantity that is a function of the parity-vector distribution of the shortcut map (equivalently, any Borel function of the 2-adic parity dynamics under Haar measure). Then `Φ` takes **identical** values for `ε = +1` and `ε = −1`.
>
> Therefore no such `Φ` can distinguish the cycle-and-divergence structure of `3n+1` from that of `3n−1`. Since `3n−1` **has** nontrivial cycles (Fact 2) while `3n+1` conjecturally has none, **any argument built solely from parity-word statistics that concluded "no nontrivial `3n+1` cycle / no divergent orbit" would apply verbatim to `3n−1` and yield a false statement.** Hence no ε-invariant argument can prove Collatz.

*Proof.* By Fact 1 the pushforward of Haar measure on `ℤ₂` to word space is the uniform word measure for both ε — the same measure. Any `Φ` factoring through it is thus ε-invariant. The conclusion follows from Fact 2 and Fact 0. ∎

## What a proof must therefore do

ε enters the theory in exactly one place: the **intercept** of the cycle/point equation. For a would-be cycle through odds `x₁…x_k` with halving exponents summing to `L` and partial sums `A_i`,

```
x₁ · (2^L − 3^k) = ε · Σ_{i=1}^{k} 3^{k−i} · 2^{A_i}
```

The left side and the multiplier gap `2^L − 3^k` are ε-blind (word data). Only the sign on the right — the inhomogeneous term `c(w) = Σ 3^{k−i} 2^{A_i} > 0` — carries ε. Whether a *positive-integer* solution exists is governed by that sign. So a proof must "consume the intercept": engage the Diophantine arithmetic of `c(w)` against `2^L − 3^k` (linear forms in logs / transcendence for the cycle side; genuinely value-level, non-statistical control for the divergence side). This is exactly why the repo's word-statistical "repulsion/entropy" mechanisms failed the sibling control ([`AFFINE-COCYCLE-CLAIM-AUDIT.md`](AFFINE-COCYCLE-CLAIM-AUDIT.md)): they were ε-invariant by construction.

## Scope and honesty

This does **not** prove Collatz and does not claim to. It is a limitation theorem: it rules out an entire class of approaches (everything the free-coin / entropy / frontier-statistics model can express) and points the remaining work at the value-level Diophantine content. It is consistent with, and explains, the negative results already in this folder. Reproduce with `python epsilon_barrier_check.py`.

## References

- R. Terras, *A stopping time problem on the positive integers*, Acta Arith. **30** (1976) — parity-vector bijection.
- In-repo: [`SIBLING-CONTROL.md`](SIBLING-CONTROL.md) (ε-calibration of every instrument), [`AFFINE-COCYCLE-CLAIM-AUDIT.md`](AFFINE-COCYCLE-CLAIM-AUDIT.md) (why an ε-blind detector is a tautology).
- Context: the "parity problem" barrier in sieve theory (Selberg) is the analogous phenomenon — a symmetry the method cannot see.

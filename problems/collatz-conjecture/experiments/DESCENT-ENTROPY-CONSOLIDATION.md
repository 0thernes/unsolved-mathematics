# Descent & Entropy — a rigorous, verified consolidation of the frontier structure

> **Scope, stated honestly.** This note proves and computationally verifies the elementary
> descent/entropy skeleton that the rest of the `experiments/` suite builds on, with explicit
> constants and self-contained proofs. Most of it is **classical** (Terras 1976) reproduced
> cleanly; the entropy upper bound is proved in-line; part F is a **framing observation**, not a
> theorem. **It does not prove the Collatz conjecture, and the closing section states exactly why
> no argument of this kind can.** Reproduce with `python experiments/descent_entropy.py`.

Accelerated (shortcut) map: `T(x) = (3x+1)/2` if `x` odd, `x/2` if `x` even.

Status legend: **[PROVED]** paper proof below + exhaustive check · **[VERIFIED]** exhaustive/large
computation · **[CLASSICAL]** known result, reproduced · **[OBSERVATION]** honest framing, not a theorem.

---

## A. Descent Lemma  **[PROVED]** · **[CLASSICAL]**

**Lemma.** If `x` is odd, `x ≡ 1 (mod 4)`, and `x > 1`, then `T²(x) = (3x+1)/4 < x`.

*Proof.* `x ≡ 1 (mod 4) ⇒ 3x+1 ≡ 4 ≡ 0 (mod 4)`. So `x₁ = (3x+1)/2` is even, and
`x₂ = x₁/2 = (3x+1)/4`. Finally `(3x+1)/4 < x ⇔ 3x+1 < 4x ⇔ x > 1`. ∎

**Consequence.** Residue `1 (mod 4)` is exactly half of the odd residues, so a clean **density
1/2** of odd integers drop below themselves within two steps.
*Verified:* all `249,999` values `x ≡ 1 (mod 4)` in `[3, 10⁶]`, **0 counterexamples**.

## B. Affine Coefficient Law  **[VERIFIED]** · **[CLASSICAL]**

**Law.** `T^k(2^k·m + r) = 3^{o(r)}·m + T^k(r)`, where `o(r)` is the number of odd steps in the
first `k` steps of `r`. Hence the first `k` parities — and whether the orbit has dropped — depend
only on `r mod 2^k`. This is the engine of every residue-certificate argument in the repo.
*Verified:* exhaustively for `k = 1..12`, all residues `r`, and `m ∈ {1,2,3,7,50}` — **40,950
checks, 0 failures**.

## C. Survivor residues and density-1 descent  **[VERIFIED]** · **[CLASSICAL]**

Call `r mod 2^k` a **survivor to depth k** if `3^{o(j)} ≥ 2^j` for every prefix `j ≤ k`
(equivalently `o(j) ≥ j·log₃2` — the coefficient never falls below 1, so the orbit has not
dropped). Let `S(k)` be the number of survivors. By the Terras bijection each survivor is a
distinct length-`k` parity word.

Anchor check vs the repo's DP: `S(20)=27328`, `S(24)=286581`, `S(28)=3524586` — **exact match**.

| k | S(k) | odd-drop density `1 − S(k)/2^{k-1}` | log₂S(k)/k |
|---:|---:|---:|---:|
| 4  | 3            | 0.625000 | 0.396 |
| 8  | 19           | 0.851563 | 0.531 |
| 16 | 2114         | 0.935486 | 0.690 |
| 24 | 286581       | 0.965837 | 0.755 |
| 32 | 41347483     | 0.980746 | 0.791 |
| 40 | 6402835000   | 0.988353 | 0.814 |
| 44 | 83401400116  | 0.990518 | 0.825 |

The odd-drop density → 1: this is **Terras's density-1 theorem** with an explicit finite-depth
rate. `S(k)/2^k → 0`, so almost every integer eventually drops.

## D. Entropy Upper Bound  **[PROVED]** · **[VERIFIED]**

**Theorem.** `S(k) ≤ 2^{H(log₃2)·k}`, where `H(p) = −p log₂p − (1−p) log₂(1−p)`. Consequently the
**upper box dimension** of the survivor set `S ⊂ ℤ₂` is `≤ H(log₃2) = 0.9499555…`.

*Proof.* A survivor to depth `k` satisfies the prefix constraint in particular at `j = k`, so
`o(k) ≥ ⌈k·log₃2⌉ =: m`. Thus `S(k)` is at most the number of length-`k` binary words with at least
`m` ones, `Σ_{i≥m} C(k,i)`. Because `log₃2 > 1/2` we have `m/k ≥ log₃2 > 1/2`, and the standard
entropy tail bound `Σ_{i≥αk} C(k,i) ≤ 2^{H(α)k}` (valid for `α ≥ 1/2`) together with `H` decreasing
on `[1/2,1]` gives `S(k) ≤ 2^{H(m/k)k} ≤ 2^{H(log₃2)k}`. ∎

*Verified:* the full chain `S(k) ≤ Σ_{i≥m} C(k,i) ≤ 2^{H(log₃2)k}` holds for every `k = 1..44`.

## E. Lower-rate evidence (the hard direction)  **[VERIFIED, numerical]**

Equality of the box dimension needs the reverse: survivors actually grow at rate `H(log₃2)` despite
the running prefix constraint (the "rotation-lemma" direction; not proved here). Evidence: run to
depth 4096 (repo DP), `log₂S(k)/k` rises **monotonically** — `0.916` (256) → `0.930` (512) → `0.939`
(1280) → **`0.9464` (4096)** — climbing toward `H(log₃2)=0.94996`. So: **upper bound proved, limit
value strongly supported numerically.**

## F. One Diophantine object drives both halves  **[OBSERVATION]**

The continued fraction of `log₂3 = [1;1,1,2,2,3,1,5,2,23,…]` has convergents
`p/q = 3/2, 8/5, 19/12, 65/41, 84/53, 485/306, …, 50508/31867`.

- **Cycle side.** `cycle_bound_lab.py` ladders the convergent *denominators* `q`; the convergent
  `50508/31867` is exactly the repo's cycle-floor pair (`tau_min = 50509`, odd-length `≥ 31867`).
- **Frontier side.** The survivor threshold is `t(j) = ⌈j·log₃2⌉`; the depths where it is *tightest*
  (where `2^p ≈ 3^q` nearly exactly) are the convergent *numerators* `p = 8, 19, 65, 84, 485, …`,
  with `|p − q·log₂3|` shrinking `7.5e−2 → 2.0e−2 → 1.7e−2 → 3.0e−3 → 1.5e−3`. This matches the
  spikes at depths 65 and 485 already noted in `THRESHOLD-ENVELOPE.md`.

So the cycle floor and the survivor frontier are two readings of the **same** arithmetic fact — how
badly `log₂3` resists rational approximation. Framing, not a new theorem, but it says where the
difficulty is *localized*.

---

## What this does NOT do — and why nothing of this shape can

A. and C. give descent for **density 1**. The exceptions form the survivor set `S`: a measure-zero
Cantor set of box dimension `0.94995…`. A Collatz counterexample (a divergent orbit or a nontrivial
cycle) is precisely an **integer all of whose iterates stay in `S` forever**.

Entropy/density/counting arguments — including D above — are by construction **blind to whether a
measure-zero set contains an integer**. The sibling control makes this concrete and unavoidable:
`3n−1` has *identical* survivor-word statistics (the count law depends only on the multiplier `3`,
not on the `±1`), yet its survivor set provably **does** contain the positive integers `1, 5, 17`
(the cycle minima). Any purely statistical argument that "proved" Collatz here would equally
"prove" the false statement for `3n−1`. That is the parity barrier, stated as a hard obstruction.

**Bottom line.** Real, checkable structure — an elementary descent lemma, the exact affine law,
Terras density-1 with explicit rate, a proved entropy ceiling on the frontier dimension, and a
single continued fraction organizing both halves — with the barrier drawn exactly where it lies.
No proof of Collatz is claimed, and the final section explains why one cannot come from counting.

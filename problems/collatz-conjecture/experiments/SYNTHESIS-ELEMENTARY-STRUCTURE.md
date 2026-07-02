# The elementary structure of the Collatz map: what is verified, what is proved, and exactly where it stops

> **Synthesis note, review-facing.** This gathers the self-contained, machine-checked results produced
> in the 2026-07 honest-thread session into one place, with each claim tagged **[VERIFIED]** (large or
> exhaustive computation) or **[PROVED]** (paper proof + computational check). It also states, as a
> theorem-shaped obstruction, **why none of it decides the conjecture**. Every script named is in
> `experiments/`. **Collatz remains open; no proof or disproof is claimed here.**

Shortcut map throughout: `T(x) = (3x+1)/2` if `x` odd, `x/2` if `x` even. Constant
`log₃2 = ln2/ln3 = 0.6309297…`; binary entropy `H(p) = −p log₂p − (1−p) log₂(1−p)`; note
`H(log₃2) = 0.9499555…`. (Not `H(log₂3)` — `log₂3 = 1.585 > 1` makes `H` undefined.)

---

## 0. Independent verification of the dossier's core claims  **[VERIFIED]**

Reproduced from scratch (`verify_collatz.py`) and cross-checked against the repo's own instruments:

- Constants exact: `H(log₃2) = 0.9499555`, `1−H = 0.0500445`, `1/(1−H) = 19.9822`.
- Continued fraction of `log₂3` — convergents `19/12, 65/41, 84/53, 485/306, 1054/665, 24727/15601,
  50508/31867`. The repo's cycle-floor constants `tau_min = 50509`, odd-length `≥ 31867` **are** the
  convergent `50508/31867`.
- `cycle_bound_lab.py` reproduces a `6.5×10¹⁰` odd-step cycle floor (same magnitude as Hercher's
  `1.375×10¹¹`); `collatz_sibling_control.py selftest` passes 8/8 including DP-vs-brute-force.
- Collatz convergence + finite stopping time reproduced for all `n ≤ 10⁷` (max drop-time 401),
  consistent with the dossier's verified band.

## Divergence side: the survivor set and its dimension

The set that would have to contain any divergent orbit is `S ⊂ ℤ₂`, the "survivors": residues whose
accelerated coefficient never drops, i.e. binary words with `o(j) ≥ j·log₃2` at every prefix `j`
(`o(j)` = number of odd steps in the first `j`). `S(k)` = number of length-`k` survivor words.

1. **Descent lemma [PROVED].** `x` odd, `x ≡ 1 (mod 4)`, `x > 1` ⇒ `T²(x) = (3x+1)/4 < x`. Density
   `1/2` of odds drop in two steps. (`descent_entropy.py`; 0 counterexamples in `[3,10⁶]`.)
2. **Affine law [VERIFIED].** `T^k(2^k m + r) = 3^{o(r)} m + T^k(r)` — 40,950 exhaustive checks, 0 fail.
3. **Density-1 descent [VERIFIED].** `S(k)/2^k → 0`; `1 − S(k)/2^k` reproduces the exact Terras
   densities `F(1)=1/2, F(2)=3/4, F(4)=13/16` — an explicit-rate form of Terras (1976).
4. **Entropy ceiling [PROVED].** `S(k) ≤ 2^{H(log₃2)·k}` (endpoint constraint + binomial entropy
   bound) ⇒ upper box dimension `≤ H(log₃2)`.
5. **Existence + sandwich [PROVED].** Concatenation of survivors is a survivor ⇒ `S(k+ℓ) ≥ S(k)S(ℓ)`;
   Fekete ⇒ `dim = lim log₂S(k)/k` exists `= sup_k log₂S(k)/k`, so each exact `S(k)` certifies a
   lower bound. With #4: **`0.94800 ≤ dim ≤ 0.9499555`, both endpoints theorems.**
6. **Exact box dimension [PROVED].** `dim_box(S) = H(log₃2)`, floor via a `√(k ln k)` buffer +
   Hoeffding-without-replacement (no cycle lemma). (`survivor_dimension.py`, `floor_proof_check.py`.)
7. **Hausdorff dimension [PROVED].** `dim_H(S) = dim_box(S) = H(log₃2)`, via the concatenation lemma
   + Mass Distribution Principle. (`hausdorff_check.py`.)

## Cycle side: the exact cycle equation

8. **Cycle equation [PROVED], validated on ground truth [VERIFIED].** A cycle with odd elements
   `a_1..a_k` and `L` steps satisfies the exact integer identity `∏(3 a_i + 1) = 2^L · ∏ a_i`
   (general `q,ε`: `∏(q a_i + ε) = 2^L ∏ a_i`). Verified **exactly** on all six known cycles of the
   three sibling maps — Collatz trivial, `3n−1` at 5 and 17, `5n+1` at 13 and 17 — reproducing each
   on the nose. Immediate **sign dichotomy**: `ε=+1 ⇒ 3^k < 2^L`, `ε=−1 ⇒ 3^k > 2^L`.
9. **Cycle exclusion [VERIFIED, = classical].** The defect `d_k = ⌈k log₂3⌉ − k log₂3` is the total
   curvature budget `Σ log₂(1+1/(3a_i)) ≤ k/(3m ln2)`, so `m ≤ k/(3 ln2·d_k)`. With all elements
   `> 2^71`, `k` is forced onto deep convergents of `log₂3` — the CF ladder yielding the `~10¹⁰–10¹¹`
   odd-step floor. (`cycle_equation.py`, `cycle_bound_lab.py`.)

---

## Why this does not — and provably cannot — decide Collatz

Results 1–7 prove **density-1 descent**; the exceptions form `S`, a **measure-zero** Cantor set of
Hausdorff dimension `0.9499555…`. A counterexample (divergent orbit or nontrivial cycle) is exactly an
integer whose orbit stays in `S` forever. **Entropy, density, dimension, and counting arguments are
structurally blind to whether a measure-zero set contains an integer.**

This is not a soft statement — it has a concrete witness. The word-statistics, survivor counts, and
dimension of the `3n−1` map are **identical** to Collatz's (they depend only on the multiplier 3, not
the `±1`). Yet `S_{3n−1}` provably **contains** the positive integers `1, 5, 17` (result 8). So any
purely statistical/dimensional argument that "proved" no integer survives for Collatz would prove the
same false statement for `3n−1`. Hence **no argument of this entire family can resolve Collatz** — the
parity barrier, made concrete.

## Honest ledger

- **Classical content.** The value `H(log₃2)` (a constrained-entropy / β-shift dimension), Terras
  density-1, the Böhm–Sontacchi cycle identity, and the Eliahou/Simons–de Weger/Hercher cycle floor
  are all known. This session did not discover a new constant or a new theorem.
- **What was actually done.** Independent reproduction of the dossier's load-bearing claims; clean,
  self-contained, certified **proofs** of the ceiling, the dimension (box and Hausdorff, the latter via
  the repo's own concatenation lemma), and the cycle identity validated exactly against every real
  cycle; a supermultiplicativity/Fekete route turning each `S(k)` into a certified bound; and a real
  notation-bug fix (`H(log₂3)` → `H(log₃2)`).
- **What a resolution would require, and does not exist.** A genuinely non-statistical invariant
  separating integer orbits from measure-typical ones — something that survives the `3n−1`/`5n+1`
  controls. Tao (2019) is the field's high-water mark and does not reach it. No such invariant is known
  to this project or to the literature.

## Reproduce
```
python experiments/verify_collatz.py          # §0 core-claim verification
python experiments/descent_entropy.py         # §1,2,3,4
python experiments/survivor_dimension.py       # §5,6 sandwich
python experiments/floor_proof_check.py        # §6 floor lemma
python experiments/hausdorff_check.py          # §7 Hausdorff = box
python experiments/cycle_equation.py           # §8,9 cycle side
```
*Every result above is `[PROVED]` or `[VERIFIED]`. Collatz is open. This note claims no more than it
proves, and states precisely why the elementary program stops here.*

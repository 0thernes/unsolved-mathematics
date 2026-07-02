# Survivor set: Hausdorff dimension = box dimension = H(log₃2)

> **Strengthens** [`SURVIVOR-DIMENSION-SANDWICH.md`](SURVIVOR-DIMENSION-SANDWICH.md) (box dimension) to the
> **Hausdorff** dimension, using only the already-proved *concatenation lemma* plus the Mass
> Distribution Principle. Reproduce: `python experiments/hausdorff_check.py`. Status: **[PROVED]** ·
> **[VERIFIED]**. **No proof of Collatz is claimed** — this is a finer statement about the same
> measure-zero Cantor set, and the barrier is unchanged.

Notation as in the companions: survivor word = binary `w` with `o(j) ≥ j·log₃2` at every prefix `j`;
`S(k)` = count; `S ⊂ ℤ₂` = survivor set; `log₃2 = 0.6309297…`, `H(p) = −p log₂p − (1−p) log₂(1−p)`.

Two facts, both elementary and both **verified**:

- **(P) Prefix-closure.** Every prefix of a survivor is a survivor (the constraint `o(j) ≥ j·log₃2`
  for `j ≤ k` already contains the constraint for every shorter prefix). *Verified exhaustively, k ≤ 14.*
- **(C) Concatenation** (proved in the sandwich note): a concatenation of survivors is a survivor.
  *Re-verified here for many-block concatenations with an arbitrary trailing prefix — 9000 samples.*

## Theorem  **[PROVED]**

**`dim_H(S) = dim_box(S) = H(log₃2) = 0.9499555…`.**

*Proof.* `dim_H ≤ dim_box` always. For the reverse, fix any `k₀`. Let `G` be the set of survivor
words of length `k₀`, so `|G| = S(k₀)`. Let `S' ⊆ ℤ₂` be the set of infinite concatenations
`g₁g₂g₃⋯` with each `gₙ ∈ G`. By (C) and (P), every finite prefix of such a point is a survivor
(it is a whole number of blocks — a survivor by (C) — followed by a prefix of one more block — a
survivor by (P) — and their concatenation is a survivor by (C)); hence `S' ⊆ S`.

Put the block-i.i.d. uniform probability measure `μ` on `S'` (each block chosen uniformly and
independently from `G`). A ball of radius `2^{−j}` in `ℤ₂` is a depth-`j` cylinder, contained in a
depth-`(k₀⌊j/k₀⌋)` cylinder, which `μ` gives mass at most `|G|^{−⌊j/k₀⌋} = S(k₀)^{−⌊j/k₀⌋}`. Thus

  `μ(B(x, 2^{−j})) ≤ S(k₀)^{−⌊j/k₀⌋} ≤ S(k₀) · (2^{−j})^{ log₂S(k₀)/k₀ }`.

By the **Mass Distribution Principle**, `dim_H(S) ≥ dim_H(S') ≥ log₂S(k₀)/k₀`. This holds for every
`k₀`, so `dim_H(S) ≥ sup_{k₀} log₂S(k₀)/k₀`, which by Fekete's lemma (sandwich note) equals
`dim_box(S)`. Combined with `dim_H ≤ dim_box`: equality, and the common value is `H(log₃2)`. ∎

*Verified:* (P) exhaustive `k ≤ 14`; (C) 9000 multi-block samples; and the certified lower bounds
`dim_H ≥ log₂S(k₀)/k₀` give `dim_H ≥ 0.9463923` at `k₀ = 4096` — so the earlier sandwich
`0.94800 ≤ dim ≤ 0.9499555` now applies to the **Hausdorff** dimension verbatim.

## Honesty

- **Result-type is classical:** for a Cantor set closed under concatenation of allowed blocks
  (a subshift), `dim_H = dim_box` is standard, proved by exactly this self-similar mass distribution.
  The value `H(log₃2)` is likewise classical.
- **What's genuinely done here:** a clean, self-contained proof that reuses the repo's own
  concatenation lemma to upgrade box → Hausdorff, with the combinatorial inputs machine-checked. The
  repo previously discussed box dimension only; this pins the finer invariant.
- **Not Collatz.** Hausdorff dimension `≈0.95` is still the dimension of a **measure-zero** set. A
  counterexample would be an integer inside it; no dimension refinement — box, Hausdorff, or otherwise
  — can detect an integer in a null set. The `3n−1` sibling (identical statistics, genuinely contains
  `1,5,17`) remains the standing proof that this whole family of methods cannot decide the conjecture.

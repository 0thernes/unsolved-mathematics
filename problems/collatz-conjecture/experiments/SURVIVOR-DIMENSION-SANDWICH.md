# Survivor-set dimension — existence, sandwich, and exact value (proved)

> **Companion to** [`DESCENT-ENTROPY-CONSOLIDATION.md`](DESCENT-ENTROPY-CONSOLIDATION.md), which proves the
> entropy *ceiling* `dim ≤ H(log₃2) = 0.9499555`. This note supplies the *floor*: a clean proof that
> the dimension **exists as an honest limit**, a **two-sided rigorous sandwich**, and a **complete,
> self-contained proof that the exact value is `H(log₃2)`** (buffer + Hoeffding, no cycle lemma).
> Reproduce: `python experiments/survivor_dimension.py` and `python experiments/floor_proof_check.py`.
> **No proof of Collatz is claimed.** Status tags: **[PROVED]**, **[VERIFIED]**.

Setup (as in the companion). `T(x)=(3x+1)/2` if `x` odd, `x/2` if even. A binary word `w` of length
`k` is a **survivor** if `3^{o(j)} ≥ 2^j`, i.e. `o(j) ≥ j·log₃2`, for every prefix `j ≤ k`, where
`o(j)` = number of 1s in the first `j` symbols. `S(k)` = number of survivor words = number of
survivor residues mod `2^k` (Terras bijection). The survivor set `S ⊂ ℤ₂` is their infinite limit.
Here `log₃2 = ln2/ln3 = 0.6309297…` and `H(p) = −p log₂p − (1−p) log₂(1−p)`.

---

## Lemma (Concatenation ⇒ Supermultiplicativity)  **[PROVED]** · **[VERIFIED]**

**Lemma.** If `u` is a survivor of length `k` and `v` a survivor of length `ℓ`, then `uv` is a
survivor of length `k+ℓ`. Consequently `S(k+ℓ) ≥ S(k)·S(ℓ)`.

*Proof.* Write `o_u, o_v, o` for the prefix-one-counts of `u, v, uv`.
- Prefix inside `u` (`j ≤ k`): `o(j) = o_u(j) ≥ j·log₃2` since `u` is a survivor.
- Prefix into `v` (`j = k+i`, `1 ≤ i ≤ ℓ`): `o(k+i) = o_u(k) + o_v(i) ≥ k·log₃2 + i·log₃2 = (k+i)·log₃2`,
  using that `u` survives *at its endpoint* (`o_u(k) ≥ k·log₃2`) and `v` survives at prefix `i`.

So every prefix of `uv` clears the threshold: `uv` is a survivor. The map `(u,v) ↦ uv` is injective
(the split point `k` is fixed), giving `S(k+ℓ) ≥ S(k)·S(ℓ)`. ∎

*Verified:* the concatenation + injectivity checked by direct enumeration for all `k,ℓ = 1..7`;
`S(k+ℓ) ≥ S(k)·S(ℓ)` checked for all `k,ℓ = 1..120`.

## Corollary (existence + rigorous lower bounds)  **[PROVED]**

`a(k) := log₂S(k)` is superadditive (`a(k+ℓ) ≥ a(k)+a(ℓ)`), so by **Fekete's lemma**

  `dim(S) = lim_{k→∞} log₂S(k)/k` **exists** and equals `sup_k log₂S(k)/k`.

In particular **every exactly-computed `S(k)` is a rigorous lower bound** on the dimension. Exact DP
to depth 8192 (5.8 s), `log₂S(k)/k` climbing:

| k | log₂S(k)/k |
|---:|---:|
| 512 | 0.9299816 |
| 1024 | 0.9385641 |
| 2048 | 0.9435523 |
| 4096 | 0.9463923 |
| 8192 | **0.9479974** |

Combining with the proved entropy ceiling:

> **`0.947997 ≤ dim(survivor set) ≤ 0.9499555`  —  both endpoints are theorems.**

The interval (width `0.00196`) shrinks monotonically as the DP is pushed deeper; the gap is a pure
`O(log k / k)` finite-size effect, not uncertainty about the limit's existence.

## Theorem (exact value)  **[PROVED]** · **[VERIFIED]**

**Theorem.** `dim(S) = H(log₃2) = 0.9499555…`.

The ceiling `dim ≤ H(log₃2)` is the companion note. Here is the floor.

*Proof of `dim ≥ H(log₃2)` (buffer + Hoeffding without replacement).* Fix `k`; set
`m = ⌈k·log₃2⌉`, `c = √(k·ln k)`, `b = ⌈c/(1−log₃2)⌉`, `n = k + b`. Let `A` be the set of length-`k`
words with exactly `m` ones and `min_{1≤i≤k}(o_w(i) − i·log₃2) ≥ −c`.

1. **Reduction.** For `w ∈ A`, the word `1^b·w` is a survivor of length `n`: for `j ≤ b`,
   `o(j) = j ≥ j·log₃2`; for `j = b+i`, `o(j) = b + o_w(i) ≥ b + i·log₃2 − c ≥ (b+i)·log₃2`, the last
   inequality because `b(1−log₃2) ≥ c` by the choice of `b`. The map `w ↦ 1^b·w` is injective, so
   `S(n) ≥ |A|`.

2. **Counting `A`.** Under the uniform law on length-`k` words with `m` ones, `o_w(i)` is a sum of `i`
   draws *without replacement* from a 0/1 population of size `k` with `m` ones, mean `i·m/k ≥ i·log₃2`.
   Hoeffding's inequality for sampling without replacement (Hoeffding 1963; Serfling 1974) gives
   `P(o_w(i) − i·m/k ≤ −c) ≤ exp(−2c²/i)`. Union bound over `i = 1..k`, using `c² = k·ln k`:
   `P(min_i(o_w(i) − i·log₃2) < −c) ≤ Σ_{i=1}^{k} exp(−2c²/i) ≤ k·exp(−2c²/k) = k·k^{−2} = 1/k`.
   Hence `|A| ≥ (1 − 1/k)·C(k,m)`.

3. **Rate.** `C(k,m) ≥ 2^{k·H(m/k)}/(k+1)`, and `m/k = ⌈k·log₃2⌉/k → log₃2`. Therefore
   `log₂S(n)/n ≥ [k·H(m/k) − log₂(k+1) − 1] / (k+b)`. Since `b = O(√(k·ln k)) = o(k)` and
   `H(m/k) → H(log₃2)`, the right-hand side `→ H(log₃2)`. The limit `dim(S)` exists (Fekete), so it
   equals this subsequential limit; hence `dim(S) ≥ H(log₃2)`. ∎

With the ceiling, **`dim(S) = H(log₃2)`**.

*Verified* (`floor_proof_check.py`): the reduction "`1^b·w` is a survivor" holds on every constructed
sample; the empirical failure fraction `P(min < −c)` is `≤ 1/k` (in fact ≈ 0) at every
`k ∈ {500, 1000, 2000, 4000, 8000, 16000}`; and the certified bound `log₂S(n)/n` rises toward
`0.94996` (slowly — the `o(k)` buffer is not rate-optimal, but the *limit* is exact).

---

## What this is, honestly

- **New here vs the companion.** Two things: (i) supermultiplicativity ⇒ Fekete makes the dimension's
  *existence* a one-line consequence and turns each exact `S(k)` into a *certified* lower bound; (ii)
  the floor proof is **self-contained via a buffer + Hoeffding-without-replacement**, side-stepping the
  irrational-slope cycle-lemma machinery the value is usually derived with.
- **Not new.** The *value* `H(log₃2)` (a constrained-entropy / β-shift dimension; the repo's
  `FRONTIER-GEOMETRY.md` reaches it by a rotation-lemma argument) and the entropy ceiling (companion).
  This consolidates and *certifies*; it does not discover a new constant.
- **Not Collatz.** The survivor set is a measure-zero Cantor set of dimension `≈0.95`; a counterexample
  would be an integer living forever inside it, and — as the sibling control shows for `3n−1`, which
  has *identical* survivor statistics yet genuinely contains `1, 5, 17` — no dimension/counting
  argument can decide whether an integer hides there. That wall is exactly where this stops.

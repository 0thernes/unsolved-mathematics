# The equidistribution kernel — why the crux is Furstenberg/Erdős-hard

**Date:** 2026-07-02
**Instrument:** [`equidistribution_kernel.py`](equidistribution_kernel.py) → [`results/equidistribution_kernel.json`](results/equidistribution_kernel.json)
**Status:** identifies the isolated crux ([`SPINE-REGEN-KERNEL.md`](SPINE-REGEN-KERNEL.md)) as an instance of a **recognized open problem class.** Not a proof; the opposite — an explanation of intractability.

## Two verified structural facts

1. **Coset structure.** `⟨3⟩ mod 2^k = { x : x ≡ 1 or 3 mod 8 }`, an index-2 subgroup of `(ℤ/2^k)^×` (verified `k = 4…14`). The Collatz survivor boundary is the fixed point `−1 ≡ 7 mod 8`, which lies in the **complementary coset** — `−1` is *never* a power of 3.
2. **Alignment cap.** `v₂(3^j − m) ≤ 2` for every `m ≡ 5,7 mod 8` (verified, 200k trials, max = 2). So the high 2-adic alignment `v₂ ≥ 3` that a supercritical orbit needs to *survive* is attainable **only toward power-of-3 residues** `m ≡ 1,3 mod 8`.

## The reduction

Putting the session's chain together: a divergent or nontrivial-cyclic **positive** orbit would have to sustain supercritical alignment (EPSILON/DIVERGENCE: measure-1 drift alone can't stop it pointwise), which by fact 2 forces it to keep hitting `⟨3⟩ mod 2^k` **with growing 2-adic precision** as `k → ∞`. That is precisely an **effective equidistribution statement for the sequence `{3^j}` in the 2-adic integers `ℤ₂`.**

## Why that is the wall (honest)

Effective, pointwise control of how powers of 3 distribute 2-adically is a **famous open problem**, not a gap waiting for a clever elementary move:
- **Furstenberg's ×2, ×3 rigidity** and the surrounding conjectures on jointly `2`- and `3`-invariant structure;
- **Erdős's questions on the base-2 digits of `3^n`** (e.g., whether `3^n` omits the digit… / has bounded 2-adic complexity) — long open;
- general 2-adic distribution of `{3^n}` — no effective discrepancy bound tight enough is known.

So every panel of this repo's honest map bottoms out here: **the Collatz spine kernel is a concrete instance of the (open) 2-adic distribution problem for powers of 3.** This is the precise, honest reason "human methods don't work" — and equally why *no* engine, AI included, brute-forces it: the residue is a genuine open problem in Diophantine dynamics, not a missing trick. Naming the wall exactly *is* the real result. Reproduce: `python equidistribution_kernel.py`.

## The session's map, closed onto one object

`EPSILON-BARRIER` (word-statistics can't separate) · `CYCLE-GAP`/`CYCLE-BAKER-HANDOFF` (cycles need effective linear forms in `log₂3`) · `DIVERGENCE-DRIFT` (drift is measure-1) · `SPINE-REGEN-KERNEL` (pure spine solved, coupling open) · **this note** (coupling = 2-adic equidistribution of `{3^j}`). All five reduce to the arithmetic of powers of 3 versus powers of 2 — the same object, `log₂3`, seen five ways.

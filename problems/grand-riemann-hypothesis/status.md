# Status & Frontier — The Grand Riemann Hypothesis

**Status: open.** GRH is unproven for *every* degree-$\ge 1$ $L$-function, and is not known even for a single automorphic $L$-function on $\mathrm{GL}_n$ with $n\ge 2$. It is strictly harder than RH (the degree-one, level-one case) and than the Generalized RH for Dirichlet $L$-functions, both of which it contains. There is no claimed proof accepted by the community; the recurring disputed announcements (de Branges, Atiyah) are addressed in `attempts.md`.

## What is known

**Unconditional.**
- Each $L$-function in the Selberg class with the standard axioms has its non-trivial zeros confined to the critical strip $0\le\mathrm{Re}(s)\le 1$, with a classical zero-free region near $\mathrm{Re}(s)=1$ (the input to prime-number theorems in all these settings).
- For $\zeta$: a positive proportion — roughly $41.7\%$ (Bui–Conrey–Young 2011 and successors) — of non-trivial zeros lie exactly on $\mathrm{Re}(s)=\tfrac12$, and infinitely many are simple. Analogous positive-proportion results hold for Dirichlet and some $\mathrm{GL}_2$ $L$-functions.
- Density theorems bound the number of possible off-line zeros; **Bombieri–Vinogradov** (1965) gives "GRH on average" over moduli, sufficient for many applications.
- The **function-field analogue is a theorem** (Weil 1948; Deligne 1974): over $\mathbb{F}_q$, the corresponding RH holds.
- **Rodgers–Tao (2020)** proved the de Bruijn–Newman constant satisfies $\Lambda\ge 0$; since RH $\iff \Lambda\le 0$, RH is "barely" true if true (arXiv:1801.05914; *Forum of Mathematics, Pi*, doi:10.1017/fmp.2020.6).
- **Structure of $\mathcal{S}$:** Kaczorowski–Perelli proved there are no elements of degree $0<d<1$ and none with $1<d<2$, and classified degrees $0$ and $1$ — confirming the automorphic picture without locating zeros.

**Conditional.** Assuming GRH, one obtains: square-root error in primes in arithmetic progressions; effective Chebotarev with strong bounds; deterministic polynomial-time primality and small least-quadratic-residue/primitive-root results; sharp subconvexity-flavored estimates; and precise low-lying-zero statistics matching Katz–Sarnak symmetry types. Vast tracts of analytic number theory are written "under GRH."

## What a full resolution requires

A proof must exclude *every* off-line zero of *every* element of the class simultaneously — a uniform statement, not a function-by-function argument. The leading diagnosis is that we lack an arithmetic analogue of the geometric tools (an $\ell$-adic cohomology over $\mathrm{Spec}\,\mathbb{Z}$, or a working "field with one element" $\mathbb{F}_1$ geometry) that made Deligne's proof possible. Equivalent positivity reformulations (Weil explicit formula, Li's criterion, Connes' trace formula) convert GRH into a single positivity statement but do not make it tractable.

## Plausible routes

1. **Spectral / Hilbert–Pólya:** construct a self-adjoint operator whose spectrum is the set of zero ordinates; Connes' adèlic trace formula is the most developed version, reducing GRH to a positivity.
2. **Arithmetic geometry over $\mathbb{F}_1$:** import Deligne's cohomological mechanism to the number-field setting — currently the most-hoped-for but least-developed path.
3. **Moments and RMT:** continued growth of critical-line proportions and full moment conjectures; unlikely to reach $100\%$ but disciplines expectations.
4. **Selberg-class structure:** prove the degree conjecture and Selberg's orthonormality conjectures, narrowing the class enough that automorphic input applies uniformly.

## Related problems

- [Riemann Hypothesis](../riemann-hypothesis/README.md) — the degree-one seed case GRH contains.
- [Montgomery's Pair Correlation Conjecture](../montgomery-pair-correlation/README.md) — the statistical face of the zeros.
- [Birch and Swinnerton-Dyer Conjecture](../birch-swinnerton-dyer/README.md) — concerns the same automorphic $L$-functions at the central point.
- [Chowla Conjecture](../chowla-conjecture/README.md) — multiplicative-function statistics deeply tied to $L$-function zeros.
- [Artin's Primitive Root Conjecture](../artin-primitive-root-conjecture/README.md) — a classic consequence of GRH for Dirichlet $L$-functions.

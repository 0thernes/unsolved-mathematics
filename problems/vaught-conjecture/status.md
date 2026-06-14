# Status & Frontier — Vaught's Conjecture

_Where the problem stands and what a resolution would require._

## Current status: OPEN

Vaught's Conjecture is **open**. For a countable complete first-order theory $T$, it asserts that the number of countable models up to isomorphism, $I(T,\aleph_0)$, is either $\le\aleph_0$ or exactly $2^{\aleph_0}$ — never strictly between. The statement has content only when CH fails (under CH it is vacuous, since $\aleph_1 = 2^{\aleph_0}$), so the live problem is to rule out **exactly $\aleph_1$ countable models** when $\aleph_1 < 2^{\aleph_0}$.

## What is known (unconditional)

- **Morley (1970):** $I(T,\aleph_0)\in\{0,1,2,\dots,\aleph_0\}\cup\{\aleph_1,2^{\aleph_0}\}$. The conjecture reduces to excluding the single value $\aleph_1$.
- **No theory has exactly 2 countable models** (Vaught, 1961); more generally several small finite/infinite counts are constrained.
- **VC holds for $\omega$-stable theories** (Harrington–Makkai–Shelah, 1981) and for **superstable theories of finite rank** (Buechler and successors).
- **VC holds for theories of trees** (Steel, 1978), for **o-minimal theories** (Mayer, 1988), for **linear orders**, and for **modules** over various rings.
- **VC holds for $\aleph_0$-categorical theories** (trivially, one countable model) and for many **tame** (NIP/dp-minimal) fragments.

## What is known (negative / barrier)

- **Hjorth (2002):** the **Topological Vaught Conjecture fails for general Polish groups** — there is, consistently, a Borel Polish-group action with exactly $\aleph_1$ orbits. Hence VC is **not** a corollary of any purely topological dichotomy holding for all Polish groups; a proof must use specific features of $S_\infty$ / first-order definability. This is the central obstruction shaping the frontier.

## What is known (conditional / structural)

- VC is equivalent to the **Topological Vaught Conjecture for $S_\infty$** (via Becker–Kechris), and to a statement about the orbit-counting of the logic action.
- Links to **Martin's Conjecture** and the **Borel-reducibility hierarchy** give conditional constraints on the complexity of isomorphism relations, contingent on those open problems.

## What a full resolution requires

A **proof** must show that no countable complete $T$ produces exactly $\aleph_1$ non-isomorphic countable models — equivalently, that a thin (perfect-free) yet uncountable tree of Scott sentences cannot be realized by a single first-order theory. This means extracting, uniformly across *all* theories (including strictly stable, NIP, and unstable ones), the perfect-set dichotomy currently available only for tame/stable classes — and doing so without relying on the general-Polish-group route that Hjorth closed.

A **disproof** must exhibit an explicit theory with exactly $\aleph_1$ countable models in a model of $\neg$CH, with a fully checkable Scott analysis — the goal of Knight's disputed, unverified manuscript.

## Plausible routes

1. **Push stability methods outward** from $\omega$-stable to broader stable/NIP classes, seeking a uniform coordinatization.
2. **Exploit $S_\infty$-specific combinatorics** (Vaught transforms, definability over admissible fragments) to recover a dichotomy where the general Polish-group version fails.
3. **Counting Scott sentences** in $L_{\omega_1\omega}$ with sharper infinitary-combinatorial bounds.
4. **Settle relevant cases of Martin's Conjecture** to constrain orbit-equivalence complexity.
5. **Verified counterexample** — construct and certify a thin-tree theory with $\aleph_1$ models.

## Related problems

- [Continuum Hypothesis](../continuum-hypothesis/README.md) — VC is non-trivial precisely when CH fails; the $\aleph_1$-vs-$2^{\aleph_0}$ gap is its arena.
- [Invariant Subspace Problem](../invariant-subspace-problem/README.md) — another long-open structural problem at the analysis/logic boundary with descriptive-set-theoretic flavor.
- [Novikov Conjecture](../novikov-conjecture/README.md) — uses Borel/topological group-action machinery cognate to the Topological Vaught Conjecture.
- [Baum–Connes Conjecture](../baum-connes-conjecture/README.md) — group actions and assembly maps, sharing tools with the Polish-group-action program.

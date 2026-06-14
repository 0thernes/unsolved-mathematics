# Status & Frontier — Köthe's Conjecture

**Status: open** (posed 1930, unresolved as of the present). No accepted proof or counterexample exists in general; the problem is alive and actively worked, chiefly through its matrix and polynomial reformulations.

## What is known (unconditional)

- **PI-rings.** True. Nil one-sided ideals in rings satisfying a polynomial identity are locally nilpotent (Levitzki, Amitsur–Levitzki, Kaplansky), hence absorbed by a nil two-sided ideal.
- **Chain conditions.** True for right/left Noetherian, Goldie, and Krull-dimension rings: Levitzki's theorem makes nil one-sided ideals nilpotent.
- **Algebras over uncountable fields.** True, via an Amitsur-style counting argument.
- **Amitsur's polynomial theorem.** $J(R[x]) = N[x]$ for some nil ideal $N \trianglelefteq R$ holds unconditionally and links the reformulations.
- **Equivalences (Krempa, 1972).** The conjecture holds in general $\iff$ $M_2(R)$ is nil for every nil ring $R$ $\iff$ $R[x]$ is Jacobson radical for every nil ring $R$. Settling any one settles all.

## What is known (conditional / delimiting)

- The strengthening "$R$ nil $\Rightarrow R[x]$ nil" is **false** (Smoktunowicz, 2000): there is a nil ring whose polynomial ring is not nil. This does **not** refute Köthe's conjecture, which only needs $R[x]$ to be Jacobson radical, but it rules out the most natural proof strategy and shows how narrow the truth's margin is.
- Simple nil rings **exist** (Smoktunowicz, 2002), so "nil $\Rightarrow$ structurally small" intuitions are invalid; yet the known simple nil ring is consistent with the conjecture.

## What a full resolution requires

A proof must establish, for an arbitrary nil ring $R$ with no chain conditions and unbounded nil index, that $M_2(R)$ is again nil — i.e. that products of $2\times2$ matrices over $R$ are nilpotent despite the entries' nil exponents being uncontrolled. Equivalently, it must show $R[x]$ is Jacobson radical for every nil $R$. A *disproof* must engineer a nil ring violating the $M_2$-nilness criterion, presumably from Golod–Shafarevich-type or Smoktunowicz-type raw material. The central obstruction in both directions is the absence of any technique that bounds or organizes nil index in the wild (non-Noetherian, non-PI) setting.

## Plausible routes

1. **Push the polynomial reformulation** — exploit Amitsur's $J(R[x])=N[x]$ to force $N=R$ for nil $R$, possibly via new growth/Hilbert-series constraints on nil algebras.
2. **Refine counterexample machinery** — adapt Smoktunowicz's nil-but-$R[x]$-not-nil constructions or Golod–Shafarevich algebras to attack the $M_2$ criterion directly; success would *disprove* the conjecture.
3. **Quantitative nil-index control** — develop combinatorial or growth-theoretic bounds (à la Shirshov/Gröbner-Shirshov methods) that constrain index in matrix products.

The honest assessment is that no current program is close: the field expects that resolution awaits a fundamentally new idea for handling unbounded nil index.

## Related problems

- [Jacobian Conjecture](../jacobian-conjecture/README.md) — another long-open conjecture in (commutative/affine) algebra resistant to structural attack.
- [Zariski Cancellation Problem](../zariski-cancellation-problem/README.md) — sibling open problem in ring/algebra theory with recent activity in positive characteristic.
- [Invariant Subspace Problem](../invariant-subspace-problem/README.md) — analogous "one-sided structure forces a global object?" flavor in operator algebra.
- [Connes Embedding Aftermath](../connes-embedding-aftermath/README.md) — frontier question in operator algebra where a long-standing conjecture's status was dramatically revised, a cautionary parallel for radical theory.

# Approaches — The Cherlin–Zilber Algebraicity Conjecture

_Major strategies, partial results, and barriers._

## The Borovik program (CFSG-by-analogy)

The dominant strategy, due to Alexandre Borovik, is to transport the architecture of the Classification of the Finite Simple Groups (CFSG) into the category of groups of finite Morley rank. One studies the connected component $S^\circ$ of a Sylow $2$-subgroup and partitions putative simple groups into four **types**: *even* ($S^\circ$ is a nontrivial $2$-unipotent, i.e. definable elementary-abelian $2$-group), *odd* ($S^\circ$ is a nontrivial $2$-torus, a divisible abelian $2$-group), *mixed* (both pieces nontrivial), and *degenerate* ($S^\circ$ trivial). One then seeks "identification theorems" matching each configuration to a Chevalley group.

**Best result.** The even-type case is *completely solved*: Altınel, Borovik, and Cherlin (2008) prove that an infinite simple group of finite Morley rank and even type is a Chevalley group over an algebraically closed field of characteristic $2$. Mixed type was eliminated (no such simple groups exist). This is the strongest unconditional evidence for the conjecture.

**Barrier.** The analogy with CFSG breaks down in two places: there is no analogue of the "$N$-group" / signalizer-functor finiteness available for free, and — most seriously — **degenerate type** has no finite-group counterpart, since every nonabelian finite simple group has even order (Feit–Thompson). The methods that drive the finite classification have no traction where there are no involutions at all.

## Sylow and torus theory; unipotence

A foundational layer establishes that fMr groups behave like algebraic groups at the level of subgroup structure: conjugacy of Sylow $2$-subgroups (Borovik–Poizat), good torus theory, and Burdges's notion of **unipotence parameters** that substitutes for characteristic-$p$ unipotence when no field is yet visible.

**Best result.** A robust theory of decent tori, Carter subgroups (shown to exist and be conjugate by Frécon–Jaligot), and genericity arguments now exist, enabling "generic identification" theorems in odd type.

**Barrier.** Without an ambient field one cannot speak of unipotent elements directly; the surrogate unipotence theory is technical and does not yet cover all configurations uniformly, particularly in small rank.

## Field-recovery (Zilber) theorems

The engine that turns group data into algebraic geometry is **Zilber's field theorem**: if $A$ is an infinite definable abelian group acted on definably and (sufficiently) irreducibly by an infinite abelian group $T$, then an infinite field $K$ is interpretable, with $A$ a $K$-vector space and $T \hookrightarrow K^\times$. Coupled with **Zilber's indecomposability theorem** (the fMr analogue of the fact that a family of irreducible subvarieties generates a connected subgroup), this lets one reconstruct the algebraic-group structure once enough internal action is located.

**Best result.** These theorems reduce algebraicity, in many configurations, to *finding* a definable field and a faithful enough representation.

**Barrier.** The hypotheses fail precisely in the most dangerous case — a **bad group** or **bad field** — where the expected field simply does not appear.

## Odd type and degenerate type — the live front

For **odd type**, work by Burdges, Cherlin, Deloro, and others combines unipotence parameters with genericity to identify groups of bounded Prüfer $2$-rank. **Best result:** simple odd-type groups of small Prüfer rank, and "minimal connected simple" groups under tameness or genericity hypotheses, are identified as $\mathrm{PSL}_2$ or related Chevalley groups.

For **degenerate type**, Borovik–Burdges–Cherlin proved a key negative-leaning fact: a connected degenerate-type group has **no involutions** (its Sylow $2$-subgroup is trivial, not merely torsion-free in its connected part). This rules out one pathology but leaves the existence question wide open.

## Bad groups and bad fields (the central obstruction)

A **bad group** is a (hypothetical) nonsolvable connected fMr group all of whose proper definable connected subgroups are nilpotent; a **bad field** is a field of finite Morley rank with a proper infinite definable multiplicative subgroup. Their conjectural nonexistence is the crux.

**Negative/barrier results.** Bad fields of characteristic $0$ were **constructed** by Baudisch, Hils, Martin-Pizarro, and Wagner (2009) under a number-theoretic hypothesis (a consequence of Schanuel-type conjectures), using Hrushovski amalgamation — showing the fMr universe is genuinely richer than the algebraic one and that the conjecture cannot be proved by "soft" means alone. On the positive side, **Frécon (2018)** proved there is **no bad group of Morley rank $3$**, closing the smallest open test case and removing the simplest potential counterexample to the rank-$3$ instance of the conjecture. No bad *simple* group is known to exist, but none is known to be impossible in general.

## Tameness and analytic hypotheses

A recurrent device is to add a hypothesis ruling out bad configurations — e.g. *tameness* (no bad fields interpretable) or *no infinite definable simple bad-field-free* assumptions. Under such hypotheses several classification statements become theorems. The barrier is that the bad-field constructions show these hypotheses are not free: the unconditional conjecture must confront the pathologies head-on.

# Status & Frontier — The Invariant Subspace Problem

_Where the problem stands and what a resolution would require._

**Status: open (active progress).** The Hilbert-space invariant subspace problem — does every bounded operator on a separable, infinite-dimensional, complex Hilbert space have a non-trivial closed invariant subspace? — has **not** been resolved to the satisfaction of the operator-theory community.

### What is known (unconditional)

- **Compact and Lomonosov class.** Every compact operator has a non-trivial invariant subspace (von Neumann; Aronszajn–Smith 1954). More generally, any operator commuting with a non-zero compact operator has a non-trivial *hyperinvariant* subspace (Lomonosov 1973). This is the broadest general positive theorem.
- **Normal and subnormal operators.** Normal operators have invariant subspaces via the spectral theorem; subnormal operators do too (Scott Brown 1978).
- **Contractions with thick spectrum.** Contractions whose spectrum contains the unit circle have invariant subspaces (Brown–Chevreau–Pearcy 1988); various hyponormal and dual-algebra classes are covered by the property-$(\mathbb{A})$ machinery.
- **Spectral handles.** Any operator with a non-trivial point spectrum, residual spectrum, or a disconnected spectrum yields invariant subspaces via the Riesz functional calculus.
- **Almost-invariant subspaces.** Every operator on an infinite-dimensional Banach space has almost-invariant half-spaces (Androulakis–Popov–Tcaciuc–Troitsky and collaborators) — a genuine but strictly weaker result.

### What is known (the negative side, other categories)

- **Banach spaces: false.** Enflo (1976/1987) and Read (1984–1986, including an operator on $\ell^1$) constructed bounded operators with *no* non-trivial invariant subspace. Read (1997) gave quasinilpotent counterexamples. These use Banach-space geometric freedom unavailable in Hilbert space.

### The disputed 2023 claim

In 2023, **Per Enflo** posted a preprint, *On the invariant subspace problem in Hilbert spaces* (arXiv:2305.15442), claiming that every bounded operator on a separable Hilbert space has a non-trivial invariant subspace. The claim attracted significant attention but, as of this writing, has **not** been peer-reviewed, published, or accepted; independent verification of the central construction is incomplete, and no agreed-upon error has been published either. The community's working position remains that the problem is open. This dossier records the claim as a notable development, not a resolution. (A separate, unrelated 2023 preprint by another author also circulated without accepted verification.)

### What a full resolution would require

An **affirmative** proof must produce a non-trivial invariant subspace for *arbitrary* bounded $T$, including the hardest case: operators with trivial commutant, no compact operators nearby, quasinilpotent spectrum (so no spectral handle), and no usable functional model. Because the Banach-space counterexamples show a structure-free construction can defeat the affirmative, any successful Hilbert-space proof must exploit **Hilbert-space-specific rigidity** — orthogonality, the parallelogram law, polar decomposition, or $C^*$-algebraic structure — in an essential way. A **negative** resolution would require a Hilbert-space operator provably lacking invariant subspaces, which decades of effort and the rigidity of the inner-product geometry have so far prevented.

### Plausible routes

1. Upgrading **almost-invariant** to invariant via a quantitative or fixed-point argument tailored to Hilbert space.
2. Extending **dual-algebra / Scott Brown** methods past the unit-circle-spectrum barrier to general contractions.
3. New **functional models** for quasinilpotent or trivial-commutant operators.
4. A genuinely new structural invariant detecting hidden invariant subspaces — or, conversely, a Read-style construction adapted to the Hilbert norm.

## Related problems

- [Connes Embedding Aftermath](../connes-embedding-aftermath/README.md)
- [Yang–Mills Mass Gap](../yang-mills-mass-gap/README.md)
- [Crouzeix's Conjecture](../crouzeix-conjecture/README.md)
- [Sendov's Conjecture](../sendov-conjecture/README.md)
- [Riemann Hypothesis](../riemann-hypothesis/README.md)

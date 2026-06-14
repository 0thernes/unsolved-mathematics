# Status & Frontier — P versus NP

_Where the problem stands and what a resolution would require._

**Status: open.** $\mathrm{P}$ versus $\mathrm{NP}$ is unresolved and remains a Clay Millennium Prize Problem. No proof exists in either direction, and no claimed proof has survived peer scrutiny. The strong working conjecture, shared by the overwhelming majority of complexity theorists, is $\mathrm{P} \neq \mathrm{NP}$.

## What is known (unconditional)

- **Structure if $\mathrm{P} \neq \mathrm{NP}$.** Ladner's theorem guarantees an infinite hierarchy of $\mathrm{NP}$-intermediate problems—neither in $\mathrm{P}$ nor $\mathrm{NP}$-complete—should the classes differ. Candidate natural examples (factoring, graph isomorphism) are studied in this light; graph isomorphism was shown by Babai (2016) to be solvable in quasipolynomial time $2^{(\log n)^{O(1)}}$, removing it as a likely $\mathrm{NP}$-complete candidate.
- **Restricted lower bounds.** Unconditional superpolynomial/exponential lower bounds hold for monotone circuits (Razborov), constant-depth $\mathrm{AC}^0$ and $\mathrm{AC}^0[p]$ circuits (Furst–Saxe–Sipser, Håstad, Razborov, Smolensky), and resolution proof systems (Haken). Williams's $\mathrm{NEXP} \not\subseteq \mathrm{ACC}^0$ (2011) is the strongest non-natural circuit separation against a low class.
- **Time hierarchy.** Deterministic and nondeterministic time-hierarchy theorems prove that more time strictly buys more computational power—but they relativize and so cannot separate $\mathrm{P}$ from $\mathrm{NP}$.

## The barriers — what a resolution must overcome

Any proof must simultaneously be **non-relativizing** (Baker–Gill–Solovay 1975), **non-naturalizing** (Razborov–Rudich 1994, assuming strong one-way functions exist), and **non-algebrizing** (Aaronson–Wigderson 2008). Essentially every technique in the standard toolkit is excluded by at least one barrier. This is the central reason the problem is considered so hard: it is not merely unsolved but provably resistant to all currently known general methods.

## Conditional landscape

A great deal of complexity theory is organized around assuming $\mathrm{P} \neq \mathrm{NP}$ (or its strengthenings). The **Exponential Time Hypothesis** and **Strong ETH** (Impagliazzo–Paturi) underpin fine-grained complexity, yielding tight conditional lower bounds for problems in $\mathrm{P}$ (edit distance, orthogonal vectors). Cryptography presumes the existence of one-way functions, which implies $\mathrm{P} \neq \mathrm{NP}$ but is strictly stronger and itself unproven. Recent **meta-complexity** work (on $\mathrm{MCSP}$ and time-bounded Kolmogorov complexity) and **hardness magnification** results show that seemingly modest lower bounds, if proved, would magnify into major separations—an avenue some hope might thread the barriers.

## Plausible routes

The most actively pursued long-range programs are **Geometric Complexity Theory** (Mulmuley–Sohoni), targeting the algebraic analogue $\mathrm{VP} \neq \mathrm{VNP}$ through representation-theoretic obstructions, and **proof complexity**, targeting $\mathrm{NP} \neq \mathrm{coNP}$ via lower bounds for strong propositional systems (Frege, Extended Frege). Both are deep but currently far from the goal; a 2016 result of Bürgisser–Ikenmeyer–Panova showed the simplest GCT obstructions are insufficient, redirecting that program. A full resolution would require either an explicit polynomial-time algorithm for an $\mathrm{NP}$-complete problem ($\mathrm{P} = \mathrm{NP}$) or a superpolynomial lower bound for one—achieved by mathematics that does not yet exist.

## Related problems

- [Riemann Hypothesis](../riemann-hypothesis/README.md)
- [Yang–Mills Mass Gap](../yang-mills-mass-gap/README.md)
- [Navier–Stokes Smoothness](../navier-stokes-smoothness/README.md)
- [Hodge Conjecture](../hodge-conjecture/README.md)
- [Birch–Swinnerton-Dyer Conjecture](../birch-swinnerton-dyer/README.md)

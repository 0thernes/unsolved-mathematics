# Approaches — The Černý Conjecture

_Major strategies, partial results, and barriers._

1. **Extension Method & Linear-Algebraic Rank Arguments (Pin 1983; Kari 1998; Steinberg 2011).** Working backward from a singleton set $\{q\}$, let $S_k$ be a subset of size $k$ reachable as preimages $\delta^{-1}(q, w)$. Extending $S_k$ to a strictly larger preimage set $S_{k+1}$ using a word of length $\le n$ at every step immediately yields $O(n^2)$ *whenever* short extending words exist. Kari and Steinberg proved this via linear algebra over $\mathbb{Q}^Q$ (showing the characteristic vectors of preimage sets span an increasing subspace) for Eulerian and one-cluster automata.
2. **Pin–Frankl Extremal Set Bounds & Avoiding Words (Szykuła 2018; Shitov 2019).** Without algebraic structure, the best guaranteed length of an extending word from a $k$-element subset is bounded by Frankl's theorem on two set families, giving $\binom{k+1}{2}$ per step and summing to $(n^3-n)/6$. Szykuła and Shitov beat $1/6$ by exploiting conflicts between successive worst-case avoiding sets.
3. **Road Coloring Theorem (Trahtman 2009) & Primitive Matrix / Representation Theory.** Trahtman proved Adler–Goodwyn–Weiss's Road Coloring Conjecture (every aperiodic strongly connected directed graph of constant out-degree admits a synchronizing coloring), and representation theory of transformation monoids (Arnold–Steinberg) gives quadratic bounds for automata with specific group actions.

## Core Barrier
The central mystery is **why even $O(n^{2.99})$ — let alone $O(n^2)$ — remains unproved**! For general DFAs, the backward preimage extension can require length $\Omega(k^2)$ at an *individual* step (so naive step-by-step Pin–Frankl summation inevitably gives $\Theta(n^3)$). Proving a quadratic bound requires an **amortized** global invariant showing that worst-case $\Omega(n^2)$ extension steps cannot happen $\Omega(n)$ times in a row.

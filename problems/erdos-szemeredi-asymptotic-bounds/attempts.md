# Attempts — Erdős Problem 142 (Asymptotic Density of $k$-AP-Free Sets)

_Notable attempts, near-misses, retracted proofs._

- **Ergodic-Theory Proofs (Furstenberg 1977; Katznelson–Ornstein).** Furstenberg's correspondence principle gave a conceptual proof of Szemerédi's theorem via multiple recurrence, but because it relies on infinitary compactness / Zorn's lemma, it yields **no quantitative bound** on $r_k(N)$ (subsequent finitary translations by Tao 2006 give Ackermann-type bounds).
- **Hypergraph Regularity (Gowers 2007; Rödl–Skokan 2004).** Extends Szemerédi's graph regularity to $k$-uniform hypergraphs, yielding a purely combinatorial proof of Szemerédi's theorem, but with wowzer/tower-type bounds far weaker than Fourier/nilsequence methods.
- **Polynomial-Method Hope after Cap Sets (Croot–Lev–Pach 2016; Ellenberg–Gijswijt 2017).** The slice-rank polynomial method solved the finite-field cap set problem ($r_3(\mathbb{F}_3^n) \le 2.756^n$), sparking hopes for a power saving $r_3(N) \ll N^{1-c}$ over the integers. Behrend's 1946 lower bound immediately forbids any power saving over $\{1,\dots,N\}$, and the slice-rank barrier fails to lift from $\mathbb{F}_3^n$ to $\mathbb{Z}$ because integer wrap-around breaks low-degree polynomial structure.

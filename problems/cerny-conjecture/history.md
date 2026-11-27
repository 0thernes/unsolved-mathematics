# History — The Černý Conjecture

_Origin, formulation, and timeline._

A deterministic finite automaton (DFA) $\mathcal{A} = (Q, \Sigma, \delta)$ with $|Q| = n$ states is called **synchronizing** if there exists a finite word $w \in \Sigma^*$ such that $\delta(q, w)$ is the same state for every $q \in Q$ (resetting the machine regardless of its unknown initial state). In 1964, Slovak computer scientist Ján Černý constructed for every $n \ge 2$ a two-letter synchronizing $n$-state automaton whose shortest synchronizing word has exact length $(n-1)^2$, and conjectured that $(n-1)^2$ is the universal maximum over *all* $n$-state synchronizing automata.

Despite its elementary combinatorial statement and huge practical importance in robotics (part orienters), formal verification, and symbolic dynamics, the **Černý conjecture** has resisted proof for over 60 years. Strikingly, every general upper bound proved to date is still **cubic** ($O(n^3)$) — not even a sub-cubic $o(n^3)$ bound (let alone $O(n^2)$!) is known!

## Timeline

- **1964** — Ján Černý constructs the extremal $n$-state family requiring $(n-1)^2$ steps and poses the conjecture.
- **1966** — Starke proves the first polynomial upper bound $O(n^3)$ (specifically $\approx \frac{1}{2} n^3$).
- **1982–1983** — Peter Frankl (`10.1016/s0195-6698(82)80025-5`) and Jean-Éric Pin (`10.1016/s0304-0208(08)73432-7`) combine Pin's reduction with Frankl's extremal set theorem to prove the landmark **Pin–Frankl bound** $(n^3 - n)/6 \approx 0.16667\,n^3$, which stood unbroken for **35 years**!
- **1987** — Klyachko, Rystsov, and Spivak refine combinatorial extensions and verify structural classes (`10.1007/bf01071771`).
- **1998** — Kari proves the Černý conjecture for **Eulerian automata** (bound $(n-2)(n-1) + 1$), later followed by proofs for circular (Dubuc 1998), monotonic, aperiodic (Trahtman 2007), and one-cluster automata (Steinberg 2011).
- **2008** — Mikhail Volkov publishes the landmark survey *Synchronizing Automata and the Černý Conjecture* (`10.1007/978-3-540-88282-4_4`).
- **2017–2018** — Marek Szykuła breaks the 35-year-old Pin–Frankl $n^3/6$ barrier (`arXiv:1702.05455`), proving $\le \frac{114}{685} n^3 + O(n^2) \approx 0.16642\,n^3$.
- **2019** — Yaroslav Shitov improves the cubic constant slightly further to $\le 0.1654\,n^3 + o(n^3)$ (`arXiv:1901.06542`), still cubic!

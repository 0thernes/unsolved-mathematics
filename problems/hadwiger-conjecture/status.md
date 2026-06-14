# Status & Frontier — Hadwiger's Conjecture (Graph Coloring)

_Where the problem stands and what a resolution would require._

## Current status: open, active progress

Hadwiger's Conjecture — every graph $G$ with no $K_t$ minor is $(t-1)$-colorable, equivalently $h(G) \ge \chi(G)$ — is **open in general**. It is proved for $t \le 6$, with the cases $t=5$ and $t=6$ resting on the Four Color Theorem; the first open exact case is $t=7$. The conjecture is universally believed true and is widely regarded as one of the deepest open problems in graph theory.

## What is known (unconditional)

- **Exact cases.** $t \le 4$ (Hadwiger 1943, Dirac 1952) elementary; $t=5$ equivalent to the Four Color Theorem (Wagner 1937 + Appel–Haken 1976); $t=6$ proved by Robertson–Seymour–Thomas (1993) via the apex reduction.
- **Quantitative bounds.** Every graph satisfies $\chi(G) = O(h(G)\sqrt{\log h(G)})$ (Kostochka 1980; Thomason 1984), improved by Norin–Postle–Song (2019) past the square-root barrier, and currently to $\chi(G) = O(h(G)\log\log h(G))$ (Delcourt–Postle 2021). This is within a $\log\log$ factor of the *linear* target.
- **Restricted classes.** $K_7$-minor-free graphs avoiding $K_{4,4}$ are 6-colorable (Kawarabayashi–Toft 2005); linear bounds hold for various excluded-substructure regimes.

## What is known (conditional / relaxed)

- **Fractional Hadwiger** holds: $\chi_f(G) = O(h(G))$ (Reed–Seymour 2005).
- **Almost all graphs** satisfy the conjecture (Bollobás–Catlin–Erdős).
- Variants — **list coloring**, **odd minors**, **subdivisions** — have partial results; note the *subdivision* analogue (Hajós' Conjecture) is **false** for $t \ge 7$ (Catlin 1979; Erdős–Fajtlowicz 1981), a cautionary contrast.

## What a full resolution would require

A complete proof faces two distinct walls. First, the **$\sqrt{\log t}$ density barrier**: routing chromatic number through average degree is provably lossy because random graphs decouple density from Hadwiger number, so any proof of even the *Linear* Hadwiger Conjecture must reason about coloring more cleverly than counting edges. Second, the **structural wall at $t=7$**: there is no known finite reduction of any case $t \ge 7$ to the Four Color Theorem or to a computer check, because no tractable decomposition theorem for $K_t$-minor-free graphs is available for large $t$. A resolution would plausibly require either a new global coloring technique that removes the residual $\log\log$ factor and reaches the exact constant $1$, or a structural breakthrough yielding a Robertson–Seymour-style classification fine enough to control $\chi$ exactly.

## Plausible routes

1. **Close the $\log\log$ gap** — extend the Norin–Postle–Song / Delcourt–Postle machinery to prove $\chi(G) = O(h(G))$ (Linear Hadwiger), then attack the constant.
2. **Settle $t=7$ structurally** — find a decomposition theorem for $K_7$-minor-free graphs analogous to the apex characterization, reducing to colorability of a controlled base class.
3. **Probabilistic / entropy methods** — local sparsification and nibble-type arguments tailored to minor-free graphs.
4. **Odd-Hadwiger or list-coloring intermediaries** — prove strengthenings that imply linear bounds.

The status field is **active-progress**: no claimed full proof is accepted, the small cases are secure, and the quantitative frontier has moved decisively since 2019 without yet reaching linearity.

## Related problems

- [Hadwiger–Nelson Problem](../hadwiger-nelson-problem/README.md) — chromatic number of the plane, another Hadwiger-named coloring problem.
- [Kakeya Conjecture](../kakeya-conjecture/README.md) — a sibling combinatorial/geometric problem with deep structural barriers.
- [Union-Closed Sets Conjecture](../union-closed-sets-conjecture/README.md) — a sibling open problem in extremal combinatorics.
- [Lonely Runner Conjecture](../lonely-runner-conjecture/README.md) — combinatorial conjecture with a comparable "easy to state, hard to prove" character.

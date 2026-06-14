# Approaches — Hadwiger's Conjecture (Graph Coloring)

_Major strategies, partial results, and barriers._

## Reduction to the Four Color Theorem (small cases)

The earliest and most decisive line of attack exploits structural decompositions to reduce a Hadwiger case to a known result. **Wagner (1937)** showed that $K_5$-minor-free graphs decompose by clique-sums over planar graphs and the Wagner graph $V_8$; since planar graphs are 4-colorable (Appel–Haken, 1976) and clique-sums preserve colorability, the case $t=5$ is *equivalent* to the Four Color Theorem. **Robertson, Seymour, and Thomas (1993)** extended this for $t=6$: they proved that any minimal counterexample to the $K_6$ case is **apex** (planar plus one vertex), which is 5-colorable, again invoking the Four Color Theorem. *Best result:* unconditional truth for $t \le 6$. *Barrier:* the structural classification of $K_t$-minor-free graphs becomes wildly more complex for $t \ge 7$. There is no known clean decomposition theorem for $K_7$-minor-free graphs (Kawarabayashi–Toft and others verified special configurations, e.g. graphs with no $K_7$ or $K_{4,4}$ minor), and no reduction of $t=7$ to a finite check is in sight.

## Extremal / density (Mader–Kostochka–Thomason) bounds

If high chromatic number forces high *density*, and density forces a large clique minor, one obtains $\chi(G) = O(h(G) \cdot f(h(G)))$. **Mader (1968)** proved linear edge-density bounds forcing $K_t$ minors for small $t$. **Kostochka (1980)** and independently **Thomason (1984)** proved that average degree $\Omega(t\sqrt{\log t})$ forces a $K_t$ minor, and that this is tight; **Thomason (2001)** pinned the constant at $c = 0.6382\ldots$ Combined with the greedy/degeneracy bound $\chi(G) \le d(G)+1$, this yields the long-standing *general* bound $\chi(G) = O(h(G)\sqrt{\log h(G)})$. *Barrier:* the $\sqrt{\log t}$ factor is **provably tight for the density-forcing problem** — random graphs $G(n,p)$ have Hadwiger number $\Theta(n/\sqrt{\log n})$ while density forces no more. So one cannot close the gap to Hadwiger's linear target by density alone; a counting argument loses a $\sqrt{\log t}$ factor that is real for the *minor* problem even though Hadwiger's *coloring* statement does not see it.

## Beyond the square-root barrier (Norin–Postle–Song and successors)

The 2019 breakthrough of **Norin, Postle, and Song** circumvented the density barrier by arguing about coloring directly rather than routing through worst-case density. Using a delicate analysis of how a hypothetical minimal counterexample distributes its dense parts — building on Kostochka's framework and on "fractional" and local sparsity arguments — they proved $\chi(G) = O(h(G)(\log h(G))^{\beta})$ with $\beta = 1/4 + o(1)$, the first asymptotic improvement on the exponent in nearly four decades. **Postle** and **Norin–Postle** subsequently lowered $\beta$ toward $0$, and **Delcourt–Postle (2021)** reached $\chi(G) = O(h(G)\log\log h(G))$, the current record. *Best result:* $\chi(G) = O(h(G)\log\log h(G))$ unconditionally. *Barrier:* the remaining $\log\log h(G)$ factor resists removal; pushing to $O(h(G))$ (let alone the exact constant $1$) appears to need genuinely new ideas about the interaction of coloring and connectivity, not just sharper density accounting.

## Linear bounds and the Linear Hadwiger Conjecture

A natural intermediate target — the **Linear Hadwiger Conjecture** — asks only for $\chi(G) = O(h(G))$, dropping the exact constant. This is open in general but established in important restricted classes: for graphs of bounded "local structure," for $K_{s,t}$-minor-free and excluded-topological-minor settings, and for graphs with no $K_t$ *subdivision* in some regimes. **Reed and Seymour (1998/2005)** proved the **fractional** Hadwiger Conjecture, $\chi_f(G) \le 2h(G)$, and the **list-coloring** and **odd-Hadwiger** variants have spawned parallel literatures. *Barrier:* even the linear version is open; the constant-factor versions known are confined to sparse or excluded-substructure regimes.

## Structural and minor-theory approaches

The Robertson–Seymour Graph Minors project supplies a structure theorem for $K_t$-minor-free graphs (clique-sums of pieces almost-embeddable on surfaces of bounded genus). In principle this could feed an inductive coloring argument; in practice the "apex" and "vortex" parts of the decomposition obstruct controlling $\chi$ tightly, and the bounds the structure theorem yields are far from linear. **Odd-minor** variants (Geelen–Gerards–Reed–Seymour–Vetta) and the **Hadwiger number versus treewidth** angle are active. *Barrier:* the structure theorem's parameters grow too fast in $t$ to recover $\chi \le t-1$.

## Computer-assisted verification of small cases

Since the foundational small cases bottom out at the Four Color Theorem, *any* unconditional proof of $t \le 6$ inherits the computer-assisted status of Appel–Haken (1976) and its later formal verification by Gonthier (2005, in Coq). Configuration-checking and discharging methods have been used to verify Hadwiger-type statements for restricted minor-closed classes. *Barrier:* the case $t=7$ has no known finite reduction, so brute force does not apply; computation can confirm sub-cases but cannot, with current reductions, settle a full new value of $t$.

## Summary of the barrier landscape

The defining obstruction is the **$\sqrt{\log t}$ density barrier**: the most natural quantitative route (chromatic $\to$ density $\to$ minor) is provably lossy because random graphs separate density from Hadwiger number. Post-2019 methods evade but do not eliminate it, halting at a $\log\log$ factor. On the structural side, no decomposition theorem controls $\chi(G)$ tightly for $t \ge 7$. There is no known *negative* barrier (à la relativization or natural proofs) that would forbid a proof — the consensus is that Hadwiger's Conjecture is true and hard, not unprovable.

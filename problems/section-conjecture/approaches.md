# Approaches — Grothendieck's Section Conjecture

_Major strategies, partial results, and barriers._

## Injectivity via anabelian rigidity

The "easy half" — that distinct rational points give non-conjugate sections — is known. **Core idea:** Mochizuki's $p$-adic Hodge-theoretic and anabelian rigidity results, building on Nakamura and Tamagawa, show that the section attached to a point determines the point. **Best result:** injectivity of $X(k) \to \{\text{sections}\}$ holds unconditionally for hyperbolic curves over number fields and over sub-$p$-adic fields. **Barrier:** injectivity says nothing about surjectivity; the genuine difficulty is producing a point from an abstract section, i.e. showing *every* section is geometric.

## Local-to-global and the $p$-adic local conjecture

**Core idea:** study the analogue over local fields $k_v$ and try to glue. A section over $k$ restricts to sections over every completion; one hopes geometric local sections plus a Hasse-type principle yield a global point. **Best result:** the local section conjecture is itself open in general, but Koenigsmann (2005) proved the **birational** $p$-adic local section conjecture, and there are strong partial results (Pop, Saïdi, Wickelgren) for cuspidal/birational variants over $p$-adic fields. **Barrier:** there is no Hasse principle for sections — Stix and others exhibit the gap, and the failure is governed by Tate–Shafarevich-type obstructions, so local solvability does not force global geometricity.

## Birational section conjecture

**Core idea:** replace $\pi_1$ of the curve by the absolute Galois group of its function field $k(X)$, where extra valuation-theoretic structure (decomposition and inertia groups) becomes available. This is often more tractable. **Best result:** Koenigsmann (2005) proved the birational section conjecture over $p$-adic fields; Pop (2010s) proved strong forms over large fields and $p$-adically/real closed fields; Stix and Esnault–Wittenberg gave further cases. **Barrier:** descending from the birational (function-field) statement to the original curve-level conjecture over a *number* field is not formal — number fields lack the local rigidity that drives the $p$-adic proofs, and global birational results over $\mathbb{Q}$ remain out of reach.

## Minimalist / nilpotent and pro-$p$ quotients

**Core idea:** weaken the group from full $\pi_1$ to a metabelian, two-step nilpotent, or pro-$p$ quotient, asking whether sections of the quotient sequence are already geometric. Success here would prove the conjecture using far less of the group. **Best result:** Wickelgren and others establish that the $3$-nilpotent / lower-central-series obstructions (Massey products, the "$n$-nilpotent section conjecture") can already detect non-geometric sections in examples; the cuspidalization program (Mochizuki, Hoshi) reconstructs configuration-space data from quotients. **Barrier:** for the *positive* direction, abelian and even metabelian quotients are provably too weak — they cannot in general distinguish geometric from non-geometric sections, so one cannot truncate the group too far.

## Obstruction theory: descent, Brauer–Manin, étale homotopy

**Core idea:** sections live in the "fake" rational points $X(\mathbb{A}_k)^{\mathrm{Br}}$ or the étale-homotopy fixed points; the section conjecture predicts these obstructions cut out exactly the real points. **Best result:** Harari–Stix, Stix, and Haran–Jarden relate sections to the Brauer–Manin set; Esnault–Wittenberg (2009) tie surjectivity to finiteness of $\Sha$ of the Jacobian and to the cycle-class / Tate conjecture circle. Conditional on widely believed finiteness statements, partial surjectivity follows in cases. **Barrier:** these are reductions, not proofs — they trade the section conjecture for equally deep unproven inputs ($\Sha$ finiteness, Tate conjecture).

## Anabelian reconstruction and Mochizuki's framework

**Core idea:** leverage the *isomorphism* anabelian theorem (Mochizuki 1996: $\pi_1$ over sub-$p$-adic fields determines the curve) and its cuspidalization refinements to control sections. **Best result:** mono-anabelian reconstruction recovers the curve and its function field from $\pi_1$, supplying the rigidity that injectivity needs and constraining the shape of sections. **Barrier:** reconstruction recovers the *curve*, not a *point* from a section; bridging "I can rebuild $X$" to "this section is $s_x$ for some $x$" is precisely the open problem. Mochizuki's broader inter-universal Teichmüller theory is not accepted by the community as resolving these questions.

## Real and archimedean analogues

**Core idea:** over $\mathbb{R}$ the picture is fully understood and serves as a testing ground. **Best result:** the **real section conjecture** is a theorem — Mochizuki, and Pál, showed sections over $\mathbb{R}$ correspond to real points together with connected components / "sections at infinity", giving a complete topological picture. **Barrier:** $\mathbb{R}$ is too rigid to model number fields; the archimedean proof exploits the order topology and has no analogue at finite or global places.

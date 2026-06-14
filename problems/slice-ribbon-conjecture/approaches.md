# Approaches — The Slice–Ribbon Conjecture

_Major strategies, partial results, and barriers._

The conjecture is attacked from two opposite directions: **(A)** prove it for ever-larger families by showing "slice $\Rightarrow$ ribbon" directly (typically by certifying that every slice candidate is in fact ribbon, or that no member is slice at all); and **(B)** search for a **counterexample** — a smoothly slice knot proved *not* ribbon. No general proof or counterexample exists. The principal lines of attack:

## Lattice embeddings and Donaldson's diagonalization

**Core idea.** If a knot $K$ is slice, then the double branched cover $\Sigma_2(K)$ bounds a rational homology ball. For many knot families $\Sigma_2(K)$ is a lens space or a small Seifert space bounding a canonical *negative-definite* 4-manifold (a plumbing). Donaldson's theorem forces the intersection form of any smooth filling to embed in a diagonal lattice $-\mathbb{Z}^n$; combining this with the rational-homology-ball constraint yields strong, often finite, **lattice-embedding** conditions. Lisca's celebrated solution for **2-bridge knots** (2007) classifies exactly which lens spaces bound rational homology balls and matches them precisely to the ribbon 2-bridge knots.

**Best result reached.** The full conjecture for all **2-bridge (rational) knots** (Lisca, 2007), and for **odd 3-pretzel knots** $P(p,q,r)$ (Greene–Jabuka, 2011); extensions to many **Montesinos knots** (Lecuona and collaborators).

**Barrier.** The method needs $\Sigma_2(K)$ to bound a *definite* plumbing whose lattice is tractable — true for 2-bridge and Montesinos knots, but the double cover of a general knot is an arbitrary 3-manifold with no such structure. The technique does not scale beyond "small Seifert / plumbed" doubles.

## Heegaard Floer $d$-invariants and correction terms

**Core idea.** Ozsváth–Szabó's $d$-invariants (correction terms) of $\Sigma_2(K)$, and the Manolescu–Owens $\delta$ invariant, obstruct a rational homology sphere from bounding a rational homology ball. These refine the lattice obstruction and detect non-sliceness where Donaldson's theorem alone is silent.

**Best result reached.** Sharp non-sliceness verdicts that complete the case analyses for pretzel and Montesinos families; ruling out sliceness of many candidate "potential counterexamples."

**Barrier.** $d$-invariants obstruct sliceness but do not, by themselves, certify ribbon-ness; they confirm the conjecture only by eliminating the non-ribbon slice candidates, family by family.

## Knot Floer and the $\tau$, $\Upsilon$, $\nu^+$, $\varepsilon$ concordance invariants

**Core idea.** The Ozsváth–Szabó concordance invariant $\tau$, Rasmussen's $s$ (from Khovanov homology), and refinements ($\Upsilon$, $\nu^+$, $\varepsilon$, $\phi_j$) give lower bounds on the **smooth 4-genus** and obstruct sliceness. They are central to deciding whether specific candidate knots are slice at all.

**Best result reached.** Resolution of the slice status of long lists of low-crossing knots (the KnotInfo program), narrowing where a counterexample could hide.

**Barrier.** These are *concordance* invariants: they vanish on slice knots and so cannot distinguish slice-but-non-ribbon from ribbon. They prune candidates but cannot prove the conjecture.

## The handle / Morse-theoretic (ribbon = no maxima) attack

**Core idea.** Reformulate "ribbon" as "the slice disk admits a Morse function with no local maxima." A counterexample is then a slice disk that *provably cannot* be simplified to remove all maxima. This connects to the **Slice–Ribbon** problem's sibling, the question of whether handle structures on $B^4$ can always be simplified, and to Akbulut–Kirby–style attempts.

**Best result reached.** Reframing only; it supplies the language for candidate counterexamples (e.g., the **square knot vs. granny knot** type analyses and the **(2,1)-cable / Whitehead double** candidates).

**Barrier.** No invariant is known that distinguishes "slice with no-maxima disk" from "slice with maxima"; the obstruction one needs is precisely what is missing. This is widely seen as the heart of the difficulty.

## Searching among Whitehead doubles, cables, and fibered candidates

**Core idea.** Build candidate counterexamples from operations that preserve sliceness but threaten ribbon-ness — untwisted Whitehead doubles, satellite/cabling constructions, and Brieskorn-type fibered knots — then test ribbon-ness combinatorially.

**Best result reached (negative-result flavor).** Repeated *failures* to break the conjecture: candidate after candidate either is shown ribbon or is shown non-slice. Notably, work on the **fibered, ribbon** condition and on **algebraically slice** but non-slice knots (Casson–Gordon, 1975) shaped which constructions are even viable.

**Barrier.** Producing a knot that is *certifiably slice* yet *certifiably non-ribbon* requires simultaneously a positive sliceness certificate (hard; usually only ribbon knots come with one) and a non-ribbon obstruction (no such smooth invariant is known). This double bind is why no counterexample has surfaced.

## Cross-cutting obstacle

Every certified-slice knot anyone can currently exhibit comes *with a ribbon presentation* — the only general way to prove a knot smoothly slice is essentially to build a ribbon (or band) move sequence. Thus the conjecture is hard to disprove because our sliceness certificates are themselves ribbon certificates, and hard to prove because no 4-dimensional invariant sees the "no maxima" distinction.

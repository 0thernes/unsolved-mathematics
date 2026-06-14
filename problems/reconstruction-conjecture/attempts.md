# Attempts — The Reconstruction Conjecture (Ulam)

_Notable attempts, near-misses, retracted proofs._

## Foundational partial results

The earliest genuine progress is **Kelly's proof that trees are reconstructible** (thesis 1942; published 1957), together with **Kelly's Lemma**, which underwrites virtually everything that followed. Kelly and later **Bondy and Manvel** extended reconstructibility to **disconnected graphs**, graphs with an isolated or pendant vertex, and **regular graphs** (a regular graph is trivially reconstructible because the deck reveals the degree and number of edges, and all $n$-vertex regular graphs of a given degree with the right cards coincide). These are not near-misses but solid theorems carving out tractable territory.

## The dense-graph near-resolution (edge reconstruction)

The deepest "almost there" results concern the **Edge Reconstruction Conjecture**. **Lovász (1972)** settled all graphs with $m > \binom{n}{2}/2$ edges. **V. Müller (1977)** sharpened the bound to $2^{m-1} > n!$, which covers every graph whose number of edges exceeds about $\log_2 n!$ — i.e. all but the sparse graphs. Combined, these results mean the edge conjecture is open only for a thin sparse band, and many practitioners regard the edge version as "morally" almost done while the vertex version remains genuinely open.

## The probabilistic near-miss

**Béla Bollobás (1990)** proved that **almost all graphs are reconstructible**, with reconstruction number $3$ for the random graph. This is the closest thing to a resolution in spirit: it shows counterexamples, if they exist, form a vanishingly small and highly structured set. It is a near-miss only in the precise sense that "almost all" is not "all" — the structured exceptions (large-automorphism-group graphs, certain sparse families) are exactly the ones the probabilistic method cannot see.

## Computational verification

Exhaustive machine checking has confirmed the conjecture for all small graphs. Using the **nauty** graph-isomorphism software, **Brendan McKay** verified that **every graph on up to 11 vertices is reconstructible** (and the bound has since been pushed further). No counterexample has ever been found at any size, which is strong empirical support but, of course, not a proof. McKay also computed reconstruction numbers, confirming Bollobás-type behavior in the small cases.

## Cautionary refutations of neighboring problems

A recurring "attempt" pattern is to import a method from a related setting — and these refutations explain why such imports fail:

- **Stockmeyer (1977)** found infinite families of **non-reconstructible tournaments and digraphs**, including counterexamples to the directed reconstruction conjecture that had been informally expected to hold. This famously dashed hopes that a purely combinatorial/counting argument transferable to digraphs could settle the undirected case.
- **Kocay (1987)** and others produced **non-reconstructible hypergraphs**; **infinite-graph** counterexamples are also known (Fisher; and constructions in the Nash-Williams circle). 

These are not failed attempts at the main conjecture but decisive obstructions: any valid proof must avoid generalizing to these structures.

## Claimed proofs and disputed announcements

The Reconstruction Conjecture has attracted a steady trickle of **claimed full proofs**, predominantly circulated as **arXiv preprints** rather than in refereed venues. As a class these have **not been accepted by the community**, and none has appeared in a major peer-reviewed journal as a verified resolution. The standard, neutral objection raised against such manuscripts is consistent: they typically reduce the problem to a counting or symmetry argument that, on inspection, either (i) silently assumes a form of the global gluing the deck does not actually determine, or (ii) would apply verbatim to **digraphs**, where Stockmeyer's counterexamples prove the conclusion false — an immediate sign of a gap. Because the digraph refutation is so clean, it functions as a quick litmus test that has repeatedly exposed flaws in announced proofs.

In keeping with this dossier's standards, no specific preprint is cited here as a resolution: as of 2026 the conjecture's official status is **open**, and there is **no community-accepted proof or disproof** for finite simple graphs. Readers encountering a "solution" preprint should check, first, whether its argument survives the directed-graph test, and second, whether it has cleared peer review — to date none has.

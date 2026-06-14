---
title: "Meta-Analysis: The Reconstruction Conjecture (Ulam)"
slug: reconstruction-conjecture
author: Alexander Donahue
type: ai-assisted-meta-analysis
peer_reviewed: false
problem_status: open
ai_review:
  claude:
    verdict: accept-with-revisions
    date: "2026-06-14"
    version: "claude-opus-4-8"
    summary: "A faithful and appropriately hedged survey of an open problem whose factual backbone is sound but whose citation layer carries explicit verification flags that must be checked against primary sources."
  gpt:
    verdict: pending
  gemini:
    verdict: pending
  grok:
    verdict: pending
human_review: pending
---

# Meta-Analysis: The Reconstruction Conjecture (Ulam)

> **AI-generated meta-analysis — not peer-reviewed.** Curated and accredited by **Alexander Donahue** (human-in-the-loop). A survey/assessment of an open problem; it makes no claim of a new result. Citations carry verification flags and require human source-checking.

## Abstract

The Reconstruction Conjecture, posed by Stanisław Ulam and Paul Kelly around 1941, asserts that every finite simple graph on at least three vertices is determined up to isomorphism by its **deck**: the multiset of vertex-deleted subgraphs $G - v$, each taken only up to isomorphism. Despite an elementary statement and eight decades of attention, it remains **open**. This meta-analysis surveys the state of the art: the counting machinery descending from Kelly's Lemma; the large catalogue of reconstructible graph classes and recognizable invariants; the near-resolution of the dense-graph *edge* analogue by Lovász and Müller; Bollobás's theorem that almost all graphs are reconstructible from three cards; and Brendan McKay's exhaustive verification for small $n$. It then examines the structural barriers — counting fixes how many pieces exist but not how they glue, and the decisive refutation of the directed, hypergraph, and infinite analogues (Stockmeyer; Kocay) forces any valid proof to exploit something specific to finite undirected simple graphs. We assess what a resolution would require and flag, throughout, that the cited literature carries verification flags requiring primary-source confirmation.

## 1. Statement and significance

For a finite simple graph $G$ on $n$ vertices, the **deck** is the multiset $\{\, G - v : v \in V(G)\,\}$ of $n$ **cards**, each an unlabelled (isomorphism-only) vertex-deleted subgraph. The conjecture states that for $n \ge 3$ the deck determines $G$ up to isomorphism — equivalently, no two non-isomorphic graphs on $\ge 3$ vertices are **hypomorphic** (share a deck). The threshold $n \ge 3$ is necessary: the two graphs on two vertices have identical decks.

The problem sits at the heart of structural graph theory because it asks the cleanest possible version of a recurring question across mathematics — *to what extent does a collection of substructures determine the whole?* — an Ulam theme also visible in his metric-space framing of the original question. It connects to graph isomorphism, extremal graph theory, and graph polynomials, and serves as a fixed benchmark in every survey of combinatorics' great open problems. Its difficulty is rated high in this dossier (difficulty 78) against modest centrality (45) and low tractability (38), reflecting a problem that is famous and stubborn rather than a load-bearing hub.

## 2. State of the art

The official status is **open** as of 2026: no counterexample and no community-accepted proof exists for finite simple graphs. What is firmly established is a large body of partial and recognizability results.

- **Reconstructible classes.** Trees (Kelly), disconnected graphs, regular graphs, graphs with an end-vertex, unit-interval graphs, and maximal-planar and outerplanar graphs are proven reconstructible.
- **Recognizable invariants.** Via Kelly's Lemma the deck determines the number of edges, the degree sequence, the number of components, connectivity, planarity, the count of subgraphs isomorphic to any fixed smaller graph, and (Tutte) the characteristic, chromatic, and rank/Tutte polynomials.
- **Dense graphs (edge version).** Müller's bound $2^{m-1} > n!$, building on Lovász, proves *edge*-reconstructibility for essentially every dense graph.
- **Generic case.** Bollobás proved almost all graphs are reconstructible, with reconstruction number $3$; potential counterexamples form a density-zero, highly structured set.
- **Computation.** Exhaustive checking via *nauty* (McKay) confirms reconstructibility for all graphs up to at least $n = 11$, with no exception ever found.
- **Negative results on relatives.** The conjecture is **false** for digraphs/tournaments (Stockmeyer), hypergraphs (Kocay), and infinite graphs — facts that do not bear on the finite simple case but tightly constrain admissible proofs.

There are no widely used *conditional* theorems of the "assuming X" type; the frontier is unconditional and incremental, each settled class shrinking the residue where a counterexample could hide.

## 3. Principal approaches and barriers

**Kelly's counting lemma.** For any $H$ with $|V(H)| < |V(G)|$, the number of subgraphs of $G$ isomorphic to $H$ is reconstructible. This underwrites nearly every positive result and yields the recognizable-invariant cascade above, including Tutte's polynomial reconstructions. **Barrier:** counting fixes *how many* of each piece exist, not *how they fit*; the lemma is blind to the global gluing and cannot by itself close the gap.

**Reduction to recognizable classes.** If a defining property ("tree", "disconnected", "regular") is recognizable from the deck and the class is internally reconstructible, those graphs are settled. **Barrier:** the hard residue is exactly the graphs that resist classification — sparse, irregular, $2$-connected graphs with small automorphism groups.

**Dense / edge-counting attack (Lovász–Müller).** An extremal permutation-group / Möbius-function argument on the subgraph lattice settles all sufficiently dense graphs for the edge version. **Barrier:** the method needs many edges; the open vertex cases are sparse, where the bounds are vacuous.

**Probabilistic (Bollobás).** The potential-counterexample set has density zero. **Barrier:** measure-zero is not emptiness; the structured, low-entropy exceptions are precisely where genericity is silent.

**Algebraic / group-theoretic.** Lattice Möbius functions, characteristic-polynomial structure, and automorphism constraints give clean theorems. **Barrier:** the relevant linear systems are singular exactly in the hard sparse cases.

**Decisive negative analogues.** Stockmeyer's non-reconstructible tournaments, Kocay's hypergraphs, and infinite-graph counterexamples refute any argument that would generalize to those settings. A successful proof must exploit something specific to finite, undirected, simple graphs.

## 4. Critical assessment

The dossier's central claims are consistent with the mathematical consensus and are appropriately hedged. The clearest organizing insight — that the **directed-graph test functions as a litmus** against announced proofs, since any counting/symmetry argument transferring to digraphs is refuted by Stockmeyer — is correct and is the standard, neutral objection to circulated preprints. The framing of the residue as "sparse, irregular, $2$-connected, small-automorphism" graphs is the right characterization of where every tool (Kelly counting, Lovász–Müller density, Bollobás genericity) simultaneously fails.

Two points warrant calibration. First, the relationship between the vertex and edge conjectures should not be overstated: edge-reconstructibility being "morally almost done" for dense graphs does not narrow the vertex conjecture's genuinely open sparse regime, and the dossier is right to keep them distinct. Second, the historical attributions and dates in the citation table are uneven in confidence — Müller's bound is variously dated 1976/1977, Tutte's polynomial work spans several papers, and Lovász's bound is sometimes stated as $m > \binom{n}{2}/2$ versus the refined forms. These are bibliographic, not mathematical, uncertainties, but they matter for a reference work.

## 5. What a resolution would require / open directions

A proof must handle the sparse, irregular, $2$-connected, small-automorphism graphs where counting is too weak and genericity says nothing, and it must use a property **specific to finite undirected simple graphs** — anything generalizing to digraphs is refuted on arrival. Plausibly viable routes:

1. **A new global invariant** recoverable from the deck that pins down the gluing rather than mere subgraph counts — something the directed case provably lacks.
2. **A structural reduction** to a finite or tightly constrained family, then computer-assisted closure extending the McKay verification with a theorem bounding the worst case.
3. **A symmetry / self-complementary argument** leveraging finiteness and undirected symmetry of the deck's counting matrix to force invertibility in the singular sparse regime.

A disproof would need an explicit hypomorphic pair; the exhaustive small-$n$ checks make any small counterexample impossible, so a disproof would have to be large and structured, against the grain of all evidence.

## 6. Selected references

1. Paul J. Kelly, *A congruence theorem for trees* (1957) — foundational; Kelly's Lemma and trees. [high-confidence]
2. Stanisław M. Ulam, *A Collection of Mathematical Problems* (1960) — broadcasts the conjecture. [high-confidence]
3. Frank Harary, *On the reconstruction of a graph from a collection of subgraphs* (1964) — modern vocabulary; Edge Reconstruction Conjecture. [high-confidence]
4. Frank Harary, *Graph Theory* (1969) — text introducing reconstruction terminology. [high-confidence]
5. László Lovász, *A note on the line reconstruction problem* (1972) — first strong edge bound. [high-confidence]
6. Bennet Manvel, *Reconstructing graphs* (survey, 1974). [needs-verification]
7. Vladimír Müller, *On graph reconstruction: a counting approach to edge reconstruction* (1976) — sharp $2^{m-1} > n!$ bound. [needs-verification]
8. Paul K. Stockmeyer, *The falsity of the reconstruction conjecture for tournaments* (1977) — non-reconstructible digraphs. [high-confidence]
9. W. T. Tutte, *On graphic and reconstructible properties / reconstruction of polynomials* (1977/1979). [needs-verification]
10. J. A. Bondy & R. L. Hemminger, *All the king's horses: a guide to reconstruction* (1979) — standard survey. [high-confidence]
11. William L. Kocay, *A family of nonreconstructible hypergraphs* (1987) — negative result. [needs-verification]
12. C. St. J. A. Nash-Williams, *The reconstruction problem* (in *Selected Topics in Graph Theory*, 1988) — recognizability machinery. [needs-verification]
13. Béla Bollobás, *Almost every graph has reconstruction number three* (1990) — breakthrough generic result. [high-confidence]
14. J. A. Bondy, *A graph reconstructor's manual* (1991) — the standard reference. [high-confidence]
15. Brendan D. McKay, *Small graphs are reconstructible / reconstruction numbers* (1997/2004) — computational verification. [needs-verification]

## AI Review Panel

### Claude (Anthropic) — in-house review

The survey is faithful to the consensus picture and, importantly, honest about the limits of its own evidence. Its strengths are real: it correctly identifies the structural core of the difficulty (the counting machinery determines piece-counts but not gluing), it draws the right boundary between the vertex and edge conjectures, and it elevates the single most useful heuristic in the field — the directed-graph refutation as a quick test that a proposed proof has a gap. The catalogue of reconstructible classes and recognizable invariants matches what I understand to be established, and the open-directions section avoids the common failure mode of presenting incremental class results as if they trend toward a proof.

My principal reservation is bibliographic, and it is not minor for a reference work. The papers table explicitly flags most non-foundational rows as **needs-verification** or **ai-suggested**, and the dossier candidly notes that several titles, years, and venues may be conflated — Müller's bound dated 1976 versus 1977, Lovász's bound stated in multiple forms, Tutte's polynomial work spread across papers, and rows 23–25 of the source table being plausible-but-unconfirmed surveys. A human reviewer must check every cited paper against a primary source (MathSciNet/zbMATH, original journal pages) before this is treated as citable; no DOI or arXiv id should be trusted from this document.

Two further cautions. (i) There is some single-source reliance on the dossier's own framing — claims such as "verified to $n = 11$ and beyond" and "reconstruction number three for almost all graphs" are correct as I understand them but rest here on the dossier rather than independent confirmation, and should be checked against McKay's and Bollobás's primary statements. (ii) The phrase "morally almost done" for the edge conjecture is appropriately scare-quoted but a careless reader could mistake it for progress on the vertex conjecture; the text does guard against this, and that guard should be preserved. The single most important thing a human reviewer should verify is the **exact statement and attribution of the Lovász and Müller edge-reconstruction bounds**, since those are the load-bearing "near-resolution" claims and are precisely where the dossier's own confidence flags are weakest.

**Verdict:** accept-with-revisions.

### GPT (OpenAI) — pending
_Not yet run. To complete the panel, run the prompt in docs/review/REVIEW-TEMPLATE.md through GPT and record the verdict here and in the front matter._

### Gemini (Google) — pending
_Not yet run. See docs/review/REVIEW-TEMPLATE.md._

### Grok (xAI) — pending
_Not yet run. See docs/review/REVIEW-TEMPLATE.md._

## Human verification

AI review is not human peer review. This assessment is offered for academic verification per ../docs/review/ACADEMIC-REVIEW.md, and its citations in particular require source-checking against primary literature before reuse. Status: human_review pending.

---
*Accredited to **Alexander Donahue** · The Unsolved Mathematics Atlas · CC BY 4.0. Cite per CITATION.cff.*

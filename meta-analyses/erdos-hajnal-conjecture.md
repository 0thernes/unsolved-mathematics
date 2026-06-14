---
title: "Meta-Analysis: The Erdős–Hajnal Conjecture"
slug: erdos-hajnal-conjecture
author: Alexander Donahue
type: ai-assisted-meta-analysis
peer_reviewed: false
problem_status: active-progress
ai_review:
  claude:
    verdict: accept-with-revisions
    date: "2026-06-14"
    version: "claude-opus-4-8"
    summary: "A faithful and appropriately hedged survey of an open problem; its claims about recent breakthroughs are plausible and well-attributed but rest on references that still carry verification flags."
  gpt:
    verdict: pending
  gemini:
    verdict: pending
  grok:
    verdict: pending
human_review: pending
---

# Meta-Analysis: The Erdős–Hajnal Conjecture

> **AI-generated meta-analysis — not peer-reviewed.** Curated and accredited by **Alexander Donahue** (human-in-the-loop). A survey/assessment of an open problem; it makes no claim of a new result. Citations carry verification flags and require human source-checking.

## Abstract

The Erdős–Hajnal conjecture asserts that for every graph $H$ there is a constant $c(H)>0$ such that every $n$-vertex graph with no induced copy of $H$ contains a clique or independent set of size at least $n^{c(H)}$ — a polynomial leap over the logarithmic homogeneity forced in general graphs. Posed in 1989, it remains open, but its dossier status is "active-progress," and the assessment here supports that label. The classical unconditional bound $\exp(c\sqrt{\log n})$ stood for thirty-three years until Nguyen–Scott–Seymour improved it to $\exp(c\sqrt{\log n\,\log\log n})$, and in 2023 Bucić–Nguyen–Scott–Seymour resolved the long-standing test case $H=C_5$ with a genuine polynomial bound. This meta-analysis synthesizes the dossier's account of the principal strategies — substitution closure, explicit structural case analysis, Fox–Sudakov density/bi-clique reformulations, the Nguyen–Scott–Seymour program, and model-theoretic tameness — and the barriers (the prime-graph obstruction, the regularity wall) that keep the conjecture out of reach in full generality. It then offers a skeptical referee assessment, flagging citation reliability as the document's chief weakness.

## 1. Statement and significance

**Conjecture (Erdős–Hajnal, 1989).** For every graph $H$ there exists $c(H)>0$ such that every $H$-free graph $G$ on $n$ vertices — that is, $G$ contains no induced subgraph isomorphic to $H$ — has a clique or independent set ("homogeneous set") of size at least $n^{c(H)}$.

The significance is best understood against Ramsey theory. Ramsey's theorem guarantees a homogeneous set of size $\tfrac{1}{2}\log_2 n$ in any graph, and Erdős's 1947 probabilistic bound shows this logarithmic order is essentially optimal for general graphs. The conjecture proposes that a single forbidden induced pattern destroys enough "genericity" — random graphs being generic precisely because they contain every small graph as an induced subgraph — to force an exponentially larger, polynomial-size island of perfect order. The clique/stable-set form, a bi-clique ("large complete or empty bipartite pair") form, and the polynomial Rödl property are known to be equivalent, so a resolution of any one settles all. The problem is a central organizing question of structural graph theory and modern Ramsey theory.

## 2. State of the art

The conjecture is **open in full generality** and widely believed true. The best unconditional general bound is a homogeneous set of size $\exp\big(c(H)\sqrt{\log n\,\log\log n}\big)$ (Nguyen–Scott–Seymour, 2022–2023), the first asymptotic improvement on the Erdős–Hajnal $\exp\big(c\sqrt{\log n}\big)$ of 1989 — but both remain *subpolynomial*, short of the conjectured $n^{c}$.

The conjecture is verified for a growing list of $H$: all graphs on $\le 4$ vertices; all cographs ($P_4$-free graphs), via the substitution theorem (Alon–Pach–Solymosi, 2001); the bull (Chudnovsky–Safra, 2015); and, decisively, the five-cycle $C_5$ (Bucić–Nguyen–Scott–Seymour, 2023), the first prime non-cograph beyond size 4 to fall, with a polynomial bound. Closures of these under substitution and blow-up, plus several sporadic graphs from the 2023–2024 Nguyen–Scott–Seymour papers, are also settled, and a directed analogue holds for many tournaments (Berger–Choromanski–Chudnovsky and successors). Conditionally, stable classes (forbidding a half-graph) admit homogeneous sets of *linear* size, and bounded-VC-dimension (NIP) regularity gives strong structure — but not polynomial homogeneity.

## 3. Principal approaches and barriers

**Substitution and closure.** Alon–Pach–Solymosi (2001) showed the EH property is preserved under vertex substitution, yielding all cographs and infinite families built from verified prime seeds. The barrier is fundamental: substitution is silent on *prime* graphs (those with no nontrivial modular decomposition), where all remaining difficulty lives.

**Structural case analysis.** For specific small $H$ one exploits forced structure, often via a polynomial-Rödl step. This defeated the bull and $C_5$, but the proofs are intricate and graph-specific; $P_5$, the apparent "next" path, remains open, showing the methods are not uniform.

**Fox–Sudakov density / bi-clique.** Dependent random choice and regularity arguments yield the equivalences and quantitative gains in structured cases, but regularity incurs tower-type or $\exp(c\sqrt{\log n})$ losses — exactly the wall to be broken.

**Nguyen–Scott–Seymour program.** Tree-decomposition and asymptotic-dimension structure theory produced both the loglog general bound and the $C_5$ breakthrough. Yet the improvement is only a $\sqrt{\log\log n}$ factor in the exponent; crossing to $n^{c}$ uniformly appears to need a genuinely new idea.

**Model-theoretic tameness.** $H$-free classes are NIP; the *stable* case yields linear homogeneity. The unstable (order-bearing) part, with the half-graph as canonical obstruction, is precisely where polynomial bounds are unknown.

## 4. Critical assessment

The dossier's "active-progress" status is well-justified. After three decades of stasis, two distinct advances — the loglog general improvement and the $C_5$ resolution — emerged from a single coherent toolkit, and the verified-case list is genuinely expanding. The reformulation equivalences (Fox–Sudakov) give the field a unified target, which is methodologically healthy.

That said, the qualitative gap remains enormous. Every general technique is stuck at the $\exp(c\sqrt{\log n\,\cdot\,\mathrm{poly}\log\log n})$ ceiling; the distance from there to any $n^{c}$ is the whole problem, not a refinement. The case-by-case nature of the prime-graph results is a structural, not merely tactical, obstacle: each new prime seed demands bespoke work, and the failure to resolve even $P_5$ after the $C_5$ success is a sober indicator that no uniform principle is yet in hand. The dossier is honest on all these points and does not overstate the breakthroughs. Its weakness is bibliographic, not analytic (see Section 6 and the panel review).

## 5. What a resolution would require / open directions

A full proof must handle prime graphs *uniformly* across all $H$, producing a homogeneous set of size $n^{c(H)}$ and thereby crossing the subpolynomial wall that all general methods hit. Plausible routes recorded in the dossier: (1) extend the $C_5$ tree-decomposition / asymptotic-dimension machinery to all paths and then to a general principle; (2) find an essentially regularity-free argument converting local pattern-avoidance directly into polynomial order; (3) leverage NIP tameness to bridge the stable and unstable cases; (4) push the general exponent beyond $\sqrt{\log n\,\log\log n}$ toward $(\log n)^{1-o(1)}$, a major step short of the target. None is known to suffice; the central missing ingredient is uniformity.

## 6. Selected references

1. P. Erdős, G. Szekeres (1935), *A combinatorial problem in geometry*. [high-confidence]
2. P. Erdős (1947), *Some remarks on the theory of graphs*. [high-confidence]
3. V. Rödl (1977), *On the dimension of a graph (and Ramsey-type density results)*. [needs-verification]
4. P. Erdős, A. Hajnal (1989), *Ramsey-type theorems*. [high-confidence]
5. P. Erdős, A. Hajnal, J. Pach (1989), *A bipartite analogue of Dilworth's theorem / Ramsey-type results*. [needs-verification]
6. N. Alon, J. Pach, J. Solymosi (2001), *Ramsey-type theorems with forbidden subgraphs*. [high-confidence]
7. J. Fox, B. Sudakov (2009), *Density theorems for bipartite graphs and related Ramsey-type results*, arXiv:0707.4159. [needs-verification]
8. M. Conlon, J. Fox, B. Sudakov (2010), *Erdős–Hajnal-type theorems in hypergraphs*. [ai-suggested]
9. E. Berger, K. Choromanski, M. Chudnovsky (2013), *The Erdős–Hajnal conjecture for tournaments*. [needs-verification]
10. M. Chudnovsky (2014), *The Erdős–Hajnal conjecture — a survey*. [high-confidence]
11. M. Chudnovsky, S. Safra (2015), *The Erdős–Hajnal conjecture for bull-free graphs*. [needs-verification]
12. T. Nguyen, A. Scott, P. Seymour (2022), *Induced subgraphs and tree-decompositions (EH applications)*. [needs-verification]
13. T. Nguyen, A. Scott, P. Seymour (2023), *A loglog improvement to the Erdős–Hajnal bound*. [needs-verification]
14. M. Bucić, T. Nguyen, A. Scott, P. Seymour (2023), *The Erdős–Hajnal conjecture for the five-cycle ($C_5$)*. [needs-verification]
15. É. Bonnet, E. Kim, S. Thomassé, R. Watrigant (2021), *Twin-width and tame graph classes (EH connections)*, arXiv:2004.14789. [needs-verification]

## AI Review Panel

### Claude (Anthropic) — in-house review

The survey is technically faithful and, crucially, appropriately hedged. It states the conjecture precisely, distinguishes the unconditional general bound from the verified-case results, and correctly frames the equivalences (clique/stable-set, bi-clique, polynomial Rödl) so that the reader understands why the field treats them as a single target. The barrier discussion — the prime-graph obstruction to substitution and the regularity wall — is the document's strongest section, and it resists the temptation to read the $C_5$ breakthrough as more than it is. The repeated emphasis that $P_5$ remains open despite the $C_5$ success is exactly the right note of caution.

My principal reservation is bibliographic. The dossier's own papers table marks most of the load-bearing modern citations — the Chudnovsky–Safra bull-free result, the Nguyen–Scott–Seymour loglog improvement, and the Bucić–Nguyen–Scott–Seymour $C_5$ resolution — as "needs-verification," and several supporting rows as "ai-suggested," with titles, years, and identifiers explicitly flagged as unconfirmed. The two arXiv numbers (0707.4159, 2004.14789) are offered only as plausible matches. A human reviewer must source-check each of these against the original venues before any citation is treated as authoritative; the existence and authorship of these results are well established in the community, but exact metadata here is not.

Two further cautions. First, the narrative leans heavily on a single research cluster (the Princeton/Oxford circle) for nearly all recent progress; this is an accurate reflection of where the advances came from, but the reader should not infer that the broader picture has been independently cross-checked here. Second, the loglog improvement and the $C_5$ resolution are stated as facts without the document itself verifying the proofs — appropriate for a survey, but the single most important thing a human reviewer should confirm is that the $C_5$ result indeed achieves a *polynomial* bound (the claim that elevates it from incremental to landmark) and that the general bound is correctly quoted as $\exp(c\sqrt{\log n\,\log\log n})$ rather than a misremembered variant.

**Verdict:** accept-with-revisions.

### GPT (OpenAI) — pending

_Not yet run. To complete the panel, run the prompt in docs/review/REVIEW-TEMPLATE.md through GPT and record the verdict here and in the front matter._

### Gemini (Google) — pending

_Not yet run. See docs/review/REVIEW-TEMPLATE.md._

### Grok (xAI) — pending

_Not yet run. See docs/review/REVIEW-TEMPLATE.md._

## Human verification

AI review is not human peer review. This assessment is offered for academic verification per ../docs/review/ACADEMIC-REVIEW.md; an expert in structural graph theory and Ramsey theory should confirm the statements, the quantitative bounds, and especially the reference metadata before the document is relied upon. Status: human_review pending.

---
*Accredited to **Alexander Donahue** · The Unsolved Mathematics Atlas · CC BY 4.0. Cite per CITATION.cff.*

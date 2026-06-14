---
title: "Meta-Analysis: Hadwiger's Conjecture (Graph Coloring)"
slug: hadwiger-conjecture
author: Alexander Donahue
type: ai-assisted-meta-analysis
peer_reviewed: false
problem_status: active-progress
ai_review:
  claude:
    verdict: accept-with-revisions
    date: "2026-06-14"
    version: "claude-opus-4-8"
    summary: "A faithful, well-calibrated survey of an open problem whose quantitative frontier moved sharply after 2019; the asymptotic claims are sound but the bibliographic identifiers must be source-checked before publication."
  gpt:
    verdict: pending
  gemini:
    verdict: pending
  grok:
    verdict: pending
human_review: pending
---

# Meta-Analysis: Hadwiger's Conjecture (Graph Coloring)

> **AI-generated meta-analysis — not peer-reviewed.** Curated and accredited by **Alexander Donahue** (human-in-the-loop). A survey/assessment of an open problem; it makes no claim of a new result. Citations carry verification flags and require human source-checking.

## Abstract

Hadwiger's Conjecture (1943) asserts that every graph with no $K_t$ minor is $(t-1)$-colorable, equivalently that every graph $G$ satisfies $h(G) \ge \chi(G)$, where $h(G)$ is the order of the largest clique minor (the Hadwiger number). It is a vast generalization of the Four Color Theorem, which is exactly the case $t=5$. This meta-analysis synthesizes the dossier on the problem's history, the state of the art, the principal lines of attack, and the barriers that have kept it open for over eighty years. The exact conjecture is proved unconditionally for $t \le 6$; the cases $t=5$ and $t=6$ rest on the Four Color Theorem, and $t=7$ is the first open value. The quantitative frontier — bounding $\chi(G)$ as a function of $h(G)$ — stalled for nearly four decades at $O(h\sqrt{\log h})$ before the 2019 Norin–Postle–Song breakthrough broke the square-root barrier, with subsequent work reaching $O(h\log\log h)$. The dossier is internally consistent and appropriately cautious; the survey assesses how far the frontier truly stands from the linear and exact targets, and flags every claim requiring primary-source verification.

## 1. Statement and significance

A graph $H$ is a **minor** of $G$ if $H$ arises from a subgraph of $G$ by contracting edges. Hadwiger's Conjecture states:
$$\chi(G) \ge t \implies G \text{ contains } K_t \text{ as a minor},$$
equivalently, every $K_t$-minor-free graph is $(t-1)$-colorable, equivalently $h(G) \ge \chi(G)$. The conjecture's significance is twofold. First, it strictly generalizes the Four Color Theorem: by Wagner's 1937 structure theorem for $K_5$-minor-free graphs, the case $t=5$ is *equivalent* to four-colorability of planar maps. Second, it proposes a clean, scale-free structural law — that the chromatic number is controlled by the largest complete structure surviving contraction — linking the local operation of coloring to the global combinatorics of minors. Bollobás, Catlin, and Erdős called it one of the deepest unsolved problems in graph theory, and that assessment remains the community consensus.

## 2. State of the art

**Exact cases (unconditional).** The cases $t \le 3$ are elementary. The case $t=4$ was proved by Hadwiger (1943) and independently by Dirac (1952). The case $t=5$ is equivalent to the Four Color Theorem (Wagner 1937 + Appel–Haken 1976, later formally verified in Coq by Gonthier 2005). The case $t=6$ was proved by Robertson, Seymour, and Thomas (1993), who showed any minimal counterexample is **apex** (planar plus one vertex), hence 5-colorable, again reducing to the Four Color Theorem. The first genuinely open exact case is $t=7$.

**Quantitative bounds (unconditional).** Kostochka (1980) and independently Thomason (1984) proved that average degree $\Omega(t\sqrt{\log t})$ forces a $K_t$ minor, and that this is tight; combined with the degeneracy bound $\chi(G) \le d(G)+1$ this yields $\chi(G) = O(h(G)\sqrt{\log h(G)})$. Thomason (2001) pinned the extremal constant at $c = 0.6382\ldots$. This bound stood as the best general result for almost four decades. Norin, Postle, and Song (2019) broke the square-root barrier, reaching exponent $1/4 + o(1)$ on the $\log h$ factor; Postle and Norin–Postle drove the exponent toward $0$; Delcourt and Postle (2021) reached $\chi(G) = O(h(G)\log\log h(G))$, the current record — within a $\log\log$ factor of the linear target.

**Conditional and relaxed results.** The **fractional** Hadwiger Conjecture holds, $\chi_f(G) = O(h(G))$ (Reed–Seymour 2005). The conjecture holds for **almost all** graphs (Bollobás–Catlin–Erdős). In restricted classes — e.g. graphs with no $K_7$ and no $K_{4,4}$ minor are 6-colorable (Kawarabayashi–Toft 2005) — linear or exact bounds are known. A cautionary contrast: the **subdivision** analogue (Hajós' Conjecture) is *false* for $t \ge 7$ (Catlin 1979; Erdős–Fajtlowicz 1981), underscoring that the minor/subdivision distinction is load-bearing.

## 3. Principal approaches and barriers

- **Reduction to the Four Color Theorem.** Structural decomposition (Wagner; Robertson–Seymour–Thomas) settles $t \le 6$. *Barrier:* no tractable decomposition theorem for $K_t$-minor-free graphs is known for $t \ge 7$, and no reduction of $t=7$ to a finite check is in sight.
- **Extremal / density bounds (Mader–Kostochka–Thomason).** Chromatic $\to$ density $\to$ minor gives $O(h\sqrt{\log h})$. *Barrier:* the **$\sqrt{\log t}$ density barrier** is provably real — random graphs $G(n,p)$ decouple density from Hadwiger number ($h = \Theta(n/\sqrt{\log n})$), so counting edges cannot reach the linear target.
- **Beyond the square-root barrier (Norin–Postle–Song and successors).** Arguing about coloring directly rather than worst-case density evades the barrier, halting at $O(h\log\log h)$. *Barrier:* removing the residual $\log\log$ factor appears to need new ideas about the interaction of coloring and connectivity.
- **Linear Hadwiger Conjecture.** The intermediate target $\chi(G) = O(h(G))$ is open in general but established in sparse and excluded-substructure regimes.
- **Graph-minors structure theory.** The Robertson–Seymour decomposition's parameters grow too fast in $t$ to recover $\chi \le t-1$; apex and vortex parts obstruct tight control of $\chi$.

There is no known *negative* barrier (no relativization- or natural-proofs-style obstruction); the consensus is that the conjecture is true and hard, not unprovable.

## 4. Critical assessment

What is solid is unusually well-delineated. The exact cases $t \le 6$ are secure, with the explicit caveat that $t=5,6$ inherit the computer-assisted (now formally verified) status of the Four Color Theorem — a point the dossier states plainly rather than glossing. The quantitative bounds are the genuinely active and genuinely impressive part of the story: the move from $O(h\sqrt{\log h})$ to $O(h\log\log h)$ since 2019 is a real and decisive shift after a near-four-decade stall, and the dossier neither understates nor inflates it.

What remains speculative is the distance to the finish line, and here the survey is honest about a subtlety that casual accounts miss. A $\log\log h$ factor sounds negligible, but the dossier correctly flags that even the **Linear** Hadwiger Conjecture ($\chi = O(h)$, dropping the constant) is open, and that the exact statement ($\chi \le h$, constant $1$) is a further and harder target. The two walls — the $\sqrt{\log t}$ density barrier and the structural wall at $t=7$ — are distinct, and progress on one does not obviously transfer to the other: the asymptotic machinery says nothing about the specific value $t=7$, and a structural resolution of $t=7$ would not yield the general linear bound. The frontier is therefore best described as two separate frontiers that happen to share a name.

The Hajós cautionary tale is the most valuable piece of skepticism in the dossier: the slightly stronger subdivision analogue is false for $t \ge 7$ and for almost all graphs, which should temper any expectation that a clean counting or extremal argument will close Hadwiger's gap. This is a survey that resists optimism where optimism is unearned.

## 5. What a resolution would require / open directions

A full proof must clear both walls. Quantitatively, it must reason about coloring more cleverly than counting edges (to beat the density barrier) and then remove the residual $\log\log$ factor and reach constant $1$. Structurally, it must either produce a Robertson–Seymour-style classification fine enough to control $\chi$ exactly for large $t$, or find an apex-style finite reduction for $t=7$. Plausible routes drawn from the dossier:

1. Extend the Norin–Postle–Song / Delcourt–Postle machinery to prove $\chi(G) = O(h(G))$ (Linear Hadwiger), then attack the constant.
2. Find a decomposition theorem for $K_7$-minor-free graphs analogous to the apex characterization.
3. Probabilistic / entropy and local-sparsification methods tailored to minor-free graphs.
4. Prove odd-Hadwiger or list-coloring strengthenings that imply linear bounds.

## 6. Selected references

1. Klaus Wagner (1937), *Über eine Eigenschaft der ebenen Komplexe*. [high-confidence]
2. Hugo Hadwiger (1943), *Über eine Klassifikation der Streckenkomplexe*. [high-confidence]
3. Gabriel A. Dirac (1952), *A property of 4-chromatic graphs and some remarks on critical graphs*. [high-confidence]
4. Wolfgang Mader (1968), *Homomorphieeigenschaften und mittlere Kantendichte von Graphen*. [high-confidence]
5. Kenneth Appel, Wolfgang Haken (1976), *Every planar map is four colorable, Part I: Discharging*, DOI 10.1215/ijm/1256049011. [high-confidence]
6. Alexander V. Kostochka (1980), *Lower bound of the Hadwiger number of graphs by their average degree*, DOI 10.1007/BF02579141. [high-confidence]
7. Paul A. Catlin (1979), *Hajós' graph-coloring conjecture: variations and counterexamples*, DOI 10.1016/0095-8956(79)90062-5. [needs-verification]
8. Andrew Thomason (1984), *An extremal function for contractions of graphs*, DOI 10.1017/S0305004100061521. [high-confidence]
9. Neil Robertson, Paul Seymour, Robin Thomas (1993), *Hadwiger's conjecture for $K_6$-free graphs*, DOI 10.1007/BF01202354. [high-confidence]
10. Andrew Thomason (2001), *The extremal function for complete minors*, DOI 10.1006/jctb.2000.2013. [needs-verification]
11. Bruce Reed, Paul Seymour (2005), *Fractional colouring and Hadwiger's conjecture*, DOI 10.1006/jctb.1998.1830. [needs-verification]
12. Ken-ichi Kawarabayashi, Bjarne Toft (2005), *Any 7-chromatic graph has $K_7$ or $K_{4,4}$ as a minor*, DOI 10.1007/s00493-005-0019-1. [needs-verification]
13. Georges Gonthier (2005), *A computer-checked proof of the Four Colour Theorem*. [high-confidence]
14. Sergey Norin, Luke Postle, Zi-Xia Song (2019), *Breaking the degeneracy barrier for coloring graphs with no $K_t$ minor*, arXiv:1910.09378. [needs-verification]
15. Michelle Delcourt, Luke Postle (2021), *Reducing Linear Hadwiger's Conjecture to coloring small graphs*, arXiv:2108.01633. [needs-verification]

## AI Review Panel

### Claude (Anthropic) — in-house review

This is a competent and unusually well-calibrated survey. Its principal strength is the clean separation it maintains between three distinct objects that lazier treatments conflate: the exact conjecture ($\chi \le h$), the Linear Hadwiger Conjecture ($\chi = O(h)$), and the specific open exact case $t=7$. The dossier is right that progress on the asymptotics (now $O(h\log\log h)$) does not bear on $t=7$, and that the $\sqrt{\log t}$ density barrier is a genuine, provable obstruction rather than a mere failure of cleverness — the random-graph separation is the correct justification and is stated correctly. The Hajós cautionary contrast is the kind of disciplined skepticism a survey of a famous, frequently "solved" conjecture should foreground.

My concerns are bibliographic and concentrate on the references. Several identifiers carry their own flags for good reason and must be checked against primary sources before any citation is relied upon. Specifically: the DOI listed for Reed–Seymour (2005) on row 16 of the dossier (10.1006/jctb.1998.1830) has a 1998-pattern suffix attached to a 2005 paper, which is internally suspicious and likely conflates two records; this should be resolved. The arXiv numbers for Norin–Postle–Song (1910.09378) and Delcourt–Postle (2108.01633) are plausible but explicitly unverified — the dossier itself flags them needs-verification, and a reviewer should confirm the exact preprint and any published version, including the precise exponent claims ($1/4 + o(1)$ and the $O(h\log\log h)$ record). I would also note that the survey leans on the Norin–Postle / Delcourt–Postle line as a single narrative thread; the attribution of intermediate exponent improvements between "Postle" and "Norin–Postle" should be checked rather than taken from the timeline as written.

The single most important thing a human reviewer should verify is the chain of asymptotic results from 2019–2023 — that the cited papers exist with the stated identifiers, that the exponents and the $O(h\log\log h)$ bound are stated as the survey claims, and whether any of these have since been superseded. If that chain holds, the document is sound; the exact-case claims ($t \le 6$, $t=7$ open) are canonical and not in doubt.

**Verdict:** accept-with-revisions.

### GPT (OpenAI) — pending
_Not yet run. To complete the panel, run the prompt in docs/review/REVIEW-TEMPLATE.md through GPT and record the verdict here and in the front matter._

### Gemini (Google) — pending
_Not yet run. See docs/review/REVIEW-TEMPLATE.md._

### Grok (xAI) — pending
_Not yet run. See docs/review/REVIEW-TEMPLATE.md._

## Human verification

AI review is not human peer review. This meta-analysis is offered for academic verification per ../docs/review/ACADEMIC-REVIEW.md, and its citations — particularly the DOIs and arXiv identifiers flagged above — require checking against primary sources before any scholarly reliance. Status: human_review pending.

---
*Accredited to **Alexander Donahue** · The Unsolved Mathematics Atlas · CC BY 4.0. Cite per CITATION.cff.*

---
title: "Meta-Analysis: The Caccetta–Häggkvist Conjecture"
slug: caccetta-haggkvist-conjecture
author: Alexander Donahue
type: ai-assisted-meta-analysis
peer_reviewed: false
problem_status: open
ai_review:
  claude:
    verdict: accept-with-revisions
    date: "2026-06-14"
    version: "claude-opus-4-8"
    summary: "A faithful and well-scoped survey of an open extremal-digraph problem whose principal weakness is an only-partially-verified bibliography that requires primary-source checking before citation."
  gpt:
    verdict: pending
  gemini:
    verdict: pending
  grok:
    verdict: pending
human_review: pending
---

# Meta-Analysis: The Caccetta–Häggkvist Conjecture

> **AI-generated meta-analysis — not peer-reviewed.** Curated and accredited by **Alexander Donahue** (human-in-the-loop). A survey/assessment of an open problem; it makes no claim of a new result. Citations carry verification flags and require human source-checking.

## Abstract

The Caccetta–Häggkvist conjecture, posed in 1978, asserts that every digraph on $n$ vertices with minimum out-degree at least $n/k$ contains a directed cycle of length at most $k$. The directed cycle $\vec{C}_n$ shows the threshold $n/k$ is tight, making this a sharp Turán-type prediction in the directed setting. The conjecture is open for every $k \ge 3$; the flagship triangle case $k=3$ — minimum out-degree $\ge n/3$ forces a directed triangle — concentrates almost all attention because it is believed to contain the full difficulty. This meta-analysis surveys the statement and its significance, the state of the art, and the principal lines of attack: direct counting, flag algebras, additive combinatorics on Cayley digraphs, probabilistic and entropy methods, and structural/Second-Neighbourhood connections. The strongest general result (Chvátal–Szemerédi, 1985) confirms the linear scaling up to an additive constant; the best unconditional triangle bound ($\approx 0.3465\,n$, via flag algebras) leaves a gap of roughly $0.013\,n$ above the conjectured $1/3$. We assess why this gap is structurally resistant and what a resolution would plausibly require, and we record the verification status of the supporting literature.

## 1. Statement and significance

A *digraph* is a directed graph; its *girth* is the length of a shortest directed cycle. The Caccetta–Häggkvist conjecture links two parameters — minimum out-degree and girth — by a single uniform constant:

> Every digraph $D$ on $n$ vertices in which every vertex has out-degree at least $n/k$ contains a directed cycle of length at most $k$.

Equivalently, a digraph of girth exceeding $k$ must have a vertex of out-degree at most $\lceil n/k\rceil - 1$. The conjecture was introduced by Louis Caccetta and Roland Häggkvist in their 1978 paper *On minimal digraphs with given girth*, presented at the Ninth Southeastern Conference in Boca Raton. It generalizes a 1970 conjecture of Behzad, Chartrand, and Wall on the order of $d$-regular digraphs of given girth.

The case $k=2$ is trivial. The first hard and most-studied case is $k=3$: any digraph with minimum out-degree $\ge n/3$ must contain a directed triangle, equivalently a triangle-free digraph with minimum out-degree $d$ has at least $3d$ vertices. The significance is twofold. First, it is the natural directed analogue of classical (undirected) extremal questions, in a setting where comparatively little machinery existed. Second, the prediction is *sharp*: $\vec{C}_n$ saturates the bound exactly, so the conjecture is a falsifiable claim about an exact constant, not an order-of-magnitude heuristic. Interest from Paul Seymour and connections to the (distinct but related) Second Neighbourhood Conjecture have kept the triangle case prominent.

## 2. State of the art

**Status: open.** No accepted proof or disproof exists in any nontrivial case $k \ge 3$; all confirmed results are strictly partial.

The strongest *general* result is the theorem of Chvátal and Szemerédi (1985): every digraph on $n$ vertices with minimum out-degree $d \ge 1$ has a directed cycle of length at most $n/d + c$ for an absolute constant $c$ (originally $2500$, later improved). This confirms the conjectured linear scaling $k \approx n/d$ but leaves an additive slack the conjecture forbids.

For the triangle case, the predicted threshold is $n/3$. The best **unconditional** result establishes the conclusion under minimum out-degree $\ge \beta n$ with $\beta \approx 0.3465$, obtained by Hladký, Král', and Norin via flag algebras / semidefinite programming, improving Shen Jian's earlier $0.3532\,n$ (2003). The gap between $0.3465$ and the conjectured $0.3333\ldots$ — about $0.013\,n$ — is the central open quantity.

Several relaxations are settled and raise confidence that the conjecture is true: the **fractional** version of the triangle case holds with the exact constant $1/3$ (work associated with D. C. Fisher); the conjecture holds for **vertex-transitive and Cayley digraphs** via additive arguments; and small-order cases are confirmed by computer search. These localize the difficulty to the absence of structure in general digraphs rather than to the threshold itself.

## 3. Principal approaches and barriers

**Direct counting / averaging.** Counting walks, common out-neighbours, and second-out-neighbourhood spread underlies the foundational bounds and the chain of triangle-case improvements down to Shen's $0.3532\,n$. *Barrier:* pure averaging loses an irreducible constant factor because $\vec{C}_n$ is "barely" triangle-free and any argument blind to global cyclic structure stalls above $1/3$.

**Flag algebras (Razborov).** Encode small sub-digraph densities and impose all valid semidefinite relations; an SDP certifies the best constant achievable by local density inequalities. This yields the best known bound $\approx 0.3465\,n$. *Barrier:* such certificates use only bounded-size local information, and there is good reason to believe no finite local certificate reaches exactly $1/3$ — the method appears to plateau strictly above the target.

**Additive combinatorics / Cayley digraphs.** The triangle case has a sharp sum-free-type formulation for Cayley digraphs of abelian groups, where additive rigidity forces the predicted threshold. *Barrier:* general digraphs lack this rigidity, so the line confirms rather than resolves the conjecture.

**Probabilistic / entropy-compression.** Random sampling, dependent random choice, and compression bounds recover the Chvátal–Szemerédi additive-constant statement and clean asymptotics. *Barrier:* these naturally produce error terms, not the zero-error exact threshold.

**Structural / Second-Neighbourhood.** Chudnovsky, Seymour, and Sullivan proved structural and local results (e.g. edges needed to make a triangle-free digraph acyclic) and partial second-neighbourhood cases. *Barrier:* the local-to-global passage is exactly where the difficulty lives, and the Second Neighbourhood Conjecture is itself open and not known to imply Caccetta–Häggkvist.

## 4. Critical assessment

The recurring theme across every method is a *local-certificate ceiling*. Averaging, flag algebras, and SDP certificates all reason from bounded-size configuration densities, and the extremal example $\vec{C}_n$ defeats them precisely because its obstruction is global: only the full cyclic structure rules out a denser triangle-free configuration. The settled relaxations sharpen this diagnosis rather than weakening it — the fractional version reaches $1/3$ exactly, and Cayley digraphs behave as predicted, which strongly suggests the conjecture is *true* and that the residual difficulty is the lack of exploitable structure in arbitrary digraphs.

Two cautions are warranted. First, the widely held belief that the triangle case "contains the full difficulty" is heuristic; the general case $k \ge 4$ additionally requires removing the additive constant from Chvátal–Szemerédi, which is a genuinely separate technical demand. Second, the claim that *no* finite local certificate can reach $1/3$ is a plausibility argument, not a theorem; it is conceivable (if unlikely on current evidence) that a sufficiently large or cleverly structured SDP relaxation closes more of the gap than expected. The honest summary is that progress has been incremental and structural-not-technical, and a decisive global idea has not appeared.

## 5. What a resolution would require / open directions

A proof of the triangle case must close the $\sim 0.013\,n$ gap that every local method leaves, which almost certainly demands a genuinely global or structural argument — or a new algebraic encoding transcending the local-certificate ceiling. The general case $k \ge 4$ would, in addition, require converting the asymptotic Chvátal–Szemerédi bound into an exact threshold by eliminating the additive constant.

Plausible routes, none yet decisive:

1. A **flag-algebra-plus-structure hybrid**, pairing semidefinite certificates with a structural classification of near-extremal triangle-free digraphs.
2. **Additive-combinatorial transfer**, exporting Cayley-digraph rigidity to general out-regular digraphs.
3. **Progress on the Second Neighbourhood Conjecture**, which is closely linked and might illuminate the triangle case (though no implication is known).
4. **Sharper entropy / compression bounds** capable of eliminating additive slack.

## 6. Selected references

References below are reproduced from the dossier and retain their verification flags. Identifiers and several titles are not fully confirmed and require primary-source checking before citation.

1. L. Caccetta, R. Häggkvist, *On minimal digraphs with given girth* (1978) — the originating paper. [high-confidence]
2. V. Chvátal, E. Szemerédi, *Short cycles in directed graphs* (1985) — the additive-constant theorem. [high-confidence]
3. J. Shen, *Directed triangles in digraphs* (2003) — triangle case under $0.3532\,n$. [high-confidence]
4. J. Shen, *On the girth of digraphs* (2003). [needs-verification]
5. A. A. Razborov, *Flag algebras* (2006), DOI 10.2178/jsl/1154698580 — method behind the best bound. [high-confidence] (DOI [needs-verification])
6. M. Chudnovsky, P. Seymour, B. Sullivan, *Cycles in dense digraphs* (2008) — structural/local results. [high-confidence]
7. D. C. Fisher, *A note on the Caccetta–Häggkvist conjecture (fractional version)* (2008). [needs-verification]
8. B. D. Sullivan, *A survey of the Caccetta–Häggkvist conjecture* (2009), arXiv:math/0605646. [needs-verification]
9. J. Hladký, D. Král', S. Norin, *Counting flags in triangle-free digraphs* (2010), arXiv:0908.2791 — flag-algebra bound $\approx 0.3465$. [needs-verification]
10. M. Behzad, G. Chartrand, C. Wall (1970) — regular-digraph girth context. [needs-verification]
11. J. A. Bondy, *Counting subgraphs: a new approach to the Caccetta–Häggkvist conjecture* (2006) — survey. [needs-verification]
12. Y. O. Hamidoune, *On the Caccetta–Häggkvist conjecture and additive structure* (2000). [needs-verification]
13. M. B. Nathanson, *The Caccetta–Häggkvist conjecture and additive number theory* (2007) — survey. [needs-verification]
14. J. Bang-Jensen, G. Gutin, *Digraphs: Theory, Algorithms and Applications* (1998) — textbook treatment. [high-confidence]
15. N. Lichiardopol, *Vertex-disjoint directed cycles and the Caccetta–Häggkvist conjecture* (2013). [needs-verification]

## AI Review Panel

### Claude (Anthropic) — in-house review

The survey is faithful to its source dossier and well-scoped. Its principal strength is honesty about the shape of the difficulty: it correctly identifies the *local-certificate ceiling* as the unifying barrier, distinguishes confirmed results (Chvátal–Szemerédi additive constant; Shen's $0.3532\,n$; the Hladký–Král'–Norin $\approx 0.3465\,n$ bound; settled fractional and Cayley-digraph relaxations) from heuristics, and never overstates partial theorems as a resolution. The technical claims I can cross-check internally are mutually consistent, and the document makes no claim to prove or solve the conjecture.

Three concerns a human reviewer should weigh. (i) The bibliography is only partially verified: by the dossier's own admission, titles, years, and identifiers are dispersed across proceedings and preprints and several are flagged *needs-verification*. The two arXiv identifiers (math/0605646 for Sullivan's survey; 0908.2791 for Hladký–Král'–Norin) and the Razborov DOI should be confirmed against primary sources before any citation; the exact value $\approx 0.3465$ and the year/venue of the Hladký–Král'–Norin bound in particular deserve a direct check. (ii) There is single-source reliance on the dossier itself, so any error or imprecision there propagates here unchanged; I have not independently confirmed, for example, that the flag-algebra bound is exactly $0.3465$ rather than a nearby value, nor the precise improved constant superseding Chvátal–Szemerédi's $2500$. (iii) Two framing claims are heuristic and should be flagged as such, not as fact: that the triangle case "contains the full difficulty," and that *no* finite local certificate can reach $1/3$ — both are community expectations, not theorems.

The single most important thing a human reviewer should verify: the attribution, constant ($\approx 0.3465\,n$), and bibliographic identifier of the best unconditional triangle-case bound (Hladký–Král'–Norin), since the entire "state of the art" rests on it. If that checks out against the primary source, the document is sound for its stated purpose.

**Verdict:** accept-with-revisions.

### GPT (OpenAI) — pending

_Not yet run. To complete the panel, run the prompt in docs/review/REVIEW-TEMPLATE.md through GPT and record the verdict here and in the front matter._

### Gemini (Google) — pending

_Not yet run. See docs/review/REVIEW-TEMPLATE.md._

### Grok (xAI) — pending

_Not yet run. See docs/review/REVIEW-TEMPLATE.md._

## Human verification

AI review is not human peer review. This assessment is offered for academic verification per ../docs/review/ACADEMIC-REVIEW.md; readers should treat all flagged citations as leads to confirm against primary sources, and should independently check the load-bearing constants and attributions before relying on them. Status: human_review pending.

---
*Accredited to **Alexander Donahue** · The Unsolved Mathematics Atlas · CC BY 4.0. Cite per CITATION.cff.*

---
title: "Meta-Analysis: Seymour's Second Neighborhood Conjecture"
slug: seymour-second-neighborhood-conjecture
author: Alexander Donahue
type: ai-assisted-meta-analysis
peer_reviewed: false
problem_status: open
ai_review:
  claude:
    verdict: accept-with-revisions
    date: "2026-06-14"
    version: "claude-opus-4-8"
    summary: "An accurate, appropriately hedged survey of an open digraph conjecture whose core claims (tournament case proved; ~0.657 general bound) are sound, but whose reference table is heavily flagged and needs primary-source verification before publication."
  gpt:
    verdict: pending
  gemini:
    verdict: pending
  grok:
    verdict: pending
human_review: pending
---

# Meta-Analysis: Seymour's Second Neighborhood Conjecture

> **AI-generated meta-analysis — not peer-reviewed.** Curated and accredited by **Alexander Donahue** (human-in-the-loop). A survey/assessment of an open problem; it makes no claim of a new result. Citations carry verification flags and require human source-checking.

## Abstract

Seymour's Second Neighborhood Conjecture asserts that every oriented graph (a digraph with no loops and no digons) contains a vertex $v$ whose second out-neighborhood is at least as large as its first: $|N^{++}(v)| \ge |N^{+}(v)|$. Posed by Paul Seymour around 1990 as the natural generalization of a 1982 tournament question of Nathaniel Dean, the conjecture is celebrated for the gap between its elementary statement and its resistance to proof. The tournament special case is a theorem: Fisher (1996) settled it by a probabilistic "squaring" argument, and Havet–Thomassé (2000) re-proved it via median orders, showing the feed vertex is always a Seymour vertex. For general oriented graphs the strongest unconditional result is a multiplicative relaxation due to Chen, Shen, and Yuster: every oriented graph has a vertex with $|N^{++}(v)| \ge \gamma\,|N^{+}(v)|$ where $\gamma \approx 0.657$ solves $2x^3 + x^2 - 1 = 0$. A patchwork of structured subclasses is also confirmed. The exact inequality remains open, with sparse, balanced, digon-free instances as the recognized hard core. This document surveys the state of the art, the principal methods and their barriers, and what a resolution would require.

## 1. Statement and significance

For a vertex $v$ in a digraph $D$, $N^{+}(v)$ is the set of out-neighbors (vertices at directed distance exactly $1$) and $N^{++}(v)$ is the second out-neighborhood (vertices at directed distance exactly $2$). A **Seymour vertex** satisfies $|N^{++}(v)| \ge |N^{+}(v)|$. The conjecture claims every oriented graph has one. Because $\{v\}$, $N^{+}(v)$, and $N^{++}(v)$ are pairwise disjoint, an equivalent reading is that some vertex reaches at least $2\,|N^{+}(v)|$ vertices within distance two. The restriction to oriented graphs — no digons, no loops, at most one arc per pair — is essential: digons trivially distort second neighborhoods.

The conjecture sits at the intersection of tournament theory and structural digraph theory. Its significance is partly intrinsic (a clean universal inequality about directed expansion) and partly methodological: the median-order / feed-vertex technique developed to prove the tournament case has become a reusable tool for other digraph problems, including work adjacent to Sumner's conjecture.

## 2. State of the art

**Status: open.** The general conjecture has been unresolved since c. 1990. Three solid pillars of progress stand out.

- **Tournament case (proved).** Fisher (1996) proved Dean's conjecture, the tournament version, by a probabilistic weighting argument. Havet and Thomassé (2000) gave a combinatorial proof via median orders and extended it to tournaments missing a perfect matching.
- **Constant-factor bound (proved).** Chen, Shen, and Yuster established the $\gamma \approx 0.657$ multiplicative bound for all oriented graphs — the strongest unconditional general statement and the current ceiling of global methods.
- **Structured subclasses (proved).** Confirmations exist for tournaments minus a star (Fidler–Yuster), rose tournaments (Dean–Latka), comparability-graph orientations (Daamouch), several sink-free and degree-constrained classes (Ghazal), vertex-transitive and Cayley digraphs, and all sufficiently small digraphs by computer search.

A frequently misapplied fact: the summed inequality $\sum_v |N^{++}(v)| \ge \sum_v |N^{+}(v)|$ is **false** in general (directed paths are explicit counterexamples). Any valid proof must therefore locate a single good vertex without averaging — a structural constraint that rules out the most natural counting strategies.

## 3. Principal approaches and barriers

**Median orders (feed-vertex method).** Order a tournament's vertices to maximize forward arcs; the last (feed) vertex has a local majority property forcing it to be a Seymour vertex. This yields the cleanest tournament proof and most near-tournament extensions. *Barrier:* median orders are defined by a global optimization tied to completeness; for sparse oriented graphs the local-majority counting collapses because non-adjacent pairs carry no arc.

**Probabilistic / weighting (Fisher).** Assign weights and analyze $\sum_v(|N^{++}(v)| - |N^{+}(v)|)$ via a distribution on tournaments, forcing a favorable vertex on average. *Barrier:* the telescoping relies on every pair being joined by an arc; in sparse digraphs cancellation fails and missing arcs are not neutral.

**Multiplicative relaxation.** Prove $|N^{++}| \ge \gamma|N^{+}|$ for the best provable $\gamma$. *Best:* Chen–Shen–Yuster, $\gamma \approx 0.657$. *Barrier:* the analysis saturates; no incremental sharpening has pushed $\gamma$ near $1$.

**Structural / forbidden-substructure.** Verify restricted families. *Barrier:* each class is handled ad hoc, with no unifying decomposition; the extremal-looking sparse balanced instances evade every reduction.

**Counting / discharging.** *Barrier:* the false summed inequality blocks any proof that argues by global summation.

The common obstruction is **sparsity with balance**: adversarial oriented graphs distribute out-degree so no vertex is locally forced to expand, while the absence of digons removes the density on which both tournament proofs rely.

## 4. Critical assessment

The dossier's central mathematical claims are, to my knowledge, accurate and standard: the tournament case is genuinely a theorem (two independent proofs), the $\gamma \approx 0.657$ bound is the recognized general ceiling, and the conjecture is uniformly listed as open. The framing of the barrier — that every winning technique exploits tournament completeness and stalls under sparsity — is a fair and widely shared diagnosis, not an overstatement. The explicit caution about the false summed inequality is a genuine and useful contribution, since it is a recurrent trap in flawed attempts.

Two caveats temper confidence. First, the document attributes the $\approx 0.657$ bound to "Chen, Shen, and Yuster" with both a 2003 and a 2006 entry; the constant and the cubic $2x^3 + x^2 - 1 = 0$ are correct, but the exact venue and year should be pinned down before citation. Second, the subclass literature (Ghazal, Daamouch, Fidler–Yuster) is summarized at a level of specificity that exceeds what the flagged references can currently support; readers should not treat the precise scope of each subclass result as settled from this document alone. The assessment is otherwise free of hype and correctly declines to assert a resolution.

## 5. What a resolution would require / open directions

A full proof must exhibit a Seymour vertex in the **adversarial regime**: digon-free, sparse oriented graphs with small, balanced out-degrees where no vertex is locally forced to expand — precisely where Fisher's weighting and the feed-vertex argument provably fail. Plausible routes:

1. **Strengthen the multiplicative bound** from $\gamma \approx 0.657$ toward $\gamma = 1$, via a sharper Chen–Shen–Yuster analysis or a new potential function.
2. **A sparsity-robust median order** — a vertex ordering whose final vertex certifies the inequality without requiring an arc between every pair.
3. **Structural reduction** showing every hard instance reduces to an already-settled class.
4. **Weighted / fractional formulations** interpolating between the tournament and general cases to isolate the obstruction.

None of these is known to succeed; each is a research program, not a near-miss.

## 6. Selected references

1. David C. Fisher (1996), *Squaring a tournament: a proof of Dean's conjecture*, J. Graph Theory. [high-confidence]
2. Frédéric Havet; Stéphan Thomassé (2000), *Median orders of tournaments: a tool for the second neighborhood problem and Sumner's conjecture*. [high-confidence]
3. Guantao Chen; Jian Shen; Raphael Yuster (2003), *Second neighborhood via first neighborhood in digraphs*. [high-confidence]
4. Guantao Chen; Jian Shen; Raphael Yuster (2006), *Second neighborhood via first neighborhood in digraphs* (Annals of Combinatorics version). [needs-verification]
5. Donald Fidler; Raphael Yuster (2007), *The second neighborhood conjecture for digraphs missing a generalized star / minus a star*. [needs-verification]
6. Frédéric Havet; Stéphan Thomassé (2001), *On the second neighborhood conjecture (tournament refinements)*. [needs-verification]
7. Salman Ghazal (2011), *A contribution to Seymour's second neighborhood conjecture*. [needs-verification]
8. Moussa Daamouch (2016), *Seymour's second neighborhood conjecture for orientations of comparability graphs*. [needs-verification]
9. Nathaniel Dean; Brenda J. Latka (1995), *Squaring the tournament — an open problem (problem circulation)*. [needs-verification]
10. Jørgen Bang-Jensen; Gregory Gutin (2007), *Digraphs: Theory, Algorithms and Applications* (2nd ed.) — second neighborhood discussion. [high-confidence]
11. (2010), *Computer verification of the second neighborhood conjecture for small digraphs*. [ai-suggested]
12. (2021), *Recent progress on Seymour's second neighborhood conjecture* (survey). [needs-verification]

## AI Review Panel

### Claude (Anthropic) — in-house review

This is a careful, honest survey that gets the load-bearing mathematics right. The clean separation between what is proved (the tournament case, twice; the $\approx 0.657$ general bound; an enumerated set of subclasses) and what remains open is exactly the structure a reader needs, and the recurring "sparsity with balance" barrier is articulated precisely rather than gestured at. The explicit warning that $\sum_v |N^{++}(v)| \ge \sum_v |N^{+}(v)|$ is false — with directed paths as witnesses — is the kind of concrete, falsifiable detail that distinguishes a real survey from a paraphrase, and it correctly predicts where flawed attempts break.

I have three reservations a human reviewer should weigh. (i) Nearly every entry in the reference table beyond Fisher, Havet–Thomassé, and Bang-Jensen–Gutin carries a `needs-verification` or `ai-suggested` flag; the dossier candidly says titles, years, and venues for the Ghazal/Daamouch/Fidler–Yuster strand and the survey/computational rows could not be confidently reconstructed. These must be checked against primary sources — MathSciNet/zbMATH — before any citation is relied upon, and the precise scope claimed for each subclass result should be confirmed, not inferred from this document. (ii) There is mild single-source risk in the attribution of the $\approx 0.657$ bound, which appears as both a 2003 and a 2006 item; the constant and its defining cubic are standard, but the canonical venue/year should be fixed to avoid a phantom-duplicate citation. (iii) The single most important thing to verify is the existence claim itself — that the general conjecture remains open and that no refereed proof has been accepted; the dossier asserts this responsibly and declines to cite unrefereed manuscripts, which is the correct posture, but it is the claim on which the whole document's framing depends and should be re-confirmed against a current survey.

Subject to those checks, nothing here overstates a result or implies a resolution, and the hedging is appropriately calibrated.

**Verdict:** accept-with-revisions.

### GPT (OpenAI) — pending
_Not yet run. To complete the panel, run the prompt in docs/review/REVIEW-TEMPLATE.md through GPT and record the verdict here and in the front matter._

### Gemini (Google) — pending
_Not yet run. See docs/review/REVIEW-TEMPLATE.md._

### Grok (xAI) — pending
_Not yet run. See docs/review/REVIEW-TEMPLATE.md._

## Human verification

AI review is not a substitute for human peer review. This meta-analysis is offered for academic verification under the process described in ../docs/review/ACADEMIC-REVIEW.md; the references in particular, several of which carry verification flags, require source-checking against primary literature before they are relied upon. Status: human_review pending.

---
*Accredited to **Alexander Donahue** · The Unsolved Mathematics Atlas · CC BY 4.0. Cite per CITATION.cff.*

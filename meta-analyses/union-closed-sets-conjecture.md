---
title: "Meta-Analysis: The Union-Closed Sets Conjecture (Frankl)"
slug: union-closed-sets-conjecture
author: Alexander Donahue
type: ai-assisted-meta-analysis
peer_reviewed: false
problem_status: active-progress
ai_review:
  claude:
    verdict: accept-with-revisions
    date: "2026-06-14"
    version: "claude-opus-4-8"
    summary: "An accurate, appropriately hedged survey of an open problem whose post-2022 entropy results are correctly stated, but whose pre-2022 references carry verification flags that demand primary-source checking."
  gpt:
    verdict: pending
  gemini:
    verdict: pending
  grok:
    verdict: pending
human_review: pending
---

# Meta-Analysis: The Union-Closed Sets Conjecture (Frankl)

> **AI-generated meta-analysis — not peer-reviewed.** Curated and accredited by **Alexander Donahue** (human-in-the-loop). A survey/assessment of an open problem; it makes no claim of a new result. Citations carry verification flags and require human source-checking.

## Abstract

The Union-Closed Sets Conjecture, attributed to Péter Frankl around 1979, asserts that in any finite family of sets closed under union (and containing a non-empty member), some element belongs to at least half of the sets. Despite an elementary statement and overwhelming empirical support — no near-counterexample is known — the conjecture resisted proof for over four decades, accumulating a reputation as a trap in extremal set theory. This meta-analysis surveys the problem's formulations (set, lattice, graph, and weighting forms), its principal attack lines, and the qualitative shift that occurred in November 2022 when Justin Gilmer introduced an entropy argument yielding the first unconditional constant-fraction bound. Within weeks several independent groups sharpened this to $(3-\sqrt5)/2 \approx 0.38$, the natural barrier of the single-step method. We assess what remains: the gap from $0.38$ to the conjectured $1/2$ has resisted the very researchers who closed the earlier gap, and the known barriers across averaging, lattice, graph, and entropy approaches are documented and sharp. The conjecture remains open in full generality. References below carry verification flags and require human source-checking.

## 1. Statement and significance

A finite family $\mathcal{F}$ of sets is *union-closed* if $A \cup B \in \mathcal{F}$ whenever $A,B \in \mathcal{F}$. Writing $m = |\mathcal{F}|$ and $d(x)$ for the number of members containing an element $x$, the conjecture states that $\max_x d(x) \ge m/2$ for any union-closed family with a non-empty member; the empty family and $\{\emptyset\}$ are the only excluded cases. The statement is provably equivalent to a *lattice* form — every finite lattice with $\ge 2$ elements has a join-irreducible element below at most half its elements — an equivalence developed in the order-theory community (Poonen, Reinhold, and others). Dual *intersection-closed* and *graph* (size-$\le 2$ generator) forms also circulate.

Its significance is partly intrinsic and partly methodological. Union-closed families are ubiquitous (closed-set lattices, unions of generating systems), so an abundance theorem would be broadly applicable. More influentially, the problem has become a proving ground for techniques: averaging and compression in the Frankl tradition, structural induction in lattice theory, and — since 2022 — information-theoretic entropy methods, whose success here renewed interest in entropy as a tool for extremal combinatorics.

## 2. State of the art

**Status: open, with active progress.** The decisive recent development is the *entropy bound*. Gilmer's November 2022 preprint (arXiv:2211.09055 [high-confidence]) proved unconditionally that some element appears in at least $c\,m$ sets with $c \approx 0.01$ — the first constant-fraction bound after four decades, replacing the previous best general guarantees of order $m/\log_2 m$. Within roughly two weeks the constant was sharpened independently — by Will Sawin, by Zachary Chase and Shachar Lovett, by Alweiss–Liu–Sawhney–Wu, and by Luke Pebody — to
$$\max_x d(x)\ \ge\ \frac{3-\sqrt5}{2}\,m\ \approx\ 0.3820\,m,$$
the natural optimum of Gilmer's single-step two-set entropy inequality. Sawin subsequently obtained a small improvement strictly beyond $0.38$, demonstrating the barrier is not absolute.

These coexist with robust special-case results, all accepted in the literature: the conjecture holds when $\mathcal{F}$ contains a singleton or doubleton; for all ground sets with $|X| \le 12$ and families with $m \le 50$ (computational, Bošnjak–Marković and predecessors); for "dense" families $m \ge \tfrac23 2^{|X|}$ (Balla–Bollobás–Eccles); for the graph / size-$\le 2$ case (Bruhn–Charbit–Schaudt–Telle); and for modular, lower-semimodular, and relatively complemented lattices (Abe, Reinhold, Czédli–Schmidt).

## 3. Principal approaches and barriers

- **Entropy / information-theoretic (Gilmer).** Sample $A,B \in \mathcal{F}$ uniformly; union-closure forces $A \cup B \in \mathcal{F}$, and a coordinate-wise comparison of binary entropies forces abundance unless the bookkeeping fails. *Barrier:* the single-step two-set inequality cannot exceed $(3-\sqrt5)/2$; its extremal configuration saturates there. Reaching $1/2$ requires genuinely new input (non-uniform sampling, multi-set unions, or discarded correlations).
- **Averaging / abundant-element counting.** The oldest line, seeking a counting identity forcing some $d(x) \ge m/2$. *Barrier:* Sarvate–Renaud exhibited families where the natural "abundant" generator is not abundant, refuting natural strengthenings; any averaging proof must be subtle.
- **Small-ground-set / structural.** Exhaustive verification for $|X|\le 12$, $m \le 50$. *Barrier:* super-exponential search growth; no scaling to large families.
- **Lattice-theoretic.** Settled for modular, semimodular, relatively complemented, and planar lattices. *Barrier:* general lattices have numerous, uncorrelated join-irreducibles; no controlling induction is known.
- **Graph / stable-set (Bruhn et al.).** Settles the size-$\le 2$ slice via stable sets. *Barrier:* general families have arbitrary-size generators, and no reduction to the graph case exists.
- **Weighting (Salzborn/Poonen).** *Barrier:* Poonen showed no fixed weighting certifies all families; weighting must be family-dependent, essentially as hard as the original problem.

## 4. Critical assessment

The dossier's central claims are internally consistent and align with the well-documented public record of the 2022 entropy episode, which unfolded openly on arXiv and research blogs and was independently reproduced by multiple strong groups within days — an unusually transparent and self-verifying sequence. The Gilmer breakthrough is genuine and accepted; the $(3-\sqrt5)/2$ refinement and its status as the one-step ceiling are correctly characterized, including Sawin's marginal improvement beyond it.

Two cautions are warranted. First, the historical bibliography (pre-2022) is the weaker part of the record: several entries carry "needs-verification" or "ai-suggested" flags, with attributions and years (e.g., the precise Renaud/Sarvate, Knill, Reinhold, and Czédli–Schmidt papers) that should be checked against a bibliographic database before citation. Second, the framing of "active progress" should not be misread as imminent resolution: the gap from $0.38$ to $0.5$ has resisted exactly the researchers who closed the prior gap, and the dossier is appropriately sober that no claimed full proof has survived expert scrutiny. The standard failure mode of such claims — reducing at a crucial step to the abundance inequality itself, or invoking a Sarvate–Renaud-refuted strengthening — is correctly noted.

## 5. What a resolution would require / open directions

A complete proof must produce an element of frequency $\ge m/2$ for *every* finite union-closed family, with no restriction on ground-set size, family size, lattice structure, or generator size. The known barriers are sharp and each rules out a class of "easy" routes. The plausible directions are: (i) a *multi-step* or *non-uniform* entropy argument that genuinely breaks the $0.38$ ceiling and reaches $1/2$ — currently the most active hope, tempered by the resistance of the remaining gap; (ii) a structural reduction of the general case to an already-settled class (e.g., extending the graph reduction past size-$2$ generators); or (iii) a wholly new invariant insensitive to the configurations that defeat averaging and single-step entropy. A negative resolution (a counterexample) is regarded as unlikely given decades without a near-miss, but is not excluded.

## 6. Selected references

1. Gilmer, J. (2022). *A constant lower bound for the union-closed sets conjecture.* arXiv:2211.09055. [high-confidence]
2. Sawin, W. (2022). *Improved bound for the union-closed sets conjecture.* arXiv:2211.11504. [needs-verification]
3. Chase, Z., & Lovett, S. (2022). *Approximate union-closed conjecture / sharpening Gilmer to $(3-\sqrt5)/2$.* arXiv:2211.11689. [needs-verification]
4. Alweiss, R., Liu, Y., Sawhney, M., & Wu, K. (2022). *An optimization of the Gilmer bound for the union-closed sets conjecture.* arXiv:2211.11731. [needs-verification]
5. Pebody, L. (2022). *A note on the union-closed sets conjecture (sharp constant).* arXiv:2212.00658. [ai-suggested]
6. Bruhn, H., Charbit, P., Schaudt, O., & Telle, J. A. (2013). *The graph formulation of the union-closed sets conjecture.* arXiv:1212.4175. [needs-verification]
7. Bruhn, H., & Schaudt, O. (2015). *The journey of the union-closed sets conjecture.* arXiv:1309.3297. [needs-verification]
8. Poonen, B. (1989). *Union-closed families.* [needs-verification]
9. Renaud, J.-C., & Sarvate, D. G. (1989). *Improved bounds for the union-closed sets conjecture.* [needs-verification]
10. Sarvate, D. G., & Renaud, J.-C. (1990). *Counterexample to a stronger statement / small families.* [needs-verification]
11. Reimer, D. (1994). *Average set size of union-closed families.* [needs-verification]
12. Reinhold, J. (1999). *Union-closed families of sets (lattice cases).* [needs-verification]
13. Abe, T., & Nakano, B. (2008). *Frankl's conjecture for modular / lower-semimodular lattices.* [needs-verification]
14. Czédli, G., & Schmidt, E. T. (2009). *Frankl's conjecture for large semimodular and planar semimodular lattices.* [needs-verification]
15. Balla, I., Bollobás, B., & Eccles, T. (2013). *Large families verifying the union-closed sets conjecture ($m \ge \tfrac23 2^n$).* [needs-verification]

## AI Review Panel

### Claude (Anthropic) — in-house review

The survey is accurate where it matters most. The 2022 entropy story — Gilmer's $\approx 0.01$ bound, the rapid independent sharpening to $(3-\sqrt5)/2$, the identification of that constant as the single-step ceiling, and Sawin's marginal push beyond it — is correctly stated and matches the public record of an episode that was, unusually, verified in the open by several strong groups within days. The treatment of barriers is the document's real strength: each approach (averaging, lattice, graph, weighting, entropy) is paired with a specific, documented obstruction rather than vague hand-waving, and the Sarvate–Renaud caution against natural strengthenings is correctly deployed. The hedging is appropriate throughout; nowhere does the document claim a resolution.

My skeptical flags. (i) Every reference here carries a verification flag, and most of the pre-2022 entries are "needs-verification" or "ai-suggested." Only Gilmer (arXiv:2211.09055) is high-confidence. The arXiv identifiers on rows 2–5 are plausibly the correct late-2022 notes, but near-simultaneous papers shared similar titles and the exact id/author pairing must be confirmed against arXiv before citation. The older works (Poonen, Renaud/Sarvate, Reimer, Reinhold, Abe, Czédli–Schmidt) are real in spirit but their precise titles, years, and venues should be checked against MathSciNet or zbMATH. (ii) Several attributions rest on single-source recollection of an oral-tradition problem (the 1979 origin, the canonical-statement provenance); these are plausible but not independently corroborated here. (iii) Single most important thing for a human reviewer to verify: that the $(3-\sqrt5)/2$ constant is correctly attributed to the four independent groups named, and that Sawin's improvement "strictly beyond $0.38$" is real and not a conflation — this is the load-bearing claim distinguishing "barrier" from "absolute barrier," and it should be checked directly against the arXiv abstracts.

None of these flags undermine the survey's conclusions; they bear on citation integrity rather than mathematical substance. Revisions should focus on source-checking the bibliography, not on the assessment itself.

**Verdict:** accept-with-revisions.

### GPT (OpenAI) — pending

_Not yet run. To complete the panel, run the prompt in docs/review/REVIEW-TEMPLATE.md through GPT and record the verdict here and in the front matter._

### Gemini (Google) — pending

_Not yet run. See docs/review/REVIEW-TEMPLATE.md._

### Grok (xAI) — pending

_Not yet run. See docs/review/REVIEW-TEMPLATE.md._

## Human verification

AI review is not human peer review. This meta-analysis is offered for academic verification per ../docs/review/ACADEMIC-REVIEW.md, and its citations — most of which carry "needs-verification" or "ai-suggested" flags — require primary-source checking before any scholarly reliance. Status: human_review pending.

---
*Accredited to **Alexander Donahue** · The Unsolved Mathematics Atlas · CC BY 4.0. Cite per CITATION.cff.*

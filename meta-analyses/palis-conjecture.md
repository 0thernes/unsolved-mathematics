---
title: "Meta-Analysis: The Palis Conjecture (Finitude / Density of Attractors)"
slug: palis-conjecture
author: Alexander Donahue
type: ai-assisted-meta-analysis
peer_reviewed: false
problem_status: open
ai_review:
  claude:
    verdict: accept-with-revisions
    date: "2026-06-14"
    version: "claude-opus-4-8"
    summary: "An accurate, appropriately hedged survey of an open program whose one-dimensional case is genuinely settled, but whose references carry verification flags and whose high-regularity caveats deserve more weight."
  gpt:
    verdict: pending
  gemini:
    verdict: pending
  grok:
    verdict: pending
human_review: pending
---

# Meta-Analysis: The Palis Conjecture (Finitude / Density of Attractors)

> **AI-generated meta-analysis — not peer-reviewed.** Curated and accredited by **Alexander Donahue** (human-in-the-loop). A survey/assessment of an open problem; it makes no claim of a new result. Citations carry verification flags and require human source-checking.

## Abstract

The Palis Conjecture proposes that the long-term behavior of a *typical* dynamical system is tame: a dense set of diffeomorphisms or flows on a compact manifold, and Lebesgue-almost-every system in any generic finite-parameter family through them, should possess finitely many attractors whose basins cover almost all of phase space and which carry statistically stable physical (SRB) measures. Articulated by Jacob Palis in the mid-1990s and given canonical form in his 2000 *Astérisque* essay, the conjecture reframes the post-hyperbolic landscape — wild on a topologically generic set after Newhouse — by retreating from topological genericity to measure-theoretic typicality. This meta-analysis surveys the statement, the state of the art, the principal attacks (one-dimensional density of hyperbolicity, $C^1$-generic dichotomies, dominated splittings, SRB theory), and the obstructions (Newhouse phenomena, Berger's robust universality) that bound any proof. The conjecture is fully confirmed in dimension one and supported by fragmentary higher-dimensional results, but remains open in every dimension $\geq 2$. It makes no claim of resolution here.

## 1. Statement and significance

Let $f$ be a $C^r$ diffeomorphism (or flow) of a compact manifold. The conjecture asserts that, for a *dense* set of such systems and for Lebesgue-almost-every system in any generic parametrized family through them, $f$ has (i) **finitely many attractors**; (ii) the union of their **basins has full Lebesgue measure**; and (iii) each attractor supports a **physical (SRB) measure that is statistically stable** under perturbation. A structural sub-conjecture — **density of hyperbolicity or homoclinic bifurcations** — holds that every system is approximable either by a hyperbolic (Axiom A) one or by one exhibiting a homoclinic tangency or heterodimensional cycle, making these the universal mechanisms of dynamical complexity.

The significance is foundational. Smale's 1960s hope that hyperbolicity would be dense collapsed under his own horseshoe and Newhouse's infinitely-many-sinks phenomenon. Palis's response reorients the discipline's central goal from "classify all dynamics" to "the generic *statistical* behavior is finitely describable and robust" — a target physicists and applied scientists actually care about, since SRB measures govern observable time-averages.

## 2. State of the art

**Dimension one is settled in the relevant sense.** Kozlovski, Shen, and van Strien (2007) proved density of hyperbolicity for $C^k$ maps of the interval and circle. Combined with Lyubich's "regular or stochastic" dichotomy (2003) and the Avila–Lyubich–de Melo analytic results, almost every quadratic map is either regular (a hyperbolic attracting cycle) or stochastic (an absolutely continuous SRB measure). The Palis picture holds completely in this regime.

**Higher dimension is fragmentary.** Bonatti–Viana and Alves–Bonatti–Viana construct SRB measures and prove finitude for partially hyperbolic systems with mostly-contracting or mostly-expanding center. Benedicks–Carleson and Mora–Viana secured positive-Lebesgue-measure sets of Hénon parameters with SRB attractors; Tucker (2002) rigorously established the Lorenz attractor with its physical measure. In the $C^1$ topology, Pujals–Sambarino and Crovisier–Pujals proved essential hyperbolicity away from homoclinic bifurcations, confirming the structural sub-conjecture in significant generality. No general finitude theorem exists for a typical $C^2$ surface diffeomorphism.

## 3. Principal approaches and barriers

- **One-dimensional density of hyperbolicity.** The strongest unconditional confirmation. Its tools — Schwarzian derivative, complex bounds, quasiconformal rigidity — have no higher-dimensional analogue; renormalization rigidity fails once stable and unstable directions coexist.
- **$C^1$-generic dichotomies (Mañé–Pujals–Sambarino–Crovisier).** The closing/connecting-lemma toolkit (Pugh, Hayashi, Mañé) gives strong perturbation control, but only in $C^1$, where generic systems may possess *no* SRB measure. The metric and statistical clauses are out of reach, and the methods notoriously do not upgrade to $C^2$.
- **Dominated splittings and partial hyperbolicity (Bonatti–Díaz–Viana).** Weaker invariant structures survive perturbation and admit SRB constructions, but only under structural hypotheses; the neutral-center and general non-uniformly hyperbolic cases have no finitude theorem.
- **SRB / physical-measure theory (Sinai–Ruelle–Bowen, Young, Benedicks–Carleson).** Delivers measure-theoretic confirmations family-by-family via delicate parameter exclusion, which does not globalize.
- **Negative results.** Newhouse (1974) forces the measure-zero qualifier; Bonatti–Díaz produced robustly heterodimensional systems; Berger (2016) proved robust universality / persistent Newhouse phenomena in $C^r$, $r \geq 2$, placing the high-regularity finitude clause under genuine tension.

## 4. Critical assessment

The conjecture's honest standing is a tale of two regimes. In dimension one it is not merely supported but *proved*, and the dossier is right to treat this as a complete verification rather than as suggestive evidence. The danger in popular framing is to read this success as near-momentum toward the general case; it is not. The one-dimensional proof is powered by renormalization rigidity that is structurally absent in dimension $\geq 2$, so the settled case offers technique-level encouragement only at the level of *what is true*, not *how to prove it*.

The most consequential tension is Berger's robust universality. The dossier handles this carefully: Berger's open sets of $C^r$ systems with persistent infinitely-many-sinks behavior do not contradict Palis's full-measure formulation (which concerns Lebesgue-almost-every parameter in generic families, not topological density), but they raise a live, unresolved question about whether even the *metric* finitude clause survives in high regularity. A reader should not mistake "not a counterexample" for "no threat" — the scope of the conjecture, and possibly the precise hypotheses, may need revision. This is the single most important interpretive nuance in the entire dossier, and it is correctly flagged as unresolved tension rather than resolution.

## 5. What a resolution would require / open directions

A full proof must (i) construct SRB/physical measures for the generic non-uniformly hyperbolic system — for which no general technique exists; (ii) prove finitude of attractors off a Lebesgue-null parameter set, reconciled with Newhouse/Berger abundance; and (iii) establish statistical stability under perturbation. Plausible routes include extending the $C^1$-generic dichotomy framework with new tools to control physical measures; finding a higher-dimensional substitute for one-dimensional renormalization rigidity; or proving a sharp finitude theorem inside the dominated-splitting category and showing such structures are generic. Most experts regard the conjecture as decades away, with high-regularity universality a serious caveat on its scope.

## 6. Selected references

1. S. Smale, *Differentiable dynamical systems* (1967). [high-confidence]
2. J. Palis, *An Omega-stability theorem* (1970). [high-confidence]
3. S. Newhouse, *Diffeomorphisms with infinitely many sinks* (1974). [high-confidence]
4. R. Mañé, *A proof of the $C^1$ stability conjecture* (1988). [high-confidence]
5. M. Benedicks, L. Carleson, *The dynamics of the Hénon map* (1991). [high-confidence]
6. J. Palis, F. Takens, *Hyperbolicity and Sensitive Chaotic Dynamics at Homoclinic Bifurcations* (1993). [high-confidence]
7. L. Mora, M. Viana, *Abundance of strange attractors* (1993). [high-confidence]
8. J. Palis, *A global view of dynamics and a conjecture on the denseness of finitude of attractors* (2000). [high-confidence]
9. J. F. Alves, C. Bonatti, M. Viana, *SRB measures for partially hyperbolic systems whose central direction is mostly expanding* (2000). [high-confidence]
10. S. Hayashi, *Connecting invariant manifolds and the solution of the $C^1$ stability and Omega-stability conjectures for flows* (2000). [high-confidence]
11. W. Tucker, *A computer-assisted proof of the Lorenz attractor* (2002). [high-confidence]
12. M. Lyubich, *Almost every real quadratic map is either regular or stochastic* (2003). [high-confidence]
13. C. Bonatti, L. J. Díaz, M. Viana, *Dynamics Beyond Uniform Hyperbolicity* (2005). [high-confidence]
14. O. Kozlovski, W. Shen, S. van Strien, *Density of hyperbolicity in spaces of $C^k$ maps of the interval and circle* (2007). [high-confidence]
15. S. Crovisier, E. Pujals, *Essential hyperbolicity and homoclinic bifurcations: a dichotomy* (2012). [needs-verification; arXiv:1011.3836 tentative]
16. P. Berger, *Generic family with robustly infinitely many sinks* (2016). [needs-verification]

## AI Review Panel

### Claude (Anthropic) — in-house review

This is a careful, expert-level survey that gets the central distinction right: the conjecture is a *program*, not a single equation, and its honest status is "settled in dimension one, fragmentary and contested above." The strengths are real. The dossier correctly identifies renormalization rigidity as the load-bearing tool that makes dimension one work and dimension $\geq 2$ hard, and it resists the common temptation to present the one-dimensional success as momentum toward the general case. Its treatment of Berger's robust universality — as a tension that sharpens the target rather than a counterexample to Palis's full-measure formulation — is precisely the nuance a careless survey would botch.

Three cautions. First, the references: a substantial minority of the underlying paper list carries explicit `needs-verification` flags (rows 16, 21–25 in the source, including the Crovisier–Pujals arXiv id and the Berger title/venue), and several pre-2000 works have no identifier at all. A human must source-check titles, years, and venues before any of this is cited downstream; I have preserved the flags in the reference list above and a reviewer should not treat the bracketed `[high-confidence]` items as independently verified by me. Second, single-source reliance: the framing of Berger's results as compatible-but-threatening rests on a reading of one body of work whose precise statements the dossier itself flags as unverified — the exact regularity classes and whether the examples touch full-measure-in-families claims should be confirmed against the primary papers, not the secondary characterization. Third, possible overstatement: phrases like "the Palis picture holds completely" in dimension one are defensible but depend on stitching together several deep theorems (Kozlovski–Shen–van Strien, Lyubich, Avila–Lyubich–de Melo) whose combined reach a referee should verify covers all three clauses (finitude, metric covering, statistical stability), not just density of hyperbolicity.

The single most important thing a human reviewer should verify: whether Berger's high-regularity universality results genuinely leave Palis's *measure-theoretic, generic-family* statement intact, or whether they constrain its scope more than the dossier concedes — this is the one place where the difference between "open" and "needs reformulation" actually lives.

**Verdict:** accept-with-revisions.

### GPT (OpenAI) — pending
_Not yet run. To complete the panel, run the prompt in docs/review/REVIEW-TEMPLATE.md through GPT and record the verdict here and in the front matter._

### Gemini (Google) — pending
_Not yet run. See docs/review/REVIEW-TEMPLATE.md._

### Grok (xAI) — pending
_Not yet run. See docs/review/REVIEW-TEMPLATE.md._

## Human verification

AI review is not human peer review. This assessment is offered for academic verification per ../docs/review/ACADEMIC-REVIEW.md, and every citation carrying a verification flag requires confirmation against primary sources before use. Status: human_review pending.

---
*Accredited to **Alexander Donahue** · The Unsolved Mathematics Atlas · CC BY 4.0. Cite per CITATION.cff.*

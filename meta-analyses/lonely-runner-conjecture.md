---
title: "Meta-Analysis: The Lonely Runner Conjecture"
slug: lonely-runner-conjecture
author: Alexander Donahue
type: ai-assisted-meta-analysis
peer_reviewed: false
problem_status: active-progress
ai_review:
  claude:
    verdict: accept-with-revisions
    date: "2026-06-14"
    version: "claude-opus-4-8"
    summary: "A faithful and appropriately cautious survey of a genuinely open problem; sound on the proven cases and Tao's reduction, but its citation table is partly reconstructed from memory and must be source-checked before use."
  gpt:
    verdict: pending
  gemini:
    verdict: pending
  grok:
    verdict: pending
human_review: pending
---

# Meta-Analysis: The Lonely Runner Conjecture

> **AI-generated meta-analysis — not peer-reviewed.** Curated and accredited by **Alexander Donahue** (human-in-the-loop). A survey/assessment of an open problem; it makes no claim of a new result. Citations carry verification flags and require human source-checking.

## Abstract

The Lonely Runner Conjecture asserts that for $k$ runners starting together on a unit circular track at distinct constant speeds, each runner is at some moment at distance at least $\tfrac{1}{k}$ along the track from all others. After the standard reduction — fix one runner at speed $0$ and take the remaining $n=k-1$ speeds to be distinct positive integers $v_1,\dots,v_n$ — the claim is that there exists a real $t$ with $\|t v_i\| \ge \tfrac{1}{n+1}$ for every $i$, where $\|\cdot\|$ denotes distance to the nearest integer. The constant $\tfrac{1}{n+1}$ is sharp, realized by $v_i = i$. Posed independently by Wills (1967) in Diophantine approximation and by Cusick (1973) as a view-obstruction problem, and named by Goddyn in the 1990s, the conjecture is proven for $n \le 5$ moving runners and, by Tao (2017), reduced to a finite computation for each fixed $n$. It remains open in general. This meta-analysis surveys the proven ladder, the principal attack families, the structural barriers at the sharp constant, and what a uniform resolution would require. It makes no claim of a new result.

## 1. Statement and significance

Fix one runner as a stationary reference; the others run at distinct nonzero speeds, which by scaling and clearing denominators may be taken to be distinct positive integers $v_1,\dots,v_n$ with $\gcd = 1$. Writing $\|x\|$ for the distance from $x$ to the nearest integer, the conjecture states that

$$ \exists\, t \in \mathbb{R} \quad \text{such that} \quad \|t v_i\| \ge \frac{1}{n+1} \quad \text{for all } i. $$

Equivalently, $\sup_t \min_i \|t v_i\| \ge \tfrac{1}{n+1}$. The bound is tight: the arithmetic progression $1,2,\dots,n$ forces equality, so no larger universal constant exists.

The problem's significance lies in its density of equivalent guises. It is simultaneously a sharp inhomogeneous Diophantine approximation question (Wills), a covering/obstruction property of axis-aligned cubes pierced by rays (Cusick's view-obstruction problem), a statement about the circular and regular chromatic numbers of distance graphs (Goddyn–Zhu), a question about nowhere-zero flows and matroid invariants, and a problem on extremal trigonometric polynomials. A single elementary-looking inequality thus sits at the crossroads of the geometry of numbers, additive combinatorics, graph colouring, and harmonic analysis — which is much of why it has resisted resolution while attracting tools from all four.

## 2. State of the art

**Status: open, with active progress.** The verified frontier advances roughly one runner per decade, each case demanding markedly more work than the last:

- $n \le 3$: Wills (1967–1968), by direct Diophantine estimates.
- $n = 4$ (five runners total): Cusick–Pomerance (1984); reproved within a broader framework by Bienia–Goddyn–Gvozdjak–Sebő–Tarsi (1998).
- $n = 5$ (six runners total): Barajas–Serra (2008), a tour de force of the view-obstruction method; an elementary reproof by Renault (2011).

The most consequential general result is Tao's (2017, arXiv:1701.02048): a **finiteness reduction** showing it suffices to check speed sets whose entries are bounded by an explicit (super-polynomial) function of $n$, so that for each fixed $n$ the conjecture is decidable by finite computation. Tao also proved the conjecture with the constant relaxed from $\tfrac{1}{n+1}$ to a bound of the form $\tfrac{1}{2n} + \tfrac{c\log n}{n^2}$ — an explicit but sub-sharp improvement over the trivial averaging constant $\tfrac{1}{2n}$. The dossier notes that $n = 6$ remains the live frontier: no single paper has closed it the way Barajas–Serra closed $n = 5$. There are no significant conditional results of "follows from GRH" type; the difficulty is combinatorial-geometric rather than dependent on deep arithmetic hypotheses.

## 3. Principal approaches and barriers

**View-obstruction / geometry of numbers.** The dominant line, after Cusick: one asks whether every ray into the open orthant pierces a cube of side $1/(n+1)$ centered at half-integer lattice points, partitioning the torus by the residues $t v_i \bmod 1$ and showing the forbidden region cannot cover everything. This delivered the strongest fully proven cases ($n=4$, $n=5$). Barrier: the case analysis is super-exponential in $n$, with no uniform-in-$n$ obstruction known.

**Gap-of-divisors / combinatorial number theory.** Exploiting divisibility structure to locate a good $t$ when the speed set is suitably spread out (Renault and others). Barrier: it fails precisely on near-arithmetic-progression speed sets — the hard instances.

**Harmonic analysis (Tao's reduction).** Bounding the loneliness indicator below by a trigonometric polynomial whose moments can be estimated; this yields the finiteness reduction and the improved constant. Barrier: Fourier-moment methods inherently lose the sharp constant because the extremal polynomial is delicate; the finite check is astronomically large for $n \ge 7$.

**Polyhedral / Ehrhart / computational geometry.** Recasting feasibility in terms of a "lonely-runner polytope" and lattice points (Beck–Hoşten–Schymura circle). Barrier: reframes rather than resolves; general feasibility is as hard as the conjecture.

**Graph colouring.** Via the Goddyn–Zhu dictionary, equivalent to statements on circular/regular chromatic numbers of distance graphs. Barrier: inherits the same hardness; no new $n$ broken by colouring alone.

**Probabilistic / averaging.** A random $t$ gives the trivial $\tfrac{1}{2n}$. Intrinsic barrier: the extremizer $1,2,\dots,n$ has loneliness region of measure exactly meeting the bound, so any purely measure-theoretic argument is provably incapable of reaching the sharp constant — an analogue of a "parity barrier."

## 4. Critical assessment

The dossier's central honest claim — that the conjecture is proven for small $n$ and reduced to finite computation, but open in general — is well supported and consistent with the documented literature. The structural diagnosis is the strongest part of the analysis: two independent obstructions are identified with precision. First, averaging and second-moment methods see only the order $\tfrac{1}{2n}$ and provably never the sharp threshold, because the extremizer's loneliness region has measure meeting the bound exactly. Second, the hard instances are the near-arithmetic-progression speed sets, on which divisibility shortcuts fail. That the same configuration $1,2,\dots,n$ is the obstruction to both the analytic and the combinatorial approaches is a genuinely illuminating observation, and it explains why so many announced general proofs collapse: they silently assume a covering structure absent near the extremizer, or lose the constant exactly there.

Two cautions. The "one runner per decade" framing is a useful narrative but should not be read as a law; progress at the frontier is now computational and may be discontinuous. And the precise total-runner-count conventions (whether $n=5$ corresponds to six or seven total runners) drift between sources, including within this dossier — a human editor should standardize the indexing.

## 5. What a resolution would require / open directions

A full proof must be **uniform in $n$ and attain the exact constant $\tfrac{1}{n+1}$**, simultaneously defeating both barriers. Plausibly this requires a new invariant that is tight at the extremizer $1,2,\dots,n$ yet stable across all speed sets — something neither Fourier moments nor view-obstruction case analysis currently provide. Concrete directions flagged in the dossier:

- **Mechanizing Tao's finite check** for $n = 6, 7$ via the lonely-runner polytope and modern integer-feasibility / Ehrhart computation — the most likely source of the next confirmed cases.
- **A sharp harmonic-analytic identity** recovering $\tfrac{1}{n+1}$ exactly, via extremal trigonometric polynomials tuned to the arithmetic-progression extremizer.
- **A colouring-theoretic breakthrough** on circular chromatic numbers of distance graphs (Zhu's dictionary) that bypasses explicit case analysis.

The consensus the dossier reports is that incremental case-by-case progress will continue while a uniform proof remains out of reach. The shifted, rational, and dynamical variants remain active both for their own sake and as testing grounds — and are also where corrections to over-optimistic sharp constants have appeared, a useful caution against premature claims in the main problem.

## 6. Selected references

1. Jörg M. Wills (1967), *Zwei Sätze über inhomogene diophantische Approximation von Irrationalzahlen* — foundational; poses the conjecture. [high-confidence]
2. T. W. Cusick (1973), *View-obstruction problems* — independent geometric formulation. [high-confidence]
3. T. W. Cusick (1974), *View-obstruction problems in n-dimensional geometry*. [needs-verification]
4. T. W. Cusick & Carl Pomerance (1984), *View-obstruction problems and the lonely runner* ($n=4$) — breakthrough. [high-confidence]
5. W. Bienia, L. Goddyn, P. Gvozdjak, A. Sebő, M. Tarsi (1998), *Flows, view obstructions, and the lonely runner*, JCTB, doi:10.1006/jctb.1997.1770 — unifying synthesis. [high-confidence]
6. Y. G. Chen & T. W. Cusick (2001), *The view-obstruction problem for n-dimensional cubes*. [needs-verification]
7. Xuding Zhu (2001), *Circular chromatic number and distance graphs / the lonely runner*. [needs-verification]
8. J. Barajas & O. Serra (2008), *Regular chromatic number and the lonely runner problem* ($n=5$) — breakthrough. [high-confidence]
9. J. Barajas & O. Serra (2009), *The lonely runner with seven runners* (structured/partial). [needs-verification]
10. M. Renault (2011), *View-obstruction and the lonely runner: an elementary proof for six runners*. [needs-verification]
11. G. Perarnau & O. Serra (2012), *Correlation among runners and some results on the lonely runner conjecture*. [needs-verification]
12. Terence Tao (2017), *Some remarks on the lonely runner conjecture*, arXiv:1701.02048 — finiteness reduction and improved constant. [high-confidence]
13. M. Beck, S. Hoşten, M. Schymura, et al. (c. 2022), *Lonely runner polytopes / Ehrhart and computational approaches*. [needs-verification]
14. Survey/retrospective (c. 2021), *The lonely runner conjecture turns 60*. [needs-verification]

## AI Review Panel

### Claude (Anthropic) — in-house review

This is a careful, honestly hedged survey that gets the load-bearing facts right: the standard reduction and sharp constant $\tfrac{1}{n+1}$ with extremizer $1,2,\dots,n$; the proven ladder through $n=5$; and Tao's two contributions (the finiteness reduction and the sub-sharp improved constant). The strongest intellectual content is the unified diagnosis of why the problem is hard — that the same extremal speed set simultaneously defeats averaging arguments (measure meets the bound exactly) and divisibility/covering arguments (near-arithmetic-progression instances) — which is both correct in spirit and genuinely explanatory. The document scrupulously avoids any claim of resolution.

I have three skeptical flags. (i) The reference list is, by the dossier's own admission, partly reconstructed from memory: only two identifiers are vouched for — the JCTB DOI 10.1006/jctb.1997.1770 (1998) and arXiv:1701.02048 (Tao, 2017). Titles, years, and author lists for the Chen–Cusick, Zhu, Barajas–Serra 2009, Renault 2011, Perarnau–Serra, Beck–Hoşten–Schymura, and survey entries carry verification flags and must be checked against MathSciNet/zbMATH/arXiv before any of them is cited as fact. (ii) There is some single-source reliance and convention drift: the total-runner-count indexing (six vs. seven runners for $n=5$) is internally inconsistent across the dossier, and the precise form of Tao's improved constant ($\tfrac{1}{2n} + \tfrac{c\log n}{n^2}$-type) is stated loosely and should be quoted from the paper rather than paraphrased. (iii) The single most important thing a human reviewer should verify is the exact statement and current status of the proven frontier — specifically whether the published record stands at $n=5$ (six runners) as claimed, and what, if anything, is rigorously established for $n=6$ beyond Tao's reduction; this is precisely the point most prone to overstatement.

None of these undermine the survey's core, which is appropriately modest and does not assert a resolution. They are revisions to citation hygiene and precision, not corrections of substance.

**Verdict:** accept-with-revisions.

### GPT (OpenAI) — pending

_Not yet run. To complete the panel, run the prompt in docs/review/REVIEW-TEMPLATE.md through GPT and record the verdict here and in the front matter._

### Gemini (Google) — pending

_Not yet run. See docs/review/REVIEW-TEMPLATE.md._

### Grok (xAI) — pending

_Not yet run. See docs/review/REVIEW-TEMPLATE.md._

## Human verification

AI review is not human peer review. This meta-analysis is offered for academic verification per ../docs/review/ACADEMIC-REVIEW.md; the AI panel above flags points of uncertainty but does not substitute for source-checking by a qualified mathematician. Reference identifiers, proven-case conventions, and the exact form of cited constants in particular require human confirmation against primary sources. Status: human_review pending.

---
*Accredited to **Alexander Donahue** · The Unsolved Mathematics Atlas · CC BY 4.0. Cite per CITATION.cff.*

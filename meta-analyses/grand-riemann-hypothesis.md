---
title: "Meta-Analysis: The Grand Riemann Hypothesis"
slug: grand-riemann-hypothesis
author: Alexander Donahue
type: ai-assisted-meta-analysis
peer_reviewed: false
problem_status: open
ai_review:
  claude:
    verdict: accept-with-revisions
    date: "2026-06-14"
    version: "claude-opus-4-8"
    summary: "A faithful, well-sourced survey of GRH that correctly frames it as open and uniform across the Selberg/automorphic class, but leans on several pre-DOI and needs-verification citations that require primary-source checking."
  gpt:
    verdict: pending
  gemini:
    verdict: pending
  grok:
    verdict: pending
human_review: pending
---

# Meta-Analysis: The Grand Riemann Hypothesis

> **AI-generated meta-analysis — not peer-reviewed.** Curated and accredited by **Alexander Donahue** (human-in-the-loop). A survey/assessment of an open problem; it makes no claim of a new result. Citations carry verification flags and require human source-checking.

## Abstract

The Grand Riemann Hypothesis (GRH) asserts that every non-trivial zero of every automorphic $L$-function — equivalently, of every element of Selberg's axiomatic class $\mathcal{S}$ — lies on the critical line $\mathrm{Re}(s)=\tfrac12$. It is the maximal generalization of Riemann's 1859 conjecture, containing both the classical Riemann Hypothesis (RH, the degree-one level-one case) and the Generalized RH for Dirichlet $L$-functions (Piltz, 1884). This meta-analysis surveys the problem's lineage, its present status as **open**, the principal lines of attack, and the structural barriers that have kept it open. The recurring diagnosis is that GRH is a *uniform* statement over an entire class, and that the only decisive proof technique known for an RH-type assertion — Deligne's $\ell$-adic cohomology in the function-field setting — has no counterpart over $\mathrm{Spec}\,\mathbb{Z}$. Equivalent positivity and spectral reformulations (Weil, Li, Connes) relocate the difficulty without resolving it. We assess what a genuine resolution would require and flag the verification status of the cited literature. No new result is claimed.

## 1. Statement and significance

GRH ("Grand," not merely "Generalized") asserts RH simultaneously for the whole family of arithmetic $L$-functions: in automorphic language, for every $L(s,\pi)$ attached to a cuspidal automorphic representation $\pi$ of $\mathrm{GL}_n(\mathbb{A}_{\mathbb Q})$ (and over any number field); in axiomatic language, for every $F$ in the Selberg class $\mathcal{S}$ (Dirichlet series satisfying Euler product, analytic continuation, a Riemann-type functional equation, and a Ramanujan-type growth bound). The two formulations are conjecturally equivalent because $\mathcal{S}$ is expected to coincide with the automorphic class.

The stakes are exceptional. Under GRH one obtains square-root error terms for primes in arithmetic progressions, effective Chebotarev with strong bounds, deterministic polynomial-time primality and small bounds on least quadratic non-residues and primitive roots, subconvexity-flavored estimates, and precise low-lying-zero statistics. Large parts of analytic number theory are written "under GRH"; a proof would convert this conditional edifice into theorems.

## 2. State of the art

The problem is **open** for every degree-$\ge 1$ element, and is unknown even for a single $\mathrm{GL}_2$ cusp form's $L$-function. What is established is substantial but never closes the line:

- **Zero localization and proportions.** Zeros of every standard Selberg-class element lie in the critical strip, with a classical zero-free region near $\mathrm{Re}(s)=1$. For $\zeta$, roughly $41.7\%$ of non-trivial zeros lie exactly on the line (Bui–Conrey–Young 2011 and successors), tracing the lineage Hardy (1914) $\to$ Selberg (1942) $\to$ Levinson (1974, $>34\%$) $\to$ Conrey (1989, $>40\%$). Analogous positive proportions hold for Dirichlet and some $\mathrm{GL}_2$ $L$-functions.
- **Averages and density.** Bombieri–Vinogradov (1965) gives "GRH on average" over moduli, sufficient for many applications; density theorems bound the number of possible off-line zeros.
- **Function-field analogue is a theorem.** Weil (1948) for curves and Deligne (1974) for general varieties prove the RH analogue over $\mathbb{F}_q$ — the one setting where a Grand-RH-type statement holds.
- **Marginality.** Rodgers–Tao (2020) proved the de Bruijn–Newman constant satisfies $\Lambda\ge 0$; since RH $\iff \Lambda\le 0$, RH is "barely" true if true.
- **Class structure.** Kaczorowski–Perelli showed there are no elements of degree $0<d<1$ or $1<d<2$ and classified degrees $0$ and $1$, confirming the automorphic picture without locating zeros.

## 3. Principal approaches and barriers

- **Critical-line / mollifier method.** Computes mollified moments and applies Levinson's method to bound the on-line proportion from below. *Barrier:* mollifier length is capped by available moment estimates, so the method cannot in principle reach $100\%$, and it says nothing about a single high off-line zero.
- **Pair correlation and random matrix theory.** Montgomery (1973) and Katz–Sarnak (1999) match zero statistics to eigenvalues of random unitary/orthogonal/symplectic ensembles, making GRH statistically expected. *Barrier:* RMT describes average behavior and forbids no individual off-line zero; pair correlation itself is only partially proven.
- **Function-field transport / $\mathbb{F}_1$.** Deligne's $\ell$-adic cohomology realizes zeros as Frobenius eigenvalues. *Barrier:* $\mathrm{Spec}\,\mathbb{Z}$ is not a variety over a field, and no cohomology theory (a working "field with one element") is known to make $\zeta$ geometric.
- **Hilbert–Pólya / spectral.** Seek a self-adjoint operator whose spectrum is the zero ordinates; Connes (1999) gave an adèlic trace formula equivalent to GRH for $L$-functions with Größencharakter. *Barrier:* GRH becomes a positivity statement (a Weil explicit formula must be a positive distribution) exactly as hard as the original.
- **Selberg-class structure theory.** Classify $\mathcal{S}$ via the degree conjecture and Selberg's orthonormality conjectures. *Barrier:* structure constrains which $L$-functions exist but never locates their zeros; degree $2$ is already out of reach.
- **Positivity / explicit-formula criteria.** Weil's explicit formula, Li's criterion ($\lambda_n\ge 0$ for all $n$), and Lagarias-type extensions to $\mathcal{S}$ give clean equivalences. *Barrier:* each is logically equivalent to GRH, relocating rather than removing the difficulty.

## 4. Critical assessment

The dossier's central thesis is well supported: every genuine advance proves something *about* zeros — counts, proportions, statistics, zero-free regions — without excluding a single off-line zero, and the equivalent reformulations are equivalent precisely because they cannot be easier. The contrast with the function-field case is the sharpest available diagnostic: where a cohomological mechanism exists, the analogue is a theorem (Deligne 1974); where it is absent, the problem persists. The "grand" character compounds the difficulty, since a proof must be uniform over an entire class rather than function-by-function.

Two cautions are warranted. First, the disputed announcements (de Branges' long-running program; Atiyah's 2018 "Todd function" sketch) are correctly recorded as not accepted, and the dossier states this neutrally with the relevant objections (Conrey–Li 2000 for de Branges). Second, the numerical evidence — the first $\sim 10^{13}$ zeros of $\zeta$ on the line — is evidence, not proof, and the document is appropriately careful to say so.

## 5. What a resolution would require / open directions

A full resolution must exclude *every* off-line zero of *every* element of the class at once. The most-hoped-for route is an arithmetic analogue of $\ell$-adic cohomology over $\mathrm{Spec}\,\mathbb{Z}$ (or a genuine $\mathbb{F}_1$ geometry) that imports Deligne's mechanism; this is the least developed. The most developed reformulation is Connes' adèlic positivity, but proving the required positivity unconditionally is the whole problem. Continued growth of critical-line proportions and full moment conjectures discipline expectations without plausibly reaching $100\%$. Proving Selberg's degree and orthonormality conjectures would narrow $\mathcal{S}$ enough for uniform automorphic input. Consensus across the active community (analytic number theory, RMT, Langlands functoriality, noncommutative geometry) is that a genuinely new idea is required.

## 6. Selected references

1. B. Riemann (1859), *Über die Anzahl der Primzahlen unter einer gegebenen Größe* — [high-confidence]
2. A. Piltz (1884), generalization of the hypothesis to $L(s,\chi)$ — [needs-verification]
3. G. H. Hardy (1914), *Sur les zéros de la fonction $\zeta(s)$ de Riemann* — [high-confidence]
4. E. Hecke (1918), *Eine neue Art von Zetafunktionen und ihre Beziehungen zur Verteilung der Primzahlen* — [high-confidence]
5. A. Selberg (1942), *On the zeros of Riemann's zeta-function on the critical line* — [high-confidence]
6. R. P. Langlands (1970), *Problems in the theory of automorphic forms* — [high-confidence]
7. H. L. Montgomery (1973), *The pair correlation of zeros of the zeta function* — [high-confidence]
8. P. Deligne (1974), *La conjecture de Weil. I*, doi:10.1007/BF02684373 — [high-confidence]
9. N. Levinson (1974), *More than one third of zeros of Riemann's zeta-function are on $\sigma=1/2$* — [high-confidence]
10. J. B. Conrey (1989), *More than two fifths of the zeros of the Riemann zeta function are on the critical line* — [high-confidence]
11. A. Selberg (1992), *Old and new conjectures and results about a class of Dirichlet series* — [high-confidence]
12. X.-J. Li (1997), *The positivity of a sequence of numbers and the Riemann hypothesis* — [high-confidence]
13. A. Connes (1999), *Trace formula in noncommutative geometry and the zeros of the Riemann zeta function*, doi:10.1007/s000290050042 — [high-confidence]
14. N. M. Katz, P. Sarnak (1999), *Zeroes of zeta functions and symmetry*, doi:10.1090/S0273-0979-99-00766-1 — [high-confidence]
15. J. Kaczorowski, A. Perelli (1999), *On the Selberg class of Dirichlet series: small degrees* — [needs-verification]
16. H. M. Bui, J. B. Conrey, M. P. Young (2011), *More than 41% of the zeros of the zeta function are on the critical line* — [needs-verification]
17. B. Rodgers, T. Tao (2020), *The de Bruijn–Newman constant is non-negative*, doi:10.1017/fmp.2020.6 — [high-confidence]

## AI Review Panel

### Claude (Anthropic) — in-house review

The survey is accurate where it matters most. It correctly identifies GRH as strictly harder than both RH and the Dirichlet GRH it contains, never overstates partial results, and keeps the crucial epistemic distinction between equivalence and tractability front and center — the positivity and spectral "reformulations" are flagged as logically equivalent to GRH and therefore not shortcuts. The function-field contrast is deployed correctly: Deligne's theorem is presented as the model of what GRH would mean, not as evidence that GRH is nearly within reach. The framing of the problem as a *uniform* statement over a class, rather than a sequence of individual conjectures, is the right emphasis and is handled well.

Three reservations. (i) The reference list inherits verification flags from the dossier, and several load-bearing items are not high-confidence: the Piltz 1884 citation (the very origin of the "generalized" form) is needs-verification and notoriously hard to pin to a precise 1884 reference; the Bui–Conrey–Young 2011 and Kaczorowski–Perelli 1999 entries are needs-verification. The headline "$\approx 41.7\%$" figure rests on the latter chain and should be checked against the primary papers and any subsequent improvements before being quoted as current. (ii) There is mild single-source reliance on the dossier itself for the precise proportion record and for the attribution of objections (e.g., Conrey–Li 2000 against de Branges); these are plausible and consistent with the public record but were not independently re-derived here. (iii) The claim that $\mathcal{S}$ coincides with the automorphic class is stated as expected/conjectural, which is correct — a reviewer should ensure it is never read as established.

The single most important thing a human reviewer should verify: that no sentence anywhere drifts from "open" to suggesting any degree-$\ge 2$ case is proven — the strongest unconditional statements remain proportions, averages, and the function-field analogue, none of which establish GRH for even one automorphic $L$-function. Verify also the exact current critical-line proportion against primary sources.

**Verdict:** accept-with-revisions.

### GPT (OpenAI) — pending
_Not yet run. To complete the panel, run the prompt in docs/review/REVIEW-TEMPLATE.md through GPT and record the verdict here and in the front matter._

### Gemini (Google) — pending
_Not yet run. See docs/review/REVIEW-TEMPLATE.md._

### Grok (xAI) — pending
_Not yet run. See docs/review/REVIEW-TEMPLATE.md._

## Human verification

AI review is not human peer review. This meta-analysis is offered for academic verification per ../docs/review/ACADEMIC-REVIEW.md; the flagged citations in particular require primary-source checking before any scholarly reliance. Status: human_review pending.

---
*Accredited to **Alexander Donahue** · The Unsolved Mathematics Atlas · CC BY 4.0. Cite per CITATION.cff.*

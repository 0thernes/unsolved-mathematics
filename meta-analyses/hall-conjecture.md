---
title: "Meta-Analysis: Hall's Conjecture"
slug: hall-conjecture
author: Alexander Donahue
type: ai-assisted-meta-analysis
peer_reviewed: false
problem_status: open
ai_review:
  claude:
    verdict: accept-with-revisions
    date: "2026-06-14"
    version: "claude-opus-4-8"
    summary: "An accurate, well-balanced survey of an open problem whose weak form is a textbook consequence of abc/Vojta; references carry verification flags and several need primary-source checking."
  gpt:
    verdict: pending
  gemini:
    verdict: pending
  grok:
    verdict: pending
human_review: pending
---

# Meta-Analysis: Hall's Conjecture

> **AI-generated meta-analysis — not peer-reviewed.** Curated and accredited by **Alexander Donahue** (human-in-the-loop). A survey/assessment of an open problem; it makes no claim of a new result. Citations carry verification flags and require human source-checking.

## Abstract

Hall's conjecture concerns how small the gap between a perfect cube and a perfect square can be: for integers with $x^3 \neq y^2$, how does $|x^3 - y^2|$ grow with $x$? Marshall Hall Jr. (1971), generalizing computational study of the Mordell equation $y^2 = x^3 + k$, proposed the **strong form** $|x^3 - y^2| > C\sqrt{x}$ for an absolute constant $C > 0$. The exponent $1/2$ is best possible: parametric families of Davenport–Lewis–Schinzel (1965) and Danilov (1982) yield infinitely many pairs with $|x^3 - y^2| \asymp \sqrt{x}$. The **weak form**, $|x^3 - y^2| \gg_\varepsilon x^{1/2-\varepsilon}$, is now the standard reading; it follows from the $abc$ conjecture and from Vojta's conjecture. Both forms remain unconditionally open. No power-saving unconditional lower bound $|x^3 - y^2| \gg x^\delta$ with fixed $\delta > 0$ is known — only the trivial $\geq 1$. The function-field analogue is a sharp theorem (Davenport). This meta-analysis surveys the statement, the state of the art, the principal approaches and their barriers, and what a resolution would require. It claims no new result.

## 1. Statement and significance

Let $x, y$ be integers with $x^3 \neq y^2$. The difference $k = x^3 - y^2$ is a nonzero integer, so $|k| \geq 1$ trivially; the real question is the growth of $|k|$ as $x \to \infty$. Hall's **strong conjecture** (1971) asserts an absolute $C > 0$ with $|x^3 - y^2| > C\sqrt{x}$ — equivalently $x \ll k^2$. The **weak conjecture** relaxes this to: for every $\varepsilon > 0$ there is $C_\varepsilon > 0$ with $|x^3 - y^2| > C_\varepsilon\, x^{1/2-\varepsilon}$.

The significance is structural. Hall's bound governs the height of integral points on the Mordell curves $y^2 = x^3 - k$: writing $H = |x^3 - y^2|$, the claim $x \ll H^{2+\varepsilon}$ controls how large integral solutions can be relative to the arithmetic complexity $H$ that forces them. It is a clean, concrete model case of the general principle — made precise by the $abc$ conjecture (Masser–Oesterlé, 1985) and Vojta's height inequalities — that integral points cannot greatly exceed their arithmetic complexity. For this reason Hall's conjecture appears persistently as a benchmark in expositions of $abc$, heights, and the Bombieri–Lang–Vojta program.

## 2. State of the art

**Status: open**, both forms. The honest unconditional picture is stark.

- *Unconditional lower bound.* Only the trivial $|x^3 - y^2| \geq 1$ is known. No fixed $\delta > 0$ is proved with $|x^3 - y^2| \gg x^\delta$ — not even a tiny power saving. The conjecture wants $\delta = 1/2 - \varepsilon$.
- *Per-fixed-$k$ effectivity.* For each individual $k$, Baker's linear forms in logarithms make $y^2 = x^3 + k$ effectively solvable, and integral points are tabulated for large $|k|$ (Gebel–Pethő–Zimmer; Stroeker–Tzanakis). This is effective but exponential and non-uniform in $k$ — the wrong shape for Hall.
- *Function-field analogue is a theorem.* Davenport (1965) proved $\deg(f^3 - g^2) \geq \tfrac12 \deg f + 1$ for coprime polynomials with $f^3 \neq g^2$, the exact strong inequality with sharp constant (equivalently via Mason–Stothers). The exponent $1/2$ is confirmed in the polynomial world.
- *Sharpness.* Davenport–Lewis–Schinzel (1965) and Danilov (1982) produce infinitely many integers with $|x^3 - y^2| \asymp \sqrt{x}$ (Danilov's ratios fall below $1$), so no exponent exceeding $1/2$ holds, and any strong constant must be small.
- *Conditional results.* Weak Hall follows from $abc$ and from Vojta's conjecture — robust, standard deductions, but both premises are open. Mochizuki's claimed $abc$ proof via inter-universal Teichmüller theory (PRIMS, 2021) is not accepted by the broad community; Scholze and Stix (2018) identified a contested inequality at the "Corollary 3.12" step. Weak Hall therefore cannot be treated as proven through this channel.

## 3. Principal approaches and barriers

**Deduction from $abc$.** Treating $y^2 + k = x^3$ as an $abc$ triple and bounding the radical yields, after standard manipulation, $x \ll_\varepsilon |k|^{2+\varepsilon}$, i.e. the weak bound with essentially optimal exponent. *Barrier:* $abc$ is itself open, and even granting it one does not extract the strong form's explicit constant.

**Vojta's conjecture.** Viewing integral points on $y^2 = x^3 - k$ as $S$-integral points on a genus-1 affine curve, Vojta's height inequality specializes to weak Hall and explains why $1/2$ is the natural exponent. *Barrier:* Vojta is at least as hard as $abc$; the diophantine-approximation machinery (Schmidt subspace theorem, Roth-type bounds) gives ineffective constants and does not reach this case with the needed uniformity.

**Baker's method.** For fixed $k$, linear forms in logarithms bound $x$ effectively. *Barrier:* the bounds are exponential and non-uniform in $k$; the gap to a uniform power law $x \ll k^2$ has never been bridged and the method seems structurally incapable of it.

**Function-field transfer.** Davenport's proof uses the Wronskian/Riemann–Hurwitz argument (the polynomial derivative). *Barrier:* there is no known arithmetic analogue of differentiation — the same wall separating the solved function-field $abc$ from the open number-field $abc$.

**Computation.** Lattice-reduction searches (Elkies) and Mordell-curve tabulation calibrate the strong constant and supply small-ratio data. *Barrier:* search is finite; it can refute over-strong constants but cannot prove a lower bound.

## 4. Critical assessment

The dossier's central claim — that Hall's conjecture is "transparently tied to $abc$/Vojta" — is sound and well documented, and the meta-analysis follows it. The weak form is genuinely a conditional theorem under $abc$; this is standard and uncontroversial. The honest emphasis on the **trivial-bound gap** (no unconditional $\delta > 0$) is the single most important fact a reader should retain: it shows how far unconditional methods are from the target, and it correctly resists any temptation to overstate partial progress.

Two points deserve calibration. First, the **strong form may be false as literally stated**: Danilov's family and Elkies's record ($r \approx 0.0211$ near $x = 5853886516781223$) show the Hall ratio $r = |x^3-y^2|/\sqrt{x}$ can be very small, and whether $\inf r > 0$ is itself unsettled. The dossier states this honestly and the meta-analysis preserves it; readers should not conflate "weak Hall is morally true" with "strong Hall is true." Second, the function-field theorem is strong positive evidence for the *exponent* but not for the integer *constant*, because the archimedean obstruction it sidesteps is exactly what governs the constant.

The numerical record (Elkies's $x$, $r$) and the Danilov constant ($\approx 0.97$) are quoted from secondary characterization in the dossier and should be checked against primary sources before being cited as exact.

## 5. What a resolution would require / open directions

- **Weak form.** Any accepted proof of $abc$ (or the relevant case of Vojta) yields it immediately. Alternatively, a direct uniform power-saving lower bound by some genuinely new method — none is on the horizon, since Baker's method is exponential and approximation tools are ineffective and non-uniform.
- **Strong form.** Beyond the exponent, one must determine the correct absolute constant — and even decide whether $\inf r > 0$, i.e. whether the strong form (with a positive constant) is true at all.
- **Function-field transfer.** Would require an arithmetic analogue of the derivative/Wronskian bridging the function-field/number-field divide.
- **Refined effective methods.** Improvements toward uniformity in $k$ in Baker-type bounds; no known path converts these into a power law.
- **Computation.** Can refute over-strong constants and guide the conjectural constant; cannot prove a lower bound.

## 6. Selected references

1. H. Davenport (1965), *On $f^3(t) - g^2(t)$* — function-field analogue, sharp constant. [high-confidence]
2. H. Davenport, D. J. Lewis, A. Schinzel (1965), *Polynomial identities for $x^3 - y^2 = k$ with small $k$* — sharpness constructions. [needs-verification]
3. A. Baker (1968), *Contributions to the theory of Diophantine equations II* (Mordell equation) — effective per-$k$ bounds. [needs-verification]
4. L. J. Mordell (1969), *Diophantine Equations* — background on $y^2 = x^3 + k$. [high-confidence]
5. Marshall Hall Jr. (1971), *The Diophantine equation $x^3 - y^2 = k$* — original conjecture. [high-confidence]
6. L. V. Danilov (1982), *The Diophantine equation $x^3 - y^2 = k$* (explicit sharp family). [needs-verification]
7. J. Oesterlé (1985), *Nouvelles approches du «théorème» de Fermat* ($abc$ conjecture). [high-confidence]
8. D. W. Masser (1986), *Open problems* (statement of the $abc$ conjecture). [needs-verification]
9. P. Vojta (1987), *Diophantine Approximations and Value Distribution Theory*, LNM 1239 — Vojta's conjecture. [high-confidence] (10.1007/BFb0072989)
10. S. Lang (1990), *Old and new conjectured Diophantine inequalities* — height conjectures. [high-confidence]
11. R. J. Stroeker, N. Tzanakis (1994), *Computing integral points on elliptic curves*. [high-confidence]
12. J. Gebel, A. Pethő, H. G. Zimmer (1997), *Computing integral points on Mordell's elliptic curves*. [needs-verification]
13. N. D. Elkies (2000), *Rational points near curves and small $|x^3 - y^2|$ via lattice reduction*. [high-confidence] (math/0005139)
14. I. Jiménez Calvo, J. Herranz, G. Sáez (2000), *A new approach to find good examples for Hall's conjecture*. [needs-verification]
15. M. Waldschmidt (2009), *Open Diophantine Problems* — Hall in the $abc$ context. [high-confidence]
16. S. Mochizuki (2021), *Inter-universal Teichmüller theory I–IV* (claimed $abc$ proof; disputed). [needs-verification]
17. P. Scholze, J. Stix (2018), *Why $abc$ is still a conjecture* (report on the IUT manuscripts). [high-confidence]

## AI Review Panel

### Claude (Anthropic) — in-house review

This is a careful and honest survey. Its strengths are that it states the open status of both forms plainly, foregrounds the genuinely stark unconditional gap (no proved $\delta > 0$, only the trivial $\geq 1$), and resists the common slip of presenting "weak Hall follows from $abc$" as if it settled anything — it correctly treats the Mochizuki route as contested per Scholze–Stix and does not lean on it. The separation of the robust qualitative claim (weak Hall) from the fragile quantitative one (the strong constant, possibly false as literally stated) is the right framing and is maintained throughout.

Three caveats a human reviewer must weigh. (i) **Reference reliability.** A majority of the cited works carry "needs-verification" flags — including Danilov (1982), Davenport–Lewis–Schinzel (1965), Baker's Mordell-equation paper, Gebel–Pethő–Zimmer, and the Masser problem list. Exact titles, venues, years, and (for Danilov) the *Mathematical Notes* citation must be checked against primary sources before quotation. Only Vojta's LNM 1239 and Elkies's lattice-reduction paper carry confident identifiers; no identifier was fabricated, but the em-dashes signal real gaps. (ii) **Single-source reliance and possible overstatement.** The numerical claims — Elkies's $x = 5853886516781223$ with $r \approx 0.0211$, and Danilov's constant $\approx 0.97$ — trace to the dossier's own characterization, not to independently re-derived primary data; they are plausible and widely repeated but should not be quoted as exact without source-checking. The derivation "$abc$ $\Rightarrow$ $x \ll |k|^{2+\varepsilon}$" is stated at the textbook level of rigor and should be confirmed against a standard treatment (e.g. Waldschmidt or Nitaj) rather than taken as self-contained here.

(iii) **The single most important thing to verify:** that the *exponent* in weak Hall ($1/2 - \varepsilon$) and the *power* in the height bound ($x \ll H^{2+\varepsilon}$) are stated consistently and correctly throughout, since a factor-of-two slip between the $\sqrt{x}$ form and the $H^2$ form is the easiest error to introduce and the one most likely to propagate. I recommend acceptance once the flagged citations are primary-source-checked and the numerical records are confirmed.

**Verdict:** accept-with-revisions.

### GPT (OpenAI) — pending
_Not yet run. To complete the panel, run the prompt in docs/review/REVIEW-TEMPLATE.md through GPT and record the verdict here and in the front matter._

### Gemini (Google) — pending
_Not yet run. See docs/review/REVIEW-TEMPLATE.md._

### Grok (xAI) — pending
_Not yet run. See docs/review/REVIEW-TEMPLATE.md._

## Human verification

AI review is not human peer review. This document is offered for academic verification per ../docs/review/ACADEMIC-REVIEW.md: a domain expert should check the statement of both forms, the conditional $abc$/Vojta deductions, the sharpness constructions, and especially the flagged citations and numerical records against primary sources. Status: human_review pending.

---
*Accredited to **Alexander Donahue** · The Unsolved Mathematics Atlas · CC BY 4.0. Cite per CITATION.cff.*

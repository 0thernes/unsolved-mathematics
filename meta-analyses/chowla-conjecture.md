---
title: "Meta-Analysis: The Chowla Conjecture"
slug: chowla-conjecture
author: Alexander Donahue
type: ai-assisted-meta-analysis
peer_reviewed: false
problem_status: active-progress
ai_review:
  claude:
    verdict: accept-with-revisions
    date: "2026-06-14"
    version: "claude-opus-4-8"
    summary: "A faithful, well-scoped survey of the logarithmic-vs-natural-density and odd-vs-even-order frontier, sound on the mathematics but dependent on references whose exact identifiers still need primary-source confirmation."
  gpt:
    verdict: pending
  gemini:
    verdict: pending
  grok:
    verdict: pending
human_review: pending
---

# Meta-Analysis: The Chowla Conjecture

> **AI-generated meta-analysis — not peer-reviewed.** Curated and accredited by **Alexander Donahue** (human-in-the-loop). A survey/assessment of an open problem; it makes no claim of a new result. Citations carry verification flags and require human source-checking.

## Abstract

The Chowla conjecture asserts that the Liouville function $\lambda(n)=(-1)^{\Omega(n)}$ is asymptotically uncorrelated along shifts: for distinct shifts and exponents not all even, $\sum_{n\le x}\lambda(n+h_1)^{a_1}\cdots\lambda(n+h_k)^{a_k}=o(x)$. It is the higher-order, autocorrelation form of the heuristic that prime-factor parity is pseudorandom, generalizing the single-sum statements equivalent to the Prime Number Theorem ($k=1$) and the Riemann Hypothesis (square-root cancellation). This meta-analysis surveys the problem's status as recorded in the dossier. The modern era is defined by two breakthroughs: the Matomäki–Radziwiłł short-interval theorem (2015), which yields the two-point case *averaged over shifts*; and Tao's entropy decrement argument (2016), which yields the *logarithmically-averaged* two-point case at a fixed shift, extended by Tao–Teräväinen (2018) to all odd orders. The conjecture remains open in its original natural-density form, and even-order correlations lie beyond current methods. We assess the principal approaches, the parity barrier, and the precise gaps — removing logarithmic averaging and reaching even orders — that a resolution must close, and we flag the verification status of the cited literature.

## 1. Statement and significance

For the Liouville function $\lambda(n)=(-1)^{\Omega(n)}$, where $\Omega$ counts prime factors with multiplicity, Chowla's conjecture (1965, in his monograph *The Riemann Hypothesis and Hilbert's Tenth Problem*) predicts that all higher correlations vanish: for distinct non-negative integers $h_1,\dots,h_k$ and exponents $a_i\in\{1,2\}$ not all even,
$$\sum_{n\le x}\lambda(n+h_1)^{a_1}\cdots\lambda(n+h_k)^{a_k}=o(x).$$
The function $\lambda$ agrees with the Möbius function $\mu$ on squarefree integers, so the conjecture is equally a statement about $\mu$. Its significance is structural: $\sum_{n\le x}\lambda(n)=o(x)$ is the Prime Number Theorem, and $O(x^{1/2+\varepsilon})$ cancellation is equivalent to the Riemann Hypothesis. Chowla's leap was to demand statistical *independence* of shifted copies — vanishing autocorrelations — which encodes pseudorandomness of prime-factor parity far beyond single-sum cancellation. The two-point case $\sum_{n\le x}\lambda(n)\lambda(n+h)=o(x)$ is the simplest open instance. Sarnak's 2010 reformulation tied this circle of ideas to Möbius orthogonality against zero-entropy dynamical systems, making Chowla a keystone linking multiplicative number theory and ergodic theory.

## 2. State of the art

Per the dossier, the unconditional landscape is as follows.

- **Single sums ($k=1$):** $\sum_{n\le x}\lambda(n)=o(x)$, the Prime Number Theorem, settled 1896/1899.
- **Logarithmically-averaged two-point Chowla:** Tao (2016) proved $\sum_{n\le x}\frac{\lambda(n)\lambda(n+h)}{n}=o(\log x)$ for every fixed $h\neq 0$ via the entropy decrement argument (arXiv:1509.05422).
- **Logarithmically-averaged odd-order Chowla:** Tao–Teräväinen (2018) extended this to all odd-order correlations of arbitrary length, and established equivalence with the logarithmic Sarnak conjecture in broad generality (arXiv:1802.05870).
- **Averaged (non-logarithmic) two-point Chowla:** Matomäki–Radziwiłł–Tao (2016) proved the two-point case averaged over $h\le H$ with $H\to\infty$, building on the Matomäki–Radziwiłł short-interval theorem (arXiv:1501.04585).
- **Sign patterns:** Hildebrand (1986) showed all eight length-3 sign patterns occur with positive density; the number of realized length-$k$ patterns grows superlinearly (Matomäki–Radziwiłł–Tao).

Conditionally, ergodic uniformity hypotheses (Frantzikinakis–Host) yield further logarithmic cases. Notably, GRH and zero-density hypotheses sharpen error terms but are *not* known to imply Chowla: the correlation content is believed orthogonal to, and harder than, RH. The original natural-density conjecture, and all even-order correlations, are open and uniformly listed as such.

## 3. Principal approaches and barriers

**Entropy decrement (logarithmic averaging).** Tao's method exploits multiplicativity via $\lambda(pn)=-\lambda(n)$; aggregating across primes would force correlations unless an entropy quantity decreases at each scale, but boundedness of entropy forces the correlations to vanish. *Barrier:* the argument is tied to logarithmic weights and to *odd* products, where the sign twist survives. Even orders see no cancellation from this mechanism.

**Short intervals (Matomäki–Radziwiłł).** Their 2015 theorem shows bounded multiplicative functions have near-mean averages in almost all short intervals $[x,x+h]$, $h\to\infty$ arbitrarily slowly — breaking the longstanding $x^\theta$ length barrier. *Barrier:* averaging over $h$ hides individual-shift behavior; localizing the gain to a single fixed shift without logarithmic weighting is the canonical open obstacle.

**Ergodic structure.** Following Sarnak, Frantzikinakis, Host, Tao and Teräväinen decompose multiplicative functions into structured (nilsequence) and pseudorandom parts via Furstenberg correspondence and Gowers–Host–Kra theory. *Barrier:* the inverse theory for higher Gowers $U^k$ norms of multiplicative functions is incomplete, and the logarithmic Chowla/Sarnak equivalence does not upgrade to natural density.

**Sieves and the parity barrier.** Selberg's parity obstruction is a *negative* result: sieve weights cannot distinguish even- from odd-prime-factor integers — exactly the information $\lambda$ encodes — so no purely sieve-theoretic argument can settle even the two-point case. Breaking parity requires global exploitation of multiplicativity (as in entropy decrement) or external $L$-function input.

## 4. Critical assessment

The dossier's framing is accurate and admirably disciplined about what is and is not proven. The crucial conceptual distinction it sustains — between *logarithmic* and *natural-density* averaging, and between *odd* and *even* orders — is the correct axis along which to read the field. The logarithmic odd-order results (Tao; Tao–Teräväinen) are genuine, peer-reviewed theorems; the natural-density and even-order statements are genuinely open. The dossier does not overclaim in either direction, and it correctly resists the common error of asserting that the natural-density statement "follows" from Tao's logarithmic theorem.

Two points warrant emphasis for a reader calibrating difficulty. First, the apparent smallness of the remaining gap is deceptive: "remove the average over $h$" and "remove the $1/n$ weight" are one-line *statements* whose resolution has resisted a decade of concentrated effort by the strongest practitioners, precisely because the operative inputs (short-interval cancellation, entropy decrement) are structurally averaged or logarithmic. Second, the claimed independence from RH is a belief, well-motivated but not a theorem; a reader should treat "harder than RH" as expert consensus rather than established fact.

The treatment of disputed announcements is appropriately neutral and diagnostic, sorting recurring failure modes (parity-barrier violations, illegitimate log-to-density passage, Gowers-norm uniformity gaps) without naming or amplifying specific claims.

## 5. What a resolution would require / open directions

Per the dossier, a full resolution must (1) **remove logarithmic averaging**, passing to natural-density sums at a fixed shift, which demands control of "thin scales" where multiplicativity gives no leverage; (2) **reach even-order correlations**, where the entropy-decrement sign twist cancels and a genuinely new mechanism is needed; and (3) **break the parity barrier quantitatively** beyond the single-shift case, likely via higher-order Gowers-norm inverse theory for multiplicative functions. The realistic near-term targets are the **natural-density two-point case at a fixed shift** and the **logarithmic four-point (even-order) case**. Plausible routes include higher-uniformity estimates for multiplicative functions in short intervals (Matomäki–Shao–Tao–Teräväinen) feeding improved Gowers-norm control, an ergodic resolution of characteristic-factor structure upgrading logarithmic statements to natural density, or an even-order analogue of entropy decrement.

## 6. Selected references

1. S. Chowla, *The Riemann Hypothesis and Hilbert's Tenth Problem* (1965) — foundational. [high-confidence]
2. P. Sarnak, *Three lectures on the Möbius function, randomness and dynamics* (2010) — survey. [high-confidence]
3. K. Matomäki, M. Radziwiłł, *Multiplicative functions in short intervals*, arXiv:1501.04585 (2015) — breakthrough. [high-confidence]
4. K. Matomäki, M. Radziwiłł, T. Tao, *Sign patterns of the Liouville and Möbius functions*, arXiv:1509.01545 (2015) — breakthrough. [high-confidence]
5. T. Tao, *The logarithmically averaged Chowla and Elliott conjectures for two-point correlations*, arXiv:1509.05422 (2016) — breakthrough. [high-confidence]
6. K. Matomäki, M. Radziwiłł, T. Tao, *An averaged form of Chowla's conjecture*, arXiv:1503.05121 (2016) — breakthrough. [high-confidence]
7. T. Tao, J. Teräväinen, *The structure of logarithmically averaged correlations of multiplicative functions*, arXiv:1708.02610 (2017) — modern. [high-confidence]
8. T. Tao, J. Teräväinen, *Odd order cases of the logarithmically averaged Chowla conjecture*, arXiv:1802.05870 (2018) — breakthrough. [high-confidence]
9. T. Tao, *Equivalence of the logarithmically averaged Chowla and Sarnak conjectures*, arXiv:1605.04628 (2018) — modern. [high-confidence]
10. A. Hildebrand, *On consecutive values of the Liouville function* (1986) — foundational. [needs-verification]
11. N. Frantzikinakis, B. Host, *The logarithmic Sarnak conjecture for ergodic weights*, arXiv:1708.00677 (2018) — breakthrough. [needs-verification]
12. S. Ferenczi, J. Kułaga-Przymus, M. Lemańczyk, *Sarnak's conjecture: what's new* (survey), arXiv:1710.04039 (2018) — survey. [needs-verification]
13. T. Tao, J. Teräväinen, *A quantitative bound for the logarithmically averaged Chowla conjecture*, arXiv:1911.11891 (2020) — modern. [needs-verification]
14. K. Matomäki, X. Shao, T. Tao, J. Teräväinen, *Higher uniformity of bounded multiplicative functions in short intervals*, arXiv:2007.15644 (2022) — modern. [needs-verification]
15. J. Bourgain, P. Sarnak, T. Ziegler, *The Möbius function and distribution of orbits* (Sarnak conjecture context) (2012) — breakthrough. [needs-verification]

## AI Review Panel

### Claude (Anthropic) — in-house review

The survey is mathematically sound and unusually well-calibrated. Its central organizing distinctions — logarithmic versus natural-density averaging, and odd versus even order — are exactly the right ones, and they are applied consistently across the statement, state-of-the-art, and barrier sections. The parity-barrier discussion correctly identifies Selberg's obstruction as a *negative* theorem rather than a mere difficulty, and the document avoids the most common overstatement in this area (that natural-density Chowla "follows" from Tao's logarithmic result). The handling of disputed proofs is neutral and diagnostically useful. I see no claim here that the natural-density or even-order conjecture has been resolved, which is correct.

My principal reservation is bibliographic. The genuinely load-bearing results — Tao 2016 (arXiv:1509.05422), Matomäki–Radziwiłł 2015 (arXiv:1501.04585), Tao–Teräväinen 2018 (arXiv:1802.05870) — are canonical and very likely correct as stated, but the dossier itself flags that even these arXiv identifiers should be confirmed against the published record, and several references carry `needs-verification` flags where the exact title, year, or identifier may differ from the published version. A human reviewer must check each identifier at the primary source; I have not independently verified any arXiv number here. I also note a mild single-source character to some claims (e.g., the precise form of the entropy-decrement constraint on odd versus even orders) that rests on the dossier's own exposition rather than cross-checked literature.

The single most important thing a human reviewer should verify is the **attribution and exact statement of the odd-order extension**: confirm that Tao–Teräväinen (arXiv:1802.05870) proves the logarithmically-averaged Chowla conjecture for *all odd orders* unconditionally (not merely under an ergodic hypothesis), since this is the strongest unconditional fixed-shift result the survey relies on and the boundary of what is claimed proven. Secondarily, verify the "harder than / independent of RH" claim is presented as belief, not theorem — which, in this draft, it is.

**Verdict:** accept-with-revisions.

### GPT (OpenAI) — pending

_Not yet run. To complete the panel, run the prompt in docs/review/REVIEW-TEMPLATE.md through GPT and record the verdict here and in the front matter._

### Gemini (Google) — pending

_Not yet run. See docs/review/REVIEW-TEMPLATE.md._

### Grok (xAI) — pending

_Not yet run. See docs/review/REVIEW-TEMPLATE.md._

## Human verification

AI review is not human peer review; it is offered here only as a structured aid for academic verification, per ../docs/review/ACADEMIC-REVIEW.md. The references above carry verification flags and require primary-source confirmation, and the mathematical claims should be checked against the published record before being relied upon. Status: human_review pending.

---
*Accredited to **Alexander Donahue** · The Unsolved Mathematics Atlas · CC BY 4.0. Cite per CITATION.cff.*

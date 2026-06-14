---
title: "Meta-Analysis: Singmaster's Conjecture"
slug: singmaster-conjecture
author: Alexander Donahue
type: ai-assisted-meta-analysis
peer_reviewed: false
problem_status: active-progress
ai_review:
  claude:
    verdict: accept-with-revisions
    date: "2026-06-14"
    version: "claude-opus-4-8"
    summary: "A faithful and well-calibrated survey of an open problem whose averaged-vs-pointwise gap is correctly identified as the crux, but whose reference list leans heavily on unverified entries that require source-checking."
  gpt:
    verdict: pending
  gemini:
    verdict: pending
  grok:
    verdict: pending
human_review: pending
---

# Meta-Analysis: Singmaster's Conjecture

> **AI-generated meta-analysis — not peer-reviewed.** Curated and accredited by **Alexander Donahue** (human-in-the-loop). A survey/assessment of an open problem; it makes no claim of a new result. Citations carry verification flags and require human source-checking.

## Abstract

Singmaster's conjecture asserts that the multiplicity $N(a) = \#\{(n,k):\binom{n}{k}=a\}$ of any integer $a>1$ in Pascal's triangle is bounded by an absolute constant. Posed by David Singmaster in 1971, the problem is elementary to state but sits atop deep Diophantine geometry. Every $a$ appears at least twice by symmetry and at least four times for $a>1$ via $a=\binom{a}{1}$; a Fibonacci-driven family yields $N(a)\ge 6$ infinitely often, with $3003$ the smallest known sextuple occurrence. No integer is known to occur seven or more times. This meta-analysis surveys the landscape: the benchmark 1974 Abbott–Erdős–Hanson bound $N(a)=O(\log a/\log\log a)$, still essentially unimproved unconditionally; per-equation finiteness via Siegel, Baker, and Faltings; and the 2021 Matomäki–Radziwiłł–Shao–Tao–Teräväinen power-saving average bound. The central obstruction is that all strong modern results control multiplicity *on average* or off a sparse exceptional set, while the conjecture demands a *pointwise* bound for every $a$ — including a single rare worst case that averaging methods cannot reach. The conjecture remains open. Citations below carry verification flags; several entries are unconfirmed and require human source-checking.

## 1. Statement and significance

Pascal's triangle lists the binomial coefficients $\binom{n}{k}$. For a fixed integer $a>1$ define its multiplicity $N(a)=\#\{(n,k):\binom{n}{k}=a\}$. Symmetry $\binom{n}{k}=\binom{n}{n-k}$ and the identities $a=\binom{a}{1}=\binom{a}{a-1}$ force $N(a)\ge 4$ for every $a>1$. Singmaster (1971) asked whether there is an absolute constant $C$ with $N(a)\le C$ for all $a$. He observed, via a Fibonacci coincidence, that $N(a)\ge 6$ holds infinitely often, and singled out $3003=\binom{3003}{1}=\binom{78}{2}=\binom{15}{5}=\binom{14}{6}$ (with mirror images) as the least number occurring six times.

The significance is twofold. First, the problem is a model case of how a question requiring no machinery to state can encode hard arithmetic geometry: bounding $N(a)$ reduces to counting integral points on a family of curves $\binom{n}{k}=\binom{m}{\ell}$. Second, it is a fixture of the Erdős problem circle and a recurring testbed for both effective Diophantine methods and modern analytic number theory.

## 2. State of the art

The conjecture is **open**, classified *active-progress*. Three strata of knowledge stand out.

**Unconditional, uniform.** The Abbott–Erdős–Hanson bound $N(a)=O(\log a/\log\log a)$ (1974) remains the strongest fully unconditional bound valid for all $a$. It is exponentially weaker than the conjectured $O(1)$ and has not been improved in order of magnitude for general $a$ in half a century.

**Per-equation finiteness.** For each fixed pair $(k,\ell)$, the equation $\binom{n}{k}=\binom{m}{\ell}$ has finitely many solutions by Siegel's theorem (and Faltings for genus $\ge 2$); in low cases such as $\binom{n}{2}=\binom{m}{4}$ the solution set has been completely enumerated by Baker's effective methods (de Weger and others). These yield $N(a)\le 8$ off a controlled exceptional set, but the bounds are not uniform in $(k,\ell)$.

**Averaged frontier.** Matomäki, Radziwiłł, Shao, Tao, and Teräväinen (2021, arXiv:2106.03335) prove that the number of nontrivial solutions of $\binom{n}{k}=a$ with $k\ge 3$ and $a\le N$ is $O(N^{2/3})$, a power saving over the trivial $O(N\log N)$. This gives the conjecture *on average* and forces anomalously high-multiplicity $a$ to be very sparse.

Empirically, exhaustive searches find no integer occurring more than six times below very large bounds; Erdős conjectured the true maximum is $\le 8$, attained at most finitely often.

## 3. Principal approaches and barriers

**Elementary growth/divisor bounds.** Because $\binom{n}{k}\sim n^k/k!$, a target $a$ equals $\binom{n}{k}$ for at most one $n$ per fixed $k$, and only for $k\lesssim\log a/\log\log a$. Counting levels gives the 1974 bound. *Barrier:* treating each level separately is lossy and cannot see the rigidity that makes solutions rare, so it cannot reach a constant.

**Diophantine equations on individual curves.** Most multiplicity must come from small $k$, reducing to $\binom{n}{2}=\binom{m}{\ell}$ and neighbours like $\binom{n}{3}=\binom{m}{4}$. Each defines a curve; integral points are finite (Siegel) and effectively computable (Baker). *Barrier:* the constants are non-uniform across $(k,\ell)$, and Faltings — which upgrades genus $\ge 2$ — is ineffective, so finiteness per curve does not assemble into one bound for all $a$.

**Analytic / averaged bounds.** The 2021 sieve-theoretic count controls multiplicity in aggregate and bounds the exceptional set's density. *Barrier:* averaged and sparse-exception statements are structurally blind to a single rare $a$ with huge $N(a)$, which is precisely what the conjecture forbids.

**abc-conditional smoothness.** Repeated binomial coefficients force unusually structured integers; abc-type input could make these scarce. *Barrier:* abc is itself open, so this transfers rather than resolves the difficulty.

## 4. Critical assessment

The dossier's central claim — that the gap between "bounded on average / off exceptions" and "bounded for every $a$" is the crux, and that the obstructions are structural rather than technical — is sound and is the standard expert reading. The three high-confidence anchors (Singmaster 1971, Abbott–Erdős–Hanson 1974, the 2021 MRSTT paper) are correctly identified and correctly characterized, including the honest framing that the 2021 result is *evidence for*, not a *proof of*, the conjecture.

Two cautions. First, the dossier's quantitative claims should be read as load-bearing and verified against primary sources: the exact statement of the $O(N^{2/3})$ count (the precise range of $k$ and the definition of "nontrivial"), and the precise constant in Erdős's "$\le 8$" guess. Second, the empirical claim that no number is known to appear more than six times is robustly reported across sources, but the specific search bound (the dossier elsewhere cites figures like $10^{60}$) is the kind of detail that drifts between secondary accounts and should be pinned to a primary computational reference.

The reduction "almost all multiplicity comes from small $k$" is stated cleanly and is the correct organizing principle; it is what licenses the entire Diophantine-curve reformulation. The treatment of claimed elementary proofs is appropriately skeptical and house-policy-compliant: it reports the problem as open and flags the recurring error (conflating an average or single-equation bound with the uniform statement).

## 5. What a resolution would require / open directions

A proof must control a **single, arbitrary, potentially very rare $a$** — exactly the regime averaged methods cannot enter. Two routes are visible. (i) A uniform-in-$(k,\ell)$ bound on integral points of the curves $\binom{n}{k}=\binom{m}{\ell}$ — effectively, a uniform Bombieri–Lang / Caporaso–Harris–Mazur type input bounding points on curves of bounded genus. This collides with the ineffectivity of Faltings and the non-uniformity of known effective methods. (ii) A structural obstruction — plausibly abc-type smoothness — forbidding an integer from lying on too many of these curves simultaneously. A third, more incremental direction is pushing the 2021 analytic framework from averages toward pointwise control, which must defeat the standard large-sieve/large-values barrier that is blind to a single sparse exception. None is currently in reach; consensus holds that an essentially new idea is required.

## 6. Selected references

1. David Singmaster (1971), *How often does an integer occur as a binomial coefficient?* — foundational. [high-confidence]
2. H. L. Abbott, P. Erdős, D. Hanson (1974), *On the number of times an integer occurs as a binomial coefficient* — benchmark bound $O(\log a/\log\log a)$. [high-confidence]
3. David Singmaster (1975), *Repeated binomial coefficients and Fibonacci numbers.* [needs-verification]
4. Paul Erdős (1980), *Some problems and results on the multiplicity of binomial coefficients.* [needs-verification]
5. B. M. M. de Weger (1985), *The equation $\binom{n}{2}=\binom{m}{4}$ and related Diophantine problems.* [needs-verification]
6. B. M. M. de Weger (1988), *Integral points on curves and equal binomial coefficients.* [needs-verification]
7. Richard K. Guy (1995), *Unsolved Problems in Number Theory* (section on binomial multiplicity). [high-confidence]
8. T. N. Shorey, R. Tijdeman (1997), *Powers in arithmetic progressions and binomial coefficients.* [needs-verification]
9. T. N. Shorey (2003), *Diophantine equations with binomial coefficients and exponential Diophantine equations.* [needs-verification]
10. M. A. Bennett and collaborators (2005), *The number of solutions of $\binom{n}{k}=\binom{m}{l}$.* [ai-suggested]
11. K. Matomäki, M. Radziwiłł, X. Shao, T. Tao, J. Teräväinen (2021), *Singmaster's conjecture in the interior of Pascal's triangle*, arXiv:2106.03335 — power-saving average bound. [high-confidence]
12. Terence Tao (2021), *Equal binomial coefficients: blog exposition and reductions.* [needs-verification]
13. (2023), *David Singmaster (1938–2023): obituary and mathematical legacy.* [needs-verification]

## AI Review Panel

### Claude (Anthropic) — in-house review

**Strengths.** This survey is well-calibrated and honest about the one thing that matters here: the difference between an averaged bound and a pointwise bound. It does not overstate the 2021 result, it correctly anchors the three landmark works, and it resists the standard trap of treating per-curve finiteness or an on-average statement as if it settled the uniform conjecture. The reduction to small $k$ and to integral points on the curves $\binom{n}{k}=\binom{m}{\ell}$ is presented accurately, and the barriers (ineffectivity of Faltings, non-uniformity across $(k,\ell)$, sieve-blindness to a single exception) are the genuine ones, not strawmen.

**Concerns.** (i) The reference list is the weak point. Of the entries cited, only four carry `high-confidence` flags (Singmaster 1971, Abbott–Erdős–Hanson 1974, Guy's *Unsolved Problems*, and the 2021 arXiv paper); the remainder are `needs-verification` or `ai-suggested`, with titles, years, and even authorship that I could not confirm and that should not be treated as established. A human must source-check every non-`high-confidence` row before citation, and in several cases should expect to correct or delete it. (ii) There is meaningful single-source reliance: the modern narrative leans almost entirely on the 2021 MRSTT paper, and the precise quantitative claims ($O(N^{2/3})$, the range $k\ge 3$, the meaning of "nontrivial," the empirical search bound) are paraphrased from secondary framing and need to be checked against the primary text. (iii) The "$N(a)\ge 6$ infinitely often via Fibonacci" claim and the $3003$ identity are standard and almost certainly correct, but the exact Fibonacci identity as transcribed in the dossier history should be verified symbolically.

**Most important thing to verify.** A human reviewer should confirm, directly from arXiv:2106.03335, the exact statement and range of validity of the 2021 power-saving bound, since the entire "state of the art" rests on it and the gap to the conjecture hinges on its being *averaged* rather than pointwise. If that statement is reproduced faithfully, the rest of the assessment stands.

**Verdict:** accept-with-revisions.

### GPT (OpenAI) — pending
_Not yet run. To complete the panel, run the prompt in docs/review/REVIEW-TEMPLATE.md through GPT and record the verdict here and in the front matter._

### Gemini (Google) — pending
_Not yet run. See docs/review/REVIEW-TEMPLATE.md._

### Grok (xAI) — pending
_Not yet run. See docs/review/REVIEW-TEMPLATE.md._

## Human verification

AI review is not human peer review. This assessment is offered for academic verification per ../docs/review/ACADEMIC-REVIEW.md; an AI panel can flag overstatement and source-quality issues but cannot replace a referee checking primary literature and symbolic identities. Status: human_review pending.

---
*Accredited to **Alexander Donahue** · The Unsolved Mathematics Atlas · CC BY 4.0. Cite per CITATION.cff.*

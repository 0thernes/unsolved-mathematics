---
title: "Meta-Analysis: The Catalan–Dickson Conjecture (Aliquot Sequences)"
slug: catalan-dickson-conjecture
author: Alexander Donahue
type: ai-assisted-meta-analysis
peer_reviewed: false
problem_status: open
ai_review:
  claude:
    verdict: accept-with-revisions
    date: "2026-06-14"
    version: "claude-opus-4-8"
    summary: "A careful, appropriately hedged survey of an open problem whose evidential weight favors the Guy–Selfridge counter-conjecture, but whose citations are largely unverified and require primary-source checking."
  gpt:
    verdict: pending
  gemini:
    verdict: pending
  grok:
    verdict: pending
human_review: pending
---

# Meta-Analysis: The Catalan–Dickson Conjecture (Aliquot Sequences)

> **AI-generated meta-analysis — not peer-reviewed.** Curated and accredited by **Alexander Donahue** (human-in-the-loop). A survey/assessment of an open problem; it makes no claim of a new result. Citations carry verification flags and require human source-checking.

## Abstract

The Catalan–Dickson conjecture asserts that every *aliquot sequence* — the orbit of an integer under iteration of the sum-of-proper-divisors map $s(n)=\sigma(n)-n$ — is bounded, hence eventually periodic, terminating at $1$ or entering a perfect, amicable, or sociable cycle. Posed by Catalan (1888) in an over-strong form and corrected by Dickson (1913), it stands opposed by the Guy–Selfridge counter-conjecture (1975), which predicts that a positive proportion of sequences diverge. This meta-analysis surveys the present state: the problem remains open, with computational and heuristic evidence favoring divergence but no proof either way. We review the four principal lines of work — direct computation of the "Lehmer five," the drivers/guides heuristic, the one-step statistical theory of $s$ (the Bosma–Kane aliquot constant), and the structural theory of the image and fibers of $s$ (untouchable numbers, Pomerance–Pollack) — and the barriers each faces. We assess what a resolution in either direction would require, and flag throughout that the underlying dossier's citations are largely unverified and demand primary-source confirmation.

## 1. Statement and significance

For $n\in\mathbb{Z}_{>0}$, write $s(n)=\sigma(n)-n$ for the sum of the proper divisors of $n$. The *aliquot sequence* from $n$ is $n,\,s(n),\,s(s(n)),\dots$. Three outcomes are classical: the sequence reaches $1$ and terminates; it enters a cycle (a fixed point — a perfect number; a $2$-cycle — amicable numbers; or a longer sociable cycle, as in Poulet's period-$28$ chain from $14{,}316$); or it grows without bound. The **Catalan–Dickson conjecture** asserts the third case never occurs: every orbit is bounded, hence eventually periodic. The significance is twofold. First, the iteration unifies the oldest objects of number theory — perfect, amicable, and sociable numbers are exactly its fixed points and cycles. Second, it is a sharp test case for the dynamics of arithmetic functions: $s$ is deterministic but neither monotone nor contractive, and its behavior is governed by factorizations that are themselves computationally hard.

## 2. State of the art

The problem is **open**, and the consensus tilt is against the conjecture it names. No aliquot sequence has been proved to diverge, and none of the small undetermined starters has been proved to terminate or cycle. All starting values below $1000$ are resolved except the **Lehmer five** — $276, 552, 564, 660, 966$ — which have been extended to thousands of terms; $276$ has surpassed two thousand terms with index values exceeding $200$ digits, showing no sign of bounding or termination. Unconditionally, the *one-step* dynamics are well understood: abundant numbers (where $s(n)>n$) have positive density $\approx 0.2476$, and the average of $\log(s(n)/n)$ — the Bosma–Kane aliquot constant — is known, with even $n$ tending to increase. The image and fibers of $s$ are controlled: untouchable numbers (outside the range of $s$) have positive lower density, and the fibers $s^{-1}(m)$ obey sharp average bounds. None of this reaches the infinite-iterate question.

## 3. Principal approaches and barriers

**Direct computation.** Extend each open sequence, factoring every term, until it resolves. The barrier is *asymmetry*: a terminating or cycling sequence can be certified in finite time, but an unbounded one can never be certified unbounded by extension. Each step requires factoring a large "stubborn cofactor"; cost grows without bound. Computation informs intuition but cannot settle the conjecture.

**Drivers and guides (Guy–Selfridge).** Certain divisors — drivers such as $2\cdot 3$ or $2^3\cdot 3\cdot 5$ — tend to persist across iterations and force $s(n)>n$. Even numbers carrying a strong driver are expected to grow until the driver breaks. This heuristic predicts unbounded sequences of positive density and matches computation strikingly. The barrier: it is a heuristic, not a theorem. It assumes quasi-independence of successive terms and offers no proof that a driver persists indefinitely, nor that rare downward excursions never overcome the drift.

**Statistical theory of $s$.** Erdős initiated, and Bosma–Kane sharpened, the rigorous study of the distribution of $s(n)/n$. The results are unconditional but *short-horizon*: a positive average growth does not preclude every individual orbit eventually descending.

**Image and fibers (Pomerance–Pollack–Kobayashi).** Deep unconditional theorems on untouchable-number density and fiber sizes constrain the phase space. The barrier: single-application structure does not transfer to the iterate.

The unifying obstruction is the absence of any **Lyapunov function** — a quantity provably monotone along every orbit — or any rigorous probabilistic model with controlled dependence.

## 4. Critical assessment

The dossier's framing is honest and well-calibrated. The asymmetry of computation is correctly identified as the structural reason the empirical program, however far extended, cannot resolve the conjecture; this is a genuine epistemic limit, not a passing difficulty. The claim that evidence favors Guy–Selfridge is defensible but should be stated with care: the one-step results (positive abundant density, even-$n$ upward drift) establish *plausibility* of divergence, not its likelihood as a measure over orbits, and the leap from one-step statistics to infinite-iterate behavior is precisely where rigor fails. A reader should not mistake "expert opinion favors divergence" for "divergence is nearly established."

Two numerical specifics warrant verification against primary sources: the abundant-number density $\approx 0.2476$ and the characterization of the Bosma–Kane aliquot constant. Both are stated in the literature, but the exact figures and the precise statement of the constant (it is the mean of $\log(s(n)/n)$, with sign and domain conventions that matter) should be checked. The historical attribution sequence — Catalan 1888, Dickson 1913, Guy–Selfridge 1975 — is standard and credible, though Catalan's original 1888 venue is given only loosely in the dossier and should be confirmed.

## 5. What a resolution would require / open directions

To prove **Catalan–Dickson** (boundedness) one would need an effective a priori bound on $\sup_k s^{(k)}(n)$ in terms of $n$, or a Lyapunov-type invariant; the positive average growth of $s$ on even numbers is evidence *against* any such universal bound, which is part of why the conjecture is doubted. To prove **Guy–Selfridge** (divergence) one would need rigorous control of an infinite, factorization-dependent orbit — certifying that some explicit sequence never descends below its floor, or that a positive-density family escapes — far beyond present analytic technique. The most promising distant route is a proven mixing/decorrelation statement replacing the quasi-independence assumption; intermediate routes include driver-persistence theorems and multi-step extensions of the Pomerance–Pollack program. Continued computation, while incapable of resolution, sharpens the empirical case and tests heuristics.

## 6. Selected references

1. E. Catalan (1888), *Note on aliquot sequences (proper-divisor iteration)* — foundational. [needs-verification]
2. L. E. Dickson (1913), *Theorems and tables on the sum of divisors of a number and its iterates* — foundational. [needs-verification]
3. L. E. Dickson (1919–1923), *History of the Theory of Numbers, Vol. I* — expository. [high-confidence]
4. P. Poulet (1929), *Sociable numbers and long cycles of the aliquot map* — foundational. [needs-verification]
5. D. H. Lehmer et al. (1965), *On amicable and aliquot sequences (machine computations)* — computational. [needs-verification]
6. R. K. Guy, J. L. Selfridge (1975), *What drives an aliquot sequence?* — breakthrough. [high-confidence]
7. R. K. Guy (2004), *Unsolved Problems in Number Theory* (3rd ed.), §B6 — expository. DOI 10.1007/978-0-387-26677-0. [high-confidence]
8. W. Bosma, B. Kane (2004), *The aliquot constant (average of $\log(s(n)/n)$)* — modern. [high-confidence]
9. W. Bosma (2008), *Aliquot sequences with small starting values: computations* — computational. [needs-verification]
10. M. Kobayashi, P. Pollack, C. Pomerance (2011), *On the distribution of sociable numbers* — modern. [needs-verification]
11. P. Pollack, C. Pomerance (2013), *Some problems of Erdős on the sum-of-divisors function* — survey. [needs-verification]
12. P. Pollack, C. Pomerance (2014), *Untouchable numbers and their density* — breakthrough. [needs-verification]
13. P. Zimmermann et al. (2020), *Computational records for the Lehmer five (FactorDB project notes)* — computational. [needs-verification]

## AI Review Panel

### Claude (Anthropic) — in-house review

This survey is one of the better-disciplined entries I have reviewed. Its central virtue is that it does not oversell: it states the problem as open, identifies the Guy–Selfridge counter-conjecture as the favored-but-unproved alternative, and — crucially — explains *why* the computational program cannot in principle resolve the question (the asymmetry between certifying boundedness and certifying divergence). The taxonomy of approaches is accurate and the barriers are correctly located at the gap between one-step statistics and infinite-iterate control. I have no substantive objection to the mathematics as presented.

My concerns are evidential rather than conceptual. First, the reference list is dominated by entries flagged **[needs-verification]**; only a handful — Dickson's *History*, Guy–Selfridge 1975, Guy's *Unsolved Problems* §B6, and Bosma–Kane — carry high confidence, and even the §B6 DOI is a book-series identifier that must be matched to the correct edition. Catalan's 1888 note and Lehmer's 1965 computations are real but their exact venues and titles are not pinned down here; a human must confirm them via MathSciNet/zbMATH before any of this is cited downstream. Second, there is a mild single-source character to the quantitative claims: the figure $0.2476$ for abundant density and the precise statement of the Bosma–Kane constant both trace to a thin set of references and should be independently checked, including sign and domain conventions. Third — and this is the single most important thing a human reviewer should verify — the survey's evidential framing ("computation and theory favor divergence") rests on extrapolating one-step statistics to the full orbit; a referee should confirm that the dossier nowhere lets that extrapolation harden into an implicit claim of near-resolution. It does not, in my reading, but the line is thin and worth a deliberate check.

On balance the document is accurate, honest, and useful, with the caveat that its citation apparatus is not yet verified. That is a revisable defect, not a fatal one.

**Verdict:** accept-with-revisions.

### GPT (OpenAI) — pending
_Not yet run. To complete the panel, run the prompt in docs/review/REVIEW-TEMPLATE.md through GPT and record the verdict here and in the front matter._

### Gemini (Google) — pending
_Not yet run. See docs/review/REVIEW-TEMPLATE.md._

### Grok (xAI) — pending
_Not yet run. See docs/review/REVIEW-TEMPLATE.md._

## Human verification

AI review is not human peer review. This meta-analysis is offered for academic verification per ../docs/review/ACADEMIC-REVIEW.md, and its citations — most of which carry a [needs-verification] flag — require primary-source confirmation before reuse. Status: human_review pending.

---
*Accredited to **Alexander Donahue** · The Unsolved Mathematics Atlas · CC BY 4.0. Cite per CITATION.cff.*

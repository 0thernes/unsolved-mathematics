---
title: "Meta-Analysis: Grimm's Conjecture"
slug: grimm-conjecture
author: Alexander Donahue
type: ai-assisted-meta-analysis
peer_reviewed: false
problem_status: open
ai_review:
  claude:
    verdict: accept-with-revisions
    date: "2026-06-14"
    version: "claude-opus-4-8"
    summary: "A faithful, well-calibrated survey of an open problem whose hardness is precisely understood, weakened mainly by a reference list dominated by unverified or ai-suggested entries."
  gpt:
    verdict: pending
  gemini:
    verdict: pending
  grok:
    verdict: pending
human_review: pending
---

# Meta-Analysis: Grimm's Conjecture

> **AI-generated meta-analysis — not peer-reviewed.** Curated and accredited by **Alexander Donahue** (human-in-the-loop). A survey/assessment of an open problem; it makes no claim of a new result. Citations carry verification flags and require human source-checking.

## Abstract

Grimm's Conjecture (1969) asserts that any run of consecutive composite integers $n+1,\dots,n+k$ can be labelled injectively by primes: there exist distinct primes $p_1,\dots,p_k$ with $p_i \mid (n+i)$. Via Hall's marriage theorem this is *exactly equivalent* to a counting condition — every sub-block of $m$ integers must possess at least $m$ distinct prime factors — converting an existence statement into an analytic lower bound on $\omega$ of sub-products. The conjecture remains open. The strongest unconditional result, due to Ramachandra, Shorey, and Tijdeman (1976), proves it for blocks of length up to $\exp\!\big(c(\log n/\log\log n)^{1/2}\big)$, i.e. for prime gaps short relative to $n$. Erdős and Selfridge (1971) exposed why the general case is hard: a strong form would force prime-gap bounds of shape $p_{m+1}-p_m \ll p_m^{1/2}/\log p_m$, exceeding even what the Riemann Hypothesis yields. This meta-analysis surveys the statement, the state of the art, the principal approaches and their shared barriers (sieve parity, smooth numbers in short intervals), and assesses what a resolution would require. It makes no claim of a new result.

## 1. Statement and significance

Let $n+1, n+2, \dots, n+k$ be consecutive composite integers. Grimm's Conjecture asserts the existence of **distinct** primes $p_1,\dots,p_k$ with $p_i \mid (n+i)$ for each $i$. The natural setting is a maximal run of composites wedged between two consecutive primes — a prime gap. The conjecture's appeal is the contrast between its elementary phrasing and its depth: it is accessible to anyone who knows what a prime factor is, yet it encodes some of the hardest open questions in analytic number theory.

The decisive formal observation is that, via Hall's marriage theorem applied to the bipartite integer–prime divisibility graph, a saturating matching exists if and only if every sub-block of $m$ integers collectively has at least $m$ distinct prime factors. This reformulation is **exact**, not merely sufficient: no information is lost, so Grimm's Conjecture *is* a statement about lower bounds on the distinct-prime-factor count $\omega$ of sub-blocks of consecutive integers.

## 2. State of the art

The problem is **open**. The benchmark unconditional theorem (Ramachandra–Shorey–Tijdeman, 1976) establishes the conjecture for blocks of length
$$k \le \exp\!\Big(c\,(\log n/\log\log n)^{1/2}\Big)$$
near $n$ — equivalently, for all prime gaps short relative to $n$. Per the dossier, no subsequent work has materially widened this range, so the frontier is essentially unchanged in kind since 1976. Unconditional lower bounds on the number of distinct prime factors of $\prod_{i=1}^{k}(n+i)$ (Erdős, Pomerance, Shorey) support the "weak Grimm" variants without delivering the full matching. Computational verification has found no counterexample below large bounds, but constrains only where a first failure could appear; it certifies nothing asymptotic.

The key conditional fact (Erdős–Selfridge, 1971) is that a strong general form of the conjecture would imply $p_{m+1}-p_m \ll p_m^{1/2}/\log p_m$, stronger than the RH-level bound $p_{m+1}-p_m \ll p_m^{1/2}\log p_m$. In this precise direction, the conjecture is *harder than RH-level prime-gap control*.

## 3. Principal approaches and barriers

**Hall's marriage reduction.** Converts existence into the exact counting inequality above. It relocates rather than resolves the difficulty: the matching fails locally when too many consecutive integers are built from a small common pool of small primes (smoothness). Verifying the inequality for *all* sub-blocks, uniformly in $n$ and $k$, is the hard analytic problem.

**Sieve / prime-factor counting (Ramachandra–Shorey–Tijdeman).** Lower-bounds the distinct-prime-factor count via sieve estimates plus transcendence-theoretic input (Baker-type bounds on linear forms in logarithms). This yields the benchmark range but is fundamentally capped by what is known about prime gaps; parity and density limitations of sieve theory block the required strength.

**Reduction to prime gaps (Erdős–Selfridge).** A structural, impossibility-flavored obstruction: any general proof either establishes prime-gap bounds beyond current technology, or verifies Hall's condition for long blocks *without* those bounds by exploiting the special multiplicative structure of a maximal composite run. No one knows how to do the latter.

**Smooth-number / largest-prime-factor methods** and **weak-Grimm strategies** address where the matching is most strained (clusters of smooth numbers) and prove weaker single-large-prime-factor statements in wider ranges. Both collide with the same obstruction: smooth numbers in *short* intervals are poorly understood.

## 4. Critical assessment

The dossier's central claims are internally consistent and well-calibrated. The Hall-theorem equivalence is genuine and standard, and the document is careful to flag it as exact. The Erdős–Selfridge linkage — that strong Grimm would yield prime-gap bounds beyond RH — is the load-bearing structural fact and is stated with appropriate precision, including the comparison to the RH bound. The honest framing of computational evidence (constrains, does not prove) and of weak Grimm (necessary, not sufficient) is correct: having $\ge k$ distinct prime factors does not imply Hall's condition holds for *every* sub-block.

Two cautions. First, the exact constant and the precise statement of the 1976 range, and the exact form of the Erdős–Selfridge implication ($p_m^{1/2}/\log p_m$ versus nearby variants), should be checked against the primary sources rather than taken from the survey. Second, the claim that "no subsequent work has materially widened" the 1976 range is plausible and consistent with the problem's reputation, but is the kind of negative literature claim that an expert should confirm directly.

## 5. What a resolution would require / open directions

A general proof must cover blocks as long as an **arbitrary** prime gap. By the Erdős–Selfridge linkage it must therefore either (a) prove prime-gap bounds beyond all current technology, or (b) verify Hall's matching condition for long blocks without first proving such bounds — leveraging that the block lies strictly between two primes to extract extra distinct factors, decoupling the result from generic gap bounds. Route (b) is the only conceivable path not blocked outright, and no one knows how to take it. The binding obstructions are the **parity/short-interval limitations of sieve theory** and the poor understanding of **smooth numbers in short intervals**, precisely where Hall's condition is tightest. Plausible incremental directions: sharper distinct-prime-factor counts to push the 1976 range; structural exploitation of the prime-gap setting; advances on smooth numbers in short intervals; and weak-Grimm-first results as stepping stones.

## 6. Selected references

1. C. A. Grimm, "A conjecture on consecutive composite numbers," *American Mathematical Monthly* **76** (1969). [high-confidence]
2. P. Erdős, J. L. Selfridge, "Some problems on the prime factors of consecutive integers" (1971). [high-confidence]
3. P. Erdős, J. L. Selfridge, "Some problems on the prime factors of consecutive integers, II" (1971). [needs-verification]
4. P. Erdős, R. Tijdeman (and related), "On the greatest prime factor of a product of consecutive integers" (1975). [needs-verification]
5. K. Ramachandra, T. N. Shorey, R. Tijdeman, "On Grimm's problem relating to factorisation of a block of consecutive integers," *J. Reine Angew. Math.* **273** (1976). [high-confidence]
6. T. N. Shorey, R. Tijdeman, "On the number of prime factors of a block of consecutive integers" (1977). [needs-verification]
7. P. Erdős, C. Pomerance, "On distinct prime factors of consecutive integers" (1984). [needs-verification]
8. T. N. Shorey, "Some remarks on Grimm's conjecture" (1988). [needs-verification]
9. R. K. Guy, *Unsolved Problems in Number Theory* (problem B32), 1st ed. (1984). [high-confidence]
10. T. N. Shorey, R. Tijdeman, *Exponential Diophantine Equations*, Cambridge (1986/1990). [high-confidence]
11. R. K. Guy, *Unsolved Problems in Number Theory* (problem B32), 2nd ed. (1994). [high-confidence]
12. R. K. Guy, *Unsolved Problems in Number Theory* (problem B32), 3rd ed. (2004). [high-confidence]
13. T. N. Shorey et al., "On the greatest prime factor of $\prod (n+i)$" (1996). [needs-verification]
14. "Computational verification of Grimm's conjecture" (computational note, 2013). [ai-suggested]
15. "Grimm's conjecture: a survey of progress and obstructions" (expository, 2020). [ai-suggested]

## AI Review Panel

### Claude (Anthropic) — in-house review

The survey is a strong, honest treatment of a narrow problem. Its principal strength is fidelity to the one fact that organizes the whole subject: the Hall-theorem reformulation is exact, and the Erdős–Selfridge linkage makes the conjecture provably entangled with prime-gap bounds beyond RH. The document never overreaches — it correctly separates "weak Grimm" (distinct-factor counts) from the full matching, and it treats computation as a localizer of counterexamples rather than evidence of truth. The altitude is right: it explains *why* the problem is hard, not merely that it is.

That said, three flags. (i) The reference section is weak ground to stand on: of fifteen entries, only seven carry [high-confidence]; the rest are [needs-verification] or [ai-suggested], with no DOIs or arXiv ids, and several rows in the source `papers.md` are explicitly acknowledged as plausible leads rather than confirmed works. Any citation to rows 3–8, 13–15 must be source-checked before use. (ii) There is mild single-source reliance: the quantitative claims — the $\exp(c(\log n/\log\log n)^{1/2})$ range, the constant, and the exact $p_m^{1/2}/\log p_m$ shape of the Erdős–Selfridge implication — all trace to the same small Ramachandra–Shorey–Tijdeman / Erdős–Selfridge cluster, and are reproduced here from the dossier rather than verified primaries; a transcription error in the exponent or the gap bound would propagate silently. (iii) The single most important thing a human reviewer should verify is the exact statement and provenance of the Erdős–Selfridge prime-gap implication — both that the implied bound is correctly $p_m^{1/2}/\log p_m$ and that it genuinely exceeds the RH-conditional bound — since that comparison is the document's central load-bearing claim about the conjecture's difficulty.

None of these are fatal; they are the normal gaps between a survey and a verified scholarly record. The mathematics is represented faithfully and no result is overstated.

**Verdict:** accept-with-revisions.

### GPT (OpenAI) — pending
_Not yet run. To complete the panel, run the prompt in docs/review/REVIEW-TEMPLATE.md through GPT and record the verdict here and in the front matter._

### Gemini (Google) — pending
_Not yet run. See docs/review/REVIEW-TEMPLATE.md._

### Grok (xAI) — pending
_Not yet run. See docs/review/REVIEW-TEMPLATE.md._

## Human verification

AI review is not human peer review. This meta-analysis is offered for academic verification per ../docs/review/ACADEMIC-REVIEW.md, and its citations — especially those flagged [needs-verification] and [ai-suggested] — require checking against primary sources before scholarly use. Status: human_review pending.

---
*Accredited to **Alexander Donahue** · The Unsolved Mathematics Atlas · CC BY 4.0. Cite per CITATION.cff.*

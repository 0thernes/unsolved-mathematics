---
title: "Meta-Analysis: Carmichael's Totient Conjecture"
slug: carmichael-totient-conjecture
author: Alexander Donahue
type: ai-assisted-meta-analysis
peer_reviewed: false
problem_status: open
ai_review:
  claude:
    verdict: accept-with-revisions
    date: "2026-06-14"
    version: "claude-opus-4-8"
    summary: "A faithful, well-scoped survey of an open century-old problem whose claims track the dossier, but whose references are largely unverified and lean heavily on a few canonical sources that a human must check."
  gpt:
    verdict: pending
  gemini:
    verdict: pending
  grok:
    verdict: pending
human_review: pending
---

# Meta-Analysis: Carmichael's Totient Conjecture

> **AI-generated meta-analysis — not peer-reviewed.** Curated and accredited by **Alexander Donahue** (human-in-the-loop). A survey/assessment of an open problem; it makes no claim of a new result. Citations carry verification flags and require human source-checking.

## Abstract

Carmichael's Totient Conjecture (1907) asserts that Euler's totient $\varphi$ never takes any value exactly once: for the multiplicity $A(n)=\#\varphi^{-1}(n)$, one has $A(n)\neq 1$ for all $n$. Equivalently, every integer $m$ has a "sibling" $m'\neq m$ with $\varphi(m')=\varphi(m)$. The statement is elementary and empirically robust, yet remains unproven after more than a century. This meta-analysis surveys the problem's status, the principal lines of attack — elementary sibling constructions, Klee's finite criterion (1947), Pomerance's structural constraint (1974), and Ford's analytic theory of totients (1998) — and the barrier common to all of them: converting average or structural control of $\varphi$-fibers into a uniform statement excluding a single rogue value of arbitrary size. We record what is unconditionally known (enormous lower bounds on any counterexample; resolution of the companion Sierpiński multiplicity problem), what is conditional or heuristic, and what a resolution would require. The conjecture is widely believed true. The assessment makes no claim of a new result; it is a curated survey whose cited references carry verification flags and require human source-checking.

## 1. Statement and significance

For a positive integer $n$, let $A(n)=\#\{m:\varphi(m)=n\}$ be the size of the totient fiber over $n$. Values with $A(n)=0$ are *nontotients*; the conjecture concerns the possibility $A(n)=1$, a value taken exactly once ("sporadic"). Carmichael's Totient Conjecture states: **no totient value is sporadic**, i.e. $A(n)\neq 1$ for every $n$.

The significance is twofold. First, $\varphi$ is the most basic multiplicative arithmetic function attached to $(\mathbb{Z}/n\mathbb{Z})^\times$, and the conjecture is the simplest unresolved statement about the *fibers* of that function. Second, it sits at the junction of two solved or near-solved companion questions: Sierpiński's conjecture (every multiplicity $k\geq 2$ occurs), and Ford's distribution theory for the image $V(x)=\#\{\varphi(m)\leq x\}$. In that framing $k=1$ is the single multiplicity whose realizability is undecided, which sharpens the conjecture into a precise gap rather than a vague open question.

## 2. State of the art

The status is **open**, and the consensus is that the conjecture is **true**. The two strongest unconditional facts are (i) a sequence of computational lower bounds on the least counterexample, certified via Klee's finite criterion, reportedly pushing the threshold past $10^{10^{10}}$ (Schlafly–Wagon 1994 to $\sim 10^{10^{7}}$; Ford 1998 and later refinements beyond $10^{10^{10}}$), and (ii) Pomerance's (1974) structural theorem that any counterexample $m$ satisfies $p^2\mid m$ for every prime $p$ with $(p-1)\mid\varphi(m)$, forcing $m$ to be extraordinarily square-rich. The companion Sierpiński problem was settled outright by Ford (1998): every $k\geq 2$ is attained as a multiplicity. No counterexample is known in either direction, and no method has closed the gap between "no counterexample below $X$" and "no counterexample."

## 3. Principal approaches and barriers

**Elementary sibling constructions.** Given $\varphi(m)=n$, one manufactures $m'\neq m$ with the same totient — e.g. $\varphi(2m)=\varphi(m)$ for odd $m$, or swapping a prime power $p^a$ for $q^b$ with $\varphi(p^a)=\varphi(q^b)$. These dispose of essentially all "generic" $m$ and reduce the problem to integers of rigid factorization. *Barrier:* no finite family of substitutions is exhaustive; a counterexample is precisely an $m$ on which every construction fails simultaneously, which elementary methods cannot exclude uniformly.

**Klee's reformulation (1947).** A least counterexample must have a constrained ("irreducible") form, yielding a finite, checkable criterion. *Barrier:* the criterion can in principle be satisfied for arbitrarily large $m$; computation certifies only a finite range, and no descent or finiteness theorem upgrades a bound to a proof.

**Pomerance's structural constraints (1974).** The $p^2\mid m$ condition ties a counterexample to an implausible configuration of primes $p$ with $p-1$ supported on a prescribed prime set. *Barrier:* "implausible" is not "impossible"; one needs an analytic input on the joint distribution of shifted primes that is currently out of reach.

**Ford's analytic theory (1998).** Precise asymptotics for $V(x)$ and fiber sizes, plus the resolution of Sierpiński's $k\geq 2$ case. *Barrier:* the methods control averages and typical behavior, but the conjecture is a worst-case statement about a single value; bridging from average/structural control to uniform $A(n)\neq 1$ is the central obstruction.

## 4. Critical assessment

The four programs are convergent rather than competing: each independently makes a counterexample look more pathological, yet none crosses the uniformity threshold. This is the recurring signature of the problem. The most consequential historical episode is Carmichael's own 1907 "proof" and its 1922 retraction — a textbook case of an elementary argument silently assuming the uniformity it must prove. The dossier is right to stress that the same flaw recurs in informal "proofs" that circulate periodically: a sibling construction handling all but an unaddressed special class, then an unjustified claim that the class is empty.

A second hazard the dossier handles well is the conflation of Carmichael's conjecture with Sierpiński's. Ford's 1998 resolution of the latter ($k\geq 2$ all occur) is genuine and proven, but says nothing decisive about whether $k=1$ ever occurs. Describing Carmichael as "nearly done" because its neighbor is solved is a category error; the methods that realize multiplicities $\geq 2$ do not address the existence of a sporadic value. Similarly, the gigantic computational bounds are evidence, not proof — a point worth repeating because the sheer size of $10^{10^{10}}$ tempts overstatement.

The most likely route to a resolution, per the dossier, is analytic control of shifted primes extending Pomerance's program — which honestly ties the problem to the hardness of the surrounding analytic number theory (smooth shifted primes, prime $k$-tuples for $p-1$) rather than promising an elementary shortcut.

## 5. What a resolution would require / open directions

A proof must convert structural/average control of $\varphi$-fibers into a uniform worst-case exclusion of multiplicity $1$ for every $n$. Concretely, the most-cited route is an analytic statement showing the simultaneous prime conditions in Pomerance's theorem cannot all hold — a claim about the joint distribution of shifted primes presently beyond reach. Plausible directions: (1) shifted-prime analysis controlling primes $p$ with $p-1$ supported on prescribed prime sets; (2) sieve and large-deviation refinements of Ford's totient machinery to reach the $k=1$ tail; (3) continued computation to extend the bound — valuable as evidence but not expected to prove the conjecture. A counterexample, conversely, would be a single explicitly square-structured integer larger than any tested threshold; the structural constraints make one appear unlikely.

## 6. Selected references

1. R. D. Carmichael, *On Euler's $\varphi$-function*, Bulletin AMS, 1907 — foundational. [high-confidence]
2. R. D. Carmichael, *Note on Euler's $\varphi$-function*, Bulletin AMS, 1922 (retraction; first lower bound $>10^{37}$) — foundational. [high-confidence]
3. P. Erdős, *On the function $\varphi(n)$* (multiplicity remarks), 1935 — foundational. [needs-verification]
4. V. Klee, *On a conjecture of Carmichael*, 1947 (finite criterion) — breakthrough. [high-confidence]
5. A. Schinzel & W. Sierpiński, *Sur l'équation $\varphi(x)=m$*, 1959 — modern. [needs-verification]
6. P. T. Bateman, *On the multiplicity of Euler's totient*, 1963 — modern. [needs-verification]
7. C. Pomerance, *On Carmichael's conjecture*, 1974 (structural constraint $p^2\mid m$) — breakthrough. [high-confidence]
8. C. Pomerance, *Popular values of Euler's function*, 1980 — modern. [needs-verification]
9. A. Schlafly & S. Wagon, *Carmichael's conjecture on the Euler function is valid below $10^{10^{7}}$*, 1994 — computational. [high-confidence]
10. W. R. Alford, A. Granville & C. Pomerance, *There are infinitely many Carmichael numbers*, 1994 — modern. [high-confidence]
11. K. Ford, *The distribution of totients*, Annals of Mathematics, 1998 — breakthrough. [high-confidence]
12. K. Ford, *The number of solutions of $\varphi(x)=m$*, 1998 — breakthrough. [high-confidence]
13. R. K. Guy, *Unsolved Problems in Number Theory* (§B36–B39), 1999 — survey. [high-confidence]
14. Ford, Konyagin & Luca, *Multiplicative structure of values of the Euler function*, 2008 — modern. [needs-verification]
15. Ford, Luca & Pomerance, *The image of Carmichael's $\lambda$-function and totient relations*, 2014 — modern. [needs-verification]

## AI Review Panel

### Claude (Anthropic) — in-house review

The survey is accurate to its dossier and well-proportioned. Its strengths: it cleanly isolates the single load-bearing difficulty (worst-case uniformity versus average control), it correctly separates the *proven* companion result (Sierpiński's $k\geq 2$, Ford 1998) from the *open* Carmichael case ($k=1$), and it resists the most common overstatement — treating astronomical computational bounds as a proof. The history of Carmichael's own 1907/1922 proof-and-retraction is handled responsibly and used to inoculate against the recurring informal-proof error.

I flag three things for a human reviewer. (i) The references carry explicit verification flags, and several load-bearing ones (the lower-bound chronology, the precise thresholds $10^{10^{7}}$ and $10^{10^{10}}$, and the attribution and dating of Pomerance 1974 and Ford 1998) are reproduced from the dossier without primary-source confirmation; no DOIs are asserted, and they should be checked against MathSciNet/zbMATH and the journals' archives. (ii) The narrative leans heavily on a small canonical core — Klee, Pomerance, and especially Ford — so the framing risks single-source reliance on Ford's 1998 work for the entire "state of the art"; an independent reading of Ford's paper is the natural cross-check. (iii) The single most important thing to verify is the exact statement and the precise numerical lower bound currently certified for the least counterexample, since the dossier itself hedges ("beyond $10^{10^{10}}$", "later refinements pushed further still") and these figures are the most quotable and most error-prone claims in the document.

A minor caution: the phrase "an event of effectively zero probability" (heuristic) should be read as informal, not as a probabilistic theorem. None of these flags indicates an error I can identify; they indicate where confidence rests on unverified secondary description rather than checked primary sources.

**Verdict:** accept-with-revisions.

### GPT (OpenAI) — pending
_Not yet run. To complete the panel, run the prompt in docs/review/REVIEW-TEMPLATE.md through GPT and record the verdict here and in the front matter._

### Gemini (Google) — pending
_Not yet run. See docs/review/REVIEW-TEMPLATE.md._

### Grok (xAI) — pending
_Not yet run. See docs/review/REVIEW-TEMPLATE.md._

## Human verification

This AI review is not a substitute for human peer review. It is offered to assist academic verification per ../docs/review/ACADEMIC-REVIEW.md: an expert should confirm the problem statement, the chronology and exact values of the computational lower bounds, the statements and attributions of Klee (1947), Pomerance (1974), and Ford (1998), and every reference flagged `needs-verification` against primary sources. Status: human_review pending.

---
*Accredited to **Alexander Donahue** · The Unsolved Mathematics Atlas · CC BY 4.0. Cite per CITATION.cff.*

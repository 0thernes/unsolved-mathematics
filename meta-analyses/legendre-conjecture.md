---
title: "Meta-Analysis: Legendre's Conjecture"
slug: legendre-conjecture
author: Alexander Donahue
type: ai-assisted-meta-analysis
peer_reviewed: false
problem_status: open
ai_review:
  claude:
    verdict: accept-with-revisions
    date: "2026-06-14"
    version: "claude-opus-4-8"
    summary: "A careful, well-calibrated survey of a genuinely open Landau problem that correctly identifies the 0.525-to-0.5 exponent gap and the RH log-factor deficit as the real barriers, but whose references must be source-checked before citation."
  gpt:
    verdict: pending
  gemini:
    verdict: pending
  grok:
    verdict: pending
human_review: pending
---

# Meta-Analysis: Legendre's Conjecture

> **AI-generated meta-analysis — not peer-reviewed.** Curated and accredited by **Alexander Donahue** (human-in-the-loop). A survey/assessment of an open problem; it makes no claim of a new result. Citations carry verification flags and require human source-checking.

## Abstract

Legendre's conjecture asserts that for every positive integer $n$ there is a prime $p$ with $n^2 < p < (n+1)^2$ — equivalently, that the maximal prime gap below $X$ is $O(\sqrt{X})$. Stated around 1808 and canonized in 1912 as one of Edmund Landau's four "unattackable" prime problems, it remains open. Heuristically the claim is overwhelming: the prime number theorem predicts $\sim n/\log n$ primes per square-interval, and direct computation confirms a prime in every interval far past $n=10^9$. The obstacle is uniformity. The strongest unconditional short-interval theorem (Baker–Harman–Pintz, 2001) places a prime in $(x, x+x^{0.525})$ for large $x$, missing the required exponent $0.5$ by $0.025$. Strikingly, even the Riemann Hypothesis does not suffice: it yields gaps $O(\sqrt{x}\log x)$, short by one logarithmic factor. This meta-analysis synthesizes the dossier's account of the state of the art, the principal lines of attack (zero-density estimates, sieves, conditional bounds, small-gap technology, computation) and their named barriers, and offers a skeptical critical assessment of how far the frontier truly sits.

## 1. Statement and significance

The conjecture is elementary to state: each open interval between consecutive perfect squares contains at least a prime. Because $(n+1)^2 - n^2 = 2n+1$, it is a statement about prime gaps at square-root spacing — a near-equivalent form is $p_{k+1}-p_k < (2+o(1))\sqrt{p_k}$, i.e. uniformly $O(\sqrt{p_k})$ gaps. It sits inside a clear hierarchy: it is stronger than the Bertrand–Chebyshev postulate (a prime between $m$ and $2m$) and is implied by Oppermann's, Andrica's, and Brocard's conjectures, as well as by the Cramér heuristic. Its significance is that it is the cleanest unresolved benchmark for our ability to locate primes in genuinely short windows; progress on it is essentially progress on the distribution of primes in intervals of length $x^{1/2}$.

## 2. State of the art

**Unconditional.** The benchmark is Baker–Harman–Pintz (2001): for all sufficiently large $x$ there is a prime in $(x, x+x^{0.525})$. Applied at $x=n^2$ this gives a prime in $(n^2, n^2+n^{1.05})$, whereas Legendre demands one already in $(n^2, n^2+2n+1)$, an interval of length $\Theta(x^{0.5})$. The lineage behind this record is well documented: Hoheisel's first nontrivial exponent $1-1/33000$ (1930), Ingham's deduction of a prime between consecutive cubes via zero-density estimates (1937), and Huxley's durable $7/12 \approx 0.583$ (1972/1979). The Guth–Maynard (2024) improvement to large-value/Dirichlet-polynomial bounds sharpens related zero-density exponents but does not move the Legendre-relevant constant to $1/2$.

**Conditional.** Under the Riemann Hypothesis, Cramér's bound gives $p_{k+1}-p_k = O(\sqrt{p_k}\log p_k)$ — insufficient, because the extra $\log$ factor does not exclude an empty square-interval. RH does yield (Selberg, conditional) that *almost all* intervals $(n^2,(n+1)^2)$ contain a prime, but a sparse exceptional set survives. Stronger statements — the Cramér probabilistic model ($O((\log p)^2)$ gaps), the Hardy–Littlewood $k$-tuple conjecture, Montgomery's pair-correlation conjecture, and Oppermann's/Andrica's conjectures — each comfortably imply Legendre, but none is proved. The conjecture is universally believed true; the entire difficulty is the *every-$n$, no-exceptions* clause.

## 3. Principal approaches and barriers

- **Zero-density estimates (classical short-interval program).** Via Perron's formula, primes in $(x,x+y)$ are governed by zeros of $\zeta(s)$; density theorems $N(\sigma,T)\ll T^{A(\sigma)(1-\sigma)+\varepsilon}$ bound the aggregate near-critical-line contribution. This produces the $0.525$ record. **Barrier:** reaching exponent $1/2$ with the needed uniformity appears to require RH *and more* — even on RH a $\log x$ factor remains, and no known density argument removes it.
- **Sieve methods.** Harman's sieve and Chen-type bilinear decompositions of $\Lambda$ underpin the $0.525$ constant. **Barrier:** the **parity problem** (Selberg) — a sieve alone cannot separate integers with an even versus odd number of prime factors, so it cannot detect primes unaided at the $x^{1/2}$ scale without external arithmetic input.
- **Conditional (RH and beyond).** Assuming strong hypotheses sharpens the statistics, but the **RH log-deficit** is genuine: Legendre is *not* a formal consequence of RH, so even settling RH would leave it open.
- **Small-gap technology (GPY / Zhang / Maynard–Tao / Polymath8).** Spectacular for *bounded* gaps ($\le 246$ infinitely often). **Barrier:** Legendre concerns the rare *large*-gap regime and demands a prime in *every* window — an essentially orthogonal target.
- **Computation.** Verified well past $n=10^9$; observed maximal gaps stay far under $\sqrt{x}$. **Barrier:** computation cannot prove a universal statement, only guard against a small counterexample.

## 4. Critical assessment

What is solid here is the framing. The dossier correctly identifies the two precise quantitative deficits that make the problem hard — the $0.525$-versus-$0.5$ exponent gap and the one-logarithm shortfall under RH — and does not overstate either. The clean separation between "believed true" (heuristics, computation, almost-all results) and "proved for every $n$" (nothing) is exactly right, and the treatment of why the small-gaps revolution does *not* transfer is honest rather than hopeful. The parity barrier and the zero-density bottleneck are named as the genuine obstructions, which is the correct diagnosis.

What is speculative — and the survey says so — is any near-term route to $1/2$. The claim that the residual $0.025$ is "exactly the unbridged chasm" is a fair characterization, but a reader should understand it is a heuristic statement about the limits of current methods, not a theorem that $0.5$ is unreachable. The frontier is, realistically, far: there is no known argument that converts even a proof of RH into Legendre, so the problem is in a real sense *harder than RH plus epsilon*. The Guth–Maynard mention is appropriately hedged; it would be a mistake to read it as materially closer to Legendre.

The principal weakness of the dossier is bibliographic, not mathematical: a majority of the key-paper entries carry `needs-verification`, and several share near-identical titles ("the difference between consecutive primes") across different authors and decades, which is a real conflation risk.

## 5. What a resolution would require / open directions

A proof must guarantee $\pi(x+y)-\pi(x)\ge 1$ for $y\asymp\sqrt{x}$ uniformly in $x$, with no exceptional set — pushing the admissible short-interval exponent from $0.525$ past $0.5$. Because RH alone leaves a $\log$ factor, a successful argument must either (i) prove RH *and* extract the missing logarithm through additional structure (strong pair-correlation, twin-prime-type arithmetic input), or (ii) introduce a genuinely new short-interval method that bypasses the zero-density bottleneck. The parity barrier forbids pure sieves from reaching primes at this scale, so new arithmetic input is essential. The most credible near-term direction is continued improvement of zero-density estimates for $\zeta(s)$ (the Guth–Maynard line); the longer-term resolution is widely expected to arrive only alongside deep progress toward RH and finer correlation information, likely as a by-product rather than a targeted assault.

## 6. Selected references

- Legendre, A.-M. (1808). *Essai sur la théorie des nombres* (2e éd.). [high-confidence]
- Chebyshev, P. L. (1850). Mémoire sur les nombres premiers (proof of Bertrand's postulate). [high-confidence]
- Hadamard, J. (1896). Sur la distribution des zéros de la fonction $\zeta(s)$. [high-confidence]
- de la Vallée Poussin, C.-J. (1896). Recherches analytiques sur la théorie des nombres premiers. [high-confidence]
- Landau, E. (1912). Gelöste und ungelöste Probleme aus der Theorie der Primzahlverteilung (ICM Cambridge). [high-confidence]
- Hoheisel, G. (1930). Primzahlprobleme in der Analysis. [high-confidence]
- Cramér, H. (1936). On the order of magnitude of the difference between consecutive prime numbers. [high-confidence]
- Ingham, A. E. (1937). On the difference between consecutive primes. DOI 10.1093/qmath/os-8.1.255. [needs-verification]
- Selberg, A. (1943). On the normal density of primes in small intervals. [needs-verification]
- Montgomery, H. L. (1972). *Topics in Multiplicative Number Theory*. DOI 10.1007/BFb0060851. [needs-verification]
- Huxley, M. N. (1972). The difference between consecutive primes. [needs-verification]
- Heath-Brown, D. R., & Iwaniec, H. (1980). The difference between consecutive primes, II. DOI 10.1112/blms/12.6.449. [needs-verification]
- Baker, R. C., Harman, G., & Pintz, J. (2001). The difference between consecutive primes, II. DOI 10.1112/plms/83.3.532. [high-confidence]
- Goldston, D., Pintz, J., & Yıldırım, C. (2009). Primes in tuples I. DOI 10.4007/annals.2009.170.819. [high-confidence]
- Maynard, J. (2015). Small gaps between primes. DOI 10.4007/annals.2015.181.1.7. [high-confidence]
- Guth, L., & Maynard, J. (2024). New large value estimates for Dirichlet polynomials. DOI 10.48550/arXiv.2405.20552. [needs-verification]

## AI Review Panel

### Claude (Anthropic) — in-house review

This is a strong, appropriately humble survey of a problem that invites overreach. Its central virtue is quantitative honesty: it pins down that the unconditional record sits at exponent $0.525$ against a required $0.5$, and — the point most amateur treatments miss — that the Riemann Hypothesis itself falls one $\log$ factor short, so Legendre does not follow even from RH. The hierarchy placement (stronger than Bertrand, implied by Oppermann/Andrica/Cramér) is correct and load-bearing, and the explanation of why bounded-gap technology is orthogonal to a large-gap, every-window demand is exactly the right caution. I see no place where the survey claims more than the literature supports.

My concrete reservations are three. First, the references: a clear majority of the key-paper entries are flagged `needs-verification`, and the dossier itself warns that the recurring "difference between consecutive primes" title is shared across Ingham, Erdős, Huxley, Heath-Brown–Iwaniec, and Baker–Harman so the exact title/year/DOI of entries like Ingham (1937), Huxley (1972), and Heath-Brown–Iwaniec (1980) must be confirmed against MathSciNet or zbMATH before any citation is trusted. Second, the survey leans heavily on the single Baker–Harman–Pintz (2001) result as *the* unconditional frontier; that is defensible since it is the standing record, but a reviewer should confirm no incremental improvement to the short-interval exponent has appeared since, particularly in the wake of Guth–Maynard (2024). Third, the characterization of the $0.025$ gap as the "unbridged chasm" is rhetorically apt but should be read as a statement about method limits, not an impossibility theorem.

The single most important thing a human reviewer should verify is the precise current status of the best unconditional short-interval exponent and whether any post-2024 work (Guth–Maynard or its successors) has nudged the Legendre-relevant constant below $0.525$ — the entire "how far is the frontier" assessment turns on that number.

**Verdict:** accept-with-revisions.

### GPT (OpenAI) — pending

_Not yet run. To complete the panel, run the prompt in docs/review/REVIEW-TEMPLATE.md through GPT and record the verdict here and in the front matter._

### Gemini (Google) — pending

_Not yet run. See docs/review/REVIEW-TEMPLATE.md._

### Grok (xAI) — pending

_Not yet run. See docs/review/REVIEW-TEMPLATE.md._

## Human verification

AI review is not human peer review. The Claude panel above is a machine-generated referee pass and may miss errors a domain expert would catch, especially in bibliographic detail. This meta-analysis is offered for academic verification per ../docs/review/ACADEMIC-REVIEW.md, and every reference flagged `needs-verification` must be checked against a primary bibliographic source before being relied upon. Status: human_review pending.

---
*Accredited to **Alexander Donahue** · The Unsolved Mathematics Atlas · CC BY 4.0. Cite per CITATION.cff.*

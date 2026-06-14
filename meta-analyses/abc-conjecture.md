---
title: "Meta-Analysis: The abc Conjecture"
slug: abc-conjecture
author: Alexander Donahue
type: ai-assisted-meta-analysis
peer_reviewed: false
problem_status: disputed-claim
ai_review:
  claude:
    verdict: accept-with-revisions
    date: "2026-06-14"
    version: "claude-opus-4-8"
    summary: "A faithful, well-structured survey that correctly frames abc as open with a disputed IUT claim, but its reference apparatus carries verification flags and the IUT episode leans heavily on a small set of sources."
  gpt:
    verdict: pending
  gemini:
    verdict: pending
  grok:
    verdict: pending
human_review: pending
---

# Meta-Analysis: The abc Conjecture

> **AI-generated meta-analysis — not peer-reviewed.** Curated and accredited by **Alexander Donahue** (human-in-the-loop). A survey/assessment of an open problem; it makes no claim of a new result. Citations carry verification flags and require human source-checking.

## Abstract

The abc conjecture (Masser–Oesterlé, 1985) asserts that for coprime positive integers with $a+b=c$, one has $c < K_\varepsilon\,\mathrm{rad}(abc)^{1+\varepsilon}$ for every $\varepsilon>0$, where $\mathrm{rad}$ is the product of distinct primes dividing its argument. It is the integer shadow of the unconditional Mason–Stothers theorem for polynomials and, via Vojta, of the Second Main Theorem of value-distribution theory. Its centrality is exceptional: it implies, often immediately, asymptotic Fermat, effective Mordell, effective Roth, infinitude of non-Wieferich primes, and more. This meta-analysis synthesizes the dossier on abc's history, the unconditional frontier (Stewart–Yu's exponentially weak $\log c \ll \mathrm{rad}(abc)^{1/3+\varepsilon}$), the principal approaches and their structural barriers, and the central controversy: Shinichi Mochizuki's 2012 Inter-universal Teichmüller theory (IUT) claim, whose load-bearing Corollary 3.12 was challenged by Scholze–Stix (2018) and remains unverified by the mainstream community. The institute's status of **disputed-claim** is assessed and endorsed: abc is regarded as open, with a prominent, unresolved proof claim.

## 1. Statement and significance

For coprime positive integers $a,b,c$ with $a+b=c$, define the radical $\mathrm{rad}(abc)=\prod_{p\mid abc}p$. The conjecture states that for every $\varepsilon>0$ there is a constant $K_\varepsilon$ with $c < K_\varepsilon\,\mathrm{rad}(abc)^{1+\varepsilon}$ for all such triples; equivalently, the quality $q(a,b,c)=\log c/\log\mathrm{rad}(abc)$ exceeds $1+\varepsilon$ only finitely often. The $\varepsilon$ is essential — infinitely many triples have $q>1$ (e.g. families exploiting $2^{6n}\equiv 1\pmod 9$), so the $\varepsilon=0$ statement is provably false.

The conjecture's significance lies in its reach rather than its statement, which a strong undergraduate can grasp. It "linearizes" a swath of Diophantine geometry: hard finiteness theorems become near-corollaries. The dossier records the standard list of consequences — asymptotic Fermat, effective Mordell/Faltings (Elkies, 1988), Roth's theorem with effective constants, infinitude of non-Wieferich primes, Erdős–Woods, Granville–Langevin, and constraints on Brocard–Ramanujan-type equations. It is essentially equivalent to a uniform Szpiro inequality $|\Delta_E| \ll N_E^{6+\varepsilon}$ for elliptic curves (via the Frey curve) and is a special case of Vojta's height conjectures.

## 2. State of the art

**Unconditional.** The strongest unconditional result is Stewart–Yu (1991; sharpened 2001): $\log c \ll_\varepsilon \mathrm{rad}(abc)^{1/3+\varepsilon}$, obtained through $p$-adic linear forms in logarithms (Baker's method, with Yu's $p$-adic theory). This is *exponentially* weaker than the conjectured $\log c \le (1+\varepsilon)\log\mathrm{rad}(abc)+O(1)$; the gap is structural, not a matter of constants. Computationally, abc is verified for all triples below large bounds (ABC@home, Reken mee met ABC), and the record extremal triple has quality only $q\approx 1.6299$, namely $2 + 3^{10}\cdot 109 = 23^5$ — consistent with the conjecture but proving nothing about the infinitely many large triples that matter.

**Conditional and by analogy.** The function-field analogue (Mason–Stothers, 1981/84) and the holomorphic/Nevanlinna analogue are complete theorems. They establish the conjecture's "moral truth" and isolate the missing ingredient: an integer analogue of the derivative/Wronskian used in those proofs. abc is equivalent to uniform Szpiro and a special case of Vojta's conjectures, both of which are at least as hard.

**Disputed claim.** Mochizuki's IUT (four papers, ~500 pages, 2012; published in *Publications of the RIMS*, 2020/21) claims a Szpiro-type inequality yielding abc with effective constants. It has not achieved independent verification; the institute classifies the problem as **disputed-claim** to capture a high-profile claim coexisting with a mainstream view that abc remains open.

## 3. Principal approaches and barriers

- **Baker's method (linear forms in logarithms).** The only source of unconditional progress (Stewart–Yu). *Barrier:* intrinsically exponential — it bounds $\log c$ by a *power* of $\mathrm{rad}(abc)$ and cannot, even in principle, reach a polynomial-in-$\log$ bound. This is a hard ceiling on the technique.
- **Frey curve / Szpiro reduction.** abc is exactly equivalent to uniform Szpiro; modularity (Wiles; Taylor–Wiles; BCDT) makes the elliptic-curve side systematic. *Barrier:* nothing in the modularity toolkit produces the required *uniformity* over all curves; the difficulty is merely re-encoded.
- **Vojta's conjectures / Nevanlinna dictionary.** Recasts the radical as a truncated counting function and abc as an arithmetic Second Main Theorem. *Barrier:* the arithmetic case lacks a derivative; the Wronskian/logarithmic-derivative step of the function-field and holomorphic proofs has no integer counterpart. Vojta's full conjecture is strictly harder.
- **Inter-universal Teichmüller theory (Mochizuki).** Deforms the additive/multiplicative structures of a number field across "universes," tracking distortion via Hodge theaters, theta-links, and a multiradial algorithm; the claimed payoff is Corollary 3.12 of IUT III. *Barrier / dispute:* Scholze–Stix (2018) argue the central inequality is unjustified — that identifications relating the deformed copies cause the claimed quantitative gain to collapse to a triviality. Mochizuki rejects this, asserting they conflate copies IUT must keep distinct. The objection stands unanswered to the community's satisfaction; this is a genuine open dispute, not a settled refutation.
- **Heuristics and computation.** Robert–Stewart–Tenenbaum predict the precise extremal shape; ABC@home and successors supply data and record triples. *Barrier:* no finite verification constrains the infinite tail.

## 4. Critical assessment

What is solid: the unconditional Stewart–Yu bound and its exponential distance from the target; the exactness of the Szpiro equivalence and the Elkies implication; the completeness of the function-field and holomorphic analogues; and the precise diagnosis that the integer case lacks a derivative. These are not in serious dispute and the dossier reports them accurately.

What is speculative or contested: the entire IUT claim. The honest reading is that the proof has not been independently verified, that its load-bearing step (Corollary 3.12) is the subject of a specific, documented objection, and that publication within Mochizuki's home institute and journal did not supply the external validation the community expects. The dossier's framing — claim, not fact — is the correct neutral posture. It is worth stressing that "disputed-claim" is not a verdict that IUT is wrong; it records that the claim is neither verified nor refuted to consensus.

How far is the frontier? Very far, and the distance is qualitative. No incremental sharpening of Baker's method can reach a polynomial-in-$\log$ bound; the function-field proof cannot be transplanted without an arithmetic derivative. Absent IUT's vindication, there is no second candidate proof in hand — only programs (e.g. Joshi's arithmetic-Teichmüller spaces) that aim to reconstruct or supersede the machinery. The conjecture should be read as genuinely open, with the unusual feature that its most prominent attack is simultaneously the most complete and the least assimilable.

## 5. What a resolution would require / open directions

A genuine resolution must produce a bound $\log c \le (1+\varepsilon)\log\mathrm{rad}(abc) + C_\varepsilon$ for all but finitely many triples — polynomial-in-log control with explicit $\varepsilon$-dependence. Two live routes are identified. (i) **Rehabilitate or refute IUT**: make Corollary 3.12 rigorous and quantitatively non-trivial against the Scholze–Stix reading, or show it definitively fails. Either outcome would be decisive, and both require an independently checkable reformulation of the contested inequality. (ii) **Supply the missing arithmetic mechanism**: an integer analogue of the derivative/Wronskian, whether through arithmetic-Teichmüller spaces, $p$-adic Hodge-theoretic comparison, or an as-yet-unknown construction. A subordinate but valuable direction is continued sharpening of unconditional bounds and extremal-triple search — not a path to proof, but a constraint on any purported counterexample and a testbed for heuristics like Robert–Stewart–Tenenbaum.

## 6. Selected references

1. R. C. Mason, *Diophantine Equations over Function Fields* (1984) — function-field analogue. [high-confidence]
2. W. W. Stothers, polynomial degree inequality (1981) — predecessor of Mason–Stothers. [needs-verification]
3. L. Szpiro, *Discriminant et conducteur des courbes elliptiques* (1983) — the equivalent Szpiro conjecture. [needs-verification]
4. D. Masser, *Open problems* (Cambridge, 1985) — statement in standard $\mathrm{rad}(abc)^{1+\varepsilon}$ form. [needs-verification]
5. J. Oesterlé, *Nouvelles approches du "théorème" de Fermat*, Sém. Bourbaki 694 (1988). [high-confidence]
6. N. D. Elkies, *ABC implies Mordell* (1988), DOI:10.1155/S1073792891000144. [high-confidence]
7. P. Vojta, *Diophantine Approximations and Value Distribution Theory*, LNM 1239 (1987). [high-confidence]
8. C. L. Stewart & K. Yu, *On the abc conjecture* (1991), DOI:10.1007/BF01459803. [high-confidence]
9. C. L. Stewart & K. Yu, *On the abc conjecture, II* (2001), DOI:10.1215/S0012-7094-01-10815-6. [high-confidence]
10. A. Granville & T. J. Tucker, *It's As Easy As abc* (2002), expository. [high-confidence]
11. S. Mochizuki, *Inter-universal Teichmüller Theory I–IV* (2012) — listed as documents; status disputed. [high-confidence]
12. O. Robert, C. L. Stewart & G. Tenenbaum, *Lower bounds for the greatest quality of abc triples* (2014), DOI:10.1112/S0025579314000035. [needs-verification]
13. P. Scholze & J. Stix, *Why abc is still a conjecture* (2018) — report on Corollary 3.12. [high-confidence]
14. K. Joshi, *Construction of Arithmetic Teichmüller Spaces and applications* (2021). [needs-verification]
15. M. Waldschmidt, *Lectures on the abc Conjecture / consequences* (2009), survey. [needs-verification]

## AI Review Panel

### Claude (Anthropic) — in-house review

This survey is faithful to the dossier and, more importantly, faithful to the actual epistemic situation: it consistently presents abc as open and IUT as a claim, never as a result. The structural diagnosis is the survey's strongest feature — it correctly identifies that the unconditional gap is exponential rather than constant-factor, and that the function-field/holomorphic proofs fail to transplant precisely because the integers lack a derivative. The decision to treat "disputed-claim" as recording non-consensus (neither verified nor refuted) rather than as a verdict against IUT is the right call and is stated cleanly.

Three concrete reservations. (i) The references carry explicit verification flags, and several are real concerns: items #2, #3, #4, #12, #14, and #15 are marked needs-verification, and the dossier separately flags two entries (its #9, #14) as "ai-suggested" leads whose existence/attribution could not be confirmed — I excluded those from the reference list here, but a human must still confirm the surviving DOIs against primary sources (especially the Elkies and Stewart–Yu identifiers) before any citation is trusted. (ii) The IUT episode leans heavily on a narrow source base — essentially the Scholze–Stix report and Mochizuki's rebuttals as relayed by the dossier. The characterization of Corollary 3.12 as "collapsing to a triviality" is Scholze–Stix's reading; it should be attributed as such (the survey does) and not hardened into settled fact. A reviewer should independently consult both the Scholze–Stix manuscript and Mochizuki's responses rather than accept the dossier's paraphrase.

(iii) The single most important thing a human reviewer should verify: that the record extremal triple and quality figure ($q\approx 1.6299$ for $2 + 3^{10}\cdot 109 = 23^5$) and the Stewart–Yu exponent ($1/3+\varepsilon$) are stated correctly and current — these are the two load-bearing quantitative claims, and an error in either would distort the "how far is the frontier" assessment. I found no claim in the document that overstates progress or asserts a resolution, and no hype; the risk is in citation accuracy, not in framing.

**Verdict:** accept-with-revisions.

### GPT (OpenAI) — pending
_Not yet run. To complete the panel, run the prompt in docs/review/REVIEW-TEMPLATE.md through GPT and record the verdict here and in the front matter._

### Gemini (Google) — pending
_Not yet run. See docs/review/REVIEW-TEMPLATE.md._

### Grok (xAI) — pending
_Not yet run. See docs/review/REVIEW-TEMPLATE.md._

## Human verification

AI review is not human peer review. This meta-analysis is offered for academic verification per ../docs/review/ACADEMIC-REVIEW.md; the AI panel above is an aid to, not a substitute for, expert scrutiny of the sources, the quantitative claims, and the contested IUT step. Status: human_review pending.

---
*Accredited to **Alexander Donahue** · The Unsolved Mathematics Atlas · CC BY 4.0. Cite per CITATION.cff.*

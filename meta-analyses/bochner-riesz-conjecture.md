---
title: "Meta-Analysis: The Bochner–Riesz Conjecture"
slug: bochner-riesz-conjecture
author: Alexander Donahue
type: ai-assisted-meta-analysis
peer_reviewed: false
problem_status: active-progress
ai_review:
  claude:
    verdict: accept-with-revisions
    date: "2026-06-14"
    version: "claude-opus-4-8"
    summary: "A faithful and well-calibrated survey of an open problem; technically accurate on the n=2/n≥3 split and the restriction–Kakeya hierarchy, but its citation strings need primary-source verification."
  gpt:
    verdict: pending
  gemini:
    verdict: pending
  grok:
    verdict: pending
human_review: pending
---

# Meta-Analysis: The Bochner–Riesz Conjecture

> **AI-generated meta-analysis — not peer-reviewed.** Curated and accredited by **Alexander Donahue** (human-in-the-loop). A survey/assessment of an open problem; it makes no claim of a new result. Citations carry verification flags and require human source-checking.

## Abstract

The Bochner–Riesz conjecture concerns the $L^p(\mathbb{R}^n)$ convergence of the Bochner–Riesz means $\widehat{S^\delta_R f}(\xi) = (1 - |\xi|^2/R^2)_+^{\delta}\,\widehat{f}(\xi)$ as $R \to \infty$. It asserts that uniform $L^p$ boundedness holds precisely when $\delta > \delta(p) := \max\{ n|1/p - 1/2| - 1/2,\, 0\}$, the threshold known to be necessary. Posed implicitly by Bochner in 1936 on the foundation of Marcel Riesz's typical means, the conjecture became the organizing hub of a hierarchy: the Fourier restriction conjecture implies it, and it in turn implies the Kakeya maximal conjecture. This meta-analysis surveys the dossier's account of the problem: the complete planar resolution (Carleson–Sjölin, 1972), the unconditional Stein–Tomas baseline, and the bilinear, multilinear, decoupling, and polynomial-partitioning advances that have steadily enlarged the admissible range in dimensions $n \ge 3$ without reaching $\delta(p)$. It assesses the principal barriers — chiefly the lossy descent from multilinear/local estimates to sharp linear ones and the irreducible Kakeya obstruction — and states what a full resolution would require. The problem remains open for every $n \ge 3$.

## 1. Statement and significance

For $f$ on $\mathbb{R}^n$ and $\delta \ge 0$, the Bochner–Riesz mean of order $\delta$ multiplies $\widehat{f}$ by the radial profile $(1-|\xi|^2/R^2)_+^{\delta}$. At $\delta = 0$ this is the ball (disc) multiplier, which Fefferman (1971) proved unbounded on $L^p(\mathbb{R}^n)$ for $n \ge 2$, $p \ne 2$; positive $\delta$ smooths the cutoff. The conjecture is that $S^\delta_R$ is uniformly $L^p$-bounded — equivalently, that $S^\delta_R f \to f$ in $L^p$ — exactly when $\delta > \delta(p)$. The threshold $\delta(p)$ is established as necessary by test functions concentrated near the sphere (Herz 1954; later Christ, Tao), so the live question is sufficiency.

Significance derives from position. The operator is, after rescaling, an oscillatory-integral operator whose kernel concentrates on the sphere $|\xi| = R$, and its analysis is governed by the geometry of wave packets adapted to that sphere. Within Stein's restriction program the implications run **Restriction $\Rightarrow$ Bochner–Riesz $\Rightarrow$ Kakeya** (maximal/set bound). The conjecture thus sits between two of the deepest open problems in modern harmonic analysis and connects outward to local smoothing, the cone multiplier, and decoupling.

## 2. State of the art

**Solved in the plane.** Carleson–Sjölin (1972) settled $n=2$ completely: $S^\delta_R$ is $L^p(\mathbb{R}^2)$-bounded for all $\delta > \delta(p)$. Independent proofs followed (Fefferman 1973; Córdoba 1977), and Hörmander placed the result in a general oscillatory-integral (Carleson–Sjölin–Hörmander) class. This is the only full-dimensional resolution.

**Unconditional in higher dimensions, but partial.** The Stein–Tomas $L^2$ restriction theorem (Tomas 1975, endpoint by Stein) yields Bochner–Riesz on a restricted range up to the Stein–Tomas exponent $p = 2(n+1)/(n-1)$ in all $n$. Beyond this baseline, the admissible range for $n \ge 3$ has been progressively enlarged by the bilinear method (Tao–Vargas–Vega 1998; Wolff 2001; Tao 2003; Lee 2004), the multilinear method (Bennett–Carbery–Tao 2006 combined with Bourgain–Guth 2011), and the decoupling theorem (Bourgain–Demeter 2015) together with polynomial partitioning (Guth 2016–2018; Guth–Hickman–Iliopoulou 2019). Each record range falls strictly short of $\delta(p)$ for the full $p$.

**Conditional.** A proof of the restriction conjecture in dimension $n$ would settle Bochner–Riesz in dimension $n$, via $\epsilon$-removal and Littlewood–Paley. The dossier records no community-accepted full proof for any $n \ge 3$ and no notable retracted publication; the threshold $\delta(p)$ is not in dispute.

## 3. Principal approaches and barriers

- **Square functions ($n=2$).** Decompose the multiplier into arc-localized pieces and control the sum by an $L^p$ square function; Córdoba's sharp $L^4$ Kakeya-maximal estimate exploits that two non-parallel tubes in $\mathbb{R}^2$ meet in essentially one parallelogram. *Barrier:* in $n \ge 3$ multiple tubes can be coplanar, and the clean two-tube/$L^4$ geometry has no analogue.
- **Restriction–extension duality.** Restriction is formally stronger and implies Bochner–Riesz at matching exponents. *Barrier:* restriction is itself open for all $n \ge 3$ and believed comparable in strength, so this route cannot beat the restriction frontier.
- **Bilinear / multilinear estimates.** Transversality between separated caps yields gains over linear estimates; multilinear restriction plus induction-on-scales gave the records that stood for a decade. *Barrier:* converting $k$-linear gains to the linear estimate loses a dimension-dependent amount, leaving a gap to $\delta(p)$.
- **Polynomial partitioning + decoupling.** The two structural advances of the last decade; near-sharp control of cap-localized square-sums and algebraic organization of wave packets. *Barrier:* decoupling loses the $\epsilon$-room at the *critical* exponent, and polynomial partitioning has not fully captured the lower-dimensional concentration of extremizers.
- **Kakeya-maximal obstruction (negative side).** Bochner–Riesz implies the Kakeya maximal conjecture, so it is at least as hard as Kakeya — open for $n \ge 3$. This pins $\delta(p)$ as sharp but marks a hard floor.

## 4. Critical assessment

The dossier's central claims are internally consistent and align with the standard expert picture: $n=2$ solved, $n \ge 3$ open, threshold sharp, restriction above and Kakeya below. The framing of the recurring obstruction — the lossy multilinear-to-linear descent and the irreducible Kakeya packing problem — is the correct diagnosis of why the records stall short of $\delta(p)$. The "attempts" record is appropriately sober: it notes that periodic preprints claiming the full conjecture circulate and that experts typically locate the error in an unjustified passage from a multilinear/local estimate to the sharp linear one, or in an implicit Kakeya assumption.

Two cautions. First, the field moves quickly at its Kakeya/restriction base — recent incidence-geometry work (Katz–Zahl; Wang and collaborators) cited in the dossier as feeding the hierarchy may have shifted what is currently "best," so any specific record range should be treated as a snapshot, not a fixed fact. Second, the dossier's own caveat that improvements at the base do not automatically yield the endpoint at the critical exponent is essential and correctly stated.

## 5. What a resolution would require / open directions

A proof for $n \ge 3$ must control the worst-case overlap of $\sim R^{(n-1)/2}$ tubes pointing in distinct directions *at the critical exponent*, without the $\epsilon$-loss that decoupling and multilinear methods incur. Per the dossier this means one of: (i) a proof of the restriction conjecture, transferred down; (ii) a sharp *linear* (not merely multilinear or local) estimate recovering the endpoint; or (iii) a new lossless mechanism converting known multilinear/polynomial-partitioning gains into the linear bound. The plausible routes named are the Guth–Hickman–Iliopoulou polynomial-partitioning lineage (closing the multilinear-to-linear gap), a restriction-first strategy, and Kakeya-driven incidence estimates feeding back up the hierarchy — the last necessary but not known to be sufficient alone.

## 6. Selected references

1. Salomon Bochner (1936), *Summation of multiple Fourier series by spherical means* — foundational [high-confidence]
2. Elias M. Stein (1954), *Interpolation of linear operators* — foundational [high-confidence]
3. Carl S. Herz (1954), *On the mean inversion of Fourier and Hankel transforms* — foundational [needs-verification]
4. Charles Fefferman (1971), *The multiplier problem for the ball* — breakthrough [high-confidence]
5. Lennart Carleson, Per Sjölin (1972), *The disc multiplier (planar Bochner–Riesz / Carleson–Sjölin theorem)* — breakthrough [high-confidence]
6. Peter A. Tomas (1975), *A restriction theorem for the Fourier transform* — foundational [high-confidence]
7. Antonio Córdoba (1977), *A note on the Kakeya maximal function and Bochner–Riesz* — breakthrough [needs-verification]
8. Jean Bourgain (1991), *Besicovitch type maximal operators and applications to Fourier analysis* — breakthrough [high-confidence]
9. Terence Tao, Ana Vargas, Luis Vega (1998), *A bilinear approach to the restriction and Kakeya conjectures* — breakthrough [high-confidence]
10. Thomas Wolff (2001), *A sharp bilinear cone restriction estimate* — breakthrough [high-confidence]
11. Terence Tao (2003), *A sharp bilinear restriction estimate for paraboloids* — breakthrough [needs-verification] (DOI 10.1007/s00039-003-0449-0)
12. Jonathan Bennett, Anthony Carbery, Terence Tao (2006), *On the multilinear restriction and Kakeya conjectures* — breakthrough [high-confidence]
13. Jean Bourgain, Larry Guth (2011), *Bounds on oscillatory integral operators based on multilinear estimates* — breakthrough [high-confidence]
14. Jean Bourgain, Ciprian Demeter (2015), *The proof of the $\ell^2$ decoupling conjecture* — breakthrough [high-confidence]
15. Larry Guth (2016), *A restriction estimate using polynomial partitioning* — breakthrough [high-confidence]
16. Larry Guth, Jonathan Hickman, Marina Iliopoulou (2019), *On the sharp $L^p$ bounds of oscillatory integral operators (Bochner–Riesz ranges)* — modern [needs-verification]

## AI Review Panel

### Claude (Anthropic) — in-house review

The document is a careful, honest survey. Its principal strength is calibration: it never overstates the state of knowledge, draws the $n=2$/$n\ge3$ line cleanly, identifies $\delta(p)$ correctly as a *necessary* (hence non-negotiable) threshold whose sufficiency is the open question, and correctly orients the restriction–Bochner–Riesz–Kakeya hierarchy with the direction of implications. The diagnosis of *why* the problem resists — the lossy multilinear-to-linear conversion and the Kakeya obstruction — is the genuine expert consensus, not a paraphrase of folklore.

I flag three things for a human reviewer. (i) Every reference here inherits a verification flag from the dossier; the rows marked *needs-verification* — notably Herz (1954), Córdoba (1977), the Tao 2003 DOI string, and the Guth–Hickman–Iliopoulou (2019) title — pair real, central work with title/identifier strings that I cannot certify. These require primary-source checking against MathSciNet/zbMATH before any citation is propagated. The underlying theorems are real; the *citation strings* are the risk. (ii) The document relies substantially on a single curated dossier for its record-range claims and timeline; quantitative statements about "current best ranges" are time-sensitive and may already be superseded by Kakeya/restriction progress, so they should be read as a snapshot. (iii) The single most important thing to verify is the precise current frontier for $n=3$ and the exact statements attributed to Bourgain–Guth (2011), Bourgain–Demeter (2015), and Guth–Hickman–Iliopoulou (2019), since the document's account of "best known ranges short of $\delta(p)$" rests on them; a reviewer should confirm none has been overtaken or misattributed.

Nothing here claims to resolve the conjecture, and the proven related results (Carleson–Sjölin in $n=2$; Fefferman's ball multiplier; Stein–Tomas) are stated as the genuine theorems they are. The remaining work is source-checking, not correction of substance.

**Verdict:** accept-with-revisions.

### GPT (OpenAI) — pending
_Not yet run. To complete the panel, run the prompt in docs/review/REVIEW-TEMPLATE.md through GPT and record the verdict here and in the front matter._

### Gemini (Google) — pending
_Not yet run. See docs/review/REVIEW-TEMPLATE.md._

### Grok (xAI) — pending
_Not yet run. See docs/review/REVIEW-TEMPLATE.md._

## Human verification

This AI-assisted review is not a substitute for human peer review. It is offered as a structured starting point for academic verification per ../docs/review/ACADEMIC-REVIEW.md: a human reviewer should check the primary sources behind every flagged citation, confirm the current state of the art for $n \ge 3$, and validate the mathematical statements before any claim here is relied upon. Status: human_review pending.

---
*Accredited to **Alexander Donahue** · The Unsolved Mathematics Atlas · CC BY 4.0. Cite per CITATION.cff.*

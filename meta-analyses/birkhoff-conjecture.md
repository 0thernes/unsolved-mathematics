---
title: "Meta-Analysis: The Birkhoff Conjecture (Integrable Billiards)"
slug: birkhoff-conjecture
author: Alexander Donahue
type: ai-assisted-meta-analysis
peer_reviewed: false
problem_status: active-progress
ai_review:
  claude:
    verdict: accept-with-revisions
    date: "2026-06-14"
    version: "claude-opus-4-8"
    summary: "A faithful and well-calibrated survey of the local/algebraic rigidity landscape, sound on what is open versus settled, but resting on a citation table whose identifiers the dossier itself flags as unverified."
  gpt:
    verdict: pending
  gemini:
    verdict: pending
  grok:
    verdict: pending
human_review: pending
---

# Meta-Analysis: The Birkhoff Conjecture (Integrable Billiards)

> **AI-generated meta-analysis — not peer-reviewed.** Curated and accredited by **Alexander Donahue** (human-in-the-loop). A survey/assessment of an open problem; it makes no claim of a new result. Citations carry verification flags and require human source-checking.

## Abstract

The Birkhoff conjecture asserts that the only smooth, strictly convex planar billiard tables whose dynamics are integrable are ellipses (the disk being the degenerate case). Posed by George David Birkhoff in the orbit of his 1927 monograph *Dynamical Systems* and sharpened into its local "Birkhoff–Poritsky" form by Poritsky (1950), it sits at the junction of dynamical systems, the calculus of variations, and inverse spectral theory. This meta-analysis surveys the conjecture's precise formulations — global, local, and rational integrability — and the principal rigidity programs attacking it: Hopf-type total-integrability rigidity (Bialy, 1993), polynomial/algebraic integrability (Bialy–Mironov), and the deformation/spectral approach of Avila–De Simoi–Kaloshin and Kaloshin–Sorrentino. Every unconditional theorem assumes either global integrability, a polynomial integral, or proximity to an ellipse; the general conjecture, for arbitrary locally integrable convex tables, remains open. We assess the barriers — closing Aubry–Mather gaps, bridging polynomial to analytic integrability, and removing perturbative smallness — and outline what a resolution would require. The status is *active-progress*: incremental, reliable advances, no accepted general proof.

## 1. Statement and significance

A billiard in a smooth strictly convex domain $\Omega$ sends a point mass along straight chords reflecting with equal angles off $\partial\Omega$. The induced billiard map acts on the phase cylinder of oriented chords, coordinatized by arclength $s$ and reflection angle $\varphi\in(0,\pi)$; it is an area-preserving monotone twist map. The table is *integrable* when this map admits a foliation by invariant curves — equivalently, when $\Omega$ carries a continuous family of caustics (curves to which a whole family of trajectories stays tangent). The ellipse is integrable: its confocal conics are caustics and the product of angular momenta about the foci (the Joachimsthal integral) is conserved. Birkhoff's conjecture is that this is rigid — ellipses are the *only* such tables.

The significance is twofold. Dynamically, integrability is the most ordered regime a Hamiltonian system can occupy, and the conjecture encodes the intuition that such order is exceptional and essentially algebraic, not robust. Structurally, the problem is a model "rigidity" statement ("the only objects with property $P$ are the obvious symmetric ones") with deep ties to inverse spectral geometry — whether one can "hear the shape" of a billiard table.

## 2. State of the art

The conjecture is sensitive to the meaning of "integrable," and the modern literature separates inequivalent versions: **global** integrability (the whole cylinder is foliated), **local / Birkhoff–Poritsky** integrability (invariant curves only accumulate on the boundary), and **rational** integrability (the $q$-periodic invariant curves are smooth for all $q\ge 3$). Most contemporary theorems address the local or rational forms, which Poritsky recognized as the natural objects.

Unconditional results exist only under strong hypotheses. Bialy (1993) proved that global foliation forces the disk. Lazutkin (1973) showed every smooth convex billiard has a positive-measure Cantor family of caustics near the boundary, so integrability is the *completeness* (gap-freeness) of this family, not its existence. Bialy–Mironov proved that a convex billiard with an integral polynomial in momenta is a conic. The deepest perturbative results — Avila–De Simoi–Kaloshin (small-eccentricity rational integrability) and Kaloshin–Sorrentino (local Birkhoff rigidity near generic ellipses) — show that integrable deformations of an ellipse are ellipses. The general conjecture, with no nearness, polynomiality, or symmetry assumption, is open.

## 3. Principal approaches and barriers

**Hopf-type rigidity.** Adapting Hopf's no-conjugate-points theorem, Bialy (1993) derived an integral-geometric inequality forcing constant curvature under *global* foliation. Barrier: the hypothesis is far stronger than local integrability, and the inequality loses control on a one-sided boundary neighborhood — the genuinely hard case.

**Polynomial / algebraic integrability.** The Bialy–Mironov program shows billiards with a polynomial-in-momenta integral are conics, using the angular-momentum integral and algebraic geometry of the boundary curve. Barrier: general integrability need not be polynomial; reducing analytic integrability to polynomial integrability is unavailable, so these theorems do not close the analytic conjecture.

**Deformation / spectral rigidity.** Kaloshin, Sorrentino, De Simoi, and collaborators linearize the integrability condition along families of tables, extracting infinitely many constraints from preserved periodic orbits and the Mather $\beta$-function, then annihilate all but trivial deformations via Fourier analysis. Barrier: the methods are perturbative and local around conics; estimates degrade as eccentricity grows or smoothness drops.

**Caustics and the calculus of variations.** Integrability equals a complete caustic foliation. Lazutkin's caustics generically leave gaps filled by Aubry–Mather sets and Birkhoff instability regions; proving the gaps must vanish for an integrable table is exactly the unsolved difficulty, and Mather's destruction-of-invariant-curves results show how delicate full foliation is.

## 4. Critical assessment

The dossier's central judgment is correct and well-calibrated: *every* unconditional theorem assumes global integrability, a polynomial integral, or proximity to an ellipse, and no method approaches the general statement. The recent decade did not narrow the conjecture so much as fence the region a counterexample could inhabit — it cannot be globally integrable (Bialy), cannot admit a polynomial integral (Bialy–Mironov), and cannot be a small smooth perturbation of an ellipse (Avila–De Simoi–Kaloshin, Kaloshin–Sorrentino). What remains uncontrolled is precisely the non-perturbative, transcendental middle.

The survey is also commendably careful about confusable results. It correctly flags that Treschev's formally integrable non-conic billiards concern a different (degenerate, formal/asymptotic) setting and do not contradict the convex conjecture, and that outer-billiard and polygonal results are separate problem classes. This discipline matters: the literature's reliability comes from authors stating hypotheses explicitly (global vs. local, polynomial vs. analytic), and the field has largely avoided the dramatic-claim-then-retraction cycle.

Two cautions. First, the survey leans on a handful of canonical works (Bialy 1993; the two *Annals* papers) for its load-bearing claims; the more recent items — Bialy–Mironov on centrally symmetric tables, Koval on arbitrary eccentricity — are cited from preprints whose full arguments warrant independent verification. Second, the precise demarcation between "rational" and "Birkhoff–Poritsky" integrability is subtle, and a reader should not conflate the rational-integrability rigidity results with the full local conjecture.

## 5. What a resolution would require / open directions

A general proof would need to: (1) **remove the nearness hypothesis**, passing from integrable deformations *of an ellipse* to *any* integrable convex table; (2) **bridge local-to-global / polynomial-to-analytic**, either by showing every integrable billiard admits an algebraic integral (reducing to Bialy–Mironov) or by developing non-perturbative caustic-foliation rigidity that does not start from a conic; (3) **close the Aubry–Mather gaps**, proving a complete boundary-accumulating caustic foliation forces global confocal structure; and (4) **weaken regularity** from $C^\infty$/analytic to finite smoothness. The most plausible routes are the deformation/spectral program extending outward (possibly merging with inverse-spectral techniques) and the algebraic line delivering clean statements under structural hypotheses; a genuine resolution likely needs a new mechanism forcing algebraicity of integrable caustics.

## 6. Selected references

1. George D. Birkhoff, *Dynamical Systems*, AMS Colloquium Publications IX, 1927. [high-confidence]
2. Hillel Poritsky, "The billiard ball problem on a table with a convex boundary," 1950. [high-confidence]
3. Vladimir F. Lazutkin, "The existence of caustics for a billiard problem in a convex domain," 1973. [high-confidence]
4. Misha Bialy, "Convex billiards and a theorem by E. Hopf," 1993. [high-confidence]
5. Misha Bialy, L. Polterovich, "A theorem of Hopf type for billiards," 1989. [needs-verification]
6. Serge Tabachnikov, *Geometry and Billiards*, Student Mathematical Library, AMS, 2005. [high-confidence]
7. Artur Avila, Jacopo De Simoi, Vadim Kaloshin, "An integrable deformation of an ellipse of small eccentricity is an ellipse," arXiv:1412.2853; *Annals of Mathematics*, 2018. [high-confidence]
8. Vadim Kaloshin, Alfonso Sorrentino, "On the local Birkhoff conjecture for convex billiards," arXiv:1612.09194; *Annals of Mathematics*, 2018. [high-confidence]
9. Jacopo De Simoi, Vadim Kaloshin, Qiaoling Wei, "Dynamical spectral rigidity among $\mathbb{Z}_2$-symmetric strictly convex domains," arXiv:1306.4233. [needs-verification]
10. Misha Bialy, Andrey E. Mironov, "Polynomially integrable convex billiards on surfaces of constant curvature," arXiv:1612.02913. [needs-verification]
11. Hamid Hezari, Steve Zelditch, "Nearly circular domains which are integrable are ellipses," arXiv:1603.07449. [needs-verification]
12. Misha Bialy, Andrey E. Mironov, "The Birkhoff–Poritsky conjecture for centrally symmetric billiard tables," arXiv:2008.03566. [needs-verification]
13. Comlan E. Koval, "Local rigidity of Birkhoff billiards for ellipses of arbitrary eccentricity (rational integrability)," arXiv:2306.04143. [needs-verification]
14. Eugene Gutkin, Anatole Katok, "Caustics for inner and outer billiards," 1986. [needs-verification]
15. A. Sorrentino, V. Kaloshin, "Birkhoff billiards, integrability and rigidity — a survey," 2022. [needs-verification]

## AI Review Panel

### Claude (Anthropic) — in-house review

This is a strong, honestly hedged survey. Its taxonomy of integrability notions (global / local-Birkhoff–Poritsky / rational) is the correct organizing axis, and the document never overstates: it consistently says the general conjecture is open and locates each theorem inside its hypothesis. The "fencing a counterexample" framing in §4 is an accurate and useful way to read the last decade, and the treatment of confusable results (Treschev's formal integrability, outer/polygonal billiards) guards against the most common mis-citations.

That said, the analysis inherits real risks from its sources. (i) The reference list carries verification flags directly from the dossier: rows beyond the four pillars (Birkhoff 1927, Poritsky 1950, Lazutkin 1973, Bialy 1993) and the two *Annals* papers are recalled, not confirmed — several arXiv identifiers (e.g., 1412.2853, 1612.09194, 2008.03566, 2306.04143) and at least one apparent year/venue inconsistency (the Avila–De Simoi–Kaloshin "2016" arXiv vs. 2018 *Annals*) need primary-source checking against MathSciNet/zbMATH before any of them is cited as established. (ii) There is single-source reliance on the Bialy–Mironov and Koval preprints for the frontier claims (centrally symmetric case, arbitrary eccentricity); these full arguments should be independently verified rather than taken as settled. (iii) The most important thing a human reviewer should verify is the precise logical scope of the headline theorems — specifically that "rational integrability" rigidity is *not* silently conflated with the full local Birkhoff–Poritsky conjecture, since the survey's calibration depends on keeping those hypotheses distinct.

None of these are conceptual errors; they are verification and precision gaps appropriate to flag before publication. The mathematical narrative is sound and representative of the field's consensus.

**Verdict:** accept-with-revisions.

### GPT (OpenAI) — pending
_Not yet run. To complete the panel, run the prompt in docs/review/REVIEW-TEMPLATE.md through GPT and record the verdict here and in the front matter._

### Gemini (Google) — pending
_Not yet run. See docs/review/REVIEW-TEMPLATE.md._

### Grok (xAI) — pending
_Not yet run. See docs/review/REVIEW-TEMPLATE.md._

## Human verification

AI review is not human peer review. This meta-analysis is offered for academic verification per ../docs/review/ACADEMIC-REVIEW.md, and its citations — particularly the arXiv identifiers and the frontier preprint claims flagged above — require confirmation against primary sources before use. Status: human_review pending.

---
*Accredited to **Alexander Donahue** · The Unsolved Mathematics Atlas · CC BY 4.0. Cite per CITATION.cff.*

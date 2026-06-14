---
title: "Meta-Analysis: The Hadwiger Covering Conjecture"
slug: hadwiger-covering-conjecture
author: Alexander Donahue
type: ai-assisted-meta-analysis
peer_reviewed: false
problem_status: open
ai_review:
  claude:
    verdict: accept-with-revisions
    date: "2026-06-14"
    version: "claude-opus-4-8"
    summary: "A faithful and well-calibrated survey of an open conjecture whose central facts are reliable, but whose reference apparatus carries explicit verification flags and needs primary-source confirmation before citation."
  gpt:
    verdict: pending
  gemini:
    verdict: pending
  grok:
    verdict: pending
human_review: pending
---

# Meta-Analysis: The Hadwiger Covering Conjecture

> **AI-generated meta-analysis — not peer-reviewed.** Curated and accredited by **Alexander Donahue** (human-in-the-loop). A survey/assessment of an open problem; it makes no claim of a new result. Citations carry verification flags and require human source-checking.

## Abstract

The Hadwiger covering conjecture asserts that every convex body $K\subset\mathbb{R}^n$ can be covered by at most $2^n$ smaller homothetic copies of itself, with equality only for parallelepipeds. Posed by Hadwiger (1957), independently restated as a covering-by-homothets problem by Gohberg and Markus (1960), and reformulated by Boltyanski (1960) in terms of an *illumination number* $I(K)=c(K)$, it is one of the headline open problems of discrete geometry. The planar case is a complete theorem (Levi: $c(K)\le 4$, equality iff parallelogram), and smooth bodies in every dimension need only $n+1$ directions. Yet the conjecture is open for all $n\ge 3$ — including the full three-dimensional case, where it predicts $c(K)\le 8$. The best unconditional upper bound for general bodies is of order $4^n$ up to polynomial factors, exponentially above the target; the 2021 thin-shell improvement of Huang–Slomka–Tkocz–Vritsiou sharpened constants but did not close the factor-$2^n$ gap. This meta-analysis surveys the principal approaches — illumination, volumetric/probabilistic covering, belt-body and symmetry methods, low-dimensional topological attacks, and fractional relaxations — and the structural barriers that have kept the conjecture unresolved for nearly seventy years.

## 1. Statement and significance

Let $K\subset\mathbb{R}^n$ be a convex body (compact, convex, nonempty interior). A *homothet* is $\lambda K+t$ with $\lambda>0$, $t\in\mathbb{R}^n$; it is *smaller* if $0<\lambda<1$. The *covering number* $c(K)$ is the least number of smaller homothets whose union contains $K$. The conjecture is
$$
c(K)\le 2^n\quad\text{for every convex body }K\subset\mathbb{R}^n,
$$
with equality **iff** $K$ is an $n$-dimensional parallelepiped. For the cube the $2^n$ copies sit at the corners, and the bound is sharp.

The problem is famous for its three equivalent disguises. Boltyanski's *illumination number* $I(K)$ — the least number of directions illuminating every boundary point — equals $c(K)$, as does the minimum number of translates of $\operatorname{int}K$ covering $K$; the literature uses the three interchangeably. The significance is the tension between an exceptionally clean, dimension-uniform statement and an extremizer (the parallelepiped) that is the *least* generic body, combined with the brutal difficulty of even $n=3$.

## 2. State of the art

Per the source metadata the status is **open**. The conjecture is unproven for all $n\ge 3$, and no accepted proof of the full three-dimensional case exists.

What is established unconditionally: the **planar case** is complete (Levi, $c(K)\le 4$, equality only for parallelograms); **smooth bodies** in any dimension satisfy $I(K)=n+1$; and broad structured classes are settled — zonotopes/zonoids, belt polytopes and belt bodies, direct sums and many Cartesian products, **centrally symmetric bodies in $\mathbb{R}^3$** ($c\le 8$, attributed to Lassak), **constant-width bodies in $\mathbb{R}^3$**, bodies of revolution, and bodies with sufficiently large symmetry groups. The best *general* upper bound is roughly $4^n$ up to polynomial factors, via economic-covering estimates; for symmetric bodies the sharpest current statement is the Huang–Slomka–Tkocz–Vritsiou (2021) bound
$$
c(K)\le\binom{2n}{n}\big(n\ln n+n\ln\ln n+5n\big),
$$
improving the classical Rogers / Erdős–Rogers $\binom{2n}{n}\,n\ln n$ estimate. Since $\binom{2n}{n}\approx 4^n/\sqrt{n}$, this remains exponentially above $2^n$.

## 3. Principal approaches and barriers

**Illumination (Boltyanski).** Converting covering into illumination localizes the problem to boundary points and normal cones. This is the working language of nearly all progress, but illumination is genuinely combinatorial at vertices, lacks monotonicity under sections/projections, and does not aggregate from local control into a global $2^n$ bound.

**Probabilistic / volumetric covering.** Random-covering and the Rogers–Zong economic-covering lemma give the $\sim 4^n$ bounds above. The method is intrinsically lossy: the slack $\binom{2n}{n}/2^n\approx 2^n$ is inherent to covering-by-volume and cannot be removed by sharpening density constants alone.

**Belt bodies, zonotopes, symmetry.** Boltyanski's belt-body structure theory and symmetry arguments settle large classes with the parallelepiped as unique extremizer. These methods are class-specific; a generic body has no belts, symmetry, or product structure.

**Low-dimensional topological attack ($n=3$).** One partitions $\partial K$ (a topological $2$-sphere) into regions illuminable by a common direction via the Gauss map. The general $\mathbb{R}^3$ case remains open: irregular "spiky" vertices defeat naive partitions of the direction sphere into $8$ caps.

**Fractional / LP relaxation.** Fractional illumination (Naszódi, Artstein-Avidan, and others) gives the cleanest current proofs and stability estimates near the cube, but the integrality gap between fractional and integer covering can itself be exponential.

**Equality / stability program.** A full solution must also prove uniqueness of parallelepipeds. Partial rigidity is known for already-verified classes; a general stability theorem is absent, and this program waits on the existence question.

## 4. Critical assessment

The dossier's central claims align with the established consensus of the survey literature: the conjecture is open for $n\ge 3$, the planar and smooth cases are complete, and the quantitative gap is between $2^n$ and $\sim 4^n$. The framing of the $\binom{2n}{n}/2^n\approx 2^n$ slack as *intrinsic* to volumetric methods is a fair characterization of why incremental sharpening of constants has not, and likely will not, reach the target. The treatment of disputed claims is appropriately neutral: sporadic preprints asserting a full $\mathbb{R}^3$ proof are recorded as unverified pending refereed publication and survey endorsement, which is the correct posture.

Two cautions. First, attributions and dates in the dossier are plausible but not all independently confirmed here — in particular the precise statements credited to Lassak (the $\mathbb{R}^3$ symmetric case), Dekster (constant width), and the exact form of the 2021 bound should be checked against primary sources. Second, the claim of equality (uniqueness of parallelepipeds) is genuinely a *second* open problem nested inside the first, and the document is right not to treat an eventual upper-bound proof as automatically delivering it.

## 5. What a resolution would require / open directions

A full resolution appears to need three ingredients, none currently in hand. (1) **A non-volumetric method** exploiting convex structure (faces, normal cones, polarity) rather than volume ratios, since the probabilistic route is lossy by a factor $\approx 2^n$. (2) **A vertex / normal-cone theory** robust enough to partition the sphere of directions into $\le 2^n$ illuminable regions for arbitrary bodies — the missing piece even at $n=3$. (3) **A global rigidity/stability theorem** establishing the equality clause.

Plausible partial routes: push thin-shell/concentration and fractional methods to obtain $c(K)\le c^n$ with $c<4$ (any sub-$4^n$ exponential base for general bodies would be a milestone); resolve $\mathbb{R}^3$ outright via a new Gauss-map partition and seek transfer to higher dimensions; or expand the family of structured bodies until the residual generic case yields to approximation. The survey consensus (Bezdek–Khan; Boltyanski–Martini–Soltan; Naszódi) is that a genuinely new idea is needed.

## 6. Selected references

1. F. W. Levi (1955), *Über die Anzahl der Teilkörper, in die ein konvexer Körper zerlegt werden kann* (planar illumination). [high-confidence]
2. Hugo Hadwiger (1957), *Ungelöste Probleme Nr. 20* (and related problem notes). [high-confidence]
3. I. Ts. Gohberg, A. S. Markus (1960), *A problem concerning covering convex bodies by smaller homothetic copies* (Russian). [high-confidence]
4. V. G. Boltyanski (1960), *Solution of a problem concerning the illumination of convex bodies* (Russian). [high-confidence]
5. C. A. Rogers (1963), economic covering estimates / covering a sphere with spheres. [high-confidence]
6. M. Lassak (1984), *Solution of Hadwiger's covering problem for centrally symmetric bodies in $\mathbb{R}^3$*. [needs-verification]
7. B. V. Dekster (1991), illumination/constant-width bodies in $\mathbb{R}^3$. [needs-verification]
8. K. Bezdek (1993), *The problem of illumination of the boundary of a convex body by affine subspaces*. [needs-verification]
9. V. Boltyanski, H. Martini, P. S. Soltan (2001), *Excursions into Combinatorial Geometry* (monograph). [high-confidence]
10. K. Bezdek, M. A. Khan (2010), *The geometry of homothetic covering and illumination* (survey), arXiv:1602.06040. [needs-verification]
11. K. Bezdek (2011), *Classical Topics in Discrete Geometry* (illumination chapters). [high-confidence]
12. S. Artstein-Avidan, M. Naszódi (2016), *Fractional illumination of convex bodies*. [needs-verification]
13. M. Naszódi (2016), improved bounds for illumination of symmetric convex bodies (concentration methods). [needs-verification]
14. H. Huang, B. A. Slomka, T. Tkocz, B.-H. Vritsiou (2021), *Improved bounds for Hadwiger's covering problem via thin-shell estimates*, arXiv:1911.00559. [needs-verification]
15. M. Naszódi (2022), *Covering and illumination: recent progress and open problems* (survey). [needs-verification]

## AI Review Panel

### Claude (Anthropic) — in-house review

The survey is accurate and well-calibrated. Its strengths are the clean separation of what is proven (planar case with equality, smooth bodies, structured classes) from what is conjectured; the honest framing of the quantitative gap as $2^n$ versus $\sim4^n$; and the explanation of *why* the volumetric route is intrinsically lossy rather than merely unoptimized. The handling of withdrawn/disputed proof claims is exemplary — neutral, and correctly deferring to refereed venues and the survey literature rather than adjudicating preprints.

Three concerns a human reviewer should weigh. (i) Every reference carries a verification flag, and most of the modern entries are marked "needs-verification"; the two arXiv identifiers (Bezdek–Khan 1602.06040; Huang–Slomka–Tkocz–Vritsiou 1911.00559) and the Lassak/Dekster attributions in particular must be confirmed against primary sources before any of this is cited downstream. (ii) There is mild single-source reliance on the standard survey trio (Bezdek–Khan; Boltyanski–Martini–Soltan; Naszódi); claims about which classes are "settled" and by whom inherit whatever errors those surveys contain, and the document does not cross-check them independently. (iii) The numerically load-bearing claim is the exact form of the 2021 bound $c(K)\le\binom{2n}{n}(n\ln n+n\ln\ln n+5n)$ — this is the single most important item to verify, since the document's central narrative (a persistent factor-$2^n$ gap) rests on it; the constant $5n$ and the $n\ln\ln n$ term should be checked against arXiv:1911.00559 directly.

No overstatement of resolution is present; the document makes no claim to prove or resolve the conjecture and correctly lists both the general statement and the $n=3$ case as open. **Verdict:** accept-with-revisions.

### GPT (OpenAI) — pending

_Not yet run. To complete the panel, run the prompt in docs/review/REVIEW-TEMPLATE.md through GPT and record the verdict here and in the front matter._

### Gemini (Google) — pending

_Not yet run. See docs/review/REVIEW-TEMPLATE.md._

### Grok (xAI) — pending

_Not yet run. See docs/review/REVIEW-TEMPLATE.md._

## Human verification

AI review is not human peer review. This meta-analysis is offered for academic verification per ../docs/review/ACADEMIC-REVIEW.md; the AI panel above flags items for checking but does not substitute for a domain expert's reading of the primary sources, especially the attributions and the exact form of the 2021 bound. Status: human_review pending.

---
*Accredited to **Alexander Donahue** · The Unsolved Mathematics Atlas · CC BY 4.0. Cite per CITATION.cff.*

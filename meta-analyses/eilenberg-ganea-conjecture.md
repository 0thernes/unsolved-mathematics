---
title: "Meta-Analysis: The Eilenberg–Ganea Conjecture"
slug: eilenberg-ganea-conjecture
author: Alexander Donahue
type: ai-assisted-meta-analysis
peer_reviewed: false
problem_status: open
ai_review:
  claude:
    verdict: accept-with-revisions
    date: "2026-06-14"
    version: "claude-opus-4-8"
    summary: "An accurate, well-scoped survey of a genuinely open dimension-2 problem whose only real defects are an under-verified bibliography and reliance on a small number of canonical sources."
  gpt:
    verdict: pending
  gemini:
    verdict: pending
  grok:
    verdict: pending
human_review: pending
---

# Meta-Analysis: The Eilenberg–Ganea Conjecture

> **AI-generated meta-analysis — not peer-reviewed.** Curated and accredited by **Alexander Donahue** (human-in-the-loop). A survey/assessment of an open problem; it makes no claim of a new result. Citations carry verification flags and require human source-checking.

## Abstract

The Eilenberg–Ganea conjecture asks whether every group $G$ of cohomological dimension $\operatorname{cd}(G)=2$ also has geometric dimension $\operatorname{gd}(G)=2$ — that is, whether it admits a $2$-dimensional aspherical CW model $K(G,1)$. Posed in 1957, it is the single unresolved case in the dimension dictionary relating an algebraic invariant ($\operatorname{cd}$, the projective dimension of $\mathbb{Z}$ over $\mathbb{Z}G$) to a geometric one ($\operatorname{gd}$). Eilenberg and Ganea settled all dimensions $\ge 3$; Stallings and Swan settled dimensions $0$ and $1$. Only $\operatorname{cd}=2$ remains, where the general bound forces $\operatorname{gd}\in\{2,3\}$, making the question binary. This meta-analysis surveys the algebraic core (the $D(2)$-problem and relation modules), the dimension-$1$ analogy, the Bestvina–Brady dichotomy linking the conjecture to the Whitehead asphericity conjecture, and $K$-theoretic obstructions in $\widetilde{K}_0(\mathbb{Z}G)$. It records broad verifications (one-relator groups, surface and $\mathrm{PD}_2$ groups) alongside the structural reasons no counterexample has been located. The consensus leans toward truth; no decisive technique exists in either direction. The document makes no claim of a resolution.

## 1. Statement and significance

To a discrete group $G$ one associates the aspherical classifying space $K(G,1)$, whose homotopy type is determined by $G$. Its minimal complexity is measured two ways: the **cohomological dimension** $\operatorname{cd}(G)$, the projective dimension of the trivial $\mathbb{Z}G$-module $\mathbb{Z}$ (equivalently the largest $n$ with $H^n(G;M)\neq 0$ for some module $M$); and the **geometric dimension** $\operatorname{gd}(G)$, the least dimension of an aspherical CW model. One always has $\operatorname{cd}(G)\le\operatorname{gd}(G)$.

> **Conjecture (Eilenberg–Ganea, 1957).** If $\operatorname{cd}(G)=2$ then $\operatorname{gd}(G)=2$.

The significance is foundational: the conjecture is the last place in the $\operatorname{cd}$-versus-$\operatorname{gd}$ dictionary where a clean algebraic invariant is not known to have a clean geometric realization. It sits at the intersection of group cohomology, two-dimensional homotopy theory, and the algebraic $K$-theory of group rings, and is logically entangled with the Whitehead asphericity conjecture (Section 3).

## 2. State of the art

**Status: open.** No group with $\operatorname{cd}=2$ and $\operatorname{gd}=3$ has been found, and no proof that none exists is known. What is settled is the surrounding frame. The **Eilenberg–Ganea theorem** establishes $\operatorname{cd}(G)=n\Rightarrow\operatorname{gd}(G)=n$ for all $n\ge 3$, by explicit cell attachment using the "slack" available above dimension $2$. Stallings (1968, finitely generated case) and Swan (1969, general) proved $\operatorname{cd}(G)=1 \iff G$ free $\iff \operatorname{gd}(G)=1$. Together with the general inequality $\operatorname{gd}(G)\le\max(3,\operatorname{cd}(G))$, these results isolate $\operatorname{cd}=2$ as the only open case and force $\operatorname{gd}\in\{2,3\}$ there — the conjecture is genuinely binary.

The conjecture holds on broad classes: torsion-free one-relator groups (via Lyndon's Identity Theorem, giving aspherical presentation $2$-complexes); surface groups and two-dimensional Poincaré-duality ($\mathrm{PD}_2$) groups, which are surface groups and so realized by surfaces; and groups with $\widetilde{K}_0(\mathbb{Z}G)=0$ and trivial $D(2)$-obstruction. Every verified class shares one feature: the relation module is provably free and the presentation $2$-complex is provably aspherical.

## 3. Principal approaches and barriers

**Algebraic core — the $D(2)$-problem.** If $\operatorname{cd}(G)=2$, the trivial module admits a length-$2$ projective resolution; realizing $\operatorname{gd}=2$ requires this to come from a presentation $2$-complex whose attaching maps kill $\pi_2$. The obstruction is whether a stably-free relation module can be replaced by a genuinely free one of the same rank. Wall's $D(2)$ framing, developed extensively by F.E.A. Johnson (and W.H. Mannan), converts the problem into computations in the stable module category and $K$-theory. The barrier: the relevant class lives in $\widetilde{K}_0(\mathbb{Z}G)$, which is nonzero for many infinite groups, and even when it vanishes the *realization* of a free resolution by attaching maps is not automatic.

**Dimension-$1$ analogy.** The clean Stallings–Swan classification is the template — but its proof uses Stallings' theorem on ends of groups and the freeness of submodules of free $\mathbb{Z}G$-modules in projective dimension $\le 1$. No structure theorem for projective-dimension-$2$ modules exists; the accessibility/JSJ machinery that controls dimension $1$ has no dimension-$2$ counterpart that controls $\pi_2$.

**Bestvina–Brady Morse theory.** From a flag complex $L$ one builds the kernel $H_L$ of a height map on a right-angled Artin group. Choosing $L$ acyclic but not simply connected yields $\operatorname{cd}=2$ groups that are $\mathrm{FP}_2$ but not finitely presented, and proves the **dichotomy**: at least one of Eilenberg–Ganea and Whitehead asphericity must fail. The barrier is sharp — the candidate $H_L$ are not finitely presented, so they do not refute the finitely-presented form of the conjecture, and pinning their exact $\operatorname{gd}$ confronts the same $\pi_2$ obstruction. The dichotomy shows a counterexample exists *somewhere* without locating it.

**Duality and $\ell^2$ / profinite invariants.** For $\mathrm{PD}_2$ groups the answer is affirmative; deficiency arguments handle one-relator and small-deficiency cases. But $\ell^2$-Betti numbers and deficiency do not detect the difference between $\operatorname{gd}=2$ and $\operatorname{gd}=3$, so these methods stall on general $\operatorname{cd}=2$ groups.

## 4. Critical assessment

The dossier's central claim — that the problem reduces to a single binary obstruction governed by relation-module freeness and $D(2)$-realization — is accurate and is the standard modern framing. The most consequential structural fact is the Bestvina–Brady dichotomy: it converts the search for a counterexample into a problem of *finite presentability*, since the natural candidates are $\mathrm{FP}_2$ but not finitely presented. This is why six decades of work have produced rich partial results in both directions without resolution. The asymmetry is worth stressing: the "prove it" line needs a dimension-$2$ analogue of Stallings–Swan that no one has; the "break it" line needs a finitely presented witness that the only known construction cannot supply.

One caution: the dossier's characterization of folkloric claimed proofs — that they invariably assume the free-replacement step, which *is* the $D(2)$ problem — is plausible and consistent with the literature's skepticism, but the survey does not (and cannot) catalogue every such manuscript, so this should be read as a fair generalization rather than an exhaustive audit.

## 5. What a resolution would require / open directions

To **prove** the conjecture: a structure theorem for $\mathbb{Z}G$-modules of projective dimension $2$ strong enough to force a stably-free relation module to be realized by an aspherical presentation $2$-complex — an affirmative $D(2)$-answer in this generality, the missing dimension-$2$ analogue of Stallings–Swan.

To **disprove** it: a finitely presented $G$ with $\operatorname{cd}(G)=2$ together with a genuine, computable obstruction proving $\operatorname{gd}(G)=3$. By the dichotomy this would leave the Whitehead conjecture as the survivor.

Plausible routes: (1) extend the $D(2)$ / stable-module programme to ever-larger classes, aiming at a general theorem; (2) engineer Bestvina–Brady / RAAG-subgroup constructions toward a *finitely presented* $\operatorname{cd}=2$ group with computable $\operatorname{gd}=3$; (3) develop a new invariant sensitive to the $\operatorname{gd}=2$-versus-$3$ distinction, which current $\ell^2$ and deficiency invariants are not.

## 6. Selected references

1. S. Eilenberg, S. Mac Lane, *General Theory of Natural Equivalences* (1945), DOI 10.2307/1990284. [high-confidence]
2. S. Eilenberg, S. Mac Lane, *Cohomology Theory in Abstract Groups, I* (1947), DOI 10.2307/1969145. [high-confidence]
3. H. Cartan, S. Eilenberg, *Homological Algebra* (1956). [high-confidence]
4. S. Eilenberg, T. Ganea, *On the Lusternik–Schnirelmann Category of Abstract Groups* (1957), DOI 10.2307/1969854. [high-confidence]
5. J. Stallings, *On Torsion-Free Groups with Infinitely Many Ends* (1968), DOI 10.2307/1970577. [high-confidence]
6. R. G. Swan, *Groups of Cohomological Dimension One* (1969), DOI 10.1016/0021-8693(69)90074-3. [high-confidence]
7. K. S. Brown, *Cohomology of Groups* (1982). [high-confidence]
8. C. Hog-Angeloni, W. Metzler, A. Sieradski (eds.), *Two-Dimensional Homotopy and Combinatorial Group Theory* (1987). [needs-verification]
9. A. Hatcher, *Algebraic Topology* (1993/2002). [high-confidence]
10. M. Bestvina, N. Brady, *Morse Theory and Finiteness Properties of Groups* (1997), DOI 10.1007/s002220050168. [high-confidence]
11. M. Bestvina, *Questions in Geometric Group Theory* (problem list, 1998). [needs-verification]
12. F. E. A. Johnson, *Stable Modules and the D(2)-Problem* (2003, LMS Lecture Notes). [needs-verification]
13. W. H. Mannan, *Realizing 2-dimensional algebraic complexes geometrically* (2009). [needs-verification]
14. C. T. C. Wall (ed.), *Homological Group Theory* (LMS Lecture Note Series 36, 1976). [needs-verification]
15. M. Clay, D. Margalit (eds.), *Office Hours with a Geometric Group Theorist* (2017). [needs-verification]

## AI Review Panel

### Claude (Anthropic) — in-house review

**Strengths.** The survey gets the mathematics right where it matters most. It correctly identifies the binary nature of the open case ($\operatorname{gd}\in\{2,3\}$ when $\operatorname{cd}=2$), correctly attributes the boundary results (Eilenberg–Ganea for $n\ge3$; Stallings/Swan for $n=1$), and correctly centers the analysis on the two genuinely hard objects: relation-module freeness / the $D(2)$-problem, and the Bestvina–Brady dichotomy. The treatment of the dichotomy as a *relocation* of difficulty rather than a counterexample is precise and is the single most important conceptual point about the problem; the survey does not overstate it.

**Concerns.** First and most important, the bibliography is uneven: only six entries carry high-confidence identifiers, and a substantial block (Johnson's $D(2)$ lecture notes, Mannan's realization papers, the Bestvina problem list, the Hog-Angeloni–Metzler–Sieradski volume) is flagged needs-verification with exact titles, years, and DOIs unconfirmed. A human reviewer must check these against MathSciNet/zbMATH before any citation is relied upon — the dossier itself is admirably candid about this. Second, there is some single-source reliance: the dichotomy claim rests on Bestvina–Brady (1997), and the $D(2)$ reduction leans heavily on Johnson's programme; both are correctly attributed but neither is cross-checked here against independent expositions. Third, watch for mild overstatement in the phrase that surface/$\mathrm{PD}_2$ groups are "known" — the identification of $\mathrm{PD}_2$ groups with surface groups (Eckmann–Müller–Linnell and related) is a deep theorem in its own right and should be cited as such rather than treated as routine.

**Most important thing to verify.** The precise statement and scope of the Bestvina–Brady dichotomy — specifically that their construction yields $\operatorname{cd}=2$, $\mathrm{FP}_2$, non-finitely-presented groups and that "not both conjectures hold" is exactly what they prove (not a folklore strengthening). This single fact carries the document's structural narrative, so a primary-source check of Bestvina–Brady (1997) is the highest-value verification.

**Verdict:** accept-with-revisions.

### GPT (OpenAI) — pending
_Not yet run. To complete the panel, run the prompt in docs/review/REVIEW-TEMPLATE.md through GPT and record the verdict here and in the front matter._

### Gemini (Google) — pending
_Not yet run. See docs/review/REVIEW-TEMPLATE.md._

### Grok (xAI) — pending
_Not yet run. See docs/review/REVIEW-TEMPLATE.md._

## Human verification

AI review is not human peer review. This meta-analysis is offered for academic verification per ../docs/review/ACADEMIC-REVIEW.md; readers should independently confirm all flagged citations, the precise statements of the Eilenberg–Ganea theorem and the Bestvina–Brady dichotomy, and the scope of the cited verifications on one-relator and $\mathrm{PD}_2$ groups against primary sources. Status: human_review pending.

---
*Accredited to **Alexander Donahue** · The Unsolved Mathematics Atlas · CC BY 4.0. Cite per CITATION.cff.*

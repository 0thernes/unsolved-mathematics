---
title: "Meta-Analysis: The Jacobian Conjecture"
slug: jacobian-conjecture
author: Alexander Donahue
type: ai-assisted-meta-analysis
peer_reviewed: false
problem_status: open
ai_review:
  claude:
    verdict: accept-with-revisions
    date: "2026-06-14"
    version: "claude-opus-4-8"
    summary: "A faithful, well-structured survey of an open problem whose central claims match the consensus literature, but whose references carry explicit verification flags that demand primary-source checking."
  gpt:
    verdict: pending
  gemini:
    verdict: pending
  grok:
    verdict: pending
human_review: pending
---

# Meta-Analysis: The Jacobian Conjecture

> **AI-generated meta-analysis — not peer-reviewed.** Curated and accredited by **Alexander Donahue** (human-in-the-loop). A survey/assessment of an open problem; it makes no claim of a new result. Citations carry verification flags and require human source-checking.

## Abstract

The Jacobian Conjecture, posed by Ott-Heinrich Keller in 1939, asserts that a polynomial map $F\colon\mathbb{C}^n\to\mathbb{C}^n$ with constant nonzero Jacobian determinant admits a polynomial inverse. It remains open for every $n\ge 2$ over fields of characteristic zero, despite more than eight decades of effort and a notorious catalogue of retracted general proofs. This meta-analysis synthesizes the problem's history, the state of the art, and the principal lines of attack. The decisive structural achievement is the reduction (Bass–Connell–Wright; Yagzhev; Drużkowski) of the full conjecture to cubic-homogeneous and cubic-linear maps, recasting it as a nilpotency question for the Jacobian of the nonlinear part. Equivalences to the Dixmier conjecture (Belov-Kanel–Kontsevich) and to Zhao's vanishing conjecture relocate the difficulty into noncommutative algebra and differential-operator theory without dissolving it. The recurring failure mode is the local-to-global gap: a constant Jacobian supplies a local analytic inverse, but forcing a global polynomial inverse has never been achieved in full generality. The conjecture is solid as a problem but distant as a target; no route has survived the dimension/degree trade-off.

## 1. Statement and significance

A polynomial map $F=(F_1,\dots,F_n)\colon\mathbb{C}^n\to\mathbb{C}^n$ is invertible with polynomial inverse only if its Jacobian determinant $\det DF=\det(\partial F_i/\partial x_j)$ is a nonzero constant — by the chain rule, $\det DF$ and $(\det DF^{-1})\circ F$ are mutually inverse polynomials, hence units in $\mathbb{C}[x]$. The Jacobian Conjecture asks whether this necessary condition is also sufficient. The hypotheses are sharp: the statement is **false in positive characteristic** ($x\mapsto x-x^p$ over $\mathbb{F}_p$ has Jacobian $1$ but is non-injective) and false if "polynomial" is weakened to "holomorphic." Dimension $1$ is trivial.

The problem sits at a crossroads of algebraic geometry, commutative algebra, and the structure theory of $\mathrm{Aut}(\mathbb{C}[x_1,\dots,x_n])$. Steve Smale included it in his 1998 list of problems for the next century, cementing its standing among the central open questions in algebra. Its centrality derives less from applications than from the deep, still-unmapped relationship between local infinitesimal invertibility and global algebraic invertibility.

## 2. State of the art

The conjecture is **open** in all dimensions $n\ge 2$; no proof or counterexample for $n\ge 2$ has survived refereeing, and there is no warranted "resolved" or "disputed-claim" flag.

**Unconditional results.** The foundational theorem is degree reduction: it suffices to treat $F=X+H$ with $H$ homogeneous of degree $3$ (Bass–Connell–Wright 1982; Yagzhev c. 1980), and further the cubic-linear normal form $H_i=(a_i\cdot x)^3$ (Drużkowski 1983). In this form the conjecture is equivalent to the implication "$DH$ nilpotent $\Rightarrow X+H$ invertible." Degree-2 (quadratic) maps are invertible in all dimensions (Wang). In dimension 2, Moh (1983) settled degree $\le 100$, but the plane case in unbounded degree remains open. Various structurally special families — symmetric (gradient) maps, low-rank nilpotent Jacobians — are resolved (de Bondt–van den Essen). If $F$ is invertible then $\deg F^{-1}\le(\deg F)^{n-1}$, a bound on the inverse assuming it exists rather than a proof of existence.

**Conditional results / equivalences.** Belov-Kanel and Kontsevich (2007) proved $\mathrm{JC}_{2n}$ is stably equivalent to the Dixmier conjecture $\mathrm{DC}_n$ on endomorphisms of the Weyl algebra $A_n$. Zhao's vanishing conjecture for the Laplacian, and the associated Mathieu–Zhao-subspace formulation, is equivalent to the full conjecture. Both equivalences are genuine and structurally illuminating, but each ties the problem to another open conjecture rather than to a solved one.

## 3. Principal approaches and barriers

**Degree reduction (Bass–Connell–Wright / Yagzhev / Drużkowski).** A permanent foundation of the subject. *Barrier:* the reduction trades degree for dimension — a degree-$d$ map in dimension $n$ becomes cubic in much higher dimension — so the cubic case is genuinely as hard as the general one. The difficulty concentrates rather than dissolves; no dimension-uniform handle on nilpotency has emerged.

**Low-dimension / low-degree verification.** Settles bounded-degree subcases and special families. *Barrier:* there is no known degree threshold beyond which the general case follows, and dimension 2 in unbounded degree is itself open.

**Nilpotency / structure of $DH$.** Recasts the cubic case as combinatorics of nilpotent matrices over polynomial rings; the symmetric case links to polynomials with nilpotent Hessian. *Barrier:* the combinatorial explosion of nilpotency conditions in growing dimension resists a general argument, and overly optimistic nilpotency statements have known counterexamples in the analogous Hessian classification.

**Mathieu–Zhao / vanishing-conjecture framework.** A genuine new equivalent formulation via differential operators with fertile links to noncommutative algebra. *Barrier:* the reformulation has not proven easier to attack; the general vanishing statement is as open as the conjecture.

**Dixmier–Weyl-algebra bridge (Belov-Kanel–Kontsevich).** A precise equivalence to a famous noncommutative conjecture. *Barrier:* Dixmier's conjecture is itself unproven, so the bridge relocates difficulty rather than removing it.

**Tame–wild / Newton-polytope methods.** Shestakov–Umirbaev (2004) proved the Nagata automorphism is wild in dimension 3, and degree-bound techniques control formal inverse data. *Barrier:* these bounds presuppose invertibility or control only formal/analytic data; they do not force a polynomial inverse.

Crucially, the conjecture has **no widely accepted formal barrier theorem** (unlike relativization/natural-proofs in complexity, or the parity barrier in sieve theory). The recurring obstruction is empirical: the **local-to-global gap** and the dimension/degree trade-off.

## 4. Critical assessment

What is solid is genuinely solid. The cubic and cubic-linear reductions, the degree-2 settlement, Moh's degree-100 plane theorem, the Belov-Kanel–Kontsevich equivalence, and Shestakov–Umirbaev's wildness theorem are accepted, refereed mathematics. The dossier's framing — that these results concentrate or relocate the difficulty rather than resolve it — is accurate and refreshingly unhyped.

What is speculative is the prospect of any near-term resolution. Every active route (Dixmier, vanishing conjecture, nilpotency induction, tropical degree control) terminates at the same wall: no argument has survived the passage to arbitrary dimension. The equivalences are double-edged — they are evidence of the problem's depth, not of imminent progress, since they connect it to problems no easier than itself. The frontier is, honestly, far: there is no consensus candidate strategy and no partial result that visibly "points toward" a general proof. The most reliable empirical signal is negative — the steady production of retracted general proofs, which the dossier rightly treats as the field's main cautionary datum rather than as progress.

## 5. What a resolution would require / open directions

A complete proof must close the local-to-global gap: the constant-Jacobian hypothesis already furnishes an analytic/formal local inverse everywhere; the work is to force a single global polynomial inverse. Concretely, this means either (a) a dimension-uniform proof that nilpotency of $DH$ forces invertibility of $X+H$ in the cubic-linear case, overcoming the degree/dimension trade-off that defeats induction, or (b) a proof of an equivalent conjecture (Dixmier or Zhao's vanishing conjecture) by methods strong enough to transfer back. A counterexample would require a polynomial map with constant nonzero Jacobian that fails injectivity or whose inverse is non-polynomial; the analytic rigidity of characteristic zero makes such an object hard even to search for, and none is known.

Active directions: the noncommutative/quantization route via Dixmier; differential-operator cases of Zhao's vanishing conjecture; structural induction extending de Bondt–van den Essen nilpotency classifications to higher rank; and tropical/Newton-polytope degree control aimed at excluding non-polynomial inverses.

## 6. Selected references

1. Keller, O.-H. (1939). *Ganze Cremona-Transformationen.* Monatshefte für Mathematik und Physik. [high-confidence]
2. Bass, H., Connell, E. H., & Wright, D. (1982). *The Jacobian conjecture: reduction of degree and formulation of equations.* Bull. Amer. Math. Soc. DOI:10.1090/S0273-0979-1982-15032-7. [high-confidence]
3. Yagzhev, A. V. (c. 1980). *Keller's problem and the reduction to cubic maps.* [needs-verification]
4. Abhyankar, S. S., & Moh, T. T. (1975). *Embeddings of the line in the plane (Abhyankar–Moh theorem).* [high-confidence]
5. Moh, T. T. (1983). *On the global injectivity of polynomial maps; degree $\le 100$ in dimension 2.* [needs-verification]
6. Drużkowski, L. M. (1983). *The Jacobian conjecture in the case of cubic-linear maps.* [needs-verification]
7. Wang, S. S.-S. (1980). *Injectivity of polynomial maps and the quadratic case.* [needs-verification]
8. Smale, S. (1998). *Mathematical problems for the next century.* DOI:10.1007/BF03025291. [high-confidence]
9. van den Essen, A. (2000). *Polynomial Automorphisms and the Jacobian Conjecture* (Progress in Math. 190, monograph). [high-confidence]
10. de Bondt, M., & van den Essen, A. (2003). *Nilpotent Jacobians and the Jacobian conjecture in low dimension.* [needs-verification]
11. Shestakov, I., & Umirbaev, U. (2004). *The Nagata automorphism is wild.* DOI:10.1090/S0894-0347-03-00440-5. [high-confidence]
12. de Bondt, M., & van den Essen, A. (2005). *A reduction of the Jacobian conjecture to the symmetric case.* [needs-verification]
13. Zhao, W. (2005). *Hessian nilpotent polynomials and the Jacobian conjecture.* [needs-verification]
14. Belov-Kanel, A., & Kontsevich, M. (2007). *The Jacobian conjecture is stably equivalent to the Dixmier conjecture.* [high-confidence]
15. Zhao, W. (2012). *A vanishing conjecture on differential operators with constant coefficients.* [needs-verification]

## AI Review Panel

### Claude (Anthropic) — in-house review

This is a careful, intellectually honest survey. Its principal strength is that it consistently distinguishes what is proven (degree reduction, degree-2, Moh's plane theorem, the Dixmier and vanishing-conjecture equivalences, Shestakov–Umirbaev wildness) from what is conjectural, and it never inflates an equivalence into a step toward solution. The "barrier" framing per approach is apt, and the emphasis on the local-to-global gap as the recurring obstruction matches the field's own diagnosis. The treatment of retracted general proofs as a negative signal — rather than ignoring or relitigating them — is exactly right for a problem with this reputation.

Three concrete reservations. (i) Most non-canonical references carry `needs-verification` or `ai-suggested` flags in the source dossier, and the reference list above preserves that uncertainty deliberately: the Yagzhev, Drużkowski, Wang, Moh, and several Zhao and de Bondt–van den Essen entries have reconstructed titles/years/venues that must be checked against primary sources (MathSciNet/zbMATH/publisher records) before any downstream citation. Even the high-confidence DOIs should be confirmed against the publisher record. (ii) Several characterizations of the Belov-Kanel–Kontsevich equivalence and Zhao's vanishing conjecture lean on a small number of sources and on the dossier's own paraphrase; the precise statement of "stable equivalence" ($\mathrm{JC}_{2n}\Leftrightarrow\mathrm{DC}_n$ in the limit) and the exact hypotheses of the vanishing conjecture should be verified against the original papers, since loose paraphrase here could overstate how tight or how directional these links are. (iii) The inverse-degree bound $\deg F^{-1}\le(\deg F)^{n-1}$ is stated as a clean fact; its precise attribution and hypotheses warrant a source check.

The single most important thing a human reviewer should verify: the exact logical form and directionality of the Belov-Kanel–Kontsevich equivalence and Zhao's vanishing-conjecture equivalence, because these "equivalent reformulation" claims do the heaviest load-bearing work in Sections 2–5 and are the easiest place for a survey to subtly overstate.

**Verdict:** accept-with-revisions.

### GPT (OpenAI) — pending
_Not yet run. To complete the panel, run the prompt in docs/review/REVIEW-TEMPLATE.md through GPT and record the verdict here and in the front matter._

### Gemini (Google) — pending
_Not yet run. See docs/review/REVIEW-TEMPLATE.md._

### Grok (xAI) — pending
_Not yet run. See docs/review/REVIEW-TEMPLATE.md._

## Human verification

AI review is not human peer review. The panel above reflects automated assessment only and may miss errors that a domain expert would catch, particularly in citation accuracy and the precise statements of the Dixmier and vanishing-conjecture equivalences. This meta-analysis is offered for academic verification per ../docs/review/ACADEMIC-REVIEW.md. Status: human_review pending.

---
*Accredited to **Alexander Donahue** · The Unsolved Mathematics Atlas · CC BY 4.0. Cite per CITATION.cff.*

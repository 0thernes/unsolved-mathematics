---
title: "Meta-Analysis: The Fontaine–Mazur Conjecture"
slug: fontaine-mazur-conjecture
author: Alexander Donahue
type: ai-assisted-meta-analysis
peer_reviewed: false
problem_status: active-progress
ai_review:
  claude:
    verdict: accept-with-revisions
    date: "2026-06-14"
    version: "claude-opus-4-8"
    summary: "A faithful, well-mapped survey of an open conjecture whose GL_2/Q case is morally settled, but whose references and a few hedged claims require primary-source verification."
  gpt:
    verdict: pending
  gemini:
    verdict: pending
  grok:
    verdict: pending
human_review: pending
---

# Meta-Analysis: The Fontaine–Mazur Conjecture

> **AI-generated meta-analysis — not peer-reviewed.** Curated and accredited by **Alexander Donahue** (human-in-the-loop). A survey/assessment of an open problem; it makes no claim of a new result. Citations carry verification flags and require human source-checking.

## Abstract

The Fontaine–Mazur conjecture (1995) asserts an intrinsic, local-at-$p$ characterization of which $p$-adic Galois representations of a number field "come from geometry." Precisely, a continuous irreducible $\rho: G_{\mathbb{Q}} \to \mathrm{GL}_n(\overline{\mathbb{Q}_p})$ that is unramified outside a finite set of primes and de Rham at $p$ should, up to twist, be a subquotient of the étale cohomology of a smooth projective variety — and, conjecturally, arise from an automorphic representation. It fuses Fontaine's $p$-adic Hodge theory with the Langlands program, yielding the slogan "geometric $\Leftrightarrow$ automorphic." This meta-analysis surveys the source dossier: the unconditional $\mathrm{GL}_2/\mathbb{Q}$ case (Kisin 2009; Emerton's completed cohomology), the residual-modularity input from Serre's conjecture (Khare–Wintenberger), and the conditional or potential results in higher rank (potential automorphy; Calegari–Geraghty; Scholze's torsion construction). It identifies the two dominant obstructions — the absence of a $p$-adic local Langlands correspondence beyond $\mathrm{GL}_2(\mathbb{Q}_p)$ and the lack of unconditional local–global compatibility for Galois representations in torsion cohomology — and offers a skeptical assessment. The problem remains open; no counterexample is known and the community consensus holds the conjecture true and deep.

## 1. Statement and significance

Let $\rho: G_{\mathbb{Q}} \to \mathrm{GL}_n(\overline{\mathbb{Q}_p})$ be continuous and irreducible. Call $\rho$ **geometric** if it is unramified outside finitely many primes and its restriction to a decomposition group at $p$ is de Rham in Fontaine's sense. The conjecture predicts every geometric $\rho$ is, up to cyclotomic twist, a subquotient of $H^i_{\text{ét}}(X_{\overline{\mathbb{Q}}}, \mathbb{Q}_p)$ for some smooth projective $X/\mathbb{Q}$, and conjecturally automorphic. Its significance is organizational: it recasts Wiles' modularity theorem as one instance of a vast principle linking $p$-adic Hodge theory and the Langlands philosophy. The dimension-two corollary — an odd, irreducible, Hodge–Tate regular geometric $\rho$ into $\mathrm{GL}_2$ is modular — connects directly to elliptic curves and modular forms. The conjecture's converse content is equally pointed: representations that are *not* de Rham at $p$ should not be geometric, excluding "exotic" sources.

## 2. State of the art

The flagship **$\mathrm{GL}_2/\mathbb{Q}$** case is, per the dossier, "morally settled." Kisin (2009) proved that an irreducible, odd, de-Rham-at-$p$, Hodge–Tate regular $\rho: G_{\mathbb{Q}} \to \mathrm{GL}_2(\overline{\mathbb{Q}_p})$ is modular, outside a short list of degenerate residual situations, via local deformation rings and $p$-adic local Langlands for $\mathrm{GL}_2(\mathbb{Q}_p)$ (Breuil, Colmez). Emerton's completed-cohomology / local–global compatibility approach gives an independent proof of large parts of the same statement. The residual modularity these methods presuppose is furnished unconditionally over $\mathbb{Q}$ by Serre's conjecture (Khare–Wintenberger, 2009). Together with Breuil–Conrad–Diamond–Taylor (2001), this delivers automorphy for every elliptic curve over $\mathbb{Q}$ and essentially every regular odd two-dimensional geometric representation of $G_{\mathbb{Q}}$.

In higher rank and over general fields, results are **conditional or potential**. Potential automorphy (Taylor and collaborators; the "ten-author" potential-automorphy-over-CM-fields work, 2023) establishes automorphy after base change for regular, essentially self-dual representations — enough for Sato–Tate, weaker than the conjecture over the base field. Calegari–Geraghty (2018) extend modularity lifting to defect $\ell_0 > 0$ but contingent on expected properties of torsion Galois representations and on local–global compatibility at $p$. Scholze's perfectoid construction supplies Galois representations attached to torsion classes but not, in general, the local conditions to close the argument.

## 3. Principal approaches and barriers

**Modularity lifting (Taylor–Wiles–Kisin patching).** Mazur's deformation theory packages geometric lifts of a fixed residual $\bar\rho$ into a universal ring $R$; the goal is $R = \mathbb{T}$. *Barrier:* requires a residual-modularity starting point (no higher-rank analogue of Serre), Hodge–Tate regularity, and oddness/self-duality; the Calegari–Geraghty defect $\ell_0 > 0$ breaks naive patching.

**$p$-adic local Langlands.** Kisin and Emerton convert the local de Rham condition at $p$ into automorphic vectors inside completed cohomology. *Barrier:* a usable correspondence is known essentially only for $\mathrm{GL}_2(\mathbb{Q}_p)$; nothing comparable exists for $\mathrm{GL}_2(F)$, $F \neq \mathbb{Q}_p$, or $\mathrm{GL}_n$, $n \ge 3$.

**Potential automorphy and the "$p,q$ switch."** Prove modularity after an unknown CM/totally real base change. *Barrier:* "potential" is weaker than the base-field claim and confined to essentially self-dual (polarizable) representations.

**Derived deformations and completed cohomology.** Calegari–Geraghty derived Hecke algebras and Scholze's torsion construction open non-self-dual cases in principle. *Barrier:* largely conditional on torsion Galois-representation conjectures and integral $p$-adic local Langlands input unavailable beyond $\mathrm{GL}_2(\mathbb{Q}_p)$.

The conjecture also makes **non-existence** predictions (no geometric representation that is non-de-Rham at $p$) which serve as consistency checks; no counterexample and no obstruction theorem against the conjecture is known. The difficulty is uniformly one of construction.

## 4. Critical assessment

The dossier's framing is sober and, on internal evidence, accurate: this is a problem of incremental, peer-reviewed progress rather than contested claims. The central honest caveat is correctly foregrounded — that Kisin's $\mathrm{GL}_2/\mathbb{Q}$ theorem carries genuine hypotheses (regularity, oddness, avoidance of degenerate residual local shapes, weight-one and small-image exclusions), so the two-dimensional case is "essentially" but not "completely" resolved. The treatment of the Calegari–Geraghty obstruction is the dossier's analytic high point: it correctly identifies that many higher-rank results are *theorems-modulo-conjectures*, not unconditional, which is the single most important distinction a reader must retain.

Two reservations. First, the dossier relies heavily on a coherent "two missing pillars" narrative ($p$-adic local Langlands beyond $\mathrm{GL}_2(\mathbb{Q}_p)$; unconditional torsion local–global compatibility). This is a fair expert consensus, but it is a *consensus*, and the meta-analysis should not let narrative tidiness substitute for the messier reality that the frontier (Fargues–Scholze geometrization, derived deformation, spectral action) may reshape what "the obstruction" even is. Second, several specific attributions and especially the precise scope of each cited theorem are stated with more confidence than the flagged references warrant.

## 5. What a resolution would require / open directions

Per the dossier, a full resolution needs: (1) a **$p$-adic local Langlands correspondence beyond $\mathrm{GL}_2(\mathbb{Q}_p)$** — the dominant obstruction; (2) **unconditional local–global compatibility** and full control of Galois representations in torsion cohomology, removing conditionality from Calegari–Geraghty-type theorems; (3) a path to the **non-self-dual** case, where no Shimura variety directly produces the representation; and (4) removal of the **regularity and oddness** hypotheses, reaching irregular/weight-one and even-image situations. The most active routes are derived-deformation programs (Calegari–Geraghty; Gee–Newton), the categorical geometrization of local Langlands (Fargues–Scholze) feeding a spectral-action approach, and continued extension of potential automorphy. A clean general theorem most plausibly awaits a usable higher-rank $p$-adic local Langlands, which the dossier judges years to decades away.

## 6. Selected references

1. Jean-Marc Fontaine, *Sur certains types de représentations $p$-adiques du groupe de Galois d'un corps local* (1982). [high-confidence]
2. Barry Mazur, *Deforming Galois Representations* (1988). [high-confidence]
3. Jean-Marc Fontaine, *Le corps des périodes $p$-adiques* (1989). [high-confidence]
4. Jean-Marc Fontaine, *Représentations $p$-adiques semi-stables* (1990). [high-confidence]
5. Jean-Marc Fontaine, Barry Mazur, *Geometric Galois Representations* (1995). [high-confidence]
6. Andrew Wiles, *Modular elliptic curves and Fermat's Last Theorem* (1995), doi:10.2307/2118559. [high-confidence]
7. Richard Taylor, Andrew Wiles, *Ring-theoretic properties of certain Hecke algebras* (1995), doi:10.2307/2118560. [high-confidence]
8. C. Breuil, B. Conrad, F. Diamond, R. Taylor, *On the modularity of elliptic curves over $\mathbb{Q}$: wild 3-adic exercises* (1999), doi:10.1090/S0894-0347-01-00370-8. [high-confidence]
9. Kazuya Kato, *$p$-adic Hodge theory and values of zeta functions of modular forms* (2003). [high-confidence]
10. Mark Kisin, *The Fontaine–Mazur conjecture for $\mathrm{GL}_2$* (2009), doi:10.1090/S0894-0347-09-00628-6. [high-confidence]
11. Pierre Colmez, *Représentations de $\mathrm{GL}_2(\mathbb{Q}_p)$ et $(\varphi,\Gamma)$-modules* (2009). [high-confidence]
12. Chandrashekhar Khare, Jean-Pierre Wintenberger, *Serre's modularity conjecture (I) & (II)* (2009), doi:10.1007/s00222-009-0205-7. [high-confidence]
13. Matthew Emerton, *Local–global compatibility and the $p$-adic Langlands programme for $\mathrm{GL}_2/\mathbb{Q}$* (2014). [needs-verification]
14. Peter Scholze, *On torsion in the cohomology of locally symmetric varieties* (2015), doi:10.4007/annals.2015.182.3.1. [high-confidence]
15. Frank Calegari, David Geraghty, *Modularity lifting beyond the Taylor–Wiles method* (2018), doi:10.1007/s00222-017-0749-x. [high-confidence]
16. A. Allen, F. Calegari, A. Caraiani, et al., *Potential automorphy over CM fields* (2023), doi:10.4007/annals.2023.197.3.3. [needs-verification]

## AI Review Panel

### Claude (Anthropic) — in-house review

The meta-analysis is faithful to its dossier and well-calibrated to the genre. Its strengths are real: it correctly separates the unconditional $\mathrm{GL}_2/\mathbb{Q}$ result from the conditional higher-rank program, it foregrounds the Calegari–Geraghty defect-$\ell_0$ obstruction as the analytic crux rather than burying it, and it never overstates the global situation — the conjecture is presented as open, with the two-dimensional case "morally" but not completely settled. The "geometric $\Leftrightarrow$ automorphic" framing is standard and the converse (non-existence) content is handled with appropriate restraint.

Three flags for a human referee. (i) Every cited reference inherits the dossier's verification status, and several entries — notably Emerton's completed-cohomology papers (which appeared across multiple venues with varying scope), the "ten-author" CM-fields paper, and the precise DOI/year pairings — are marked needs-verification; the DOIs and the exact theorem each paper proves must be checked against primary sources before any downstream use. I dropped the dossier's explicit placeholder row (the Skinner–Wiles "almost ordinary" pointer) from the reference list precisely because it was an unverified pointer, not a citation. (ii) The "two missing pillars" narrative, while genuine expert consensus, is single-thread: the document leans on one organizing story for why the general case is hard, and a referee should confirm it is not flattening live alternative framings (Fargues–Scholze, spectral action). (iii) The single most important thing to verify: the precise hypotheses and scope of Kisin (2009) — regularity, oddness, the excluded degenerate residual local shapes, and weight-one/small-image cases — since the entire "essentially settled" claim rests on stating those exclusions correctly and not overstating coverage.

The survey makes no claim of settling the conjecture, and I detect no fabricated identifier; the unverifiable ones are honestly flagged. The remaining risk is precision of attribution, not invention.

**Verdict:** accept-with-revisions.

### GPT (OpenAI) — pending
_Not yet run. To complete the panel, run the prompt in docs/review/REVIEW-TEMPLATE.md through GPT and record the verdict here and in the front matter._

### Gemini (Google) — pending
_Not yet run. See docs/review/REVIEW-TEMPLATE.md._

### Grok (xAI) — pending
_Not yet run. See docs/review/REVIEW-TEMPLATE.md._

## Human verification

AI review is not human peer review. This assessment is offered for academic verification per ../docs/review/ACADEMIC-REVIEW.md, and its citations, theorem scopes, and identifiers require checking against primary sources by a qualified human reviewer. Status: human_review pending.

---
*Accredited to **Alexander Donahue** · The Unsolved Mathematics Atlas · CC BY 4.0. Cite per CITATION.cff.*

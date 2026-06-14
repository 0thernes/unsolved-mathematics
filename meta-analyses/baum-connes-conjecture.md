---
title: "Meta-Analysis: The Baum–Connes Conjecture"
slug: baum-connes-conjecture
author: Alexander Donahue
type: ai-assisted-meta-analysis
peer_reviewed: false
problem_status: active-progress
ai_review:
  claude:
    verdict: accept-with-revisions
    date: "2026-06-14"
    version: "claude-opus-4-8"
    summary: "An accurate, well-scoped survey of a genuinely open conjecture; the technical narrative is sound, but every citation carries an explicit verification flag and the unproven higher-rank frontier must not be blurred with the proven special cases."
  gpt:
    verdict: pending
  gemini:
    verdict: pending
  grok:
    verdict: pending
human_review: pending
---

# Meta-Analysis: The Baum–Connes Conjecture

> **AI-generated meta-analysis — not peer-reviewed.** Curated and accredited by **Alexander Donahue** (human-in-the-loop). A survey/assessment of an open problem; it makes no claim of a new result. Citations carry verification flags and require human source-checking.

## Abstract

The Baum–Connes conjecture asserts that for every second-countable locally compact group $G$ the assembly (analytic index) map $\mu\colon K^G_*(\underline{E}G)\to K_*(C^*_r(G))$ from the equivariant $K$-homology of the classifying space for proper actions to the $K$-theory of the reduced group $C^*$-algebra is an isomorphism. Formulated by Paul Baum and Alain Connes in 1982 and given its modern $\underline{E}G$ shape with Nigel Higson in 1994, it unifies index theory, noncommutative geometry, and coarse geometry, and implies the strong Novikov and (for torsion-free $G$) Kadison–Kaplansky idempotent conjectures. This meta-analysis surveys the problem's history, the principal proof strategies — Kasparov's Dirac–dual-Dirac method, Higson–Kasparov for a-T-menable groups, Lafforgue's Banach $KK$-theory for Property (T) and hyperbolic groups, and the Meyer–Nest categorical reformulation — and the central obstruction. It records that the conjecture is verified in vast generality, has no known counterexample, yet remains open for higher-rank lattices such as $SL_3(\mathbb{Z})$, while its strong "with coefficients" form is provably false. All cited references carry verification flags and require primary-source confirmation.

## 1. Statement and significance

Let $G$ be a second-countable locally compact (Hausdorff) group. The conjecture states that the assembly map
$$\mu\colon K^G_*(\underline{E}G)\longrightarrow K_*(C^*_r(G))$$
is an isomorphism, where $\underline{E}G$ is the classifying space for proper $G$-actions and $C^*_r(G)$ is the reduced group $C^*$-algebra. Geometrically it says every $K$-theory class of $C^*_r(G)$ is the index of a $G$-equivariant elliptic operator, with no relations beyond the geometric ones — a "no exotic $K$-theory" statement. Its significance is that of a hub: it implies the strong Novikov conjecture (homotopy invariance of higher signatures), the Kadison–Kaplansky idempotent conjecture for torsion-free $G$, and portions of the Gromov–Lawson–Rosenberg positive-scalar-curvature program; for connected and almost-connected Lie groups it specializes to the Connes–Kasparov isomorphism. The standard modern reference is the 1994 Baum–Connes–Higson Oberwolfach survey, which fixed the $\underline{E}G$ formulation needed to accommodate torsion.

## 2. State of the art

The honest status is **active progress, open in general, no known counterexample to the plain conjecture, and the coefficient version refuted.** Unconditionally proven cases include: all a-T-menable (Haagerup) groups — amenable, free, one-relator with torsion, Coxeter — with coefficients (Higson–Kasparov, 2001); many Property (T) groups including cocompact lattices in $Sp(n,1)$ and rank-one groups (Lafforgue, 2002); all Gromov-hyperbolic groups and their lattices, with coefficients (Lafforgue, 2012, via strong Property (T)); almost-connected and reductive $p$-adic groups (Chabert–Echterhoff–Nest, 2003); and groups acting properly on bolic spaces, CAT(0) spaces, trees, and buildings. On the injectivity (Novikov) side, every group that coarsely embeds into Hilbert space, or has finite asymptotic dimension or Property A, satisfies injectivity (Yu and successors). The open frontier is the surjectivity ("exotic $K$-theory") half for higher-rank lattices — $SL_n(\mathbb{Z})$ for $n\ge 3$ and lattices in higher-rank simple $p$-adic groups — where no current technique reaches surjectivity.

## 3. Principal approaches and barriers

**Dirac–dual-Dirac (Kasparov).** Construct Dirac $\alpha\in KK^G(C_0(X),\mathbb{C})$ and dual-Dirac $\beta\in KK^G(\mathbb{C},C_0(X))$ on a proper $G$-space $X$ whose product $\gamma=\beta\otimes\alpha$ is an idempotent in $KK^G(\mathbb{C},\mathbb{C})$; if $\gamma=1$, assembly is an isomorphism. *Barrier:* for Property (T) groups $\gamma\neq 1$ in $C^*$-theory — a genuine obstruction.

**Haagerup property (Higson–Kasparov).** A proper affine-isometric Hilbert-space action forces $\gamma=1$ via infinite-dimensional Bott periodicity, yielding the conjecture with coefficients. *Barrier:* Property (T) is exactly the negation of the Haagerup property, so the route is structurally blind to higher-rank lattices.

**Banach $KK$-theory (Lafforgue).** Replacing $C^*$-algebra $KK$ by a Banach/unconditional-completion version dissolves the Property-(T) obstruction because representations need not be unitary; strong Property (T) (2012) then reaches all hyperbolic groups. *Barrier:* higher-rank lattices satisfy strong forms of Property (T) obstructing even the Banach approach.

**Coarse geometry / Property A (Yu; Skandalis–Tu–Yu).** Coarse embeddability into Hilbert space yields injectivity and Novikov for an enormous class. *Barrier:* Gromov monster groups containing expanders do not coarsely embed.

**Categorical reformulation (Meyer–Nest).** Assembly is the localization of the equivariant Kasparov category at the compactly-induced subcategory, with a spectral sequence converging to $K_*(C^*_r G)$; this explains the failure with coefficients as a non-vanishing derived term. *Barrier:* it reorganizes rather than removes the analytic difficulty for Property (T) groups.

## 4. Critical assessment

The defining structural fact is the **Higson–Lafforgue–Skandalis counterexample (2003)**: the conjecture *with coefficients* is false, because Gromov monster groups containing coarsely embedded expanders break exactness of the reduced crossed product, destroying surjectivity. This is a genuinely proven negative result about a strengthening, and it must be stated precisely: it refutes the coefficient version, not the plain conjecture, but it permanently rules out any proof of the plain conjecture that reduces to the coefficient version in full generality. It identifies non-exactness, expanders, and Property (T) as the true enemy of a uniform method.

A second clarification the literature now treats as settled: Property (T) is *not* itself an obstruction. The early intuition that Property (T) groups might be counterexamples was reversed by Lafforgue, definitively for hyperbolic groups. The remaining wall is the conjunction of higher rank with strong Property (T) and bad coarse geometry, where both the unitary and the Banach routes stall. The dossier's framing — confirmed in vast generality, refuted only in its strongest coefficient form, open for higher-rank lattices — is accurate and appropriately cautious. The principal risk in a survey like this is rhetorical drift between "proven for class X" and "expected to hold," and between the with- and without-coefficient statements; this document keeps them distinct.

## 5. What a resolution would require / open directions

A full proof must handle an arbitrary second-countable locally compact $G$ without the Haagerup property and past strong Property (T) — producing either a surjectivity argument or an obstruction-killing element in the regime of $SL_3(\mathbb{Z})$, $SL_n(\mathbb{Z})$ ($n\ge3$), and higher-rank $p$-adic lattices. In the Meyer–Nest picture, one must show the derived obstruction term vanishes there. Plausible routes: (1) extending Lafforgue's strong-Property-(T) / Banach-$KK$ technology to higher-rank lattices — the most direct attack but reliant on hard Banach representation theory; (2) higher-rank Mackey-analogy / deformation methods relating $SL_n(\mathbb{Z})$ to motion-group degenerations; (3) categorical vanishing results isolating and killing the obstruction class; (4) coarse-geometric advances handling expander-containing groups for the reduced theory. A resolution would simultaneously settle Novikov and Kadison–Kaplansky for these groups.

## 6. Selected references

1. M. Pimsner, D. Voiculescu, *Exact sequences for K-groups and Ext-groups of certain cross-product C\*-algebras* (1980). [high-confidence]
2. P. Baum, A. Connes, *Geometric K-theory for Lie groups and foliations* (1982). [high-confidence]
3. A. Connes, G. Skandalis, *The longitudinal index theorem for foliations* (1984). [high-confidence]
4. G. G. Kasparov, *Equivariant KK-theory and the Novikov conjecture* (1988). [high-confidence]
5. P. Baum, A. Connes, N. Higson, *Classifying space for proper actions and K-theory of group C\*-algebras* (1994). [high-confidence]
6. G. Yu, *The coarse Baum–Connes conjecture for spaces which admit a uniform embedding into Hilbert space* (2000). [high-confidence]
7. N. Higson, G. Kasparov, *E-theory and KK-theory for groups which act properly and isometrically on Hilbert space* (2001). [high-confidence]
8. V. Lafforgue, *K-théorie bivariante pour les algèbres de Banach et conjecture de Baum–Connes* (2002). [high-confidence]
9. N. Higson, V. Lafforgue, G. Skandalis, *Counterexamples to the Baum–Connes conjecture* (2003). [high-confidence]
10. J. Chabert, S. Echterhoff, R. Nest, *The Baum–Connes conjecture for almost-connected groups and for linear p-adic groups* (2003). [high-confidence]
11. G. Skandalis, J.-L. Tu, G. Yu, *Expanders, exact crossed products, and the Baum–Connes conjecture* (2004). [needs-verification]
12. R. Meyer, R. Nest, *The Baum–Connes conjecture via localisation of categories* (2008), DOI 10.1016/j.top.2006.05.001. [needs-verification]
13. V. Lafforgue, *La conjecture de Baum–Connes à coefficients pour les groupes hyperboliques* (2012). [high-confidence]
14. R. Willett, G. Yu, *Higher index theory and the Baum–Connes conjecture* (lecture notes, 2015). [needs-verification]
15. P. Hochs, H. Wang, *The Connes–Kasparov isomorphism for reductive Lie groups* (2019). [needs-verification]

## AI Review Panel

### Claude (Anthropic) — in-house review

The survey is technically sound and well calibrated to the dossier. Its strongest feature is the disciplined separation of three things that are easy to conflate: the plain conjecture (open in general), the with-coefficients version (proven false by Higson–Lafforgue–Skandalis), and the long list of confirmed special cases. The treatment of the obstruction — that Property (T) was once feared as the wall but was circumvented by Lafforgue, leaving the genuine enemy as the conjunction of higher rank, strong Property (T), and expander-driven non-exactness — matches the current consensus and avoids the common error of calling Property (T) groups counterexamples.

Three cautions. (i) Every reference here carries an explicit verification flag, and several core anchors are recorded without DOIs or precise volume data by deliberate choice; the with-coefficient counterexample (GAFA 2003), the Higson–Kasparov theorem (Inventiones 2001), and Lafforgue's Fields-Medal work are real and central, but exact bibliographic identifiers must be confirmed against MathSciNet/zbMATH before any downstream citation. The single DOI present (Meyer–Nest, row 12) is itself flagged needs-verification and should be checked. (ii) The narrative leans heavily on a small number of landmark theorems by a tight community; a human reviewer should confirm that the attributions (e.g., the precise scope of Lafforgue 2002 vs. 2012, and exactly which groups Chabert–Echterhoff–Nest covers — almost-connected and linear $p$-adic of characteristic zero) are stated with the correct hypotheses, since over-broad paraphrase is the main risk. (iii) The single most important thing to verify: that no recent (post-2020) preprint has either extended a proven case to a higher-rank lattice or, conversely, produced a counterexample to the *plain* conjecture — the claim "no known counterexample, open for higher-rank lattices" is time-sensitive and load-bearing for the entire assessment.

Subject to source-checking the flagged references and the hypotheses on the named theorems, the document is accurate, honest, and makes no claim of a new result.

**Verdict:** accept-with-revisions.

### GPT (OpenAI) — pending
_Not yet run. To complete the panel, run the prompt in docs/review/REVIEW-TEMPLATE.md through GPT and record the verdict here and in the front matter._

### Gemini (Google) — pending
_Not yet run. See docs/review/REVIEW-TEMPLATE.md._

### Grok (xAI) — pending
_Not yet run. See docs/review/REVIEW-TEMPLATE.md._

## Human verification

AI review is not human peer review. This assessment is offered for academic verification per ../docs/review/ACADEMIC-REVIEW.md and should be checked by a specialist in operator algebras and $K$-theory before being relied upon, with particular attention to the flagged citations and the precise hypotheses of the cited theorems. Status: human_review pending.

---
*Accredited to **Alexander Donahue** · The Unsolved Mathematics Atlas · CC BY 4.0. Cite per CITATION.cff.*

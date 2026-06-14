---
title: "Meta-Analysis: The Bombieri–Lang Conjecture"
slug: bombieri-lang-conjecture
author: Alexander Donahue
type: ai-assisted-meta-analysis
peer_reviewed: false
problem_status: open
ai_review:
  claude:
    verdict: accept-with-revisions
    date: "2026-06-14"
    version: "claude-opus-4-8"
    summary: "A faithful, well-structured survey of an open conjecture whose factual backbone is sound, but whose secondary citations carry verification flags and must be primary-source checked before publication."
  gpt:
    verdict: pending
  gemini:
    verdict: pending
  grok:
    verdict: pending
human_review: pending
---

# Meta-Analysis: The Bombieri–Lang Conjecture

> **AI-generated meta-analysis — not peer-reviewed.** Curated and accredited by **Alexander Donahue** (human-in-the-loop). A survey/assessment of an open problem; it makes no claim of a new result. Citations carry verification flags and require human source-checking.

## Abstract

The Bombieri–Lang conjecture is the central higher-dimensional generalization of Mordell's finiteness theorem. It predicts that a smooth projective variety $X$ of general type over a number field $K$ has rational points $X(K)$ that are not Zariski dense, with Lang's stronger geometric form locating all but finitely many points inside a proper "special" locus. This meta-analysis surveys the statement, its place in the conjectural web culminating in Vojta's conjecture, and the state of the art. It remains open in every dimension $\ge 2$: no variety is known unconditionally to have non-dense rational points purely because it is of general type. The decisive partial evidence is Faltings's resolution of Mordell (1983) and of the Mordell–Lang conjecture for subvarieties of (semi)abelian varieties (1991, 1994), where an ambient group structure supplies the missing machinery. We assess the three principal approaches — Vojta-type height inequalities, the hyperbolicity/Nevanlinna analogy, and the Lawrence–Venkatesh $p$-adic period method — and identify the precise obstructions at which each currently terminates. The document is a survey; it asserts no new theorem.

## 1. Statement and significance

Mordell conjectured in 1922 that a smooth projective curve of genus $g \ge 2$ over a number field $K$ has only finitely many $K$-rational points; such curves are exactly the one-dimensional varieties of general type. In higher dimension finiteness manifestly fails — a general-type surface may contain rational or elliptic curves carrying infinitely many points — so the correct generalization, due independently to Enrico Bombieri (a 1980 Chicago seminar, never formally published by him) and Serge Lang (across his writings of the late 1970s and 1980s), replaces "finite" by "**not Zariski dense**." For $X$ of general type (big canonical bundle $K_X$) over $K$, the weak form asserts $X(K)$ lies in a proper Zariski-closed subset. Lang's geometric refinement predicts a proper closed special set $\mathrm{Sp}(X)$, conjecturally the union of all positive-dimensional images of non-constant maps from abelian varieties, outside which points are sparse and the variety is Mordellic and Kobayashi-hyperbolic. The significance is structural: the conjecture encodes the thesis that birational positivity governs arithmetic, and it now sits beneath Vojta's 1987 conjecture, a single height/discriminant inequality that would imply it.

## 2. State of the art

The conjecture is **open** in every dimension $\ge 2$. The confirmed evidence falls into three regimes. First, the curve case: Mordell's conjecture is Faltings's 1983 theorem, with later independent proofs by Vojta (1989), Bombieri (1990), and Lawrence–Venkatesh (2020). Second, and most important for the higher-dimensional picture, **subvarieties of (semi)abelian varieties**: Faltings (1991, 1994) proved the Mordell–Lang conjecture there, confining rational points to translates of subgroups; Vojta (1996) and McQuillan (1995) gave independent proofs. This is the largest fully settled higher-dimensional family and is unconditional Bombieri–Lang whenever $X$ sits inside a group. Third, **large-monodromy families**: the Lawrence–Venkatesh period method yields genuinely new non-density and Shafarevich-type finiteness for certain varieties carrying a sufficiently non-degenerate variation of Hodge structure (e.g. Lawrence–Sawin, 2020). On the complex-analytic side, McQuillan's Green–Griffiths–Lang theorem for general-type surfaces with $c_1^2 - c_2 > 0$ and Brotbek's hyperbolicity of generic high-degree hypersurfaces (2017) confirm the geometric half of Lang's web, though these are theorems about $\mathbb{C}$ and do not transfer to number fields. Conditionally, uniform Bombieri–Lang yields the Caporaso–Harris–Mazur (1997) genus-only bound on points of curves.

## 3. Principal approaches and barriers

**Vojta-type height inequalities.** The consensus "right" route recasts the conjecture as a height inequality $h_{K_X}(P) \le \epsilon\, h_A(P) + d(P) + O(1)$ outside a proper closed subset. For $X$ of general type this confines all but finitely many points to the exceptional set. This circle of ideas — the Faltings–Vojta product theorem and index estimates — delivered the (semi)abelian Mordell–Lang results, but crucially exploits the group structure, the Néron–Tate height, and the ambient $X \times X$ geometry. For arbitrary general-type $X$ there is no substitute, and extracting the inequality is essentially equivalent to the conjecture itself.

**Hyperbolicity and the Nevanlinna analogy.** Lang's program demands that arithmetic non-density mirror complex hyperbolicity, with theorems about entire curves $\mathbb{C} \to X$ predicting the arithmetic. Strong analytic results exist (McQuillan, Demailly, Diverio–Merker–Rousseau, Brotbek). The barrier is that "hyperbolic $\Rightarrow$ Mordellic" is itself part of Lang's conjecture; the analogy is heuristic, and the arithmetic bridge is missing.

**$p$-adic period maps.** Lawrence–Venkatesh (2020) reproved Mordell via the variation of $p$-adic Galois representations in a family over $X$, producing new higher-dimensional finiteness. The method needs a family with a non-degenerate period map; a general variety of general type carries none, so it proves special cases.

**Geometry of the special set** (minimal model program, Campana's orbifold theory) clarifies $\mathrm{Sp}(X)$ but supplies no mechanism converting "outside the special set" into finiteness without Vojta-type input.

## 4. Critical assessment

The dossier's central claim — that the conjecture is open in every dimension $\ge 2$, with the (semi)abelian and large-monodromy families as the only unconditionally settled regimes — is accurate and reflects the field's working consensus. The framing of Vojta's conjecture as the master inequality, and of the group structure as the precise pivot on which the Faltings–Vojta method turns, is correct and well-judged. The treatment honestly distinguishes proven related results (Faltings, Mordell–Lang) from the open target, and correctly notes that the conjecture *cannot* be strengthened to finiteness, since the exceptional locus is unavoidable.

Three points warrant caution. (i) The Caporaso–Harris–Mazur implication is stated as depending on a *uniform* Bombieri–Lang; this is right, and the dossier appropriately flags it as conditional rather than as evidence for the conjecture. (ii) The Lawrence–Venkatesh contribution is described in places via an approximate paper title (the papers.md note concedes the exact wording is uncertain); the underlying mathematics is correctly characterized, but the bibliographic detail is soft. (iii) The complex-analytic results are correctly walled off as non-transferable, which is the single most common overstatement in popular accounts of this conjecture — the dossier avoids it.

## 5. What a resolution would require / open directions

A full proof must force $X(K)$ into a proper closed subset for arbitrary general-type $X$ **without** an ambient group. Three identified routes each terminate at a hard obstruction: (i) a Vojta-type inequality on general $X$ — currently out of reach and essentially equivalent to the conjecture; (ii) a transfer principle realizing "hyperbolic $\Rightarrow$ Mordellic" — itself conjectural; (iii) a vast generalization of the period method to varieties carrying no natural family of motives. The community's working belief is that the conjecture is true and will fall, if at all, as a corollary of Vojta's conjecture or of a dramatic extension of period-theoretic methods, not via an isolated elementary argument. The most active unconditional front is the period-map lineage; the Lang–Vojta integral-point work of Corvaja–Zannier, Levin, and Autissier continues to settle special cases.

## 6. Selected references

1. L. J. Mordell (1922), *On the rational solutions of the indeterminate equations of the third and fourth degrees* [high-confidence]
2. Serge Lang (1974), *Higher dimensional Diophantine problems*, Bull. AMS [high-confidence]
3. Gerd Faltings (1983), *Endlichkeitssätze für abelsche Varietäten über Zahlkörpern* [high-confidence]
4. Serge Lang (1986), *Hyperbolic and Diophantine analysis*, Bull. AMS [high-confidence]
5. Paul Vojta (1987), *Diophantine Approximations and Value Distribution Theory* [high-confidence]
6. Enrico Bombieri (1990), *The Mordell conjecture revisited* [high-confidence]
7. Gerd Faltings (1991), *Diophantine approximation on abelian varieties* [high-confidence]
8. Serge Lang (1991), *Number Theory III: Diophantine Geometry* (Encyclopaedia survey) [high-confidence]
9. Gerd Faltings (1994), *The general case of S. Lang's conjecture* [high-confidence]
10. Michael McQuillan (1995), *Division points on semi-abelian varieties* [needs-verification]
11. Paul Vojta (1996), *Integral points on subvarieties of semiabelian varieties, I* [needs-verification]
12. L. Caporaso, J. Harris, B. Mazur (1997), *Uniformity of rational points*, J. Amer. Math. Soc., doi:10.1090/S0894-0347-97-00195-1 [high-confidence]
13. Frédéric Campana (2008), *Orbifolds, special varieties and classification theory* [needs-verification]
14. M. Hindry, J. Silverman (2016), *Diophantine geometry: an introduction* [high-confidence]
15. Damian Brotbek (2017), *Hyperbolicity of generic high-degree hypersurfaces in projective space*, doi:10.1007/s10240-017-0090-3 [needs-verification]
16. Brian Lawrence, Akshay Venkatesh (2020), *period maps and Diophantine geometry (Mordell via $p$-adic Hodge theory)*, Invent. Math., doi:10.1007/s00222-020-00966-7 [needs-verification]
17. Brian Lawrence, Will Sawin (2020), *Shafarevich-type theorems for hypersurfaces in abelian varieties* [needs-verification]

## AI Review Panel

### Claude (Anthropic) — in-house review

The survey is faithful to the mathematics and avoids the field's most common traps. Its strengths are real: it correctly identifies the group structure as the exact technical pivot separating the proven (semi)abelian Mordell–Lang results from the open general case; it keeps the complex-analytic hyperbolicity theorems firmly walled off as non-transferable to number fields, rather than smuggling them in as near-proofs; and it is scrupulous about the conditional status of the Caporaso–Harris–Mazur uniformity corollary. The placement of the conjecture beneath Vojta's inequality is the standard and correct organizing frame.

I flag three things for the human curator. First, the secondary bibliography carries explicit verification flags, and they are load-bearing: the Vojta (1996), McQuillan (1995), Campana, Brotbek, Lawrence–Venkatesh, and Lawrence–Sawin entries are real, canonical works, but their exact titles, venues, and identifiers are *not* confirmed here — the Lawrence–Venkatesh title in particular is acknowledged in the dossier to be approximate, and the cited DOI should be checked against the published *Inventiones* article before any citation is relied upon. Second, there is a single-source character to several historical claims (notably Bombieri's unpublished 1980 Chicago formulation), which by its nature cannot be primary-source-verified from a paper and rests on Lang's transmission; this should be presented as such. Third, the most important item for a human reviewer to verify is the precise scope of what Faltings (1994) and the Lawrence–Sawin/period methods actually establish as *unconditional Bombieri–Lang* versus Mordell–Lang or Shafarevich-type statements — these are closely related but not identical, and a careless reading could overstate how much of the conjecture is settled.

None of these are mathematical errors in the survey; they are verification and emphasis concerns appropriate to a non-peer-reviewed document. The factual backbone is sound and the open status is stated correctly and repeatedly.

**Verdict:** accept-with-revisions.

### GPT (OpenAI) — pending
_Not yet run. To complete the panel, run the prompt in docs/review/REVIEW-TEMPLATE.md through GPT and record the verdict here and in the front matter._

### Gemini (Google) — pending
_Not yet run. See docs/review/REVIEW-TEMPLATE.md._

### Grok (xAI) — pending
_Not yet run. See docs/review/REVIEW-TEMPLATE.md._

## Human verification

AI review is not human peer review. This meta-analysis is offered for academic verification per ../docs/review/ACADEMIC-REVIEW.md; the AI panel above is an aid to, not a substitute for, expert source-checking of every flagged citation and historical claim. Status: human_review pending.

---
*Accredited to **Alexander Donahue** · The Unsolved Mathematics Atlas · CC BY 4.0. Cite per CITATION.cff.*

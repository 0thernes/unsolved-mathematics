---
title: "Meta-Analysis: Köthe's Conjecture"
slug: kothe-conjecture
author: Alexander Donahue
type: ai-assisted-meta-analysis
peer_reviewed: false
problem_status: open
ai_review:
  claude:
    verdict: accept-with-revisions
    date: "2026-06-14"
    version: "claude-opus-4-8"
    summary: "A faithful, well-structured survey of an open ring-theory conjecture whose reformulations are accurately reported, but whose later citations carry self-declared verification flags and need primary-source checking before publication."
  gpt:
    verdict: pending
  gemini:
    verdict: pending
  grok:
    verdict: pending
human_review: pending
---

# Meta-Analysis: Köthe's Conjecture

> **AI-generated meta-analysis — not peer-reviewed.** Curated and accredited by **Alexander Donahue** (human-in-the-loop). A survey/assessment of an open problem; it makes no claim of a new result. Citations carry verification flags and require human source-checking.

## Abstract

Köthe's conjecture (1930) asserts that a ring with no nonzero nil two-sided ideal also has no nonzero nil one-sided ideal — equivalently, that the sum of two nil left ideals is nil, and that the upper nil radical $\mathrm{Nil}^*(R)$ already absorbs all one-sided nilness. It is among the oldest unresolved questions in the radical theory of associative noncommutative rings. This meta-analysis surveys the conjecture's statement, its remarkable web of equivalent reformulations, the partial results that establish it for tractable classes, and the structural obstruction that has kept it open for nearly a century. The decisive technical pivot is Krempa's 1972 reduction: the conjecture holds iff $M_2(R)$ is nil for every nil ring $R$, iff $R[x]$ is Jacobson radical for every nil $R$. Positive results cover PI-rings, rings with chain conditions, and algebras over uncountable fields. The negative frontier is shaped by Smoktunowicz's constructions, which disprove the natural strengthening "$R$ nil $\Rightarrow R[x]$ nil" while leaving Köthe's weaker target standing. The consensus is that resolution awaits a genuinely new method for controlling unbounded nil index. The document is a survey; it claims no new result.

## 1. Statement and significance

Let $R$ be an associative (generally noncommutative, not necessarily unital) ring. An ideal is *nil* if each of its elements is nilpotent. Köthe's conjecture states: if $R$ has no nonzero nil two-sided ideal, then it has no nonzero nil one-sided ideal. Equivalently — in its most-quoted symmetric form — the sum of two nil left ideals of any ring is again nil, so that the upper nil radical $\mathrm{Nil}^*(R)$ (the sum of all nil two-sided ideals) contains every nil one-sided ideal.

The conjecture sits precisely at the fault line where the *element-wise* and *one-sided* notion of nilness meets the *two-sided* requirement of a clean Kurosh–Amitsur radical theory. Wedderburn–Artin theory handles the Artinian case via the nilpotent radical; nil ideals are the natural non-Artinian generalization, and Köthe's question is whether one-sidedness generates "extra" nilness beyond the two-sided radical. Its significance is amplified by the gap between the lower nil (prime) radical $\mathrm{Nil}_*$ and the upper nil radical $\mathrm{Nil}^*$, and by the fact that the Jacobson radical contains $\mathrm{Nil}^*$ but can be strictly larger.

## 2. State of the art

The conjecture is **open** in full generality (status per metadata: `open`). It is established unconditionally in several classes:

- **PI-rings.** True: nil one-sided ideals in rings satisfying a polynomial identity are locally nilpotent (Levitzki; Amitsur–Levitzki; Kaplansky), the strongest robust positive class.
- **Chain-condition rings.** True for right/left Noetherian, Goldie, and Krull-dimension rings, via Levitzki's theorem that a nil one-sided ideal under ACC is nilpotent.
- **Algebras over uncountable fields.** True, by an Amitsur-style counting argument.

The unconditional **Amitsur theorem** $J(R[x]) = N[x]$ for a nil ideal $N \trianglelefteq R$ is the workhorse linking formulations. On the delimiting side, Smoktunowicz (2000) showed the strengthening "$R$ nil $\Rightarrow R[x]$ nil" is *false*, and (2002) that simple nil rings exist — both consistent with Köthe's conjecture, but invalidating the most natural proof routes and the intuition that nil rings must be structurally small.

## 3. Principal approaches and barriers

**Matrix reformulation (Krempa, 1972).** Köthe's conjecture is equivalent to: $M_n(R)$ is nil for every nil ring $R$, and $n=2$ suffices. This converts a statement about one-sided ideals into a closure property of nil rings under a single explicit functor. *Barrier:* no technique controls the nilpotence index of products of matrices whose entries have unbounded nil exponent; matrix multiplication mixes nil indices in ways that defeat uniform bounds.

**Polynomial / Jacobson-radical reformulation.** Equivalently, $R[x]$ is Jacobson radical for every nil $R$ (Krempa, building on Amitsur). *Barrier:* Smoktunowicz's nil ring with $R[x]$ not nil shows the optimistic "nil $\Rightarrow$ nil polynomial ring" route is closed; the weaker Jacobson-radical target survives but with a very thin margin.

**Special-class arguments.** Each positive result (PI, chain conditions, uncountable fields, monomial/graded) works by bounding nil index or imposing a finiteness/dimension condition. The general conjecture is exactly about rings — Golod–Shafarevich algebras, Smoktunowicz's simple nil ring — where no such bound exists.

**Counterexample program.** Golod–Shafarevich (1964) supplied the first wild (infinite-dimensional, nil, non-nilpotent) algebras; Smoktunowicz engineered further pathologies. Yet none has produced a nil $R$ with $M_2(R)$ non-nil, and there is no known mechanism converting these constructions into a genuine counterexample.

**Radical-theoretic framing.** Kurosh–Amitsur radicals, special radical classes, and torsion theories reorganize the conjecture as a statement that $\mathrm{Nil}^*$ is a left-strong radical, but yield reformulations rather than leverage on the core obstruction.

## 4. Critical assessment

The dossier's central claim — that the conjecture is genuinely open and that all serious modern attacks route through the $M_2$ / Jacobson-radical gates — is well supported by the historical record and the cited survey literature. The web of equivalences is the conjecture's most striking feature and is reported accurately: a proof or counterexample in any one formulation settles all of them. The honest framing of Smoktunowicz's results as *near-misses in the negative direction* — disproving strengthenings while leaving Köthe's exact statement intact — is the correct and non-overstated reading.

Two cautions. First, the dossier's own papers list flags many later entries (rows 4, 6, 8, 10–12, 14, 18–25) as `needs-verification`, candidly noting that titles and years for parts of the Puczyłowski–Smoktunowicz corpus are approximate; the verifiable core is Köthe (1930), Amitsur's polynomial-radical work, Krempa (1972), Golod–Shafarevich (1964), and Smoktunowicz (2000–2002). Second, the modern narrative leans heavily on a single contemporary school (Warsaw/Edinburgh); while accurate, this concentration means independent corroboration of attribution detail is thinner than for more crowded fields.

## 5. What a resolution would require / open directions

A proof must show, for an arbitrary nil ring $R$ with no chain conditions and unbounded nil index, that $M_2(R)$ is nil — equivalently that $R[x]$ is Jacobson radical for every nil $R$. A disproof must engineer a nil ring violating the $M_2$-nilness criterion, presumably from Golod–Shafarevich- or Smoktunowicz-type material. The single obstruction in both directions is the absence of any technique that bounds or organizes nil index in the wild (non-Noetherian, non-PI) setting. Plausible routes flagged in the dossier: (i) force $N=R$ in Amitsur's $J(R[x])=N[x]$ via new growth/Hilbert-series constraints; (ii) adapt Smoktunowicz-type constructions directly against the $M_2$ criterion; (iii) develop quantitative nil-index control through combinatorial or Gröbner–Shirshov growth methods. The field's honest assessment is that no current program is close.

## 6. Selected references

1. Gottfried Köthe (1930), *Die Struktur der Ringe, deren Restklassenring nach dem Radikal vollständige Matrizenringe ist*, Math. Z. 32, 161–186. [high-confidence]
2. Jacob Levitzki (1945), *On the radical of a general ring*. [high-confidence]
3. A. S. Amitsur, J. Levitzki (1950), *A theorem on the structure of rings* (Amitsur–Levitzki identity). [high-confidence]
4. A. S. Amitsur (1956), *Radicals of polynomial rings*. [high-confidence]
5. E. S. Golod, I. R. Shafarevich (1964), *Infinite-dimensional nil non-nilpotent algebras (nil-algebra / Kurosh problem)*. [high-confidence]
6. Jan Krempa (1972), *Logical connections between some open problems concerning nil rings*. [high-confidence]
7. A. S. Amitsur (1951), *A generalization of Hilbert's Nullstellensatz*. [needs-verification]
8. A. S. Amitsur (1956), *Algebras over infinite fields*. [needs-verification]
9. V. A. Andrunakievich, Yu. M. Ryabukhin (1974), *The Theory of Radicals of Rings* (monograph). [needs-verification]
10. T. Y. Lam (1991), *A First Course in Noncommutative Rings* (textbook exposition of Köthe's conjecture). [high-confidence]
11. Agata Smoktunowicz (2000), *Polynomial rings over nil rings need not be nil*. [high-confidence]
12. Agata Smoktunowicz (2002), *A simple nil ring exists*. [high-confidence]
13. Agata Smoktunowicz (2002), *On some results related to Köthe's conjecture* (survey). [high-confidence]
14. E. R. Puczyłowski (1993), *Some questions about radicals of rings (Köthe's problem reformulations)*. [needs-verification]
15. E. R. Puczyłowski (2012), *On the Köthe problem and nil rings* (survey/update). [needs-verification]

## AI Review Panel

### Claude (Anthropic) — in-house review

This is a careful, technically literate survey. Its strengths are real: the statement and its several equivalent forms are reported with the right qualifications (associative, generally noncommutative, not necessarily unital); the Krempa reduction is correctly identified as the methodological pivot; and the treatment of Smoktunowicz's constructions is precise — it resists the common error of presenting "nil $R$ with $R[x]$ not nil" as a refutation of Köthe, correctly noting that the conjecture needs only the weaker Jacobson-radical property. The hierarchy $\mathrm{Nil}_* \subseteq \mathrm{Nil}^* \subseteq J(R)$ is handled accurately, and the obstruction (unbounded nil index outside chain-condition/PI settings) is stated honestly rather than hand-waved.

The principal weakness is citational, and the dossier is admirably candid about it: a substantial share of the references carry `needs-verification` flags, with titles and years for parts of the Puczyłowski–Smoktunowicz body of work declared approximate from memory. No persistent identifiers (DOI/arXiv) are supplied, which is defensible given the pre-1995 canonical literature, but it means a human must reconcile rows against MathSciNet/zbMATH before any of the flagged entries is cited downstream. I would also flag a mild single-source reliance: the modern narrative rests largely on one school's survey output, so attribution detail (exact years for Krempa's reductions, the precise statement Smoktunowicz proved in 2000 versus 2002) should be cross-checked against an independent secondary source such as Lam's textbook.

The single most important thing a human reviewer should verify: that the equivalence chain attributed to Krempa (1972) — Köthe $\iff$ $M_2(R)$ nil for nil $R$ $\iff$ $R[x]$ Jacobson radical for nil $R$ — is stated in exactly that form in a primary or authoritative secondary source, since the entire document's logical architecture rests on it. Everything else is supporting structure around that claim. I see no overstatement of the problem's status (it is correctly reported as open) and no claim of a new result.

**Verdict:** accept-with-revisions.

### GPT (OpenAI) — pending
_Not yet run. To complete the panel, run the prompt in docs/review/REVIEW-TEMPLATE.md through GPT and record the verdict here and in the front matter._

### Gemini (Google) — pending
_Not yet run. See docs/review/REVIEW-TEMPLATE.md._

### Grok (xAI) — pending
_Not yet run. See docs/review/REVIEW-TEMPLATE.md._

## Human verification

AI review is not human peer review. This meta-analysis is offered for academic verification per ../docs/review/ACADEMIC-REVIEW.md; the in-house Claude review above is a structured skeptical read, not an independent referee report, and the flagged citations in particular require primary-source confirmation. Status: human_review pending.

---
*Accredited to **Alexander Donahue** · The Unsolved Mathematics Atlas · CC BY 4.0. Cite per CITATION.cff.*

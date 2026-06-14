---
title: "Meta-Analysis: The Weinstein Conjecture"
slug: weinstein-conjecture
author: Alexander Donahue
type: ai-assisted-meta-analysis
peer_reviewed: false
problem_status: active-progress
ai_review:
  claude:
    verdict: accept-with-revisions
    date: "2026-06-14"
    version: "claude-opus-4-8"
    summary: "An accurate survey of a problem solved in dimension three (Taubes 2007) and open in dimensions five and above, whose citation identifiers require primary-source verification."
  gpt:
    verdict: pending
  gemini:
    verdict: pending
  grok:
    verdict: pending
human_review: pending
---

# Meta-Analysis: The Weinstein Conjecture

> **AI-generated meta-analysis — not peer-reviewed.** Curated and accredited by **Alexander Donahue** (human-in-the-loop). A survey/assessment of an open problem; it makes no claim of a new result. Citations carry verification flags and require human source-checking.

## Abstract

The Weinstein conjecture asserts that every Reeb vector field on a closed contact manifold possesses at least one periodic orbit. Posed by Alan Weinstein in 1979, it isolated the contact-type condition as the operative hypothesis behind earlier periodic-orbit theorems of Rabinowitz and Weinstein for star-shaped and convex energy hypersurfaces in Euclidean space. The conjecture has organized four decades of symplectic topology and is the proving ground for its principal technologies: variational methods, pseudoholomorphic curves, symplectic field theory, and gauge theory. In dimension three the conjecture is a theorem of Clifford Taubes (2007), obtained through Seiberg–Witten Floer theory; this is the only complete proof of a general case and is universally accepted. In dimensions five and above the statement remains open, established only under auxiliary hypotheses such as symplectic fillability, overtwistedness, or special topology. This meta-analysis surveys the statement, the state of the art, the methods and their structural barriers, and what an unconditional higher-dimensional resolution would require. It assesses the dossier's claims and flags points needing human verification. The metadata status is active-progress.

## 1. Statement and significance

A contact form $\alpha$ on a $(2n-1)$-manifold $M$ satisfies $\alpha \wedge (d\alpha)^{n-1} \neq 0$; its Reeb field $R$ is defined by $\alpha(R)=1$ and $d\alpha(R,\cdot)=0$. The conjecture asserts that $R$ always carries a periodic orbit. Equivalently, a hypersurface of contact type in a symplectic manifold carries a closed characteristic. The Reeb dynamics depend on the choice of form $\alpha$, not merely on the contact structure $\xi = \ker\alpha$, but the conjecture asserts existence for every $\alpha$.

The significance is twofold. Dynamically, it answers when energy hypersurfaces of mechanical systems must support periodic motion — the thread running back through Weinstein (1978), Rabinowitz (1978), and Seifert (1948). Structurally, Weinstein's reformulation made contact geometry the natural home for the periodic-orbit problem and forced the development of the symplectic-topological machinery of the 1980s onward. It is a focal existence problem whose pursuit has been disproportionately generative for its field.

## 2. State of the art

The frontier is sharply stratified by dimension.

- **Dimension three — solved.** Every Reeb vector field on a closed contact 3-manifold has a closed orbit (Taubes, 2007), via Seiberg–Witten Floer theory and the nontriviality of the monopole invariant. This is settled and accepted.
- **Euclidean case, all dimensions.** Every hypersurface of contact type in $\mathbb{R}^{2n}$ carries a closed characteristic (Viterbo, 1987).
- **Overtwisted structures, all dimensions where defined** — closed Reeb orbits exist (Hofer in dimension three; higher dimensions after Borman–Eliashberg–Murphy made the notion available).
- **Multiplicity in dimension three.** Every contact form on a closed 3-manifold has at least two embedded Reeb orbits (Cristofaro-Gardiner–Hutchings, 2016), and infinitely many in many/generic cases.
- **Dimensions $\geq 5$, conditional.** Existence holds for symplectically fillable manifolds (via symplectic / Rabinowitz–Floer homology), Boothby–Wang prequantization bundles, subcritically Stein-fillable manifolds, and cases where contact homology is well-defined and nonvanishing.

The unconditional statement in dimensions $\geq 5$ is the central open problem. No counterexample is known or expected.

## 3. Principal approaches and barriers

**Variational/convexity methods** produced the founding theorems and Viterbo's 1987 result, minimizing or applying minimax to the symplectic action functional. The barrier is structural: these arguments require an ambient $\mathbb{R}^{2n}$ or an exact filling where a global primitive and action functional exist. A general closed contact manifold may admit no such filling.

**Pseudoholomorphic curves** (Hofer, 1993) detect a Reeb orbit as the asymptotic limit of a finite-energy holomorphic curve in the symplectization, degenerating a Bishop family of disks onto an orbit. This settled $S^3$, overtwisted structures, and the $\pi_2(M)\neq 0$ case, but the degeneration need not occur for tight structures, and transversality/compactness for the moduli spaces is delicate.

**Contact homology and symplectic field theory** (Eliashberg–Givental–Hofer, 2000) build an invariant generated by Reeb orbits whose nonvanishing forces existence. Foundational transversality failures for multiply covered curves obstructed rigorous definition for years; polyfold (Hofer–Wysocki–Zehnder) and virtual (Pardon) techniques repair this. The machinery typically still requires a filling.

**Gauge theory — the dimension-three solution.** Taubes reduced the three-dimensional conjecture to Seiberg–Witten Floer theory; embedded contact homology (Hutchings) reinterprets the counts geometrically, and the ECH $\cong \widehat{HM}$ isomorphism makes the picture canonical. The decisive barrier to generalization: Seiberg–Witten theory and ECH are intrinsically three/four-dimensional, with no known higher-dimensional analogue of comparable force.

## 4. Critical assessment

The dossier's central factual claims are sound and align with the established literature: dimension three is closed by Taubes (2007); higher dimensions are open; the conditional higher-dimensional results carry hypotheses the conjecture does not. The framing of the obstruction as "method, not truth" is the consensus view and is stated with appropriate care.

Two emphases deserve scrutiny. First, the dossier rightly distinguishes the foundational disputes over contact homology / SFT transversality (now addressed by polyfolds and virtual techniques) from the main existence theorems; this distinction is important and correctly drawn — Taubes's proof is independent of contact-homology transversality. Second, the multiplicity results (two-or-infinitely-many) are near-frontier refinements in dimension three, not progress on the open higher-dimensional case, and the dossier does not conflate them.

The principal weakness is bibliographic, not mathematical: a majority of the paper-table identifiers are flagged needs-verification, and several entries bundle multi-part series without a stable identifier. The mathematical narrative does not depend on those identifiers, but any citation of record built from this dossier must resolve them against primary sources.

## 5. What a resolution would require / open directions

An unconditional proof in dimensions $\geq 5$ would need a closed Reeb orbit for every contact form on every closed contact manifold, with no fillability or topological hypothesis. Plausible routes:

1. **Higher-dimensional Floer or gauge invariants** playing the role ECH plays in dimension three, detecting orbits without a filling.
2. **Foundationally complete SFT/contact homology** (post-polyfold) proving nonvanishing in full generality, removing the fillability hypothesis.
3. **Holomorphic-curve compactness arguments** generalizing Hofer's degeneration beyond the overtwisted and fillable regimes.
4. **Quantitative/dynamical inputs** — symplectic capacities or $C^0$-dynamics — forcing orbits abstractly.

The honest assessment is that no current program has a clear path to the unconditional higher-dimensional statement, and the decisive low-dimensional tool does not transfer.

## 6. Selected references

1. Paul H. Rabinowitz, *Periodic solutions of Hamiltonian systems* (1978). [high-confidence]
2. Alan Weinstein, *Periodic orbits for convex Hamiltonian systems* (1978). [high-confidence]
3. Alan Weinstein, *On the hypotheses of Rabinowitz's periodic orbit theorems* (1979). [high-confidence]
4. Mikhail Gromov, *Pseudoholomorphic curves in symplectic manifolds* (1985). [high-confidence]
5. Claude Viterbo, *A proof of Weinstein's conjecture in $\mathbb{R}^{2n}$* (1987). [high-confidence]
6. Helmut Hofer, Eduard Zehnder, *Symplectic Invariants and Hamiltonian Dynamics* (1990). [high-confidence]
7. Helmut Hofer, *Pseudoholomorphic curves in symplectizations with applications to the Weinstein conjecture in dimension three* (1993). [high-confidence]
8. Y. Eliashberg, A. Givental, H. Hofer, *Introduction to Symplectic Field Theory* (2000), arXiv:math/0010059. [high-confidence]
9. Michael Hutchings, *An index inequality for embedded pseudoholomorphic curves in symplectizations* (2004), arXiv:math/0112165. [needs-verification]
10. Clifford H. Taubes, *The Seiberg–Witten equations and the Weinstein conjecture*, Geom. Topol. 11 (2007), arXiv:math/0611007. [high-confidence]
11. K. Cieliebak, U. Frauenfelder, A. Oancea, *Rabinowitz Floer homology and symplectic homology* (2009), arXiv:0903.0768. [needs-verification]
12. C. H. Taubes, *Embedded contact homology and Seiberg–Witten Floer cohomology I–V* (2010). [needs-verification]
13. Michael Hutchings, *Taubes's proof of the Weinstein conjecture in dimension three* (survey, 2010), arXiv:0906.2444. [needs-verification]
14. Daniel Cristofaro-Gardiner, Michael Hutchings, *From one Reeb orbit to two* (2016), arXiv:1202.4839. [high-confidence]
15. D. Cristofaro-Gardiner, M. Hutchings, D. Pomerleano, *Two or infinitely many Reeb orbits* (2019), arXiv:1702.02493. [needs-verification]

## AI Review Panel

### Claude (Anthropic) — in-house review

The survey is accurate and well-proportioned. Its chief strength is the clean separation of what is settled from what is open: dimension three is closed unconditionally by Taubes (2007), and the higher-dimensional results are correctly presented as conditional on fillability, overtwistedness, or special topology — never as partial progress on the unconditional statement. The treatment of the contact-homology foundational disputes is fair: it credits the transversality problem, notes the polyfold/virtual repair, and correctly observes that Taubes's gauge-theoretic proof is independent of those issues and therefore unaffected. The diagnosis that the obstruction is "method, not truth" reflects genuine community consensus rather than wishful framing.

I want to flag three things for a human reviewer. (i) The cited references carry verification flags; the majority of identifiers in the source dossier are marked needs-verification, and several bundle multi-part series (Taubes's ECH $\cong \widehat{HM}$ papers, the HWZ properties series) without a stable identifier. These are real, canonical works, but every arXiv id and venue here must be checked against the primary abstract page before this is used as a citation of record. (ii) There is mild single-source reliance: the narrative draws heavily on a few survey-level framings (notably Hutchings's expository account of Taubes's proof), and the higher-dimensional conditional results are attributed in aggregate rather than to specific theorems — a reader should not infer that any single cited paper establishes the full conditional landscape. (iii) The single most important thing to verify is the precise scope of the Taubes (2007) theorem and its venue (Geom. Topol. 11) — it is the load-bearing claim of the entire document, and while I am confident in it, the document's authority rests on it being exactly stated.

No claim of a new result is made, and none should be inferred; this is a survey of an open problem. Subject to primary-source checking of the flagged citations, the document is sound.

**Verdict:** accept-with-revisions.

### GPT (OpenAI) — pending

_Not yet run. To complete the panel, run the prompt in docs/review/REVIEW-TEMPLATE.md through GPT and record the verdict here and in the front matter._

### Gemini (Google) — pending

_Not yet run. See docs/review/REVIEW-TEMPLATE.md._

### Grok (xAI) — pending

_Not yet run. See docs/review/REVIEW-TEMPLATE.md._

## Human verification

AI review is not human peer review. This assessment is offered for academic verification per ../docs/review/ACADEMIC-REVIEW.md, and its citations — several of which carry needs-verification flags — require checking against primary sources before any scholarly reliance. Status: human_review pending.

---
*Accredited to **Alexander Donahue** · The Unsolved Mathematics Atlas · CC BY 4.0. Cite per CITATION.cff.*

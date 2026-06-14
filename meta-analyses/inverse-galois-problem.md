---
title: "Meta-Analysis: The Inverse Galois Problem"
slug: inverse-galois-problem
author: Alexander Donahue
type: ai-assisted-meta-analysis
peer_reviewed: false
problem_status: active-progress
ai_review:
  claude:
    verdict: accept-with-revisions
    date: "2026-06-14"
    version: "claude-opus-4-8"
    summary: "A faithful, well-calibrated survey of an open problem whose dossier claims are sound in outline but rest on several memory-reconstructed citations that require primary-source verification."
  gpt:
    verdict: pending
  gemini:
    verdict: pending
  grok:
    verdict: pending
human_review: pending
---

# Meta-Analysis: The Inverse Galois Problem

> **AI-generated meta-analysis — not peer-reviewed.** Curated and accredited by **Alexander Donahue** (human-in-the-loop). A survey/assessment of an open problem; it makes no claim of a new result. Citations carry verification flags and require human source-checking.

## Abstract

The Inverse Galois Problem (IGP) asks whether every finite group $G$ occurs as the Galois group $\mathrm{Gal}(L/\mathbb{Q})$ of some finite Galois extension of the rational numbers. Posed implicitly in David Hilbert's 1892 work on irreducibility and sharpened by Emmy Noether's 1918 rationality formulation, it remains open with active progress. The arithmetic IGP reduces, via the Hilbert Irreducibility Theorem, to the regular IGP over $\mathbb{Q}(t)$, recasting an existence question as the construction of branched covers of $\mathbb{P}^1$ with prescribed monodromy and a $\mathbb{Q}$-rational structure. Large families are settled: all abelian groups (Kronecker–Weber), all finite solvable groups (Shafarevich, 1954), the symmetric and alternating groups (Hilbert), and most finite simple groups including the Monster (Thompson, 1984) via the rigidity method. The standard concrete holdout is the Mathieu group $M_{23}$. Over ample (large) fields every finite group is regularly realizable by patching, but $\mathbb{Q}$ is not ample. This meta-analysis surveys the state of the art, the principal methods and their structural barriers, and assesses what a complete resolution would require, flagging citation-verification needs throughout.

## 1. Statement and significance

The problem is elementary to state: is every finite group $G$ isomorphic to $\mathrm{Gal}(L/\mathbb{Q})$ for some Galois extension $L/\mathbb{Q}$? Its significance lies in what an affirmative answer would mean for the structure of the absolute Galois group $G_{\mathbb{Q}} = \mathrm{Gal}(\bar{\mathbb{Q}}/\mathbb{Q})$: every finite group would be a continuous quotient of $G_{\mathbb{Q}}$, a strong structural constraint on the most important object in algebraic number theory. The problem sits at the intersection of Galois theory, arithmetic geometry (covers and moduli of curves), and finite group theory, and its standard reductions tie it to Hilbert irreducibility, Hurwitz spaces, and embedding-problem cohomology. Two formulations are standard: the **arithmetic IGP** over $\mathbb{Q}$, and the stronger **regular IGP (RIGP)** over $\mathbb{Q}(t)$, which implies the arithmetic version. The dossier's framing of both, and of Noether's invariant-field reformulation, is accurate and standard.

## 2. State of the art

The unconditional positive results are well-established and not in dispute:

- **Abelian groups** are realized classically via cyclotomic fields and the Kronecker–Weber theorem.
- **Finite solvable groups** are all realizable over $\mathbb{Q}$ — Shafarevich (1954), with the original argument's gap at the prime $2$ now repaired in the literature (Neukirch–Schmidt–Wingberg).
- **Symmetric and alternating groups** $S_n, A_n$ for all $n$ — Hilbert (1892).
- **Most finite simple groups**, including many groups of Lie type and 25 of the 26 sporadic groups, are realized by the rigidity method; Thompson's 1984 realization of the Monster is the emblem.
- The **salient gap** is the Mathieu group $M_{23}$, conventionally cited as the simplest sporadic group not yet known to be Galois over $\mathbb{Q}$, alongside many other non-solvable groups.

Over **ample (large) fields** — $\mathbb{Q}_p$, $\mathbb{C}((t))$, PAC fields — and function fields $k(t)$, every finite group is regularly realizable by the patching methods of Harbater, Pop, and Haran–Völklein. The barrier to importing this to $\mathbb{Q}$ is precisely that $\mathbb{Q}$ is not ample. The **Malle conjecture** on counting $G$-extensions by discriminant is a conditional sharpening that would entail realizability for the groups it covers.

## 3. Principal approaches and barriers

**Hilbert irreducibility and the reduction to $\mathbb{Q}(t)$.** The organizing reduction: realizing $G$ regularly over $\mathbb{Q}(t)$ yields, by specialization, infinitely many realizations over $\mathbb{Q}$. *Barrier:* RIGP is itself open in general, and descending a cover's field of moduli to $\mathbb{Q}$ can be obstructed.

**The rigidity method.** One seeks a rigid, rational tuple of conjugacy classes $(C_1,\dots,C_r)$ generating $G$ with trivial product; rigidity collapses the Hurwitz space to a point and rationality descends the cover to $\mathbb{Q}$. This is the most successful tool for simple and almost-simple groups. *Barrier:* rigid rational tuples are rare, most groups lack them, and there is no method to manufacture them — $M_{23}$ is the canonical victim.

**Hurwitz spaces and the braid-group action.** A geometric generalization: covers with fixed branch data are parametrized by Hurwitz spaces whose components correspond to braid-orbit Nielsen classes; a $\mathbb{Q}$-rational point on a component with $\mathbb{Q}$-structure realizes $G$. *Barrier:* higher-genus components need not have rational points, and the $G_{\mathbb{Q}}$-action on braid orbits is generally intractable.

**Embedding problems / the solvable strategy.** Lifting realizations along $G \twoheadrightarrow G/N$ via $H^2$-obstructions is the engine behind Shafarevich's solvable theorem. *Barrier:* non-abelian embedding problems for non-solvable kernels lack a general solvability criterion.

**Rationality / Noether problem.** Rationality of the invariant field yields a generic polynomial. *Barrier:* the Noether problem fails — Swan (1969) for $C_{47}$; Saltman (1984) and Bogomolov (1987) via nonzero unramified Brauer groups — though failure of rationality does not imply non-realizability ($C_{47}$ is abelian, hence realizable).

**Patching over large fields.** Settles the RIGP over ample fields completely. *Barrier:* $\mathbb{Q}$ is not ample; no arithmetic substitute for ampleness is known.

## 4. Critical assessment

The dossier is, on the mathematics, a careful and honest account. It correctly distinguishes arithmetic from regular IGP, correctly identifies the four-or-five genuinely distinct method families, and is appropriately precise about the boundary between what is proven and what is conjectural. It avoids the common popularization error of conflating "solvable groups are done" with "the problem is nearly solved" — the non-solvable simple groups are exactly where the difficulty concentrates, and the dossier says so.

Two calibration points deserve emphasis. First, the claim that "25 of 26 sporadic groups are realized" with $M_{23}$ as the sole sporadic holdout is the standard textbook statement (Malle–Matzat, Serre) and is plausible, but the precise count and the current status of $M_{23}$ should be checked against a recent source, since incremental results do appear. Second, the dossier is commendably explicit that the IGP has **no** seriously-considered claimed proof of the full statement — the field advances by realizing families, not by adjudicating a putative resolution. This is an honest and, I believe, accurate characterization that distinguishes this problem from others in the Atlas.

The principal weakness is bibliographic rather than mathematical: the papers list openly flags that many entries (rows 3–4, 7–9, 11–16, 18–19, 21, 23) have titles/years reconstructed from memory, and row 15 is an unverified "ai-suggested" lead. The mathematical narrative does not depend on those specific citations being bibliographically exact, but a reader should not cite them downstream without checking.

## 5. What a resolution would require / open directions

By the classification of finite simple groups and standard extension arguments, a full resolution would essentially reduce to (i) realizing every finite simple group over $\mathbb{Q}$ and (ii) solving the resulting non-abelian embedding problems to assemble general $G$ from its composition factors. Step (ii) is mature in the solvable case; step (i) is where rigidity runs out. The consensus the dossier reports — that a genuinely new mechanism beyond rigidity, Hurwitz-space rational points, and patching is needed for the remaining simple groups uniformly — is sound. The three plausible routes are: beyond-rigidity Hurwitz-space arithmetic (rational points on positive-genus components, with control of the $G_{\mathbb{Q}}$-action on braid orbits); an arithmetic substitute for ampleness that descends patching to $\mathbb{Q}$; and general solvability criteria for non-solvable embedding problems. A concrete near-term test of any new method is whether it realizes $M_{23}$.

## 6. Selected references

1. David Hilbert (1892), *Über die Irreducibilität ganzer rationaler Funktionen mit ganzzahligen Koeffizienten*. [high-confidence]
2. Emmy Noether (1918), *Gleichungen mit vorgeschriebener Gruppe*. [high-confidence]
3. Igor R. Shafarevich (1954), *Construction of fields of algebraic numbers with given solvable Galois group*. [high-confidence]
4. Richard G. Swan (1969), *Invariant rational functions and a problem of Steenrod*. [high-confidence]
5. John G. Thompson (1984), *Some finite groups which appear as $\mathrm{Gal}\,L/K$, where $K \subseteq \mathbb{Q}(\mu_n)$*. [high-confidence]
6. David J. Saltman (1984), *Noether's problem over an algebraically closed field*. [needs-verification]
7. Fedor A. Bogomolov (1987), *The Brauer group of quotient spaces by linear group actions*. [needs-verification]
8. Michael D. Fried, Helmut Völklein (1990), *The inverse Galois problem and rational points on moduli spaces*. [needs-verification]
9. Jean-Pierre Serre (1992), *Topics in Galois Theory*. [high-confidence]
10. David Harbater (1994), *Abhyankar's conjecture on Galois groups over curves*. [needs-verification]
11. Michel Raynaud (1995), *Étale covers of affine curves in positive characteristic (Abhyankar's conjecture)*. [needs-verification]
12. Helmut Völklein (1996), *Groups as Galois Groups: An Introduction*. [high-confidence]
13. Florian Pop (1996), *Embedding problems over large fields*. [needs-verification]
14. Gunter Malle, B. Heinrich Matzat (1999), *Inverse Galois Theory*. [high-confidence]
15. C. U. Jensen, A. Ledet, N. Yui (2002), *Generic Polynomials: Constructive Aspects of the Inverse Galois Problem*. [high-confidence]
16. J. Neukirch, A. Schmidt, K. Wingberg (2008), *Cohomology of Number Fields* (2nd ed.; embedding problems / Shafarevich). [high-confidence]

## AI Review Panel

### Claude (Anthropic) — in-house review

The strengths of this dossier are real. The mathematical scaffolding is correct and standard: the Hilbert-irreducibility reduction, the arithmetic-versus-regular dichotomy, the rigidity/Hurwitz/embedding/Noether/patching taxonomy of methods, and the identification of $M_{23}$ and the non-solvable simple groups as the live frontier all match the consensus literature (Serre, Malle–Matzat, Völklein). The document is honest in a way that matters: it does not oversell the solvable-group success, and it explicitly states that no seriously-considered proof of the full statement exists — which is the correct and responsible framing.

My skeptical flags. (i) **Citations carry verification flags and need primary-source checking.** The dossier itself concedes that a large fraction of its papers list has titles, years, or journal details reconstructed from memory (rows 3–4, 7–9, 11–16, 18–19, 21, 23), with one entry (row 15) merely "ai-suggested." I have preserved these flags in the references above; none should be cited downstream without confirmation against the actual publications. (ii) **Single-source reliance.** The status claims — particularly "25 of 26 sporadic groups realized, $M_{23}$ the sole sporadic exception" — appear to rest on the standard monographs without an independent recent cross-check; given that incremental realizations do occur, a human should confirm the current count rather than treat the dossier's figure as fixed. There is no overstatement of the problem's status that I can identify; if anything the framing is conservative.

The single most important thing a human reviewer should verify: the **current status of $M_{23}$ and the precise sporadic-group count**, against a recent authoritative survey, since this is the dossier's most load-bearing concrete claim and the one most exposed to drift. Secondarily, confirm that Shafarevich's $2$-adic correction is attributed and sourced as stated.

**Verdict:** accept-with-revisions.

### GPT (OpenAI) — pending

_Not yet run. To complete the panel, run the prompt in docs/review/REVIEW-TEMPLATE.md through GPT and record the verdict here and in the front matter._

### Gemini (Google) — pending

_Not yet run. See docs/review/REVIEW-TEMPLATE.md._

### Grok (xAI) — pending

_Not yet run. See docs/review/REVIEW-TEMPLATE.md._

## Human verification

AI review is not human peer review. This assessment is offered for academic verification per ../docs/review/ACADEMIC-REVIEW.md, and its citation flags in particular require checking against primary sources before any downstream use. Status: human_review pending.

---
*Accredited to **Alexander Donahue** · The Unsolved Mathematics Atlas · CC BY 4.0. Cite per CITATION.cff.*

---
title: "Meta-Analysis: The Inscribed Square Problem (Toeplitz)"
slug: inscribed-square-problem
author: Alexander Donahue
type: ai-assisted-meta-analysis
peer_reviewed: false
problem_status: active-progress
ai_review:
  claude:
    verdict: accept-with-revisions
    date: "2026-06-14"
    version: "claude-opus-4-8"
    summary: "A faithful and well-calibrated survey of an open problem whose smooth case is settled and whose continuous case turns entirely on a single degeneration obstruction; references require primary-source verification."
  gpt:
    verdict: pending
  gemini:
    verdict: pending
  grok:
    verdict: pending
human_review: pending
---

# Meta-Analysis: The Inscribed Square Problem (Toeplitz)

> **AI-generated meta-analysis — not peer-reviewed.** Curated and accredited by **Alexander Donahue** (human-in-the-loop). A survey/assessment of an open problem; it makes no claim of a new result. Citations carry verification flags and require human source-checking.

## Abstract

The inscribed square problem, posed by Otto Toeplitz in 1911 and also called the square peg problem, asks whether every simple closed (Jordan) curve in the Euclidean plane contains four points that are the vertices of a square. The conjecture is widely believed true and is proved on every well-behaved subclass of curves — convex (Emch, 1913), smooth or analytic (Schnirelmann, 1929; Jerrard, 1961), and locally monotone (Stromquist, 1989), the last covering all piecewise-$C^1$ curves and polygons. The most striking modern advance is the symplectic resolution of the smooth rectangular peg problem by Greene and Lobb (2020), which inscribes rectangles of every aspect ratio — hence squares — in every smooth Jordan curve. Yet the original question, for arbitrary continuous curves with no smoothness, remains open. This meta-analysis assembles the dossier's account of the history, the principal proof strategies, and the single recurring obstruction — the possible degeneration of inscribed squares to a point under smooth approximation — and assesses what a full resolution would require. It is a survey and critical assessment, not a new result; all cited references retain verification flags pending human source-checking.

## 1. Statement and significance

The problem asks: for every injective continuous map $\gamma : S^1 \to \mathbb{R}^2$, does the image $\gamma(S^1)$ contain four points forming a non-degenerate square? Toeplitz announced the conjecture in 1911 at the Deutsche Mathematiker-Vereinigung, together with a proof for convex curves. Its significance is twofold. First, it is a canonical example of an elementary-to-state problem — comprehensible to a schoolchild — that has resisted a century of effort, making it a touchstone for the gap between intuition and proof in plane topology. Second, its difficulty is diagnostic: the class of Jordan curves includes nowhere-differentiable, fractal-like, and Osgood curves, and every known method founders precisely on this generality. The problem sits at the intersection of geometric topology and differential geometry and has seeded an entire family of inscribed-figure questions (rectangles, cyclic quadrilaterals, similar quadrilaterals).

## 2. State of the art

Per the dossier, the conjecture is **proved unconditionally** for: convex curves (Emch, 1913); smooth and analytic curves via parity counts (Schnirelmann, 1929; Jerrard, 1961); locally monotone curves (Stromquist, 1989), the strongest broad result, covering all piecewise-$C^1$ curves and polygons; and unions of two Lipschitz graphs with small constant (Tao, 2017). The headline recent advance is Greene and Lobb (2020): every **smooth** Jordan curve inscribes a rectangle of every aspect ratio, and hence a square, via symplectic geometry of Lagrangian tori in $\mathbb{R}^4 \cong \mathbb{C}^2$. Separately, Vaughan's Möbius-band argument shows every Jordan curve — smooth or not — inscribes some rectangle. The general continuous square case remains open; the frontier is bridging from smooth and locally monotone curves to arbitrary Jordan curves. The active community is small but vibrant, currently centered on the symplectic and knot-theoretic frontier (Greene, Lobb, Hugelmeyer, Schwartz), with Matschke and Tao as reference points for the configuration-space and analytic routes.

## 3. Principal approaches and barriers

The dossier organizes the proof strategies into five families, each with a clearly stated barrier.

**Smoothing and limiting.** Prove inscribed squares for smooth $\gamma_n \to \gamma$, extract squares $S_n \subset \gamma_n$, and pass to the limit. *Barrier:* the limit square may **degenerate to a point**. No uniform lower bound on the size of an inscribed square is known for arbitrary continuous curves, and this collapse is the central obstruction — roughness, not non-convexity, is the enemy.

**Parity / degree counting** (Emch, Schnirelmann, Jerrard). For smooth or analytic curves, the number of inscribed squares is shown to be odd, hence nonzero. *Barrier:* transversality of the auxiliary map requires smoothness; the odd count can collapse under degeneration.

**Locally monotone / bounded variation** (Stromquist). Tracks square configurations through a continuous family with a connectedness/winding argument. *Barrier:* local monotonicity is exactly what genuinely wild curves lack.

**Topology in $\mathbb{R}^4$** (Vaughan, Hugelmeyer). Encode unordered point pairs as a Möbius band with boundary $\gamma$; the relevant map cannot embed it in the plane without a coincidence, forcing a rectangle. *Barrier:* a square is a rectangle plus the extra constraint of equal diagonals at $90°$, which the pure topology does not force; the strongest square versions still require smoothness.

**Symplectic geometry** (Greene–Lobb). Reformulate inscribed rectangles as a non-displaceability/intersection problem for monotone Lagrangian tori. *Barrier:* the Lagrangian machinery needs the curve to be smooth or sufficiently rectifiable; the symplectic objects are not defined for wild curves.

## 4. Critical assessment

The dossier's framing is, in my assessment, well-calibrated and consistent across files. Its central claim — that the obstruction is a single, sharply identified phenomenon (degeneration of inscribed squares under approximation) rather than a deep structural impossibility — is the standard expert reading and is stated without overreach. The history correctly distinguishes the *solved smooth case* from the *open continuous case*, and the attempts file is exemplary in flagging both the recurring methodological pitfall (unjustified limiting arguments in amateur "elementary proofs") and the recurring reporting pitfall (popular coverage conflating "smooth Jordan curve" with "every Jordan curve" after Greene–Lobb).

Two points of nuance deserve sharpening. First, the dossier occasionally telescopes "Greene–Lobb proved the smooth rectangular peg problem" into language adjacent to "hence the smooth square problem" — which is correct (a square is the aspect-ratio-1 rectangle) but worth stating explicitly each time to avoid drift. Second, no impossibility/barrier result is known, so the consensus that the conjecture is *true* is an expectation, not a theorem; the document is appropriately careful to label it as such. The five-family taxonomy of approaches is accurate and matches the literature; the barriers are stated honestly and are not strawmen.

## 5. What a resolution would require / open directions

A full proof must handle arbitrary continuous curves with no smoothness. The missing step is uniform: show that inscribed squares (or the relevant configuration-space intersections) **do not degenerate to a point** in the limit of a smooth approximation. The dossier lists three plausible routes. (1) **Extend the symplectic method off the smooth class** — define the Lagrangian objects or a Floer-theoretic count for rectifiable or merely continuous curves and recover the square as the aspect-ratio-1 rectangle; the most promising direction, but the symplectic data is not yet available for wild curves. (2) **A uniform non-degeneracy bound** — a quantitative lower bound on the size of an inscribed square in terms of the geometry of $\gamma$, validating the limiting argument for all continuous curves. (3) **Equivariant topology with weaker hypotheses** — push Matschke-style $\mathbb{Z}/4$ configuration-space arguments into the continuous category. All three converge on the same target: converting the abundant smooth-case successes into a statement about the full, untamed class of Jordan curves.

## 6. Selected references

Drawn from the dossier's papers list; each retains its original verification flag. Identifiers reported from memory require confirmation against a bibliographic source before citation.

1. Otto Toeplitz (1911), *Announcement of the inscribed square conjecture* (Jahresbericht DMV / conference report). [high-confidence]
2. Arnold Emch (1913), *Some properties of closed convex curves in a plane*. [high-confidence]
3. Lev Schnirelmann (1929), *Über eine neue Methode in der kombinatorischen Topologie* (inscribed square via parity). [high-confidence]
4. R. P. Jerrard (1961), *Inscribed squares in plane curves*. [high-confidence]
5. H. E. Vaughan (1977), *Survey of the inscribed square problem / rectangle peg observations*. [needs-verification]
6. Walter Stromquist (1989), *Inscribed squares and square-like quadrilaterals in closed curves*. [high-confidence]
7. Mark J. Nielsen (2008), *Figures inscribed in curves: a short tour of an old problem* (survey). [needs-verification]
8. Benjamin Matschke (2014), *A survey on the square peg problem*. [high-confidence]
9. Benjamin Matschke (2014), *Equivariant topology of configuration spaces and the square peg problem*. [needs-verification]
10. Terence Tao (2017), *An integration approach to the Toeplitz square peg problem*, arXiv:1611.07441. [high-confidence]
11. Cole Hugelmeyer (2018), *Inscribed rectangles in a smooth Jordan curve attain at least one third of all aspect ratios*, arXiv:1803.07417. [needs-verification]
12. Joshua Evan Greene, Andrew Lobb (2020), *The rectangular peg problem*, arXiv:2005.09193. [high-confidence]
13. Joshua Evan Greene, Andrew Lobb (2021), *Cyclic quadrilaterals and smooth Jordan curves*, arXiv:2011.07546. [needs-verification]
14. Richard Evan Schwartz (2021), *A trichotomy for rectangles inscribed in Jordan loops*, arXiv:2009.11539. [needs-verification]

## AI Review Panel

### Claude (Anthropic) — in-house review

The survey's principal strength is calibration. It does not blur the central distinction on which everything hinges — that the smooth case (including the smooth square via Greene–Lobb's aspect-ratio-1 rectangle) is settled while the continuous case is open — and it isolates the single operative obstruction (degeneration of inscribed squares to a point under approximation) without inflating it into a mystique. The five-family taxonomy of approaches is faithful to the literature, and each barrier is stated as a genuine technical limitation rather than a strawman. The history and attempts material is honest about both the amateur pitfall (unjustified limits) and the journalistic one (conflating "smooth" with "every").

That said, a referee should be skeptical on three fronts. First, the references carry explicit verification flags for good reason: of the entries cited here, several (Vaughan 1977, the 2014 equivariant-topology paper, Hugelmeyer, the two 2021 entries) are flagged needs-verification, and the arXiv identifiers — including 2005.09193 for Greene–Lobb and 1611.07441 for Tao — are reported from memory and must be checked against arXiv and the published record before any citation is trusted. Second, the document leans on a small number of load-bearing canonical sources (Schnirelmann, Stromquist, Matschke, Greene–Lobb); the framing of "consensus that the conjecture is true" is an expert expectation, not a proven fact, and a single-source reliance on survey-level summaries means the precise smoothness hypotheses (e.g., exactly what regularity Schnirelmann's argument requires, the precise statement of Stromquist's "locally monotone" class) should not be quoted as definitive without consulting the primary papers.

The single most important thing a human reviewer should verify is the **exact scope and identifier of Greene–Lobb (2020)** — that arXiv:2005.09193 is correct, that the theorem is stated for smooth (not merely rectifiable) Jordan curves, and that "rectangle of every aspect ratio, hence a square" is reproduced accurately — since this is the load-bearing modern result and the most likely point at which a popular-source overstatement could have crept into the dossier. Secondarily, confirm that no announced extension to the full continuous case has appeared since the dossier was compiled.

**Verdict:** accept-with-revisions.

### GPT (OpenAI) — pending

_Not yet run. To complete the panel, run the prompt in docs/review/REVIEW-TEMPLATE.md through GPT and record the verdict here and in the front matter._

### Gemini (Google) — pending

_Not yet run. See docs/review/REVIEW-TEMPLATE.md._

### Grok (xAI) — pending

_Not yet run. See docs/review/REVIEW-TEMPLATE.md._

## Human verification

AI review is not human peer review. This assessment is offered for academic verification per ../docs/review/ACADEMIC-REVIEW.md; the AI panel's findings are advisory and the reference flags signal claims that a human must source-check against primary literature. Status: human_review pending.

---
*Accredited to **Alexander Donahue** · The Unsolved Mathematics Atlas · CC BY 4.0. Cite per CITATION.cff.*

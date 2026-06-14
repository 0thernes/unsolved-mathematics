---
title: "Meta-Analysis: The Moving Sofa Problem"
slug: moving-sofa-problem
author: Alexander Donahue
type: ai-assisted-meta-analysis
peer_reviewed: false
problem_status: active-progress
ai_review:
  claude:
    verdict: accept-with-revisions
    date: "2026-06-14"
    version: "claude-opus-4-8"
    summary: "A faithful, well-calibrated survey of a famous plane-geometry extremal problem that correctly frames Baek's 2024 optimality claim as unverified rather than settled, but leans on uncertain bibliographic identifiers that need primary-source checking."
  gpt:
    verdict: pending
  gemini:
    verdict: pending
  grok:
    verdict: pending
human_review: pending
---

# Meta-Analysis: The Moving Sofa Problem

> **AI-generated meta-analysis — not peer-reviewed.** Curated and accredited by **Alexander Donahue** (human-in-the-loop). A survey/assessment of an open problem; it makes no claim of a new result. Citations carry verification flags and require human source-checking.

## Abstract

The moving sofa problem asks for the sofa constant $\mu$: the largest area of a rigid planar region that can be maneuvered around a single right-angled corner in a corridor of unit width. Posed by Leo Moser in 1966, it is the two-dimensional escalation of the elementary "ladder around a corner" exercise, and its difficulty is genuinely two-sided — lower bounds require an explicit shape and a valid motion, upper bounds require excluding all shapes and all motions. The standing lower bound, $\mu \ge \mu_G \approx 2.219531669$, has been Gerver's 18-piece shape since 1992; the best published unconditional upper bound is $\mu \le 2.37$ (Kallus–Romik, 2018). In November 2024 Jineon Baek posted a preprint claiming a proof that $\mu = \mu_G$, i.e. that Gerver's sofa is optimal. This meta-analysis surveys the envelope/corridor-intersection method, the calculus-of-variations characterization, the finite-angle upper-bound machinery, and the role of variant problems such as Romik's ambidextrous sofa. It treats Baek's claim as a proof under verification, not an accepted theorem, and records what an accepted resolution would require. It makes no original mathematical claim.

## 1. Statement and significance

Fix an L-shaped hallway whose two arms each have width 1, meeting at a single $90^\circ$ corner. A "sofa" is a rigid planar region that may be translated and rotated continuously but must lie entirely within the hallway at every instant. The sofa constant $\mu$ is the supremum of areas of regions admitting such a motion from one arm to the other. The problem was posed in print by Leo Moser in 1966. Its appeal is the same as that of several other Moser problems (the worm problem, the Moser spindle in the Hadwiger–Nelson question): trivial to state, demanding genuine geometric machinery to attack. The optimal boundary is not a conic but an envelope of swept lines, which is precisely why the area-maximization version is so much harder than the one-dimensional rod version.

## 2. State of the art

Unconditionally, the present bracket is $2.2195 \le \mu \le 2.37$.

- **Lower bound (unbeaten since 1992):** $\mu \ge \mu_G \approx 2.219531669$, realized by Gerver's sofa, whose boundary is assembled from 18 analytic pieces — straight segments, circular arcs, and arcs of involutes of circles. No larger admissible shape has ever been exhibited.
- **Upper bound (best published rigorous):** $\mu \le 2.37$, proved by Kallus and Romik (2018) via computer-assisted analysis bounding the area of the intersection of finitely many corridor placements. This superseded Hammersley's classical $\mu \le 2\sqrt{2} \approx 2.8284$.

The current frontier is a November 2024 preprint by Jineon Baek, *Optimality of Gerver's Sofa* (arXiv:2411.19826, identifier needs verification), claiming a complete proof that $\mu = \mu_G$. Honestly characterized, this is a long, technical, single-author manuscript settling a famous problem; it is a claimed proof undergoing verification, not yet an accepted theorem. No refutation or retraction is recorded, but neither is community confirmation. This meta-analysis therefore records $\mu_G$ and $2.37$ as the standing unconditional facts and $\mu = \mu_G$ as the conjectured — and now claimed — value.

## 3. Principal approaches and barriers

**Envelope / corridor-intersection method (lower bounds).** Hammersley's 1968 reformulation fixes the sofa and slides the rotating L-corridor over it; an admissible shape lies inside the intersection of all corridor placements, so its boundary is an envelope of moving inner-corner lines. Applied to a simple one-parameter motion this yields Hammersley's shape ($\pi/2 + 2/\pi \approx 2.2074$); applied with a richer translate-and-rotate motion, Gerver (1992) obtained the 18-piece shape with involute arcs, area $\mu_G$. The barrier is intrinsic: the method *constructs* candidates via a local matching condition but does not *certify global optimality*.

**Calculus of variations / Euler–Lagrange characterization.** Treating the boundary as an unknown function stationary for area under the corridor constraint explains why Gerver's pieces take their form (the involutes are forced by the contact geometry) and yields necessary conditions for any smooth optimizer. The barrier is that necessary conditions for a smooth critical shape do not exclude a larger competitor of different or lower-regularity contact structure. Promoting "Gerver's shape is the unique smooth critical point of this type" to "$\mu = \mu_G$" is the hard step that Baek's 2024 preprint claims to complete.

**Finite-angle / LP upper bounds (computer-assisted).** Any admissible sofa fits inside the intersection of corridors at finitely many rotation angles; the maximal area of that intersection is a computable upper bound. Kallus and Romik (2018) certified $\mu \le 2.37$ this way. The barrier is that the relaxation has a genuine gap from $\mu$ that closes only asymptotically; squeezing from $2.37$ down to $2.2195$ by adding angles appears computationally infeasible, which is what motivated the search for a closed-form optimality proof.

**Variants as testing grounds.** Romik (2017) fully solved the ambidextrous sofa (must turn both left and right), finding the exact "Romik sofa" of area $\approx 1.6449$ — a complete theorem for a cousin problem that validated the envelope/variational machinery. Unequal corridor widths, non-right-angle corners, and 3D analogues remain mostly exploratory.

## 4. Critical assessment

The dossier's central judgment is sound and, importantly, well-calibrated: it neither dismisses Baek's claim nor accepts it, and it keeps the unconditional ledger ($\mu_G$ below, $2.37$ above) cleanly separated from the conditional frontier. This is the correct posture for a single-author proof of a sixty-year problem that has not yet completed independent verification. The structural story is also internally consistent — the same variational characterization that *constructs* Gerver's shape is what an optimality proof must *upgrade* into a matching upper bound, and the survey makes that load-bearing connection explicit.

Two cautions. First, the numerical values are stable across the literature and self-consistent ($\mu_G \approx 2.2195$ sitting strictly inside $[2.2074, 2.37]$), but several bibliographic identifiers are explicitly uncertain — the Romik DOI, the Kallus–Romik arXiv id, and the Baek arXiv id are all flagged for confirmation, and the papers table itself notes this. Second, the survey is necessarily reliant on second-hand descriptions of Baek's argument ("reportedly upgrades the variational characterization"); no independent verification is cited, and that limitation should remain visible to any reader.

## 5. What a resolution would require / open directions

An accepted resolution must do one of two things. (1) **Confirm $\mu = \mu_G$** by an upper-bound argument matching Gerver's value — exactly what Baek's preprint attempts — which requires showing that *no* admissible shape, smooth or not, symmetric or not, exceeds $\mu_G$, i.e. that Gerver's local/variational optimum is the global maximizer over all rigid regions and motions. (2) **Or exhibit a larger shape**, refuting the long-standing conjecture; given the stability of Gerver's value across three decades this is regarded as unlikely. The dominant near-term route is independent verification of Baek (2024). Secondary routes include strengthening the finite-angle/LP relaxation toward $\mu_G$ analytically, and a structure theory for any optimizer informed by the fully solved ambidextrous variant and by corridor-width generalizations.

## 6. Selected references

1. Leo Moser (1966), *Problem 66-11 (moving sofa)*, Problems and Solutions. [high-confidence]
2. J. M. Hammersley (1968), sofa reformulation and bounds (in the "enfeeblement of mathematical skill" essay). [needs-verification]
3. H. T. Croft (1976), *Research Problems in Discrete Geometry* (early listing). [needs-verification]
4. H. T. Croft, K. J. Falconer, R. K. Guy (1991), *Unsolved Problems in Geometry*. [high-confidence]
5. Joseph L. Gerver (1992), *On Moving a Sofa Around a Corner*, *Geometriae Dedicata*. [high-confidence]
6. Eric W. Weisstein (2003), *The Moving Sofa Problem* (MathWorld exposition). [needs-verification]
7. Peter Winkler (2005), *Mathematical Puzzles: A Connoisseur's Collection* (sofa discussion). [needs-verification]
8. Philip Gibbs (2008), *A Note on Moving a Sofa* (bounds/refinements). [needs-verification]
9. Philip Gibbs (2011), *An Ambidextrous Sofa* (early two-way variant). [ai-suggested]
10. Dan Romik (2016), *The Moving Sofa Problem* (expository survey). [high-confidence]
11. Dan Romik (2017), *Differential equations and exact solutions in the moving sofa problem*, DOI 10.1080/10586458.2016.1270858. [needs-verification]
12. Yoav Kallus, Dan Romik (2018), *Improved Upper Bounds in the Moving Sofa Problem*. [high-confidence]
13. Yoav Kallus, Dan Romik (2018), arXiv:1706.06630 (preprint of the upper-bound paper). [needs-verification]
14. Jineon Baek (2024), *Optimality of Gerver's Sofa*, arXiv:2411.19826. [needs-verification]
15. Steven R. Finch (2003), *Mathematical Constants* (sofa constant entry). [needs-verification]

## AI Review Panel

### Claude (Anthropic) — in-house review

Strengths: this survey gets the hardest editorial decision right. The 2024 Baek preprint is treated throughout as a claim under verification rather than a settled theorem, and the unconditional bracket $[2.2195, 2.37]$ is kept rigorously distinct from the conjectured-and-claimed equality $\mu = \mu_G$. The technical narrative is coherent and the barriers are stated at the right level of generality — in particular the recurring point that the envelope/variational machinery *constructs* Gerver's shape via a local condition but cannot by itself certify global optimality, which is exactly the gap an upper-bound proof must close.

Three concerns a human reviewer should weigh. (i) Every citation here carries a verification flag, and several of the most load-bearing identifiers — the Romik DOI (10.1080/10586458.2016.1270858), the Kallus–Romik arXiv id (1706.06630), and above all the Baek arXiv id (2411.19826) — are marked needs-verification. These must be checked against primary sources before the document is treated as authoritative; an incorrect arXiv id on the very paper the frontier rests on would be a material error. (ii) The account of Baek's argument is unavoidably single-sourced and second-hand ("reportedly upgrades the variational characterization"); there is no independent technical verification cited, and the survey should not be read as endorsing correctness. (iii) The single most important thing to verify is the live status of Baek (2024): whether, as of the human review date, it has been peer-reviewed, accepted, refuted, or revised — because that one fact determines whether the problem's status remains "active-progress" or moves to resolved.

Subject to those checks — primarily confirming the identifiers and the current verification status of the Baek preprint — this is an accurate and honest survey that overstates nothing.

**Verdict:** accept-with-revisions.

### GPT (OpenAI) — pending
_Not yet run. To complete the panel, run the prompt in docs/review/REVIEW-TEMPLATE.md through GPT and record the verdict here and in the front matter._

### Gemini (Google) — pending
_Not yet run. See docs/review/REVIEW-TEMPLATE.md._

### Grok (xAI) — pending
_Not yet run. See docs/review/REVIEW-TEMPLATE.md._

## Human verification

AI review is not human peer review. This assessment is offered for academic verification per ../docs/review/ACADEMIC-REVIEW.md; the AI panel can flag gaps and miscalibration but cannot certify the underlying mathematics or the bibliographic record. A human reviewer should source-check the flagged citations and confirm the current status of the Baek (2024) claim. Status: human_review pending.

---
*Accredited to **Alexander Donahue** · The Unsolved Mathematics Atlas · CC BY 4.0. Cite per CITATION.cff.*

# Attempts — The Moving Sofa Problem

_Notable attempts, near-misses, retracted proofs._

The history of the sofa constant is unusually clean on the lower-bound side — one construction has stood unbeaten for over thirty years — and slow but steady on the upper-bound side. The interest lies in the near-misses, the conjectures that proved false, and the recent claimed resolution.

## Hammersley's shape and his false optimality conjecture (1968)

John Michael Hammersley not only reformulated the problem via the corridor-intersection picture but produced an elegant explicit candidate: a rectangle of length 2 and width 1 with a semicircle of radius $2/\pi$ removed from the bottom edge and two quarter-pieces arranged to clear the corner, giving area $\pi/2 + 2/\pi \approx 2.2074$. Hammersley conjectured this might be optimal. This was a genuine near-miss that was later **disproved by construction**: Gerver's shape is demonstrably larger, so Hammersley's optimality conjecture is false. The episode is the standard cautionary tale that "clean closed form" does not imply "extremal."

## Gerver's construction (1992) — the standing record

Joseph Gerver's 18-piece shape, area $\mu_G \approx 2.219531669$, is the central near-miss in the sense that it is *conjectured* to be exactly optimal but, until 2024, had no matching upper bound. Gerver himself conjectured optimality and gave heuristic support, but explicitly did not prove that no larger shape exists. For three decades, the situation was: best lower bound $= \mu_G$, best upper bound $> \mu_G$, with the community broadly believing the lower bound was tight.

## Romik's ambidextrous solution (2017)

Dan Romik fully solved the *ambidextrous* variant — a partial result of the strongest kind, in that it is a complete theorem for a closely related problem. The Romik sofa (area $\approx 1.6449$) is the exact maximizer for a shape required to turn both ways. This is not a partial result on $\mu$ itself, but it validated the envelope/variational machinery on a tractable cousin and increased confidence that Gerver-type analysis captures the right structure.

## Kallus–Romik upper bound (2018)

The certified bound $\mu \le 2.37$ is the most significant rigorous partial result on the upper-bound side. It is computer-assisted (validated numerics over a finite angle set) and represents real progress from Hammersley's $2\sqrt 2$, but it left a substantial gap to $\mu_G \approx 2.2195$ and did not, by itself, suggest how to close that gap analytically.

## Baek's 2024 claimed proof of optimality (disputed-as-unverified, not refuted)

In late 2024, **Jineon Baek** posted a lengthy preprint claiming a complete proof that $\mu = \mu_G$ — i.e. that Gerver's sofa is optimal. The argument reportedly establishes an upper bound matching Gerver's value through a careful variational/optimization analysis combined with rigorous estimates, resolving the long-standing question if correct.

State of the claim, neutrally: as of the present, this is a **claimed proof undergoing verification**, not an accepted theorem. The relevant caution is the usual one for a long, technical, single-author preprint that settles a famous open problem: such proofs require time and independent scrutiny before acceptance, and no specific published refutation is recorded here. There is no indication of retraction. Until peer review and community checking conclude, the honest description is that the lower bound $\mu_G$ is unbeaten, the best *published* unconditional upper bound is $2.37$ (Kallus–Romik), and the gap is claimed — but not yet confirmed by the community — to be closed. See status.md for the live frontier and citation.

## On crank/erroneous attempts

Because the problem is easy to state, it attracts informal "solutions." None of the credible mathematical literature records a serious *refuted* proof of optimality prior to Baek; the genuine error in the record is Hammersley's optimality conjecture, corrected by Gerver's larger construction. This relative cleanliness — one record-holding shape, one false optimality conjecture, one recent claimed proof — is characteristic of the problem.

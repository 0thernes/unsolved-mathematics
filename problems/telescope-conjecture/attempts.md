# Attempts — The Telescope Conjecture (Disproved 2023)

_Notable attempts, near-misses, retracted proofs._

The telescope conjecture's history is unusual: there was no high-profile *claimed proof* that later collapsed, and no widely circulated *false counterexample*. Instead there was a long stretch of computational reconnaissance whose results were genuinely ambiguous, followed by a decisive disproof. The neutral record below distinguishes evidence from proof.

## The height-2 computational program (Mahowald–Ravenel–Shick)

The most sustained attempt to settle the conjecture by direct computation was the height-2 work of **Mark Mahowald, Douglas Ravenel, and Paul Shick**, pursued from the late 1980s through the 2000s ("The triple loop space approach to the telescope conjecture," 2001, and related papers). They studied the $v_2$-periodic homotopy of Smith–Toda complexes at primes $p \ge 5$ via the localized Adams spectral sequence. The program produced detailed charts but **could not reach a verdict**: the computations were consistent with both truth and failure, and Ravenel himself repeatedly framed the work as a *test* rather than an expected confirmation. This is the principal "near-miss" — an attempt that mapped the terrain without resolving it.

## Early skepticism and informal counterexample folklore

From the 1990s onward several experts (including Ravenel) voiced doubt that the conjecture held at $n \ge 2$, citing apparent numerical discrepancies in the $v_2$-periodic ranges. These were **not** rigorous counterexamples; the suspected "extra" classes lay beyond computable bounds, so the folklore skepticism remained heuristic. No published claim of a counterexample from this era survived scrutiny.

## Why no false proofs accumulated

Unlike many famous open problems, the telescope conjecture did not attract numerous amateur or flawed "solutions." Its statement is deep inside chromatic homotopy theory, requiring the Nilpotence and Periodicity theorems even to formulate cleanly, which kept casual attempts away. The serious community treated it as genuinely open and hard.

## The 2023 disproof (not disputed)

The resolution came from **Robert Burklund, Jeremy Hahn, Ishan Levy, and Tomer Schlank** in 2023, who proved the conjecture **false for all $n \ge 2$ and all primes**. Crucially, this is a *disproof*, not a contested claim: it rests on independently established pillars — the Lichtenbaum–Quillen property for $\mathrm{BP}\langle n\rangle$ (Hahn–Wilson), the chromatic Nullstellensatz (Burklund–Schlank–Yuan), and redshift results — and was vetted by the chromatic homotopy community without substantive objection. As of the present frontier there is **no dispute** over the disproof itself; ongoing work concerns its quantitative consequences (the precise size and growth of the telescopic–vs–$K(n)$-local gap), not its validity.

## Net assessment

The instructive lesson is methodological: four decades of computation could neither confirm nor refute the conjecture because the obstruction is invisible to height-$n$ tools and only surfaces through algebraic $K$-theory ascending to height $n+1$. The "attempts" record is therefore less a catalogue of errors than a demonstration that the right machinery (trace methods) had to be built before the question could be answered.

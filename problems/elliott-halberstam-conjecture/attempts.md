# Attempts — The Elliott–Halberstam Conjecture

_Notable attempts, near-misses, retracted proofs._

The Elliott–Halberstam conjecture has not attracted a culture of "claimed proofs" the way Goldbach or the twin-prime conjecture have; it is technical enough that amateurs rarely engage it, and experts regard the full uniform statement as out of reach of present methods. The notable history is instead one of **genuine partial progress and well-defined near-misses**.

## Bombieri–Friedländer–Iwaniec: past the square-root barrier (for fixed classes)

The single most important near-miss is the work of **Bombieri, Friedländer, and Iwaniec** (1986–1989). Using the dispersion method and Deshouillers–Iwaniec bounds for averages of Kloosterman sums, they proved level-of-distribution estimates *exceeding* $1/2$ — reaching $\theta = 4/7$ — but only for a **fixed** residue class $a$, with the supremum over $a$ removed. This established that the $1/2$ barrier is not an absolute feature of the primes, lending strong heuristic support to EH while falling short of the uniform statement. It remains the deepest unconditional evidence for the conjecture.

## Zhang's restricted distribution estimate (2013)

**Yitang Zhang's** celebrated 2013 paper *Bounded gaps between primes* (Annals of Mathematics, 2014) did not attempt full EH. Its arithmetic heart is a *restricted* Bombieri–Vinogradov estimate valid for **smooth, well-factorable moduli** at level $\theta = 1/2 + 1/584$. This was enough, via GPY, to produce the first finite bound on prime gaps ($< 7\times 10^7$). The result was independently checked and rapidly absorbed by the community; no dispute arose, though the original exponent was quickly improved.

## Polymath8: optimization and verification

The **Polymath8a** collaboration (2013–14, organized largely through Terence Tao's blog) re-derived, simplified, and substantially strengthened Zhang's distribution estimate, pushing the restricted level toward $\theta = 1/2 + 7/300$ and exposing exactly which exponential-sum inputs (Weil/Deligne, Birch–Bombieri) controlled the gain. This is a near-miss in the sense that it represents the current practical ceiling for unconditional level-of-distribution gains, still confined to special moduli.

## Maynard–Tao: sidestepping the distribution problem

**James Maynard** (2013, *Annals* 2015) and, in parallel, **Terence Tao** introduced a multidimensional sieve that obtains bounded gaps using only the unconditional Bombieri–Vinogradov level $\theta = 1/2$ — in effect making the hard distribution gains of Zhang unnecessary for the *finiteness* of gaps. Under the **generalized** Elliott–Halberstam conjecture, the same machinery (refined in **Polymath8b**) yields $\liminf(p_{n+1}-p_n)\le 12$, the strongest conditional consequence to date. This is a near-miss on the *conclusion* (twin primes would require $\le 2$, which the parity problem forbids from EH alone) rather than on the conjecture itself.

## Status of disputed claims

There are **no widely circulated retracted or disputed claimed proofs** of the full uniform Elliott–Halberstam conjecture in the refereed literature. The conjecture's profile is that of a respected, deeply studied open problem approached through incremental, peer-verified gains, not through dramatic claimed solutions. Any future claim should be evaluated against the parity obstruction and against whether it genuinely supplies new exponential-sum cancellation beyond the large sieve — the precise point where every prior unconditional approach has stalled.

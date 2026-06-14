# Attempts — Lehmer's Conjecture on the Ramanujan Tau Function

_Notable attempts, near-misses, retracted proofs._

The conjecture has attracted steady, serious effort, but — unlike some famous open problems — it has not generated a public record of high-profile *claimed* proofs that were later retracted. Its status as genuinely hard is widely accepted, and most experts regard it as out of reach of present methods. The notable contributions are therefore partial results and reductions rather than disputed solutions. They should be read as honest progress that stops short of the goal, not as failed proofs.

## Computational near-certainty

Lehmer's 1947 verification ($n<33{,}333$) has been extended relentlessly. The introduction of the Edixhoven–Couveignes polynomial-time algorithm for $\tau(p)$ (book, 2011) and its implementations let researchers evaluate $\tau(p)$ for individual primes of very large size, and to sweep ranges far beyond what naive recursion allows. Every computed value is nonzero. This makes the conjecture *empirically overwhelming* but, as a matter of logic, computation cannot close it: a single unexamined large prime could in principle harbor a zero, and no bound is known beyond which zeros are provably impossible.

## Murty–Murty–Shorey: the finiteness near-miss

Perhaps the strongest unconditional structural result toward "$\tau$ avoids fixed values" is due to M. Ram Murty, V. Kumar Murty, and T. N. Shorey (1987). Using Baker's theory of linear forms in logarithms, they proved that for each fixed integer $v$, the equation $\tau(n)=v$ has only finitely many solutions, with an *effective* bound, and that $|\tau(n)|\to\infty$ effectively through nonzero values. This is tantalizingly close: it controls every fixed nonzero target. But the method degenerates precisely at $v=0$ — the transcendence input that yields a nontrivial lower bound for $|\tau(n)-v|$ collapses when $v=0$ — so it leaves Lehmer's conjecture itself untouched. It is the canonical example of a technique that "almost" resolves the problem but provably cannot reach the one value that matters.

## Serre–Swinnerton-Dyer: constraining a hypothetical zero

Serre and Swinnerton-Dyer's determination (1972–1977) of the image of $\rho_{\Delta,\ell}$ and the exceptional primes does not attempt a proof of non-vanishing; instead it converts a hypothetical zero into a list of necessary congruence conditions. A prime $p$ with $\tau(p)=0$ must simultaneously satisfy trace-zero conditions modulo $2,3,5,7,23,691$ (and their relevant powers). This is the principal tool for *ruling out* zeros in arithmetic progressions and for guiding searches, and it explains why no small zero exists — but it is finite local data and cannot cover all primes.

## Sato–Tate as a "why it should be true" heuristic

The proof of Sato–Tate for $\Delta$ (Barnet-Lamb–Geraghty–Harris–Taylor, 2011) gives the equidistribution of the angles $\theta_p$ and thereby a precise heuristic that $\tau(p)$ should be $0$ for a density-zero set of primes — consistent with "never." Effective and conditional refinements (under GRH for the relevant symmetric-power $L$-functions) sharpen the rarity of small $|\tau(p)|$. This is strong *evidence* and a clean explanatory framework, but, by its measure-zero nature, it is not and cannot be a proof.

## Status of claimed proofs

To date there is no widely circulated claimed proof of Lehmer's tau conjecture that the community has had to adjudicate or retract. Occasional informal claims and preprints proposing elementary or congruence-based proofs appear, but none has gained acceptance; the standard objection is the same in each case — they implicitly require excluding a single sporadic Frobenius-trace zero, which finitely many congruences and equidistribution statements cannot do. In the interest of neutrality: the absence of a disputed "proof" reflects the problem's reputation for hardness rather than any settled negative result. The honest summary is that the conjecture is believed true, supported by overwhelming computation and a coherent heuristic, and unproven.

# Status & Frontier — Lehmer's Conjecture on the Ramanujan Tau Function

_Where the problem stands and what a resolution would require._

**Status: open.** The conjecture $\tau(n)\ne 0$ for all $n\ge1$ has been verified far beyond any feasible search range and is universally believed true, but no proof exists. No claimed proof is in dispute; the difficulty is structural, not a matter of awaiting confirmation of a recent announcement.

## What is known unconditionally

- **Reduction.** $\tau(n)\ne 0$ for all $n$ $\iff$ $\tau(p)\ne 0$ for all primes $p$ (multiplicativity + Hecke recursion). A single prime zero would force $\tau(p^{r})=0$ for all odd $r$.
- **Size.** $|\tau(p)|\le 2p^{11/2}$ (Deligne, 1974). This is sharp in magnitude but compatible with $\tau(p)=0$.
- **Image of Galois.** The representation $\rho_{\Delta,\ell}$ has open image in $\mathrm{GL}_2(\mathbb{Z}_\ell)$ for all $\ell$; the exceptional primes are exactly $\{2,3,5,7,23,691\}$ (Serre, Swinnerton-Dyer). A hypothetical zero must satisfy simultaneous trace-zero congruences modulo these.
- **Equidistribution.** Sato–Tate holds for $\Delta$ (Barnet-Lamb–Geraghty–Harris–Taylor, 2011): the angles $\theta_p$ with $\tau(p)=2p^{11/2}\cos\theta_p$ equidistribute for $\tfrac{2}{\pi}\sin^2\theta\,d\theta$. Vanishing is the measure-zero event $\theta_p=\pi/2$.
- **Value equations.** For each fixed $v\ne 0$, $\tau(n)=v$ has finitely many, effectively bounded solutions (Murty–Murty–Shorey, 1987), and $\tau(n)=\pm\ell^m$ is resolved for many $\ell$ (Bennett et al., 2020s). The case $v=0$ is precisely the one these methods cannot reach.
- **Computation.** $\tau(p)$ is computable in time polynomial in $\log p$ (Edixhoven–Couveignes, 2011); all computed values are nonzero.

## What is known conditionally

Under GRH for the symmetric-power $L$-functions $L(s,\mathrm{Sym}^k\Delta)$, effective Sato–Tate gives quantitative bounds on the number of primes $p\le X$ with small $|\tau(p)|$, making zeros provably extremely sparse — but still not excluded. No conditional argument (under GRH, BSD, or standard automorphy hypotheses) is known to deliver full non-vanishing.

## What a full resolution requires

A proof must control the *exact value* (not merely the size or distribution) of the Frobenius trace $\tau(p)$ at **every** prime simultaneously. The obstruction is sharp: the set of trace-zero elements in the image of Galois is nonempty (so group theory alone permits zeros) yet has density zero (so Chebotarev and equidistribution see nothing). Bridging "no zero has density zero" to "no zero exists" is the crux. Resolution would need genuinely new input — plausibly an arithmetic or geometric mechanism forbidding $\tau(p)=0$ outright, rather than a counting argument.

## Plausible routes

1. **A new Diophantine reduction** turning $\tau(p)=0$ into a finite, decidable statement (e.g. integral points on an explicit curve), extending the value-equation program to the degenerate target $v=0$.
2. **A finer Galois-theoretic obstruction** — a congruence or local condition, perhaps at a prime not yet exploited, incompatible with trace-zero Frobenius.
3. **An automorphy/$L$-function argument** extracting non-vanishing from analytic properties of $L(s,\Delta)$ or its symmetric powers beyond what equidistribution yields.
4. **Refutation** — an unanticipated large prime with $\tau(p)=0$, found by targeted computation guided by the congruence conditions; considered very unlikely but logically the only way computation could settle it.

None of these is currently within reach, and the consensus is that the problem will outlast incremental refinement of present techniques.

## Related problems

- [Lehmer's Mahler-Measure Conjecture](../lehmer-mahler-measure-conjecture/README.md)
- [Riemann Hypothesis](../riemann-hypothesis/README.md)
- [Grand Riemann Hypothesis](../grand-riemann-hypothesis/README.md)
- [Sato–Tate / Chowla Conjecture](../chowla-conjecture/README.md)
- [Sarnak–Möbius Conjecture](../sarnak-mobius-conjecture/README.md)

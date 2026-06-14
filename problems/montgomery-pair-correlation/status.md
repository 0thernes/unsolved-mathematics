# Status & Frontier — Montgomery's Pair Correlation Conjecture

_Where the problem stands and what a resolution would require._

**Status: open.** The strong pair correlation conjecture — that $F(\alpha,T)\to 1$ uniformly for $1\le|\alpha|\le A$, equivalently that the pair correlation of normalized zeta zeros converges to the GUE density $1-\big(\tfrac{\sin\pi u}{\pi u}\big)^2$ — remains unproven. No retraction or claimed resolution is on record; the metadata status is correct and no resolving paper exists to cite.

**What is known (unconditional, in the sense of "RH-free" smoothed statements).**
- The function-field analogue is a *theorem*: Katz–Sarnak (1996/1999) established the conjectured RMT statistics for families of curve $L$-functions over $\mathbb{F}_q$ via monodromy.
- Rudnick–Sarnak (1994) proved that the $n$-level correlations of zeros of $\zeta$ and of general automorphic $L$-functions match GUE for test functions of suitably restricted Fourier support — generalizing Montgomery's result to all correlation orders within the trivial range.

**What is known conditionally (under RH).**
- Montgomery (1973): $F(\alpha)\sim|\alpha|$ for $|\alpha|<1$, hence the pair-correlation asymptotic holds for test functions supported in $(-1,1)$ in the dual variable.
- Goldston–Montgomery (1987): the conjecture is equivalent to a precise asymptotic for the variance of primes in short intervals.
- Consequences within the proven range: at least a positive proportion of zeros are simple, and a positive proportion of "small gaps" exist, with the GUE model predicting the precise constants.

**What a full resolution requires.** The single decisive obstruction is the **support barrier at $|\alpha|=1$**. Pushing $F(\alpha)$ to constant value $1$ for $|\alpha|\ge1$ demands uniform control of the off-diagonal terms in the explicit-formula sum — effectively a strong, *uniform* form of the Hardy–Littlewood prime-pair (and prime-tuple) conjecture with explicit error terms. Such uniformity is itself open and is widely regarded as at least as hard as the surrounding problems; an unconditional proof of the strong conjecture would be a landmark in the theory of prime correlations, not merely a statement about zeros.

**Plausible routes.**
1. New unconditional input on prime-pair correlations (uniform in shift), enlarging the admissible support of $F(\alpha)$ beyond $1$ — the most direct but hardest path.
2. Transfer of function-field/monodromy techniques to the number-field setting, currently with no known mechanism.
3. A genuine spectral realization (Hilbert–Pólya): exhibiting the zeros as eigenvalues of a self-adjoint operator with GUE statistics would yield pair correlation as a corollary; the Berry–Keating / quantum-chaos program pursues this heuristically.
4. Refinements from the RMT moment/ratios models (Keating–Snaith, CFKRS) that, if derived from arithmetic rather than posited, would supply the lower-order structure and possibly the leading law.

The overwhelming numerical agreement (Odlyzko) and the proven restricted-support and function-field cases leave essentially no doubt that the conjecture is *true*; the open problem is to *prove* the unrestricted GUE law over $\mathbb{Q}$.

## Related problems

- [Riemann Hypothesis](../riemann-hypothesis/README.md)
- [Twin Prime Conjecture](../twin-prime-conjecture/README.md)
- [Hardy–Littlewood $k$-tuple Conjecture](../hardy-littlewood-k-tuple/README.md)
- [Polignac's Conjecture](../polignac-conjecture/README.md)
- [Legendre's Conjecture](../legendre-conjecture/README.md)

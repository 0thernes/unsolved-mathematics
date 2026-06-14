# Status & Frontier — The Chowla Conjecture

_Where the problem stands and what a resolution would require._

**Status: active-progress.** The Chowla conjecture is open in its original natural-density form, but the last decade has produced major partial resolutions, chiefly under logarithmic averaging.

## What is known (unconditional)

- **Single sums.** $\sum_{n\le x}\lambda(n)=o(x)$ is the Prime Number Theorem — known since 1896/1899. This is the $k=1$ base case.
- **Logarithmically-averaged two-point Chowla.** Tao (2016) proved $\sum_{n\le x}\frac{\lambda(n)\lambda(n+h)}{n}=o(\log x)$ for every fixed $h\neq 0$, via the **entropy decrement argument** (arXiv:1509.05422).
- **Logarithmically-averaged odd-order Chowla.** Tao and Teräväinen (2018) extended this to all correlations of **odd order** $k$ and arbitrary distinct shifts (arXiv:1802.05870), and established the equivalence with the logarithmic Sarnak conjecture in broad generality.
- **Averaged (non-logarithmic) two-point Chowla.** Matomäki, Radziwiłł and Tao (2016) proved the two-point conjecture **averaged over the shift** $h\le H$ with $H\to\infty$ (building on the Matomäki–Radziwiłł short-interval theorem, arXiv:1501.04585).
- **Sign patterns.** All length-3 sign patterns of $\lambda$ occur with positive density (Hildebrand, 1986); the count of realized patterns grows superlinearly (Matomäki–Radziwiłł–Tao).

## What is known (conditional)

- Under the **logarithmic Sarnak conjecture** or suitable ergodic uniformity hypotheses (Frantzikinakis–Host), further cases of logarithmic Chowla follow.
- GRH and zero-density hypotheses sharpen error terms but, notably, do **not** imply Chowla — the correlation content is believed to be orthogonal to, and harder than, the Riemann Hypothesis.

## What a full resolution requires

1. **Remove logarithmic averaging.** Pass from $\sum \frac{1}{n}$-weighted sums to natural-density sums $\frac{1}{x}\sum_{n\le x}$ for a *fixed* shift. This demands control of "thin scales" where multiplicativity gives no leverage — the central obstruction.
2. **Reach even-order correlations.** The entropy decrement argument constrains only odd products (where the twist $\lambda(pn)=-\lambda(n)$ survives); even orders (e.g. the four-point sum) need a genuinely new idea.
3. **Break the parity barrier quantitatively** beyond the single-shift case, presumably via higher-order Gowers-norm inverse theory for multiplicative functions, which remains incomplete.

## Plausible routes

- **Higher uniformity** estimates for multiplicative functions in short intervals (Matomäki–Shao–Tao–Teräväinen) feeding improved Gowers-norm control.
- An ergodic-theoretic resolution of the structure of characteristic factors that upgrades logarithmic statements to natural density.
- A new mechanism decoupling shifted values without averaging, the analogue of entropy decrement for even orders.

No claimed proof of the natural-density or even-order conjecture has been accepted by the community; the conjecture is uniformly listed as open. The realistic near-term targets are the **natural-density two-point case at a fixed shift** and the **logarithmic four-point (even-order) case**.

## Related problems

- [Sarnak's Möbius Disjointness Conjecture](../sarnak-mobius-conjecture/README.md)
- [Elliott–Halberstam Conjecture](../elliott-halberstam-conjecture/README.md)
- [Riemann Hypothesis](../riemann-hypothesis/README.md)
- [Twin Prime Conjecture](../twin-prime-conjecture/README.md)
- [Hardy–Littlewood $k$-tuple Conjecture](../hardy-littlewood-k-tuple/README.md)

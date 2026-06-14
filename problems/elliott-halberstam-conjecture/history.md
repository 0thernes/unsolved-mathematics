# History — The Elliott–Halberstam Conjecture

_Origin, formulation, and timeline._

## Origin and motivation

The conjecture grew out of the great sieve-theoretic results on primes in arithmetic progressions established in the mid-1960s. For a modulus $q$ coprime to $a$, the natural error term in the prime-counting function is
$$\Delta(x;q,a) = \pi(x;q,a) - \frac{\pi(x)}{\varphi(q)},$$
and the central question is: for how large a range of moduli $q$ does the prime counting function behave, *on average over $q$*, as the Generalized Riemann Hypothesis (GRH) would predict?

In 1965 Enrico Bombieri and (independently, in slightly different form) A. I. Vinogradov proved that for any $A>0$ there is a $B=B(A)$ with
$$\sum_{q \le x^{1/2}/(\log x)^B} \max_{(a,q)=1} \left| \psi(x;q,a) - \frac{x}{\varphi(q)} \right| \ll_A \frac{x}{(\log x)^A}.$$
This **Bombieri–Vinogradov theorem** reaches moduli up to $x^{1/2}$ on average — exactly the strength GRH gives for individual moduli — and it is often described as "GRH on average." The level of distribution $\theta$ is the supremum of exponents for which such a bound holds with $q\le x^\theta$; Bombieri–Vinogradov gives $\theta = 1/2$.

In their 1968 monograph **Sequences** (Vol. I), Peter D. T. A. Elliott and Heini Halberstam conjectured that this can be pushed essentially as far as possible: the same average bound should hold for every $\theta < 1$, i.e. for moduli up to $x^{1-\varepsilon}$. This is the **Elliott–Halberstam conjecture (EH)**. The barrier at $\theta=1$ itself is genuine — the conjecture is stated for $\theta<1$ — because at level $1$ the individual terms cease to be controllable (the "parity problem" and the breakdown of the asymptotic when $q$ is comparable to $x$).

## Reformulations

EH admits several equivalent or near-equivalent formulations: with the von Mangoldt function $\Lambda$, with the maximal error over residue classes, or with smoothed weights. A crucial weakening is the **Bombieri–Vinogradov-type estimate restricted to a fixed residue class or to smooth/well-factorable moduli** — these "restricted EH" or $\mathrm{EH}[\theta]$ statements are what bounded-gaps arguments actually need, and Zhang's 2013 work proved exactly such a restricted variant for some $\theta>1/2$.

## Timeline

**1965** — Bombieri and Vinogradov independently establish level of distribution $\theta=1/2$ for primes in progressions on average.

**1968** — Elliott and Halberstam state the conjecture ($\theta<1$ for all $\varepsilon$) in their book *Sequences*.

**1970** — Gallagher and others refine and popularize the Bombieri–Vinogradov method; the larger sieve and dispersion methods mature.

**1986–89** — Bombieri, Friedländer, and Iwaniec prove EH-type results *beyond* $\theta=1/2$ for **fixed** residue classes $a$ (level up to $4/7$, later improvements), using the dispersion method and bounds for Kloosterman sums.

**2005** — Goldston, Pintz, and Yıldırım (GPY) show that any level of distribution $\theta>1/2$ would yield **bounded gaps between primes**; under full EH, $\liminf_n (p_{n+1}-p_n) \le 16$.

**2013** — Yitang Zhang proves a restricted Bombieri–Vinogradov estimate for smooth moduli with $\theta = 1/2 + 1/584$, giving the first finite bound $\liminf (p_{n+1}-p_n) < 7\times10^7$.

**2013–14** — The Polymath8a project optimizes Zhang's distribution estimate, reaching effective levels near $\theta = 1/2 + 7/300$.

**2013** — James Maynard (and independently Tao) introduce a multidimensional GPY sieve that gives bounded gaps using **only** Bombieri–Vinogradov ($\theta=1/2$), bypassing Zhang's distribution result; Polymath8b drives the gap to $246$.

**2014** — Maynard's method shows that under the **generalized** Elliott–Halberstam conjecture (GEH) one obtains $\liminf (p_{n+1}-p_n) \le 12$ and $\liminf(p_{n+2}-p_n)\le \text{(small)}$.

**Present** — EH remains open for every $\theta>1/2$ in the *uniform* (max over $a$) sense. The frontier lies in extending Bombieri–Friedländer–Iwaniec-type gains past $1/2$ uniformly, and in the Polymath/Maynard sieve machinery that converts any such gain into sharper prime-gap bounds.

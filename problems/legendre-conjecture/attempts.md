# Attempts — Legendre's Conjecture

Legendre's conjecture has no accepted proof, and — like the other Landau problems — it attracts a steady stream of elementary-looking claimed proofs that do not survive scrutiny. What it does have is a long sequence of genuine partial results that have steadily narrowed, without closing, the gap to the required $x^{1/2}$ threshold.

## Genuine partial results and near-misses

- **Hoheisel (1930).** The first breakthrough: primes exist in $(x, x+x^\theta)$ for some $\theta < 1$, namely $\theta = 1 - 1/33000$. This established that short-interval prime existence was attackable at all, but the interval $x^{0.99997}$ is vastly longer than the $x^{0.5}$ Legendre needs.

- **Ingham (1937).** Using zero-density estimates, Ingham proved that for large $n$ there is a prime between **consecutive cubes** $n^3$ and $(n+1)^3$. This is the natural analogue of Legendre's conjecture one dimension "easier," and it remains, in spirit, the closest fully proved cousin. Notably, the analogue for squares stays out of reach.

- **Huxley (1972/1979).** The exponent $7/12 + \varepsilon$ for prime-containing intervals $(x, x+x^\theta)$ stood as the benchmark for two decades. Still, $7/12 \approx 0.583 > 0.5$.

- **Baker–Harman–Pintz (2001).** The current record: a prime in $(x, x+x^{0.525})$ for all large $x$. This is the closest unconditional approach to Legendre's $x^{0.5}$, yet the residual $0.025$ in the exponent is exactly the unbridged chasm. The authors did not claim Legendre's conjecture, and their method is understood to be unable to reach $1/2$.

- **Cramér (1936) / Selberg (conditional, 1943).** Under the Riemann Hypothesis, Cramér derived $p_{k+1}-p_k = O(\sqrt{p_k}\log p_k)$; Selberg showed RH implies that *almost all* intervals $(n^2,(n+1)^2)$ contain a prime. The word "almost all" is the catch — a sparse exceptional set is not excluded, so even conditionally the *every-$n$* statement is unproven.

## Counts and "almost" statements

Several authors have proved that the interval $(n^2,(n+1)^2)$ contains the *expected* number $\sim n/\log n$ of primes for almost all $n$, and that the number of exceptional $n \le N$ (if any) is small. These results make a counterexample seem extraordinarily unlikely but do not eliminate one.

## Disputed and erroneous claimed proofs

Because the statement is so accessible, Legendre's conjecture is a frequent target of flawed "elementary proofs," many posted to preprint servers (arXiv, viXra) or vanity venues. As a class, these claims fail for recurring reasons, stated here neutrally:

- **Misuse of the prime number theorem.** A common error is to argue that since $(n^2,(n+1)^2)$ should contain $\approx n/\log n$ primes *on average*, it must contain at least one for *every* $n$. The PNT is an asymptotic average statement and provides no per-interval guarantee; the error terms are too large to exclude an empty interval. This conflation of average and uniform behavior is the single most common defect.

- **Circular or unjustified gap bounds.** Some attempts assume a prime-gap bound (e.g. $g(p) < \sqrt{p}$, or Andrica's inequality) that is itself equivalent to or stronger than Legendre's conjecture, then "derive" the conjecture from it.

- **Sieve arguments ignoring the parity barrier.** Several elementary sieve-style proofs implicitly require detecting a prime where Selberg's parity obstruction provably blocks a pure sieve from doing so.

No such claimed proof has been accepted by the mathematical community or published in a reputable peer-reviewed venue with subsequent endorsement. The consensus position is that the conjecture is **open**, and that a correct proof would require fundamentally new ideas beyond the current zero-density-plus-sieve toolkit. Readers should treat any announced "elementary solution" with strong skepticism and look for independent expert verification before accepting it.

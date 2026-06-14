# Attempts — Bunyakovsky's Conjecture

_Notable attempts, near-misses, retracted proofs._

## Almost-prime near-misses

The strongest partial results stop one factor short of the goal.

- **Iwaniec (1978).** For any irreducible quadratic $f$ meeting Bunyakovsky's conditions, $f(n)=P_2$ infinitely often. Applied to $x^2+1$, this is the headline near-miss for Landau's problem: infinitely many $n$ with $n^2+1$ a product of at most two primes. The parity barrier prevents the same machinery from delivering a prime.
- **Richert / Halberstam–Richert** weighted-sieve results give $P_r$ bounds for higher-degree polynomials (the value of $r$ grows with the degree), again never reaching $P_1$.

## Genuinely-prime results for thin multivariate sequences

These are not single-variable Bunyakovsky cases, but they are the only places where the parity barrier was actually beaten for sparse polynomial sequences, and they define the realistic frontier.

- **Friedlander–Iwaniec (1998).** Infinitely many primes of the form $a^2+b^4$. A two-variable polynomial of density $\sim N^{3/4}$; the bilinear structure of the two variables is what breaks parity.
- **Heath-Brown (2001), and Heath-Brown–Moroz.** Infinitely many primes represented by $a^3+2b^3$ (and by suitable binary cubic forms). Density $\sim N^{2/3}$.

Both are celebrated, fully accepted, and frequently cited as the analytic high-water mark — yet neither method extends to a polynomial in a single variable.

## Function-field analogues (proved)

Over $\mathbb{F}_q[t]$ the analogue of Hypothesis H — hence of Bunyakovsky — has been established in significant generality, e.g. by **Sawin and Shusterman** (for $q$ large relative to the degree) and earlier by **Pollack** and others. These are correct theorems in the function-field world; they are not proofs over $\mathbb{Z}$ and rely on geometric inputs (Riemann hypothesis for curves, monodromy) with no integer counterpart. They are cited here as strong evidence, not as a resolution.

## Claimed elementary proofs (disputed / not accepted)

Because $x^2+1$ is so easy to state, it attracts elementary "proofs," chiefly on preprint servers and in self-published notes. None has been accepted by the mathematical community.

- A recurring family of attempts argues from sieve/heuristic density estimates that the count of prime values is positive for all $N$ and concludes infinitude. **Objection:** such arguments invariably collide with the **parity problem** — a density lower bound from a classical sieve cannot certify primality (only $P_2$-ness), so the inference is unjustified. This is the standard, decisive objection raised against every elementary attempt.
- Other attempts misapply Dirichlet's theorem by treating $n^2+1$ as if it lay in a single arithmetic progression; the values of an irreducible quadratic are *not* confined to one progression, so the appeal is invalid.

To be explicit and neutral: **no claimed proof of Bunyakovsky's conjecture — not even of the single case $x^2+1$ — is recognized as correct.** The problem is open. The legitimate "attempts" of record are the almost-prime theorems (Iwaniec) and the multivariate prime theorems (Friedlander–Iwaniec, Heath-Brown), which together show the conjecture is approachable in spirit while the single-variable degree-$\ge 2$ case remains untouched.

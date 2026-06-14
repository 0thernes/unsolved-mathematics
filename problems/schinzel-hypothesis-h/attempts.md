# Attempts — Schinzel's Hypothesis H

_Notable attempts, near-misses, retracted proofs._

Hypothesis H has the unusual status of being so strong that essentially every major result in prime-distribution theory of the last seventy years can be read as a partial result toward it, while no instance of it has ever been fully proved. There is no famous *retracted proof* of the full hypothesis in the published record — its difficulty is so well understood that experts do not announce proofs lightly — but there is a rich catalogue of near-misses and conditional results, and a recurring pattern of overoptimistic preprints on its simplest instances.

## Near-misses and famous partial results

**Chen's theorem (1973).** Chen Jingrun proved that there are infinitely many primes $p$ such that $p+2$ is either prime or a product of two primes ($P_2$). This is the closest unconditional approach to the twin-prime case — arguably the most celebrated single result in the orbit of Hypothesis H — and it is famous precisely for stopping one prime factor short of the goal, blocked by the parity problem.

**Friedlander–Iwaniec (1998) and Heath-Brown (2001).** That $a^2+b^4$ and $a^3+2b^3$ are prime infinitely often are genuine theorems giving primes represented by *polynomial* sequences thinner than the integers. They are not instances of Hypothesis H (which concerns one-variable polynomials), but they are the only proven cases where a sparse polynomial sequence is shown to capture infinitely many primes, and they are the principal evidence that the parity barrier is not absolute.

**Bounded gaps (Zhang 2014; Maynard, Tao 2015).** Zhang's proof that $\liminf_n (p_{n+1}-p_n) < 7\times 10^7$, sharpened by Maynard, Tao, and Polymath8 to $\le 246$, establishes infinitely many bounded prime pairs and, for every $m$, infinitely many bounded $m$-tuples of primes. This proves a *weak existential* form of Dickson/Hypothesis H — some admissible tuple recurs — without resolving any prescribed tuple.

**Green–Tao (2008) and Green–Tao–Ziegler (2012).** The asymptotic count of primes in any finite-complexity linear system is a theorem. It settles a genuinely infinite family of Dickson configurations, the largest unconditional fragment of the linear half of Hypothesis H, while explicitly failing for the infinite-complexity twin-prime pattern.

## Conditional results

Several authors have shown that Hypothesis H or pieces of it follow from other deep conjectures, or imply striking consequences. Under the Elliott–Halberstam conjecture (equidistribution of primes in progressions beyond the Bombieri–Vinogradov range), Maynard's sieve gives gaps as small as $12$ — illustrating how close to the prescribed twin-prime case the methods come when granted an extra hypothesis, yet still falling short of any single tuple. Conversely, Hypothesis H is known to imply numerous statements (e.g. infinitely many primes $n^2+1$, the Sophie Germain conjecture, certain cases of the existence of prescribed prime constellations), which is why it serves as a benchmark "if-then" hypothesis throughout the field.

## Disputed and overoptimistic claims

The simplest unsolved instance — whether $n^2+1$ is prime infinitely often (the degree-2 Bunyakovsky case) — periodically attracts amateur and preprint "proofs." None has survived scrutiny. The recurring flaw is the **parity obstruction**: such arguments typically construct a sieve-type weight that, by Selberg's parity principle, cannot distinguish primes from $P_2$ numbers, so they at best reprove an almost-prime statement. Because this obstruction is a theorem about the limitations of the method class rather than a gap to be patched, the community treats any claimed elementary or pure-sieve proof of a one-variable case as presumptively flawed until the parity barrier is shown to be circumvented by genuinely new (bilinear or higher-order) input. As of the present, no such claim for the integer Hypothesis H has been accepted; the dispute in each case is resolved not by a single cited objection but by appeal to the structural parity theorem. The function-field analogues (Sawin–Shusterman) are accepted and unchallenged, but they do not bear on the integer case.

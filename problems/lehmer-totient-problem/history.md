# History — Lehmer's Totient Problem

Lehmer's totient problem asks whether there exists a *composite* integer $n$ for which Euler's totient $\varphi(n)$ divides $n-1$. Equivalently, writing $k = (n-1)/\varphi(n)$, the question is whether the relation $\varphi(n) \mid n-1$ admits any solution beyond the primes. For every prime $p$ one has $\varphi(p) = p-1$, so $\varphi(p) \mid p-1$ holds trivially; the problem is precisely whether this divisibility *characterizes* the primes. A composite solution would be, in effect, a number "totient-indistinguishable" from a prime — a near-counterexample to the would-be primality criterion "$\varphi(n) = n-1 \iff n$ prime."

The problem arose in 1932 when Derrick Henry Lehmer, working on the structure of Euler's function and on Fermat-type primality testing, isolated the divisibility relation $\varphi(n) \mid n-1$ and observed that it would furnish a primality test if no composite satisfied it. He proved several structural constraints at once: any composite solution $n$ must be odd, squarefree, and a product of at least seven distinct primes ($n = p_1 p_2 \cdots p_k$ with $k \ge 7$). These follow from elementary manipulation of the multiplicativity of $\varphi$ together with the divisibility constraint, and they already showed any counterexample must be enormous.

A central reformulation places the problem inside the family of *Carmichael-like* conditions. A Carmichael number satisfies $\lambda(n) \mid n-1$ (Korselt's criterion, with $\lambda$ the Carmichael function), and these exist in abundance — infinitely many, by Alford–Granville–Pomerance (1994). Lehmer's condition $\varphi(n) \mid n-1$ is strictly stronger, since $\lambda(n) \mid \varphi(n)$; thus every Lehmer number would be a Carmichael number, but the converse fails for all known Carmichael numbers. This nesting — primes $\subset$ Lehmer solutions $\subset$ Carmichael numbers — is the modern frame for the problem and explains why it sits at the heart of multiplicative number theory.

The principal line of progress has been to push up the *minimum number of prime factors* $\omega(n)$ a composite solution must have, and to bound the *count* of any solutions below a height $x$. Successive authors combined sieve estimates with the special algebraic structure of the divisibility to raise the floor and to show solutions, if any, are extraordinarily sparse.

## Timeline

- **1932** — D. H. Lehmer poses the problem in "On Euler's totient function" (*Bull. Amer. Math. Soc.* **38**), proving any composite solution is odd, squarefree, and has at least 7 prime factors.
- **1944** — The problem circulates in number-theoretic folklore as a test case for primality criteria; related totient-divisibility questions are discussed by Schuh and others.
- **1970s** — Analytic and computational refinements show that solutions $n \le x$ are extremely sparse and push the minimum number of prime factors upward.
- **1977** — E. Lieuwens proves that if $3 \mid n$ then $\omega(n) \ge 212$ and $n > 5.5 \times 10^{570}$, dramatically tightening the constraints in that case.
- **1980** — M. Kishore, and independently G. L. Cohen and P. Hagis, refine the general lower bounds; Cohen and Hagis establish $\omega(n) \ge 14$ and $n > 10^{20}$.
- **1988** — C. Pomerance bounds the *counting function*, showing the number of Lehmer numbers up to $x$ is at most $x^{1/2 + o(1)}$ via a counting argument on the prime factors.
- **2007–2008** — W. Banks, A. Güloğlu, C. W. Nevans, F. Luca and collaborators study Lehmer's relation restricted to special sets (Fibonacci numbers, repunits, shifted primes), proving finiteness or non-existence in those families.
- **2011** — F. Luca and C. Pomerance, "On composite integers $n$ for which $\varphi(n) \mid n-1$," sharpen the upper bound on the counting function to roughly $x^{1/2}/(\log x)^{1/2 + o(1)}$.
- **2010s** — Continued sharpening of the lower bound to $\omega(n) \ge 15$ and the size bound well beyond $10^{30}$, via combined computational sieving and analytic arguments.
- **Present** — The problem remains open. No composite solution is known, none has been excluded in general, and the strongest results remain lower bounds on $\omega(n)$ and on $n$, together with sub-$\sqrt{x}$ counting bounds.

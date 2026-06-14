# Status & Frontier — Lehmer's Totient Problem

**Status: open.** No composite integer $n$ with $\varphi(n) \mid n-1$ is known, and none has been proven to exist or to be impossible. The conjecture — that no such $n$ exists, i.e. that the relation $\varphi(n) \mid n-1$ characterizes the primes — is the expected answer but remains unproved after nearly a century.

## What is known (unconditional)

Any composite solution $n$ must be:

- **odd** and **squarefree** (Lehmer, 1932);
- a product of at least **$\omega(n) \ge 15$** distinct primes, with the certified floor raised over time from Lehmer's $7$ through Cohen–Hagis/Kishore's $14$;
- **enormous**: $n > 10^{30}$ in general, and dramatically larger under side conditions — if $3 \mid n$ then $\omega(n) \ge 212$ and $n > 5.5 \times 10^{570}$ (Lieuwens);
- a **Carmichael number**, since $\varphi(n) \mid n-1$ implies the weaker $\lambda(n) \mid n-1$ (Korselt's criterion). No tabulated Carmichael number — and these have been enumerated past $10^{18}$ — satisfies the stronger totient condition.

On the density side, the counting function $L(x) = \#\{n \le x : n \text{ composite}, \varphi(n)\mid n-1\}$ satisfies
$$ L(x) \le x^{1/2}/(\log x)^{1/2 + o(1)} $$
(Luca–Pomerance, 2011, sharpening Pomerance's earlier $x^{1/2+o(1)}$). So solutions, if any, are at most as common as $\sqrt{x}$ — vanishingly sparse.

## What is known (conditional / family-restricted)

Within structured sets — Fibonacci and Lucas sequences, repunits, and various linear-recurrence families — there are **no** Lehmer numbers (Banks, Luca, and collaborators, 2007–2008). Heuristic models (treating the relevant prime-residue events as quasi-independent) predict that the expected number of Lehmer numbers is zero, strongly supporting the conjecture, though such arguments are non-rigorous.

## What a full resolution would require

A proof of non-existence must do something no current method can: rule out solutions for **all** $\omega(n)$ simultaneously. The two main lines each hit a wall.

- The **lower-bound method** raises $\omega(n) \ge k$ one increment at a time and cannot reach $k = \infty$.
- The **sieve/counting method** is blocked by the **parity (square-root) barrier**: sieves cannot reach $L(x) = 0$, only $L(x) = O(x^{1/2})$.

Plausibly, resolution would come from either (i) a genuinely new algebraic obstruction forcing a contradiction from $\varphi(n) \mid n-1$ for squarefree $n$ with many prime factors, independent of $\omega(n)$; or (ii) breakthroughs in the distribution of primes in residue classes (stronger than GRH-type inputs currently available) that defeat the parity barrier for this specific multiplicative condition. A *counterexample*, conversely, would require exhibiting (or proving the existence of) an astronomically large squarefree product of $\ge 15$ primes meeting the divisibility — for which no construction or existence heuristic is known.

## Related problems

- [Carmichael / Mersenne primes infinitude](../mersenne-primes-infinitude/README.md) — Lehmer's Lucas–Lehmer test and the same computational tradition.
- [Odd Perfect Numbers](../odd-perfect-numbers/README.md) — a sibling divisibility problem ($\sigma(n) = 2n$) attacked by identical "lower bound on $\omega(n)$ plus enormous size bound" technology.
- [Erdős–Straus Conjecture](../erdos-straus-conjecture/README.md) — another elementary-looking multiplicative/Diophantine question resisting elementary methods.
- [Riemann Hypothesis](../riemann-hypothesis/README.md) — the distribution-of-primes input whose strengthenings bear on parity-barrier obstructions.
- [Twin Prime Conjecture](../twin-prime-conjecture/README.md) — a flagship instance of the sieve parity barrier that also blocks progress here.

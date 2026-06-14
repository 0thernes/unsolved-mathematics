# Status & Frontier — Existence of Odd Perfect Numbers

**Status: open.** No odd perfect number (OPN) is known, none has been proved impossible, and the consensus expectation is that none exists. The problem is unconditional — there is no reduction to a deeper open conjecture (it does not, for instance, hinge on the Riemann Hypothesis) — yet it has resisted every method for over two millennia.

## What is known (unconditional)

For a hypothetical OPN $n = p^\alpha m^2$ with $p \equiv \alpha \equiv 1 \pmod 4$ (Euler), the strongest established constraints are:

- **Magnitude:** $n > 10^{1500}$ (Ochem–Rao, 2012).
- **Distinct prime factors:** $\omega(n) \ge 10$; and $\ge 12$ if $3 \nmid n$ (Nielsen, 2015).
- **Largest prime factor:** $> 10^8$ (Goto–Ohno, 2008).
- **Second-largest prime factor:** $> 10^4$ (Iannucci, 1999); **third-largest:** $> 100$ (Iannucci, 2000).
- **Largest prime-power component:** $> 10^{62}$ (Ochem–Rao, 2012).
- **Total prime factors with multiplicity:** $\Omega(n) \ge 101$ (Ochem–Rao direction).
- **Congruence shape:** $n \equiv 1 \pmod{12}$ or $n \equiv 117 \pmod{468}$ or $n \equiv 81 \pmod{324}$ (Roberts and related); $n$ is not a perfect square (Euler).

These conditions are mutually consistent: no two of them collide, which is exactly why the problem stays open.

## Conditional results

Several results assume auxiliary hypotheses. Under the **Dris conjecture** ($p^\alpha < m$, equivalently the special prime power is the smaller part), various sharper bounds on $\sigma$-quantities follow. Under assumptions bounding $\omega(n)$, the problem becomes a finite (if astronomically large) computation. There is no conditional *resolution* — no respected conditional proof of non-existence exists.

## What a full resolution would require

A proof of non-existence must produce a *global* contradiction from the local data, and this is precisely the missing ingredient. The constraints above are all "the number must be large / have many factors / avoid certain residues," none of which can self-terminate: $\omega(n)$, $n$, and the special prime $p$ all lack any proven upper bound, so size-based and counting arguments cannot close. A successful attack would likely need one of:

1. an **upper bound** on $\omega(n)$ or on $p$ (turning the problem finite), for which no mechanism is known;
2. a genuine **algebraic obstruction** — a parity-, 2-adic-, or transcendence-type barrier in the system of cyclotomic/Diophantine equations $\sigma(p^a) = \prod \Phi_d(p)$ that forces $\sigma(n)=2n$ to be unsolvable in odd integers;
3. a structural theorem from the **spoof** program explaining why every odd solution requires a non-prime factor (as Descartes' $22021 = 19^2\cdot 61$).

An existence proof, conversely, would require exhibiting an OPN exceeding $10^{1500}$ with $\ge 10$ prime factors — overwhelmingly believed not to exist.

## Plausible routes

The most active near-term routes are (a) pushing $\omega(n) \ge 11$ and beyond via refined Diophantine case analysis (Nielsen school), (b) extending magnitude bounds with verified factor-chain computation (Ochem–Rao school), and (c) the spoof/Descartes-number finiteness program, which is the only line that probes *why* no genuine OPN appears rather than merely how large one would be. None is expected to settle the question soon; the honest assessment is that a fundamentally new idea is required.

## Related problems

- [Infinitude of Mersenne Primes](../mersenne-primes-infinitude/README.md) — even perfect numbers correspond exactly to Mersenne primes via Euclid–Euler; the sibling existence question on the even side.
- [Lehmer's Totient Problem](../lehmer-totient-problem/README.md) — a structurally similar "does any $n$ satisfy this arithmetic-function divisibility?" question for $\varphi(n) \mid n-1$, also widely believed to have no solutions.
- [Riemann Hypothesis](../riemann-hypothesis/README.md) — governs the distribution of primes underlying $\sigma$ and the abundancy heuristics, though OPN non-existence is not known to depend on it.
- [Goldbach Conjecture](../goldbach-conjecture/README.md) — a sibling ancient, elementary-to-state additive/multiplicative problem about integers with massive computational verification but no proof.

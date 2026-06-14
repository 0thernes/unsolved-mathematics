# Attempts — Existence of Odd Perfect Numbers

The OPN problem has produced no accepted proof in either direction, but a long sequence of celebrated partial results, near-misses, and a recurring genre of flawed "elementary" disproofs.

## Famous partial results

- **Euler's reduction (1747).** Any OPN has the form $p^\alpha m^2$ with $p \equiv \alpha \equiv 1 \pmod 4$. This remains the structural foundation of every later attempt.
- **Sylvester's "web" (1888).** J. J. Sylvester proved an OPN must have several distinct prime factors and famously argued that the accumulation of conditions made existence "well-nigh impossible" — a sentiment, not a proof. He showed $\omega(n) \ge 5$ (and that $3,5,7$ cannot all be absent in certain configurations).
- **Hagis (1973) / Nielsen (2015).** The distinct-prime-factor count climbed from Sylvester's handful to $\ge 8$ (Hagis), $\ge 9$ (Nielsen 2007), and finally $\ge 10$ (Nielsen 2015), the current record.
- **Brent–Cohen–te Riele (1991); Ochem–Rao (2012).** Successive computational lower bounds: $n > 10^{300}$, then $n > 10^{1500}$.
- **Goto–Ohno (2008).** Largest prime factor exceeds $10^8$.

These results are universally accepted and tightly cross-checked, but none yields a contradiction.

## Near-misses

- **Descartes number (1638).** $D = 3^2 \cdot 7^2 \cdot 11^2 \cdot 13^2 \cdot 22021$ would be an OPN *if* $22021$ were prime; in fact $22021 = 19^2 \cdot 61$. It is the canonical "spoof" perfect number and the closest historical near-miss.
- **Spoof perfect numbers.** Treating a composite factor as if prime yields odd solutions of $\sigma(n)=2n$. Their existence shows the equation is "barely" unsatisfiable over genuine primes — a tantalizing structural hint studied by Banks et al. and Nielsen et al.

## Disputed and retracted claims

Because the problem is famous and elementary to state, it attracts purported elementary disproofs; **none has survived expert scrutiny.**

- A number of arXiv preprints over the years have claimed to prove no OPN exists by elementary congruence or inequality arguments. The recurring objection from the community is that these arguments silently assume a bound on $\omega(n)$ or the size of the special prime, or misuse the multiplicativity of $\sigma$ across the Euler factor — gaps that void the conclusion. As of this writing no such claim is accepted.
- Conversely, no credible claim of an explicit OPN has been made; the computational lower bound $n > 10^{1500}$ would immediately refute any small candidate.
- **Carmichael–Kanold lineage.** Early 20th-century bounds (Carmichael 1911–1913) were later sharpened and in places corrected by Kanold (1940s–1950s), who supplied rigorous proofs where heuristic claims had circulated; this is a correction within the literature rather than a disputed disproof.

The honest status: a mountain of necessary conditions, several deep partial theorems, one famous spoof, and a steady stream of erroneous elementary "solutions" — but no resolution.

(Word count ≈ 470.)

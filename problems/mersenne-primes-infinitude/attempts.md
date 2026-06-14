# Attempts — Infinitude of Mersenne Primes

Because no credible strategy for proving infinitude exists, the "attempts" in this problem's history are not failed proofs of infinitude but rather (i) corrections and verifications of Mersenne's original claim, (ii) celebrated individual discoveries, and (iii) refinements of the surrounding heuristics and sub-conjectures. We record the most notable, and flag the few amateur claims of a general proof, which are not taken seriously by the community.

## Correcting Mersenne's list — the foundational "attempts"

Mersenne's 1644 claim was effectively a conjecture about a finite range, and its verification consumed nearly three centuries:

- **Euler (1750/1772)** confirmed $M_{31}$ prime, the hardest case then reachable.
- **Pervushin (1883)** found $M_{61}$ prime — an exponent Mersenne had *omitted*, the first proven gap.
- **Cole (1903)** factored $M_{67}$, famously delivering his "lecture without words" to the American Mathematical Society: he computed $2^{67}-1$ on one side of the board and $193{,}707{,}721 \times 761{,}838{,}257{,}287$ on the other, sat down, and received an ovation. This refuted Mersenne's inclusion of $67$.
- **Powers (1911, 1914)** found $M_{89}$ and $M_{107}$ prime, two more omissions; **Lehmer/Kraitchik (1922, 1927)** showed $M_{257}$ composite, removing Mersenne's largest claimed exponent.

By 1947 the full range $p \le 257$ was settled: Mersenne's list had **five errors** (wrongly including $67$ and $257$, wrongly excluding $61$, $89$, $107$). The episode is the classic cautionary tale about unverified numerical conjectures.

## Near-misses and the heuristic frontier

The most consequential "near-miss" is not a near-proof but the **Lenstra–Pomerance–Wagstaff heuristic** and its sharper cousins. The original **Mersenne conjecture** (a guessed pattern of which exponents yield primes) failed once enough data accumulated; Bateman, Selfridge and Wagstaff (1989) replaced it with the **New Mersenne Conjecture**, asserting that for any odd $p$, *any two* of the three statements — $p \equiv \pm 1 \pmod 8$; $2^p-1$ prime; $(2^p+1)/3$ prime — imply the third. This holds for all tested $p$ but is unproven and, crucially, says nothing about infinitude. These are honest conjectural refinements, not attempts at the main theorem.

A genuinely related *unconditional* milestone is **Hooley's 1967 theorem** that Artin's primitive-root conjecture holds under the Generalized Riemann Hypothesis. Since Mersenne primality is entwined with the order of $2$ modulo primes, this delineates how even the conditional toolkit stops short of the Mersenne question.

## Disputed and erroneous claims

- **Mersenne's own list (1644)** is the original disputed claim: stated without proof and later shown to contain five errors. The dispute is purely historical and fully resolved.
- **"Repunit"-style and elementary infinitude proofs.** Over the years amateurs have circulated short "proofs" that infinitely many $M_p$ are prime, typically by misapplying the fact that $2^a - 1 \mid 2^{ab}-1$ (which only constrains *composite* exponents and says nothing about primality of $M_p$), or by assuming a probabilistic heuristic is a theorem. No such argument has survived scrutiny; none has appeared in a refereed venue with a valid proof. The community's neutral objection is uniform: distinguishing primes from almost-primes in an exponentially sparse sequence runs into the sieve **parity barrier**, and no proposed elementary argument addresses it.
- **Premature primality announcements.** Several historical reports of a "new largest Mersenne prime" were later retracted as computational errors (notably some early hand- and machine-era claims), and GIMPS itself has caught hardware-induced false positives, which is why modern discoveries are independently re-verified (e.g. on different hardware and software) before announcement. These are data-integrity disputes, not disputed theorems.

In short: every *verified* result is an existence statement about a particular prime or a correction to Mersenne's table; the general theorem has attracted no serious, surviving proof attempt, reflecting the consensus that the problem is presently intractable.

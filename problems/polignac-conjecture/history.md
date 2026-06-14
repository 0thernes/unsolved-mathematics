# History — Polignac's Conjecture

_Origin, formulation, and timeline._

Polignac's conjecture sits at the heart of the modern theory of gaps between consecutive primes. In its general form it asserts: for every even integer $k$, there exist infinitely many pairs of consecutive primes $(p_n, p_{n+1})$ with $p_{n+1} - p_n = k$. The case $k = 2$ is the celebrated Twin Prime Conjecture; $k = 4$ gives infinitely many "cousin primes," $k = 6$ the "sexy primes," and so on. The conjecture is most often stated for *gaps* between consecutive primes, but a weaker companion form asks only for infinitely many prime pairs $p$, $p+k$ (allowing primes in between). The two coincide asymptotically for the purpose of Polignac's claim, and most literature treats them interchangeably.

The problem arose during a period when the distribution of primes was a central preoccupation but the analytic tools to study it were rudimentary. In 1849 the French mathematician Alphonse de Polignac, then a young polytechnician, communicated a memoir to the Académie des Sciences (published in the *Comptes Rendus*) conjecturing that every even number is the difference of two consecutive primes in infinitely many ways. He reached it empirically, tabulating gaps and observing that each even value seemed to recur without end. Polignac's note also contained a separate, flawed numerical claim—that every odd number is the sum of a prime and a power of two—which was quickly disproved (e.g. $127$, $149$, $251$ are counterexamples). The prime-gap conjecture, however, survived and carries his name.

The conjecture resisted all attempts at a theorem for over a century, because no method could even guarantee *bounded* gaps occurring infinitely often. The quantitative refinement came with Hardy and Littlewood's 1923 $k$-tuple conjecture, which predicts the asymptotic density of prime pairs $p$, $p+k$ via a singular series, making Polignac's conjecture a corollary of a far stronger heuristic. Sieve theory—Brun from 1915, Selberg in the 1940s—produced sharp *upper* bounds on twin-prime counts but, owing to the "parity barrier," could not produce *lower* bounds. The decisive twentieth-century advances were Chen Jingrun's 1973 theorem (infinitely many primes $p$ with $p+2$ prime or semiprime) and the 2005 GPY method of Goldston, Pintz and Yıldırım, which proved gaps can be arbitrarily small relative to the average. The dam broke in 2013, when Yitang Zhang proved an unconditional finite bound on gaps occurring infinitely often—settling a qualitative form of Polignac's conjecture for *some* even $k$—after which Polymath8, Maynard and Tao drove the bound sharply down.

## Timeline

- **1849** — Alphonse de Polignac states the conjecture in the *Comptes Rendus*: every even number is the difference of two consecutive primes infinitely often.
- **1896** — Hadamard and de la Vallée Poussin independently prove the Prime Number Theorem, fixing the average gap near $p_n$ at $\log p_n$.
- **1915** — Viggo Brun introduces his sieve and proves $\sum 1/p$ over twin primes converges (Brun's constant), the first analytic foothold.
- **1923** — Hardy and Littlewood publish the $k$-tuple conjecture, giving a precise conjectural density for prime pairs of every even gap.
- **1940s** — Atle Selberg develops the Selberg sieve, sharpening twin-prime upper bounds.
- **1965** — Bombieri and A. I. Vinogradov prove the large-sieve mean-value theorem giving "GRH on average" (Bombieri–Vinogradov), a key input for later work.
- **1973** — Chen Jingrun proves infinitely many primes $p$ with $p+2$ prime or semiprime—still the strongest result toward $k=2$.
- **2005** — Goldston, Pintz and Yıldırım (GPY) prove $\liminf_n (p_{n+1}-p_n)/\log p_n = 0$.
- **2013** — Yitang Zhang proves $\liminf_n (p_{n+1}-p_n) < 7 \times 10^7$: bounded gaps occur infinitely often.
- **2013** — The Polymath8a collaboration sharpens Zhang's bound to 4680.
- **2013–2014** — James Maynard and, independently, Terence Tao introduce a multidimensional sieve, reaching 600 and proving bounded gaps among any number of primes.
- **2014** — Polymath8b drives the bound to 246, the current unconditional record; under Elliott–Halberstam it falls to 6.
- **Present** — The bound of 246 means *some* even $k \le 246$ is a gap infinitely often, but no single specific value—including $k=2$—is yet known.

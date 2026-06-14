# Attempts — The Twin Prime Conjecture

_Notable attempts, near-misses, retracted proofs._

## Famous partial results (genuine near-misses)

**Brun's theorem (1919).** Viggo Brun's proof that $\sum 1/p$ over twin primes converges was the first hard quantitative fact about twins. It does not decide infinitude, but it shows that even if infinite, twins are vanishingly sparse — and it introduced the sieve that powered everything afterward. The numerical value $B_2 \approx 1.90216$ (Brun's constant) is itself only known approximately, since it depends on data about twins one cannot fully enumerate.

**Chen's theorem (1973).** Chen Jingrun's proof that infinitely many primes $p$ have $p+2$ equal to a prime or a product of two primes is the closest *structural* approximation to the conjecture: replace "prime" by "almost-prime with $\le 2$ factors." It is widely regarded as the natural ceiling of classical sieve methods, blocked from the conjecture itself only by the parity barrier.

**GPY (2005) and bounded gaps (2013–2014).** The Goldston–Pintz–Yıldırım result $\liminf (p_{n+1}-p_n)/\ln p_n = 0$ was hailed as a breakthrough after decades of incremental progress; it reduced bounded gaps to a distribution hypothesis. Yitang Zhang's 2013 paper *Bounded gaps between primes* then produced the first finite bound ($7\times 10^7$) — a result so unexpected from a then little-known mathematician that it became one of the most celebrated stories in modern mathematics. Maynard's and Tao's multidimensional sieve and the Polymath8 collaboration rapidly improved the bound to **246**.

## Pell-equation, computational, and elementary attempts

A recurring genre of attempted "proofs" reduces twin primes to Diophantine or modular conditions (e.g. characterizations via $n^2-1$ being a product of two primes, or via Wilson-theorem congruences). Such reformulations are correct as *restatements* but provide no new leverage on infinitude; they are not counted among serious attacks. Likewise, large-scale computation has verified enormous twin pairs (record twins now exceed $300{,}000$ decimal digits) and tested the Hardy–Littlewood density to high accuracy, but no amount of computation can settle an infinitude statement.

## Disputed and unverified claimed proofs

The twin prime conjecture, like the Riemann hypothesis and Goldbach's conjecture, attracts a steady stream of claimed elementary proofs, almost all from outside the research mainstream and almost all flawed. A few points of neutral record:

- **Recurrent preprint claims.** Numerous purported proofs appear on arXiv, viXra, and personal pages each year. As of this writing none has been accepted by the research community or published in a peer-reviewed venue of standing. The common failure modes are (i) tacit assumption of independence of the events "$n$ prime" and "$n+2$ prime," which is exactly what must be proved; (ii) misuse of sieve bounds as if they gave lower bounds for primes (forbidden by the parity barrier); and (iii) heuristic density arguments dressed as rigorous lower bounds. The neutral statement is that such claims fail to overcome the parity obstruction or do not control sieve error terms, and the community does not regard the conjecture as proved.

- **No retracted *accepted* proof.** Unlike some problems, the twin prime conjecture has no famous published-then-withdrawn proof by a leading figure. The honest status is that there is no claimed proof — credentialed or otherwise — that has survived scrutiny.

A useful litmus test, due to folklore in the field: any claimed elementary proof of the twin prime conjecture should explain why the **same argument** does not also (falsely or unexpectedly) settle the parity problem or prove statements known to require deep input. Most disputed claims fail this test immediately. The conjecture remains open; the strongest rigorous results are Chen's $P_2$ theorem and the gap bound $\le 246$.

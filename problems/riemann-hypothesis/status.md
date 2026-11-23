# Status & Frontier — The Riemann Hypothesis

_Where the problem stands and what a resolution would require._

**Status: open.** No proof or disproof is accepted by the mathematical community. RH is one of the seven Clay Millennium Prize Problems and the only one of Hilbert's 1900 list (problem 8) that remains squarely open and central.

## What is known (unconditional)

- **Zeros on the line are abundant.** Infinitely many non-trivial zeros lie exactly on $\Re(s)=\tfrac12$ (Hardy, 1914), and a positive proportion do—currently more than $40\%$ (Levinson 1974; Conrey 1989, with later refinements above $41\%$). No proof reaches $100\%$, and none excludes off-line zeros.
- **Zero-free regions.** $\zeta(s)\ne0$ for $\Re(s)=1$ (the PNT) and in the Vinogradov–Korobov region $\sigma>1-c/((\log t)^{2/3}(\log\log t)^{1/3})$. No zero-free region of the form $\sigma>1-\delta$ for fixed $\delta>0$ is known—that gap is exactly the difficulty.
- **Zero-density estimates** bound how many zeros could lie off the line at a given height, constraining—but not eliminating—exceptions. In a landmark May 2024 breakthrough (*Annals of Mathematics*, `arXiv:2405.20552`, verified), **Larry Guth and James Maynard** gave the first structural improvement in 84 years to Ingham's 1940 zero-density estimate at $\sigma = 3/4$, proving $N(\sigma, T) \le T^{30(1-\sigma)/13 + o(1)}$ and improving primes in short intervals to $x^{17/30 + o(1)}$.
- **Computation.** All zeros up to very large heights have been checked to lie on the line: more than $10^{13}$ low-lying zeros, and individual zeros near the $10^{22}$nd verified (Odlyzko; Gourdon–Demichel). Platt, Trudgian and others maintain rigorous, certified verifications. Computation cannot prove RH but has never produced a counterexample.
- **de Bruijn–Newman constant.** $0\le\Lambda\le0.22$ (lower bound: Rodgers–Tao 2020; upper bound: Polymath15 2019). RH is equivalent to $\Lambda\le0$, so the truth, if RH holds, sits exactly at the boundary $\Lambda=0$.

## November 2026 frontier watch (claimed Lean-only proof — pending community audit)

- On November 20, 2026, Levent Alpöge (Anthropic) released a ~17-million-line Lean 4 formal archive, developed with heavy assistance from Claude, claiming a proof of the **Generalized Riemann Hypothesis** (and therefore RH). Independent kernel checkers and the Lean FRO/Mathlib Initiative reported clean formal compilation under Lean's logic.
- However, as Terence Tao and working analysts emphasized immediately after release, machine kernel compilation alone does not establish mathematical consensus for an undigested 17M-line formalization: human conceptual verification and statement-fidelity auditing (ruling out any representational mismatch between the formalized statement and the canonical analytic definition) remain ongoing. Per this atlas's cardinal honesty policy, RH remains recorded as **`open`** until independent mathematical verification and consensus are established.

## What is known (conditional)

Assuming RH (or GRH), an enormous body of consequences follows: the sharp error term $\pi(x)=\operatorname{li}(x)+O(\sqrt{x}\log x)$, strong bounds on $M(x)=\sum\mu(n)$, effective bounds in many $L$-function problems, the deterministic primality and gap results conditional on GRH, and much of the quantitative theory of primes in arithmetic progressions. This dense web of consequences is itself strong circumstantial evidence and a powerful incentive.

## What a full resolution would require

A proof must establish that *no* zero lies in the open strip $0<\Re(s)<\tfrac12$ (equivalently, by the functional equation, in $\tfrac12<\Re(s)<1$). The recognized routes each demand a missing ingredient: (i) a Hilbert–Pólya self-adjoint operator with spectrum equal to the zeros, with self-adjointness proved; (ii) the positivity in Weil's explicit formula or Connes's trace formula, established unconditionally; (iii) an arithmetic-geometry framework over $\mathbb{Q}$ (or $\mathbb{F}_1$) mirroring Deligne's finite-field proof, including a positive-definite cohomological pairing; or (iv) a genuinely new analytic input that converts positive-proportion/zero-density control into the exclusion of all off-line zeros. The random-matrix correspondence (GUE statistics) is the most suggestive structural clue but is not itself a proof strategy. Most experts regard RH as true and believe its proof will require a fundamentally new idea rather than refinement of existing methods.

## Related problems

- [Generalized framework — pair correlation](../montgomery-pair-correlation/README.md)
- [Birch and Swinnerton-Dyer Conjecture](../birch-swinnerton-dyer/README.md)
- [Twin Prime Conjecture](../twin-prime-conjecture/README.md)
- [Goldbach's Conjecture](../goldbach-conjecture/README.md)
- [Hardy–Littlewood k-tuple Conjecture](../hardy-littlewood-k-tuple/README.md)

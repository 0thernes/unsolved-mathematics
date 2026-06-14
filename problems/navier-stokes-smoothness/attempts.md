# Attempts — Navier–Stokes Existence and Smoothness

_Notable attempts, near-misses, retracted proofs._

The Navier–Stokes regularity problem attracts claimed proofs with unusual regularity, and a Millennium Prize problem of this profile draws many. The professional record contains a small number of genuine near-misses and a steady stream of claimed full solutions, almost all withdrawn or refuted. The items below are stated neutrally with the technical objection that the community raised.

**Penny Smith (2006).** Smith, a respected mathematician at Lehigh, posted a paper ("Immortal smooth solution of the three space dimensional Navier–Stokes system") claiming global regularity. She withdrew it within weeks after Cheng Yeop Yeo and others identified a counterexample to an auxiliary lemma (a maximum-principle-type estimate) on which the argument depended. The withdrawal was prompt and uncontested; the episode is often cited as an example of the community's rapid self-correction.

**Mukhtarbay Otelbaev (2014).** Otelbaev, a senior Kazakh mathematician, published a claimed proof of global solvability in a Kazakh journal. It received wide attention. Within months specialists, including Terence Tao on MathOverflow, observed that the argument, if correct, would also apply to scenarios known to blow up — i.e. it appeared to prove too much, conflicting with the supercriticality barrier — and a concrete gap was located. The claim is not accepted.

**Other claimed proofs.** Numerous arXiv preprints assert resolution (in either direction). None has survived expert scrutiny. A recurring failure mode is precisely the one Tao's 2014 averaged-equation construction predicts: arguments that use only the energy inequality and scaling, which cannot succeed because they would also "prove" regularity for systems that demonstrably blow up.

Among **legitimate near-misses and partial triumphs**:

- **Leray (1934)** himself could not close the gap he opened; his weak solutions remain non-unique in the largest classes (Buckmaster–Vicol, 2019).
- **Caffarelli–Kohn–Nirenberg (1982)** is the closest unconditional approach: it confines any singular set to parabolic Hausdorff dimension $\le 1$ but cannot remove it. Shrinking this dimension below $1$ has resisted decades of effort.
- **Escauriaza–Seregin–Šverák (2001)** closed the critical $L^3_x$ endpoint of the Serrin criteria — a genuine and celebrated advance — but conditional criteria assume the very critical control that is unavailable unconditionally.
- **Koch–Tataru (2001)** reached the optimal small-data space $BMO^{-1}$; **Bourgain–Pavlović (2008)** then showed the program cannot be pushed to $\dot B^{-1}_{\infty,\infty}$, marking a hard boundary.
- **Buckmaster–Vicol (2019)** and the broader convex-integration program produced non-uniqueness of weak solutions — a structural near-miss that constrains *which* solution concept any proof must use, without resolving the Leray–Hopf regularity question.
- **Hou–Luo (2014)** found compelling numerical evidence of finite-time blow-up for *axisymmetric Euler* near a boundary, energizing rigorous blow-up programs (e.g. Elgindi's 2021 $C^{1,\alpha}$ Euler blow-up); these results concern Euler or modified models, not viscous Navier–Stokes.

The net state: real progress has been incremental and one-sided (sharper conditional criteria, finer partial regularity, decisive negative/barrier results), while every claimed *complete* resolution of the 3D viscous problem has, so far, been retracted or refuted.

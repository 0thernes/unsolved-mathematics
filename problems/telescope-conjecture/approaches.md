# Approaches — The Telescope Conjecture (Disproved 2023)

_Major strategies, partial results, and barriers._

The telescope conjecture asks whether $L_n^f X \to L_{K(n)} X$ is an equivalence, equivalently whether $T(n)$ and $K(n)$ are Bousfield-equivalent for $n \ge 2$. The lines of attack split into (i) direct computation of $v_n$-periodic homotopy, (ii) algebraic models of the two localizations, (iii) categorical/Bousfield-lattice structure, and (iv) the trace-methods route that ultimately settled it. Below, "best result" means the strongest verified statement along that line; "barrier" the obstruction that blocked or redirected it.

## Direct computation of $v_n$-periodic homotopy

**Core idea.** Pick a type-$n$ finite complex $F$, a $v_n$-self map $v$, and compute $v^{-1}\pi_* F$ (the telescope homotopy) versus its $K(n)$-local approximation $\pi_* L_{K(n)} F$ via the $E(n)$- or $E_n$-based Adams spectral sequence. Equality at all $F$ is the conjecture.

**Best result.** At $n=0$ (rational) and $n=1$ the computation is complete and the conjecture **holds**: at height 1 the telescope is controlled by the image of the $J$-homomorphism (Mahowald, Miller). At $n=2, p \ge 5$, partial computations (Mahowald–Ravenel–Shick) produced detailed pictures of the $v_2$-periodic homotopy of Smith–Toda complexes.

**Barrier.** The telescope is an infinite colimit; its homotopy can contain "extra" elements with no $K(n)$-local shadow, and the relevant Adams spectral sequences have unbounded $E_2$-pages and intricate differentials. Computation alone could neither confirm nor refute the conjecture — the suspected discrepancy classes lived beyond the range of any finite calculation.

## Algebraic / Bousfield-lattice approach

**Core idea.** Compare the localizing subcategories $\langle T(n)\rangle$ and $\langle K(n)\rangle$ inside the Bousfield lattice of the $p$-local stable category. The conjecture is the assertion that these two acyclicity classes coincide; the smashing localization $L_n^f$ should equal $L_n$.

**Best result.** General structure theory (Hovey, Palmieri, Ravenel) clarified that $\langle T(n)\rangle \le \langle K(n)\rangle$ always, so the only question is the reverse containment, and that a failure would manifest as a *strictly larger* telescopic acyclicity class. This pinned the problem precisely.

**Barrier.** The Bousfield lattice is enormous and poorly understood at $n \ge 2$; abstract lattice arguments gave no purchase on whether the inequality is strict.

## Algebraic models of the localizations

**Core idea.** Model $L_{K(n)}$ by the **Morava stabilizer group** acting on Lubin–Tate space ($K(n)$-local category $\simeq$ continuous representations of $\mathbb{G}_n$), and seek a parallel algebraic model for $L_n^f$. If both are algebraic in the same way, the comparison map is an equivalence.

**Best result.** The $K(n)$-local side is beautifully algebraic (Goerss–Hopkins–Miller, Devinatz–Hopkins). At low heights/large primes the telescopic side was *suspected* to be more than algebraic.

**Barrier.** No comparably rigid algebraic model for the telescope existed, precisely because (as we now know) it carries genuinely extra, non-algebraic information.

## Trace methods and algebraic $K$-theory (the decisive route)

**Core idea.** The cyclotomic trace $K \to \mathrm{TC}$ and the **redshift philosophy** (Ausoni–Rognes) predict that algebraic $K$-theory raises chromatic height by one. Computing $\mathrm{TC}$ and $K$-theory of height-$n$ ring spectra gives access to $v_{n+1}$-periodic and telescopic phenomena that the $K(n+1)$-local approximation cannot see. The strategy: exhibit a ring spectrum whose telescopic $K$-theory provably outstrips its $K(n)$-localization.

**Best result — the disproof.** **Burklund–Hahn–Levy–Schlank (2023)** combined the **Lichtenbaum–Quillen property** for truncated Brown–Peterson spectra ($\mathrm{BP}\langle n\rangle$, due to Hahn–Wilson), the **chromatic Nullstellensatz** (Burklund–Schlank–Yuan), and **redshift** (Hahn–Raksit–Wilson and others) to show the comparison map $L_n^f \to L_{K(n)}$ is **not** an equivalence for any $n \ge 2$ and any prime. Telescopic homotopy is strictly larger, and grows without bound.

**Barrier (now historical).** The route required the entire post-2018 trace-methods apparatus — Lichtenbaum–Quillen bounds, even filtration / motivic filtrations on $\mathrm{TC}$, and the Nullstellensatz — none of which existed when the conjecture was posed. This explains why four decades of direct computation could neither prove nor disprove it: the discrepancy is real but only visible through $K$-theory ascending one height.

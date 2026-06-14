# Approaches — The Catalan–Dickson Conjecture (Aliquot Sequences)

_Major strategies, partial results, and barriers._

The conjecture is a statement about the long-term dynamics of iterating $s(n)=\sigma(n)-n$. No approach has come close to a proof in either direction; the work divides into computational extension, the drivers/guides heuristic, statistical theory of $s$, and structural results on the image and fibers of $s$.

## Direct computation and the open low-index sequences

**Core idea.** Extend each undetermined sequence term by term, factoring every value, until it terminates, cycles, or visibly stabilizes its behavior. A single value's fate is decidable in finite time *if* the sequence happens to terminate or cycle; the obstruction is that an unbounded sequence can never be certified unbounded by extension alone.

**Best result reached.** The "Lehmer five" ($276, 552, 564, 660, 966$) are the smallest open starters and have been pushed enormously — $276$ past two thousand terms with index size beyond $200$ digits — by Lehmer, Guy, Selfridge, te Riele, Creyaufmüller, Zimmermann, and the FactorDB/aliquot community. All sequences with starting value below $1000$ except the Lehmer five are resolved; open starters are catalogued well into the tens of thousands.

**Barrier.** Computation is *asymmetric*: it can prove boundedness for any individual terminating sequence but can never prove divergence, and each step requires factoring a large integer (the "stubborn cofactor" problem). Growth of term size makes the program unbounded in cost; it informs intuition but cannot settle the conjecture.

## Drivers, guides, and the Guy–Selfridge heuristic

**Core idea.** Guy and Selfridge (1975) observed that the parity and small-prime structure of a term largely controls whether $s$ increases or decreases. A **driver** is a divisor $d \mid n$ (e.g. $2 \cdot 3$, or $2^k \cdot$ a related odd part such as $2^3\cdot 3\cdot 5$, $2^4\cdot 31$, etc.) that tends to persist across iterations and force $s(n) > n$; a **guide** is a weaker, less persistent analogue. Even numbers carrying a strong driver are expected to grow until the driver breaks, at which point the sequence may "escape." The heuristic predicts unbounded sequences, contradicting Catalan–Dickson.

**Best result reached.** The driver/guide framework quantitatively explains observed up-and-down patterns and predicts which sequences are "stuck" in growth. It is the source of the counter-conjecture and matches computation strikingly well.

**Barrier.** It is a *heuristic*, not a theorem. There is no proof that a driver persists forever, nor that the expected upward drift is never overcome by rare downward excursions. The probabilistic model treats successive terms as quasi-independent, which is not rigorous; correlations could in principle conspire to keep every sequence bounded.

## Statistical theory of $s$ (density and average order)

**Core idea.** Study the distribution of $s(n)/n$ and the densities of numbers that increase or decrease under one step. Erdős initiated the rigorous study of the iterated $\sigma$/$s$ behavior; Bosma and Kane (and later Bosma's large computations) determined the *average value* of $\log(s(n)/n)$ and the proportion of $n$ for which $s(n) > n$, giving precise figures for the "first step" of the dynamics.

**Best result reached.** It is known unconditionally that the abundant numbers (where $s(n)>n$) have a positive density (about $0.2476$), and the average of $s(n)/n$ over even $n$ exceeds $1$, lending rigorous support to the *plausibility* of divergence. Erdős proved that for almost all $n$ with $s(n)=m$, the value $m$ inherits constrained statistics — results about the *image* of $s$.

**Barrier.** These are one-step or short-horizon statements. The conjecture is about the *infinite* iterate, and no statistical result controls the full orbit; a positive growth rate on average does not preclude every individual orbit eventually descending.

## Structure of the image and fibers of $s$ (untouchable numbers)

**Core idea.** Understand which integers lie in the range of $s$ and how many preimages they have. Numbers *not* in the range are **untouchable** (e.g. $2, 5, 52, 88, \dots$); their density bears on whether sequences can collapse. Pomerance, Pollack, and collaborators proved that untouchable numbers have positive lower density and that the number of solutions of $s(n)=m$ obeys sharp average bounds.

**Best result reached.** Strong unconditional theorems on the size of fibers $s^{-1}(m)$ and on the density of untouchables, plus refined estimates for amicable-pair counts. These constrain the "phase space" of the dynamics.

**Barrier.** Structure of a single application of $s$ does not transfer to the iterate. The fiber and image results are deep but tangential to the global boundedness question, which would require controlling arbitrarily long backward and forward orbits simultaneously.

## Why the problem resists

The unifying obstruction is the **non-self-averaging, deterministic-but-erratic** nature of the iteration: $s$ is neither monotone nor contractive, its behavior is governed by factorizations that are themselves hard, and there is no known Lyapunov function (a quantity provably monotone along every orbit) that would force boundedness or unboundedness. Until such an invariant — or a rigorous probabilistic model with controlled dependence — is found, neither Catalan–Dickson nor Guy–Selfridge appears attackable.

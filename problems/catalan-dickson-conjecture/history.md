# History — The Catalan–Dickson Conjecture (Aliquot Sequences)

_Origin, formulation, and timeline._

## The object of study

For a positive integer $n$, let $s(n) = \sigma(n) - n$ be the **sum of proper divisors** (the *aliquot sum*), where $\sigma$ is the sum-of-divisors function. The **aliquot sequence** starting at $n$ is the orbit $n,\ s(n),\ s(s(n)),\dots$ obtained by iterating $s$. Three behaviors are classical: the sequence may reach $1$ (its predecessor being a prime) and terminate; it may enter a cycle — a fixed point (a *perfect number*, $s(n)=n$), a $2$-cycle (*amicable numbers*), or a longer *sociable* cycle; or it may, in principle, increase without bound. The conjecture concerns whether the third possibility ever occurs.

## Precise formulation and reformulations

The **Catalan–Dickson conjecture** asserts that *every aliquot sequence is bounded*, hence — since each term lies in a finite range and the dynamics are deterministic — eventually periodic (terminating at $1$ or entering a sociable cycle). Catalan's original 1888 wording was stronger and quickly seen to be too restrictive: he suggested every sequence terminates at $1$ or at a perfect number. Dickson (1913) corrected this to allow termination in any cycle, giving the modern statement. The standing **counter-conjecture of Guy and Selfridge (1975)** holds the opposite: a positive proportion of starting values — in particular many even numbers — produce *unbounded* sequences. The two conjectures cannot both be true, and the empirical evidence has long been read as favoring Guy–Selfridge, though neither is proved.

## Timeline

**1888** — Eugène Catalan, in a note associated with the *Bulletin de la Société Mathématique de France*, proposes that iterating the aliquot sum always leads to $1$ or a perfect number.

**1913** — Leonard Eugene Dickson, in his memoir on amicable and related numbers, refines Catalan's claim to its correct form: every aliquot sequence is bounded and ends in a cycle. This becomes the **Catalan–Dickson conjecture**.

**1929** — Poulet exhibits long sociable cycles (including a period-$28$ chain beginning at $14{,}316$), showing the cyclic endpoints are richer than perfect or amicable numbers alone.

**1965** — Digital computations by Lehmer and collaborators push small starting values far, isolating the "Lehmer five" — $276, 552, 564, 660, 966$ — as the smallest values whose fate is undetermined.

**1975** — Richard Guy and John Selfridge publish *"What drives an aliquot sequence?"*, articulating a divergence heuristic via the *guide* and *driver* concepts and conjecturing that many sequences are unbounded — directly opposing Catalan–Dickson.

**1976** — Guy, Selfridge, and te Riele extend computations; the open starters below $1000$ remain exactly the Lehmer five.

**1990s** — Improved factoring (continued-fraction, quadratic-sieve, and later number-field-sieve methods) lets researchers extend $276$ and its companions to hundreds of terms with large composite "stubborn" cofactors.

**1998–present** — Wolfgang Creyaufmüller, Paul Zimmermann, and the community-run *aliquot* effort (FactorDB and the "Aliquot Sequences" pages) systematically extend all open sequences below high bounds, tracking driver/guide transitions.

**2000s** — Bosma and Kane, and later Bosma, give density and average-order results for $s$, quantifying how often a sequence increases versus decreases at a step and refining the divergence heuristic.

**2010s–2020s** — Pomerance, Pollack, and collaborators prove structural theorems on the *image* and *fibers* of $s$ (on numbers in the range of $s$ and on "untouchable" numbers absent from the range). All five Lehmer sequences remain open; $276$ has been extended past two thousand terms with index size exceeding $200$ digits, with no sign of bounding or termination.

**Present frontier** — No aliquot sequence has been *proved* to diverge, and none of the open low-index sequences has been resolved. The conjecture is settled neither way; computation continues to favor divergence (Guy–Selfridge) without supplying a proof, while the unconditional theory of $s$ has advanced markedly.

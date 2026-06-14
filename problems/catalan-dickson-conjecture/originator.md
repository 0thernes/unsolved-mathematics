# Originator(s) — The Catalan–Dickson Conjecture (Aliquot Sequences)

_Biography, background, and the ideas that led here._

The conjecture carries two names because it was posed in stages: a bold historical root by **Eugène Catalan** and the corrected modern formulation by **Leonard Eugene Dickson**. A third pairing — **Richard Guy** and **John Selfridge** — supplies the influential counter-conjecture that animates the modern subject, and is treated where their ideas appear, but the *bounding* conjecture itself is Catalan's and Dickson's.

## Eugène Charles Catalan (1814–1894)

Catalan was a French and Belgian mathematician, born in Bruges and active for most of his career in Liège, where he held a chair from 1865. A student in Paris in the circle of Liouville, he is remembered across several fields: the **Catalan numbers** of enumerative combinatorics, the **Catalan conjecture** on consecutive perfect powers ($8$ and $9$; proved by Mihăilescu in 2002), the Catalan surface in geometry, and the constant $G = 1 - 1/9 + 1/25 - \cdots$ that bears his name. His mathematical temperament was that of a problem-poser with a strong arithmetical streak, comfortable issuing sharp conjectures about integers.

His remark on aliquot sequences fits that pattern. Iterating the proper-divisor sum was already a venerable game — perfect, amicable, and sociable numbers are exactly its fixed points and cycles, studied since antiquity and revived by Euler. Catalan's contribution (1888) was to assert a *global* dynamical claim: that the iteration always settles, and specifically into $1$ or a perfect number. The motivation was the natural expectation that, "on average," dividing-and-summing should not grow a number — most $n$ have $s(n) < n$ (so-called *deficient* numbers dominate). His error was to underestimate the abundant numbers, where $s(n) > n$, and the way a sequence can be repeatedly pushed upward.

## Leonard Eugene Dickson (1874–1954)

Dickson was an American number theorist and algebraist, the first PhD in mathematics from the University of Chicago, and one of the founders of the American research school. He is best known for his monumental three-volume *History of the Theory of Numbers* (1919–1923), a comprehensive survey that itself shaped the field, and for foundational work on finite fields, linear groups, and the arithmetic of quadratic forms. His scholarship gave him unmatched command of the classical literature on perfect, amicable, and aliquot numbers.

It was precisely this command that let Dickson (1913) correct Catalan. Sociable cycles of length greater than two were already implicit in the literature, and Dickson's reformulation — every aliquot sequence is *bounded* and ends in *some* cycle, not necessarily $1$ or a perfect number — is the statement that has stood ever since. Dickson treated the question as part of the broader theory of $s$ and its iterates, situating it among amicable-number problems rather than as an isolated curiosity.

## The modern counterpoint

The *bounding* claim is Catalan's and Dickson's; the prevailing modern expectation is the opposite. **Richard K. Guy** (1916–2020), the British-Canadian number theorist and master expositor of unsolved problems, and **John L. Selfridge** (1927–2010), the American computational number theorist, argued in 1975 that drivers and guides can sustain indefinite growth, so that many even sequences should diverge. Their *"What drives an aliquot sequence?"* reframed the problem dynamically and predicted that Catalan–Dickson is *false*.

## Legacy

The dual legacy is characteristic of the subject: a clean, plausible-sounding conjecture (Catalan–Dickson) that careful theory and computation have come to doubt, opposed by a heuristic counter-conjecture (Guy–Selfridge) that nobody can prove either. The problem endures as a showcase of how iterated arithmetic functions resist closure, and as a long-running testbed for computational number theory, integer factorization, and the statistical study of $\sigma$ and $s$.

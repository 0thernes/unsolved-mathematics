# Originator(s) — Existence of Odd Perfect Numbers

The problem has no single author; it descends from the Greek arithmetical tradition. Metadata names two figures — **Euclid** and **Nicomachus of Gerasa** — who together gave perfect numbers their definition and their first theory, thereby implicitly posing the parity question.

## Euclid (fl. c. 300 BCE)

Euclid of Alexandria is the towering figure of ancient mathematics, author of the *Elements*, the most influential textbook in history. Little is known of his life; he worked in Alexandria under the early Ptolemaic dynasty and organized the accumulated geometry and number theory of his predecessors into a rigorous deductive system built from definitions, postulates, and proved propositions.

Perfect numbers appear in the arithmetical Books VII–IX, which treat the theory of integers, divisibility, primes, and proportion geometrically (numbers as lengths). The capstone is **Proposition IX.36**: *if as many numbers as we please beginning from a unit be set out continuously in double proportion until the sum of all becomes prime, and if the sum multiplied into the last make some number, the product will be perfect.* In modern terms, if $1 + 2 + \cdots + 2^{k-1} = 2^k - 1$ is prime, then $2^{k-1}(2^k-1)$ is perfect. Euclid's motivation was the internal architecture of arithmetic — perfection is a divisor-theoretic analogue of the "complete" figures he prized. His construction is constructive and one-directional: it produces even perfect numbers and is silent about whether others (odd ones) might exist. That silence is the seed of the OPN problem.

## Nicomachus of Gerasa (c. 60 – c. 120 CE)

Nicomachus was a Neopythagorean mathematician and philosopher from Gerasa (modern Jerash, Jordan). Unlike Euclid he wrote discursively rather than deductively; his *Introduction to Arithmetic* (*Arithmetike eisagoge*) became the standard arithmetic primer of late antiquity and the Middle Ages, transmitted through Boethius's Latin adaptation. His outlook was Pythagorean and mystical: numbers carried moral and cosmological meaning, and the "perfect" numbers — neither deficient nor abundant — held a place of special dignity, likened to virtue lying between excess and defect.

Nicomachus catalogued the first four perfect numbers $6, 28, 496, 8128$ and asserted several regularities: that perfect numbers are produced by Euclid's rule, that they alternate in ending between 6 and 8, and that there is exactly one in each "rank" of magnitude (one below 10, one below 100, one below 1000, and so on). These claims were stated as confident generalizations, not theorems; several (the strict alternation, the one-per-decade rule) are in fact false. But by treating perfectness as a fully understood phenomenon generated entirely by Euclid's even construction, Nicomachus crystallized the implicit conjecture that **all** perfect numbers are even. He thus frames the question even while presuming its answer.

## From historical root to modern problem

The decisive reformulation came two millennia later. **Euler** (1747) proved the converse of Euclid — every even perfect number is of Euclid's form — closing the even case, and derived the constraint that any odd perfect number must factor as $p^{\alpha} m^2$ with $p \equiv \alpha \equiv 1 \pmod 4$. This is the bridge between the ancient definition and the modern research problem. Where Euclid and Nicomachus left an unexamined gap, Euler made the OPN question precise and structural; everything since has elaborated his form.

## Legacy

Euclid's number theory founded the discipline; the perfect-number propositions anchor the study of $\sigma(n)$ and Mersenne primes to this day. Nicomachus shaped how perfect numbers were understood — and misunderstood — for over a thousand years. Together they bequeathed a problem that has resisted every generation since: simple to state, ancient in pedigree, and still unsolved.

(Word count ≈ 600.)

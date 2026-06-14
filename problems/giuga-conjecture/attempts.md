# Attempts — Giuga's Conjecture

_Notable attempts, near-misses, retracted proofs._

## Giuga's own bounds (1950)

Giuga's founding paper did not stop at the statement: it supplied the reduction to the squarefree divisibility condition and used it to verify, by structural argument rather than brute force, that **no counterexample is smaller than $10^{1000}$**. This is best read as a near-miss of a different kind — a demonstration that the conjecture is "true so far" at a scale that already exceeds anything a counterexample could plausibly reach by accident. It established the template every later attempt follows.

## Bedocchi's sharpening (1985)

E. Bedocchi revisited the conjecture and tightened the constraints on hypothetical counterexamples, improving both the minimal number of prime factors and the size bound. Bedocchi's analysis is the bridge between Giuga's original hand-arguments and the systematic 1996 treatment; it is frequently cited as the source of the "counterexample must be enormous" intuition that motivated the later computations.

## Borwein–Borwein–Borwein–Girgensohn (1996)

The most influential modern contribution. D. Borwein, J. M. Borwein, P. B. Borwein, and R. Girgensohn proved:

- the **equivalence** of Giuga's congruence with Agoh's Bernoulli-number criterion $nB_{n-1}\equiv-1\pmod n$;
- that any counterexample must have **at least 13 distinct prime factors** and exceed $10^{1700}$;
- a clean theory of **Giuga numbers** and **Giuga sequences**, separating the multiplicative half of the condition from the primality half.

This is a partial result, not a proof: it bounds and reorganizes the problem without resolving the converse. Its lasting effect was to make precise *why* the conjecture is hard — a counterexample must satisfy two rare conditions simultaneously.

## Giuga numbers as near-misses

The genuine "near-misses" are the **Giuga numbers** themselves: composite $n$ satisfying $\sum_{p\mid n}1/p-\prod_{p\mid n}1/p\in\mathbb Z$. The smallest, $30=2\cdot 3\cdot 5$, and its successors ($858,\,1722,\,66198,\dots$) satisfy *one* of the two conditions a counterexample needs. They are the closest known objects to a violation of Giuga's conjecture, yet every one of them fails the Carmichael/Fermat condition and so is **not** a counterexample. Their existence is a standing reminder that the relaxed problem is satisfiable while the full one resists.

## Status of claimed proofs

There is **no widely accepted proof** of Giuga's conjecture, and no famous retracted-and-disputed "proof" of the kind that has attended some better-known problems. The literature is characterized instead by accumulating *partial* results — larger lower bounds, structural reductions, and equivalences — rather than by contested resolution claims. Occasional elementary "proof" notes circulate informally (e.g., on preprint repositories and discussion forums), but none has survived expert scrutiny or appeared in a refereed venue as a complete proof. Readers should treat any announcement of a full proof with appropriate skepticism: as of the present, the converse direction remains unestablished and the problem is open.

## Generalizations and offshoots

Grau, Oller-Marcén, and collaborators (from around 2009) studied generalized Giuga numbers and the density/finiteness of the relaxed objects, producing infinite families of Giuga *sequences* and partial results on Giuga *numbers*. These are legitimate advances on the combinatorial relaxation but do not bear directly on the primality converse, which is the actual open conjecture.

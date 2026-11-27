# Attempts — Cramér's Conjecture on Prime Gaps

_Notable attempts, near-misses, retracted proofs._

- **Granville's Constant Revision (1995).** Although often framed as an "attack" on Cramér's 1936 paper, Granville's refinement targets the sharp constant $\limsup = 1$, arguing that the true $\limsup$ is $\ge 2e^{-\gamma} \approx 1.1229$ (while preserving the quadratic order $O((\log p_n)^2)$). Notice that the formal Lean target `CramerConjecture.cramer_conjecture` encodes the $O((\log p_n)^2)$ formulation (or explicit constant form) — readers should always distinguish the order-of-magnitude conjecture from the exact-constant $\limsup = 1$ version.
- **Elementary Sieve Attempts.** Numerous elementary attempts to derive $g_n \ll (\log p_n)^2$ directly from Jacobsthal's function $j(n)$ confuse the sieve bound on coprime gaps to $P_k\#$ with actual prime gaps; even Iwaniec's bound $j(n) \ll (\log n)^2$ only addresses integers coprime to a *fixed* primorial, not primality itself.

# 📖 Glossary

Recurring concepts that thread through many dossiers in the atlas. Definitions
are deliberately compact and aimed at an advanced-undergraduate / early-graduate
reader; each points at the problems where the idea is load-bearing.

## Number theory & L-functions

- **Riemann zeta function $\zeta(s)$** — $\sum_{n\ge 1} n^{-s}$ for $\Re(s)>1$,
  analytically continued to $\mathbb{C}\setminus\{1\}$. Its non-trivial zeros
  encode the distribution of primes. *(Riemann Hypothesis, Montgomery pair correlation.)*
- **L-function** — a Dirichlet series with an Euler product and (conjecturally) a
  functional equation; a vast generalization of $\zeta$. Central objects of the
  Langlands program. *(RH, BSD, Hardy–Littlewood.)*
- **Sieve theory** — methods for counting integers surviving divisibility
  constraints (Eratosthenes–Legendre, Brun, Selberg, large sieve, GPY).
  *(Goldbach, Twin Primes, Polignac.)*
- **Parity barrier** — a structural obstruction: classical sieves cannot
  distinguish numbers with an even vs. odd number of prime factors, so they
  cannot alone produce primes. *(Twin Primes, Goldbach.)*
- **Admissible tuple** — a set of integer offsets hitting no complete residue
  system mod any prime; conjecturally infinitely often all-prime. *(Hardy–Littlewood k-tuple.)*
- **Radical $\mathrm{rad}(n)$** — the product of the distinct primes dividing
  $n$. *(abc conjecture, Beal.)*
- **Elliptic curve** — a smooth projective genus-1 curve with a rational point;
  its rational points form a finitely generated abelian group (Mordell–Weil).
  *(BSD.)*
- **Rank (of an elliptic curve)** — the number of independent infinite-order
  rational points; conjecturally equals the analytic order of vanishing of the
  curve's L-function at $s=1$. *(BSD.)*
- **Totient $\varphi(n)$** — the count of integers in $[1,n]$ coprime to $n$.
  *(Lehmer's totient problem.)*
- **Perfect number** — equal to the sum of its proper divisors; equivalently
  $\sigma(n)=2n$. *(Odd perfect numbers.)*

## Analysis, PDE & geometry

- **Hausdorff / Minkowski dimension** — notions of fractional dimension of a set;
  Kakeya asks whether direction-rich sets must be full-dimensional. *(Kakeya.)*
- **Restriction / Kakeya / Bochner–Riesel circle of conjectures** — a web of
  harmonic-analysis problems linking Fourier restriction to dimension of Kakeya
  sets. *(Kakeya.)*
- **Weak / mild solution** — a solution satisfying a PDE in an integrated sense;
  global existence is known weakly for Navier–Stokes (Leray), smoothness is not.
  *(Navier–Stokes.)*
- **Regularity** — whether solutions stay smooth or can blow up in finite time.
  *(Navier–Stokes, Yang–Mills.)*
- **Mass gap** — a strictly positive lower bound on the energy of excitations
  above the vacuum in a quantum field theory. *(Yang–Mills.)*
- **Limit cycle** — an isolated periodic orbit of a planar vector field;
  bounding their number for polynomial fields is Hilbert's 16th. *(Hilbert 16th.)*
- **Numerical range $W(A)$** — the set $\{\langle Ax,x\rangle : \|x\|=1\}$ of a
  matrix/operator; a convex region controlling functional calculus.
  *(Crouzeix's conjecture.)*
- **Invariant subspace** — a closed subspace mapped into itself by an operator;
  existence of a non-trivial one on separable Hilbert space is open.
  *(Invariant subspace problem.)*

## Algebra, combinatorics & logic

- **Hodge class** — a rational cohomology class of type $(p,p)$; the Hodge
  conjecture asks whether all such are algebraic. *(Hodge.)*
- **Algebraic cycle** — a formal combination of subvarieties; its cohomology
  class is always Hodge. *(Hodge.)*
- **Graph minor** — a graph obtained by deleting and contracting edges;
  Hadwiger relates chromatic number to forbidden complete minors. *(Hadwiger.)*
- **Chromatic number** — the fewest colors for a proper coloring; for the plane
  (unit-distance graph) it is known only to be 5, 6, or 7. *(Hadwiger–Nelson.)*
- **NP / NP-complete** — problems verifiable (resp. hardest) in nondeterministic
  polynomial time; $P\ne NP$ would separate solving from checking. *(P vs NP.)*
- **Relativization, natural proofs, algebrization** — three formal *barriers*
  showing why broad classes of techniques cannot resolve $P$ vs $NP$. *(P vs NP.)*
- **Transcendence degree** — the size of a maximal algebraically independent
  subset of a field extension; Schanuel bounds it for exponentials. *(Schanuel.)*
- **Union-closed family** — a finite family of sets closed under union; Frankl
  conjectures some element lies in $\ge$ half the sets. *(Union-closed sets.)*
- **Balanced presentation** — a group presentation with equally many generators
  and relators; Andrews–Curtis concerns trivializing those of the trivial group.
  *(Andrews–Curtis.)*
- **II$_1$ factor / hyperfinite factor $R$** — von Neumann algebras with a unique
  trace; the Connes embedding problem (now resolved negatively) asked if all
  embed into an ultrapower of $R$. *(Connes embedding.)*

## Diophantine approximation & dynamics

- **$\|x\|$ (distance to nearest integer)** — the basic quantity in
  approximation; Littlewood asks $\liminf n\|n\alpha\|\|n\beta\| = 0$.
  *(Littlewood conjecture.)*
- **Homogeneous dynamics** — flows on $\mathrm{SL}_n(\mathbb{R})/\mathrm{SL}_n(\mathbb{Z})$;
  measure-rigidity (Ratner, EKL) attacks Diophantine problems. *(Littlewood.)*
- **Arithmetic dynamics** — iteration of arithmetic maps; the Collatz map
  $n\mapsto n/2$ or $3n+1$ is the canonical open case. *(Collatz.)*

## Provenance terms (atlas-specific)

- **CSS (Composite Severity Score)** — the atlas's reproducible ranking number;
  see [methodology](methodology/RANKING.md).
- **Verification flag** — provenance label on every citation: `verified`,
  `high-confidence`, `needs-verification`, `ai-suggested`; see
  [sourcing](methodology/SOURCING.md).

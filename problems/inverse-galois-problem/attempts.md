# Attempts — The Inverse Galois Problem

_Notable attempts, near-misses, retracted proofs._

## Shafarevich's solvable theorem and its $2$-adic correction

Igor Shafarevich's **1954** proof that every finite solvable group is realizable over $\mathbb{Q}$ is the single largest positive result. It is not a retraction but a famous near-miss in rigor: the original argument contained an error in its treatment of embedding problems at the prime $2$ (the handling of extensions involving $2$-power order). The gap was identified and repaired in the subsequent literature—through corrected treatments by Shafarevich himself and a complete account given in monographs such as Neukirch–Schmidt–Wingberg's *Cohomology of Number Fields*. The theorem now stands, but it is frequently cited as a cautionary example of how delicate $2$-extensions are.

## The Monster and the sporadic groups

Thompson's **1984** realization of the Monster $\mathbb{M}$ over $\mathbb{Q}$ via a rigid rational triple was a spectacular success and a proof of concept for rigidity: the largest sporadic simple group fell before far smaller groups. In the wake of rigidity, the program to realize all $26$ sporadic groups was carried out group by group through the 1980s and 1990s (Matzat, Malle, Pahlings, Hunt, and others). The persistent **near-miss is the Mathieu group $M_{23}$**: as of the standard references it remains the only sporadic simple group not known to be a Galois group over $\mathbb{Q}$, because it admits no usable rigid or rationally rigid tuple. This single group is the most-cited concrete obstruction in the subject.

## The Noether-program failures

Emmy Noether's rationality strategy looked, for decades, like a possible uniform route. **Swan (1969)** showed the invariant field for the cyclic group $C_{47}$ is *not* purely transcendental over $\mathbb{Q}$, with related counterexamples by Voskresenskii. Later, **Saltman (1984)** and **Bogomolov (1987)** exhibited $p$-groups whose unramified Brauer group is nonzero, so the Noether problem fails even over algebraically closed base fields. These are not failed proofs of the IGP but decisive demonstrations that one popular approach cannot work in general; importantly, $C_{47}$ *is* realizable (it is abelian), so failure of rationality does not contradict realizability.

## Claimed or premature general resolutions

The Inverse Galois Problem has attracted occasional sweeping claims, but—unlike some other famous open problems—it has **no widely circulated, seriously-considered claimed proof of the full statement** that the community has had to adjudicate. The status is honest incremental progress, not a contested "almost-proof." Some specific subcases have seen competing or initially incomplete arguments later tightened (e.g., particular non-solvable groups whose first realizations required braid-orbit computations subsequently rechecked by computer algebra). Where individual realizations rest on machine computation of Hurwitz components or character tables, the literature treats them as verified once independently reproduced; readers consulting primary sources for a specific group should confirm the realization in Malle–Matzat or Serre's *Topics in Galois Theory* rather than rely on announcements.

## Generic-polynomial near-completeness in low degree

A constructive thread (Jensen–Ledet–Yui and predecessors) produced explicit generic polynomials realizing all groups of small order and many transitive groups of low degree. This is a genuine partial resolution in the strongest form (generic, hence parametrizing every realization), but it stalls precisely where rationality fails, leaving the general case untouched.

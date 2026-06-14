# Attempts — P versus NP

_Notable attempts, near-misses, retracted proofs._

$\mathrm{P}$ vs. $\mathrm{NP}$ attracts an unusually large volume of claimed solutions—Gerhard Woeginger's long-running "P-versus-NP page" catalogued well over a hundred claimed proofs in both directions, the overwhelming majority flawed. The serious history is better told through *partial results* that genuinely advanced understanding, and through the small number of high-profile claims that drew sustained expert scrutiny.

## Genuine partial results and near-misses

- **Restricted circuit lower bounds.** Razborov's superpolynomial monotone lower bound for clique (1985) felt, briefly, like a path to the summit—until Razborov himself showed that monotone techniques cannot extend to general circuits (the clique problem is monotone, but the method exploits monotonicity essentially). The $\mathrm{AC}^0$ parity lower bounds (Furst–Saxe–Sipser, Ajtai, Håstad) and the $\mathrm{AC}^0[p]$ bounds (Razborov, Smolensky) are landmark unconditional separations in restricted models, but the natural-proofs barrier explains their inability to scale.
- **Williams's $\mathrm{NEXP} \not\subseteq \mathrm{ACC}^0$ (2011).** A rare non-natural lower bound, obtained by combining a faster-than-trivial $\mathrm{ACC}^0$ satisfiability algorithm with a hardness-from-algorithms paradigm. It is a real separation, but $\mathrm{NEXP}$ is far above $\mathrm{NP}$ and $\mathrm{ACC}^0$ far below $\mathrm{P}$.
- **Mulmuley's lower bound in a restricted model (1999)** ("lower bounds in a parallel model without bit operations") was an unconditional separation that motivated the GCT program, though it sidesteps the full model.

## Disputed and retracted claims

- **Vinay Deolalikar (2010).** A researcher at HP Labs circulated a roughly 100-page manuscript claiming $\mathrm{P} \neq \mathrm{NP}$, using a blend of finite model theory and statistical-physics arguments about the solution-space geometry of random $k\text{-}\mathrm{SAT}$. The claim received extraordinary, largely public scrutiny (a massively collaborative effort by Terence Tao, Scott Aaronson, Russell Impagliazzo, Neil Immerman, and others on blogs and a wiki). Within weeks the community identified fundamental gaps: the proof's notion of "polylog parametrizability" failed to distinguish $\mathrm{P}$ from problems that *are* in $\mathrm{P}$ (e.g., the argument would equally "exclude" $\mathrm{XOR}$-$\mathrm{SAT}$, which is polynomial-time solvable), and the finite-model-theory and physics components did not connect rigorously. Immerman pinpointed errors in the logical core. The proof is regarded as refuted; Deolalikar never published a corrected version in a peer-reviewed venue. The episode is notable as a model of rapid, transparent, collegial error-finding rather than a scandal.
- **Recurrent $\mathrm{P} = \mathrm{NP}$ claims.** Numerous purported polynomial-time algorithms for $\mathrm{SAT}$, the traveling salesman problem, or graph isomorphism-style problems appear regularly; none has survived scrutiny. A common failure mode is a linear or semidefinite-programming relaxation that the author believes is exact but which has an integrality gap, or an algorithm whose claimed runtime hides exponential blowup.

## The cautionary meta-result

The three barrier theorems—relativization (Baker–Gill–Solovay 1975), natural proofs (Razborov–Rudich 1994), and algebrization (Aaronson–Wigderson 2008)—are themselves "anti-attempt" results: they prove that broad families of techniques cannot succeed. Any credible future proof must be checked against all three. This is why experts greet new claims with structured skepticism rather than reflexive dismissal: a valid argument must be non-relativizing, non-naturalizing, and non-algebrizing simultaneously, and almost all attempted proofs fail at least one of these tests by construction.

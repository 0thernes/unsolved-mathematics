# Approaches — P versus NP

_Major strategies, partial results, and barriers._

Proving $\mathrm{P} \neq \mathrm{NP}$ requires a *lower bound*: a demonstration that some explicit $\mathrm{NP}$ problem cannot be solved by any polynomial-time algorithm. Proving $\mathrm{P} = \mathrm{NP}$ requires the opposite—a single efficient algorithm for an $\mathrm{NP}$-complete problem. Decades of effort have produced not a resolution but a precise map of why the standard techniques fail. That map—the three "barrier" results—shapes every serious program.

## Boolean circuit lower bounds

The dominant attack tries to show that $\mathrm{NP}$-complete functions require superpolynomial-size circuits, which would give $\mathrm{NP} \not\subseteq \mathrm{P}/\mathrm{poly}$ and hence $\mathrm{P} \neq \mathrm{NP}$. The early triumphs were in *restricted* circuit models. Furst–Saxe–Sipser and Ajtai (1983) proved that constant-depth ($\mathrm{AC}^0$) circuits cannot compute parity; Håstad's switching lemma (1986) made this tight. Razborov (1985) proved a superpolynomial lower bound for *monotone* circuits computing $k$-clique, and Razborov–Alon–Boppana extended it to exponential. Razborov and Smolensky handled $\mathrm{AC}^0[p]$ circuits with prime modular gates. **Barrier:** these methods stall at general circuits. Razborov and Rudich (1994) explained why with the **natural proofs** obstruction—most known lower-bound arguments are "natural" (constructive and large), and any natural proof against general circuits would break the pseudorandom generators whose existence cryptography presumes. Thus a successful circuit lower bound must be *unnatural*. Williams's 2011 separation $\mathrm{NEXP} \not\subseteq \mathrm{ACC}^0$ is a celebrated example of a non-natural technique, but it remains far from $\mathrm{P}$ vs. $\mathrm{NP}$.

## Diagonalization and relativization

Diagonalization—the engine behind the undecidability and time-hierarchy theorems—was the first thing tried. **Barrier:** Baker, Gill, and Solovay (1975) proved that there exist oracles $A, B$ with $\mathrm{P}^A = \mathrm{NP}^A$ and $\mathrm{P}^B \neq \mathrm{NP}^B$. Since diagonalization arguments relativize (remain valid relative to any oracle), no such argument can resolve $\mathrm{P}$ vs. $\mathrm{NP}$. Any proof must be *non-relativizing*, exploiting the internal structure of computation rather than treating machines as black boxes.

## Algebraic and arithmetic methods; the algebrization barrier

Interactive-proof results such as $\mathrm{IP} = \mathrm{PSPACE}$ (Shamir, 1990) are genuinely non-relativizing, exploiting low-degree polynomial encodings (arithmetization). For a time these raised hopes of breaking the relativization barrier altogether. **Barrier:** Aaronson and Wigderson (2008) defined **algebrization**, a refinement in which the oracle may be queried as a low-degree extension, and showed that arithmetization-based techniques algebrize—and that algebrizing techniques *also* cannot settle $\mathrm{P}$ vs. $\mathrm{NP}$. The three barriers together (relativization, natural proofs, algebrization) carve out the techniques that demonstrably cannot work.

## Geometric Complexity Theory (GCT)

Proposed by Ketan Mulmuley and Milind Sohoni (2001 onward), GCT recasts complexity lower bounds—most directly the algebraic analogue $\mathrm{VP} \neq \mathrm{VNP}$ (the permanent-versus-determinant problem)—as questions in algebraic geometry and representation theory. The strategy seeks geometric *obstructions*: representation-theoretic multiplicities distinguishing the orbit closures of the permanent and determinant. GCT is explicitly designed to evade the natural-proofs barrier by being highly non-constructive. **Status/obstruction:** the program is deep but distant from delivering bounds; a 2016 result of Bürgisser, Ikenmeyer, and Panova showed that the hoped-for "occurrence obstructions" do not by themselves suffice, redirecting the program toward subtler multiplicity obstructions.

## Proof complexity ($\mathrm{NP}$ vs. $\mathrm{coNP}$)

Cook and Reckhow (1979) showed that $\mathrm{NP} = \mathrm{coNP}$ if and only if some propositional proof system admits polynomial-size proofs of all tautologies. Proving superpolynomial lower bounds for ever-stronger proof systems (resolution, cutting planes, Frege) is thus a route toward separating $\mathrm{NP}$ from $\mathrm{coNP}$ (which would imply $\mathrm{P} \neq \mathrm{NP}$). Strong lower bounds are known for weak systems (Haken's 1985 exponential resolution bound for the pigeonhole principle), but Frege and Extended Frege systems remain wide open.

## Algorithmic / upper-bound attacks

A minority pursues $\mathrm{P} = \mathrm{NP}$ by seeking fast algorithms, or pursues *fine-grained* and average-case structure. Practical $\mathrm{SAT}$ solvers solve enormous industrial instances, and exact algorithms beat brute force (e.g., $1.3^n$-time $3\text{-}\mathrm{SAT}$ solvers), but none achieves polynomial time. The **Exponential Time Hypothesis** (Impagliazzo–Paturi) conjectures $3\text{-}\mathrm{SAT}$ requires $2^{\Omega(n)}$ time—a quantitative strengthening of $\mathrm{P} \neq \mathrm{NP}$ now central to fine-grained complexity. Conversely, the existence of any natural $\mathrm{NP}$-complete problem with a sub-exponential algorithm would be a sensation.

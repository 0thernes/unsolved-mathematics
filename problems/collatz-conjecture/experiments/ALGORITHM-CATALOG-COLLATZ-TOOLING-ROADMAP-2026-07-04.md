# Algorithm Catalog -> Collatz Tooling Roadmap

Date: 2026-07-04

Input: attached catalog, "The 1000 Algorithms, Categories, and Domains", catalog version `0.9.13-local`.

Purpose: turn the 1000-item algorithm catalog into a practical Collatz research/QA work plan. This is not a claim that the catalog solves Collatz. It is a way to choose instruments deliberately instead of letting breadth become noise.

## Executive Verdict

The catalog helps as a method-selection index, not as mathematical evidence. Roughly 30-50 entries are directly useful for this repository. Most of the 1000 are irrelevant to Collatz proof work unless they are used as visualization, pedagogy, or generic software infrastructure.

The valuable slice is concentrated in five lanes:

1. Proof formalization and algebra normalization.
2. Counterexample/refutation search.
3. Finite residue/state-space verification.
4. Statistical and large-deviation measurement.
5. Repository QA, provenance, and anti-pseudoproof gates.

The highest-leverage next move is to attach each promising method to one exact Collatz claim class: certificate frontier, spine ladder, regeneration, cycle floor, pseudo-proof quarantine, or artifact reproducibility.

## Tier 0: Do Not Confuse With Progress

These uses are allowed, but they do not advance the conjecture:

- using the catalog as vibes or authority;
- citing algorithm names without encoding a Collatz object;
- adding quantum, crypto, distributed, or generative methods because they sound powerful;
- replacing proof obligations with fitted models;
- using undecidability/Kolmogorov/Busy Beaver language to imply a concrete Collatz result.

Guardrail: every method must answer one of these questions:

- What exact claim does it check?
- What counterexample would falsify the claim?
- What artifact does it produce?
- What proof obligation remains after the artifact?

## Tier 1: Immediate High-Value Methods

| Catalog Method | Collatz Use | Target Artifact | Value | Caveat |
|---|---|---|---|---|
| SMT Solver | Encode bounded affine/parity constraints over bit-vectors and integers. | `experiments/smt_certificate_frontier.py` | Finds finite counterexamples to local lemmas. | Does not prove unbounded claims. |
| SAT / CDCL | Exhaust residue-class predicates at fixed depth. | `experiments/sat_residue_cover.py` | Strong independent check against custom Python DP. | Need proof logs for trust. |
| DRAT/LRAT Proof Checking | Certify SAT unsat claims for finite covers. | `experiments/proofs/*.lrat` | Converts finite "no counterexample" into checkable certificate. | Only finite instances. |
| Model Checking | Treat parity transitions as finite automata at bounded depth. | `experiments/frontier_automaton_check.py` | Good for prefix/lift transition claims. | State explosion. |
| Symbolic Execution | Explore branch conditions of shortcut map macros. | `experiments/symbolic_macro_paths.py` | Finds missing parity cases. | Path explosion. |
| Concolic Testing | Mix symbolic residues with concrete hard starts. | `experiments/concolic_hard_starts.py` | Better adversarial tests than random starts. | Still bounded. |
| Weakest Precondition Calculus | Derive exact preconditions for descent/certificate macros. | `experiments/wp_descent_macros.md` | Turns code-like claims into formulas. | Requires careful integer domains. |
| Abstract Interpretation | Build over-approximate orbit regions with sound widening. | `experiments/abstract_orbit_domains.md` | Could certify families, not just samples. | Coarse domains may be useless. |
| E-Graphs / Equality Saturation | Normalize affine Collatz identities. | `experiments/affine_identity_egraph.py` | Good algebra-mistake detector. | Needs a small trusted rewrite basis. |
| Knuth-Bendix Completion | Complete rewrite rules for affine/spine expressions. | `experiments/rewrite_completion.md` | Helps canonicalize proof text. | Termination/confluence may fail. |
| Congruence Closure | Check equality claims among affine terms. | `experiments/congruence_affine_check.py` | Fast sanity gate for algebraic notes. | Equalities only, not inequalities. |
| Quantifier Elimination | Attack small Presburger fragments of residue claims. | `experiments/presburger_fragments.md` | Can prove bounded linear arithmetic claims. | Collatz has multiplication by powers/branching. |
| Superposition / Resolution | Refute overstrong first-order formulations. | `experiments/fol_claim_refuter.md` | Useful for pseudo-proof QA. | Hard to model number theory fully. |
| Unsat Core Extraction | Explain which assumptions make a finite claim impossible. | `experiments/unsat_core_ledger.md` | Excellent for audits and teaching. | Depends on SAT/SMT encoding quality. |
| Proof by Reflection | Generate small certified checkers for residues. | `formal/residue_reflection.md` | Path to Lean/Coq trust. | Requires formalization effort. |

## Tier 2: Search and Stress Instruments

| Catalog Method | Collatz Use | Best Target | Why It Helps |
|---|---|---|---|
| A* Search | Search hard frontier residues with admissible debt heuristics. | Certificate frontier / retimed pressure. | Focuses compute on plausible hard cases. |
| Monte Carlo Tree Search | Explore parity-prefix trees with rollout scores. | Survivor frontier. | Better than naive beam search for rare regimes. |
| Beam Search | Already aligned with current frontier tooling. | Hard starts. | Keep, but benchmark against MCTS/A*. |
| Simulated Annealing | Optimize starts/residues for long escape depth or high regeneration. | Regeneration search. | Good for rugged residue landscapes. |
| Genetic Algorithm | Evolve parity words or residue representatives. | Rare outlier classes. | Can discover weird examples. |
| CMA-ES / Differential Evolution | Tune continuous proxy parameters for scoring functions. | Potential-function discovery. | Useful for heuristic design only. |
| Ant Colony Optimization | Explore prefix trees with pheromone on hard motifs. | Motif recurrence search. | Good visualization/search hybrid. |
| Reservoir Sampling | Maintain representative hard examples from huge scans. | Results ledgers. | Prevents biased cherry-picking. |
| Locality-Sensitive Hashing / SimHash | Deduplicate similar parity words and proof claims. | Quarantine/claim corpus. | Reduces duplicate pseudo-proof noise. |
| MinHash | Cluster similar documents or parity motifs. | Audit register. | Helps manage massive generated artifacts. |

## Tier 3: Statistical / Probabilistic Instruments

| Catalog Method | Collatz Use | Output |
|---|---|---|
| Kalman / Particle Filters | Track evolving orbit "state" estimates: debt, alignment, regeneration. | Diagnostic, not proof. |
| Belief Propagation | Factor graph model of parity constraints and residue lifts. | Heuristic pressure map. |
| Gaussian Process Regression | Surrogate model for expensive hard-start score functions. | Search prioritization. |
| Hamiltonian Monte Carlo | Sample high-dimensional parameterized families if a smooth proxy exists. | Probably low priority. |
| AMS / Count-Min / HyperLogLog | Streaming counts over huge scans. | Scalable telemetry. |
| Bloom Filters | Avoid rechecking previously seen residues/starts. | Scan acceleration. |
| Large-Deviation / Entropy Framing | Already central to frontier density. | Keep explicit in docs. |

## Tier 4: Formalization Candidates

Formalize in this order:

1. Shortcut map definitions and parity words.
2. Cylinder affine law.
3. Terras parity-word bijection.
4. Descent certificate criterion.
5. No finite 2-adic cover via all-ones path.
6. Spine ladder identity.
7. Positivity localization for supercritical spines.
8. Exact cycle product identity.
9. Continued-fraction crude lower-bound derivation.

Candidate tools from the catalog:

- Calculus of Constructions / Martin-Lof Type Theory: proof assistant foundation.
- Weakest Precondition Calculus: derive proof obligations from executable macros.
- Proof by Reflection: certify residue sweeps.
- Foundational Proof Certificates: attach finite SAT/SMT outcomes.
- Tactic Replay: make generated proofs reproducible.
- Dedukti/LF-style checking: exchange proof objects across systems.

Repo target: add `formal/ROADMAP.md` before adding any proof assistant files. The formal lane must not claim novelty; it is trust infrastructure.

## Tier 5: Pseudo-Proof Defense

The catalog is especially useful for strengthening the anti-pseudoproof layer.

| Failure Class | Useful Methods | Check |
|---|---|---|
| Prompt-as-axiom | Sequent calculus, resolution refutation, proof certificates. | Does the conclusion depend on a user command as premise? |
| Kolmogorov/Berry misuse | Undecidability sanity checks, formal logic review. | Is an existence claim being bounded by document size? |
| Fitted model relabeled theorem | Abstract interpretation, proof obligations, model checking. | Is the model soundly over-approximating true dynamics? |
| Tautological detector | Control systems, sibling dynamics, symbolic execution. | Does the detector also "prove" a false sibling theorem? |
| Algebra drift | E-graphs, congruence closure, rewrite completion. | Do stated recurrences match exact affine update rules? |

Immediate repo enhancement: extend `scripts/proof_claim_sweep.py` with detectors for:

- "therefore Collatz is solved";
- "closed for positives";
- "Kolmogorov complexity implies";
- "the prompt is the proof";
- "empirical contraction proves";
- "finite experiment proves universal".

## Practical 30-Method Shortlist

Use these first:

1. SMT Solver
2. SAT/CDCL
3. DRAT/LRAT checking
4. Model checking
5. Symbolic execution
6. Concolic testing
7. Weakest precondition calculus
8. Abstract interpretation
9. E-graphs / equality saturation
10. Congruence closure
11. Knuth-Bendix completion
12. Unsat core extraction
13. Quantifier elimination for Presburger fragments
14. Proof by reflection
15. Foundational proof certificates
16. Tactic replay
17. A* search
18. Monte Carlo tree search
19. Beam search
20. Simulated annealing
21. Genetic algorithms
22. Reservoir sampling
23. MinHash / SimHash
24. Bloom filters
25. HyperLogLog
26. Belief propagation
27. Gaussian process surrogate modeling
28. Large-deviation/entropy analysis
29. Differential testing against sibling systems
30. Reproducible manifest/checksum generation

## Concrete Next Sprint

### Sprint A: Proof/QA Infrastructure

- Add a `formal/ROADMAP.md` with the nine formalization targets above.
- Add a finite-claim manifest format:

```text
claim_id:
claim_text:
domain: residue | affine | cycle | stochastic | artifact | pseudo-proof
status: proved | checked-finite | refuted | heuristic | open
checker:
command:
counterexample:
remaining_obligation:
```

- Wire `proof_claim_sweep.py` into CI for unhedged victory claims.

### Sprint B: Finite Verification

- Build a SAT/SMT prototype for depth-bounded residue statements.
- Emit unsat certificates where possible.
- Compare against current Python DP and residue labs.

### Sprint C: Search

- Implement a small A*/MCTS comparison against existing beam/frontier examples.
- Score by max prefix debt, regeneration alignment, certificate depth, and retimed-pressure class.
- Keep all outputs under `experiments/results/` with manifest entries.

### Sprint D: Documentation

- Add a "Methods Not Used" section to prevent algorithm-name inflation.
- In the whitepaper, mention the catalog only as a post-hoc tooling roadmap, not as evidence for novelty.

## Success Criteria

The catalog helps if it produces one of these:

- a new finite counterexample to an overstrong local claim;
- a proof certificate for a bounded residue statement;
- a reproducible independent checker for an existing result;
- a smaller formal proof obligation;
- a better hard-example search frontier;
- fewer pseudo-proof artifacts reaching public docs.

It does not help if it only adds names, diagrams, or new speculative documents.

## Bottom Line

This catalog can make the Collatz lab more disciplined and more powerful, but only after aggressive triage. The useful part is not "1000 algorithms"; it is a carefully routed 30-method verification/search stack. Treat it as an instrument panel, not as evidence.

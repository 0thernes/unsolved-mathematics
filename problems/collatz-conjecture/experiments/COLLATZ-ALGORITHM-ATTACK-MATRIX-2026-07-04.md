# Collatz Algorithm Attack Matrix - 2026-07-04

Source catalog: attachment `C:\Users\Alexa\.codex\attachments\6e6a37ba-5a26-44c4-9ae8-df4377988028\pasted-text.txt`, "The 1000 Algorithms, Categories, and Domains", catalog version `0.9.13-local`.

Purpose: convert the broad 1000-entry algorithm catalog into a Collatz-specific routing matrix. This is not a proof program and not a claim of mathematical novelty. It is a triage layer: which algorithmic families can produce proof obligations, refutations, certificates, faster experiments, or better artifact hygiene for the current Collatz repository.

## Executive Verdict

The catalog helps as a battle map, not as a magic key.

Most entries are irrelevant to Collatz proof progress. The useful slice is concentrated in:

- logic, SAT/SMT, proof certificates;
- automata and model checking;
- rewriting and equality saturation;
- abstract interpretation over residue/valuation domains;
- compressed frontier data structures;
- adversarial search and counterexample mining;
- provenance and reproducibility tooling.

The actionable standard is strict: an algorithmic lens is useful only if it creates one of the following:

1. a smaller theorem target;
2. a machine-checkable finite certificate;
3. a counterexample to an overclaim;
4. a faster exact enumeration;
5. a better public artifact trail.

## Current Collatz Bottlenecks To Route Against

| Bottleneck | Meaning in this repo | What would count as progress |
|---|---|---|
| Regeneration | Alignment to negative 2-adic spines can be burned, then later regenerated. | Bound regeneration, or find a sharper invariant that blocks indefinite regeneration for positive integers. |
| Survivor frontier | Prefixes with `3^o >= 2^d` persist indefinitely in 2-adics. | Compress, classify, or prove unavoidable exit motifs for positive finite shadows. |
| Retimed pressure | A child prefix can increase required credit before naive inherited credit accounts for it. | A local lift theorem showing fresh/retimed credit always arrives before deficit. |
| Phase collision | Spine phases collide or separate by odd-unit locks. | Formalize exact phase gates and prove which collisions are harmless. |
| Certificate descent | Every positive integer must eventually drop below itself. | Finite certificates with machine-checkable coverage, or a uniform theorem replacing finite scans. |
| Pseudo-proof containment | AI sessions produce convincing false proofs. | Faster detection, quarantine, and proof-obligation extraction. |
| Public reproducibility | The repository must expose scripts/results/manifests cleanly. | One-command verification, manifests, checksums, and proof logs. |

## Tier A - Directly Actionable

These are the catalog families most worth turning into code or proof notes.

| Catalog anchors | Family | Collatz use | Concrete next move | Success test | Risk |
|---|---|---|---|---|---|
| #46-48, #146-147 | DPLL/CDCL SAT, SMT, AllSAT, MaxSAT | Encode finite lift obligations, forbidden motifs, and branch-prefix pressure constraints. | Build a SAT/SMT encoder for depth `d -> d+1` retimed-pressure cases. | UNSAT certificate for a claimed bad local transition class, or concrete satisfying counterexample. | Easy to overfit finite depths. |
| #178-179 | DRAT/LRAT proof checking | Make finite SAT claims independently checkable. | Export DRAT/LRAT for any UNSAT local-transition result. | A verifier replays the certificate without trusting the search code. | Certificates may become huge. |
| #41 | Abstract interpretation | Prove bounds over whole residue classes instead of sampled starts. | Define an abstract domain over `(phase, residue mod 2^k, excess, credit, v2 alignments)`. | Transfer functions overapproximate exact shortcut steps and prove a nontrivial finite class safe. | Too coarse domains prove nothing; too fine domains become enumeration. |
| #42-43, #181-190 | Model checking, bisimulation, CTL/LTL, Buchi, parity games | Treat survivor prefixes as transition systems/languages. | Build a minimized automaton for survivor-frontier states plus credit states. | Bad infinite behavior becomes emptiness/parity-game query. | Infinite arithmetic may not fit finite automata without lossy abstraction. |
| #44-45, #758 | Knuth-Bendix, e-graphs, term graph rewriting | Normalize affine/parity identities and detect duplicate proof sketches. | Create rewrite rules for affine block composition, rotations, spine fixed points, and valuation identities. | Two independently written lemmas reduce to the same normal form, or an invalid proof exposes an unmatched rewrite step. | Rewriting can hide missing hypotheses. |
| #173-176 | Proof by reflection, certificate translation, tactic replay | Move finite theorem checks toward formal proof artifacts. | Turn small lemmas into reflection-checkable proof scripts or replayable transcripts. | A proof checker validates a finite claim from a generated certificate. | Heavy setup cost. |
| #731-740 | NFA/DFA construction, derivatives, minimization | Represent survivor-prefix and forbidden-motif languages. | Build automata for motif families currently found in branch-prefix experiments. | Automata minimization reveals a small grammar or proves a proposed motif cover incomplete. | Automata describe words, not integer values unless tied to residues. |
| #931-932, #990 | Wavelet tree, succinct bitvector rank/select, combinatorial number system | Scale exact frontier enumeration and compressed residue storage. | Store live survivor sets by combinatorial rank instead of dense integer lists. | Same exact counts with lower memory and faster prefix/rank queries. | Engineering win, not theorem progress by itself. |
| #258-259 | Sumcheck, GKR | Certify large table computations or low-degree encodings of finite checks. | Only consider after SAT/SMT produces stable finite claims. | Third-party verifier checks a large computation faster than recomputing it. | Overkill unless finite claims are very large. |
| #78 | Freivalds matrix check | Probabilistic sanity checks for matrix/table transformations. | Use only for smoke-checking large generated matrices in experiments. | Finds corrupted outputs cheaply. | Probabilistic check cannot support proof claims alone. |
| #800 | Collatz Function Iteration | Keep the problem class explicitly represented. | Use as catalog tag tying all routes back to the actual map. | Prevents algorithm-list drift into unrelated demos. | Merely naming Collatz does not add method. |

## Tier B - Useful For Exploration And Falsification

These help find structure or break bad claims, but should not be framed as proof engines.

| Catalog anchors | Family | Collatz use | Good use | Bad use |
|---|---|---|---|---|
| #21, #27, #70, #501-510, #551-556 | A*, MCTS, alpha-beta, heuristic search, DFPN, retrograde analysis | Search for hard frontier shadows, local transition counterexamples, and candidate theorem shapes. | Counterexample mining and best-first exploration of obstruction classes. | Claiming no counterexample found means theorem proved. |
| #73-76 | Gaussian process, HMC, cluster methods, particle filters | Model empirical tail behavior and prioritize scans. | Choosing which finite regimes to stress next. | Treating posterior confidence as proof. |
| #56-60, #528-529 | Evolutionary/heuristic optimization | Generate adversarial starts or weird residue families. | Stress testing proposed invariants. | Selling heuristic convergence as mathematical convergence. |
| #64 | Belief propagation | Analyze factor-graph encodings of parity/residue constraints. | Suggest decomposition of SAT/SMT encodings. | Assuming independence where Collatz digits are dependent. |
| #77-82, #961-970 | Sketching/streaming summaries | Telemetry over huge scans. | Dashboards, anomaly detection, run summaries. | Replacing exact counts in proof-critical paths. |
| #26, #241-260 | Merkle/proof commitments | Artifact integrity and public reproducibility. | Commit result files, manifests, and script hashes. | Crypto decoration without verification value. |
| #33-35, #110 | Kolmogorov/Chaitin/Solomonoff/Levin | Intellectual caution around description-complexity claims. | Refute pseudo-proofs that confuse surprise/complexity with nonexistence. | Any "repo size bounds counterexamples" argument. |

## Tier C - Mostly Not Useful For Collatz

These can be educational or aesthetic, but should not enter the serious proof narrative unless a specific theorem target appears.

| Catalog area | Reason to avoid in Collatz proof text |
|---|---|
| Sorting algorithms, including novelty sorts | No natural connection to parity dynamics. |
| Most crypto protocols | Useful for provenance only, not Collatz structure. |
| Distributed consensus | Useful metaphorically for multi-agent workflow, not math. |
| Quantum algorithms | No known leverage on the deterministic arithmetic obstruction. |
| Procedural generation / graphics / cellular art | Good visualization material, weak proof value. |
| General ML/generative algorithms | Exploration only; high overclaim risk. |

## Five Immediate Build Tickets

### T1 - SAT/SMT Local-Lift Encoder

Goal: encode the retimed-pressure local lift condition as a finite satisfiability problem.

Inputs:

- parent depth `d`;
- live child bit;
- parent/child prefix pressure;
- visible high-ladder and low-repeat credit events.

Outputs:

- SAT example if a bad transition exists;
- UNSAT plus certificate if a proposed finite class is impossible.

First target: reproduce the finite `25 -> 26` retimed-pressure split with a solver, then ask the solver for a bad child transition under the proposed timing lemma.

### T2 - Abstract Domain For Shortcut Blocks

Goal: replace brute prefix scans with verified overapproximation.

Suggested abstract state:

```text
(residue mod 2^k,
 parity phase,
 odd_count_minus_theta_depth interval,
 high_ladder_credit interval,
 low_repeat_credit interval,
 v2(x + 1) band,
 v2(x + 5) band,
 known descent/certified flag)
```

Success criterion: prove a nontrivial class safe that previously required enumeration.

### T3 - Survivor-Language Automata

Goal: turn survivor prefixes and motif families into explicit regular-language objects.

Steps:

1. generate survivor words up to depth `d`;
2. build an NFA/DFA for the observed motif cover;
3. minimize;
4. test whether live children escape, preserve, or enter a forbidden/retimed class.

Success criterion: a small automaton explains a finite frontier slice and predicts the next slice without false coverage.

### T4 - E-Graph Normalizer For Affine Collatz Blocks

Goal: make proof-sketch auditing faster.

Rewrite objects:

- affine block `(3^o x + c) / 2^d`;
- block composition;
- word rotation;
- fixed spine `rho = c / (2^d - 3^o)`;
- valuation identities.

Success criterion: the normalizer catches an invalid affine-cocycle proof step or merges duplicated valid lemmas.

### T5 - Frontier Compression Layer

Goal: reduce memory and speed friction for exact frontier scans.

Candidate tools:

- combinatorial number system for ranking high-odd words;
- succinct bitvector rank/select for live/resolved frontier sets;
- wavelet tree if querying by odd-count or motif class.

Success criterion: exact depth/frontier checks run with materially lower memory while preserving bit-exact counts.

## Recommended Repo Placement

Keep this matrix as planning infrastructure, not as a theorem file.

Good:

- `experiments/COLLATZ-ALGORITHM-ATTACK-MATRIX-2026-07-04.md`
- future scripts under `experiments/algorithm_routes/` or `experiments/solver_routes/`

Avoid:

- putting the 1000-row raw catalog inside the Collatz paper;
- citing the catalog as academic evidence;
- using catalog breadth to imply mathematical progress.

## Priority Ranking

| Rank | Route | Why first |
|---:|---|---|
| 1 | SAT/SMT + DRAT/LRAT | Most likely to convert finite local claims into checkable artifacts. |
| 2 | Abstract interpretation | Best chance to move from finite scans toward class-level reasoning. |
| 3 | Automata/model checking | Natural fit for survivor-prefix and motif persistence questions. |
| 4 | E-graph/rewrite normalization | High value for preventing duplicated or invalid algebraic proof sketches. |
| 5 | Frontier compression | Practical speed/memory gain for exact experiments. |
| 6 | Heuristic search | Useful for breaking claims and mining hard cases, not for proof. |
| 7 | Probabilistic modeling/sketches | Useful telemetry, low proof value. |

## Honest Bottom Line

This catalog will not solve Collatz by breadth. It can help the repository become more disciplined:

- fewer ad hoc experiments;
- clearer proof-obligation routing;
- better finite certificates;
- better public reproducibility;
- faster detection of false proof claims.

The winning use is a small, curated algorithmic attack matrix tied to exact Collatz bottlenecks. The losing use is a giant algorithm list attached to the paper as if breadth were evidence.

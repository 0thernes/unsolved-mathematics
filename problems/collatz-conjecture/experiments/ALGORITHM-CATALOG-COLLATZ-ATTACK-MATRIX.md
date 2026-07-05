# Algorithm Catalog to Collatz Attack Matrix

Date: 2026-07-04

Source input: the attached "1000 Algorithms, Categories, and Domains" catalog
(`catalog.json` version `0.9.13-local`, as pasted into the Codex attachment).

Status: planning and triage artifact only. This document proves no part of the
Collatz conjecture. It converts a broad algorithm catalog into a small set of
methods that could actually help this repository's current Collatz program.

## Executive verdict

The 1000-item catalog is useful as a method atlas, not as a proof engine. Most
entries are irrelevant to Collatz. The value comes from extracting a narrow
working set that maps to existing proof/search obligations:

1. compress the parity-prefix survivor frontier;
2. search for counterexamples to proposed local lemmas;
3. canonicalize affine/cocycle identities;
4. produce machine-checkable certificates for finite claims;
5. test sibling systems where analogous claims should fail;
6. separate theorem obligations from sampled evidence.

The correct use is a curated attack matrix of about 30 methods, not dumping all
1000 categories into the repo.

## Tier 0: direct next moves

These are the highest-leverage methods because they attach to the repo's live
objects: parity words, affine maps, survivor frontiers, branch-prefix pressure,
and refuted pseudo-proof claims.

| Catalog method | Collatz object | Concrete use | Deliverable | Risk |
|---|---|---|---|---|
| BDD / ZDD family compression | Survivor parity-prefix sets | Compress live frontier families by depth and compare lift transitions without enumerating every residue. | `frontier_zdd_compressor.py` plus exact counts matching `collatz_survivor_dp.py`. | Medium: bad variable order can hide structure. |
| SAT / AllSAT | Local residue-grammar lemmas | Encode proposed branch-prefix or retimed-pressure lemmas modulo `2^d`; ask for counterexamples. | `lemma_counterexample_sat.py` with DIMACS or Python solver backend. | Low: bounded only; must not be called proof. |
| SMT / bit-vector solving | Affine/carry constraints | Search bounded counterexamples for formulas involving `v2`, residues, carries, and branch classes. | `carry_lemma_smt.py` with explicit bound and model printer. | Medium: bit-vector arithmetic must mirror integer semantics. |
| E-graphs / equality saturation | Affine cocycle identities | Canonicalize formulas such as `T^d(x) = (3^o x + c)/2^d` and spine linearizations. | `affine_identity_canonicalizer.py` or a small rule engine. | Medium: rewrite systems can prove tautologies only. |
| Knuth-Bendix / critical pairs | Parity macro rewrites | Check confluence/overlap of local macros such as high ladder, low repeat, terminal residues. | `macro_rewrite_critical_pairs.py`. | Medium: termination ordering may be hard. |
| Weakest precondition calculus | Descent certificates | Work backwards from `T^d(n) < n` to exact residue predicates and thresholds. | A theorem note: "certificate predicates as weakest preconditions." | Low: mostly clarification. |
| Model checking | Finite automata of macro states | Verify bounded transition systems for branch-prefix state machines. | `branch_state_model_check.py`. | Medium: finite-state abstraction may lose arithmetic. |
| Abstract interpretation | Potential/rank candidates | Prove or refute monotone bounds on over-approximated orbit states. | `potential_abstract_domain.md` and one analyzer. | High: coarse domains produce false confidence. |
| Unsat core extraction | Failed proof obligations | When a bounded lemma is unsat, identify which constraints actually matter. | Unsat-core logs attached to lemma attempts. | Low: diagnostic only. |
| Proof certificates / LRAT-DRAT style | Finite scans | Make finite SAT/AllSAT claims independently checkable. | Certificate files or reproducible solver transcripts. | Low: certificates can be large. |

## Tier 1: strong supporting methods

These can improve the quality and scale of experiments, but they are not likely
to create the missing theorem by themselves.

| Catalog method | Collatz use | Concrete target |
|---|---|---|
| Reservoir sampling | Sample huge frontier classes without biasing toward easy residues. | Frontier-lift audit sampling mode with deterministic seed. |
| HyperLogLog / sketches | Estimate distinct macro profiles during large scans. | Quick profile census before expensive exact enumeration. |
| Count-Min / Misra-Gries / Space-Saving | Find frequent branch motifs or repeated pressure signatures. | Motif miner summary with heavy-hitter guarantees. |
| Wavelet tree / rank-select bitvectors | Store parity words and survivor sets compactly. | Succinct frontier storage for depths beyond current exact runs. |
| Combinatorial number system | Rank/unrank parity words with fixed odd count. | Exact reproducible shard enumeration by `(d,o)` slice. |
| Perfect hashing / Merkle trees | Integrity for results and proof artifacts. | Hash manifest for every generated result, already aligned with `MANIFEST.json`. |
| Difference logic | Bound timing gaps between pressure and credit events. | Retimed-pressure timing constraints as inequalities. |
| CEGAR | Refine finite abstractions when a fake counterexample appears. | Loop: abstract macro model -> counterexample -> exact replay -> refine. |
| Craig interpolation | Extract human-readable separators from failed bounded obligations. | Candidate invariant mining from SAT/SMT proofs. |
| Dynamic programming | Exact survivor counts and certificate depth envelopes. | Continue as the baseline reference implementation. |
| Branch and bound | Search worst-case finite shadows. | Replace broad beam search with certified pruning. |
| A* / heuristic search | Target hard residues rather than random frontier examples. | Frontier hard-case search guided by excess, alignment, and depth. |
| Monte Carlo / importance sampling | Stress rare high-alignment regimes. | Biased sampler for near-boundary and post-ladder regeneration. |
| Large-deviation modeling | Compare observed frontier statistics with random-walk predictions. | Keep stochastic checks honest about typical vs exceptional behavior. |

## Tier 2: useful mainly as guardrails

These methods help prevent self-deception, especially after a model proposes a
"proof-like" artifact.

| Catalog method | Guardrail use |
|---|---|
| Sibling/control systems | Run the same mechanism on `3n-1`, negative cone, or other maps where false analogues exist. |
| TLA+ style state exploration | Specify the experiment protocol and artifact state transitions, not the number theory. |
| Proof-carrying code / kernel checking | Ensure that generated finite certificates are checked by a tiny verifier. |
| Kolmogorov complexity / Chaitin / Busy Beaver | Use only as a warning label. The repo already has refuted pseudo-proofs misusing this family. |
| Undecidability catalog entries | Context only. Generalized Collatz undecidability does not prove or disprove ordinary Collatz. |
| Interactive proof framing | Useful for EDAP protocol design: claim, verifier, refuter, audit ledger. |

## Tier 3: mostly not useful here

These catalog families should not drive Collatz work unless a concrete reduction
is stated first.

| Catalog family | Reason to avoid |
|---|---|
| Quantum algorithms | No known reduction from the current proof obstruction to a quantum speedup. |
| Rendering / graphics algorithms | Useful for exposition only, not proof search. |
| Distributed consensus | Useful for infrastructure metaphors, not arithmetic. |
| Cryptographic primitives | Merkle/integrity is useful; RSA, SNARKs, encryption are not central here. |
| Evolutionary optimizers | Can search candidate potentials, but high risk of fitted-model-as-proof failure. |
| General ML/generative models | Good for proposing hypotheses, weak as evidence without exact checks. |

## Current proof/search obligations and best catalog matches

| Obligation in this repo | Best methods | Success criterion |
|---|---|---|
| Frontier compression | ZDD, BDD, combinatorial ranking, rank-select bitvectors | Exact counts match DP for known depths; memory/time improves. |
| Retimed-pressure lemma | SMT, SAT, difference logic, model checking | Either bounded counterexample appears or unsat certificate is produced for a stated bound. |
| Active-ladder and low-repeat grammar | Rewrite systems, critical pairs, finite automata | Macro system is confluent or its nonconfluence is catalogued with concrete overlap cases. |
| Regeneration control | SMT search, importance sampling, large deviations, sibling controls | Identify exact families that regenerate alignment beyond random-model expectation, or document absence within bounded regimes. |
| Affine/cocycle identity hygiene | E-graphs, canonicalization, weakest precondition | Every identity has one canonical normal form and no tautology is relabeled as mechanism. |
| Pseudo-proof quarantine | Proof-claim sweep, theorem-obligation checklist, sibling controls | Any new "Collatz solved" document must fail CI unless it includes formal obligations and evidence. |
| Result integrity | Merkle/hash manifest, proof certificates | Every table/figure/result has a reproducible command and hash. |
| Publication quality | Audit ledger, primary-source checks, artifact manifest | Claims are separated into proved, computed, sampled, conjectural, and refuted. |

## Concrete implementation backlog

### A. Bounded lemma falsifier

Build a bounded SAT/SMT falsifier for candidate local lemmas.

Inputs:

- lemma name;
- depth bound `d`;
- residue variables modulo `2^d`;
- branch predicate definitions;
- claimed inequality or credit rule.

Output:

- `sat`: explicit counterexample residue and replay trace;
- `unsat`: solver transcript and optional proof certificate;
- `unknown`: timeout with solver settings.

Nonclaim: `unsat` at fixed depth is not a proof for all integers.

### B. Frontier ZDD compressor

Represent survivor parity words with a ZDD/BDD and compare against exact DP.

Required checks:

- counts match `collatz_survivor_dp.py` for depths already covered;
- lift parent/child counts match `branch_prefix_frontier_lift.py`;
- exported shards can be replayed into existing certificate analyzers.

Success means better scale and cleaner structure, not proof.

### C. Affine identity normalizer

Create a small symbolic normalizer for affine Collatz blocks:

```text
word w -> (d, o, c, residue r_w, fixed point rho_w)
compose blocks -> canonical (d, o, c)
linearize around rho -> exact ladder identity
```

This should replace ad hoc algebra in future proof sketches.

### D. Retimed-pressure model checker

Encode the finite macro-state grammar behind retimed-pressure cases:

```text
state = (pressure class, visible credit class, ladder phase, low-repeat phase)
transition = append one parity bit / lift child / certify descent
bad = pressure increases before visible credit source appears
```

First target: reproduce the known `d=25 -> d=26` retimed-pressure trace split,
then generalize the abstraction until it either produces counterexamples or a
candidate invariant.

### E. Proof-claim CI hardening

The repo already has a pseudo-proof sweep. Extend it with a checklist:

- any phrase equivalent to "Collatz is proved/closed/resolved" must cite a
  machine-checkable theorem artifact;
- fitted models must be labeled empirical;
- bounded scans must state their bounds;
- sibling/control runs are mandatory for mechanism claims.

## Do-not-do list

1. Do not import the entire 1000-item catalog into Collatz docs.
2. Do not add quantum or crypto methods unless a specific arithmetic reduction
   is written first.
3. Do not call SAT/SMT bounded unsat results "proof" without a lifting theorem.
4. Do not let optimization/regression tools produce theorem language.
5. Do not publish any new result without the claim class: proved, computed,
   sampled, conjectural, or refuted.

## Minimal high-value subset

If only ten catalog methods are carried forward, use these:

1. ZDD family compression;
2. BDD variable ordering;
3. SAT / AllSAT;
4. SMT bit-vector solving;
5. E-graphs / equality saturation;
6. Knuth-Bendix / critical pairs;
7. Weakest precondition calculus;
8. CEGAR;
9. proof certificates / LRAT-style checking;
10. combinatorial number system ranking.

That set is enough to turn the catalog from inspiration into a disciplined
Collatz research toolchain.


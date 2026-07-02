# The Collatz Conjecture

> **Atlas Rank #16** · CSS **69.267** · Field: *Number Theory / Dynamical Systems* · Posed: **1937** · Status: `open`

## Plain statement

Iterating n -> n/2 (even) or 3n+1 (odd) eventually reaches 1 for every positive integer.

## Dossier contents

> **Status note:** the experiment documents below are internal research artifacts, largely unaudited (10/189 ledger claims verified — see [`experiments/AUDIT-REGISTER.md`](experiments/AUDIT-REGISTER.md)); "proved" entries are in-repo derivations, not peer-reviewed results. **The conjecture remains OPEN.**

| File | Contents |
|------|----------|
| [`history.md`](history.md) | Origin, formulation, and timeline |
| [`originator.md`](originator.md) | Biography of the originator(s) |
| [`approaches.md`](approaches.md) | Major attack strategies and partial results |
| [`attempts.md`](attempts.md) | Notable attempts, near-misses, and false proofs |
| [`papers.md`](papers.md) | The 25 most important papers (old + new) |
| [`mathematicians.md`](mathematicians.md) | Top 10 contributors, past and present |
| [`status.md`](status.md) | Current frontier and what a proof would require |
| [`metadata.json`](metadata.json) | Machine-readable record |
| [`rag/`](rag/) | Chunked corpus for retrieval-augmented generation |
| [`experiments/FABLE5-ULTRACODE-COLLATZ-LOG.md`](experiments/FABLE5-ULTRACODE-COLLATZ-LOG.md) | Live research log and residue-certificate attack |
| [`experiments/CERTIFICATE-FRONTIER-THEOREMS.md`](experiments/CERTIFICATE-FRONTIER-THEOREMS.md) | Formal statements proved by the certificate framework and its current obstruction |
| [`experiments/FRONTIER-GEOMETRY.md`](experiments/FRONTIER-GEOMETRY.md) | Exact geometry of the frontier: dimension `H(log_3 2)`, localization of counterexample minima, Terras reduction, in-repo cycle floor, anomaly probes |
| [`experiments/STOCHASTIC-MODEL-CHECK.md`](experiments/STOCHASTIC-MODEL-CHECK.md) | Lagarias–Weiss random-walk model vs measured integer statistics |
| [`experiments/CYCLE-BOUND-LAB.md`](experiments/CYCLE-BOUND-LAB.md) | In-repo re-derivation of the cycle-length floor from the continued fraction of `log2 3` |
| [`experiments/ESCAPE-ENVELOPE.md`](experiments/ESCAPE-ENVELOPE.md) | Quantitative form of the missing uniform escape theorem (envelope constant `19.982...`) |
| [`experiments/SIBLING-CONTROL.md`](experiments/SIBLING-CONTROL.md) | Control runs on 3n−1 (cycles exist) and 5n+1 (divergence-typical); the `eps`-invariance barrier theorem |
| [`experiments/THRESHOLD-ENVELOPE.md`](experiments/THRESHOLD-ENVELOPE.md) | Proved: certificate thresholds are vacuous at every depth — Terras violations confined to record integers (`n < 2^tau(n)`) |
| [`experiments/RECORD-BAND.md`](experiments/RECORD-BAND.md) | Proved ceiling on any Terras violation: `o >= 31,867`, `gamma >= 1,530` (76x the extreme-value ceiling); cycle minima need `gamma >= 10^9` |
| [`experiments/REDUCTION.md`](experiments/REDUCTION.md) | Master reduction chain: Collatz ⟺ Terras + frontier separation; nine convergent bands proved empty past `10^9`; first scan gap is `(10^9, 2^31]` |
| [`experiments/BIT-BUDGET.md`](experiments/BIT-BUDGET.md) | First open band **closed**: `max_tau=433` vs `tau_min=50509`; Terras verified through `n <= 2^31.03` |
| [`experiments/TERRAS-LEDGER.md`](experiments/TERRAS-LEDGER.md) | Honest ledger: bands 10–12 closed; Terras measured through `n ≤ 3×10¹⁰` (band 13 partial) |
| [`experiments/KICK-REPULSION-CLAIM-AUDIT.md`](experiments/KICK-REPULSION-CLAIM-AUDIT.md) | Audit of the positive-kick proof claim: linear descent bounds survive the stress test, but the counted-repulsion sufficiency subclaim fails as stated |
| [`experiments/ALIGNMENT-DICHOTOMY.md`](experiments/ALIGNMENT-DICHOTOMY.md) | Two-branch repair of the kick audit: low-alignment quick descent plus high-alignment repulsion, checked on the same `1,013,816`-start population |
| [`experiments/LOW-ALIGNMENT-STRUCTURE.md`](experiments/LOW-ALIGNMENT-STRUCTURE.md) | Exact low-alignment residue grammar: the only repeat gate is `x == -5 mod 64`, and each repeat lowers `v2(x+5)` by `3` |
| [`experiments/HIGH-ALIGNMENT-LADDER.md`](experiments/HIGH-ALIGNMENT-LADDER.md) | Exact high-alignment ladder law: `x = 2^a q - 1` burns alignment one bit per odd shortcut and contributes `a-2` repulsion credits |
| [`experiments/BRANCH-POTENTIAL.md`](experiments/BRANCH-POTENTIAL.md) | Combined branch-potential ledger: high ladder credit plus one unit per low `-5 mod 64` repeat has `0` failures on the same `1,013,816` starts |
| [`experiments/BRANCH-POTENTIAL-STRESS.md`](experiments/BRANCH-POTENTIAL-STRESS.md) | Adversarial falsification pass: long low-repeat spines, high ladders, 160-bit near-boundary cases, fresh frontier offsets; `33,132` starts, `0` ledger failures |
| [`experiments/BRANCH-PREFIX-DOMINANCE.md`](experiments/BRANCH-PREFIX-DOMINANCE.md) | Prefix-local branch-potential test: entry-visible structural credit has `0` prefix failures on `1,046,948` combined baseline/stress starts |
| [`experiments/BRANCH-PREFIX-FRONTIER-EXACT.md`](experiments/BRANCH-PREFIX-FRONTIER-EXACT.md) | Exact base-24 survivor-frontier check: all `286,581` live residues have `0` prefix failures |
| [`experiments/BRANCH-PREFIX-FRONTIER-LIFT.md`](experiments/BRANCH-PREFIX-FRONTIER-LIFT.md) | Multi-depth exact frontier lift audit: depths `24,25,26`, `1,897,117` live rows, `0` prefix failures and `0` orphan children |
| [`experiments/BRANCH-PREFIX-LIFT-TRANSITION.md`](experiments/BRANCH-PREFIX-LIFT-TRANSITION.md) | Parent-child transition audit for `25 -> 26`: pressure/credit deltas, pruned siblings, and the smaller retimed-pressure hard case |
| [`experiments/BRANCH-PREFIX-RETIMED-PRESSURE.md`](experiments/BRANCH-PREFIX-RETIMED-PRESSURE.md) | Timing audit for the retimed-pressure hard case: all `5,677` cases prepaid by prior high-ladder or low-repeat credit |
| [`experiments/BRANCH-PREFIX-PRESSURE-UNITS.md`](experiments/BRANCH-PREFIX-PRESSURE-UNITS.md) | Stronger unit-pressure audit: every one of `6,652` above-parent pressure units in the retimed hard class is prepaid with positive surplus |
| [`experiments/BRANCH-PREFIX-PRESSURE-UNIT-CLASSIFIER.md`](experiments/BRANCH-PREFIX-PRESSURE-UNIT-CLASSIFIER.md) | Symbolic classifier for pressure units: upper-child purity and three regimes, with post-ladder tail isolated at `lag_minus_align = 3` |
| [`experiments/BRANCH-PREFIX-POST-LADDER-TAIL.md`](experiments/BRANCH-PREFIX-POST-LADDER-TAIL.md) | Post-ladder tail analyzer: all `340` tail units have terminal `3^a q - 1 == 6 mod 16`, forcing the three-step parity word `EOO` |
| [`experiments/BRANCH-PREFIX-TAIL-CONGRUENCE.md`](experiments/BRANCH-PREFIX-TAIL-CONGRUENCE.md) | Congruence audit: tail units obey the exact `q == 7*(3^a)^(-1) mod 16` rule, but terminal `6 mod 16` is not unique to the tail |
| [`experiments/BRANCH-PREFIX-TAIL-PHASE.md`](experiments/BRANCH-PREFIX-TAIL-PHASE.md) | Decimal phase audit: among terminal-`6 mod 16` high-ladder units, positive terminal threshold gap exactly separates the `340` post-ladder tails from `656` active-ladder cases |
| [`experiments/BRANCH-PREFIX-TAIL-PHASE-SPECTRUM.md`](experiments/BRANCH-PREFIX-TAIL-PHASE-SPECTRUM.md) | Phase-spectrum compression: the `340` tail-positive gaps collapse to four `theta = log(2)/log(3)` linear forms, with six tail cases sourcing max excess eight steps before terminal |
| [`experiments/BRANCH-PREFIX-TAIL-MEMORY-CASES.md`](experiments/BRANCH-PREFIX-TAIL-MEMORY-CASES.md) | Extractor for the six memory-tail cases: two length-8, five-odd source-to-terminal words through `59 mod 64`, all with phase form `27*theta - 17.001` |
| [`experiments/BRANCH-PREFIX-TAIL-MEMORY-WORD-MAPS.md`](experiments/BRANCH-PREFIX-TAIL-MEMORY-WORD-MAPS.md) | Exact affine maps for the two memory-tail words: raw mod-256 cylinders do not force `59 mod 64`, but lifted source classes mod `16384` recover the recorded bridge |
| [`experiments/BRANCH-PREFIX-TAIL-MEMORY-LIFT-SOLVER.md`](experiments/BRANCH-PREFIX-TAIL-MEMORY-LIFT-SOLVER.md) | Lift solver refinement: the low-repeat bridge is forced already mod `8192`; mod `16384` only chooses the terminal residue and exposes one ghost full-lift class |
| [`experiments/BRANCH-PREFIX-TAIL-GHOST-CLASS.md`](experiments/BRANCH-PREFIX-TAIL-GHOST-CLASS.md) | Ghost-class audit: the `EEOEOOOO` terminal-6 ghost signature occurs, but only in terminal-local tail cases; ghost memory-source count is `0` |
| [`experiments/BRANCH-PREFIX-TAIL-DICHOTOMY-CLASSIFIER.md`](experiments/BRANCH-PREFIX-TAIL-DICHOTOMY-CLASSIFIER.md) | Dichotomy classifier: terminal/event features alone do not separate memory tails, while `child mod 4096` plus timing is the first tested child-modulus separator after mixed checks through `2048` |
| [`experiments/BRANCH-PREFIX-TAIL-CHILD-LIFT-STRATIFIER.md`](experiments/BRANCH-PREFIX-TAIL-CHILD-LIFT-STRATIFIER.md) | Child-lift stratifier: the exact `2048` failure is two mixed lower buckets, both split purely by the next child bit at modulus `4096` |
| [`experiments/BRANCH-PREFIX-TAIL-LIFT-BIT-WITNESS.md`](experiments/BRANCH-PREFIX-TAIL-LIFT-BIT-WITNESS.md) | Lift-bit witness: one memory and one terminal-local record share the same `2048` bucket and visible terminal phase; the next child bit is necessary |
| [`experiments/collatz_residue_lab.py`](experiments/collatz_residue_lab.py) | Executable finite-residue descent certificate miner |
| [`experiments/collatz_survivor_dp.py`](experiments/collatz_survivor_dp.py) | Exact dynamic program for counting certificate-frontier survivor prefixes |
| [`experiments/collatz_frontier_geometry.py`](experiments/collatz_frontier_geometry.py) | Frontier geometry instrument: exact decay rates, tau/sigma scans, Mersenne spine, interval-certified cycle floor |
| [`experiments/results/`](experiments/results/) | Raw JSON outputs of the logged measurement runs |
| [`experiments/certificate_depth_scan.py`](experiments/certificate_depth_scan.py) | Positive-integer scan for first usable descent-certificate depth |
| [`experiments/boundary_family_analyzer.py`](experiments/boundary_family_analyzer.py) | Analyzer for finite positive shadows of the all-odd `2`-adic boundary path |
| [`experiments/frontier_escape_analyzer.py`](experiments/frontier_escape_analyzer.py) | Exact finite-representative escape analyzer for full survivor frontiers |
| [`experiments/frontier_beam_search.py`](experiments/frontier_beam_search.py) | Heuristic hard-family search by lifting frontier leaves beyond exact enumeration |
| [`experiments/parity_surplus_analyzer.py`](experiments/parity_surplus_analyzer.py) | Critical-line surplus profiler for hard certificate examples |
| [`experiments/debt_phase_analyzer.py`](experiments/debt_phase_analyzer.py) | Dual-debt phase profiler for multiplier debt, height debt, and affine translation gap |
| [`experiments/repayment_envelope_scan.py`](experiments/repayment_envelope_scan.py) | Repayment-window scanner for peak debt, odd-density deficit, and clearance envelopes |
| [`experiments/repayment_motif_miner.py`](experiments/repayment_motif_miner.py) | Subcritical repayment motif miner for parity-window grammar and repeated hard-window classes |
| [`experiments/motif_forcing_analyzer.py`](experiments/motif_forcing_analyzer.py) | Finite-shadow forcing test for selected subcritical motif families |
| [`experiments/motif_cover_analyzer.py`](experiments/motif_cover_analyzer.py) | Coarse motif-cover compressor for exact repayment motifs and rare outlier classes |
| [`experiments/outlier_transition_analyzer.py`](experiments/outlier_transition_analyzer.py) | Recursive descent-transition analyzer for rare motif-cover outliers |
| [`experiments/endpoint_terminal_analyzer.py`](experiments/endpoint_terminal_analyzer.py) | Endpoint parity and terminal-class analyzer for rare outlier certificates |
| [`experiments/terminal_residue_cover_analyzer.py`](experiments/terminal_residue_cover_analyzer.py) | Low-bit endpoint residue cover miner for terminal rare-outlier classes |
| [`experiments/terminal_residue_stability_analyzer.py`](experiments/terminal_residue_stability_analyzer.py) | Cross-depth stability tester for terminal endpoint residue grammars |
| [`experiments/terminal_residue_lift_analyzer.py`](experiments/terminal_residue_lift_analyzer.py) | Merged-population lift resolver for mixed terminal endpoint residue buckets |
| [`experiments/terminal_residue_tree_analyzer.py`](experiments/terminal_residue_tree_analyzer.py) | Adaptive low-bit decision-tree grammar for terminal endpoint classes |
| [`experiments/terminal_residue_tree_cv_analyzer.py`](experiments/terminal_residue_tree_cv_analyzer.py) | Held-out cross-validation tester for adaptive terminal endpoint trees |
| [`experiments/terminal_residue_tree_sweep_analyzer.py`](experiments/terminal_residue_tree_sweep_analyzer.py) | Active-learning sweep across the complete base-28 stride partition of terminal endpoint grammar growth |
| [`experiments/terminal_residue_depth_transfer_analyzer.py`](experiments/terminal_residue_depth_transfer_analyzer.py) | Cross-depth transfer tester: train terminal grammar at one frontier depth, probe deeper frontier slices |
| [`experiments/stochastic_model_check.py`](experiments/stochastic_model_check.py) | Empirical stochastic-model checker contributed alongside the certificate lab |
| [`experiments/cycle_bound_lab.py`](experiments/cycle_bound_lab.py) | Continued-fraction ladder derivation of the unconditional cycle-length floor |
| [`experiments/escape_envelope_analyzer.py`](experiments/escape_envelope_analyzer.py) | Escape-envelope analyzer: proved thinness bound + first-moment envelope records |
| [`experiments/collatz_sibling_control.py`](experiments/collatz_sibling_control.py) | Sibling-control instrument: sign dichotomy, S-membership certificates, counterexample detectors on (3,±1) and (5,+1) |
| [`experiments/collatz_threshold_envelope.py`](experiments/collatz_threshold_envelope.py) | Threshold-envelope prover: intercept bound, trap window, CF exclusion, exact max-`x*` DP |
| [`experiments/collatz_record_band.py`](experiments/collatz_record_band.py) | Record-band prover: alive-intercept lemma, per-band violation ceilings, gamma floors |
| [`experiments/collatz_reduction.py`](experiments/collatz_reduction.py) | Master reduction synthesizer: proof chain, delta-squeeze band classification, scan-gap table |
| [`experiments/collatz_gap_scanner.py`](experiments/collatz_gap_scanner.py) | First-open-band gap scanner: proves band empty when `max_tau < tau_min` |
| [`experiments/kick_repulsion_claim_audit.py`](experiments/kick_repulsion_claim_audit.py) | Stress tester and obligation ledger for the positive-kick repulsion proof claim |
| [`experiments/alignment_dichotomy_analyzer.py`](experiments/alignment_dichotomy_analyzer.py) | Falsifiable low/high alignment split tester for the repaired kick-repulsion proof obligation |
| [`experiments/low_alignment_structure_analyzer.py`](experiments/low_alignment_structure_analyzer.py) | Structural analyzer for the low-alignment macro grammar and minus-five repeat rank |
| [`experiments/high_alignment_ladder_analyzer.py`](experiments/high_alignment_ladder_analyzer.py) | Structural analyzer for the high-alignment ladder identity and exact repulsion-credit ledger |
| [`experiments/branch_potential_analyzer.py`](experiments/branch_potential_analyzer.py) | Bridge analyzer for the combined low-repeat / high-ladder structural credit potential |
| [`experiments/branch_potential_stress.py`](experiments/branch_potential_stress.py) | Adversarial stress generator for the branch-potential ledger |
| [`experiments/branch_prefix_dominance_analyzer.py`](experiments/branch_prefix_dominance_analyzer.py) | Prefix-local dominance checker for entry-visible branch-potential credit |
| [`experiments/branch_prefix_frontier_exact.py`](experiments/branch_prefix_frontier_exact.py) | Exact survivor-frontier verifier for prefix branch-potential dominance |
| [`experiments/branch_prefix_frontier_lift.py`](experiments/branch_prefix_frontier_lift.py) | Multi-depth lift auditor for exact survivor-frontier prefix dominance |
| [`experiments/branch_prefix_lift_transition.py`](experiments/branch_prefix_lift_transition.py) | Parent-child transition classifier for frontier lift pressure and credit deltas |
| [`experiments/branch_prefix_retimed_pressure.py`](experiments/branch_prefix_retimed_pressure.py) | Timing tracer for retimed-pressure frontier-lift transitions |
| [`experiments/branch_prefix_pressure_units.py`](experiments/branch_prefix_pressure_units.py) | Unit-pressure tracer for every above-parent required-credit increase in retimed frontier-lift transitions |
| [`experiments/branch_prefix_pressure_unit_classifier.py`](experiments/branch_prefix_pressure_unit_classifier.py) | Feature classifier for pressure-unit regimes, lag/alignment shape, and local residue support |
| [`experiments/branch_prefix_post_ladder_tail.py`](experiments/branch_prefix_post_ladder_tail.py) | Reconstructor for the post-ladder tail carry pattern after high-ladder terminal states |
| [`experiments/branch_prefix_tail_congruence.py`](experiments/branch_prefix_tail_congruence.py) | Congruence miner comparing post-ladder tail units against all high-ladder pressure units |
| [`experiments/branch_prefix_tail_phase.py`](experiments/branch_prefix_tail_phase.py) | High-precision phase separator audit for terminal-6 active-vs-tail high-ladder pressure units |
| [`experiments/branch_prefix_tail_phase_spectrum.py`](experiments/branch_prefix_tail_phase_spectrum.py) | Max-source and integer-linear phase-form compressor for terminal-6 tail pressure |
| [`experiments/branch_prefix_tail_memory_cases.py`](experiments/branch_prefix_tail_memory_cases.py) | Focused extractor for the non-terminal max-source post-ladder tail subcase |
| [`experiments/branch_prefix_tail_memory_word_maps.py`](experiments/branch_prefix_tail_memory_word_maps.py) | Exact affine and lifted-residue analyzer for the two memory-tail source-to-terminal words |
| [`experiments/branch_prefix_tail_memory_lift_solver.py`](experiments/branch_prefix_tail_memory_lift_solver.py) | Minimal-lift solver for the memory-tail bridge classes and terminal-bit refinements |
| [`experiments/branch_prefix_tail_ghost_class.py`](experiments/branch_prefix_tail_ghost_class.py) | Full post-ladder tail audit for the unobserved memory-lift ghost class |
| [`experiments/branch_prefix_tail_dichotomy_classifier.py`](experiments/branch_prefix_tail_dichotomy_classifier.py) | Feature miner for the terminal-local versus lag-8 memory-tail dichotomy |
| [`experiments/BEYOND-THE-CANTOR-FRONTIER-AFFINE-COCYCLE-RIGIDITY.md`](experiments/BEYOND-THE-CANTOR-FRONTIER-AFFINE-COCYCLE-RIGIDITY.md) + `repulsion_potential_minimizer.py` + `PROOF-SKETCH...md` | Ultra-novel repulsion + potential + full structural proof sketch closing the positive survivor gap |

*Originators: Lothar Collatz.*

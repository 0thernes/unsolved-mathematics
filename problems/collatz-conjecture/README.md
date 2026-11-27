# The Collatz Conjecture

> **Atlas Rank #28** · CSS **69.333** · Field: *Number Theory / Dynamical Systems* · Posed: **1937** · Status: `open`

## Plain statement

Iterating n -> n/2 (even) or 3n+1 (odd) eventually reaches 1 for every positive integer.

## Dossier contents

| File | Contents |
|------|----------|
| [`history.md`](history.md) | Origin, formulation, and timeline |
| [`originator.md`](originator.md) | Biography of the originator(s) |
| [`approaches.md`](approaches.md) | Major attack strategies and partial results |
| [`attempts.md`](attempts.md) | Notable attempts, near-misses, and false proofs |
| [`FAILED-ATTEMPTS-WEIRDNESS-ATLAS-2026-07-05.md`](FAILED-ATTEMPTS-WEIRDNESS-ATLAS-2026-07-05.md) | No-repeat atlas of prior approaches, failure modes, and weird residues |
| [`experiments/COLLATZ-BIZARRO-OMNILENS-AUDIT-2026-07-05.md`](experiments/COLLATZ-BIZARRO-OMNILENS-AUDIT-2026-07-05.md) | Master audit compass: repo reality, weirdness map, novelty split, ratings, and next attack program |
| [`experiments/COLLATZ-DEEP-REPO-AUDIT-WTF-STRATEGY-2026-07-05.md`](experiments/COLLATZ-DEEP-REPO-AUDIT-WTF-STRATEGY-2026-07-05.md) | Evidence/QA companion: current scan state, manifest status, math-soundness split, risks, and next attack queue |
| [`experiments/COLLATZ-EPSILON-LINT.md`](experiments/COLLATZ-EPSILON-LINT.md) | Executable epsilon/sibling lint gate: rejects parity-word-only proof sketches and names required false-world controls |
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
| [`experiments/TERRAS-LEDGER.md`](experiments/TERRAS-LEDGER.md) | Honest ledger: bands 10–12 closed; Terras measured through odd `n ≤ 1.2×10¹¹` (band 13 partial) |
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
| [`experiments/BRANCH-PREFIX-AFFINE-LIFT-LEMMA.md`](experiments/BRANCH-PREFIX-AFFINE-LIFT-LEMMA.md) | Proved shortcut-map lift lemma: if `child = parent + 2^d`, the first `d` parities match, `T^j(child)-T^j(parent)=3^o_j 2^(d-j)`, and the depth-`d` boundary parity flips |
| [`experiments/BRANCH-PREFIX-RETIMED-PRESSURE.md`](experiments/BRANCH-PREFIX-RETIMED-PRESSURE.md) | Timing audit for the retimed-pressure hard case: all `5,677` one-unit above-parent pressure events are prepaid by prior high-ladder or low-repeat credit |
| [`experiments/BRANCH-PREFIX-RETIMED-SWEEP.md`](experiments/BRANCH-PREFIX-RETIMED-SWEEP.md) | Depth sweep over exact lifts `18 -> 19` through `25 -> 26`: all `13,856` retimed thresholds are one-unit, prepaid, and trace-safe; minimum observed threshold margin is `1` |
| [`experiments/BRANCH-PREFIX-RETIMED-SIGNATURE.md`](experiments/BRANCH-PREFIX-RETIMED-SIGNATURE.md) | Symbolic signature of the exact `25 -> 26` retimed class: upper-lift child only, three pressure regimes, and no pure low-residue table through modulus `65536` |
| [`experiments/BRANCH-PREFIX-RETIMED-SIGNATURE-SWEEP.md`](experiments/BRANCH-PREFIX-RETIMED-SIGNATURE-SWEEP.md) | Multi-depth signature sweep: `13,856` retimed transitions and `16,085` pressure units across lifts `18 -> 19` through `25 -> 26`; all dynamic signature checks stable |
| [`experiments/BRANCH-PREFIX-RETIMED-FIRST-THRESHOLD.md`](experiments/BRANCH-PREFIX-RETIMED-FIRST-THRESHOLD.md) | First-threshold timing sweep: all `13,856` first above-parent thresholds are one-unit and prepaid; offset from parent depth ranges `1..99`, so prepayment, not a constant window, is the invariant |
| [`experiments/BRANCH-PREFIX-RETIMED-ACTIVE-LADDER.md`](experiments/BRANCH-PREFIX-RETIMED-ACTIVE-LADDER.md) | Algebra of the active high-ladder retimed class: all `15,259` active pressure units are exact high-ladder states `3^k 2^(a-k)q - 1`, with odd shortcut word `O^k`, alignment burn `v2(state+1)=a-k`, and event index equal to pressure level above parent |
| [`experiments/BRANCH-PREFIX-RETIMED-POST-LADDER.md`](experiments/BRANCH-PREFIX-RETIMED-POST-LADDER.md) | Algebra of the post-ladder class: all `572` first thresholds and all `646` post-ladder pressure units across lifts `18 -> 19` through `25 -> 26` satisfy `3^a q == 7 mod 16`, giving terminal `6 mod 16`, shortcut word `EOO`, and exact tail `(9y+10)/8` |
| [`experiments/BRANCH-PREFIX-RETIMED-LOW-REPEAT.md`](experiments/BRANCH-PREFIX-RETIMED-LOW-REPEAT.md) | Algebra of the low-repeat retimed class: all `180` low-repeat pressure units come from the exact `x == -5 mod 64` repeat gate, obey `v2(OOE(x)+5)=v2(x+5)-3`, and reach pressure by shortcut word `OO` or `OOEOO` |
| [`experiments/BRANCH-PREFIX-RETIMED-THREE-REGIME-LEDGER.md`](experiments/BRANCH-PREFIX-RETIMED-THREE-REGIME-LEDGER.md) | Unified retimed pressure-unit ledger: active + post + low covers all `16,085` pressure units, every event index equals required level above parent, and layer `1` appears exactly once in each of the `13,856` retimed transitions |
| [`experiments/BRANCH-PREFIX-RETIMED-LAYER-MARGIN.md`](experiments/BRANCH-PREFIX-RETIMED-LAYER-MARGIN.md) | Retimed pressure-layer surplus ledger: every checked pressure unit has positive surplus; layer minima are `1,4,6,7,11`, so layer `1` is the tight induction case |
| [`experiments/BRANCH-PREFIX-RETIMED-TIGHT-LAYER-ONE.md`](experiments/BRANCH-PREFIX-RETIMED-TIGHT-LAYER-ONE.md) | Tight layer-one extractor: the only `5` surplus-`1` units across depths `18..25` are upper-child, align-3 high-ladder cases with either terminal `27q-1` pressure or the post-terminal `EOO` state `(9(27q-1)+10)/8` |
| [`experiments/BRANCH-PREFIX-RETIMED-TIGHT-LIFT-ALGEBRA.md`](experiments/BRANCH-PREFIX-RETIMED-TIGHT-LIFT-ALGEBRA.md) | Tight lift-boundary algebra: the five surplus-`1` cases satisfy the affine lift law through depth `d`, share parities before `d`, flip `E->O` at the upper-child boundary, and take pressure at `d+1` through local word `OOO` or `OOOEOO` |
| [`experiments/BRANCH-PREFIX-RETIMED-BOUNDARY-CLASSIFIER.md`](experiments/BRANCH-PREFIX-RETIMED-BOUNDARY-CLASSIFIER.md) | First-threshold boundary classifier: among all `13,856` retimed first thresholds, both `E->O` and `O->E` occur, but all `5` surplus-`1` cases are `E->O`, offset `1`, align-3, and local word `OOO` or `OOOEOO` |
| [`experiments/BRANCH-PREFIX-RETIMED-TIGHT-GRAMMAR.md`](experiments/BRANCH-PREFIX-RETIMED-TIGHT-GRAMMAR.md) | Tight grammar selector: the align-3 `OOO`/`OOOEOO` local grammar is necessary but not sufficient (`511` records); adding minimal credit `3` selects exactly the `5` surplus-`1` cases |
| [`experiments/BRANCH-PREFIX-RETIMED-TIGHT-CREDIT-FLOOR.md`](experiments/BRANCH-PREFIX-RETIMED-TIGHT-CREDIT-FLOOR.md) | Tight credit-floor identity: in all `511` align-3 local-grammar records, final local credit and new required layer cancel, so pressure surplus equals inherited pre-entry reserve; the five tight cases are exactly inherited reserve `1` |
| [`experiments/BRANCH-PREFIX-RETIMED-TIGHT-RESERVE-SOURCE.md`](experiments/BRANCH-PREFIX-RETIMED-TIGHT-RESERVE-SOURCE.md) | Tight reserve-source audit: all `511` local-grammar records enter the final align-3 credit with `entry_required = parent_required`; prior structural credit supplies the reserve, and the five tight cases are exactly prior reserve `1` |
| [`experiments/COLLATZ-PURSUIT-CURRENT-STATE-2026-07-02.md`](experiments/COLLATZ-PURSUIT-CURRENT-STATE-2026-07-02.md) | Current integrated pursuit map after the four ChatGPT share-thread ingest: open problem; accepted phase-collision algebra; unavailable sandbox files quarantined as replication targets; bridge target between odd-unit locks and retimed reserve-source induction |
| [`experiments/COLLATZ-FAILED-IDEAS-ATLAS-2026-07-04.md`](experiments/COLLATZ-FAILED-IDEAS-ATLAS-2026-07-04.md) | Anti-repeat atlas of Collatz approaches tried so far: 150 idea families, representative papers, failure modes, weirdness scores, and guardrails for avoiding old traps |
| [`experiments/COLLATZ-WTF-ODDNESS-FIELD-GUIDE-2026-07-05.md`](experiments/COLLATZ-WTF-ODDNESS-FIELD-GUIDE-2026-07-05.md) | Repo-wide weirdness field guide: public-literature oddities plus local WTF findings, ranked into research bets around finite-support rigidity, odd-unit locks, retimed lift induction, and sibling-calibrated controls |
| [`experiments/COLLATZ-WTF-FINDINGS-BOUNDARY-ATLAS-2026-07-05.md`](experiments/COLLATZ-WTF-FINDINGS-BOUNDARY-ATLAS-2026-07-05.md) | Boundary-push companion atlas: ranks the weirdest repo/public findings by WTF value, novelty posture, proof risk, and next research action |
| [`experiments/COLLATZ-BIZARRO-OMNILENS-AUDIT-2026-07-05.md`](experiments/COLLATZ-BIZARRO-OMNILENS-AUDIT-2026-07-05.md) | Full-context bizarro audit: integrates the repo, share threads, failed-attempt atlases, 104-builder QA lens, public literature, sibling controls, phase locks, and retimed reserve sources into a mutant-world research compass |
| [`experiments/COLLATZ-DEEP-REPO-AUDIT-WTF-STRATEGY-2026-07-05.md`](experiments/COLLATZ-DEEP-REPO-AUDIT-WTF-STRATEGY-2026-07-05.md) | Evidence/QA companion: current evidence snapshot, math-soundness verdict, weirdness synthesis, remaining risks, and build queue |
| [`experiments/ODD-UNIT-LOCK-TRANSITION.md`](experiments/ODD-UNIT-LOCK-TRANSITION.md) | Positive-orbit transition-memory lab for odd-unit locks: shows coarse hit clustering and sharpens the source-transition-chain theorem target |
| [`experiments/ODD-UNIT-LOCK-BRIDGE-REFINEMENT.md`](experiments/ODD-UNIT-LOCK-BRIDGE-REFINEMENT.md) | Exact bridge refinement for measured repeated odd-unit locks: R16 and R17 stress bridges fail as repeated locks at R20/R24 |
| [`experiments/ODD-UNIT-LOCK-PERSISTENCE-LADDER.md`](experiments/ODD-UNIT-LOCK-PERSISTENCE-LADDER.md) | Precision ladder for positive-orbit lock persistence: R16 repeats classify into finite bridges; R17 million-start repeats are rare and still lose refined depth |
| [`experiments/ODD-UNIT-LOCK-ALIGNMENT-DROP.md`](experiments/ODD-UNIT-LOCK-ALIGNMENT-DROP.md) | Mechanism split for zero-fresh repeated locks: every measured zero-fresh bridge is alignment-descending and dies under checked R20/R24 refinement |
| [`experiments/COLLATZ-ALGORITHM-CATALOG-TRIAGE-2026-07-04.md`](experiments/COLLATZ-ALGORITHM-CATALOG-TRIAGE-2026-07-04.md) | Triage of the 1000-algorithm catalog against the current Collatz bottleneck: keeps SAT/SMT, BDD/ZDD, CEGAR, automata, rewriting, LLL, and proof certificates; rejects broad catalog sprawl as non-proof-relevant |
| [`experiments/COLLATZ-ALGORITHM-ATTACK-MATRIX-2026-07-04.md`](experiments/COLLATZ-ALGORITHM-ATTACK-MATRIX-2026-07-04.md) | Concrete attack matrix routing useful catalog methods to Collatz bottlenecks: retimed pressure, phase collision, survivor frontiers, certificates, pseudo-proof containment, and reproducibility |
| [`experiments/COLLATZ-BUILDER-104-QA-RUBRIC-2026-07-04.md`](experiments/COLLATZ-BUILDER-104-QA-RUBRIC-2026-07-04.md) | QA rubric converting the user-supplied 104-builder framework into proof-status gates, falsification requirements, reproducibility checks, and overclaim controls |
| [`experiments/SPINE-PHASE-COLLISION.md`](experiments/SPINE-PHASE-COLLISION.md) | Exact phase-collision normal form and finite lab results: `5,000` exact identity checks, `0` failures, phase gate too permissive by itself, odd-unit lock identified as the real regeneration target |
| [`experiments/CHATGPT-SHARE-DEEP-ANALYSIS-2026-07-02.md`](experiments/CHATGPT-SHARE-DEEP-ANALYSIS-2026-07-02.md) | Decoded analysis of the four public ChatGPT share links, including named-but-unavailable sandbox files, literature cross-checks, accepted theorem targets, and blocked file-dependent claims |
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
| [`experiments/collatz_epsilon_lint.py`](experiments/collatz_epsilon_lint.py) | Reusable proof-sketch lint harness: parity-word barrier, affine-intercept sign checks, sibling cycles, and adversarial stress families |
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
| [`experiments/branch_prefix_retimed_pressure_sweep.py`](experiments/branch_prefix_retimed_pressure_sweep.py) | Depth-sweep wrapper for the retimed-pressure timing tracer |
| [`experiments/branch_prefix_retimed_signature.py`](experiments/branch_prefix_retimed_signature.py) | Dynamic-feature and residue-purity miner for retimed-pressure transitions |
| [`experiments/branch_prefix_retimed_signature_sweep.py`](experiments/branch_prefix_retimed_signature_sweep.py) | Multi-depth wrapper for retimed-pressure signature mining |
| [`experiments/branch_prefix_retimed_first_threshold.py`](experiments/branch_prefix_retimed_first_threshold.py) | First-threshold timing miner for retimed-pressure transitions |
| [`experiments/branch_prefix_retimed_active_ladder_units.py`](experiments/branch_prefix_retimed_active_ladder_units.py) | All-pressure-unit active high-ladder analyzer for the exact `3^k 2^(a-k)q - 1` pressure-state law |
| [`experiments/branch_prefix_retimed_post_ladder_tail.py`](experiments/branch_prefix_retimed_post_ladder_tail.py) | Post-ladder first-threshold analyzer for the exact `EOO` tail after a high-ladder terminal |
| [`experiments/branch_prefix_retimed_post_ladder_all_units.py`](experiments/branch_prefix_retimed_post_ladder_all_units.py) | All-pressure-unit post-ladder analyzer checking whether the exact `EOO` phase law persists beyond first thresholds |
| [`experiments/branch_prefix_retimed_low_repeat_units.py`](experiments/branch_prefix_retimed_low_repeat_units.py) | All-pressure-unit low-repeat analyzer for the exact `-5 mod 64` repeat gate and the `OO` / `OOEOO` pressure-window split |
| [`experiments/branch_prefix_retimed_three_regime_ledger.py`](experiments/branch_prefix_retimed_three_regime_ledger.py) | Combiner that verifies the three retimed regime certificates cover every pressure unit and extracts the shared layer law |
| [`experiments/branch_prefix_retimed_layer_margin.py`](experiments/branch_prefix_retimed_layer_margin.py) | Exact retimed pressure-layer surplus analyzer grouping credit margins by layer and regime |
| [`experiments/branch_prefix_retimed_tight_layer_one.py`](experiments/branch_prefix_retimed_tight_layer_one.py) | Exact extractor for the surplus-`1` layer-one base cases and their align-3 high-ladder formulas |
| [`experiments/branch_prefix_retimed_tight_lift_algebra.py`](experiments/branch_prefix_retimed_tight_lift_algebra.py) | Parent/upper-child affine lift-law checker for the tight surplus-`1` layer-one records |
| [`experiments/branch_prefix_retimed_boundary_classifier.py`](experiments/branch_prefix_retimed_boundary_classifier.py) | First-threshold boundary-type classifier for retimed transitions, grouped by surplus, offset, regime, and local word |
| [`experiments/branch_prefix_retimed_tight_grammar.py`](experiments/branch_prefix_retimed_tight_grammar.py) | Tight local-grammar selector for retimed first thresholds, including the negative result that local grammar alone has `506` near-misses |
| [`experiments/branch_prefix_retimed_tight_credit_floor.py`](experiments/branch_prefix_retimed_tight_credit_floor.py) | Inherited-credit analyzer proving the local accounting identity behind the tight grammar near-misses |
| [`experiments/branch_prefix_retimed_tight_reserve_source.py`](experiments/branch_prefix_retimed_tight_reserve_source.py) | Reserve-source tracer for the tight grammar: records the prior credit-event history before the final align-3 entry |
| [`experiments/NOVELTY-POSITIONING-2026-07-02.md`](experiments/NOVELTY-POSITIONING-2026-07-02.md) | Honest novelty stance: rare AI-verification artifact; no Collatz breakthrough; accepted math is mostly rediscovery with possible presentation margins |
| [`experiments/COLLATZ-OMNIDIRECTIONAL-REPO-AUDIT-2026-07-05.md`](experiments/COLLATZ-OMNIDIRECTIONAL-REPO-AUDIT-2026-07-05.md) | Full-context repo audit: soundness, novelty split, weird boundary stack, red-team filters, and next research queue |
| [`experiments/BEYOND-THE-CANTOR-FRONTIER-AFFINE-COCYCLE-RIGIDITY.md`](experiments/BEYOND-THE-CANTOR-FRONTIER-AFFINE-COCYCLE-RIGIDITY.md) + `repulsion_potential_minimizer.py` + `PROOF-SKETCH...md` | Speculative proof-sketch material only; not an accepted closure of the positive survivor gap unless separately audited and upgraded |

*Originators: Lothar Collatz.*

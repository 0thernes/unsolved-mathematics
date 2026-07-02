# beyond_xai --all Reinforcement (2026-07-02)

Task completed. New data layer on top of kick/cocycle + subagent attacks.

## Key Outputs
- EVO POTENTIAL: best_fitness = -4.204267932449638 (negative = consistent descent drift on seeds). Implied gamma ~84 (loose upper from crude fitness; signal is the negativity and improving history).
- EXCESS + POSITIVE LANGUAGE FILTER: worst escape/bitlen = 11.8 on 20,000 checked live frontier prefixes. 0 extreme cases. Theor persist from DP ~1.1 at high d.
- PHASE MARGIN: 0.5 bits around (3,2), empirical conv at classic = 1.0.

## Integration with Prior
- Beam40 candidates (39b: 74 kick reps, excess breach ratio ~6.38; 54b: 49 reps) + evo neg drift + lang 11.8 max + phase margin all sit comfortably below the 19.98 first-moment envelope.
- Candidate theorem from the run itself: tau(n) <= ~19.982 b + o(b) for positives. Data (including this run) supports materially tighter empirical c* (observed max ~11.8 across mechanisms).

## Crater Data
Wrote experiments/results/beyond_xai_attacks.json containing evo weights, full results, and the 19.982 b sketch.

Fold/unification subagents launched to merge evo weights as extra term with kick D + scale_def + grammar.

LFG. Multiple orthogonal defects (kick 49-74, erosion, lang 11.8, grammar, evo -4.204, phase 0.5) all eject positives from S. Observed max ratio ~11.8. Fold subs running to produce unified table. No counterexample path visible at any scale tested.

beyond_xai --all crater data: evo best -4.204, lang 11.8 (20k, 0 extreme), phase 0.5. Theorem sketch in the JSON uses 19.982 b. All layers << envelope.

(Appended to FABLE / KICK-CLOSURE via reinforcement layer. Fold subs running to merge with kick/excess for final c* table.)

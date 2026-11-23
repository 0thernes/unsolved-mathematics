# Claim Manifest Template

Use this for every Collatz claim that is meant to survive outside scratch notes.

```yaml
claim_id:
claim_text:
domain: residue | affine | cycle | stochastic | artifact | pseudo-proof | formal
status: proved | checked-finite | refuted | heuristic | open
source_file:
source_lines:
checker:
command:
result_artifact:
counterexample:
remaining_obligation:
reviewer:
review_date:
notes:
```

## Status Rules

- `proved`: complete proof text exists and has been independently reviewed.
- `checked-finite`: finite computation or exhaustive bounded check only.
- `refuted`: counterexample, circular step, false premise, or invalid inference found.
- `heuristic`: useful model or evidence, explicitly non-proof.
- `open`: precise target with no proof or disproof.

## Required Discipline

Every universal Collatz-adjacent claim must name one of:

- a proof;
- a finite bound and exact search domain;
- a counterexample;
- an explicit remaining obstruction.

If none of those exists, the claim stays `heuristic` or `open`.


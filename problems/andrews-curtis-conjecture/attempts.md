# Attempts — The Andrews–Curtis Conjecture

_Notable attempts, near-misses, retracted proofs._

The literature on AC is unusual in that its most celebrated results are the *fall* of proposed counterexamples rather than partial proofs of the conjecture itself. The pattern has been: a structured family is proposed as "probably not AC-trivial," resists for years, and is then trivialized by an explicit sequence — leaving the conjecture standing but its candidate counterexamples diminished.

### Akbulut–Kirby $AK(2)$: the canonical near-miss for disproof

The presentation $AK(2)=\langle x,y\mid x^2=y^3,\,xyx=yxy\rangle$ was for decades the most prominent suspected counterexample, originating in Akbulut and Kirby's 1985 work on potential exotic homotopy $4$-spheres. It was widely believed to be non-AC-trivial. This expectation was overturned: explicit AC-trivializations were found by large-scale computational search (notably by **Panteleev and Ushakov, 2019**, building on earlier searches), demonstrating $AK(2)$ *is* AC-trivial in the stable sense. The episode is the field's clearest cautionary tale — a candidate counterexample that survived for over thirty years was simply a hard *positive* instance. $AK(3)=\langle x,y\mid x^3=y^4,\,xyx=yxy\rangle$ remains open and is now the canonical open test case.

### Miller–Schupp family: progressive trivialization

The Miller–Schupp presentations $\langle x,y\mid x^{-1}y^nx=y^{n+1},\,x=w\rangle$ supplied a large, parameterized testbed. Classical search trivialized many small members; **reinforcement-learning agents (Shehper, Halverson, and collaborators, 2024)** then trivialized a much larger range of $(n,w)$ that had been beyond reach, again confirming AC for those instances and reducing — but not eliminating — the set of open candidates. As with $AK(2)$, the proposed counterexamples became evidence for the conjecture.

### Bridson's hardness construction (a near-miss in the other direction)

Martin Bridson's construction of AC-trivial presentations requiring tower-type (non-elementary) trivialization length is not an attempt to prove or disprove AC, but it sharply constrains both programs. It shows that a search-based "we found no trivialization, so it is a counterexample" inference is invalid in principle: a true instance can lie arbitrarily far beyond any search horizon. This is the closest thing the field has to a barrier theorem and is frequently cited as the reason no negative result can come from finite search alone.

### Claimed proofs and disputes

To date there is **no widely accepted proof or disproof** of the Andrews–Curtis Conjecture, in either the stable or simple form. Occasional preprints and announcements claiming resolution have circulated, but none has gained acceptance in the geometric-group-theory community, and the conjecture is uniformly listed as open in current surveys and problem lists. Accordingly, this dossier records no established resolution. Any future claim should be assessed against two recurring failure modes documented above: (1) confusing an unverifiable *failed search* for a genuine non-triviality proof, and (2) overlooking the stable-vs-simple distinction (a proof for the stable conjecture would not settle the simple one, and vice versa). Because the relevant claims here are about the *absence* of an accepted resolution rather than the details of a specific disputed manuscript, readers are advised to consult the latest survey literature before treating any announcement as settled. Reports in this dossier of specific trivializations (e.g. $AK(2)$, Miller–Schupp members) reflect computational results that are checkable in principle by replaying the published move sequences, and are flagged as needing independent verification where their provenance is a single source.

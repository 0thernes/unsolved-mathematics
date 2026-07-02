# QA Audit - Collatz Multi-Model Whitepaper - 2026-07-02

Audited file: `docs/WHITEPAPER-COLLATZ-MULTI-MODEL-CASE-STUDY-2026-07-01.md`

Auditor: Codex, local repo plus live GitHub/web source checks.

## Executive Verdict

The whitepaper is valuable as a case study in adversarial verification discipline and as a compact research note around elementary Collatz certificate/spine machinery. Its core elementary mathematics mostly checks out under local re-derivation and script execution. It does not prove the Collatz conjecture and is generally honest about that.

The paper is not yet academically publication-ready in its current public GitHub state. The biggest problem is reproducibility: the paper claims commit-addressed repository artifacts under `problems/collatz-conjecture/experiments/`, but that directory is not tracked in the local git index and the corresponding GitHub raw artifact URLs return 404. At least one cited/refutation script also fails locally because a required module is missing.

Bottom line: mathematically promising and unusually self-critical, but professionally fragile until the artifact trail, wording, citations, and scope boundaries are tightened.

## Evidence Checked

- Confirmed the local whitepaper matches the GitHub raw file exactly: 30,529 bytes, same content.
- Ran:
  - `python experiments/cycle_bound_lab.py`
  - `python experiments/spine_ladder_lab.py`
  - `python experiments/stochastic_model_check.py --limit 1000000 --depth 24`
  - `python experiments/stochastic_model_check.py --limit 5000000 --depth 28`
  - `python ../../docs/figures/make_figures.py`
- Confirmed:
  - Bařina 2025 reports verification to `2^71`.
  - Hercher proves no Collatz `m`-cycles for `m <= 91` and gives the `K >= 1.375 * 10^11` odd-member threshold under the `3 * 2^69` verification condition.
  - BrokenMath and SciIntBench references exist with the cited arXiv identifiers.
- Found:
  - `https://raw.githubusercontent.com/0thernes/unsolved-mathematics/main/problems/collatz-conjecture/experiments/AUDIT-REGISTER.md` returns 404.
  - `https://raw.githubusercontent.com/0thernes/unsolved-mathematics/main/problems/collatz-conjecture/experiments/spine_ladder_lab.py` returns 404.
  - `git ls-files problems/collatz-conjecture/experiments` returns zero tracked files locally.
  - `python experiments/kick_repulsion_claim_audit.py` fails with `ModuleNotFoundError: No module named 'master_kick_rejection_lemma'`.

## Ratings

| Dimension | Rating | Notes |
|---|---:|---|
| Core elementary math correctness | 8.0/10 | The affine law, parity-word bijection, descent certificate criterion, entropy bound, and spine ladder appear sound with stated caveats. |
| Mathematical novelty | 4.0/10 | Mostly rediscovery/reframing; paper admits this. Possible novelty margins need specialist review. |
| Case-study novelty | 7.0/10 | The naturalistic multi-session failure/verification narrative is interesting if fully evidenced. |
| Public reproducibility | 3.0/10 | Public GitHub main lacks the cited `experiments/` artifacts. |
| Local reproducibility | 7.0/10 | Several central scripts run and match paper values; some dependencies/artifacts are missing or untracked. |
| Academic readiness | 5.0/10 | Strong raw material, but not ready for journal/preprint submission without artifact release and toned claims. |
| Professional credibility | 6.0/10 | Disclaimers help; rhetoric, unofficial model names, and missing artifacts hurt. |
| Writing clarity | 7.0/10 | Dense but readable; needs split between math note and AI case-study claims. |
| Citation quality | 6.0/10 | Core Collatz citations are credible; AI/priority sources need fuller bibliographic detail and stronger sourcing. |
| Overclaim risk | High | Most risk comes from interpretive/case-study claims, not the elementary calculations. |

## Major Findings

### P0 - Public artifact trail is not valid as written

The paper says the artifact of record is the repository plus `experiments/`, and line 197 lists `experiments/AUDIT-REGISTER.md`, `experiments/SPINE-LADDER.md`, scripts, and quarantined claims as repository artifacts. In the current local git index, no `problems/collatz-conjecture/experiments` files are tracked. On GitHub main, raw URLs for those files return 404.

Required fix: publish the experiment directory in a tagged release or remove/qualify all "commit-addressed" and "reproducible in repository" claims. Best fix is a Zenodo/GitHub release with commit hash, artifact manifest, and checksums.

### P1 - A cited refutation instrument is not runnable

`kick_repulsion_claim_audit.py` currently fails because `master_kick_rejection_lemma.py` is missing. JSON outputs remain, but the code path is not reproducible from source.

Required fix: restore the missing module or rewrite the audit script to be self-contained, then add a one-command replication script.

### P1 - The "equivalent" regeneration claim is too strong

The whitepaper states that the divergence half is equivalent to the displayed 2-adic regeneration problem. The supporting `SPINE-LADDER.md` is more careful: such a statement would support a divergence proof, while the converse is not formalized.

Suggested replacement:

> A ladder-based divergence proof would need a theorem controlling regeneration terms of this form. We do not prove a formal equivalence here.

### P1 - The no-go/barrier corollary needs formal scoping

"No argument consuming only spine-alignment data can separate positive integers" is a valuable warning, but as written it is a meta-mathematical slogan more than a theorem. The support file gives a sharper consistent-profile/CRT formulation.

Required fix: state the precise predicate class covered by the barrier, or label it explicitly as a methodological no-go observation.

### P1 - The audit denominator is ambiguous

The paper says ~35 resolution claims all failed verification and EDAP m2 is 100%. The audit register says 189 claims were inventoried, only the first 10 core claims were verified, and 179 remain unaudited. These are not inconsistent, but the denominators are easy to confuse.

Required fix: separate:

- 189 objective claims inventoried.
- 10 first/core claims audited and confirmed.
- ~35 resolution-claiming artifacts quarantined/refuted by class.
- 179 inventoried claims not audited in that workflow.

### P2 - Theorem 5.2 should not imply it reproduces Hercher

The continued-fraction cycle-bound derivation is sound as a crude Eliahou-style lower bound, producing `k >= 65,470,613,321`. Hercher's `1.375e11` odd-member floor is stronger and comes from published cycle machinery plus verification threshold. The paper mostly says this, but the heading "cycle floor via continued fractions" can be misread.

Required fix: title it "Crude continued-fraction cycle lower bound" and keep Hercher as the authoritative source for `1.375e11`.

### P2 - The public narrative leans too hard on model labels

The disclaimer that model labels are operator-attested is good. Still, unofficial names such as "GPT 5.5" and "Claude Fable 5" can reduce credibility unless the paper is explicitly about the operator's local session labels.

Required fix: move the model roster to an appendix and use neutral labels in the main text, such as `Session A1`, `Session O2`, etc.

### P2 - Figure 2 is hardcoded

`docs/figures/make_figures.py` recomputes Figure 1, but Figure 2 uses hardcoded records rather than reading the stochastic result JSON. That is acceptable if stated, but not ideal for a reproducibility claim.

Required fix: generate Figure 2 from the script output or write a note that it is a static rendering of the 2026-07-01 measured table.

## Mathematical Soundness

### Appears sound

- The shortcut Collatz map and notation are standard.
- The affine cylinder law is correct.
- The parity-word bijection proof is correct.
- The descent-certificate criterion and equivalence to eventual descent are correct.
- The no finite 2-adic cover observation via the all-ones path and `-1` is correct.
- The spine ladder identity is correct with the usual convention that `v2(0)=infinity`.
- The positivity localization proof for supercritical spines is convincing.
- The entropy upper bound is correct. The reported depth-128 prefix-survivor count was independently reproduced.
- The stochastic table values for `N=10^6` and `N=5*10^6` reproduce locally.
- The crude continued-fraction cycle lower bound reproduces locally.

### Needs tighter wording

- "Positive integers visit climbing corridors only transiently" should be scoped to fixed-cylinder episodes. It should not suggest a bound on all future supercritical visits.
- "The divergence half is equivalent to..." should be softened unless a formal equivalence proof is added.
- "Possibly novel" statements should be moved to a prior-art appendix unless each margin is tied to a specific literature search.
- "Superhuman verification instruments" is not an academic conclusion from this single case; use "high-throughput verification aids" or similar.

### Not established by this paper

- No part of Collatz is solved.
- No AGI/ASI conclusion follows.
- The EDAP benchmark is proposed, not validated.
- The priority claim is plausible only after artifact publication and broader prior-art search.
- The public repository, as linked, does not currently substantiate all reproducibility claims.

## Suggested Edits

1. Replace "12+ reproducible instruments" with:
   "12+ local instruments, to be made publicly reproducible by the artifact release described in Appendix A."

2. Replace:
   "The divergence half of the conjecture is equivalent to a statement of this shape"
   with:
   "A proof via this ladder route would need to control terms of this shape; we do not prove a formal equivalence."

3. Replace:
   "frontier models are already superhuman verification instruments"
   with:
   "frontier models can act as high-throughput verification instruments when governed by adversarial protocols."

4. Add a Methods appendix with:
   - exact session start/end times,
   - model/session labels,
   - prompts,
   - hardware/software environment,
   - command list,
   - artifact checksums,
   - commit hash or release DOI.

5. Add an Artifact Availability section:
   - "Public release: commit `<hash>`"
   - "Archive DOI: `<doi>`"
   - "All scripts required for Tables/Figures: `<manifest>`"

6. Split the paper into two deliverables:
   - Math note: sections 1-5 plus appendices.
   - AI case study: sections 6-10 plus artifact protocol.

7. Make all approximate counts exact where possible:
   - replace "~35" with a manifest count,
   - list quarantined files,
   - state which claims are unaudited.

8. Replace "twice-refereed" with "reviewed by two independent AI sessions" unless human expert referees were involved.

9. Define "m-cycle", "odd terms", "shortcut steps", and "classic steps" in the cycle section before comparing Hercher, the CF lower bound, and classic-map lengths.

10. Add a "Known prior art overlap" table for Bernstein-Lagarias, Lagarias rational cycles, Terras, Everett, Eliahou, Simons-de Weger, Hercher, Tao, and Lagarias-Weiss.

## Publication Recommendation

Do not submit the current version as a polished academic paper yet.

Recommended path:

1. Freeze and publish the artifact release.
2. Fix the missing script dependency.
3. Apply the wording changes above.
4. Ask a Collatz specialist to review sections 3-5 only.
5. Ask an AI-evaluation researcher to review EDAP/priority claims separately.
6. Then submit as either a technical report or workshop-style case study, not as a claimed mathematical advance.

## Final Grade

Current public version: B- as a technical narrative, C+ as an academic artifact, A- for self-critical honesty, D for public reproducibility.

After artifact release and wording fixes: potentially B+/A- as an AI-assisted mathematics case study, while remaining a modest elementary math note rather than a Collatz breakthrough.

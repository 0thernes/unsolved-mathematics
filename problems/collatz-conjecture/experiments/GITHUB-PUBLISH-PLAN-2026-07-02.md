# GitHub Publish Plan - Collatz Phase-Collision Integration

## Verdict

Do not publish the current worktree with `git add -A`.

The local checkout is on `main` with remote:

```text
origin https://github.com/0thernes/unsolved-mathematics.git
```

The worktree is heavily dirty and includes unrelated deletions, logs, sibling
problem edits, moved repo-audit docs, and a large untracked retimed-suite
population. A safe GitHub update should be scoped.

## Recommended Publish Unit

Publish the current four-share / phase-collision integration plus the
algorithm-catalog triage and 104-builder QA artifacts as one scoped branch or
commit:

```text
codex/collatz-phase-lock-integration
```

Files to include from repo root:

```text
problems/collatz-conjecture/README.md
problems/collatz-conjecture/FAILED-ATTEMPTS-WEIRDNESS-ATLAS-2026-07-05.md
problems/collatz-conjecture/status.md
problems/collatz-conjecture/experiments/AUDIT-REGISTER.md
problems/collatz-conjecture/experiments/README.md
problems/collatz-conjecture/experiments/results/INDEX.md
problems/collatz-conjecture/experiments/CHATGPT-SHARE-INGEST-2026-07-02.md
problems/collatz-conjecture/experiments/CHATGPT-SHARE-DEEP-ANALYSIS-2026-07-02.md
problems/collatz-conjecture/experiments/COLLATZ-PURSUIT-CURRENT-STATE-2026-07-02.md
problems/collatz-conjecture/experiments/COLLATZ-FAILED-IDEAS-ATLAS-2026-07-04.md
problems/collatz-conjecture/experiments/COLLATZ-FAILED-ATTEMPTS-ATLAS-2026-07-05.md
problems/collatz-conjecture/experiments/COLLATZ-WTF-ODDNESS-FIELD-GUIDE-2026-07-05.md
problems/collatz-conjecture/experiments/COLLATZ-BIZARRO-OMNILENS-AUDIT-2026-07-05.md
problems/collatz-conjecture/experiments/COLLATZ-EPSILON-LINT.md
problems/collatz-conjecture/experiments/COLLATZ-ALGORITHM-CATALOG-TRIAGE-2026-07-04.md
problems/collatz-conjecture/experiments/COLLATZ-ALGORITHM-ATTACK-MATRIX-2026-07-04.md
problems/collatz-conjecture/experiments/COLLATZ-BUILDER-104-QA-RUBRIC-2026-07-04.md
problems/collatz-conjecture/experiments/ALGORITHM-CATALOG-COLLATZ-TOOLING-ROADMAP-2026-07-04.md
problems/collatz-conjecture/experiments/SPINE-PHASE-COLLISION.md
problems/collatz-conjecture/experiments/GITHUB-PUBLISH-PLAN-2026-07-02.md
problems/collatz-conjecture/experiments/spine_phase_collision_lab.py
problems/collatz-conjecture/experiments/results/spine_phase_collision_lab_d12_20260702.json
problems/collatz-conjecture/experiments/collatz_epsilon_lint.py
problems/collatz-conjecture/experiments/results/collatz_epsilon_lint_20260705.json
problems/collatz-conjecture/experiments/results/MANIFEST.json
```

Because `experiments/results/` is ignored for new files, the dated lint result
must be force-added if it is included in the GitHub publish unit.

Optional second publish unit, after a separate audit:

```text
problems/collatz-conjecture/experiments/BRANCH-PREFIX-RETIMED-*.md
problems/collatz-conjecture/experiments/branch_prefix_retimed_*.py
problems/collatz-conjecture/experiments/results/branch_prefix_retimed_*.json
```

That second unit is large and should not be silently bundled with the
phase-collision integration.

Optional odd-unit transition publish unit, after the coverage/refinement files
are included or already present on the target branch:

```text
problems/collatz-conjecture/experiments/ODD-UNIT-LOCK-TRANSITION.md
problems/collatz-conjecture/experiments/ODD-UNIT-LOCK-TRANSITION-WITNESS-MICROSCOPE.md
problems/collatz-conjecture/experiments/ODD-UNIT-LOCK-BRIDGE-CLASSIFIER.md
problems/collatz-conjecture/experiments/ODD-UNIT-LOCK-BRIDGE-REFINEMENT.md
problems/collatz-conjecture/experiments/ODD-UNIT-LOCK-PERSISTENCE-LADDER.md
problems/collatz-conjecture/experiments/ODD-UNIT-LOCK-ALIGNMENT-DROP.md
problems/collatz-conjecture/experiments/odd_unit_lock_transition_lab.py
problems/collatz-conjecture/experiments/odd_unit_lock_transition_microscope.py
problems/collatz-conjecture/experiments/odd_unit_lock_transition_witness_microscope.py
problems/collatz-conjecture/experiments/odd_unit_lock_bridge_classifier.py
problems/collatz-conjecture/experiments/odd_unit_lock_bridge_refinement.py
problems/collatz-conjecture/experiments/odd_unit_lock_alignment_drop_analyzer.py
problems/collatz-conjecture/experiments/odd_unit_lock_coverage_lab.py
problems/collatz-conjecture/experiments/results/odd_unit_lock_transition_d13_N50000_20260705.json
problems/collatz-conjecture/experiments/results/odd_unit_lock_transition_microscope_d13_R16_N250000_20260705.json
problems/collatz-conjecture/experiments/results/odd_unit_lock_transition_microscope_d13_R17_N1000000_20260705.json
problems/collatz-conjecture/experiments/results/odd_unit_lock_transition_microscope_d13_R18_N1000000_20260705.json
problems/collatz-conjecture/experiments/results/odd_unit_lock_transition_microscope_d13_R19_N1000000_20260705.json
problems/collatz-conjecture/experiments/results/odd_unit_lock_transition_microscope_d13_R20_N250000_20260705.json
problems/collatz-conjecture/experiments/results/odd_unit_lock_transition_microscope_d13_R24_N250000_20260705.json
problems/collatz-conjecture/experiments/results/odd_unit_lock_bridge_classifier_d13_R16_N250000_20260705.json
problems/collatz-conjecture/experiments/results/odd_unit_lock_bridge_classifier_d13_R17_N1000000_20260705.json
problems/collatz-conjecture/experiments/results/odd_unit_lock_bridge_classifier_d13_R18_N1000000_20260705.json
problems/collatz-conjecture/experiments/results/odd_unit_lock_bridge_refinement_d13_R16_to_R20_R24_N250000_20260705.json
problems/collatz-conjecture/experiments/results/odd_unit_lock_bridge_refinement_d13_R17_to_R20_R24_N1000000_20260705.json
problems/collatz-conjecture/experiments/results/odd_unit_lock_bridge_refinement_d13_R18_to_R20_R24_N1000000_20260705.json
problems/collatz-conjecture/experiments/results/odd_unit_lock_alignment_drop_20260705.json
```

The transition and bridge result files are under ignored `experiments/results/`,
so publish them with `git add -f -- <path>`.

## Exclude From This Publish

Do not include:

```text
debug_field.log
defect_run*.log
defect_spectral_run.log
fdebug.log
final_clean.log
final_run.log
run_escalate.log
run_final.log
fix.py
fix_p18.py
results/
```

Do not include unrelated edits under:

```text
problems/goldbach-conjecture/
rag/
scripts/
docs/
```

Do not include the broad deleted-file set unless the user explicitly asks for
the whole dirty-tree cleanup to be published.

## Safe Command Sequence

From repo root:

```powershell
git switch -c codex/collatz-phase-lock-integration

git add -- `
  problems/collatz-conjecture/README.md `
  problems/collatz-conjecture/FAILED-ATTEMPTS-WEIRDNESS-ATLAS-2026-07-05.md `
  problems/collatz-conjecture/status.md `
  problems/collatz-conjecture/experiments/AUDIT-REGISTER.md `
  problems/collatz-conjecture/experiments/README.md `
  problems/collatz-conjecture/experiments/results/INDEX.md `
  problems/collatz-conjecture/experiments/CHATGPT-SHARE-INGEST-2026-07-02.md `
  problems/collatz-conjecture/experiments/CHATGPT-SHARE-DEEP-ANALYSIS-2026-07-02.md `
  problems/collatz-conjecture/experiments/COLLATZ-PURSUIT-CURRENT-STATE-2026-07-02.md `
  problems/collatz-conjecture/experiments/COLLATZ-FAILED-IDEAS-ATLAS-2026-07-04.md `
  problems/collatz-conjecture/experiments/COLLATZ-FAILED-ATTEMPTS-ATLAS-2026-07-05.md `
  problems/collatz-conjecture/experiments/COLLATZ-WTF-ODDNESS-FIELD-GUIDE-2026-07-05.md `
  problems/collatz-conjecture/experiments/COLLATZ-BIZARRO-OMNILENS-AUDIT-2026-07-05.md `
  problems/collatz-conjecture/experiments/COLLATZ-EPSILON-LINT.md `
  problems/collatz-conjecture/experiments/COLLATZ-ALGORITHM-CATALOG-TRIAGE-2026-07-04.md `
  problems/collatz-conjecture/experiments/COLLATZ-ALGORITHM-ATTACK-MATRIX-2026-07-04.md `
  problems/collatz-conjecture/experiments/COLLATZ-BUILDER-104-QA-RUBRIC-2026-07-04.md `
  problems/collatz-conjecture/experiments/ALGORITHM-CATALOG-COLLATZ-TOOLING-ROADMAP-2026-07-04.md `
  problems/collatz-conjecture/experiments/SPINE-PHASE-COLLISION.md `
  problems/collatz-conjecture/experiments/GITHUB-PUBLISH-PLAN-2026-07-02.md `
  problems/collatz-conjecture/experiments/spine_phase_collision_lab.py `
  problems/collatz-conjecture/experiments/results/spine_phase_collision_lab_d12_20260702.json `
  problems/collatz-conjecture/experiments/collatz_epsilon_lint.py `
  problems/collatz-conjecture/experiments/results/MANIFEST.json

git add -f -- `
  problems/collatz-conjecture/experiments/results/collatz_epsilon_lint_20260705.json

git commit -m "Add Collatz phase-collision integration audit"
git push -u origin codex/collatz-phase-lock-integration
```

If publishing directly to `main` is desired instead, use the same scoped
`git add -- <files>` list and still avoid `git add -A`.

## Verification Already Run

```powershell
python -m py_compile experiments\spine_phase_collision_lab.py
python experiments\spine_phase_collision_lab.py --max-depth 12 --identity-trials 5000 --output experiments\results\spine_phase_collision_lab_d12_20260702.json --quiet
python -m py_compile experiments\collatz_epsilon_lint.py
python experiments\collatz_epsilon_lint.py selftest --json
python experiments\collatz_epsilon_lint.py run --depth 12 --trace-depth 40 --out experiments\results\collatz_epsilon_lint_20260705.json
python experiments\build_results_manifest.py
git diff --check -- README.md status.md experiments\AUDIT-REGISTER.md experiments\README.md experiments\COLLATZ-PURSUIT-CURRENT-STATE-2026-07-02.md experiments\COLLATZ-EPSILON-LINT.md experiments\collatz_epsilon_lint.py experiments\results\INDEX.md experiments\results\MANIFEST.json
```

The lab output preserves the key status:

```text
identity checks: 5000
identity failures: 0
nonmatched valuation-rule failures: 0
```

No full-repo test suite was run because the broader checkout is already dirty
and contains unrelated changes.

# Eval — Gate Contract

Quality gates for the eval command's own behavior. These validate the eval loop execution — not the target artifact being tested.

## Step 0: Resolve Source

| ID | Check | Method | Pass Criteria | Fail Action |
|----|-------|--------|---------------|-------------|
| G0.1 | Mode detected | `mode` is `artifact` or `harness` | Non-null | Re-parse input arguments |
| G0.2 | Source resolved | `test -d` on resolved local path | Directory exists | If URL: retry clone. If local: abort with path not found. |
| G0.3 | Test repo name set | `test_repo_name` is non-empty string | Non-empty | Derive from source path or target name |

## Step 1: Create Test Repo

| ID | Check | Method | Pass Criteria | Fail Action |
|----|-------|--------|---------------|-------------|
| G1.1 | Test repo directory exists | `test -d evals/eval-[name]/` | Directory present | Create directory, retry |
| G1.2 | Git initialized | `test -d evals/eval-[name]/.git` | `.git/` exists | `git init`, retry |

## Step 2: Compile Harness

| ID | Check | Method | Pass Criteria | Fail Action |
|----|-------|--------|---------------|-------------|
| G2.1 | Protocol file exists | `test -f .claude/protocols/*-protocol.md` in test repo | At least one protocol file | Re-run domain-setup; if still fails, set `failed` with `resume_step: 2` |
| G2.2 | Hooks wired in settings | `grep -q "hooks" .claude/settings.local.json` in test repo | Hooks key present with entries | Re-run domain-setup; check hook registration |
| G2.3 | State files initialized | `test -f .claude/state/session_state.json` in test repo | State file exists | Re-run domain-setup |
| G2.4 | Kernel files present | `test -d .claude/commands/kernel/` in test repo | Kernel commands directory exists | Re-copy kernel source |

→ Contract: `contracts/step-02-contract.json`

## Step 3: Copy Artifact / Repo

### Artifact Mode

| ID | Check | Method | Pass Criteria | Fail Action |
|----|-------|--------|---------------|-------------|
| G3.1 | Artifact SKILL.md exists | `test -f` target artifact's main file in test repo | File present | Re-copy from source repo |
| G3.2 | File index references resolve | For each wikilink in SKILL.md, `test -f` the target | All linked files exist in test repo | Copy missing files from source repo |
| G3.3 | No broken wikilinks | Scan all copied `.md` files for `→` links, verify each resolves | Zero broken links | Identify missing file, copy or log gap |

### Harness Mode

| ID | Check | Method | Pass Criteria | Fail Action |
|----|-------|--------|---------------|-------------|
| G3.1h | Harness directory exists | `test -d <test-repo>/harness-under-test/` | Directory present | Re-copy source repo |
| G3.2h | CLAUDE.md present | `test -f <test-repo>/harness-under-test/CLAUDE.md` | File present | Re-copy |
| G3.3h | Commands present | `ls <test-repo>/harness-under-test/.claude/commands/` | Non-empty | Re-copy |
| G3.4h | No .git leaked | `test ! -d <test-repo>/harness-under-test/.git` | Absent | Delete .git/ |

-> Contract: `contracts/step-03-contract.json`

## Step 4: Component Check

| ID | Check | Method | Pass Criteria | Fail Action |
|----|-------|--------|---------------|-------------|
| G4.1 | Component check completed | Agent scanned `_reference/` in platform-deepeval | Scan log produced (list of found components) | Log warning, create components from scratch |
| G4.2 | Decision log produced | Agent documented reuse vs. create decisions | At least one decision entry (component name + action taken) | Agent must document decisions before proceeding |

## Step 5: Generate Tests

| ID | Check | Method | Pass Criteria | Fail Action |
|----|-------|--------|---------------|-------------|
| G5.1 | conftest.py exists | `test -f` conftest.py in test suite directory | File present | Generate conftest.py with fixtures |
| G5.2 | At least one test file | `ls test_*.py` or `ls *_test.py` in test directory | At least one match | Re-analyze artifact, generate tests |
| G5.3 | Fixtures loadable | `python -c "import conftest"` or pytest collect | No import errors | Fix conftest.py imports |
| G5.4 | Metrics selected | Test files reference at least one DeepEval metric | `grep -l "Metric\|metric" test_*.py` returns results | Agent must select metrics based on artifact analysis |

→ Contract: `contracts/step-05-contract.json`

## Step 6: Run and Score

| ID | Check | Method | Pass Criteria | Fail Action |
|----|-------|--------|---------------|-------------|
| G6.1 | Scored report exists | `test -f eval/results/report.json` in test repo | File present with valid JSON | Re-run `deepeval test`; if infra issue, set `failed` with `resume_step: 6` |
| G6.2 | All metrics have scores | Parse report.json, check each metric has numeric `score` | No null or missing score values | Re-run failed metrics individually |
| G6.3 | Score history updated | `test -f eval/results/score-history.json` in source repo | File present, latest entry matches current run | Append current scores to history |

→ Contract: `contracts/step-06-contract.json`

## Step AB-1: Generate Variants

| ID | Check | Method | Pass Criteria | Fail Action |
|----|-------|--------|---------------|-------------|
| GAB1.1 | Flat variant exists | `test -f flat/artifact-flat.md` | File present | Re-run generator |
| GAB1.2 | Tiered variant exists | `test -d tiered/` | Directory present with files | Re-copy from source |

## Step AB-3: Run Iterations

| ID | Check | Method | Pass Criteria | Fail Action |
|----|-------|--------|---------------|-------------|
| GAB3.1 | All output files exist | Check N*2 files (N iterations x 2 variants) | All present | Re-run failed iterations |
| GAB3.2 | No empty outputs | `wc -l` > 0 for each output file | Non-empty | Re-run empty outputs |

## Step AB-5: Compare Report

| ID | Check | Method | Pass Criteria | Fail Action |
|----|-------|--------|---------------|-------------|
| GAB5.1 | Report exists | `test -f ab-report.md` | File present | Re-generate report |
| GAB5.2 | Verdict valid | Value is one of: `flat_wins`, `tiered_wins`, `no_difference` | Valid verdict | Re-compute from scores |

## Gate Enforcement

- Each step's gates are checked **before** transitioning to the next state
- If any gate fails: apply the Fail Action, then re-check
- If a gate fails after retry: set state to `failed` with appropriate `resume_step`
- On any failure that sets `failed`: invoke `/kernel/learn` before stopping

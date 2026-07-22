# Eval — Skill

**Type:** Prescriptive
**Style:** Indexed — SKILL.md + steps/ + references/ + contracts/

## Identity

You are the eval agent. You test LLM artifacts using DeepEval. You take any command, skill, harness, or agent workflow, isolate it in a test repo with a compiled harness, dynamically build evaluation tests, run them, and produce scored reports.

## Vocabulary

| Term | Meaning |
|------|---------|
| **Harness compilation** | Assembling kernel + platform-deepeval + running domain-setup to produce a fully initialized test environment |
| **Harness mode** | Eval mode where the entire source repo is tested as a system — loop integrity, hook coverage, skill completeness, command quality |
| **Artifact mode** | Eval mode where a single command/skill/artifact is tested in isolation (original behavior) |
| **Source resolution** | Detecting whether input is a local path or GitHub URL and resolving to a local directory |
| **Golden dataset** | Input/expected-output pairs that exercise a specific artifact's behavior |
| **Component check** | Scanning platform-deepeval _reference/ to find existing metrics, tests, or tasks before creating new ones |
| **Artifact isolation** | Copying the target artifact + all its dependencies into the test repo so nothing resolves outside the repo |
| **Scored report** | Per-metric scores, pass/fail, thresholds — the eval's output artifact |
| **Framework growth** | New components created during eval follow _reference/ patterns and can merge back to master platform-deepeval |
| **A/B mode** | Eval mode comparing flat vs tiered variants of the same artifact across N runs |
| **Variant** | A specific structural presentation of the same content (flat or tiered) |
| **Paired comparison** | Scoring both variants with identical metrics per run |

## Workflow Summary

| Step | Action | File |
|------|--------|------|
| 0 | Resolve source + detect mode | → `steps/step-00-resolve-source.md` |
| 1 | Create test repo | → `steps/step-01-create-test-repo.md` |
| 2 | Compile harness (kernel + platform-deepeval + domain-setup) | → `steps/step-02-compile-harness.md` |
| 3 | Copy artifact (artifact mode) or entire repo (harness mode) | → `steps/step-03-copy-artifact.md` |
| 4 | Dynamic component check | → `steps/step-04-component-check.md` |
| 5 | Generate deepeval tests | → `steps/step-05-generate-tests.md` |
| 6 | Run and score | → `steps/step-06-run-and-score.md` |
| AB-1 | Generate variants (flat + tiered) | → `steps/step-ab-1-generate-variants.md` |
| AB-2 | Build prompt per variant | → `steps/step-ab-2-build-prompt.md` |
| AB-3 | Run iterations (N runs per variant) | → `steps/step-ab-3-run-iterations.md` |
| AB-4 | Score outputs (paired comparison) | → `steps/step-ab-4-score-outputs.md` |
| AB-5 | Compare and report | → `steps/step-ab-5-compare-report.md` |

## File Index

| Layer | File | Purpose |
|-------|------|---------|
| Command | `.claude/commands/kernel/eval.md` | Entry point, usage, examples |
| Skill | `SKILL.md` (this file) | Identity, vocabulary, workflow summary |
| Workflow | → `workflow.md` | State machine, loop behavior, error handling, resume |
| Gates | → `gate-contract.md` | Quality gates for the eval command itself |
| Steps | → `steps/step-00-resolve-source.md` | Resolve source (local/GitHub) + detect mode |
| Steps | → `steps/step-01-create-test-repo.md` | Create disposable test repo |
| Steps | → `steps/step-02-compile-harness.md` | Compile kernel + platform-deepeval + domain-setup |
| Steps | → `steps/step-03-copy-artifact.md` | Copy artifact + resolve all dependencies |
| Steps | → `steps/step-04-component-check.md` | Check _reference/, create missing components |
| Steps | → `steps/step-05-generate-tests.md` | Generate pytest eval suite |
| Steps | → `steps/step-06-run-and-score.md` | Execute tests, produce scored report |
| Steps | → `steps/step-ab-1-generate-variants.md` | Generate flat + tiered variants |
| Steps | → `steps/step-ab-2-build-prompt.md` | Build prompt per variant |
| Steps | → `steps/step-ab-3-run-iterations.md` | Run N iterations per variant |
| Steps | → `steps/step-ab-4-score-outputs.md` | Score outputs with paired comparison |
| Steps | → `steps/step-ab-5-compare-report.md` | Compare variants and produce report |
| References | → `references/INDEX.md` | Index of all reference payloads |
| References | → `references/step-00/source-resolution.md` | GitHub clone + local path detection |
| Contracts | → `contracts/step-02-contract.json` | Harness compilation gate |
| Contracts | → `contracts/step-03-contract.json` | Artifact isolation gate |
| Contracts | → `contracts/step-05-contract.json` | Test generation gate |
| Contracts | → `contracts/step-06-contract.json` | Scoring gate |

## Critical Rules

1. **Read _reference/ before creating new components.** The platform-deepeval _reference/ directory contains patterns for metrics, tests, golden datasets, and tasks. Always check what exists before building new. Duplicate components waste time and break merge paths.

2. **Test repo is disposable.** Every eval creates a fresh test repo at `D:\my_ai_projects\project_test_repos\evals\eval-[name]\`. It can be deleted after scoring. Never test in-place.

3. **Adapt to what you're testing.** The eval agent dynamically decides which metrics, golden datasets, and test structures to use based on the target artifact. There is no hardcoded pipeline — the agent reads the artifact, understands what it does, and builds appropriate tests. In harness mode, the "artifact" is the entire repo.

4. **Contracts validate eval's own behavior, not the target.** Step contracts verify that the eval command executed correctly (harness compiled, artifact isolated, tests generated, scores produced). The target artifact's quality is measured by the scored report.

5. **200-line threshold.** No file exceeds 200 lines. If a section grows past this, extract it into a sub-file and link to it.

6. **Mode is detected, not configured.** One arg = harness mode, two args = artifact mode. The agent never asks the user which mode — it reads the input and decides.

7. **A/B mode isolates structure as the variable.** Flat and tiered variants MUST have identical content — only organization differs.

## Composability

| Caller | How |
|--------|-----|
| **Standalone** | `/kernel/eval check-data D:\...\hmsa-healthcare-qa` |
| **Task builder** | After BUILD tasks, run eval against the output |
| **Audit workflow** | Verify an LLM artifact scores above thresholds |
| **CI/automation** | `run-task.sh` task invokes eval via `claude -p` |

When called by another command, output the scored report path so the caller can read it.

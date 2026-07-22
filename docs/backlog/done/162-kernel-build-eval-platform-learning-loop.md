# Eval Platform Learning Loop — Move Harness Eval to platform-deepeval

## Status
Open

## Priority
High — this is the feedback loop that makes the eval platform smarter after each test run. Core moat.

## Summary
Move the harness eval system (harness_metrics.py, architecture_notes.py, criteria_changelog.md, test_eval_kernel_minimal.py) from the disposable eval-kernel-minimal-test repo into platform-deepeval as a permanent capability. Separate universal criteria from per-harness architecture notes, pass notes via LLMTestCase.context so the judge gets informed context without polluted criteria. Parameterize the harness path so the same test suite can evaluate any harness, not just kernel-minimal.

## Requirements
- Move 4 files from eval-kernel-minimal-test to platform-deepeval (framework/metrics/ and tests/)
- Criteria stay universal and architecture-agnostic (no baked-in "Note:" clauses)
- Architecture notes are separate, loaded per-harness, passed via LLMTestCase.context
- GEval metrics use `use_context=True` when notes exist, `use_context=False` when they don't
- Harness path is parameterized (conftest fixture or CLI arg) — not hardcoded to isagawa-kernel
- criteria_changelog.md tracks every criteria refinement with: what failed, classification (defect vs criteria flaw), what changed
- 17/17 tests pass when run from platform-deepeval pointing at isagawa-kernel as target harness
- Consistent with existing _reference/metrics/ patterns in platform-deepeval

## References
- Source: `D:\my_ai_projects\project_test_repos\eval-kernel-minimal-test\framework\metrics\`
- Source: `D:\my_ai_projects\project_test_repos\eval-kernel-minimal-test\tests\test_eval_kernel_minimal.py`
- Destination: `D:\my_ai_projects\project_test_repos\platform-deepeval`
- Existing patterns: `platform-deepeval/framework/_reference/metrics/custom_metrics.py`
- Backlog 157: deepeval command testing (prior eval work)
- Backlog 154: deepeval L3 testing (prior eval work)

## Task Builder Input
- **Deliverable:** Harness eval system in platform-deepeval with parameterized harness path, architecture notes via context, and criteria changelog
- **Location:** new-repo:D:\my_ai_projects\project_test_repos\platform-deepeval
- **Scope:** BUILD
- **Constraints:** Must preserve existing platform-deepeval structure. Must not break existing tests. Conftest must resolve harness_root dynamically (env var or pytest CLI option).

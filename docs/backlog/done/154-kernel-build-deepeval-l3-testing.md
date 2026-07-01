# DeepEval L3 Testing: Industry-Standard Benchmarks for Kernel Commands

## Status
Open

## Priority
High — L3 testing currently has no quantifiable scoring. All pieces exist (prod-test, platform-deepeval, contract JSONs). Composition unlocks stakeholder-ready metrics and regression tracking for every kernel command.

## Summary

Enhance `/kernel/prod-test` L3 to use platform-deepeval as the evaluation engine. When prod-test runs against a deliverable, L3 composes the deepeval spec into the test repo, translates contract JSONs to golden datasets, auto-generates an eval suite (Agent pipeline: ToolCorrectness, TaskCompletion, GEval for protocol faithfulness), runs it, and produces scored reports. Scores are tracked across iteration passes so progression is visible.

All pieces exist. prod-test does master → test repo isolation. platform-deepeval does metric selection and eval suite generation. Contract JSONs define expected behaviors declaratively. They need composition, not new invention.

## Architecture

```
/kernel/prod-test [repo]
    │
    ├── Steps 1-5: unchanged (assemble, domain-setup, copy, infra)
    │
    ├── Step 6: Write inner tasks
    │   ├── L1: structural (file exists, schema valid)
    │   ├── L2: functional (run command, verify output)
    │   └── L3: deepeval eval suite (NEW)
    │       ├── Compose platform-deepeval spec into test repo
    │       ├── Domain-setup recognizes Agent pipeline
    │       ├── Translate contract JSONs → golden dataset
    │       ├── Generate eval suite (metrics auto-selected)
    │       └── Run deepeval test → scored report
    │
    ├── Step 7: Execute all (L1 → L2 → L3)
    └── Step 8: Collect report with DeepEval scores
```

## Iteration Model

```
backlog → task-builder → cycle → prod-test → gaps?
                                                │
                                   yes ─────────┤──── no → done
                                                │
                                         /kernel/learn
                                                │
                                         update backlog
                                                │
                                         task-builder (gap tasks)
                                                │
                                         cycle again → prod-test ...
```

Each pass builds what's missing, tests what's built, learns from failures. Scores tracked per pass ("Pass 1: 0.62 TaskCompletion. Pass 3: 0.91.").

## Design Documents

| Document | Purpose |
|----------|---------|
| [[154-kernel-build-deepeval-l3-testing/composition-architecture]] | How prod-test composes platform-deepeval into the test repo structure |
| [[154-kernel-build-deepeval-l3-testing/golden-dataset-translator]] | Contract JSON → DeepEval golden dataset schema mapping |
| [[154-kernel-build-deepeval-l3-testing/agent-output-capture]] | How to capture command output (files, state, reasoning) as DeepEval actual_output |
| [[154-kernel-build-deepeval-l3-testing/metric-mapping]] | Which DeepEval metrics map to kernel command evaluation, custom GEval criteria |
| [[154-kernel-build-deepeval-l3-testing/iteration-tracking]] | Score tracking across passes, progression reporting, regression detection |
| [[154-kernel-build-deepeval-l3-testing/design-decisions]] | Resolved and open design decisions |

## Requirements

- prod-test Step 6 L3 must compose platform-deepeval spec into test repo
- Contract JSONs must translate mechanically to golden datasets (no manual fixture creation)
- Agent output capture must work for any command (not just check-data)
- Eval suite auto-generated from pipeline type + contract structure
- Scored reports include per-metric scores, pass/fail, triage recommendations
- Scores trackable across iterations for progression visibility
- Must not break existing L1/L2 testing
- First target: check-data command in hmsa-healthcare-qa

## References

- prod-test skill: `.claude/skills/prod-test/SKILL.md`
- platform-deepeval spec: `D:\my_ai_projects\project_test_repos\platform-deepeval\.claude\skills\deepeval-management-layer\SKILL.md`
- platform-deepeval framework: `D:\my_ai_projects\project_test_repos\platform-deepeval\FRAMEWORK.md`
- Example contracts: `D:\my_ai_projects\project_test_repos\hmsa-healthcare-qa\.claude\skills\check-data\contracts\`
- Backlog 153 (reference scanner): `docs/backlog/153-kernel-build-reference-scanner.md`

## Task Builder Input
- **Deliverable:** Enhanced prod-test L3 with DeepEval integration + golden dataset translator
- **Location:** workspace:.claude/skills/prod-test/ (L3 enhancement) + workspace:framework/ (translator)
- **Scope:** BUILD
- **Constraints:** Must compose existing systems (prod-test + platform-deepeval), not rebuild. Contract JSONs are the bridge. First target: check-data. Agent pipeline type for kernel commands.

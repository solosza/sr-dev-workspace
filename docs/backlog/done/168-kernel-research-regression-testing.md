# Research: Regression Testing for Protocol and Hook Changes

## Status
Open

## Priority
High — changes currently ship without automated regression; eval platform exists but isn't wired in

## Summary
Research how to wire the eval platform (platform-deepeval) into the kernel's learn/anchor cycle so that protocol and hook changes are automatically regression-tested before being adopted. Currently when /kernel/learn modifies a hook or protocol, the change ships without any automated verification that it didn't break something. The eval platform could serve as a regression gate — run the eval suite after every learn event, block the change if tests regress.

## Requirements
- Research how to trigger platform-deepeval tests from within the kernel loop (after /kernel/learn completes)
- Research what "regression" means in this context: which eval tests constitute a regression gate?
- Research the integration point: should regression run inside /kernel/learn, as a post-learn hook, or as a separate command?
- Research performance: how fast can the eval suite run? Is it feasible to run on every learn event or only periodically?
- Research the failure path: what happens if regression tests fail after a learn event? Block? Warn? Rollback?
- Research how to distinguish "eval test was already failing" from "this change caused it to fail"
- Consider: should the eval suite have a "smoke test" subset for fast regression vs full suite for periodic runs?

## References
- `D:/my_ai_projects/project_test_repos/platform-deepeval/` — existing eval platform (15/16 tests passing)
- `.claude/commands/kernel/learn.md` — current learn command (modifies hooks/protocol)
- `.claude/hooks/` — hook files that get modified
- Backlog 164-167 (metrics, experiments, auto-eval, rollback — related capabilities)
- CI/CD regression testing patterns

## Task Builder Input
- **Deliverable:** Research report with regression testing architecture and integration plan
- **Location:** subproject:kernel-regression-testing-research
- **Scope:** RESEARCH
- **Constraints:** Must work with existing eval platform. GEval tests require OPENAI_API_KEY (structural tests don't). Consider cost of running LLM-as-judge on every learn event.

# Per-Step Postcondition Contract — Verify Every Step at the Boundary

## Status
Open

## Priority
High — verification-at-the-boundary is the single highest-leverage reliability lever (proven this session). This makes it a first-class, declarative contract instead of ad-hoc per-runner code.

## Summary
A per-step (and per-task) **postcondition contract**: each step declares the exact evidence that proves it actually happened — output artifact path(s), non-empty, and where applicable a schema/shape or a passing check — and the runner accepts completion **only when the postcondition holds**. This generalizes the 281 completion-truth fix (`check_step_output`) from hand-written per-step bash into a declarative contract the runner reads and enforces uniformly. An agent's `STEP_COMPLETE`/`ONE_SHOT_COMPLETE` signal becomes advisory; the postcondition is authoritative.

## Evidence (this session)
- The 281 completion-truth check caught a false-complete (no artifact) and a wrong-path `SKILL.md` — but only because someone hand-wrote `check_step_output` for each of the 12 steps. A declarative contract makes that coverage automatic and consistent, and portable to `run-task.sh` tasks (which had no such check — the swarm agent false-completed 1/3 tasks unchecked).
- Agents signal completion untruthfully as a matter of course; the boundary check is what makes that safe.

## Requirements
- **Declarative postcondition per step/task:** e.g. `{ "artifact": "output/{domain}/.claude/skills/*/SKILL.md", "must_exist": true, "non_empty": true, "schema": null | "<ref>" }`. Support glob, multiple artifacts, and an optional `verify_cmd`/gate for run_code checks.
- **Runner enforcement:** the runner reads the postcondition and treats the step complete ONLY if it holds — replacing/backing the current `check_step_output`. Signal alone never advances.
- **Generalize to run-task.sh:** tasks declare a postcondition (the expected deliverable) so completion-truth covers ordinary pipelines, not just the factory. (The swarm 288 false-complete would have been caught.)
- **Schema validation option:** for JSON/structured artifacts, validate shape — so an empty/malformed artifact fails the postcondition even if the file exists.
- **Authoring:** postconditions live with the step/task (step frontmatter or the task file / gate-contract), so they travel with the spec and are visible to the builder.

## References
- 281 completion-truth (`run-spec-factory.sh` `check_step_output`) — the hand-written precursor this formalizes.
- The reliability framework 2026-07-23: "contracts → make them checkable, not longer." This is that lever.
- Pairs with [[290-kernel-build-subagent-output-sandbox-hook]] (prevention) and worktree isolation (123/271).

## Task Builder Input
- **Deliverable:** A declarative per-step/per-task postcondition schema + runner enforcement in `domain-spec-factory` (`run-spec-factory.sh`, step frontmatter) and a parallel hook into `run-task.sh` task completion, with tests proving a false-complete (signal + missing/empty/malformed artifact) is rejected and a real completion passes.
- **Location:** new-repo:D:\my_ai_projects\project_test_repos\domain-spec-factory
- **Scope:** BUILD
- **Constraints:** Back-compatible with existing `check_step_output`/gate-contract. Keep the runner as the sole verifier (agent signal is advisory). Port the run-task.sh variant to kernel-minimal after it proves out.

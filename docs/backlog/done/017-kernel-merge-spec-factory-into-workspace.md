# Merge Spec Factory into SR Dev Workspace

## Status
Done

## Priority
Medium — consolidates tooling into single workspace

## Summary
The domain-spec-factory currently lives in its own repo (`C:/Users/solos/my_ai_projects/domain-spec-factory`). Merge its capabilities into the sr-dev-workspace so spec generation, task building, and autonomous cycling all live in one place. The factory becomes a skill or task set within this workspace rather than a separate repo.

## Why
- One workspace to rule them all — no context switching between repos
- Task-builder + spec-factory are complementary (task-builder decomposes goals, factory generates specs)
- Kernel enforcement applies to factory output
- Simpler headless execution — one repo, one run-task.sh

## Steps
- [ ] Audit domain-spec-factory repo: what files exist, what does it do, what's the workflow
- [ ] Identify what to bring over: skills, commands, templates, research output
- [ ] Determine structure: does it become a skill (`/.claude/skills/spec-factory/`), a task set (`tasks/spec-factory/`), or both?
- [ ] Copy relevant files into sr-dev-workspace
- [ ] Wire into protocol, CLAUDE.md
- [ ] Test: can we generate a spec from this workspace using the factory?
- [ ] Archive or deprecate the standalone factory repo

## Considerations
- Don't duplicate — reference, don't copy if possible
- Factory output (generated specs) should go to their own repos, not clutter this workspace
- The meta-spec templates should be accessible as references

## Task Builder Input
- **Deliverable:** Spec factory capabilities integrated into sr-dev-workspace (as skill, command, or task set), standalone factory repo archived
- **Scope:** REFACTOR
- **Constraints:** Audit factory repo first. Don't duplicate — reference where possible. Factory output goes to separate repos. Wire into protocol + CLAUDE.md.

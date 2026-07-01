# Write step-03-copy-artifact.md

## Context
Layer 3 step file for artifact isolation. Copies the target LLM artifact and all its dependencies into the test repo so it can be tested in complete isolation. The agent must dynamically determine what to copy based on what the artifact IS.

## Type
BUILD

## Execution
inline

## Dependencies
- None

## Requirements
- File: `.claude/skills/eval/steps/step-03-copy-artifact.md`
- Must contain:
  - **What to do**: identify artifact type, copy full package (skills, commands, design docs, hooks, referenced data)
  - **Pre-generation checkpoint**: read `references/step-03/dependency-resolution.md` for resolution strategy
  - **What to produce**: self-contained artifact in test repo — every file the LLM would read during execution exists
  - **Artifact type table**: command, skill, harness, agent workflow — what gets copied for each
  - **Dependency resolution**: scan SKILL.md file index, step file references, contract schemas for external paths; copy all
  - **Verification**: all files in SKILL.md file index exist in test repo, all step file references resolve, all contract JSONs parse, no broken wikilinks
  - **Error handling**: if a referenced file doesn't exist in source, log warning and continue (some references may be optional)
  - **What NOT to copy**: source repo's kernel, protocol, state, run history, domain-specific data files not referenced by artifact
- Source material: `docs/backlog/157-kernel-build-deepeval-command-testing/artifact-isolation.md`
- Must be under 200 lines

## Acceptance Criteria
- [ ] File exists at `.claude/skills/eval/steps/step-03-copy-artifact.md`
- [ ] `grep -q "dependency-resolution" .claude/skills/eval/steps/step-03-copy-artifact.md` passes
- [ ] `grep -q "SKILL.md" .claude/skills/eval/steps/step-03-copy-artifact.md` passes
- [ ] File is under 200 lines

## Gates Satisfied
BUILD-07

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.

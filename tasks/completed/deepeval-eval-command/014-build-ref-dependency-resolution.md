# Write step-03/dependency-resolution.md

## Context
Layer 4 reference payload for Step 3 (Copy Artifact). Defines how to scan the target artifact's files and resolve all external references so the artifact is fully self-contained in the test repo.

## Type
BUILD

## Execution
inline

## Dependencies
- None

## Requirements
- File: `.claude/skills/eval/references/step-03/dependency-resolution.md`
- Must contain:
  - **Scan order**: (1) SKILL.md file index, (2) each step file's References section, (3) contract JSONs for referenced schemas/data, (4) design docs for external paths
  - **Resolution strategy**: for each external path found, copy the file/directory into the test repo preserving relative structure
  - **Artifact type table**: what to scan for each artifact type (command, skill, harness, agent workflow)
  - **Verification checklist**: all file index entries exist, all step references resolve, all contract JSONs parse, no broken wikilinks
  - **Edge cases**: circular references (skip already-copied), optional references (log warning), paths that don't exist (log warning and continue)
- Source material: `docs/backlog/157-kernel-build-deepeval-command-testing/artifact-isolation.md` (Dependency Resolution section)
- Must be under 200 lines

## Acceptance Criteria
- [ ] File exists at `.claude/skills/eval/references/step-03/dependency-resolution.md`
- [ ] `grep -q "SKILL.md" .claude/skills/eval/references/step-03/dependency-resolution.md` passes
- [ ] `grep -q "wikilink" .claude/skills/eval/references/step-03/dependency-resolution.md` OR `grep -q "reference" .claude/skills/eval/references/step-03/dependency-resolution.md` passes
- [ ] File is under 200 lines

## Gates Satisfied
BUILD-14

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.

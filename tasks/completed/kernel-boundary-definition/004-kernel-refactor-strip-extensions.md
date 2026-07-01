# Document Extension Separation Plan

## Context
Identify all extensions currently in the kernel namespace and document how they should be separated. This is the actionable plan for removing non-governance items from isagawa-kernel.

## Type
BUILD

## Execution
inline

## Dependencies
- 002-kernel-build-kernel-manifest

## Phase Gate
- [ ] `D:/my_ai_projects/isagawa-kernel/kernel-manifest.json` exists

## Requirements
- Create `projects/kernel-boundary/extension-list.md`
- List every file in isagawa-kernel that is NOT in kernel-manifest.json
- For each extension: name, type (skill/command/both), current location, recommendation (remove from kernel repo or move to extensions/)
- Reference docs/backlog/147-kernel-refactor-define-kernel-boundary/extension-separation.md for the options analysis
- Include a recommendation on Option A (extensions repo), B (workspace-local), or C (extensions/ dir in kernel)

## Acceptance Criteria
- [ ] File exists: `projects/kernel-boundary/extension-list.md`
- [ ] Every non-manifest file in isagawa-kernel is listed
- [ ] Each extension has a recommendation
- [ ] Option A/B/C recommendation included with rationale

## Gates Satisfied
- BUILD-03

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.

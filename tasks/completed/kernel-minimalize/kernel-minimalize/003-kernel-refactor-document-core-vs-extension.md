# Document Core vs Extension Classification

## Context
Create a reference document that classifies every kernel component as core or extension. This is the authoritative source for what belongs in the kernel repo vs what stays in workspaces.

## Type
BUILD

## Execution
inline

## Dependencies
- 001-kernel-build-feature-freeze-policy

## Phase Gate
- [ ] `docs/kernel-feature-freeze-policy.md` exists

## Requirements
- Create `docs/kernel-core-vs-extension.md`
- Table format: Component | Type | Classification | Rationale
- Cover all commands, hooks, skills, and scripts
- Reference the kernel-manifest.json from backlog 147 if it exists
- Align with feature freeze policy from task 001

## Acceptance Criteria
- [ ] File exists: `docs/kernel-core-vs-extension.md`
- [ ] Every command classified as core or extension
- [ ] Every hook classified
- [ ] Every skill classified

## Gates Satisfied
- BUILD-02

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.

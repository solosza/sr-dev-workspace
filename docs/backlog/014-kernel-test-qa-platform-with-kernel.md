# Test QA Platform in Dev Workspace With Kernel

## Status
Open

## Priority
Medium — depends on backlog 013 (without kernel) passing first

## Summary
Pull the QA platform (isagawa-qa/platform-selenium) into a fresh dev workspace, install the Isagawa Kernel, run `/kernel/domain-setup`, and verify the full integration works — kernel enforcement, hook firing, learn loop, autonomous cycling against platform tasks.

## Why
This is the real product test. A user installs the kernel into their existing project and gets enforcement, learning, and autonomous execution. If this doesn't work smoothly, the kernel isn't ready for distribution.

## Dependencies
- Backlog 013 — QA platform confirmed working standalone

## Steps
- [ ] Use an existing dev workspace that already has the kernel installed (e.g., sr-dev-workspace) — don't create a fresh repo. The test is: can a user drop the QA platform into a workspace where the kernel is already running?
- [ ] Clone `isagawa-qa/platform-selenium` into the workspace
- [ ] Kernel is already present — no install needed
- [ ] Run `/kernel/domain-setup` — verify it discovers platform patterns and builds protocol
- [ ] Restart for hooks to load
- [ ] Run `/kernel/anchor` — verify protocol reads correctly
- [ ] Create a simple task (e.g., "generate eval suite for login page")
- [ ] Run `/kernel/autonomous-cycle` — verify task completes under enforcement
- [ ] Trigger a test failure — verify learn loop fires
- [ ] Run `/kernel/audit-workflow` — verify clean audit
- [ ] Test headless: run `bash run-task.sh` with a task — verify one-shot works
- [ ] Test batch: run `bash run-task-batch.sh` — verify batch works
- [ ] Document integration issues, friction points, missing pieces

## Success Criteria
- Domain-setup completes without errors
- Hooks fire correctly (counter increments, gates block)
- Agent completes a task under kernel enforcement
- Learn loop triggers on test failure
- Audit-workflow reports clean (or identifies real gaps)
- Both headless scripts work against the platform
- No kernel files conflict with platform files

## Task Builder Input
- **Deliverable:** Integration test report — domain-setup results, hook firing, cycling, learn loop, headless execution, friction points
- **Scope:** TEST
- **Constraints:** Use existing dev workspace with kernel installed. Depends on backlog 013 passing first. Needs restart after domain-setup (HUMAN REQUIRED for restart).

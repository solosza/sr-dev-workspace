# Install Kernel + Audit Job Application Spec

## Status
Open

## Priority
Medium — spec exists, needs kernel integration then gap audit

## Summary
The job-application-spec repo (`C:\Users\solos\my_ai_projects\job-application-spec`) has a well-structured skill (SKILL.md, workflow.md, 5 reference files, 1 command). The spec defines the blueprint but has no kernel infrastructure. Install the kernel, run domain-setup to build protocol from the spec, then audit for gaps — the domain-setup output will reveal what the spec actually missed vs what it promised.

Auditing the spec in isolation is premature. The real gaps surface after domain-setup builds the protocol, hooks, and state — then we can measure the spec against a running system.

## Steps

### Phase 1: Install Kernel
- [ ] Copy kernel files (CLAUDE.md, .claude/commands/, .claude/hooks/, .claude/skills/kernel-*, .claude/settings.local.json) into job-application-spec repo
- [ ] Run `/kernel/domain-setup` — let it discover the job-application skill and build the protocol
- [ ] Restart for hooks to load
- [ ] Run `/kernel/anchor` — verify protocol reads correctly

### Phase 2: Post-Setup Audit
- [ ] Run `/kernel/audit-workflow` — scan for infrastructure gaps
- [ ] Test `/job-apply` with a dry-run against a real job posting URL
- [ ] Identify gaps across 5 categories:
  - **Implementation:** What's missing from the kernel integration?
  - **Workflow:** Which steps fail or have no error recovery?
  - **Data Mapping:** Which form fields can't be mapped to profile?
  - **Decision Logic:** Where does the agent guess instead of having a rule?
  - **Application Boundaries:** What external factors break the workflow?
- [ ] Generate fix tasks from audit findings

### Phase 3: Fix + Validate
- [ ] Execute fix tasks via `/kernel/task-builder`
- [ ] Re-run dry-run test
- [ ] Verify all gaps closed

## Preliminary Gap Notes (from spec read — to be validated post-setup)
- No CLAUDE.md, no kernel infrastructure, no hooks wired
- Field mapping table only has ~13 labels (real forms have 30+)
- Fuzzy matching algorithm undefined
- No confidence threshold for auto-fill vs HITL
- No authentication/credential management for login-required sites
- No anti-bot detection strategy beyond CAPTCHA flagging
- No application history log

These are observations from reading the spec files — the real audit happens after domain-setup.

## References
- Spec repo: `C:\Users\solos\my_ai_projects\job-application-spec`
- Pattern: same as backlog 013/014 (QA platform with/without kernel)
- Existing files: SKILL.md, workflow.md, 5 references, 1 command, .mcp.json

## Task Builder Input
- **Deliverable:** Kernel installed, domain-setup complete, post-setup audit report, fix tasks generated and executed
- **Scope:** BUILD + TEST
- **Constraints:** Target repo is job-application-spec. Needs restart after domain-setup (HUMAN REQUIRED). Playwright MCP must be configured for dry-run test. HUMAN REQUIRED for profile.json setup.

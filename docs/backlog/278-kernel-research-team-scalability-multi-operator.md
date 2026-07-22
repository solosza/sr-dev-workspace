# Team Scalability — Beyond Bus-Factor-1 (Multi-Operator Kernel)

## Status
Open

## Priority
Medium — strategic, not urgent. The kernel is powerful but single-operator; the industry's AI-engineering ROI story is org-level (57% of orgs run agents for multi-stage workflows; the value case is teams, not individuals). If the kernel/platforms are to be adopted (HMSA, others), they must work for more than one person.

## Summary
The whole system currently assumes one operator (the author) driving from one workspace with deep tacit context. That's a bus-factor of 1 and a ceiling on adoption. Research what it takes to make the kernel usable by a *team*: shared state without contention, onboarding a new operator into the loop/discipline, role separation, and concurrent multi-operator work — so a platform like platform-hybrid can be handed to HMSA engineers and actually run.

## Requirements
- **Onboarding path:** what does a new operator need to become productive in the kernel loop (session-start → anchor → work → learn → complete + the gate discipline)? Today it's tacit knowledge held by one person. Define the minimum onboarding surface.
- **Multi-operator state:** the kernel already hit state-contention repeatedly (backlogs 244/271, this session's `anchored`-flip issues). Two+ humans + their agents working concurrently multiplies this. Research shared-state models (per-operator isolation, locking, or a coordination service) that don't deadlock.
- **Role separation:** the eval's Level-1/2/3 automation implies different human roles (author, reviewer, approver, HITL adjudicator). Does the kernel need explicit roles/permissions (cf. the writable-vs-read-only layer split platform-selenium already has)?
- **Handoff & shared memory:** lessons, protocol, and context are currently one person's. How do these become team assets (shared lessons, reviewed protocol changes, a common ledger) without losing the hard-enforcement discipline?
- **Enterprise-admin boundary:** the eval correctly says SSO/RBAC is an infrastructure concern, not a framework one — scope what the kernel owns vs what git/ADO/org infra owns.

## References
- 2026 org-level adoption + orchestration-role shift: Anthropic 2026 State of AI Agents Report (resources.anthropic.com); deloitte.com/us/en/insights/.../ai-agent-orchestration.html
- Test-automation eval Levels 1–3 (roles) + writable/read-only split (platform-selenium)
- Kernel state-contention history: `docs/backlog/244-*`, `271-*`, lessons state-contention.md, multi-agent-orchestration.md

## Task Builder Input
- **Deliverable:** Research report in `projects/kernel-team-scalability/` — onboarding surface, multi-operator state model, role separation, shared-memory/handoff design, and the framework-vs-infra boundary; a phased recommendation for making the kernel/platforms team-usable.
- **Location:** subproject:kernel-team-scalability
- **Scope:** RESEARCH
- **Constraints:** Ground in the kernel's actual state-contention history (don't re-derive). Preserve hard enforcement and the single-source-of-truth discipline. No code; produce the model + phased recommendation. Directly informs whether platform-hybrid can be handed to an HMSA team.

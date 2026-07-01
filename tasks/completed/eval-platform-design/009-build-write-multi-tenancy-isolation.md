# Write Multi-Tenancy Isolation Design Document

## Context
This document designs how the platform handles concurrent users safely: container sandboxing, rate limiting, abuse prevention, and cross-user data isolation. The platform runs untrusted user artifacts inside containers -- isolation is a security-critical concern.

This design must consume 158's research findings, specifically:
- Container sandboxing comparison (gVisor for MVP, Firecracker for enterprise) per `06-security-isolation.md`
- Malicious submission prevention (static analysis + runtime controls) per `06-security-isolation.md`
- Rate limiting tiers and abuse prevention per `06-security-isolation.md`
- Data retention policy per `06-security-isolation.md`
- GDPR/CCPA compliance per `06-security-isolation.md`
- Resource limits (2 vCPU, 4GB RAM, 1GB tmpfs, 10-min timeout) per `06-security-isolation.md`

## Type
BUILD

## Execution
inline

## Dependencies
- 002 (prerequisite gate passed)

## Phase Gate
- [ ] Task 002 verdict = PROCEED
- [ ] `projects/eval-platform-design/` directory exists

## Requirements
Write `projects/eval-platform-design/multi-tenancy-isolation.md` covering:

1. **Container sandboxing** -- isolation technology selection
   - MVP: gVisor (Cloud Run default) -- syscall interception, reduced kernel attack surface
   - Enterprise: Firecracker microVMs -- hardware-enforced isolation, 125ms startup
   - Why not Kata Containers (500ms-1s startup too slow for ephemeral eval runs)
   - Reference: sandboxing comparison from `06-security-isolation.md`

2. **Pre-execution static analysis** -- what gets checked before running
   - Artifact size limits (10MB max)
   - File type allowlist per vertical
   - Pattern scanning (reverse shells, base64 executables, fork bombs)
   - Dependency scanning against vulnerability databases
   - Reference: malicious submission prevention from `06-security-isolation.md`

3. **Runtime behavioral controls** -- what's enforced during execution
   - Seccomp profiles (restricted syscalls)
   - Read-only filesystem with tmpfs workspace (1GB limit)
   - Network egress allowlist (LLM API endpoints + platform result endpoint only)
   - Resource limits: 2 vCPU, 4GB RAM, 1GB tmpfs
   - Non-root execution, no capability additions
   - Soft timeout (8 min) + hard timeout (10 min) with SIGKILL
   - Reference: runtime controls from `06-security-isolation.md`

4. **Rate limiting and abuse prevention**
   - Per-user concurrent job limits: Free (1), Pro (3), Enterprise (10)
   - Daily/monthly run limits per tier
   - Anomaly detection: unusual API key usage, repeated failures, key sharing
   - Account suspension workflow (flag -> suspend -> admin review within 24h)
   - Reference: rate limiting from `06-security-isolation.md`

5. **Cross-user data isolation** -- preventing data leakage between users
   - No shared storage between containers
   - Each container gets ephemeral filesystem destroyed on death
   - Process-level isolation via Cloud Run (gVisor) or hardware-level via Firecracker
   - Results stored per-user in PostgreSQL with row-level security
   - API key isolation (key exists only in the requesting container's memory)

6. **Data retention and privacy compliance**
   - What gets kept: evaluation results, approved components, job metadata (12 months)
   - What gets deleted: submitted artifacts (immediately after container death), container state, API keys, logs (30 days)
   - GDPR/CCPA: right to deletion, data portability, consent for component contribution, EU data residency
   - Retention automation: daily cron purges artifacts >24h old, logs >30 days
   - Reference: data retention from `06-security-isolation.md`

7. **References** -- cite specific 158 research files

## Acceptance Criteria
- [ ] `projects/eval-platform-design/multi-tenancy-isolation.md` exists
- [ ] Document references gVisor (`grep -q 'gVisor' projects/eval-platform-design/multi-tenancy-isolation.md`)
- [ ] Document contains `## References` section referencing `eval-web-app-research`
- [ ] Document covers all 4 areas: sandboxing, pre-execution analysis, runtime controls, rate limiting
- [ ] Document addresses GDPR/CCPA compliance

## Gates Satisfied
- BUILD-09, BUILD-15

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.

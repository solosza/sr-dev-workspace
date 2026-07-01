# Write BYOK Key Management Design Document

## Context
BYOK (Bring Your Own Key) is a non-negotiable platform requirement. Users bring their own LLM API keys; the platform never touches user LLM costs. This document designs the secure key injection, provider abstraction, and zero-retention architecture.

This design must consume 158's research findings, specifically:
- Session-scoped in-memory key management for MVP per `04-byok-model.md`
- GCP Secret Manager as growth-path upgrade per `04-byok-model.md`
- Provider support matrix (Anthropic required, OpenAI/Google/Cohere/Mistral optional) per `04-byok-model.md`
- Key leakage prevention analysis per `04-byok-model.md`
- Network egress allowlist per `06-security-isolation.md`

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
Write `projects/eval-platform-design/byok-key-management.md` covering:

1. **Key lifecycle** -- from submission to destruction
   - User submits key via HTTPS (TLS encrypted in transit)
   - Backend generates per-job ephemeral encryption key
   - Encrypted key passed to container via secure channel (Cloud Run secrets or tmpfs)
   - Container decrypts key at start, holds in memory only
   - Key used for LLM API calls during evaluation
   - Container terminates -> key destroyed with process memory
   - Reference: session-scoped in-memory approach from `04-byok-model.md`

2. **Provider abstraction layer** -- how the platform supports multiple LLM providers
   - Anthropic key always required (eval agent runs on Claude)
   - Optional provider keys for LLM-as-judge (OpenAI, Google Vertex AI, Cohere, Mistral)
   - Provider adapter interface (each provider has a thin wrapper)
   - Per-vertical provider needs (LLM Eval needs judge keys; Compliance may need none)

3. **Zero-retention guarantees** -- what the platform commits to
   - Keys never written to disk
   - Keys never in environment variables (stdin pipe or tmpfs mount)
   - Keys never logged or transmitted outside container
   - Container filesystem is ephemeral
   - Audit logging of API calls made (provider, endpoint, token count) without logging the key itself

4. **Key leakage prevention** -- attack vectors and mitigations
   - Container filesystem isolation
   - Memory-only injection (not env vars)
   - Network egress allowlist (only LLM API endpoints + platform result endpoint)
   - Cross-container isolation (no shared storage)
   - Reference: leakage prevention analysis from `04-byok-model.md`

5. **Growth path** -- migration to GCP Secret Manager
   - IAM-based access control
   - Audit logging
   - Automatic secret rotation support
   - Firecracker-based isolation for enterprise

6. **References** -- cite specific 158 research files

## Acceptance Criteria
- [ ] `projects/eval-platform-design/byok-key-management.md` exists
- [ ] Document references session-scoped approach (`grep -q 'session-scoped' projects/eval-platform-design/byok-key-management.md`)
- [ ] Document contains `## References` section referencing `eval-web-app-research`
- [ ] Document covers the full key lifecycle from submission to destruction
- [ ] Document addresses all 5 attack vectors from 158's leakage prevention analysis

## Gates Satisfied
- BUILD-06, BUILD-13

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.

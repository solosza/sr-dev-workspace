# Research Security and Isolation

## Context
Container-per-run handles process isolation, but users submit arbitrary artifacts that the agent executes. Malicious submissions, data exfiltration, and abuse are real threats. This section must cover sandboxing, abuse prevention, and data retention policy.

## Type
RESEARCH

## Execution
inline

## Dependencies
- 001

## Requirements
- Research container sandboxing:
  - gVisor, Kata Containers, Firecracker microVMs vs standard Docker isolation
  - File system restrictions within container (read-only mounts, tmpfs for workspace)
  - Network egress controls (allowlist for LLM API endpoints only)
  - Resource limits (CPU, memory, time, disk)
- Research malicious submission prevention:
  - Static analysis of submitted artifacts before execution
  - Artifact size limits, file type restrictions
  - Behavioral monitoring during execution (syscall filtering, seccomp profiles)
  - Sandboxed execution timeout with forced termination
- Research rate limiting and abuse prevention:
  - Per-user rate limits, concurrent job limits
  - Anomaly detection (unusual API key usage patterns)
  - Account suspension workflow
- Research data retention policy:
  - What gets kept: results, scores, component library additions
  - What gets deleted: submitted artifacts, container state, API keys
  - GDPR/CCPA implications for user data
  - Retention windows and deletion automation
- Use WebSearch for container security best practices from comparable platforms (Replit, CodeSandbox, GitHub Codespaces)

## Acceptance Criteria
- [ ] File `projects/eval-web-app-research/06-security-isolation.md` exists
- [ ] Contains container sandboxing comparison (at least 3 approaches)
- [ ] Contains malicious submission analysis
- [ ] Contains rate limiting and abuse prevention design
- [ ] Contains data retention policy recommendation
- [ ] Minimum 400 words

## Gates Satisfied
DOC-16, DOC-17, DOC-18

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.

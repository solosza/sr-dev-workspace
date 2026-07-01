# Research BYOK Model

## Context
Users bring their own API keys — the platform provides testing intelligence and infrastructure. Secure key management is a hard requirement. Key leakage between container runs would be a platform-killing vulnerability.

## Type
RESEARCH

## Execution
inline

## Dependencies
- 001

## Requirements
- Research key management approaches:
  - HashiCorp Vault (self-hosted or HCP Vault)
  - AWS Secrets Manager / GCP Secret Manager
  - Encrypted environment variables injected at container start
  - Session-scoped keys (in-memory only, never persisted to disk)
- Compare: security posture, cost, operational complexity, latency
- Research which LLM providers need support:
  - Anthropic (required — the eval agent itself)
  - OpenAI, Google, Cohere, Mistral (user's choice for LLM-as-judge or target model)
  - Per-vertical key needs: compliance testing may not need LLM keys at all
- Research key leakage prevention:
  - Container filesystem isolation
  - Memory-only key injection (no env var persistence)
  - Network egress controls (prevent key exfiltration by malicious artifacts)
  - Audit logging of key usage
- Use WebSearch for best practices from comparable BYOK platforms (Helicone, LiteLLM proxy, Portkey)

## Acceptance Criteria
- [ ] File `projects/eval-web-app-research/04-byok-model.md` exists
- [ ] Contains key management approach comparison (at least 3 approaches)
- [ ] Contains provider support matrix
- [ ] Contains key leakage prevention analysis
- [ ] Contains recommendation with rationale
- [ ] Minimum 400 words

## Gates Satisfied
DOC-10, DOC-11, DOC-12

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.

# BYOK Model: Bring Your Own Key Architecture

## Key Management Approach Comparison

Users bring their own LLM API keys. The platform never stores keys persistently — they exist only for the duration of a container run. Four approaches evaluated:

| Approach | Security | Cost | Complexity | Latency | Recommendation |
|----------|----------|------|------------|---------|----------------|
| **Session-scoped in-memory** | High (never touches disk) | Free | Low | None | MVP |
| **GCP Secret Manager** | Very High (IAM + audit) | $0.06/10K access ops | Medium | ~5-10ms per access | Growth |
| **HashiCorp Vault** | Very High (dynamic secrets) | Self-hosted: free; HCP: $0.03/secret/mo | High | ~10-20ms per access | Enterprise |
| **Encrypted env vars** | Medium (encrypted at rest, decrypted at start) | Free | Low | None | Not recommended (key in process env) |

### Session-Scoped In-Memory (Recommended for MVP)

The user submits their API key via HTTPS. The backend encrypts it with a per-job ephemeral key, passes it to the container as a memory-only injection (not an environment variable — injected via stdin or tmpfs mount that's never persisted). The key exists only in the container's memory space. When the container dies, the key is gone.

**Key lifecycle:**
1. User submits key via HTTPS (TLS encrypted in transit)
2. Backend generates per-job encryption key, encrypts user key
3. Encrypted key passed to container via secure channel (Cloud Run secrets or tmpfs)
4. Container decrypts key at start, holds in memory only
5. Agent uses key for LLM API calls during evaluation
6. Container terminates — key destroyed with process memory

### Growth Path: GCP Secret Manager

When the platform scales beyond MVP, migrate to GCP Secret Manager for:
- IAM-based access control (container service account gets scoped access)
- Audit logging of every key access
- Automatic secret rotation support
- Integration with Cloud Run's native secret injection

## Provider Support Matrix

| Provider | Required For | Key Type | Per-Vertical Need |
|----------|-------------|----------|-------------------|
| **Anthropic** | Eval agent execution (Claude Agent SDK) | API key | All verticals (agent runs on Claude) |
| **OpenAI** | LLM-as-judge (user choice) | API key | LLM Eval only |
| **Google (Vertex AI)** | LLM-as-judge (user choice) | Service account JSON | LLM Eval only |
| **Cohere** | LLM-as-judge (user choice) | API key | LLM Eval only |
| **Mistral** | LLM-as-judge (user choice) | API key | LLM Eval only |
| **None (platform-only)** | Compliance testing (no LLM calls by user) | N/A | Compliance vertical |

**Key insight:** The Anthropic key is always required (the eval agent itself runs on Claude). Additional keys are only needed when the user wants LLM-as-judge evaluation with a specific provider. The compliance vertical may not require any user-provided keys at all if the platform covers the agent's API costs — a potential freemium hook.

## Key Leakage Prevention Analysis

Key leakage between container runs would be a platform-killing vulnerability. Attack vectors and mitigations:

### Container Filesystem Isolation
- **Threat:** Key written to disk, persists after container death
- **Mitigation:** Keys never written to disk. Container filesystem is ephemeral (Cloud Run default). Tmpfs mounts for any temporary key material. Container image is read-only except for designated workspace.

### Memory-Only Key Injection
- **Threat:** Key visible in environment variables via `/proc/self/environ`
- **Mitigation:** Do NOT use environment variables for key injection. Use stdin pipe or tmpfs mount that the agent reads once and the file is immediately deleted. Process memory is the only location.

### Network Egress Controls
- **Threat:** Malicious artifact exfiltrates key via HTTP call to attacker-controlled server
- **Mitigation:** Network egress allowlist — container can only reach LLM API endpoints (api.anthropic.com, api.openai.com, etc.) and the platform's result submission endpoint. All other outbound traffic blocked via VPC firewall rules or Cloud Run network policies.

### Audit Logging
- **Threat:** Key misuse undetected
- **Mitigation:** Log every API call made with the user's key (provider, endpoint, token count, timestamp). Surface usage summary in results dashboard. Anomaly detection for unusual patterns (excessive token usage, calls to unexpected endpoints).

### Cross-Container Isolation
- **Threat:** Container A reads Container B's key from shared storage
- **Mitigation:** No shared storage between containers. Each container gets its own ephemeral filesystem. Cloud Run provides process-level isolation between instances. For stronger isolation, Firecracker microVMs (Fly.io) provide hardware-level separation.

## Recommendation

**MVP:** Session-scoped in-memory key injection with network egress allowlisting. No persistent key storage. Container death = key destruction. This provides strong security with minimal infrastructure.

**Growth:** Migrate to GCP Secret Manager with IAM scoping and audit logging. Add Firecracker-based isolation (Fly.io or self-hosted) for enterprise customers who require hardware-level key isolation.

**Key principle:** The platform should never be able to access a user's key outside of the container execution context. If the platform's database is compromised, no user keys are exposed because they were never stored there.

## Sources

- [BYOK Explained: Why You Should Bring Your Own LLM Keys](https://turboanchor.com/blog/byok-bring-your-own-llm-keys-explained/)
- [BYOKList - AI Tools with BYOK](https://byoklist.com/)
- [Best AI Tools With BYOK 2026](https://dmchamp.com/best/best-ai-tools-byok-2026/)
- [Warp BYOLLM Enterprise Features](https://docs.warp.dev/enterprise/enterprise-features/bring-your-own-llm/)

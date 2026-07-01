# BYOK Key Management

Secure key injection, provider abstraction, and zero-retention architecture for the eval platform. Users bring their own LLM API keys; the platform never touches user LLM costs.

## Key Lifecycle

Session-scoped in-memory key management with per-job ephemeral encryption:

| Step | Action | Security Property |
|------|--------|--------------------|
| 1 | User submits key via HTTPS | TLS encrypted in transit |
| 2 | Backend generates per-job ephemeral encryption key | Key isolation per execution |
| 3 | Encrypted key passed to container via secure channel (Cloud Run secrets or tmpfs) | Not in env vars, not on persistent disk |
| 4 | Container decrypts key at start, holds in memory only | Memory-resident, no disk writes |
| 5 | Key used for LLM API calls during evaluation | Scoped to single container lifetime |
| 6 | Container terminates — key destroyed with process memory | Zero-retention on completion |

The ephemeral encryption key is generated per-job and discarded after container creation. The user's plaintext key never exists outside container memory. If the platform's database is compromised, no user keys are exposed because they were never stored there.

## Provider Abstraction Layer

### Required vs Optional Keys

| Provider | Required For | Key Type | Per-Vertical Need |
|----------|-------------|----------|-------------------|
| **Anthropic** | Eval agent execution (Claude Agent SDK) | API key | All verticals — agent runs on Claude |
| **OpenAI** | LLM-as-judge (user choice) | API key | LLM Eval only |
| **Google Vertex AI** | LLM-as-judge (user choice) | Service account JSON | LLM Eval only |
| **Cohere** | LLM-as-judge (user choice) | API key | LLM Eval only |
| **Mistral** | LLM-as-judge (user choice) | API key | LLM Eval only |
| **None** | Compliance testing (no user LLM calls) | N/A | Compliance vertical |

The Anthropic key is always required — the eval agent itself runs on Claude. Additional keys are only needed when the user selects LLM-as-judge evaluation with a specific provider.

### Provider Adapter Interface

Each supported provider gets a thin adapter:

```
ProviderAdapter
  ├── validate_key(key) -> bool     # Pre-flight key check
  ├── get_endpoints() -> list[str]  # Allowed egress URLs for this provider
  └── create_client(key) -> Client  # LLM client instantiation
```

The container receives a provider config (which provider, which adapter) alongside the encrypted key. The adapter pattern keeps provider-specific logic isolated — adding a new provider means one new adapter class, no changes to the key lifecycle.

### Per-Vertical Provider Requirements

- **LLM Eval vertical:** Anthropic key (agent) + optional judge provider key
- **Compliance vertical:** Anthropic key (agent) only — may need no user key if platform covers agent costs (freemium hook)
- **Future verticals:** Inherit base requirement (Anthropic) + vertical-specific optional keys

## Zero-Retention Guarantees

What the platform commits to:

| Guarantee | Implementation |
|-----------|----------------|
| Keys never written to disk | Memory-only injection via stdin pipe or tmpfs (immediately deleted after read) |
| Keys never in environment variables | stdin pipe or tmpfs mount — not `ENV` or `--env` flags |
| Keys never logged or transmitted outside container | Logging middleware strips key patterns; egress allowlist blocks unauthorized endpoints |
| Container filesystem is ephemeral | Cloud Run default — no persistent volumes attached |
| API call audit without key exposure | Log provider, endpoint, token count, timestamp — never the key itself |

## Key Leakage Prevention

Five attack vectors and their mitigations (from 158 research):

### 1. Container Filesystem Isolation
- **Threat:** Key written to disk, persists after container death
- **Mitigation:** Keys never written to disk. Container filesystem is ephemeral (Cloud Run default). Tmpfs mounts for any temporary key material. Container image is read-only except for designated workspace.

### 2. Memory-Only Key Injection
- **Threat:** Key visible in environment variables via `/proc/self/environ`
- **Mitigation:** Do NOT use environment variables. Use stdin pipe or tmpfs mount that the agent reads once, then immediately deletes. Process memory is the only location.

### 3. Network Egress Controls
- **Threat:** Malicious artifact exfiltrates key via HTTP to attacker-controlled server
- **Mitigation:** Network egress allowlist — container can only reach:
  - `api.anthropic.com` (Claude API)
  - `api.openai.com` (OpenAI, if key provided)
  - `generativelanguage.googleapis.com` (Google Vertex AI, if key provided)
  - Platform result submission endpoint
  - All other outbound traffic blocked via VPC firewall rules or Cloud Run network policies

### 4. Audit Logging
- **Threat:** Key misuse goes undetected
- **Mitigation:** Log every API call made with the user's key (provider, endpoint, token count, timestamp). Surface usage summary in results dashboard. Anomaly detection for unusual patterns (excessive token usage, calls to unexpected endpoints).

### 5. Cross-Container Isolation
- **Threat:** Container A reads Container B's key from shared storage
- **Mitigation:** No shared storage between containers. Each container gets its own ephemeral filesystem. Cloud Run provides process-level isolation (gVisor). For enterprise, Firecracker microVMs provide hardware-level separation.

## Growth Path: GCP Secret Manager

When the platform scales beyond MVP:

| Capability | Benefit |
|------------|---------|
| IAM-based access control | Container service account gets scoped, time-limited access to its own secret only |
| Audit logging | Every secret access logged in Cloud Audit Logs — compliance-ready |
| Automatic secret rotation | Support for customers with key rotation policies |
| Cloud Run native integration | Secret injection via `--set-secrets` without custom code |

Enterprise tier adds Firecracker-based isolation (Fly.io or self-hosted) for hardware-level key separation between tenants.

## References

- `projects/eval-web-app-research/04-byok-model.md` — session-scoped in-memory approach, provider matrix, key leakage prevention analysis, GCP Secret Manager growth path
- `projects/eval-web-app-research/06-security-isolation.md` — network egress allowlist, container sandboxing (gVisor/Firecracker), runtime behavioral controls
- `projects/eval-platform-design/execution-pipeline.md` — container lifecycle that consumes BYOK key injection
- `projects/eval-platform-design/vertical-plugin-system.md` — per-vertical provider requirements

# Security and Isolation

## Container Sandboxing Comparison

Users submit arbitrary artifacts that the agent executes inside containers. Standard Docker isolation (shared kernel, runc) is insufficient for untrusted code execution — the 2026 industry consensus is clear on this point.

| Technology | Isolation Level | Startup Time | Overhead | Security Boundary | Best For |
|-----------|----------------|-------------|----------|-------------------|----------|
| **Docker (runc)** | Process-level (shared kernel) | ~50ms | Minimal | Namespace + cgroup only | Trusted workloads |
| **gVisor (runsc)** | User-space kernel | ~50ms + 20-50% runtime | Moderate | Syscall interception via Sentry | Enhanced container security without VM complexity |
| **Firecracker microVM** | Hardware-enforced (KVM) | ~125ms | Low (minimal VMM) | Dedicated kernel, 5 devices only | Untrusted code, multi-tenant isolation |
| **Kata Containers** | Full VM per container | ~500ms-1s | Higher (full guest OS) | Hardware virtualization | Maximum isolation, Kubernetes-native |

### Recommendation: gVisor for MVP, Firecracker for Enterprise

**MVP (Cloud Run):** Google Cloud Run supports gVisor natively (it's the default sandbox runtime). No additional configuration needed. This provides syscall interception and reduced kernel attack surface with zero operational overhead.

**Enterprise:** Firecracker microVMs (available via Fly.io or self-hosted) provide hardware-enforced isolation with a minimal attack surface (50K lines of Rust, 5 virtual devices). For enterprise customers processing sensitive artifacts, this is the gold standard.

**Why not Kata Containers:** Startup time (~500ms-1s) is too slow for ephemeral eval runs, and the full guest OS overhead isn't justified when Firecracker achieves similar isolation with less overhead.

## Malicious Submission Prevention

### Pre-Execution Static Analysis
- **Artifact size limits:** Max 10MB per submission (prevents resource exhaustion)
- **File type restrictions:** Allowlist of accepted file types per vertical (.md, .py, .json, .yaml, .toml, .sh, .ts, .js)
- **Pattern scanning:** Reject artifacts containing known malicious patterns (reverse shells, base64-encoded executables, fork bombs)
- **Dependency scanning:** If artifact includes requirements.txt or package.json, scan dependencies against known vulnerability databases

### Runtime Behavioral Controls
- **Seccomp profiles:** Restrict syscalls to the minimum required for evaluation (no raw socket, no mount, no ptrace)
- **Read-only filesystem:** Container image mounted read-only. Writable workspace limited to tmpfs (RAM-backed, size-limited)
- **Network egress allowlist:** Container can only reach:
  - `api.anthropic.com` (Claude API)
  - `api.openai.com`, `generativelanguage.googleapis.com` (optional LLM providers)
  - Platform result submission endpoint
  - All other outbound traffic blocked
- **Resource limits:**
  - CPU: 2 vCPU max per container
  - Memory: 4GB max
  - Disk: 1GB tmpfs workspace
  - Time: 10-minute hard timeout with SIGKILL
- **No privilege escalation:** Container runs as non-root user, no capability additions

### Sandbox Execution Timeout
- **Soft timeout (8 minutes):** Agent receives signal to wrap up, submit partial results
- **Hard timeout (10 minutes):** Container forcefully terminated, partial results preserved if available
- **Rationale:** Eval runs should complete in 2-5 minutes. Anything beyond 8 minutes indicates either a complex legitimate run or a stuck/malicious process

## Rate Limiting and Abuse Prevention

### Per-User Rate Limits
| Tier | Concurrent Jobs | Daily Limit | Monthly Limit |
|------|----------------|-------------|---------------|
| Free | 1 | 5 | 50 |
| Pro | 3 | 50 | 500 |
| Enterprise | 10 | Unlimited | Unlimited |

### Anomaly Detection
- **Unusual API key usage:** If a user's key makes 10x more API calls than the average for their artifact type, flag for review
- **Repeated failures:** If a user submits artifacts that consistently fail or timeout, throttle further submissions
- **Key sharing detection:** If the same API key appears across multiple user accounts, flag both accounts

### Account Suspension Workflow
1. Automated flag raised (rate limit exceeded, anomaly detected, or malicious pattern found)
2. Account suspended from new submissions (existing jobs complete)
3. Platform admin reviews within 24 hours
4. Outcome: reinstate, permanent ban, or warning with reduced limits

## Data Retention Policy

### What Gets Kept
- **Evaluation results:** Scores, pass/fail status, component diffs — retained indefinitely (this is the product value)
- **Component library additions:** Approved components — retained indefinitely (this is the platform moat)
- **Job metadata:** Submission timestamp, vertical, duration, status — retained for analytics (12 months)

### What Gets Deleted
- **Submitted artifacts:** Deleted immediately after container termination (unless user opts in to retention for re-runs)
- **Container state:** Ephemeral filesystem destroyed on container death
- **API keys:** Never persisted; exist only in container memory during execution
- **Container logs:** Retained 30 days for debugging, then purged

### GDPR/CCPA Compliance
- **Right to deletion:** User can request deletion of all their data (results, job history, account)
- **Data portability:** User can export their evaluation results in standard format (JSON/CSV)
- **Consent:** Clear opt-in for component contribution (user must explicitly agree that agent-generated components can be added to the shared library)
- **Data processing agreement:** Available for enterprise customers
- **EU data residency:** Cloud Run supports region-specific deployment (europe-west1) for EU customers

### Retention Automation
- Cron job runs daily: purge artifacts older than 24 hours, purge logs older than 30 days
- User-facing data export available via dashboard
- Account deletion triggers cascade: all results, history, and metadata purged within 72 hours

## Sources

- [How to Sandbox AI Agents in 2026](https://manveerc.substack.com/p/ai-agent-sandboxing-guide)
- [Firecracker vs gVisor - Northflank](https://northflank.com/blog/firecracker-vs-gvisor)
- [Kata vs Firecracker vs gVisor Isolation Compared](https://edera.dev/stories/kata-vs-firecracker-vs-gvisor-isolation-compared)
- [MCP Security Patterns 2026: gVisor vs Firecracker](https://dev.to/chunxiaoxx/mcp-security-patterns-2026-gvisor-vs-firecracker-for-ai-agent-sandboxing-3hp7)
- [How Major Tech Companies Sandbox AI Agents](https://medium.com/@earlperry562/how-every-major-tech-company-is-sandboxing-ai-agents-differently-f41b65f14d8a)

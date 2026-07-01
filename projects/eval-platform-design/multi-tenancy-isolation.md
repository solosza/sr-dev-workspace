# Multi-Tenancy Isolation Design

The platform runs untrusted user artifacts inside containers. Isolation is security-critical: users submit arbitrary code that an agent executes, scores, and reports on. This document defines the sandboxing, analysis, runtime controls, rate limiting, data isolation, and compliance requirements.

## Container Sandboxing

### MVP: gVisor (Cloud Run Default)

Google Cloud Run uses gVisor (runsc) as its default sandbox runtime. gVisor interposes a user-space kernel (Sentry) between the container and the host kernel, intercepting syscalls and reducing the kernel attack surface to ~20 implemented syscalls vs. Linux's ~300+. Benefits:

- Zero operational overhead — Cloud Run enables gVisor by default
- ~50ms startup + 20-50% runtime overhead (acceptable for eval workloads)
- Syscall interception prevents kernel exploits from reaching the host
- Process-level isolation sufficient for MVP multi-tenancy

### Enterprise: Firecracker MicroVMs

For enterprise customers processing sensitive artifacts, Firecracker microVMs provide hardware-enforced isolation via KVM:

- ~125ms startup, minimal VMM (~50K lines of Rust)
- Only 5 virtual devices exposed — dramatically reduced attack surface
- Each container gets a dedicated kernel — no shared kernel attack vector
- Available via Fly.io managed or self-hosted on bare metal

### Why Not Kata Containers

Kata Containers provide full VM isolation but with ~500ms-1s startup time. For ephemeral eval runs (target: 2-5 minutes), 500ms+ cold start is unacceptable overhead, and the full guest OS adds resource cost that Firecracker avoids.

## Pre-Execution Static Analysis

Before any artifact enters a container, static analysis gates reject known-bad submissions:

| Check | Threshold | Rationale |
|-------|-----------|-----------|
| Artifact size | 10MB max | Prevents resource exhaustion during upload/extraction |
| File type allowlist | Per-vertical (.md, .py, .json, .yaml, .toml, .sh, .ts, .js) | Blocks executable binaries, compiled code |
| Pattern scanning | Reverse shells, base64 executables, fork bombs | Catches common attack payloads |
| Dependency scanning | requirements.txt / package.json against CVE databases | Blocks known-vulnerable dependencies |

Rejected artifacts return a clear error message with the specific rule violated. No partial execution — the artifact never enters a container.

## Runtime Behavioral Controls

Once inside the container, runtime controls enforce a minimal execution environment:

**Syscall Restriction (Seccomp):** Restricted profile blocks raw socket creation, mount, ptrace, and other unnecessary syscalls. Only the minimum syscalls required for Python/Node.js evaluation execution are permitted.

**Filesystem Isolation:**
- Container image mounted read-only
- Writable workspace: tmpfs (RAM-backed), 1GB limit
- No persistent storage across runs

**Network Egress Allowlist:**
- `api.anthropic.com` (Claude API)
- `api.openai.com`, `generativelanguage.googleapis.com` (optional LLM providers)
- Platform result submission endpoint
- All other outbound traffic blocked via network policy

**Resource Limits:**
- CPU: 2 vCPU max
- Memory: 4GB max
- Disk: 1GB tmpfs workspace
- Non-root execution, no capability additions (no `--privileged`, no `CAP_SYS_ADMIN`)

**Execution Timeout:**
- Soft timeout (8 min): agent receives SIGTERM, submits partial results
- Hard timeout (10 min): container receives SIGKILL, partial results preserved if available
- Rationale: eval runs should complete in 2-5 minutes; beyond 8 minutes indicates stuck or malicious process

## Rate Limiting and Abuse Prevention

### Per-User Limits

| Tier | Concurrent Jobs | Daily Limit | Monthly Limit |
|------|----------------|-------------|---------------|
| Free | 1 | 5 | 50 |
| Pro | 3 | 50 | 500 |
| Enterprise | 10 | Unlimited | Unlimited |

### Anomaly Detection

- **Unusual API key usage:** Flag accounts making 10x more API calls than average for their artifact type
- **Repeated failures:** Throttle accounts with consistent timeouts or failures (suggests probing)
- **Key sharing detection:** Flag accounts where the same API key appears across multiple user accounts

### Account Suspension Workflow

1. Automated flag raised (rate limit, anomaly, or malicious pattern)
2. Account suspended from new submissions (in-flight jobs complete normally)
3. Platform admin reviews within 24 hours
4. Outcome: reinstate, permanent ban, or warning with reduced limits

## Cross-User Data Isolation

No shared storage exists between containers. Each execution gets:

- Ephemeral filesystem destroyed on container death
- Process-level isolation via gVisor (MVP) or hardware-level via Firecracker (enterprise)
- Results stored per-user in PostgreSQL with row-level security (RLS)
- API keys exist only in the requesting container's memory — never persisted to disk or shared storage

Cross-user data leakage is architecturally impossible: containers share no filesystem, no network namespace, and no database rows.

## Data Retention and Privacy Compliance

### Retention Policy

| Data Type | Retention | Rationale |
|-----------|-----------|-----------|
| Evaluation results (scores, pass/fail, diffs) | 12 months | Product value — what users pay for |
| Approved components | Indefinite | Platform moat — curated library |
| Job metadata (timestamp, vertical, duration) | 12 months | Analytics |
| Submitted artifacts | Deleted on container death | Privacy — user code never persisted |
| Container state | Ephemeral — destroyed on death | Security — no residual state |
| API keys | Never persisted | Security — memory-only during execution |
| Container logs | 30 days | Debugging, then purged |

### GDPR/CCPA Compliance

- **Right to deletion:** Users can request deletion of all data (results, history, account). Cascade completes within 72 hours.
- **Data portability:** Users can export evaluation results in JSON/CSV via dashboard.
- **Consent for component contribution:** Explicit opt-in required before agent-generated components enter the shared library. No silent harvesting.
- **Data processing agreement:** Available for enterprise customers upon request.
- **EU data residency:** Cloud Run supports region-specific deployment (europe-west1) for EU customers requiring data sovereignty.

### Retention Automation

- Daily cron: purge artifacts >24 hours old, purge logs >30 days old
- User-facing data export available via dashboard
- Account deletion triggers full cascade: results, history, metadata purged within 72 hours

## References

- Container sandboxing comparison: `projects/eval-web-app-research/06-security-isolation.md` (Container Sandboxing Comparison)
- Malicious submission prevention: `projects/eval-web-app-research/06-security-isolation.md` (Malicious Submission Prevention)
- Runtime behavioral controls: `projects/eval-web-app-research/06-security-isolation.md` (Runtime Behavioral Controls)
- Rate limiting and abuse prevention: `projects/eval-web-app-research/06-security-isolation.md` (Rate Limiting and Abuse Prevention)
- Data retention and GDPR/CCPA: `projects/eval-web-app-research/06-security-isolation.md` (Data Retention Policy, GDPR/CCPA Compliance)

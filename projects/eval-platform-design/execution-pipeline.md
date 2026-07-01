# Execution Pipeline

## Overview

Full submission-to-teardown pipeline: user submits artifact + API key + vertical selection, the system queues a container job, the container runs the eval with Claude Agent SDK, results are returned, and the container is destroyed.

## 1. Submission Flow

When a user clicks "submit":

1. **Artifact validation** — FastAPI receives the upload and runs pre-execution checks:
   - Size limit: max 10MB per submission (per `06-security-isolation.md`)
   - File type allowlist per vertical: `.md`, `.py`, `.json`, `.yaml`, `.toml`, `.sh`, `.ts`, `.js`
   - Pattern scanning: reject artifacts containing reverse shells, base64-encoded executables, fork bombs
   - Dependency scanning: if `requirements.txt` or `package.json` included, scan against vulnerability databases

2. **API key encryption** — per-job ephemeral key (per `04-byok-model.md`):
   - Backend generates a per-job encryption key
   - User's API key encrypted with per-job key
   - Encrypted key passed to container via secure channel (Cloud Run secrets or tmpfs)
   - Key never written to disk, never stored in environment variables

3. **Job record creation** — PostgreSQL entry with: user ID, vertical, artifact hash, status (`queued`), timestamps

4. **Vertical routing** — vertical selection determines which pre-baked container image to use (per `03-tech-stack.md`):
   - Known verticals (e.g., platform-deepeval) → pre-baked image with compiled protocol
   - Custom specs (future) → on-demand compilation image

## 2. Job Queue

Google Cloud Tasks dispatches container execution requests (per `03-tech-stack.md`).

**Queue priority:**

| Tier | Concurrent Jobs | Priority | Daily Limit |
|------|----------------|----------|-------------|
| Free | 1 | Standard | 5 |
| Pro | 3 | High | 50 |
| Enterprise | 10 | High | Unlimited |

Per `06-security-isolation.md` rate limits.

**Job status tracking:** `queued` → `running` → `completed` | `failed` | `timed_out`

Each status transition writes to PostgreSQL and pushes an SSE event to the frontend. Queue backlog triggers user notification with estimated wait time.

## 3. Container Lifecycle

From spin-up to teardown on Google Cloud Run:

1. **Image selection** — Cloud Run pulls the pre-baked image for the selected vertical. Image contains: Node.js + Python runtime, Claude Agent SDK, kernel, platform spec with pre-compiled protocol and hooks (per `03-tech-stack.md`)

2. **API key injection** — encrypted key injected via memory-only channel (stdin pipe or tmpfs mount, per `04-byok-model.md`). Container decrypts at start, holds in memory only. Never an environment variable — prevents `/proc/self/environ` leakage

3. **Artifact mounting** — user's artifact mounted as read-only volume. Container filesystem is read-only except for designated tmpfs workspace (1GB, RAM-backed)

4. **Agent execution** — Claude Agent SDK initializes with kernel + compiled protocol:
   - Agent reads artifact, checks existing components in the vertical's component library
   - Builds missing components from `_reference/` patterns
   - Runs evaluation loop, streams progress via SSE to frontend
   - All LLM API calls use the user's injected key

5. **Timeout enforcement** (per `06-security-isolation.md`):
   - **8-minute soft timeout** — agent receives signal to wrap up, submit partial results
   - **10-minute hard timeout** — container forcefully terminated via SIGKILL
   - Normal eval runs complete in 2-5 minutes

6. **Results extraction** — before termination, agent writes scores and component diffs to a results endpoint

7. **Teardown** — container filesystem destroyed, API key purged from memory on container death. Cloud Run's ephemeral filesystem guarantees no state persists between runs

## 4. Results Pipeline

How results flow back to the user:

- **Scores and pass/fail** stored in PostgreSQL (structured results, queryable per user/vertical/time)
- **New components** queued for curation review — components the agent built from `_reference/` patterns during eval
- **Real-time progress** streamed via SSE (Server-Sent Events) to the Next.js frontend dashboard
- **API key purged** from memory on container death — no key material survives the run
- **Artifact cleanup** — submitted artifacts deleted immediately after container termination (unless user opts in to retention for re-runs, per `06-security-isolation.md` data retention policy)

## 5. Error Handling

| Failure Mode | Response | User Impact |
|-------------|----------|-------------|
| Container crash | Partial results preserved if available, job marked `failed` | Error message + any partial scores |
| API key invalid | Immediate termination, no LLM calls attempted | Clear error: "Invalid API key" |
| Soft timeout (8 min) | Agent wraps up, submits partial results | Partial results + timeout flag |
| Hard timeout (10 min) | Container killed, partial results returned if extracted | Partial results + timeout warning |
| Queue backlog | User notification with estimated wait time | Wait time estimate in dashboard |
| Artifact validation failure | Job rejected before queuing | Specific error (size, type, pattern) |

All failures log to Cloud Logging with job ID correlation for debugging. Container logs retained 30 days then purged (per `06-security-isolation.md`).

## 6. Resource Limits

Per container (per `06-security-isolation.md`):
- CPU: 2 vCPU max
- Memory: 4GB max
- Disk: 1GB tmpfs workspace
- Time: 10-minute hard timeout
- Network: egress allowlist only (api.anthropic.com, api.openai.com, generativelanguage.googleapis.com, platform result endpoint)
- Sandbox: gVisor (Cloud Run default) for MVP, Firecracker microVMs for enterprise

## References

- `projects/eval-web-app-research/03-tech-stack.md` — Cloud Run recommendation, Claude Agent SDK selection, FastAPI backend, pipeline architecture
- `projects/eval-web-app-research/04-byok-model.md` — session-scoped in-memory key injection, per-job ephemeral encryption, key lifecycle
- `projects/eval-web-app-research/06-security-isolation.md` — gVisor sandboxing, timeout policy, rate limits, artifact validation, data retention
- `projects/eval-web-app-research/01-idea-validation.md` — target users, first vertical selection

# Tech Stack Recommendation: Multi-Vertical AI Testing Platform

## Container Orchestration Comparison

The platform requires disposable, per-run containers: spin up with kernel + platform spec, run evaluation, return results, container dies. This is a serverless/ephemeral workload pattern.

| Platform | Cost (per vCPU-hr) | Cold Start | Autoscaling | Isolation | Complexity | Best For |
|----------|-------------------|------------|-------------|-----------|------------|----------|
| **Google Cloud Run** | ~$0.024/vCPU-hr | <1s (warm), ~2-5s (cold) | Scale-to-zero native | Container-level | Low | Serverless, event-driven, pay-per-use |
| **AWS ECS Fargate** | ~$0.041/vCPU-hr | ~10-30s | Task-based | Container-level | Medium | AWS-centric, low-ops |
| **AWS EKS (Kubernetes)** | ~$0.014/vCPU-hr (EC2 Spot) + $0.10/cluster-hr | Depends on node pool | Full Karpenter/Spot | Pod-level (+ gVisor) | High | Scale, multi-cloud, cost optimization |
| **Fly.io** | ~$0.031/vCPU-hr | <1s (Machines) | Scale-to-zero | Firecracker microVMs | Low | Edge, fast start, strong isolation |
| **Docker Compose** | N/A (local) | Instant | None | Container-level | Very Low | Development/testing only |

**Recommendation: Google Cloud Run for MVP, with Fly.io as alternative.**

Rationale: Cloud Run offers the lowest operational complexity with scale-to-zero (no cost when idle), pay-per-second billing, and sub-second warm starts. For an MVP that may have low initial traffic, scale-to-zero eliminates idle infrastructure costs. ECS Fargate costs ~3x more than Kubernetes for equivalent workloads, and Kubernetes is overkill for MVP. Fly.io's Firecracker-based isolation is attractive for security but has a smaller ecosystem.

**Growth path:** Migrate to EKS with Karpenter + Spot instances when traffic justifies the operational overhead (est. >50 concurrent containers). Kubernetes delivers 40-60% cost savings at scale vs Fargate.

## Agent Execution Model

The agent must run inside a container with kernel + platform spec. Three execution approaches:

### Option 1: Claude Agent SDK (Recommended)

The Claude Agent SDK (formerly Claude Code SDK) provides the same harness that powers Claude Code, with file editing tools, bash execution, MCP support, subagents, and persistent sessions. A containerized Claude Agent SDK reference implementation exists (github.com/receipting/claude-agent-sdk-container) that deploys to any Docker-compatible cloud.

**Pros:** Native tool-use loop, subagent support, session persistence, direct access to kernel commands
**Cons:** Per-token billing (metered separately from interactive Claude Code as of June 2026), requires container with Node.js/Python runtime
**Cost:** API token costs passed to user via BYOK; platform pays only for SDK infrastructure overhead

### Option 2: Claude API Direct (HTTP calls)

Build a custom agent loop using raw Anthropic API calls with tool definitions.

**Pros:** Full control over token usage and tool definitions, lower overhead
**Cons:** Must reimplement tool-use loop, file editing, bash execution; no native subagent support; significant engineering effort to replicate kernel capabilities

### Option 3: Claude Code CLI

Run `claude -p` inside the container.

**Pros:** Full Claude Code capabilities including all kernel commands
**Cons:** CLI binary must be installed in container; interactive mode complications; CLAUDECODE env var issues in nested contexts (documented lesson); not designed for programmatic API access

**Recommendation: Claude Agent SDK.** It provides kernel-compatible capabilities (tool use, file editing, bash, subagents) without reimplementing the agent loop, and it's designed for containerized deployment.

## Domain-Setup Containerization Strategy

The kernel's `/kernel/domain-setup` compiles a protocol + hooks from the platform spec's `_reference/` patterns. Two strategies:

### Pre-baked Images (Recommended for MVP)

Build per-vertical container images with domain-setup already completed:
```
Base image (Node.js + Python + Claude Agent SDK)
  └── platform-deepeval image (kernel + platform spec + pre-compiled protocol + hooks)
  └── platform-ssh image (kernel + platform spec + pre-compiled protocol + hooks)
  └── platform-selenium image (kernel + platform spec + pre-compiled protocol + hooks)
```

**Pros:** Faster container startup (skip domain-setup), deterministic protocol, no API calls wasted on compilation
**Cons:** Must rebuild images when platform spec changes; less dynamic

### On-Demand Compilation

Run domain-setup inside the container at job start.

**Pros:** Always uses latest platform spec; supports user-submitted custom platform specs
**Cons:** Adds 30-60s to every job (protocol compilation + API calls); wastes user's API tokens on setup

**Recommendation:** Pre-baked images for known verticals, on-demand compilation only for custom/user-submitted platform specs (future feature).

## Frontend/Backend Recommendation

### Frontend: Next.js

- **Submission UI:** File upload form + API key input + vertical selector
- **Results dashboard:** Real-time streaming of eval progress (SSE/WebSocket), final score display, component library browser
- **Rationale:** React ecosystem, SSR for SEO, API routes for backend, extensive component library, largest hiring pool

### Backend: FastAPI (Python)

- **API design:** REST endpoints for job submission, status polling, results retrieval
- **Job queue:** Google Cloud Tasks (matches Cloud Run) or BullMQ (Redis-backed, for self-hosted)
- **Results storage:** PostgreSQL (structured results, user accounts) + Cloud Storage/S3 (artifacts, logs)
- **Rationale:** Python aligns with kernel ecosystem (hooks are Python), FastAPI is performant with async support, integrates with Claude Agent SDK Python client

### Pipeline Architecture

```
User submits artifact + API key + vertical selection
    │
    ▼
FastAPI receives submission
    │ Validates artifact (size, type, format)
    │ Encrypts API key (session-scoped)
    │ Creates job record in PostgreSQL
    │
    ▼
Job Queue (Cloud Tasks)
    │ Enqueues container execution request
    │
    ▼
Cloud Run spins up pre-baked container
    │ Kernel + platform spec already compiled
    │ API key injected as env var (memory-only)
    │ Artifact mounted as read-only volume
    │
    ▼
Claude Agent SDK runs eval loop
    │ Reads artifact, checks existing components
    │ Builds missing components from _reference/
    │ Runs evaluation, streams progress via SSE
    │
    ▼
Results returned
    │ Scores + component diffs stored in PostgreSQL
    │ New components queued for curation review
    │ Container terminated, filesystem destroyed
    │ API key purged from memory
    │
    ▼
User views results in dashboard
    │ Scores, pass/fail, component growth contribution
```

## Sources

- [Cost Optimization: ECS Fargate vs Kubernetes 2026](https://medium.com/@inboryn/cost-optimization-why-ecs-fargate-costs-3x-more-than-kubernetes-2026-reality-check-f9a2bb726f00)
- [Kubernetes vs Nomad vs AWS ECS 2026](https://enterprise-software-review.contentwave.net/article/kubernetes-vs-nomad-vs-aws-ecs-enterprise-orchestration-june-2026)
- [Container Orchestration Alternatives Beyond Kubernetes](https://encore.dev/articles/kubernetes-orchestration-alternatives)
- [Claude Agent SDK Overview](https://platform.claude.com/docs/en/agent-sdk/overview)
- [Claude Agent SDK Container](https://github.com/receipting/claude-agent-sdk-container)
- [Hosting the Agent SDK](https://platform.claude.com/docs/en/agent-sdk/hosting)

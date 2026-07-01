# Write Execution Pipeline Design Document

## Context
This document designs the full submission-to-teardown pipeline: user submits artifact + API key + vertical selection, the system queues a container job, the container runs the eval with Claude Agent SDK, results are returned, and the container is destroyed.

This design must consume 158's research findings, specifically:
- Pipeline architecture from `03-tech-stack.md` (FastAPI -> Cloud Tasks -> Cloud Run -> Agent SDK -> Results)
- Pre-baked images for known verticals, on-demand compilation for custom specs per `03-tech-stack.md`
- Claude Agent SDK as the agent execution model per `03-tech-stack.md`
- 10-minute hard timeout, 8-minute soft timeout per `06-security-isolation.md`
- Session-scoped key injection per `04-byok-model.md`

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
Write `projects/eval-platform-design/execution-pipeline.md` covering:

1. **Submission flow** — what happens when a user clicks "submit"
   - Artifact validation (size limits, file type allowlist, pattern scanning per `06-security-isolation.md`)
   - API key encryption (per-job ephemeral key per `04-byok-model.md`)
   - Job record creation in PostgreSQL
   - Vertical selection determines which container image to use

2. **Job queue** — how submissions are queued and dispatched
   - Google Cloud Tasks for Cloud Run deployment (per `03-tech-stack.md`)
   - Queue priority (free vs paid tier)
   - Concurrency limits per user tier per `06-security-isolation.md`
   - Job status tracking (queued, running, completed, failed, timed_out)

3. **Container lifecycle** — from spin-up to teardown
   - Pre-baked image selection based on vertical
   - API key injection via secure channel (memory-only, not env var per `04-byok-model.md`)
   - Artifact mounting as read-only volume
   - Claude Agent SDK initialization with kernel + compiled protocol
   - Eval execution loop
   - Soft timeout (8 min) -> hard timeout (10 min) per `06-security-isolation.md`
   - Results extraction before termination
   - Container filesystem destruction

4. **Results pipeline** — how results flow back to the user
   - Scores and pass/fail stored in PostgreSQL
   - New components queued for curation review
   - Real-time progress streaming via SSE to frontend
   - API key purged from memory on container death

5. **Error handling** — failure modes and recovery
   - Container crash -> partial results preserved if available
   - API key invalid -> immediate termination with error
   - Timeout -> partial results returned with timeout flag
   - Queue backlog -> user notification with estimated wait time

6. **References** — cite specific 158 research files

## Acceptance Criteria
- [ ] `projects/eval-platform-design/execution-pipeline.md` exists
- [ ] Document references Cloud Run (`grep -q 'Cloud Run' projects/eval-platform-design/execution-pipeline.md`)
- [ ] Document references Claude Agent SDK as the execution model
- [ ] Document contains `## References` section referencing `eval-web-app-research`
- [ ] Document covers full lifecycle: submission -> queue -> container -> results -> teardown

## Gates Satisfied
- BUILD-05, BUILD-12

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.

# Research Tech Stack

## Context
The platform needs a web wrapper around the existing CLI eval loop: submission UI, container orchestration, job queue, results storage. The agent must run inside a container with kernel + platform spec. This section must recommend a concrete tech stack.

## Type
RESEARCH

## Execution
inline

## Dependencies
- 001

## Requirements
- Research container orchestration options: Docker Compose (dev), Kubernetes, ECS, Cloud Run, Fly.io
  - Compare: cost, complexity, autoscaling, cold start, isolation guarantees
- Research how the agent runs inside a container:
  - Claude API direct (HTTP calls) vs Claude Code CLI vs Claude Code SDK
  - How domain-setup compilation step works in a containerized environment (pre-baked vs on-demand)
  - Container image strategy: base image with kernel + mount platform spec, or per-vertical images
- Research frontend options: Next.js, SvelteKit, plain React — submission form + results dashboard
- Research backend/API: job queue (Bull/BullMQ, SQS, Cloud Tasks), results storage (Postgres, S3), API framework (FastAPI, Express, Hono)
- Research submission-to-result pipeline: submit artifact -> queue job -> spin container -> run eval -> stream results -> container dies
- Use WebSearch for current pricing of container orchestration services and comparable platform architectures

## Acceptance Criteria
- [ ] File `projects/eval-web-app-research/03-tech-stack.md` exists
- [ ] Contains container orchestration comparison table with cost estimates
- [ ] Contains agent execution model analysis (API vs CLI vs SDK)
- [ ] Contains domain-setup containerization strategy
- [ ] Contains frontend/backend recommendation with rationale
- [ ] Contains pipeline architecture diagram or description (submission to results)
- [ ] Minimum 500 words

## Gates Satisfied
DOC-07, DOC-08, DOC-09

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.

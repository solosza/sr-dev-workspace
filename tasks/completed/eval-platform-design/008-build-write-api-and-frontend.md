# Write API and Frontend Design Document

## Context
This document designs the REST API, submission UI, results dashboard, and vertical selector. The frontend is the user's primary interaction surface; the API is what the frontend and potential third-party integrations consume.

This design must consume 158's research findings, specifically:
- Frontend: Next.js for submission UI + results dashboard per `03-tech-stack.md`
- Backend: FastAPI (Python) for REST endpoints per `03-tech-stack.md`
- Job queue: Google Cloud Tasks per `03-tech-stack.md`
- Results storage: PostgreSQL + Cloud Storage per `03-tech-stack.md`
- Real-time streaming via SSE for eval progress per `03-tech-stack.md`
- Rate limiting tiers (Free/Pro/Enterprise) per `06-security-isolation.md`
- Pricing tiers (Free/Pro/Team/Enterprise) per `07-business-model.md`

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
Write `projects/eval-platform-design/api-and-frontend.md` covering:

1. **API design** -- REST endpoints for the platform
   - `POST /api/v1/jobs` -- submit artifact + API key + vertical selection
   - `GET /api/v1/jobs/{id}` -- get job status and results
   - `GET /api/v1/jobs/{id}/stream` -- SSE stream for real-time progress
   - `GET /api/v1/jobs` -- list user's jobs (paginated)
   - `POST /api/v1/keys/validate` -- validate API key without running a job
   - `GET /api/v1/verticals` -- list available verticals
   - `GET /api/v1/components` -- browse component library
   - Authentication: JWT-based user sessions
   - Rate limiting per tier per `06-security-isolation.md`

2. **Submission UI** -- the artifact upload experience
   - File upload form (drag-and-drop, file type validation per `06-security-isolation.md`)
   - API key input (secure field, client-side validation for format)
   - Vertical selector (dropdown with descriptions)
   - Submission confirmation with estimated wait time
   - Reference: pipeline architecture from `03-tech-stack.md`

3. **Results dashboard** -- how users view evaluation results
   - Real-time progress streaming during eval (SSE)
   - Final results display: scores, pass/fail, component diffs
   - Historical results list with filtering and sorting
   - Component contribution credit display
   - Export: JSON/CSV download of results

4. **Vertical selector** -- how users choose which evaluation to run
   - Visual cards for each available vertical
   - Per-vertical: description, supported artifact types, example submission
   - MVP: LLM Eval only (other verticals shown as "coming soon")

5. **User accounts and billing**
   - Registration/login (email + password, OAuth optional)
   - Tier display and upgrade flow
   - Usage dashboard (runs used, remaining, billing cycle)
   - Pricing tiers from `07-business-model.md`: Free ($0, 50 runs), Pro ($49, 500 runs), Team ($199, 2000 runs), Enterprise (custom)

6. **Tech stack specifics**
   - Frontend: Next.js with SSR for SEO
   - Backend: FastAPI with async support
   - Database: PostgreSQL for structured data
   - Object storage: Cloud Storage for artifacts and logs
   - Job queue: Google Cloud Tasks
   - Reference: tech stack from `03-tech-stack.md`

7. **References** -- cite specific 158 research files

## Acceptance Criteria
- [ ] `projects/eval-platform-design/api-and-frontend.md` exists
- [ ] Document references FastAPI (`grep -q 'FastAPI' projects/eval-platform-design/api-and-frontend.md`)
- [ ] Document contains `## References` section referencing `eval-web-app-research`
- [ ] Document defines at least 5 REST API endpoints
- [ ] Document covers submission UI, results dashboard, and vertical selector

## Gates Satisfied
- BUILD-08, BUILD-14

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.

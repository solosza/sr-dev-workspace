# API and Frontend Design

## API Design

### Authentication

All API endpoints require JWT-based authentication except `GET /api/v1/verticals` and `GET /api/v1/components` (public, read-only). JWTs are issued on login, expire after 1 hour, and refresh via a separate `/api/v1/auth/refresh` endpoint.

### REST Endpoints

#### `POST /api/v1/jobs` -- Submit Evaluation Job

Accepts multipart form data with artifact file, encrypted API key, and vertical selection.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `artifact` | file | yes | Uploaded file (max 10MB, allowlisted types per `06-security-isolation.md`) |
| `api_key` | string | yes | User's LLM provider API key (encrypted in transit, never persisted) |
| `vertical` | string | yes | Vertical ID (e.g., `llm-eval`, `compliance`, `qa-generation`) |
| `config` | JSON | no | Optional per-vertical configuration overrides |

**Response:** `201 Created` with job ID, estimated wait time, and SSE stream URL.

```json
{
  "job_id": "job_abc123",
  "status": "queued",
  "estimated_wait_seconds": 30,
  "stream_url": "/api/v1/jobs/job_abc123/stream"
}
```

#### `GET /api/v1/jobs/{id}` -- Get Job Status and Results

Returns current job status, and full results when complete.

**States:** `queued` -> `running` -> `completed` | `failed` | `timeout`

**Response (completed):**
```json
{
  "job_id": "job_abc123",
  "status": "completed",
  "vertical": "llm-eval",
  "duration_seconds": 187,
  "results": {
    "scores": { "overall": 0.82, "accuracy": 0.91, "completeness": 0.73 },
    "pass": true,
    "component_diffs": ["added: metric-hallucination-v2", "reused: metric-relevance-v1"],
    "details_url": "/api/v1/jobs/job_abc123/details"
  },
  "created_at": "2026-06-24T10:00:00Z",
  "completed_at": "2026-06-24T10:03:07Z"
}
```

#### `GET /api/v1/jobs/{id}/stream` -- SSE Stream for Real-Time Progress

Server-Sent Events stream that emits progress updates during evaluation.

**Event types:**
- `progress` -- percentage complete, current step description
- `component` -- component built/reused notification
- `score` -- individual metric score as computed
- `done` -- final results payload (same as GET job response)
- `error` -- error description if job fails

```
event: progress
data: {"percent": 35, "step": "Building hallucination metric from _reference/"}

event: component
data: {"action": "built", "name": "metric-hallucination-v2", "source": "_reference/hallucination.md"}

event: score
data: {"metric": "accuracy", "value": 0.91}

event: done
data: {"job_id": "job_abc123", "status": "completed", "scores": {...}}
```

Connection auto-closes on `done` or `error`. Client reconnection supported via `Last-Event-ID` header.

#### `GET /api/v1/jobs` -- List User's Jobs (Paginated)

Returns paginated list of the authenticated user's jobs.

| Param | Type | Default | Description |
|-------|------|---------|-------------|
| `page` | int | 1 | Page number |
| `per_page` | int | 20 | Results per page (max 100) |
| `status` | string | all | Filter by status |
| `vertical` | string | all | Filter by vertical |
| `sort` | string | `created_at:desc` | Sort field and direction |

#### `POST /api/v1/keys/validate` -- Validate API Key

Validates an API key format and optionally tests connectivity to the LLM provider without running a full job. Returns provider name, model access, and estimated token balance if available.

#### `GET /api/v1/verticals` -- List Available Verticals

Public endpoint. Returns all verticals with availability status.

```json
[
  {
    "id": "llm-eval",
    "name": "LLM Evaluation",
    "status": "available",
    "description": "Evaluate LLM applications using DeepEval metrics and custom components",
    "supported_artifacts": [".py", ".json", ".yaml", ".md"],
    "example_submission": "A Python file defining test cases with expected outputs"
  },
  {
    "id": "compliance",
    "name": "Compliance Audit",
    "status": "coming_soon",
    "description": "Automated compliance checking against SSH, NIST, and custom standards"
  }
]
```

#### `GET /api/v1/components` -- Browse Component Library

Public endpoint. Returns available components with filtering by vertical, type, and contributor.

### Rate Limiting

Rate limits enforced per user tier, per `06-security-isolation.md`:

| Tier | Concurrent Jobs | Daily Limit | Monthly Limit |
|------|----------------|-------------|---------------|
| Free | 1 | 5 | 50 |
| Pro | 3 | 50 | 500 |
| Team | 5 | 200 | 2,000 |
| Enterprise | 10+ | Unlimited | Unlimited |

Rate limit headers included in all responses: `X-RateLimit-Limit`, `X-RateLimit-Remaining`, `X-RateLimit-Reset`.

Exceeded limits return `429 Too Many Requests` with `Retry-After` header.

## Submission UI

The submission interface is the primary entry point for new evaluations.

### Layout

Single-page form with three sections in vertical flow:

1. **Vertical selector** (top) -- choose evaluation type before uploading
2. **Artifact upload** (middle) -- drag-and-drop zone with file type validation
3. **API key input** (bottom) -- secure field with format validation and test button

### Artifact Upload

- Drag-and-drop zone with click-to-browse fallback
- File type validation: only allowlisted types per selected vertical (`.py`, `.json`, `.yaml`, `.md`, `.toml`, `.sh`, `.ts`, `.js` per `06-security-isolation.md`)
- Size limit: 10MB max with client-side check before upload
- Progress bar for upload
- File preview: syntax-highlighted code preview for text files

### API Key Input

- Password-type input field (masked by default, toggle to reveal)
- Client-side format validation (checks prefix pattern: `sk-`, `AIza`, etc.)
- "Validate" button triggers `POST /api/v1/keys/validate` to confirm key works
- Key never stored client-side beyond the session; transmitted only over HTTPS

### Submission Flow

1. User selects vertical -> artifact types update to match vertical
2. User uploads artifact -> client validates type and size
3. User enters API key -> optional validation check
4. User clicks "Run Evaluation" -> `POST /api/v1/jobs`
5. Confirmation modal: vertical, artifact name, estimated wait time
6. Redirect to results dashboard with live SSE stream

## Results Dashboard

### Real-Time Progress View

Displayed immediately after job submission or when viewing a running job.

- **Progress bar** with percentage and current step description
- **Live log** of agent actions (component built, metric computed, etc.)
- **Elapsed time** counter
- **Estimated remaining time** based on vertical averages
- SSE connection via `GET /api/v1/jobs/{id}/stream`

### Final Results Display

Shown when job completes:

- **Overall score** -- large, prominent display with pass/fail indicator
- **Per-metric breakdown** -- table of individual metric scores with sparkline trends (if user has historical runs)
- **Component diffs** -- which components were built new vs. reused from library
- **Component contribution credit** -- if the run generated new components that were accepted into the library, display contribution badge
- **Run metadata** -- vertical, duration, artifact name, timestamp

### Historical Results

- **Results list** -- paginated table of all past runs
- **Filters** -- by vertical, status (pass/fail), date range
- **Sort** -- by date, score, duration
- **Search** -- by artifact name or job ID
- **Export** -- JSON or CSV download of selected results via `GET /api/v1/jobs?format=csv`

## Vertical Selector

### Visual Card Layout

Grid of cards, one per vertical. Each card shows:

- **Icon** -- vertical-specific icon (beaker for LLM eval, shield for compliance, browser for QA)
- **Name** -- vertical display name
- **Description** -- one-line summary of what the vertical evaluates
- **Supported artifacts** -- file types accepted
- **Example submission** -- brief description of a typical artifact
- **Status badge** -- "Available" (green) or "Coming Soon" (gray, non-clickable)

### MVP State

- **LLM Eval** -- available, fully functional
- **Compliance Audit** -- coming soon card (non-interactive)
- **QA Generation** -- coming soon card (non-interactive)

Coming soon cards link to a waitlist signup form.

## User Accounts and Billing

### Registration and Login

- **Email + password** registration with email verification
- **OAuth** -- Google and GitHub sign-in (optional, post-MVP)
- **Session management** -- JWT with 1-hour expiry, refresh token with 30-day expiry

### Tier Display and Upgrade

- Current tier shown in account settings and dashboard header
- Usage bar: runs used / runs included this billing cycle
- Upgrade CTA when approaching limit (80% usage)
- Stripe integration for payment processing

### Pricing Tiers

Per `07-business-model.md`:

| Tier | Price | Included Runs | Overage | Concurrent Jobs |
|------|-------|---------------|---------|-----------------|
| Free | $0/mo | 50 runs | Hard limit | 1 |
| Pro | $49/mo | 500 runs | $0.10/run | 3 |
| Team | $199/mo | 2,000 runs | $0.08/run | 5 |
| Enterprise | Custom | Unlimited | Negotiated | 10+ |

### Usage Dashboard

- **Current cycle** -- runs used, runs remaining, days until reset
- **Historical usage** -- monthly run count chart
- **Billing history** -- past invoices, downloadable
- **API key management** -- users can save multiple provider keys (encrypted at rest) for quick submission

## Tech Stack

| Layer | Technology | Rationale |
|-------|-----------|-----------|
| Frontend | Next.js (React, SSR) | SEO via SSR, React ecosystem, API routes for BFF pattern |
| Backend | FastAPI (Python, async) | Aligns with kernel Python ecosystem, high performance with async, Claude Agent SDK Python client integration |
| Database | PostgreSQL | Structured data: users, jobs, results, billing |
| Object Storage | Google Cloud Storage | Artifacts, logs, large result payloads |
| Job Queue | Google Cloud Tasks | Native Cloud Run integration, at-least-once delivery |
| Real-Time | Server-Sent Events (SSE) | Unidirectional streaming, simpler than WebSocket, native browser support |
| Auth | JWT (access + refresh tokens) | Stateless auth, standard library support |
| Payments | Stripe | Industry standard, subscription + metered billing support |

Reference: tech stack decisions from `03-tech-stack.md` -- Cloud Run for containers, FastAPI for backend, Next.js for frontend, PostgreSQL + Cloud Storage for persistence.

## References

- `projects/eval-web-app-research/03-tech-stack.md` -- container orchestration, agent execution model, frontend/backend recommendation, pipeline architecture
- `projects/eval-web-app-research/06-security-isolation.md` -- file type restrictions, artifact size limits, rate limiting tiers, runtime behavioral controls
- `projects/eval-web-app-research/07-business-model.md` -- pricing tiers (Free/Pro/Team/Enterprise), unit economics, per-vertical cost analysis

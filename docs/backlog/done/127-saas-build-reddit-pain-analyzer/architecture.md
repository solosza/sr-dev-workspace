# Reddit Pain Analyzer — System Architecture

## High-Level Architecture

```
┌─────────────────────────────────────────────────────────┐
│ Frontend (Next.js)                                       │
│ ├─ Landing page (marketing)                             │
│ ├─ Auth pages (signup/login)                            │
│ ├─ App dashboard (credit balance, input, results)       │
│ └─ Admin dashboard (usage stats, job monitoring)        │
└────────────────┬────────────────────────────────────────┘
                 │ (HTTPS API calls)
┌────────────────▼────────────────────────────────────────┐
│ Backend (FastAPI)                                        │
│ ├─ Auth service (JWT, password hashing)                 │
│ ├─ User service (CRUD users, credits)                   │
│ ├─ Job service (submit, query, cancel jobs)             │
│ ├─ Payment service (Stripe integration)                 │
│ └─ Results service (fetch, export)                      │
└────────────────┬────────────────────────────────────────┘
                 │ (message queue)
┌────────────────▼────────────────────────────────────────┐
│ Background Worker (Celery/RQ)                           │
│ ├─ Reddit data pipeline                                 │
│ ├─ AI analysis engine (LLM calls)                       │
│ └─ Results storage                                      │
└────────────────┬────────────────────────────────────────┘
                 │ (database queries)
┌────────────────▼────────────────────────────────────────┐
│ Persistent Storage                                       │
│ ├─ PostgreSQL (users, jobs, credits, results)           │
│ ├─ Redis cache (session, job status, rate limiting)     │
│ └─ S3 (result exports, logs)                            │
└─────────────────────────────────────────────────────────┘
```

## Tech Stack

| Layer | Technology | Purpose |
|-------|-----------|---------|
| Frontend | Next.js 14 + React | Web app, landing page, auth |
| Styling | Tailwind CSS | Responsive design |
| Backend | FastAPI (Python) | REST API, business logic |
| Jobs | Celery + Redis | Async job processing |
| Database | PostgreSQL | Users, jobs, credits, results |
| Cache | Redis | Session, rate limiting, job status |
| Storage | S3 / local filesystem | Result exports |
| Auth | JWT + bcrypt | User authentication |
| Payments | Stripe API | Credit purchases |
| LLM | OpenAI API (GPT-4 mini) | Pain point & idea generation |
| Reddit | PRAW (official Reddit API) | Subreddit data scraping |
| Deployment | Docker + AWS/Vercel | Production hosting |

## Database Schema

```sql
-- Users
CREATE TABLE users (
  id UUID PRIMARY KEY,
  email VARCHAR UNIQUE NOT NULL,
  password_hash VARCHAR NOT NULL,
  credits INTEGER DEFAULT 3,
  created_at TIMESTAMP DEFAULT NOW(),
  last_login TIMESTAMP
);

-- Analysis Jobs
CREATE TABLE analysis_jobs (
  id UUID PRIMARY KEY,
  user_id UUID REFERENCES users(id),
  subreddit_url VARCHAR NOT NULL,
  status VARCHAR (queued|processing|complete|failed),
  pain_points JSON,
  sentiments JSON,
  startup_ideas JSON,
  market_scores JSON,
  error_message VARCHAR,
  created_at TIMESTAMP DEFAULT NOW(),
  completed_at TIMESTAMP
);

-- Credit Transactions
CREATE TABLE credit_transactions (
  id UUID PRIMARY KEY,
  user_id UUID REFERENCES users(id),
  amount INTEGER,
  type VARCHAR (signup_bonus|purchase|analysis_cost),
  stripe_transaction_id VARCHAR,
  created_at TIMESTAMP DEFAULT NOW()
);

-- Cache (Redis)
session:{session_id} → {user_data}
job:{job_id} → {job_status, progress}
rate_limit:{user_id}:{hour} → {request_count}
```

## API Endpoints

### Authentication
```
POST /api/auth/signup
  body: { email, password }
  response: { user_id, access_token, credits: 3 }

POST /api/auth/login
  body: { email, password }
  response: { user_id, access_token, credits }

POST /api/auth/logout
  response: { success }
```

### Analysis
```
POST /api/analysis/submit
  headers: { Authorization: Bearer <token> }
  body: { subreddit_url }
  response: { job_id, status: "queued" }

GET /api/analysis/status/:job_id
  response: { job_id, status, progress, error (if failed) }

GET /api/analysis/results/:job_id
  response: { pain_points, sentiments, startup_ideas, market_scores }

POST /api/analysis/export/:job_id
  response: { download_url (JSON file) }
```

### Credits
```
GET /api/user/credits
  response: { balance, transactions (recent) }

POST /api/credits/purchase
  body: { package: "small|medium|large" }
  response: { stripe_session_url }

POST /api/credits/webhook (Stripe)
  body: { stripe_event }
  response: { success }
```

## Job Processing Flow

```
1. User submits subreddit URL
   ├─ POST /api/analysis/submit
   ├─ Validate URL format
   ├─ Deduct 1 credit from user
   ├─ Create job record (status: queued)
   ├─ Queue job to Celery
   └─ Return job_id

2. Worker picks up job
   ├─ Set status: processing
   ├─ Fetch subreddit posts (PRAW API)
   ├─ Extract text from 50-100 top posts
   ├─ LLM: Identify pain points
   ├─ LLM: Generate startup ideas
   ├─ LLM: Score market potential
   ├─ Store results in PostgreSQL
   ├─ Set status: complete
   └─ Cache results in Redis

3. User views results
   ├─ GET /api/analysis/status/{job_id}
   ├─ GET /api/analysis/results/{job_id}
   └─ Download JSON export
```

## Orchestration Integration

The entire analysis pipeline is driven by agent orchestration framework:

**Commands:**
- `/reddit-pain/submit-analysis` — Validates input, creates job
- `/reddit-pain/monitor-jobs` — Monitor queued/processing jobs
- `/reddit-pain/export-results` — Generate JSON export
- `/reddit-pain/admin-report` — Generate daily usage report

**Skills:**
- `reddit-data-pipeline` — Scrape posts, extract text (step 1-3)
- `ai-analysis-engine` — LLM analysis (step 4-6)
- `results-processor` — Store, cache, export (step 7-9)

**State:**
- `analysis_job.json` — Job status, progress, results
- `credit_ledger.json` — Credit transactions audit trail
- `performance_metrics.json` — Cost tracking per analysis

**Gate Contracts:**
- Input: `subreddit_url` valid, user has credits
- Output: `pain_points` and `startup_ideas` lists populated
- Recovery: Preserve `subreddit_data` for retry

## Cost Model

**Per Analysis:**
- Reddit API: $0 (PRAW is free)
- OpenAI GPT-4 mini: ~€0.15 (2-3 API calls)
- PostgreSQL query: <€0.01
- S3 storage: <€0.01
- **Total cost: ~€0.20 per analysis**

**Stripe fees:**
- 2.9% + €0.30 per transaction
- On €5 package: €0.15 fee
- Effective cost: €0.35 per analysis

**Profitability:**
- Revenue per analysis (€5 package, 10 analyses): €0.50
- Total cost per analysis: €0.35
- Gross margin: 30% (target 50% after scaling)

## Monitoring & Observability

- **Logs:** CloudWatch / Papertrail (job errors, LLM costs)
- **Metrics:** Prometheus (analysis latency, job queue depth, LLM cost per analysis)
- **Alerts:** Failed jobs >5 in 1 hour, avg cost > €0.30, error rate > 5%
- **Dashboard:** Grafana (real-time job stats, cost tracking, revenue)

## Security

- **Auth:** JWT tokens with 24h expiry, refresh tokens for long sessions
- **Passwords:** bcrypt with salt (cost factor 12)
- **API:** Rate limiting (10 analyses/hour per user)
- **Data:** PII encrypted at rest, TLS in transit
- **Secrets:** Environment variables, no secrets in code
- **Monitoring:** Log all credit transactions, audit failed auth attempts

## Deployment

- **Frontend:** Vercel (Next.js optimized)
- **Backend:** Docker on AWS ECS / Railway / Render
- **Worker:** Separate container, auto-scaling based on queue depth
- **Database:** AWS RDS PostgreSQL (small instance, ~$50/month)
- **Cache:** Redis Cloud free tier (small datasets)
- **Storage:** S3 or Cloudinary (exports)
- **Total infrastructure:** ~$100-150/month at scale

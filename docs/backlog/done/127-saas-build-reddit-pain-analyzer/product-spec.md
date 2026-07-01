# Reddit Pain Analyzer — Product Specification

## Product Vision

Enable aspiring entrepreneurs to discover validated startup ideas in minutes by analyzing real pain points from Reddit communities using AI. Turn user frustrations into profitable business opportunities.

## User Flows

### Flow 1: First-Time User (Signup → Free Analysis)

```
1. Land on marketing website
2. Click "Try for Free!"
3. Sign up (email, password)
4. Receive 3 free credits
5. Input subreddit URL (e.g., r/entrepreneur)
6. Click "Analyze"
7. Background job starts
8. Redirect to results page
9. View pain points, sentiment scores, startup ideas
10. Export as JSON
```

### Flow 2: Returning User (Purchase Credits → Analyze)

```
1. Login
2. View credit balance (0 credits)
3. Click "Buy Credits"
4. Select package (5/10/20 credits)
5. Stripe payment
6. Credits added to account
7. Input subreddit URL
8. Click "Analyze" (costs 1 credit)
9. View results
10. Export
```

### Flow 3: Analysis Backend (Autonomous Job)

```
1. User submits subreddit URL
2. Job queued to background worker
3. Worker deducts 1 credit from account
4. Fetch subreddit posts (PRAW API)
5. Extract comments and text
6. LLM: Identify pain points
7. LLM: Generate startup ideas
8. LLM: Score market potential
9. Store results in DB
10. Mark job complete
11. User can view results
```

## Core Features (MVP)

| Feature | Description | Priority |
|---------|-------------|----------|
| Landing page | Marketing site with features, pricing, testimonials | High |
| User auth | Email signup/login, password reset | High |
| Credit system | Free 3 credits on signup, purchases via Stripe | High |
| Subreddit input | URL input form with validation | High |
| AI analysis | Posts → pain points → startup ideas | High |
| Results view | Display pain points, sentiment, ideas, scores | High |
| JSON export | Download results as JSON | High |
| Admin dashboard | View usage, credit balance, job status | Medium |

## Data Model

### User
```
id: UUID
email: string (unique)
password_hash: string
credits: integer
created_at: timestamp
last_login: timestamp
```

### Analysis Job
```
id: UUID
user_id: UUID (foreign key)
subreddit_url: string
status: enum (queued, processing, complete, failed)
pain_points: list[string]
sentiments: list[float]
startup_ideas: list[string]
market_scores: list[float]
created_at: timestamp
completed_at: timestamp
```

### Credits Transaction
```
id: UUID
user_id: UUID (foreign key)
amount: integer (positive = purchase, negative = usage)
type: enum (signup_bonus, purchase, analysis_cost)
stripe_transaction_id: string (optional)
created_at: timestamp
```

## Pricing Model

**No subscription.** Pay-per-use with credit system.

| Package | Price | Credits | Cost per Analysis |
|---------|-------|---------|-------------------|
| Signup bonus | Free | 3 | Free |
| Small | €3.99 | 5 | €0.80 per analysis |
| Medium (popular) | €4.99 | 10 | €0.50 per analysis |
| Large | €8.99 | 20 | €0.45 per analysis |

**Unit economics (target):**
- LLM cost per analysis: ~€0.20 (OpenAI GPT-4 mini)
- Server/infra cost per analysis: ~€0.05
- Payment processing: 2.9% + €0.30
- Total cost: ~€0.30
- Revenue per analysis: €0.50-0.80
- Margin: 50-60% gross

## Success Metrics

| Metric | Target | Rationale |
|--------|--------|-----------|
| Signups (month 1) | 500 users | Bootstrap growth |
| Conversion to paid | 15% | 75 users buying credits |
| Repeat usage | 40% | Users analyze 2+ subreddits |
| MRR (month 1) | €1,500-2,000 | Profitability threshold |
| LLM cost efficiency | <€0.25/analysis | Gross margin requirement |

## Non-Functional Requirements

- **Latency:** Analysis completes within 2-5 minutes
- **Availability:** 99.5% uptime
- **Scalability:** Handle 100 concurrent jobs
- **Data privacy:** Comply with GDPR, store PII securely
- **Rate limiting:** Prevent abuse (max 10 analyses per hour per user)
- **Cost efficiency:** Unit economics must stay positive

## Risks & Mitigations

| Risk | Impact | Mitigation |
|------|--------|-----------|
| Reddit API changes | Can't scrape posts | Build fallback using public posts, cache results |
| LLM cost exceeds margin | Unprofitable | Use cheaper models, batch requests, cache responses |
| Low conversion to paid | No revenue | A/B test landing page, offer better results preview |
| High refund rate | Revenue loss | Show sample analysis before purchase, excellent UI |
| Reddit blocks scraping | No data source | Negotiate API access, use official Reddit API only |

## Launch Checklist

- [ ] Landing page live (copy reference site styling)
- [ ] User auth working (email verification)
- [ ] Payment integration (Stripe test + live)
- [ ] Analysis engine functional (end-to-end test)
- [ ] Results export working (JSON format)
- [ ] Admin dashboard built
- [ ] Monitoring/alerting set up (failed jobs, high costs)
- [ ] Documentation written
- [ ] Load test (100 concurrent jobs)
- [ ] Go live

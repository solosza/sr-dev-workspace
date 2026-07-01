# Deployment & Monetization

## Deployment Architecture

### Infrastructure

| Component | Service | Cost/month | Rationale |
|-----------|---------|-----------|-----------|
| Frontend | Vercel | Free | Optimized for Next.js, auto-deployments |
| Backend API | Railway / Render | $12-50 | Simple, auto-scaling, supports Docker |
| Database | Railway PostgreSQL | $15 | Included in Railway, managed backups |
| Cache | Redis Cloud free | Free (5MB) | Small data, upgrade to paid if needed |
| Storage | S3 / Cloudinary | $5-10 | Export files, backups |
| LLM API | OpenAI | Variable (€0.10-0.50/day) | Based on usage |
| Monitoring | Datadog free | Free | Logs, metrics, alerts |
| **Total** | | **~$50-100** | Profitable at €1,500+ MRR |

### Deployment Pipeline

```
Code commit to main
         ↓
GitHub Actions
  ├─ Run tests
  ├─ Build frontend (Vercel auto)
  ├─ Build backend Docker image
  └─ Push to Railway
         ↓
Automatic deployment
  ├─ Frontend live (Vercel)
  ├─ Backend live (Railway)
  └─ Database migrations (auto)
         ↓
Health check
  ├─ API endpoint responds
  ├─ Database connected
  └─ LLM API reachable
         ↓
Production live
```

### Environment Setup

**Development:**
```bash
NEXT_PUBLIC_API_URL=http://localhost:8000
DATABASE_URL=postgresql://user:pass@localhost/reddit_analyzer_dev
REDIS_URL=redis://localhost:6379
OPENAI_API_KEY=sk-...
STRIPE_SECRET_KEY=sk_test_...
JWT_SECRET=<dev-secret>
```

**Production:**
```bash
NEXT_PUBLIC_API_URL=https://api.redditpainanalyzer.com
DATABASE_URL=<railway-postgres-url>
REDIS_URL=<redis-cloud-url>
OPENAI_API_KEY=sk-...
STRIPE_SECRET_KEY=sk_live_...
JWT_SECRET=<prod-secret>
```

## Monetization Model

### Revenue Streams

**Primary: Credit-based pay-per-use**
- No subscription (users only pay when analyzing)
- 3 free credits on signup
- Purchase packages: 5/10/20 credits
- 1 credit = 1 analysis

**Secondary (future):**
- API access (programmatic analysis)
- White-label licensing
- Premium features (batch analysis, competitive benchmarking)

### Pricing Strategy

**Goal: Positive unit economics**

| Metric | Target |
|--------|--------|
| Cost per analysis | €0.10-0.15 |
| Revenue per analysis | €0.40-0.80 |
| Gross margin | 60-80% |
| Break-even MRR | €500 |
| Target MRR (Month 3) | €2,000 |

**Price optimization:**
- Start at €0.50/credit (€5 for 10-pack)
- Monitor conversion rate
- A/B test: €0.45, €0.55, €0.60
- Adjust based on willingness-to-pay

### Cost Structure

**Variable costs per analysis:**

| Component | Cost |
|-----------|------|
| OpenAI API | €0.08 |
| Database ops | €0.01 |
| Storage | €0.01 |
| Infrastructure | €0.02 |
| **Total** | **€0.12** |

**Fixed costs per month:**
- Frontend hosting: Free (Vercel)
- Backend hosting: €50
- Database: €15
- Monitoring: Free
- Domain: €10
- **Total: €75**

**Profitability:**
```
At 100 analyses/month:
  Revenue: 100 × €0.50 = €50
  Variable cost: 100 × €0.12 = €12
  Fixed cost: €75
  Net: €50 - €12 - €75 = -€37 (loss)

At 500 analyses/month:
  Revenue: 500 × €0.50 = €250
  Variable cost: 500 × €0.12 = €60
  Fixed cost: €75
  Net: €250 - €60 - €75 = €115 (profit!)

At 2,000 analyses/month (€2k MRR):
  Revenue: 2000 × €0.50 = €1,000
  Variable cost: 2000 × €0.12 = €240
  Fixed cost: €75
  Net: €1,000 - €240 - €75 = €685 (strong profit!)
```

**Ramp path:**
- Month 1: 100 signups, 20% conversion, ~150 analyses → -€37
- Month 2: 300 signups, 25% conversion, ~300 analyses → +€15
- Month 3: 500 signups, 30% conversion, ~600 analyses → +€180
- Month 6: 1,000 signups/month, 35% conversion → +€600+/month

## Stripe Integration

### Setup

1. Create Stripe account
2. Add API keys to env vars
3. Create 3 products (5/10/20 credit packages)
4. Configure webhooks (payment_intent.succeeded)
5. Test with test cards (4242 4242 4242 4242)

### Webhook Handling

```python
@app.post("/api/webhooks/stripe")
async def stripe_webhook(request: Request):
    event = stripe.Event.construct_from(
        json.loads(await request.body()), stripe.api_key
    )

    if event["type"] == "payment_intent.succeeded":
        payment_intent = event["data"]["object"]
        user_id = payment_intent["metadata"]["user_id"]
        credits = payment_intent["metadata"]["credits"]

        # Add credits to user account
        db.add_credits(user_id, credits)
        db.log_transaction(user_id, credits, "purchase", payment_intent["id"])

    return {"status": "success"}
```

### Error Handling

- Card declined: Show error, allow retry
- Payment timeout: Queue and retry (Celery)
- Webhook timeout: Stripe retries automatically
- Stripe API outage: Queue, alert admin, manual reconciliation

## Launch Strategy

### Phase 1: MVP Launch (Week 1-2)
- Deploy to production (Railway)
- Landing page live (Vercel)
- 50 beta users via email list
- Free 10 credits for beta testers
- Collect feedback

### Phase 2: Early Access (Week 3-4)
- Open to public with limited capacity (100 analyses/day)
- Monitor: costs, errors, performance
- Optimize: slow jobs, expensive LLM calls
- Fix bugs

### Phase 3: Public Launch (Week 5)
- Remove capacity limits
- Marketing: Product Hunt, Hacker News, Twitter
- Goal: 500 signups in first month
- Target: 150-300 analyses (€75-150 revenue)

### Phase 4: Scaling (Month 2-3)
- Implement caching (reduce costs)
- Add batch analysis
- Expand to other data sources (Twitter, Discord)
- Improve UX based on feedback

## Monitoring & Alerts

**Key metrics to track:**

| Metric | Alert Threshold |
|--------|-----------------|
| Cost per analysis | > €0.25 |
| Error rate | > 5% |
| API uptime | < 99% |
| Job processing time | > 10 min |
| Failed payments | > 5/day |
| Stripe balance | < €100 |

**Dashboard:**
- Datadog (free tier): logs, metrics
- Stripe dashboard: transaction monitoring
- Railway console: CPU, memory, logs
- Vercel analytics: page load times

## Legal / Compliance

- **Terms of Service:** Payment terms, acceptable use, data retention
- **Privacy Policy:** Data collection, GDPR compliance
- **Reddit API:** Comply with Terms of Use (no reselling data)
- **Payment:** PCI compliance (Stripe handles)
- **Taxes:** VAT for EU users, sales tax for US

## Contingencies

| Risk | Mitigation |
|------|-----------|
| OpenAI rate limit | Implement retry queue, use cheaper model |
| Reddit API changes | Monitor Reddit developers forum, build fallback |
| LLM cost spike | Set cost limits per analysis, alert admin |
| High refund rate | Clear results preview before purchase |
| Server outage | Uptime monitoring, automated failover (optional) |

# Local Business AI Pipeline — Research Report

## Executive Summary

**Verdict: Highly viable. Every step is automatable, unit economics are strong, and the addressable market is massive (5M+ US businesses with bad/missing websites).** The kernel pipeline maps perfectly: backlog = city + category, tasks = scrape → qualify → generate → outreach → follow up. The bottleneck is sales conversion (human-in-the-loop for closing), not lead gen or site generation. Recommend starting with HVAC/plumbing in 3 test cities, website builds at $800-$1,200, reputation management at $300-$500/month recurring.

---

## 1. Pipeline Architecture

### How The Loop Runs This

| Pipeline Component | Local Business Equivalent |
|-------------------|--------------------------|
| Backlog item | Target: city + business category (e.g., "HVAC in Phoenix") |
| Task decomposition | scrape → qualify → generate site mockup → cold outreach → follow up → close |
| run-task.sh | Each step as autonomous agent task |
| Gate contract | Lead quality checks: has email? rating in range? no existing site? |
| Attestation | Proof of outreach: emails sent, responses, conversions |
| Lessons | Per-category learning: which industries close fastest, what email copy converts |

### Step-by-Step Pipeline

| Step | Tool | Automation | Notes |
|------|------|-----------|-------|
| 1. Scrape Google Maps | Outscraper / Apify / google-maps-scraper (open source) | **FULL** | 50+ data points per business: name, phone, email, rating, reviews, website, hours |
| 2. Qualify leads | Claude API | **FULL** | Filter: rating 3.5-4.2, 20+ reviews, no website or outdated, high-margin category |
| 3. Enrich contacts | Hunter.io / Apollo / Enrichment APIs | **FULL** | Find owner email, LinkedIn, decision-maker name |
| 4. Generate site mockup | AI builders (Framer, Lovable) or custom | **HIGH** | Pull business data → generate 5-page site in <1 hour |
| 5. Personalized outreach | Claude API + email service | **FULL** | Reference specific rating, review count, competitor comparison |
| 6. Follow up | Automated drip sequence | **FULL** | 3-touch sequence over 7 days |
| 7. Close deal | **HUMAN** | **Manual** | Sales call, contract, payment |
| 8. Build final site | AI builder + review | **HIGH** | 2-4 hours per client site |
| 9. Reputation mgmt | Claude API + review monitoring | **FULL** | Auto-respond to reviews, generate review requests |

### Automation Coverage

- Steps 1-6 and 9: **Fully automatable** — the loop handles these
- Steps 7-8: **Human-in-the-loop** — closing requires human, final site needs review
- **Estimated 85% automation**, 15% human touch (sales + QA)

---

## 2. Technical Feasibility

### Google Maps Scraping (2026)

| Tool | Type | Cost | Output |
|------|------|------|--------|
| Outscraper | SaaS API | $0.002/result | Name, email, phone, rating, reviews, website, hours |
| Apify Google Maps AI Analyzer | SaaS | $5/1K results | Full business analysis with AI enrichment |
| google-maps-scraper (open source) | Self-hosted | Free (proxy costs) | 50+ data points, no recurring fees |
| Scrap.io | SaaS | $49-$199/mo | Unlimited scraping with filters |

**Anti-scraping challenges:** Google employs CAPTCHAs, IP blocking, rate limiting. Mitigations: proxy rotation, browser fingerprinting, headless browsers with stealth plugins. The open-source scraper (omkarcloud) handles this with built-in evasion.

### Website Generation Speed

| Builder | Time per Site | Cost | Quality |
|---------|--------------|------|---------|
| Framer AI | 15-30 min | $5-$20/mo per site | HIGH — professional templates |
| Lovable | 10-20 min | Free-$20/mo | HIGH — AI generates from description |
| Custom (HTML/CSS via Claude) | 30-60 min | API costs only (~$0.50) | MEDIUM — needs design polish |
| Webflow | 1-2 hours | $14-$39/mo per site | HIGH — most professional |

### Cold Email Deliverability

| Metric | Benchmark | Notes |
|--------|-----------|-------|
| Open rate | 20-35% | With personalization + warm-up |
| Reply rate | 3-8% | Higher with specific business data |
| Positive interest | 1-3% | Of total sent |
| Close rate | 20-40% | Of interested leads |
| Emails/day (safe) | 200-500 | Per warmed domain, multiple domains scale this |

### CAN-SPAM Compliance

- B2B cold email is legal under CAN-SPAM (no opt-in required for business emails)
- Must include: physical address, unsubscribe link, honest subject lines
- Cannot use deceptive headers or misleading subject lines
- State laws vary (California CCPA adds requirements)

---

## 3. Revenue Model

### Per-Client Revenue

| Service | One-Time | Monthly Recurring |
|---------|----------|-------------------|
| Basic website (5 pages) | $500-$800 | $0 |
| Website + booking system | $1,000-$1,500 | $0 |
| Website + monthly hosting/updates | $800-$1,200 | $150-$200/mo |
| Reputation management only | $200 setup | $300-$500/mo |
| Full bundle (site + reputation) | $1,000-$1,500 | $300-$500/mo |
| Google Business Profile optimization | $200-$500 | $150-$500/mo |

### Unit Economics Per Pipeline Run

| Metric | Value |
|--------|-------|
| Scraping cost per 1,000 businesses | $2-$10 |
| Email enrichment per lead | $0.02-$0.10 |
| AI outreach per email (Claude API) | $0.01-$0.05 |
| Website generation cost | $0.50-$20 |
| **Total cost per qualified lead** | **$0.10-$0.50** |
| **Total cost per acquired client** | **$5-$25** |
| **Revenue per client (first year)** | **$2,400-$7,800** |
| **ROI per client** | **100x-1,500x** |

### Scale Projections

| Timeline | Clients | Monthly Revenue | Monthly Costs | Profit |
|----------|---------|----------------|---------------|--------|
| Month 1 | 3-5 | $2,400-$5,000 | $200 | $2,200-$4,800 |
| Month 3 | 10-15 | $5,000-$10,000 | $500 | $4,500-$9,500 |
| Month 6 | 25-30 | $10,000-$18,000 | $1,000 | $9,000-$17,000 |
| Month 12 | 50+ | $20,000-$35,000 | $2,000 | $18,000-$33,000 |

Recurring revenue compounds — each new client adds $300-$500/month permanently.

---

## 4. Best Target Categories

| Category | Lead Volume | Close Rate | Revenue/Client | Score |
|----------|------------|------------|----------------|-------|
| **HVAC** | HIGH | HIGH (urgent need) | $1,200+ site + $400/mo | **Best** |
| **Plumbing** | HIGH | HIGH | $1,000+ site + $350/mo | **Best** |
| **Roofing** | MEDIUM | MEDIUM-HIGH | $1,500+ site + $400/mo | Good |
| **Auto repair** | HIGH | MEDIUM | $800+ site + $300/mo | Good |
| **Pest control** | MEDIUM | MEDIUM | $800+ site + $300/mo | Moderate |
| **Dental/Medical** | LOW | LOW (longer sales cycle) | $2,000+ site + $500/mo | Harder |
| **Restaurants** | HIGH | LOW (tight margins) | $500 site + $200/mo | Skip |

**Start with:** HVAC and plumbing — urgent service needs, owners respond fast, high margins, willing to pay for leads.

---

## 5. Similar Monetizable Patterns

| Pattern | Data Source | Service | Revenue |
|---------|-----------|---------|---------|
| Google Maps bad websites | Google Maps API | Website generation | $800-$1,500/client |
| Low-rated businesses | Google Maps reviews | Reputation management | $300-$500/mo |
| Businesses without booking | Google Maps + Yelp | Booking system integration | $200-$400/mo |
| Outdated social media | Facebook/Instagram | Social media management | $500-$1,000/mo |
| Missing SEO | Google Search Console | Local SEO optimization | $500-$1,500/mo |
| No video presence | YouTube | Video production for business | $500-$1,000/video |

---

## 6. Legal Considerations

| Area | Risk | Mitigation |
|------|------|------------|
| Google Maps scraping | MEDIUM — ToS violation technically | Use official APIs where possible, rate limit, rotate IPs |
| CAN-SPAM | LOW | B2B cold email is legal with required disclosures |
| State laws (CCPA) | LOW | Applies to consumer data, B2B contact info generally exempt |
| Business licensing | LOW | Web development services don't require special licensing in most states |
| Google ToS enforcement | LOW | Google rarely enforces against small-scale scrapers; use API when available |

---

## 7. Recommended Strategy

### Phase 1: Validate (Weeks 1-2)
1. Pick 3 test cities (mid-size: 200K-500K population)
2. Pick 2 categories: HVAC + plumbing
3. Scrape 1,000 businesses per city (3,000 total)
4. Qualify down to ~300 leads (10% qualification rate)
5. Send 300 personalized emails
6. Target: 5-10 interested leads, 2-3 clients
7. Build 2-3 websites manually to validate quality bar

### Phase 2: Automate (Weeks 3-6)
8. Build the domain spec (local-business-pipeline)
9. Automate scraping → qualification → outreach as pipeline tasks
10. Add reputation management as recurring upsell
11. Scale to 10 cities, 500 emails/day

### Phase 3: Scale (Month 2-3)
12. Hire VA for sales calls ($5-$10/hour offshore)
13. Scale to 50 cities
14. Add Google Business Profile optimization as service
15. Target 30+ clients, $15K+/month

### Go/No-Go Decision Points

| Checkpoint | Metric | Go | No-Go |
|-----------|--------|-----|-------|
| After 300 emails | Reply rate | >3% | <1% |
| After 10 interested leads | Close rate | >20% | <10% |
| After 3 clients | Client satisfaction | repeat/referral | churn |
| After month 1 | Revenue | >$2,000 | <$500 |

**Bottom line:** This is the most immediately monetizable pattern in the batch. Unlike YouTube or game content (which need months to build audience), local business services generate revenue from client #1. The loop handles lead gen and outreach; the human handles closing. At 85% automation, the bottleneck is sales capacity, not pipeline throughput.

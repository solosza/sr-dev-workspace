# Research Local Business AI Pipeline — Google Maps Lead Gen

## Status
Open

## Priority
High — proven $5K-15K/month model, 5M+ addressable businesses on Google Maps, every step automatable via the loop

## Summary
Research the feasibility of an autonomous pipeline that finds local businesses on Google Maps with bad/missing websites and low ratings, auto-generates professional websites and reputation management services, and runs cold outreach at scale. The entire workflow — lead scraping, qualification, website generation, outreach, review management — maps directly to the loop (backlog → tasks → autonomous execution). One pipeline run = one client acquisition cycle. Also research similar patterns where AI + public data + automated outreach = recurring revenue at scale.

## Requirements

### Pipeline Architecture (How The Loop Runs This)
- **Lead discovery:** Scrape Google Maps for businesses by category + city (HVAC, plumbing, electrical, roofing, pest control, auto repair)
- **Qualification:** AI filters targets — ratings 3.5-4.2, 20+ reviews, no website or outdated URL, high-margin service categories
- **Website generation:** Auto-build professional site from Google Maps data (services, reviews, hours, photos) using AI website builders (Framer, Webflow, Lovable, or custom)
- **Cold outreach:** Personalized emails referencing specific business data (rating, review count, missing website) at 500/day
- **Reputation management:** Monitor reviews, auto-respond via AI, implement review generation system
- Each step = a task in the loop. Each business = one pipeline run. Scale = N parallel pipeline runs.

### Revenue Model
- **Website builds:** $500-2,000 per client (one-time)
  - Basic 5-page: $500-800
  - Full with booking: $1,000-1,500
  - Website + monthly maintenance: $1,200 upfront + $200/month
- **Reputation management:** $300-800/month per client (recurring)
  - Monitor reviews, AI-generated responses, review generation system
  - 10 clients × $500/mo = $5,000/mo recurring
- **Combined projections:**
  - Month 1: 5 clients × $800 = $4,000
  - Month 3: 15 clients = $12,000
  - Month 6: 30 clients = $18,000+ (with recurring stacking)

### Technical Feasibility
- **Google Maps scraping:** Tools like Outscraper, PhantomBuster — pull names, emails, phones, ratings, review counts per city
- **Website generation speed:** Under 1 hour per site with AI builders — can the loop automate this end-to-end?
- **Cold email at scale:** Personalized outreach via Claude API — 500 emails/day, 3% response rate = 15 interested/day
- **Review response automation:** Claude generates human-sounding review responses in 30 seconds each
- **What can be fully automated vs what needs human touch?** (Sales calls, contract signing, payment processing)

### Similar Monetizable Patterns to Research
- **Restaurant menu/ordering sites** — same pattern, different vertical
- **Real estate agent sites** — agents with good sales but terrible web presence
- **Medical/dental practice sites** — high-margin, often outdated websites
- **Auto dealership reputation management** — reviews are critical for car sales
- **Any local service business with high margins + bad digital presence**
- What other public data sources (besides Google Maps) expose businesses that need help?

### Platform & Legal
- Google Maps scraping — ToS compliance, rate limiting
- CAN-SPAM compliance for cold outreach at scale
- Business licensing requirements for web development services
- Can the outreach be fully automated or does it need human-in-the-loop for compliance?

### The Loop Integration
- How does this map to the kernel pipeline?
  - Backlog item = target city + business category
  - Task decomposition = scrape → qualify → generate site → outreach → follow up
  - Autonomous cycling = process N businesses per run
  - Each "client acquired" is a completed pipeline
- Can we build a domain spec for this? (local-business-pipeline spec)
- What's the unit economics per pipeline run? (API costs vs expected revenue per client)

## References
- Source: X post (2026-04-28) — "$15,000/month finding clients on Google Maps with AI"
- The loop: execute-pipeline skill (`.claude/skills/execute-pipeline/`)
- Similar autonomous patterns: backlog 064 (game content pipeline), backlog 065 (YouTube content pipeline)
- Website cloner skill: `.claude/skills/website-cloner/` (potential reuse for site generation)

## Task Builder Input
- **Deliverable:** Research report covering pipeline architecture, revenue model, technical feasibility, similar monetizable patterns, legal considerations, and go/no-go recommendation with projected unit economics per pipeline run
- **Location:** `subproject:local-business-pipeline`
- **Scope:** RESEARCH
- **Constraints:** Research only — no building yet. Need real data on Google Maps scraping tools, AI website builder APIs, cold email deliverability rates, and honest assessment of conversion rates. Should identify which business category has the best ratio of (lead availability) × (close rate) × (revenue per client). The BUILD phase would be a separate backlog after this research lands.

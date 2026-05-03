# MVP Plan — AI Resume & Career Coach

**Pick**: #1 from scored candidate matrix (Score: 60/70)
**Codename**: CareerAgent
**Date**: 2026-04-08

---

## Product Vision

CareerAgent is an AI-native career copilot that replaces fragmented resume builders, cover letter generators, and interview prep tools with a single intelligent agent that knows your career trajectory, understands the job market, and generates tailored application materials in seconds. Unlike incumbents that bolt AI onto template-based products, CareerAgent IS the AI — there is no template picker, no field-by-field form. You talk to it, it builds your career strategy.

---

## MVP Feature Set

Ruthlessly scoped to the minimum that delivers value and commands $19/month from day 1.

### Launch Features (MVP)

1. **LinkedIn/Resume Import** — paste LinkedIn URL or upload existing resume. AI extracts full career model (roles, skills, accomplishments, trajectory).
2. **Job Description Analysis** — paste any job posting. AI identifies key requirements, cultural signals, skill gaps, and ATS keywords.
3. **Tailored Resume Generation** — one click generates a resume optimized for the target job. ATS-friendly formatting, quantified accomplishments, keyword alignment.
4. **Tailored Cover Letter** — AI writes a cover letter that connects your experience to the specific role, avoids generic filler.
5. **Application Dashboard** — track jobs applied, status, resume variants used. Simple kanban (Applied → Interview → Offer → Rejected).
6. **AI Career Chat** — conversational interface for ad-hoc questions: "Should I apply for this role?", "How do I explain my career gap?", "What salary should I ask for?"

### Explicitly Cut from MVP

- Voice-based mock interviews (Phase 2 — high token cost, needs voice infra)
- Proactive job matching/alerts (Phase 2 — needs scraping pipeline)
- LinkedIn profile optimization (Phase 2 — needs LinkedIn API or browser extension)
- A/B testing resume variants (Phase 3 — needs scale data)
- Team/recruiter features (Phase 3 — B2B pivot if warranted)

---

## Tech stack

| Layer | Choice | Rationale |
|-------|--------|-----------|
| **Frontend** | Next.js 15 + React 19 + Tailwind CSS | Fast to build, SSR for SEO, responsive |
| **Backend** | Next.js API routes + tRPC | Co-located with frontend, type-safe |
| **Database** | Supabase (Postgres + Auth + Storage) | Auth, DB, file storage in one. Free tier generous |
| **AI/LLM** | Claude API (Sonnet for generation, Haiku for classification) | Best quality for long-form writing, structured output |
| **Resume Parsing** | LLM-based extraction (Claude) | More accurate than regex/ML parsers, handles edge cases |
| **PDF Generation** | react-pdf or Puppeteer | ATS-friendly PDF output with clean formatting |
| **Payments** | Stripe | Standard. Checkout, subscriptions, customer portal |
| **Hosting** | Vercel | Zero-config Next.js deployment, edge functions |
| **Email** | Resend | Transactional email (welcome, receipts, weekly digest) |
| **Analytics** | PostHog | Product analytics, feature flags, session replay |

Estimated monthly infrastructure cost at launch: **$50-150/month** (Vercel Pro $20, Supabase Pro $25, LLM API usage $5-100 depending on users).

---

## Architecture

```
┌─────────────────────────────────────────────────┐
│                   Next.js App                    │
│  ┌───────────┐ ┌──────────┐ ┌────────────────┐ │
│  │ Dashboard  │ │ Resume   │ │ Career Chat    │ │
│  │ (Kanban)   │ │ Builder  │ │ (Streaming)    │ │
│  └─────┬─────┘ └────┬─────┘ └───────┬────────┘ │
│        │             │               │           │
│  ┌─────┴─────────────┴───────────────┴────────┐ │
│  │              tRPC API Layer                 │ │
│  └─────────────────┬──────────────────────────┘ │
└────────────────────┼────────────────────────────┘
                     │
     ┌───────────────┼───────────────┐
     │               │               │
┌────▼────┐   ┌──────▼──────┐  ┌────▼─────┐
│ Supabase │   │ Claude API  │  │  Stripe  │
│ (DB/Auth)│   │ (LLM Core)  │  │(Payments)│
└──────────┘   └─────────────┘  └──────────┘
```

**Key flows**:
- **Import**: User pastes LinkedIn URL → Claude extracts structured career data → stored in Supabase
- **Generate**: User pastes job description → Claude analyzes + generates resume/cover letter → PDF rendered → stored in Supabase Storage
- **Chat**: Streaming Claude conversation grounded in user's career data + target job context

---

## Go-to-Market

### First 100 Users Strategy

**Week 1-2: Seed audience**
- Post on r/resumes (1.2M members), r/cscareerquestions (1.1M), r/jobs
- Show before/after resume comparisons (AI-generated vs original)
- Offer free premium for first 50 signups in exchange for feedback

**Week 3-4: Content engine**
- Publish 3 SEO articles/week: "How to Write a Resume for [Role]", "AI Resume Tips", "[Industry] Resume Examples"
- Short-form video on TikTok/LinkedIn showing the AI generating a tailored resume in 30 seconds

**Week 5-8: Product Hunt + press**
- Product Hunt launch (target top 5 of the day)
- Pitch to TechCrunch, The Verge, Hacker News (the "AI career agent" angle is timely)
- Twitter/X threads showing real results (anonymized)

**Week 9-12: Paid acquisition test**
- Google Ads on high-intent keywords: "AI resume builder", "resume help", "cover letter generator"
- Expected CPC: $2-5, expected conversion: 5-10%, target CAC: $20-50

### Pricing

| Tier | Price | Features |
|------|-------|----------|
| **Free** | $0 | 1 resume + 1 cover letter + basic chat (10 msgs/day) |
| **Pro** | $19/month or $149/year | Unlimited resumes, cover letters, chat. Application tracking. Priority generation. |
| **Lifetime** | $299 (launch promo) | Everything in Pro, forever. Early adopter hook. |

### Distribution Advantages

- **SEO moat**: Resume-related keywords have massive search volume (110K/month for "resume builder" alone) and incumbents have weak content strategies
- **Viral loop**: "Built with CareerAgent" watermark on free-tier resumes drives organic discovery
- **Network effect (weak)**: Career coaches and bootcamps recommend to students → B2B2C channel

---

## Timeline

| Phase | Weeks | Milestone |
|-------|-------|-----------|
| **MVP Build** | 1-6 | Core app: import, generate, chat, dashboard, auth, payments |
| **Private Beta** | 7-8 | 50 beta users, collect feedback, fix critical issues |
| **Public Launch** | 9 | Product Hunt, Reddit, social media blitz |
| **Iterate** | 10-12 | Top feedback items, SEO content engine, paid acquisition test |
| **Phase 2 Start** | 13+ | Voice interviews, job matching, LinkedIn optimizer |

**First paying customer**: Week 9 (public launch)
**Target 100 paying users**: Week 12
**Target $1K MRR**: Week 14-16

---

## Revenue Model

### Pricing Tiers

- **Free**: Acquisition funnel. Limited usage drives conversion.
- **Pro ($19/month)**: Core revenue. Priced above incumbents ($10-15) because the AI delivers 10x more value.
- **Lifetime ($299)**: Cash injection at launch. Creates evangelists.

### Projected ARR

| Timeframe | Paying Users | MRR | ARR |
|-----------|-------------|-----|-----|
| 6 months | 200-500 | $3,800-$9,500 | $46K-$114K |
| 12 months | 1,000-3,000 | $19K-$57K | $228K-$684K |
| 24 months | 5,000-15,000 | $95K-$285K | $1.14M-$3.42M |

**Unit economics target**: LTV > 3x CAC. At $19/month with 6-month average retention = $114 LTV. Target CAC: $20-35.

### Gross Margin

- LLM API cost per user: ~$1-2/month (resume generation + chat)
- Infrastructure: ~$0.50/user/month at scale
- Stripe fees: 2.9% + $0.30
- **Estimated gross margin: 80-85%**

---

## Risks and Mitigations

### Risk 1: LLM Cost Scaling
**Threat**: Heavy chat users could push per-user API costs above $5/month, destroying margins.
**Mitigation**: Use Haiku for classification/routing, Sonnet only for generation. Cache common resume patterns. Implement soft rate limits on chat (50 msgs/day on Pro). Monitor per-user cost and adjust tiers if needed. Fine-tune a smaller model for common operations as volume grows.

### Risk 2: Job Board Data Access
**Threat**: LinkedIn, Indeed, and Glassdoor restrict scraping. Without job data, the "analyze any job posting" feature relies on manual paste.
**Mitigation**: MVP uses paste-only (user copies job description). Phase 2 explores: (a) official job board APIs where available, (b) browser extension that reads the current job page, (c) partnerships with smaller job boards (Lever, Greenhouse job pages are public). Manual paste is viable — users already copy job descriptions into ChatGPT.

### Risk 3: Incumbent Response
**Threat**: LinkedIn builds this natively with their data advantage, or Teal/Rezi raise large rounds and copy the approach.
**Mitigation**: Speed is the moat. Ship in 6 weeks, build brand and user base before incumbents react. LinkedIn is historically slow to ship new consumer products (took 2+ years to modernize LinkedIn Learning). Teal/Rezi are template-first architectures — rebuilding AI-native is a rewrite, not an iteration. Our data flywheel (every resume generated improves the system) compounds daily.

---

## Reference

- Source analysis: `projects/ai-clone-opportunity/candidate-matrix.md`
- Deep dive: `projects/ai-clone-opportunity/top-3-deep-dives.md`
- Website cloner skill (for ripping incumbent UI): backlog 034 — `docs/backlog/034-domain-build-website-cloner-skill.md`

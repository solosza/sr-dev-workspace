# Mailbox Store AI — Pricing Model

**Date:** 2026-04-23
**Source Task:** `tasks/mailbox-store-ai/005-build-write-pricing-model.md`
**Depends On:** `docs/research/mailbox-store-ai-competitors.md`, `docs/research/mailbox-store-ai-opportunities.md`

---

## 1. Competitor Pricing Benchmarks

| Solution | Monthly Cost | Model | AI? |
|----------|-------------|-------|-----|
| PostalMate | $95/month | Per-location subscription | No |
| ShipRite NEXT | ~$100-200+/month (est.) | License + annual support | No |
| Bullship | $50/month | Per-location subscription | No |
| PostalPoint | Free–$100/month cap | Revenue share (10% shipping profit) | No |
| ShipStation | $9.99–$229.99/month | Tiered by shipment volume | No |
| Stamps.com | $19.99/month | Subscription + postage | No |
| Pirate Ship | Free | Postage markup only | No |

**Key insight:** The market currently pays $50-$95/month for non-AI POS/shipping software. No competitor offers AI capabilities. An AI-powered platform that demonstrably saves 2-4 hours/day (worth $300-$600/month at $15-$30/hour) can command a meaningful premium.

---

## 2. Pricing Tiers

### Starter — $79/month per location

**Target:** Solo-operator stores with <100 packages/day who want automated notifications without the full platform.

| Feature | Included |
|---------|----------|
| Barcode scan → auto-log | Yes |
| SMS notifications (up to 500/month) | Yes |
| Email notifications (unlimited) | Yes |
| Package photo capture | Yes |
| Dashboard (today's packages) | Yes |
| Daily summary report | Yes |
| Customer preference management | Yes |
| Pickup confirmation | Yes |
| SMS overage rate | $0.01/SMS |
| Support | Email (48hr response) |

**Rationale:** Priced below PostalMate ($95) to lower switching friction. At $79/month, the store owner pays less than their current non-AI POS while getting automated notifications that save 1-2 hours/day. The 500 SMS/month cap covers ~25 packages/day (typical for small stores). This tier is the foot-in-the-door — prove value, then upsell.

### Professional — $149/month per location

**Target:** Busy stores with 100-300+ packages/day, 200+ mailbox holders, who need full automation and analytics.

| Feature | Included |
|---------|----------|
| Everything in Starter | Yes |
| SMS notifications (up to 2,000/month) | Yes |
| Shelf/bin assignment suggestions | Yes |
| Aging package alerts (auto-remind customers) | Yes |
| Weekly analytics report (volume trends, dwell time, peak hours) | Yes |
| Customer communication templates (customizable) | Yes |
| Multi-user access (up to 5 staff accounts) | Yes |
| API access (for custom integrations) | Yes |
| SMS overage rate | $0.008/SMS |
| Support | Priority email (24hr) + phone |

**Rationale:** Priced at $149/month — a $54 premium over PostalMate but with AI automation that PostalMate completely lacks. At 200 packages/day, the time savings (3-4 hrs/day × $20/hr = $60/day = ~$1,200/month) deliver 8x ROI on the subscription. The analytics and multi-user features justify the premium for larger operations.

### Enterprise — Custom pricing (starting $249/month)

**Target:** Multi-location operators (2+ stores), franchise groups, or high-volume single locations (500+ packages/day).

| Feature | Included |
|---------|----------|
| Everything in Professional | Yes |
| SMS notifications (unlimited) | Yes |
| Multi-location dashboard (consolidated view) | Yes |
| Cross-location analytics and benchmarking | Yes |
| Shipping Advisor Agent (Phase 2) | Early access |
| CMRA Compliance Agent (Phase 4) | Early access |
| Custom integrations (POS, carrier APIs) | Included |
| Dedicated account manager | Yes |
| SLA (99.9% uptime) | Yes |
| Support | Phone + Slack channel |

**Rationale:** Enterprise is the upsell path for multi-location operators. Custom pricing allows margin flexibility based on location count and volume. Starting at $249/month for 2 locations ($125/location) provides a volume discount while capturing higher total contract value. Enterprise customers get early access to future agents (Shipping Advisor, Compliance), creating lock-in and reducing churn.

---

## 3. Pricing Structure: Monthly SaaS Per-Location

**Model chosen:** Flat monthly SaaS fee per location (not per-transaction, not revenue share).

| Structure Considered | Verdict | Reason |
|---------------------|---------|--------|
| Monthly SaaS per-location | **Selected** | Predictable revenue, simple to explain, aligns with industry norm (PostalMate, Bullship both use this) |
| Per-transaction fee | Rejected | Adds friction to adoption; store owners don't want to calculate cost per package |
| Revenue share | Rejected | PostalPoint uses this but it's unpopular — store owners resent sharing margins on their core business |
| Hybrid (base + per-SMS) | Partial | SMS overage is the only usage-based component — keeps the model simple while protecting against outlier usage |

**Billing:** Monthly, paid in advance. Annual option at 2 months free (effectively 17% discount): Starter $790/year, Professional $1,490/year.

---

## 4. Revenue Projections

### Conservative Assumptions

- Average revenue per store: $110/month (weighted: 60% Starter at $79, 30% Professional at $149, 10% Enterprise at $249)
- Monthly churn: 3% (industry SaaS average for SMB)
- Customer acquisition: organic + direct outreach to CMRA stores
- Serviceable market: ~6,300-7,000 independent/small-franchise stores

### Revenue by Customer Count

| Customers | Mix (S/P/E) | Monthly Revenue | Annual Revenue (ARR) | Market Penetration |
|-----------|-------------|-----------------|---------------------|-------------------|
| 10 | 6/3/1 | $1,100 | $13,200 | 0.15% |
| 50 | 30/15/5 | $5,500 | $66,000 | 0.75% |
| 100 | 60/30/10 | $11,000 | $132,000 | 1.5% |
| 250 | 150/75/25 | $27,500 | $330,000 | 3.7% |
| 500 | 300/150/50 | $55,000 | $660,000 | 7.5% |
| 1,000 | 600/300/100 | $110,000 | $1,320,000 | 15% |
| 3,000 | 1,800/900/300 | $330,000 | $3,960,000 | 45% |

### Cost Structure (at 100 customers)

| Cost Item | Monthly | Notes |
|-----------|---------|-------|
| Twilio SMS | ~$400 | ~50,000 SMS/month at $0.0079 |
| SendGrid | $0 (free tier) | Under 100 emails/day |
| Cloud hosting | $200 | VPS for API + dashboard serving |
| Support staff | $0 (founder-handled) | Until ~250 customers |
| **Total COGS** | **~$600** | |
| **Gross margin** | **~94%** | $11,000 revenue - $600 COGS |

### Break-Even Analysis

| Scenario | Fixed Costs/Month | Break-Even Customers |
|----------|------------------|---------------------|
| Solo founder (no salary draw) | $500 (hosting, tools, Twilio) | 5 Starter customers |
| Solo founder + $5K/month draw | $5,500 | 50 Starter customers |
| Small team (2 people) | $15,000 | 137 customers (weighted mix) |

---

## 5. Free Trial & Onboarding Strategy

### 14-Day Free Trial (Professional Tier)

- Full Professional features, no credit card required
- 100 free SMS notifications included in trial
- Guided onboarding: setup wizard walks through scanner configuration, customer import, first notification test
- Trial-to-paid conversion target: 25% (industry benchmark for vertical SaaS)

### Onboarding Flow

1. **Day 0:** Sign up → download Docker install → connect barcode scanner → send test notification
2. **Day 1-3:** Import customer list (CSV upload or manual entry) → configure notification preferences
3. **Day 4-7:** Process real packages with the system → customer receives real notifications
4. **Day 8-14:** Review dashboard analytics → see time saved → decide to subscribe

### First 10 Customers Strategy

- **Direct outreach** to independent CMRA stores (not franchise-locked)
- **Offer:** 3 months at Starter price ($79/month) even on Professional tier — "founding member" pricing
- **Ask:** Detailed feedback, video testimonial, referral to 2 other store owners
- **Goal:** 10 paying customers within 90 days of launch, 5 case studies by month 6

---

## 6. Upsell Path

### Starter → Professional

| Trigger | Upsell Action |
|---------|--------------|
| SMS overage 2+ months in a row | "You're sending {N} SMS/month — Professional includes 2,000 for $70 more" |
| Store hires second employee | "Professional includes 5 staff accounts — your new hire can log in too" |
| Customer asks about analytics | "Professional includes weekly analytics — see your peak hours and trends" |
| 6 months on Starter | Proactive check-in: "Here's what Professional would unlock for you" |

### Professional → Enterprise

| Trigger | Upsell Action |
|---------|--------------|
| Opens second location | "Enterprise gives you a consolidated dashboard across locations" |
| Asks about POS integration | "Enterprise includes custom integrations — we'll connect to your POS" |
| Shipping Advisor Agent launches | "Enterprise members get early access to multi-carrier rate optimization" |
| Revenue > $50K/month at store | "Let's talk about a custom package that matches your volume" |

---

## 7. Competitive Positioning

| Feature | PostalMate ($95) | Bullship ($50) | **Ours — Starter ($79)** | **Ours — Pro ($149)** |
|---------|-----------------|----------------|--------------------------|----------------------|
| POS system | Full POS | Basic | No (standalone MVP) | No (standalone MVP) |
| Multi-carrier shipping | Yes | Yes (limited) | No (Phase 2) | No (Phase 2) |
| **Auto SMS/email on intake** | No | No | **Yes** | **Yes** |
| **Package photo capture** | No | No | **Yes** | **Yes** |
| **AI-powered dashboard** | No | No | **Basic** | **Full analytics** |
| **Aging package alerts** | No | No | No | **Yes** |
| **Multi-user access** | Yes | No | No | **Yes (5 users)** |
| **API access** | No | No | No | **Yes** |
| Cloud-based | No (desktop) | Yes | Yes | Yes |
| Mobile access | No | Yes | Yes | Yes |

**Positioning statement:** "We're not replacing your POS — we're adding the AI automation layer that your POS doesn't have. Keep PostalMate for shipping labels. Add us for instant customer notifications, package tracking, and analytics."

---

## Summary

Three-tier SaaS pricing at $79/$149/$249+ per location per month, positioned as an AI automation layer (not a POS replacement) in a market with zero AI competitors. Starter undercuts PostalMate to lower switching friction. Professional delivers 8x ROI at 200 packages/day. Revenue potential: $1.3M ARR at 1,000 customers (15% market penetration). 14-day free trial with guided onboarding. First 10 customers via direct outreach with founding member pricing.

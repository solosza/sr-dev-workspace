# QA Platform Site Integration — Research Report

## Executive Summary

**Recommendation: Portfolio showcase first, separate product sites later.**

The QA platforms (Selenium/Playwright UI testing, Docker/SSH compliance testing) are not mature enough for standalone product sites. Build polished showcase sections within the portfolio site (isagawa.co) now. Defer separate product sites until there's a clear monetization path or customer demand.

---

## 1. Competitor Site Strategy Analysis

### How QA Tool Companies Structure Their Web Presence

| Company | Approach | URL | Notes |
|---------|----------|-----|-------|
| Playwright | Single product site | playwright.dev | Clean, focused. Hero + features + docs. No parent brand site. |
| Cypress | Single product site | cypress.io | Full product site with design system. Ramotion did rebranding. |
| BrowserStack | Multi-product platform | browserstack.com | One domain, multiple products (Live, Automate, Percy, etc.) |
| Sauce Labs | Enterprise platform | saucelabs.com | Enterprise-focused, requires sales contact for pricing |
| Vercel | Platform + showcase | vercel.com | Product site with customer showcases embedded |
| Linear | Product site | linear.app | Minimalist, developer-focused. Strong brand identity. |

### Key Pattern

**Open-source tools** (Playwright, Cypress) have single-purpose product sites — one tool, one site, one message.

**Platform companies** (BrowserStack, Sauce Labs) have multi-product sites under one domain — the platform IS the brand.

**Solo/small teams** showcasing work use portfolio sites with project case studies — the person IS the brand.

### Where Isagawa Fits

Isagawa is currently a **personal brand** (solo developer with AI agent governance expertise), not a product company. The QA platforms are proof-of-work, not products with users. This maps to the portfolio + case study pattern, not the product site pattern.

---

## 2. Option Analysis

### Option A: Add QA Sections to Portfolio Site (isagawa.co)

**How it works:** Add dedicated pages/sections for each QA platform within the existing portfolio site. Each platform gets a case study page with:
- Problem statement
- Technical architecture
- Screenshots/demos
- Technology stack
- Results/outcomes

**Pros:**
- Fastest to build (extend existing site, same design system)
- Cohesive personal brand narrative ("I build governed AI agents that produce production-quality QA systems")
- Portfolio visitors see the full range of work
- Single domain, single deployment, single maintenance burden

**Cons:**
- Portfolio pages can't evolve into product pages without a major refactor
- Limits the narrative — "here's what I built" vs "here's a tool you can use"
- May feel cluttered if too many projects are showcased

**Best for:** Current stage — demonstrating capability, attracting clients/employers, building credibility.

### Option B: Separate Product Sites

**How it works:** Build standalone sites (qa.isagawa.co or separate domains) for each QA platform. Each site has its own landing page, docs, quickstart, and branding.

**Pros:**
- Professional product positioning
- Can evolve independently (pricing, docs, community)
- Better for SEO if targeting "QA testing tool" keywords
- Portfolio site links to them as "featured work"

**Cons:**
- Significant build effort (2 separate sites, each needs design, content, deployment)
- Premature — no users, no revenue, no product-market fit
- Maintenance overhead (3 sites instead of 1)
- Risk of looking like vaporware (polished site for a tool nobody uses)

**Best for:** After validating demand — when there are actual users or paying customers.

### Option C: Hybrid — Portfolio Now, Separate Later

**How it works:** Build rich case study pages in the portfolio now. When/if a platform gains traction, spin it out to its own site using the same design process (clone references → adapt → build).

**Pros:**
- No wasted effort — portfolio pages serve as initial product pages
- Natural evolution path
- Design assets (colors, components, copy) transfer to product site when ready

**Best for:** The pragmatic path. Build once, reuse later.

---

## 3. QA Platform Maturity Assessment

| Platform | Maturity | Ready for Product Site? | Notes |
|----------|----------|------------------------|-------|
| Selenium/Playwright UI Testing | Medium | No — portfolio showcase only | Framework exists, tests run, but no unique product differentiator vs Playwright/Cypress |
| Docker/SSH Compliance Testing | Medium-High | Maybe — has a unique angle | STIG/CIS/NIST compliance validation is niche and valuable. Could differentiate. |
| Attestation Pipeline | High | Yes — backlog 059 just shipped | Unique in the market. No competitor offers agent attestation with Sigstore. |

### The Differentiation Problem

Selenium/Playwright testing is a commodity — Playwright.dev and Cypress.io already own this space. Isagawa's QA platform would need a unique angle (governed testing? AI-driven test generation?) to justify a standalone product site.

Docker/SSH compliance testing has more potential — automated STIG/CIS compliance validation is a real enterprise need, and the existing framework validates against multiple standards.

The attestation pipeline (backlog 059) is the most differentiated offering — no competitor has agent attestation with Sigstore integration.

---

## 4. Design Process Recommendation

### If Building Portfolio Showcase Pages

Follow the same process as the portfolio site:

1. **Reference sites to clone:** Focus on developer portfolio project pages, not product landing pages
   - Linear.app case studies
   - Vercel customer showcases
   - Stripe developer docs (for the technical depth)

2. **Content per platform:**
   - Hero: one-sentence value prop + screenshot
   - Problem: what testing challenge this solves
   - Architecture: diagram showing how it works
   - Tech stack: logos/badges
   - Demo: GIF or embedded terminal showing it running
   - Results: metrics (tests run, coverage, pass rates)

3. **Design constraints:**
   - Match existing isagawa.co visual language (dark theme, terminal aesthetic)
   - Mobile responsive
   - Static (GitHub Pages compatible)

### If Building Separate Product Sites (Future)

1. **Reference sites to clone:**
   - Playwright.dev (clean, developer-focused)
   - Linear.app (minimalist, strong brand)
   - Resend.com (modern developer tool site)

2. **Minimum viable product site:**
   - Hero with clear value prop
   - Feature grid (3-4 key features)
   - Quickstart section
   - Pricing (even if free/open-source)
   - GitHub link

---

## 5. Open Questions Resolved

| Question | Answer |
|----------|--------|
| Integrate into portfolio or separate sites? | **Portfolio first** — separate sites are premature |
| Static or dynamic? | **Static** — GitHub Pages, same as portfolio |
| Naming/domain strategy? | **isagawa.co/projects/[name]** — subdirectories, not subdomains |
| Which platforms to showcase first? | **Attestation pipeline** (most differentiated), then **SSH compliance** |

---

## 6. Recommended Next Steps

1. **Add 2-3 project showcase pages to isagawa.co** — attestation pipeline, SSH compliance testing, and optionally the UI testing framework
2. **Use the web cloner** to find reference designs for developer project case study pages
3. **Write content** for each platform — problem statement, architecture, demo content
4. **Deploy** to GitHub Pages alongside existing portfolio
5. **Monitor** — if any platform gets inbound interest, that's the signal to build a dedicated product site

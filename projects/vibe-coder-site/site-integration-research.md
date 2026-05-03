# Vibe Coder Site Integration — Research Report

## Executive Summary

**Recommendation: Portfolio showcase page now. Separate product site only if the tool gains users.**

The vibe coding market is extremely competitive in 2026 — Bolt.new ($40M ARR), Lovable ($20M ARR in 2 months), v0, Cursor, and others dominate. A standalone product site for Vibe Coder would need a clear differentiator to avoid looking like a "me too" entry. A polished portfolio showcase page demonstrating the tool's capabilities is the right first step.

---

## 1. Competitor Landscape (2026)

### AI Vibe Coding Tools — Market Map

| Tool | ARR/Traction | Approach | Site Style |
|------|-------------|----------|------------|
| **Bolt.new** | $40M ARR | Browser-based, WebContainer, zero setup | Product site with live playground |
| **Lovable** | $20M ARR (2 months) | Full-stack MVP, Supabase, one-click deploy | Product site with demos |
| **v0** (Vercel) | Large (Vercel ecosystem) | Frontend-only, React/Tailwind components | Product site integrated into Vercel |
| **Cursor** | Large | IDE-based, Background Agents, Hooks | Polished product site with interactive demos |
| **Google Stitch** | New (Google backing) | Design exploration, multi-option generation | Integrated into Google ecosystem |
| **Mocha** | Emerging | Full-stack app builder | Product site |

### What Their Sites Have in Common

1. **Interactive demo or playground** — not just screenshots, but live experiences
2. **Clear value prop in hero** — "Build apps by chatting" (Lovable), "The best way to code with AI" (Cursor)
3. **Social proof** — ARR numbers, user counts, testimonials
4. **Free tier / try now** — immediate access, no sales call
5. **Dark theme** — almost universal in developer tool sites

### Key Insight

Every competitor with a product site has **real users and real revenue**. Their sites convert visitors into users. A product site without users is marketing without a product.

---

## 2. What is Vibe Coder?

### Current State Assessment

The Vibe Coder (isagawa-co/vibe-coder) needs to be assessed against competitors on:

| Dimension | Question |
|-----------|----------|
| **Differentiator** | What does Vibe Coder do that Bolt/Lovable/v0 don't? |
| **Users** | Does anyone besides the creator use it? |
| **Maturity** | Is it production-ready or a prototype? |
| **Demo-ability** | Can someone try it in 30 seconds? |

### Potential Differentiators

If Vibe Coder integrates the Isagawa kernel's governance model, the differentiator could be:
- **Governed vibe coding** — AI builds your app but can't go rogue (hooks, gates, attestation)
- **Attestation-backed** — every build produces cryptographic proof of what was generated
- **Self-improving** — the system learns from failures and gets better over time

This would be unique — no competitor offers governed, attested AI code generation.

---

## 3. Option Analysis

### Option A: Portfolio Showcase Page

**How it works:** Add a case study page to isagawa.co for Vibe Coder — problem, architecture, demo GIF, tech stack, differentiation.

**Pros:**
- Fast to build (same design system as portfolio)
- Presents the tool as proof-of-work, not a product promise
- Honest positioning — "here's what I built" vs "here's a tool that competes with $40M ARR companies"

**Cons:**
- Doesn't drive user adoption
- Limited to portfolio visitors

**Best for:** Current stage.

### Option B: Separate Product Site

**How it works:** Build vibecoder.dev or similar with hero, features, demo, quickstart, pricing.

**Pros:**
- Professional product positioning
- Can drive organic traffic via SEO
- Required if pursuing product-market fit

**Cons:**
- Premature without users or revenue
- High bar to compete visually with Bolt/Lovable/Cursor sites
- Requires live demo or playground (static site isn't enough)

**Best for:** After validating demand and having a clear differentiator.

### Option C: Open-Source Landing Page

**How it works:** A simple GitHub Pages site linked from the repo — README-level content but in web form. Think: a styled version of the README.

**Pros:**
- Low effort (static site, GitHub Pages)
- Professional enough for open-source discovery
- Links back to the portfolio for the full story

**Cons:**
- Won't convert non-technical visitors
- Limited SEO impact

**Best for:** If the goal is open-source adoption.

---

## 4. Design Reference Sites

### For Portfolio Showcase Page

| Reference | Why |
|-----------|-----|
| Linear.app case studies | Clean developer project showcases |
| Vercel.com/customers | Product showcase with visual polish |
| isagawa.co existing sections | Maintain visual consistency |

### For Future Product Site (if/when)

| Reference | Why | Key Pattern |
|-----------|-----|------------|
| cursor.com | Interactive IDE demo in hero | Dark theme, animated product showcase |
| bolt.new | Instant access, browser-based | "Try it now" CTA, live playground |
| lovable.dev | Clear value prop, social proof | Hero + features + testimonials |
| linear.app | Minimalist, developer-focused | Typography-driven, dark theme |
| resend.com | Modern developer tool site | Clean API-focused design |

---

## 5. Open Questions Resolved

| Question | Answer |
|----------|--------|
| Integrate into portfolio or separate site? | **Portfolio showcase now** — separate site is premature |
| Static or dynamic? | **Static** — no live playground needed for portfolio showcase |
| Naming/domain strategy? | **isagawa.co/projects/vibe-coder** — portfolio path |
| Does it warrant its own site? | **Not yet** — needs users, differentiator, or revenue first |

---

## 6. Recommended Next Steps

1. **Clarify the differentiator** — what does Vibe Coder do that Bolt/Lovable/v0 don't? If the answer is "governance + attestation," lean into that hard.
2. **Build a portfolio showcase page** on isagawa.co — architecture, demo GIF, tech stack
3. **Write a compelling README** for the GitHub repo — this IS the product site for open-source tools
4. **Monitor for signals** — GitHub stars, forks, issues. These indicate demand for a standalone site.
5. **Only build a product site** when there's a clear answer to "who would use this instead of Bolt/Lovable/Cursor?"

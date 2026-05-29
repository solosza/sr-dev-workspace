# Reference Site Nav Analysis

Research for isagawa.co nav consolidation (Pipeline 106).

---

## Site 1: Vercel (vercel.com)

**Total desktop nav items:** 7 top-level (Products, Resources, Solutions, Enterprise, Pricing, Ask AI, Log In / Sign Up)

**Always visible:** Products, Resources, Solutions, Enterprise, Pricing + CTA buttons

**Dropdown structure:**
- **Products** — grouped into sub-sections: "AI Cloud" (5 items), "Core Platform" (5 items), "Security" (4 items). ~14 items total under one dropdown.
- **Resources** — grouped: Customers, Blog, Changelog, Press, Events, Docs, Academy, Community + Open Source projects
- **Solutions** — grouped by use case and user role

**Label used:** "Products" for the main product grouping

**Mobile:** Collapses to hamburger menu

**Notable patterns:**
- Heavy use of sub-grouped dropdowns (sections within dropdowns with headings)
- Products dropdown has 14+ items but feels organized due to 3 named sub-groups
- Top-level count is low (5 text items + 2 CTAs) despite massive underlying page count
- Enterprise is a standalone top-level item (premium positioning)

---

## Site 2: Stripe (stripe.com)

**Total desktop nav items:** 6 top-level (Products, Solutions, Developers, Resources, Pricing, Sign in)

**Always visible:** All 6 items + "Start now" / "Contact sales" CTAs

**Dropdown structure:**
- **Products** — groups individual products (Payments, Billing, Connect, etc.) under category headings
- **Solutions** — by business type and use case
- **Developers** — docs, API reference, SDKs
- **Resources** — support, guides, blog

**Label used:** "Products" for product grouping, "Solutions" for use-case grouping

**Mobile:** Hamburger with collapsible sections ("Back" button pattern for nested levels)

**Notable patterns:**
- 6 visible items is remarkably restrained for a company with 20+ products
- "Products" is the catch-all — everything lives there
- Labels are simple, non-technical: Products, Solutions, Resources
- Clear separation between "what we sell" (Products) and "how to use it" (Developers, Resources)

---

## Site 3: Anthropic (anthropic.com)

**Total desktop nav items:** 7 top-level (Research, Economic Futures, Commitments, Learn, News, Try Claude, Language selector)

**Always visible:** Research, Economic Futures, Commitments, Learn, News + Try Claude CTA

**Dropdown structure:**
- **Commitments** — sub-groups: "Initiatives" (Constitution, Transparency, RSP) + "Trust center" (Security & compliance)
- **Learn** — sub-groups: "Learn" (Academy, Tutorials, Use cases, Engineering, Docs) + "Company" (About, Careers, Events)
- **Try Claude** — sub-groups: "Products" (Claude, Claude Code, Cowork, Security, Platform, Pricing) + "Models" (Opus, Sonnet, Haiku) + "Log in" options

**Label used:** "Try Claude" for product access (not "Products")

**Mobile:** Hamburger menu with same structure

**Notable patterns:**
- Only 5 text nav items visible (Research, Economic Futures, Commitments, Learn, News)
- Products are under "Try Claude" — a CTA-style label, not a generic grouping
- Multiple products (6+) and models (3) all collapse under one dropdown
- Very clean top-level despite having substantial depth
- "Learn" combines educational resources AND company info

---

## Site 4: Linear (linear.app)

**Total desktop nav items:** ~5 top-level (Features, Method, Customers, Changelog, Pricing + Sign in / Sign up CTAs)

**Always visible:** All items — no dropdowns on the marketing site

**Dropdown structure:** None (flat nav)

**Label used:** N/A

**Mobile:** Hamburger menu

**Notable patterns:**
- Extremely minimal — 5 items, all flat links, no dropdowns
- Linear is a single-product company — they don't need product grouping
- "Method" is a unique label (their opinionated approach to project management)
- Marketing site nav is separate from the app's sidebar navigation
- The restraint is intentional: Linear's brand is "less is more"

---

## Site 5: Railway (railway.com)

**Total desktop nav items:** ~8 top-level (Features, Pricing, Customers, Enterprise, Agents and AI, Docs, Changelog + Sign in / Deploy CTAs)

**Always visible:** All items appear to be flat links

**Dropdown structure:** Minimal — primarily flat navigation

**Label used:** N/A (flat structure)

**Mobile:** Hamburger menu

**Notable patterns:**
- Flat nav despite having multiple product areas (database hosting, web apps, AI agents)
- "Agents and AI" is a dedicated top-level item (trend-aware positioning)
- Similar restraint to Linear but with slightly more items
- No "Products" dropdown — each feature area is its own page
- Small enough product surface that flat nav still works

---

## Common Patterns Across Sites

1. **Top-level count: 5-7 items.** Every site keeps the visible nav to 5-7 items regardless of total page count. Stripe has 20+ products but shows 6 nav items. Vercel has dozens of features but shows 5 text items.

2. **"Products" is the dominant grouping label.** Vercel, Stripe both use "Products" as the dropdown label for their offerings. Anthropic uses "Try Claude" (CTA variant). The label communicates "here are the things we make."

3. **Sub-grouped dropdowns are standard.** When a dropdown has 10+ items, they're organized into named sub-sections (Vercel: "AI Cloud" / "Core Platform" / "Security"). This avoids the long-list problem.

4. **Flat nav works for single-product companies.** Linear (1 product) and Railway (few products) use flat nav. Once you have 4+ distinct products, a dropdown becomes necessary.

5. **CTA buttons are separate from nav items.** Sign in, Sign up, Deploy, Start now — these are visually distinct (buttons, not text links). They don't count toward the "nav item" budget.

6. **Mobile always uses hamburger.** Every site collapses to hamburger on mobile. The desktop dropdown structure doesn't affect mobile — mobile shows a flat list.

---

## Takeaway for isagawa.co

isagawa.co is a **multi-product portfolio** (like Stripe/Vercel) not a **single-product site** (like Linear). With 5+ product pages and growing, a flat nav will not scale.

**The pattern is clear:** Use a "Products" or "Work" dropdown to group product pages. Keep 3-4 items always visible. This is what every multi-product reference site does.

**Specific recommendation:**
- **Always visible:** Home, Feed, Attestation (3 items)
- **Dropdown labeled "Products":** QA Platforms, SSH Compliance, Vibe Coder (+ future items)
- **Remove from nav:** On-page story anchors (Seed, Growth, etc.) — no reference site puts in-page anchors in the global nav
- **Result:** 4 nav elements (3 links + 1 dropdown) — cleaner than any reference site

This follows the Stripe/Vercel pattern (few visible items, products grouped) while being even more minimal — appropriate for a solo engineer portfolio vs. an enterprise SaaS.

# Build Portfolio Showcase — Vibe Coder Pack

## Status
Open

## Priority
High — the vibe coder pack is the most commercially relevant product; it serves the largest addressable market (non-technical builders) with no direct competitor in the "governed vibe coding" space. Showcase page is the storefront.

## Summary
Build a portfolio showcase page for the Vibe Coder Pack on isagawa.co. The page must be framed around the corrected positioning: this is NOT another vibe coding tool competing with Bolt/Lovable/v0. It is a **governed vibe coding harness** — the user vibes (describes what they want in plain English), and a senior dev agent handles all technical decisions, builds production-grade code, and enforces its own architecture. The target user is the average person (the blue collar guy who went viral) who wants to build something real for their business but doesn't know frameworks or architecture.

## Framing

### Up front — built by the loop
This product was produced from a domain spec by the same factory that built every other product on the site. The vibe coder pack is itself a spec — markdown files that teach the kernel a new vertical. One sentence, one link back to the main site. Then move on to the product.

### What it is NOT
- Not a code generator (Bolt/Lovable/v0 territory)
- Not a prototype builder — output is production-grade, maintainable, scalable
- Not magic — the user participates in decisions, gets educated along the way

### What it IS
- A **vibe coding harness** — you describe what you want, a senior dev agent builds it professionally
- **Self-binding architecture** — the agent generates architecture docs, then enforces them on itself (hooks, gates, lessons)
- **Educational HITL** — every technical decision is presented in plain English with tradeoffs; the user picks, the agent explains
- **Governed quality** — cryptographic attestation, failure-driven learning, architecture compliance checks

### The competitive reframe

| | Bolt/Lovable/v0 | Vibe Coder Pack |
|--|-----------------|-----------------|
| What you get | A deployed prototype | A governed codebase with architecture |
| Technical decisions | Made silently by LLM | Made with user (education + HITL) |
| After v1 | Start over or hack on spaghetti | `/vibe-feature` — agent builds within its own rules |
| Quality enforcement | None | Hooks, gates, lessons, architecture compliance |
| User learns | Nothing — it's magic | Gets educated on every decision |
| Scales | No — one-shot generation | Yes — architecture.md is the protocol |

### The real competitive set
- Hiring a freelance developer ($5K-$50K)
- Watching YouTube tutorials and giving up
- Agencies that build apps for small businesses ($10K-$100K)

### Target user
The average person who wants to build something. The blue collar business owner. The solo founder. The person with a great idea and zero technical background. They don't know React from FastAPI — and they shouldn't have to.

## Requirements

### Content Sections
- **Built by the loop** — one line + link establishing this came from the factory
- **Hero:** "You vibe. Your sr dev builds." — one-sentence value prop + visual showing the 4-question discovery flow
- **Problem:** You have an idea. You don't know code. Bolt gives you a throwaway prototype. Freelancers cost $10K+. YouTube tutorials take months. What if an AI senior developer built your app — professionally, maintainably, and explained every decision along the way?
- **How it works:** The 4-phase flow (Discovery → Decisions → Scaffold → Features) with plain English examples of each phase
- **The difference:** Side-by-side comparison table (vibe coder pack vs Bolt/Lovable vs hiring a dev)
- **Self-governing:** Brief explanation of the kernel — the agent creates its own rules, then follows them. Architecture diagram showing the self-binding pattern.
- **Demo:** Terminal recording or GIF showing a real `/vibe` session — the 4 discovery questions, a decision presentation with HITL, scaffold output
- **Tech stack:** Isagawa Kernel, Claude Code, Sigstore attestation — but presented as "what powers it under the hood" not as the selling point

### Design Constraints
- Match existing isagawa.co visual language (dark theme, terminal aesthetic)
- Mobile responsive
- Static (GitHub Pages compatible)
- Lives as a new page/section on the existing portfolio site
- Language must be accessible to non-technical users — no jargon in hero/problem/how-it-works sections
- **Feature branch:** `feature/showcase-vibe-coder` in `isagawa-co.github.io` repo. Do not merge to main until user approves.
- Links back to main site Self-Extension section and to the live feed page (from 075)

### Reference Designs
- Linear.app case studies (clean developer storytelling)
- Cursor.com (dark theme, product showcase with terminal feel)
- Stripe landing pages (complex product explained simply)

## References
- Portfolio site (live): `D:\my_ai_projects\isagawa-co.github.io` (deploys to www.isagawa.co)
- Vibe coder pack spec: `D:\my_ai_projects\project_test_repos\specs\standalone\vibe-coder-spec`
- Vibe coder pack design: `projects/vibe-coder-pack/vibe-coder-pack-design.md`
- Vibe coder pack repo: `D:\my_ai_projects\project_test_repos\vibe-coder-pack`
- Site integration research: `projects/vibe-coder-site/site-integration-research.md`
- Portfolio visual refactor: backlog [053](done/053-market-refactor-portfolio-site-visual-layer.md) (done)
- Portfolio v2 terminal: backlog [055](done/055-market-build-portfolio-site-v2-terminal.md) (done)
- Vibe coder spec (GitHub): `https://github.com/isagawa-co/vibe-coder-spec`
- Live feed page: backlog [075](075-market-build-portfolio-live-feed-update.md) (ships first)
- Website cloner skill: `.claude/skills/website-cloner/`

## Task Builder Input
- **Deliverable:** Vibe Coder Pack showcase page added to isagawa.co — HTML/CSS page with hero, problem statement, 4-phase flow walkthrough, comparison table, self-governing explainer, demo section, tech stack. Framed as governed vibe coding harness for non-technical builders, NOT as a Bolt/Lovable competitor.
- **Location:** `new-repo:D:\my_ai_projects\isagawa-co.github.io`
- **Scope:** BUILD
- **Constraints:** Feature branch only — do not merge to main. Must match existing dark theme terminal aesthetic. Static HTML/CSS (GitHub Pages). Language accessible to non-technical users in hero/problem/how-it-works. Use web cloner to capture reference designs before building. Content written from the vibe-coder-pack-design.md and the spec's SKILL.md/phase files. The comparison table and corrected framing from this backlog item are the foundation of the page — do not fall back to the old "competitor to Bolt" framing.

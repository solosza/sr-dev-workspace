# Standalone Product Assessment — Release Manager for GitHub Pages

## Target Audience

1. **Solo developers** with GitHub Pages portfolio/blog sites (largest group, lowest willingness to pay)
2. **Small agencies** managing multiple client sites on GitHub Pages (smaller group, higher willingness to pay)
3. **Open source projects** using GitHub Pages for docs (moderate group, near-zero willingness to pay)
4. **Companies using GitHub Pages** for internal/external static sites (small group, highest willingness to pay)

## Competitive Landscape

### Platforms That Solve This Already

| Platform | Release Management | Price | Gap for GitHub Pages Users |
|----------|-------------------|-------|---------------------------|
| **Netlify** | Built-in: preview deploys, rollback, deploy logs, branch deploys | Free tier + $19/mo | Requires migration off GitHub Pages |
| **Vercel** | Built-in: preview deployments, instant rollback, deployment protection | Free tier + $20/mo | Requires migration off GitHub Pages |
| **Cloudflare Pages** | Built-in: preview URLs, rollback, build logs | Free tier + $20/mo | Requires migration off GitHub Pages |
| **GitHub Actions** | DIY: you write the workflow | Free (2000 min/mo) | No release management — just CI/CD primitives |

**Key insight:** The platforms that solve release management also host your site. GitHub Pages users who stay on GitHub Pages have no turnkey solution — they have to build it themselves with GitHub Actions.

### Existing GitHub Actions / Tools

| Tool | What It Does | Gap |
|------|-------------|-----|
| `release-drafter` | Auto-generates release notes from PR labels | No smoke test, no rollback, no deployment awareness |
| `semantic-release` | Auto-versioning + changelog from commits | Complex setup, designed for npm packages not static sites |
| `gh-pages` action | Deploys to GitHub Pages from a build | Deployment only — no release management |
| `actions/deploy-pages` | Official GitHub Pages deployment | Deployment only |
| `lighthouse-ci` | Performance/accessibility testing | Testing only — not release management |

**No existing tool combines:** smoke test + changelog + version tag + rollback for GitHub Pages sites. The pieces exist but nobody has assembled them into a cohesive release workflow.

## Distribution Options

| Option | Pros | Cons | Viability |
|--------|------|------|-----------|
| **GitHub Action** | Zero install, runs in CI, discoverable on Marketplace | Must fit GitHub Actions model, YAML config, limited local dev | HIGH — natural home for GitHub Pages tooling |
| **CLI tool** | Full control, works locally, can integrate with kernel | Requires install, less discoverable | MEDIUM — good for power users |
| **VS Code extension** | Visual UI, easy onboarding | Narrow audience (VS Code only), marketplace competition | LOW — overkill for this problem |
| **Composite (Action + CLI)** | Best of both — CI automation + local use | More to build and maintain | MEDIUM-HIGH — but doubles scope |

**Recommendation: GitHub Action first.** It's the natural distribution channel for GitHub Pages tooling. A CLI can come later if there's demand.

## Monetization Assessment

### Open Source + Paid Tier
- **Free tier:** Smoke test + changelog + version tags (basic release workflow)
- **Paid tier:** Multi-site management, Slack notifications, custom smoke test rules, rollback automation
- **Problem:** The free tier solves 90% of the problem. Hard to find features worth paying for.

### Honest Market Size

GitHub Pages usage estimates:
- ~1M+ GitHub Pages sites exist (based on GitHub's public stats)
- Most are personal blogs, project docs, or student portfolios — near-zero willingness to pay
- Maybe 5-10% are "serious" sites (company pages, product sites, portfolios) — ~50-100K
- Of those, maybe 5% would pay for release management — ~2,500-5,000 potential customers
- At $5-10/month: **$12,500-50,000/month revenue ceiling**

**But:** These users can switch to Netlify/Vercel for free and get better release management plus better hosting. The only reason to stay on GitHub Pages is: (a) it's free, (b) it's simple, (c) organizational requirements. Users who value (a) won't pay for tooling. Users who value (c) might.

### Realistic Revenue

- **Best case:** 1,000 paying users at $10/month = $10K/month ($120K/year)
- **Likely case:** 100-300 paying users at $5/month = $500-1,500/month
- **Worst case:** 50 users, then they switch to Netlify

## Go/No-Go Assessment

### Arguments FOR Standalone Product
- Gap exists: no turnkey release management for GitHub Pages
- GitHub Marketplace visibility is free
- Could be a lead generator for the Isagawa kernel (release manager -> kernel -> full platform)
- Low cost to build (it's a GitHub Action, not a SaaS)

### Arguments AGAINST Standalone Product
- Tiny addressable market with low willingness to pay
- Competing with "just switch to Netlify" (which is free and better)
- GitHub could ship this themselves at any time (they own the platform)
- Maintenance burden for minimal revenue
- The real value is in the kernel integration, not the standalone tool

### Verdict: NO-GO as standalone product. YES as kernel feature.

**Rationale:**
1. The market is too small and the competitors too strong (free alternatives exist)
2. The real value of release management is as part of the kernel's autonomous workflow — not as a standalone tool
3. Building it as a kernel command (`/kernel/release`) is the right scope: it solves Isagawa's own deployment problem without trying to productize for an unwilling market
4. If the kernel gains traction, release management becomes a feature, not a product
5. Time spent building a GitHub Action marketplace product would be better spent on the kernel itself

**Recommendation:** Build `/kernel/release` as a kernel command. If it works well internally, extract the smoke test + changelog logic as an open-source GitHub Action later (free, no paid tier) — purely for visibility and credibility, not revenue.

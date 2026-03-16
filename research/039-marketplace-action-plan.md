# Research 039: Domain Spec Marketplace Distribution — Action Plan

**Date:** 2026-03-10
**Status:** Research complete
**Goal:** Identify best distribution channels for our 8 domain specs and document every step to publish

---

## 1. Marketplace Comparison

### 1.1 Anthropic Skills Marketplace (`anthropics/skills`)

| Attribute | Detail |
|-----------|--------|
| **URL** | https://github.com/anthropics/skills |
| **Type** | Official Anthropic-managed GitHub repo + plugin marketplace |
| **Submission** | Fork repo, add skill folder under `skills/`, open PR |
| **Review** | Anthropic team reviews PRs; automated checks run on frontmatter format. "Anthropic Verified" badge available for extra review. No published SLA on review time; community PRs appear to merge within days to weeks based on activity. |
| **Format** | Must follow Agent Skills spec: `SKILL.md` with YAML frontmatter (`name`, `description` required; `license`, `metadata`, `compatibility` optional). Multi-file skills supported — subdirectories for `references/`, `scripts/`, `resources/`, `agents/` are all valid. |
| **Install** | Users run `/plugin marketplace add anthropics/skills` then `/plugin install <skill-name>@anthropic-agent-skills` |
| **Multi-file** | Yes. The repo contains multi-file skills (e.g., `skill-creator` has `references/`, `agents/`, `assets/` subdirectories). |
| **Monetization** | None. All skills are open source (Apache 2.0 or source-available). No payment mechanism. |
| **Audience** | Every Claude Code user. This is the default marketplace Anthropic points people to. Highest visibility. |
| **Pros** | Official channel, highest trust, "Anthropic Verified" badge possible, direct integration with `/plugin` command, largest audience |
| **Cons** | PR review bottleneck, must be open source, no monetization, Anthropic controls acceptance |

### 1.2 skills.sh (Vercel)

| Attribute | Detail |
|-----------|--------|
| **URL** | https://skills.sh + https://github.com/vercel-labs/skills |
| **Type** | Open directory / CLI tool by Vercel |
| **Submission** | No formal submission. Create a public GitHub repo with SKILL.md files. Skills get indexed automatically via install telemetry (when people run `npx skills add`). Can also be manually added to `data/manual_skills.json`. |
| **Review** | No human review. Automated indexing. Quality signals come from install counts. |
| **Format** | Standard Agent Skills spec: SKILL.md with YAML frontmatter. Multi-file supported (entire skill folder is cloned). |
| **Install** | `npx skills add <owner/repo>` or `npx skills add <owner/repo> --skill <name>` |
| **Multi-file** | Yes. Clones the entire skill directory including subdirectories. |
| **Monetization** | None. Open ecosystem. |
| **Audience** | Cross-agent (Claude Code, Cursor, Windsurf, Gemini CLI, OpenCode). Broader than Anthropic-only. |
| **Pros** | No gatekeeping, cross-agent compatibility, simple CLI install, Vercel backing, leaderboard/ranking by installs |
| **Cons** | No quality gate (anyone can publish), no monetization, discovery depends on install volume, no verification badges |

### 1.3 Claude Plugins Official (`anthropics/claude-plugins-official`)

| Attribute | Detail |
|-----------|--------|
| **URL** | https://github.com/anthropics/claude-plugins-official |
| **Type** | Official Anthropic-managed directory of high-quality plugins |
| **Submission** | Submit via in-app form: `claude.ai/settings/plugins/submit` or `platform.claude.com/plugins/submit` |
| **Review** | Anthropic performs automated review + optional manual review for "Anthropic Verified" badge. |
| **Format** | Plugin format: `.claude-plugin/` directory with `plugin.json` manifest, skills, commands, hooks, agents. More structured than raw skills. |
| **Install** | `/plugin marketplace add` then `/plugin install` |
| **Multi-file** | Yes. Plugins are explicitly designed as multi-file bundles. |
| **Monetization** | None currently. Enterprise private marketplaces exist but no payment rail. |
| **Audience** | Claude Code + Claude Cowork (enterprise) users |
| **Pros** | Higher trust than raw skills, plugin format supports hooks/agents/commands, enterprise distribution path, in-app submission |
| **Cons** | More complex format than skills, stricter review, no monetization |

### 1.4 SkillsMP

| Attribute | Detail |
|-----------|--------|
| **URL** | https://skillsmp.com |
| **Type** | Community aggregator (not affiliated with Anthropic) |
| **Submission** | No submission needed. Automated scraper syncs from public GitHub repos. Having a properly formatted SKILL.md in a public repo is sufficient. |
| **Review** | AI-evaluated on 5 dimensions: Practicality, Clarity, Automation, Quality, Impact. S-rank (9.0+), A-rank (8.0+). |
| **Format** | Standard Agent Skills spec. |
| **Install** | Links to GitHub; user installs via `npx skills add` or manual clone. |
| **Monetization** | None. |
| **Audience** | 96,000+ skills indexed. Cross-agent (Claude, Codex, ChatGPT). High volume but noisy. |
| **Pros** | Zero-effort listing (auto-scraped), AI quality scoring, large catalog, cross-agent |
| **Cons** | No curation, noisy catalog, no monetization, no verification, third-party site |

### 1.5 SkillHub

| Attribute | Detail |
|-----------|--------|
| **URL** | https://skillhub.club |
| **Type** | Community aggregator |
| **Submission** | Auto-indexed from GitHub. Push SKILL.md to public repo and it appears. |
| **Review** | AI-evaluated on 5 dimensions (same scoring as SkillsMP). |
| **Format** | Standard Agent Skills spec. |
| **Monetization** | None. |
| **Audience** | Smaller than SkillsMP. |
| **Pros** | Zero effort, AI quality scoring |
| **Cons** | Smaller audience, no curation, no monetization |

### 1.6 LobeHub Skills Marketplace

| Attribute | Detail |
|-----------|--------|
| **URL** | https://lobehub.com/skills |
| **Type** | Aggregator with publishing tools |
| **Submission** | Auto-indexed from GitHub. Can also use `@lobehub/market-cli` for explicit submission and review management. |
| **Review** | Community reviews via CLI: `npx -y @lobehub/market-cli skills comment [skill-name] -c "<review>" --rating 5` |
| **Format** | Standard Agent Skills spec. SKILL.md with frontmatter `name:` and `description:` plus `USE WHEN` / `DO NOT USE WHEN` sections. |
| **Monetization** | None. |
| **Audience** | LobeHub ecosystem users. Cross-agent. |
| **Pros** | Publishing CLI tools, community review system, cross-agent |
| **Cons** | Niche audience, no monetization |

### 1.7 Skills Directory

| Attribute | Detail |
|-----------|--------|
| **URL** | https://skillsdirectory.com |
| **Type** | Curated, security-focused directory |
| **Submission** | Submit via website. All submissions reviewed before publishing. |
| **Review** | Manual review + automated security scan (50+ rules for prompt injection, credential theft, malware). |
| **Format** | Standard Agent Skills spec. |
| **Monetization** | None. |
| **Audience** | Security-conscious users. Smaller but higher-trust audience. |
| **Pros** | Security scanning, manual curation, "verified" status, higher trust signal |
| **Cons** | Smaller audience, review wait time, no monetization |

### 1.8 GitHub as Distribution

| Attribute | Detail |
|-----------|--------|
| **Type** | Direct repository distribution |
| **Submission** | Create public repos with proper topics (`claude-skills`, `agent-skills`, `claude-code`), README with install commands, badges. |
| **Review** | None (it's your repo). |
| **Format** | Any. You control the structure. |
| **Install** | `npx skills add <owner/repo>` or `/plugin marketplace add <owner/repo>` or manual clone. |
| **Monetization** | Indirect only (drive traffic to paid services, consulting, hosted access). |
| **Audience** | Anyone who finds your repo via GitHub search, topics, or referral. |
| **Pros** | Full control, no gatekeeping, can be private (for paid/enterprise), supports all formats |
| **Cons** | No built-in discovery, requires marketing effort, no install tracking unless via skills.sh |

---

## 2. Recommended Primary Channel

**Primary: `anthropics/skills` (official Anthropic marketplace)**

**Justification:**
1. **Highest visibility** — every Claude Code user has access via `/plugin marketplace add anthropics/skills`
2. **Trust signal** — being in the official repo is the strongest credibility indicator
3. **Multi-file support proven** — existing skills like `skill-creator` have complex subdirectory structures
4. **Format alignment** — our specs already follow Agent Skills spec with SKILL.md + references/
5. **Enterprise path** — Anthropic's enterprise plugin marketplace draws from this ecosystem

**Secondary: Vercel skills.sh / `npx skills add`**

**Justification:**
1. **Cross-agent reach** — works with Cursor, Windsurf, Gemini CLI, not just Claude
2. **No gatekeeping** — publish immediately, iterate fast
3. **Install tracking** — provides real usage metrics via leaderboards
4. **Complementary** — doesn't conflict with Anthropic marketplace listing

**Tertiary: GitHub direct + auto-indexed aggregators**

Having public repos with proper tags automatically gets you listed on SkillsMP, SkillHub, and LobeHub with zero extra effort.

---

## 3. Step-by-Step Publishing Guide (Primary: anthropics/skills)

### Step 1: Account / Repo Setup

1. Ensure you have a GitHub account with push access
2. Fork `https://github.com/anthropics/skills`
3. Clone your fork locally
4. Create a feature branch: `git checkout -b add-selenium-spec`

### Step 2: Format Changes Needed

Our specs need these adjustments for the `anthropics/skills` format:

**SKILL.md frontmatter — required fields:**
```yaml
---
name: selenium-qa-testing
description: >
  Prescriptive domain spec for Selenium/Python QA test automation.
  USE WHEN building or maintaining Selenium-based test suites, creating
  page object models, writing pytest fixtures, or automating browser testing.
  DO NOT USE WHEN working with Playwright, Cypress, or non-Python test frameworks.
license: Apache-2.0
---
```

**Key changes from our current format:**
- `name` must be lowercase-hyphenated, max 64 chars (no underscores, no spaces)
- `description` must include USE WHEN / DO NOT USE WHEN triggers
- Add `license` field (Apache-2.0 for open distribution)
- Remove any non-standard frontmatter fields (keep only `name`, `description`, `license`, `metadata`, `compatibility`)
- Body content: no structural restrictions, our existing format works

**Directory structure mapping:**
```
anthropics/skills/skills/
└── selenium-qa-testing/
    ├── SKILL.md              ← Main skill file (frontmatter + instructions)
    ├── workflow.md           ← Workflow steps
    ├── references/           ← Reference files (patterns, examples)
    │   ├── step-01-*.md
    │   └── ...
    ├── commands/             ← Command definitions
    └── lessons/              ← Seeded lessons (if any)
```

### Step 3: Submission Process

1. Copy your formatted skill folder into `skills/<skill-name>/` in your fork
2. Verify SKILL.md frontmatter passes validation:
   - `name` is lowercase-hyphenated, <= 64 chars
   - `description` is present and includes triggering context
   - No disallowed frontmatter keys
3. Commit and push to your fork
4. Open a PR to `anthropics/skills` main branch
5. PR title: `Add <skill-name>: <one-line description>`
6. PR body: describe what the skill does, who it's for, and include example usage

### Step 4: Review Expectations

- **Automated checks:** Frontmatter validation runs on PR
- **Human review:** Anthropic team reviews for quality, safety, and usefulness
- **Timeline:** Based on PR activity in the repo, expect 1-4 weeks for review
- **Iteration:** Reviewers may request changes (description clarity, structure, etc.)
- **Merge:** Once approved, skill is immediately available via `/plugin install`

### Step 5: Post-Publish Maintenance

- Monitor GitHub issues on the `anthropics/skills` repo for feedback
- Submit update PRs when specs change
- Respond to community questions
- Track install metrics (if available via skills.sh cross-listing)

---

## 4. Checklist Per Spec

### Universal Pre-Publishing Checklist

For each of our 8 specs, verify these items before submission:

| Check | Description |
|-------|-------------|
| [ ] **Frontmatter `name`** | Lowercase-hyphenated, <= 64 chars, unique in the marketplace |
| [ ] **Frontmatter `description`** | Includes USE WHEN / DO NOT USE WHEN triggers |
| [ ] **Frontmatter `license`** | `Apache-2.0` (or chosen license) |
| [ ] **No secrets** | No API keys, credentials, internal URLs, customer names |
| [ ] **No proprietary content** | No client-specific configurations, internal business logic |
| [ ] **Self-contained** | Skill works without the kernel (no dependency on `.claude/state/`, hooks, etc.) |
| [ ] **README** | Clear description for GitHub repo page |
| [ ] **Example usage** | At least one concrete example of skill invocation and expected behavior |
| [ ] **Tested** | Skill has been tested with Claude Code and produces correct behavior |

### Per-Spec Status

| Spec | Name (proposed) | Sensitivity Check | Self-Contained? | Notes |
|------|----------------|-------------------|-----------------|-------|
| **selenium-spec** | `selenium-qa-testing` | Low risk (generic QA patterns) | Yes (spec-only repo) | Ready after frontmatter update |
| **playwright-spec** | `playwright-qa-testing` | Low risk | Yes | Ready after frontmatter update |
| **docker-spec** | `docker-image-testing` | Low risk (CIS/STIG/FIPS are public standards) | Yes | Verify no proprietary compliance mappings |
| **edi-testing-spec** | `edi-x12-testing` | Medium risk — review for PHI/PII patterns | Yes | Strip any real EDI transaction examples; use synthetic data only |
| **claims-testing-spec** | `health-claims-testing` | Medium risk — review for proprietary payer logic | Yes | Ensure no client-specific adjudication rules |
| **benefits-config-spec** | `benefits-config-testing` | Medium risk — review for proprietary plan structures | Yes | Ensure no real plan/benefit data |
| **auth-um-spec** | `auth-um-testing` | Medium risk — review for proprietary UM criteria | Yes | Ensure no real clinical criteria or payer-specific rules |
| **kernel-spec** | `cognitive-kernel` | Low risk (meta-spec, builds the kernel) | Needs review | May reference internal kernel architecture; verify no circular deps |

### Critical: Healthcare Spec Sensitivity Review

The 4 healthcare specs (EDI, claims, benefits, auth-um) require extra scrutiny:
- Remove ALL real transaction examples — replace with synthetic/dummy data
- Remove any payer-specific business rules
- Ensure compliance references are to public standards only (X12, HIPAA, CMS)
- Have a domain expert review before publishing
- Consider whether these should be published at all vs. kept as private/paid offerings

---

## 5. Multi-Channel Strategy

### Phase 1: GitHub Direct (Day 1)

**Effort: Low. Do this first.**

1. Ensure each spec repo is public on GitHub under `isagawa-co/`
2. Add GitHub topics to each repo: `claude-skills`, `agent-skills`, `claude-code`, `domain-spec`, plus domain-specific tags (`selenium`, `playwright`, `docker`, `healthcare`, etc.)
3. Add README badges:
   ```markdown
   ![Agent Skills Compatible](https://img.shields.io/badge/Agent%20Skills-Compatible-blue)
   ![Claude Code](https://img.shields.io/badge/Claude%20Code-Skill-purple)
   ```
4. Add install command to README:
   ```markdown
   ## Install
   npx skills add isagawa-co/selenium-spec
   ```
5. Result: Auto-indexed by SkillsMP, SkillHub, LobeHub within days

### Phase 2: Vercel skills.sh (Day 1-3)

**Effort: Low. Happens automatically after Phase 1.**

1. Having public repos with SKILL.md means `npx skills add isagawa-co/<repo>` works immediately
2. As installs accumulate, skills appear on skills.sh leaderboards
3. Optionally submit to `data/manual_skills.json` in `vercel-labs/skills` for immediate listing
4. Result: Cross-agent visibility (Claude, Cursor, Windsurf, Gemini CLI)

### Phase 3: Anthropic Official Marketplace (Week 1-2)

**Effort: Medium. Requires format adaptation and PR review.**

1. Start with 2-3 lower-risk specs: `selenium-qa-testing`, `playwright-qa-testing`, `docker-image-testing`
2. Adapt frontmatter to exact spec requirements
3. Submit PRs to `anthropics/skills`
4. After first PR merges, submit remaining specs
5. Result: Official listing, highest trust, `/plugin install` access

### Phase 4: Plugin Format (Week 3-4)

**Effort: Medium-High. Optional but valuable for enterprise.**

1. Package each spec as a Claude Code plugin with `.claude-plugin/` directory
2. Create a unified marketplace repo: `isagawa-co/domain-specs` with `marketplace.json`
3. Users can add the entire marketplace: `/plugin marketplace add isagawa-co/domain-specs`
4. Submit to `anthropics/claude-plugins-official` via in-app form
5. Result: Enterprise-ready distribution, bundled install experience

### Phase 5: Curated Directories (Week 2-3)

**Effort: Low.**

1. Submit to Skills Directory (skillsdirectory.com) — benefits from security verification badge
2. Submit to LobeHub via `@lobehub/market-cli`
3. Result: Additional discovery channels, security verification credential

---

## 6. Monetization Analysis

### Current State: No Direct Payment Rails

As of March 2026, **no skills marketplace supports paid skills**. Every channel (Anthropic, Vercel, SkillsMP, SkillHub, LobeHub, Skills Directory) is free/open source only.

### Indirect Monetization Paths

| Model | How It Works | Viability |
|-------|-------------|-----------|
| **Hosted Access** | Run skills on a hosted platform (e.g., Agent37.com) where customers pay for access. Your code stays protected. | High — proven model, some people report revenue from this. |
| **Freemium / Open Core** | Publish basic spec for free, sell advanced version (more patterns, more lessons, enterprise features) as private repo access. | Medium — requires managing two versions. |
| **Consulting / Implementation** | Free specs drive leads; charge for implementation, customization, training. | High — natural upsell from "I tried your spec and need help." |
| **Enterprise Private Marketplace** | Sell to enterprise teams who deploy via private plugin marketplaces (Claude Cowork). License per-org. | Medium-High — requires sales motion but enterprises pay for curated, verified tools. |
| **SaaS Wrapper** | Build a product around the specs (e.g., QA-as-a-Service using selenium-spec under the hood). | High — but this is a different business model entirely. |
| **Spec Bundles** | Sell bundled access to all healthcare specs as a package. Private GitHub repo with license key. | Medium — niche audience but high value per customer. |

### Recommended Monetization Strategy

1. **Publish generic specs for free** (selenium, playwright, docker, kernel) — these are lead generators
2. **Keep healthcare specs private initially** — these have higher value and sensitivity
3. **Offer healthcare specs as paid bundles** via private GitHub repo access ($X/month or $X/year per org)
4. **Use free specs as proof of quality** to drive enterprise consulting engagements
5. **Monitor for Anthropic marketplace payment rails** — when/if they launch paid skills, be first to list

### Why No Payment Rails Yet

Anthropic's current strategy appears to be:
- Skills are free to drive Claude Code adoption
- API token usage is the monetization layer (Anthropic earns when skills drive more Claude usage)
- A paid marketplace is likely planned but not yet launched
- Enterprise private marketplaces exist but don't have payment processing — it's BYOL (bring your own license)

---

## 7. Timeline

### Week 1 (March 10-16, 2026)

| Day | Action |
|-----|--------|
| Mon-Tue | Phase 1: Make all 4 generic spec repos public, add topics/badges/README install commands |
| Mon-Tue | Phase 2: Verify `npx skills add` works for each public repo |
| Wed-Thu | Adapt selenium-spec and playwright-spec frontmatter for anthropics/skills format |
| Fri | Submit first 2 PRs to anthropics/skills (selenium, playwright) |

### Week 2 (March 17-23, 2026)

| Day | Action |
|-----|--------|
| Mon-Tue | Adapt docker-spec and kernel-spec frontmatter |
| Wed | Submit PRs for docker-spec and kernel-spec to anthropics/skills |
| Thu | Submit all 4 specs to Skills Directory (skillsdirectory.com) |
| Fri | Submit to LobeHub via market-cli |

### Week 3 (March 24-30, 2026)

| Day | Action |
|-----|--------|
| Mon-Wed | Healthcare spec sensitivity review (EDI, claims, benefits, auth-um) |
| Thu-Fri | Decision: publish healthcare specs publicly or keep private/paid? |

### Week 4 (March 31 - April 6, 2026)

| Day | Action |
|-----|--------|
| Mon-Tue | If publishing healthcare specs: adapt frontmatter, strip sensitive content |
| Wed-Thu | Create unified plugin marketplace repo (isagawa-co/domain-specs) with marketplace.json |
| Fri | Submit plugin marketplace to anthropics/claude-plugins-official via in-app form |

### Week 5+ (April 7+, 2026)

| Action | Ongoing |
|--------|---------|
| Monitor PR reviews on anthropics/skills | Check weekly |
| Track install metrics on skills.sh | Check weekly |
| Respond to community feedback / issues | As needed |
| Update specs when patterns change | As needed |
| Evaluate monetization options for healthcare specs | Monthly |

### Realistic Expectations

- **GitHub + skills.sh listing:** Immediate (Day 1)
- **SkillsMP/SkillHub auto-indexing:** 1-7 days
- **Skills Directory verified listing:** 1-2 weeks
- **anthropics/skills PR merge:** 1-4 weeks (depends on review queue)
- **anthropics/claude-plugins-official listing:** 2-6 weeks
- **All 8 specs fully distributed:** 4-6 weeks total

---

## Sources

- [anthropics/skills GitHub Repository](https://github.com/anthropics/skills)
- [Agent Skills Spec](https://github.com/anthropics/skills/blob/main/spec/agent-skills-spec.md)
- [Claude Code Skills Documentation](https://code.claude.com/docs/en/skills)
- [Claude Code Plugin Marketplace Docs](https://code.claude.com/docs/en/plugin-marketplaces)
- [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official)
- [Vercel skills CLI (vercel-labs/skills)](https://github.com/vercel-labs/skills)
- [skills.sh Directory](https://skills.sh/)
- [SkillsMP](https://skillsmp.com/)
- [SkillHub](https://www.skillhub.club/)
- [LobeHub Skills Marketplace](https://lobehub.com/skills)
- [Skills Directory](https://www.skillsdirectory.com/)
- [How to Monetize Claude Code Skills (2026)](https://www.agent37.com/blog/monetize-claude-code-skills)
- [Claude Code Skills vs Plugins](https://llbbl.blog/2026/03/05/claude-code-skills-vs-plugins.html)
- [Claude Skills Marketplace Walkthrough (Medium)](https://medium.com/@markchen69/claude-code-has-a-skills-marketplace-now-a-beginner-friendly-walkthrough-8adeb67cdc89)
- [SKILL.md Format Specification (DeepWiki)](https://deepwiki.com/anthropics/skills/2.2-skill.md-format-specification)
- [Anthropic Enterprise Plugins](https://www.ghacks.net/2026/02/25/anthropic-expands-claude-with-enterprise-plugins-and-marketplace/)

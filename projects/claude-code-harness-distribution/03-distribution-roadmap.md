# Distribution Roadmap: Isagawa Kernel

## Document Purpose

This roadmap translates the strategic recommendation into an executable plan. Phase 1 is a 4-week dual-track launch with concrete weekly deliverables, metrics, and decision gates. Phase 2 presents three conditional expansion options, each triggered by specific market signals. The goal: establish Isagawa Kernel as the reference production harness in the Agent Skills ecosystem, then expand only where data justifies investment.

---

## Phase 1: Dual-Track Launch (4 Weeks)

Phase 1 runs two parallel tracks. Track A puts the Kernel on distribution platforms. Track B builds community authority and curator credibility. Both tracks are low-cost ($6-12K total), high-signal (every metric feeds Phase 2 decisions), and executable by a single person.

### Track A: Distribution Platform Expansion

#### Objective

Get Isagawa Kernel live on 4+ distribution platforms using the Agent Skills SKILL.md standard, with platform-specific documentation and installation paths verified end-to-end.

#### Week-by-Week Execution

**Week 1: SKILL.md Refactor + Initial Submissions**

- Read the [Agent Skills specification](https://github.com/agentskills/agentskills) in full. Understand frontmatter schema, instructions format, and cross-platform compatibility requirements.
- Convert Isagawa Kernel to `kernel.SKILL.md` format in `.claude/skills/` directory. The SKILL.md must include: identity block, step table, file index, and installation instructions.
- Test compatibility manually across Claude Code, Cursor, Copilot, Codex CLI, and Gemini CLI. Document which platforms support which features (hooks, commands, skills) and where degradation occurs.
- Submit to primary platforms:
  - **Claude Code Plugins Official** — Submit via Anthropic's form. Include harness category tag, production-readiness claim, and link to GitHub repo.
  - **skills.sh** — Register via GitHub. Auto-indexed from repo metadata. Verify listing appears within 24 hours.
  - **claudemarketplaces.com** — Submit via their form. Auto-crawled; verify listing reflects correct metadata.
  - **agentskills.io (GitHub registry)** — Publish via GitHub. Ensure registry entry matches SKILL.md frontmatter.
- Deliverable: `kernel.SKILL.md` committed, 4 platform submissions initiated.

**Week 2: Submission Monitoring + Documentation Polish**

- Monitor submission status daily. If any platform rejects, diagnose the rejection reason within 24 hours and resubmit.
- Write platform-specific "Getting Started" guides:
  - Claude Code: `docs/getting-started-claude-code.md` (hook setup, CLAUDE.md integration, session-start flow)
  - Cursor: `docs/getting-started-cursor.md` (how Kernel degrades gracefully without hooks)
  - Copilot: `docs/getting-started-copilot.md` (GitHub Actions integration path)
- Create unified troubleshooting guide covering the 10 most likely installation failures (missing Python, wrong directory, hooks not loading, etc.).
- Deliverable: All 4 submissions approved or resubmitted, 3 getting-started guides published.

**Week 3: Feedback Loop + Issue Resolution**

- Aggregate early feedback from all platforms (comments, GitHub issues, forum posts).
- Fix any compatibility issues discovered by real users. Prioritize by platform adoption (Claude Code first, then Cursor, then others).
- Update SKILL.md and documentation based on feedback. Every user-reported issue gets a documentation fix within 48 hours.
- Begin tracking install/view metrics across all platforms using platform-native analytics.
- Deliverable: Zero unresolved critical bugs, metrics tracking active on all platforms.

**Week 4: Metrics Review + Phase 2 Assessment**

- Compile Phase 1 metrics report: views, installs, feedback sentiment, rejection rate, community engagement.
- Compare against Phase 1 success criteria (see below). Document which criteria are met, which are trending, which are missed.
- Decide: continue Phase 1 optimization, or begin Phase 2 planning.
- Deliverable: Phase 1 metrics report, Phase 2 recommendation.

#### Track A Success Criteria

| Metric | Target | Measurement Source |
|--------|--------|--------------------|
| Platforms listed | 4 | Manual verification |
| Views/impressions (2 weeks) | 50+ | Platform analytics |
| Downloads/installs | 10+ | Platform analytics |
| Platform rejections | 0 | Submission tracking |
| Critical bugs from community | 0 | GitHub issues, platform feedback |

#### Track A Effort & Cost

| Category | Estimate |
|----------|----------|
| Engineering (SKILL.md refactor + testing) | 2 weeks |
| Documentation (guides, troubleshooting) | 1 week |
| Admin (submissions, onboarding, monitoring) | 1 week |
| Total duration | 3-4 weeks, 1 FTE |
| Internal cost | $5-10K (engineering time) |
| External cost | Minimal (all platforms free/open-source) |

---

### Track B: Community & Authority Building

#### Objective

Establish Isagawa as a trusted expert and curator in the harness ecosystem. Build community presence that makes Phase 2 options cheaper and more effective because users already know and trust the brand.

#### Week-by-Week Execution

**Week 1-2: Curator Collection + First Guides**

- Create "Enterprise Harnesses" collection on claudemarketplaces.com. This is the flagship curator offering.
  - Vet existing harnesses for production readiness using a consistent rubric: Does it have hooks? Does it have a protocol? Does it handle failures? Does it have tests?
  - Tag each harness by vertical (enterprise, healthcare, finance, DevOps, general-purpose).
  - Write a 100-200 word rationale for each selection explaining why it qualifies as production-ready.
  - Target: 10+ harnesses curated in initial collection.
- Begin writing integration guides:
  - Guide 1: "Kernel + Review Command + Audit Workflow" — the most popular combination for teams adopting Kernel. Walk through setup, configuration, and expected behavior.
  - Guide 2: "Building Domain-Specific Harnesses with Kernel" — teach developers how to use `/kernel/domain-setup` to create harnesses for their specific use case (healthcare, legal, finance).

**Week 2-3: Finish Guides + Community Engagement**

- Complete integration guides:
  - Guide 3: "Harness Performance: How to Optimize for Your Use Case" — benchmark methodology, common bottlenecks, optimization strategies.
- Publish all guides on: dev.to, GitHub (as repo docs), and linked from platform listings.
- Begin active community engagement:
  - Answer questions on claudemarketplaces.com and agentskills.io.
  - Contribute to Agent Skills spec discussions on GitHub (propose improvements, review PRs).
  - Post to Hacker News and Reddit (r/ClaudeAI, r/LocalLLaMA) with genuine value-add content, not promotional.

**Week 3-4: Sustained Engagement + Network Building**

- Continue community support cadence: 4-6 hours/week responding to questions, reviewing community harnesses, contributing to discussions.
- Expand curator network: invite other harness authors to contribute to the "Enterprise Harnesses" collection. Cross-promotion builds the ecosystem.
- Document learnings from community interactions. What do users actually want? What problems do they report? These insights feed Phase 2 decisions.
- Begin planning Phase 2 trigger strategy: set up monitoring for all trigger metrics (installs, repeat users, feedback themes, community growth, revenue model announcements).

#### Track B Success Criteria

| Metric | Target | Measurement Source |
|--------|--------|--------------------|
| Curator collection created | 1 enterprise collection, 10+ harnesses | claudemarketplaces.com |
| Integration guides published | 2-3 | dev.to, GitHub |
| Community presence | Active in comments, GitHub discussions | Manual tracking |
| Followers/watchers | 100+ across platforms | Platform analytics |

#### Track B Effort & Cost

| Category | Estimate |
|----------|----------|
| Curation | 8 hours (one-time) |
| Writing (3 guides) | 16 hours (4-5 hours each) |
| Community engagement | 4-6 hours/week ongoing |
| Total Phase 1 | 30-40 hours |
| Internal cost | $1-2K |
| External cost | $0 (all platforms free) |

---

## Phase 1 Checklist

This is the operational checklist for Phase 1 execution. Each item maps to a weekly deliverable above.

### Track A Checklist

- [ ] Read Agent Skills specification in full
- [ ] Create `kernel.SKILL.md` with frontmatter + instructions
- [ ] Test compatibility: Claude Code, Cursor, Copilot, Codex CLI, Gemini CLI
- [ ] Submit to Claude Code Plugins Official
- [ ] Submit to skills.sh (GitHub registration)
- [ ] Submit to claudemarketplaces.com (form submission)
- [ ] Submit to agentskills.io (GitHub registry)
- [ ] Write Getting Started guide: Claude Code
- [ ] Write Getting Started guide: Cursor
- [ ] Write Getting Started guide: Copilot
- [ ] Write unified troubleshooting guide
- [ ] Set up metrics tracking on all 4 platforms
- [ ] Resolve all critical bugs from early feedback
- [ ] Compile Phase 1 metrics report

### Track B Checklist

- [ ] Create "Enterprise Harnesses" curator collection
- [ ] Vet and tag 10+ harnesses for production readiness
- [ ] Write integration guide: "Kernel + Review + Audit Workflow"
- [ ] Write integration guide: "Building Domain-Specific Harnesses"
- [ ] Write integration guide: "Harness Performance Optimization"
- [ ] Publish guides on dev.to + GitHub
- [ ] Post to Hacker News and Reddit with value-add content
- [ ] Establish weekly community engagement cadence (4-6 hrs/week)
- [ ] Set up Phase 2 trigger metric monitoring

### Phase 1 Success Metrics Summary

| Metric | Target | Status |
|--------|--------|--------|
| Kernel listed on 4 platforms | 4 | Pending |
| Views/impressions (first 2 weeks) | 50+ | Pending |
| Downloads/installs | 10-20 | Pending |
| Zero platform rejections | 0 rejections | Pending |
| Zero critical bugs from community | 0 bugs | Pending |
| Curator collection: 10+ harnesses | 10+ | Pending |
| Integration guides published | 2-3 | Pending |
| Community followers/watchers | 100+ | Pending |

---

## Phase 1 Timeline (Weekly Breakdown)

```
Week 1
  Track A: Refactor to SKILL.md + submit to 4 platforms
  Track B: Create "Enterprise Harnesses" curator collection + start first 2 guides

Week 2
  Track A: Monitor submissions, write 3 Getting Started guides + troubleshooting
  Track B: Finish integration guides, begin community engagement

Week 3
  Track A: Aggregate feedback, fix compatibility issues, set up metrics tracking
  Track B: Sustained community support (4-6 hrs/week), expand curator network

Week 4
  Track A: Compile Phase 1 metrics report, assess Phase 2 readiness
  Track B: Document learnings, set up Phase 2 trigger monitoring
```

---

## Phase 2: Conditional Expansion (3-6 Months After Phase 1)

Phase 2 is not automatic. It activates only when specific market signals confirm demand. Three options exist, each addressing a different market reality. Only one should be pursued initially; the others remain available if conditions change.

### Phase 2 Trigger Criteria

All five criteria must be met before committing to any Phase 2 option. If fewer than five are met, continue optimizing Phase 1 (better messaging, broader platform coverage, deeper community engagement).

| Metric | Threshold | Measurement Source | Rationale |
|--------|-----------|-------------------|-----------|
| Total installs | >100/month | Platform analytics | Proves organic demand exists beyond initial launch push |
| Repeat users | >30% | Platform analytics | Proves value retention — users come back because Kernel solves real problems |
| User feedback | "More harness variants" mentioned 3+ times | Support tickets, Reddit, GitHub issues | Proves market wants platform-specific optimization |
| Community growth | 200+ followers/engagement | claudemarketplaces.com, GitHub | Proves brand awareness sufficient to support expansion |
| Revenue model clarity | Monetization available on at least 1 platform | Poe or Anthropic announcement | Proves economic sustainability path exists |

**Decision rule:** If all 5 criteria are met, proceed to Phase 2. Select the option that best matches which criteria are strongest. If fewer than 5 are met, stay in Phase 1 and optimize.

### Phase 2 Option A: Build Harness Variants

**When to choose:** Installs are high AND user feedback specifically requests platform-optimized versions.

#### Goal

Create Claude Code-optimized, Cursor-optimized, and Copilot-optimized Kernel variants. Each variant tunes the harness for the specific IDE's strengths, context management patterns, and integration points.

#### Why This Option

- Marketplace research identified a 4% performance gap between harnesses across platforms (Cursor outperforms Claude Code on certain benchmarks). Platform-specific optimization can close or reverse this gap.
- Developers who already use Kernel on one platform want to use it on others without performance regression.
- Agent Skills standard enables multi-platform variants with shared core + platform-specific extensions.

#### Execution Plan

1. **Benchmark current Kernel** across Claude Code, Cursor, and Copilot. Measure: task completion rate, context utilization efficiency, hook reliability, error recovery time. Document baseline metrics.
2. **Optimize Claude Code variant:** Adjust context management strategy, hook execution ordering, and anchor frequency. Leverage Claude Code's native hook support for maximum enforcement.
3. **Optimize Cursor variant:** Integrate with Cursor's visual diff, sidebar features, and inline completion patterns. Kernel commands map to Cursor's command palette.
4. **Optimize Copilot variant:** Build GitHub Actions integration for CI/CD pipeline enforcement. Kernel protocol becomes a GitHub workflow that runs on every PR.
5. **Publish variants** on existing platforms with clear labeling: `[Claude Code]`, `[Cursor]`, `[Copilot]` in marketplace listings. Each variant links to platform-specific Getting Started guide.

#### Effort & Cost

| Category | Estimate |
|----------|----------|
| Time per variant | 4-6 weeks |
| Total for 3 variants | 3-4 months |
| Cost per variant | $30-50K (engineering + testing) |
| **Total Phase 2A** | **$90-150K, 4-6 months** |

#### Success Metrics

| Metric | Target | Timeline |
|--------|--------|----------|
| Variants ranked top-5 in respective categories | 3/3 | 3 months post-launch |
| Adoption increase for optimized variants | 2-3x | 6 months post-launch |
| User feedback: "Noticeable performance improvement" | Majority positive | 3 months post-launch |

---

### Phase 2 Option B: Build Custom Marketplace

**When to choose:** Installs exceed 500/month AND revenue model is proven AND funding is available for infrastructure investment.

#### Goal

Create a dedicated harness marketplace with superior discovery UX, vertical specialization, and a harness registry with versioning, CI/CD integration, and analytics.

#### Why This Option

- If organic demand exceeds 500 installs/month, Google discoverability becomes viable — a dedicated marketplace captures search traffic that platform listings cannot.
- If a revenue model is proven (Poe monetization, Anthropic marketplace fees, or subscription), the marketplace can be self-sustaining.
- Vertical specialization (healthcare, finance, legal, DevOps) creates defensible niches that general-purpose platforms cannot serve as well.

#### Execution Plan

1. **Build discovery UI:** Search, filters, ratings, installation wizard. User can find harnesses by vertical, platform, maturity level, and use case. Mobile-responsive, fast, accessible.
2. **Create harness registry:** Versioning (semver), CI/CD integration (test harnesses on every release), analytics dashboard (installs, usage, retention per harness).
3. **Establish vertical collections:** Healthcare compliance, financial audit, legal review, DevOps automation. Each collection has a curator, a quality rubric, and a certification process.
4. **Recruit contributor harnesses:** Offer revenue share or sponsorship to high-quality harness authors. Cross-promote from existing platform listings to the custom marketplace.

#### Effort & Cost

| Category | Estimate |
|----------|----------|
| Time | 6-12 months (3-5 engineers) |
| Build cost | $200-500K |
| Ongoing operations | $50-100K/year |
| **Total first year** | **$250-600K** |

#### Success Metrics (6 Months Post-Launch)

| Metric | Target |
|--------|--------|
| Monthly visits | 5,000+ |
| Harnesses in registry | 1,000+ |
| Vertical collections | 50+ |
| Revenue model sustainable | Break-even within 12 months |

---

### Phase 2 Option C: Double Down on Curation

**When to choose:** Community authority is strong AND consulting demand is growing, but install volume doesn't justify platform investment.

#### Goal

Become the definitive curator of "production-ready" harnesses across multiple platforms. Monetize through consulting, certification, and sponsored content rather than platform infrastructure.

#### Why This Option

- Curation builds authority 10x faster than building a custom platform, at 10x lower cost.
- Community values trust more than technology — a trusted curator influences purchasing decisions more than a marketplace with better UX.
- Consulting revenue is immediate and doesn't require the scale that platform monetization demands.

#### Execution Plan

1. **Expand curator collections** across claudemarketplaces.com, agentskills.io, and GitHub. Cover every major vertical and platform combination.
2. **Create "Harness Maturity Model"** — a public framework for evaluating harness production-readiness. Levels: Experimental → Community → Production → Enterprise. Clear criteria at each level.
3. **Launch "Isagawa Certified" badge** — a certification program for harnesses that meet the Enterprise maturity level. Certification involves: code review, test coverage check, documentation audit, and production deployment verification.
4. **Build consulting practice** — help teams implement curated harness combinations. Offer: harness selection consulting, custom harness development, production deployment support.

#### Effort & Cost

| Category | Estimate |
|----------|----------|
| Time commitment | 15-20 hours/week ongoing |
| Monthly cost | $2-5K (tools, content, marketing) |
| Revenue potential | High (consulting: $150-300/hr, certification fees, sponsored content) |
| **Annual cost** | **$25-60K** |
| **Annual revenue potential** | **$100-300K** (consulting + certification) |

#### Success Metrics (6 Months)

| Metric | Target |
|--------|--------|
| Curated harnesses across platforms | 500+ |
| "Isagawa Certified" badge recognized | Community awareness > 50% |
| Consulting engagements | 3-5/month |
| Curator followers | 1,000+ |

---

## Phase 2 Decision Logic

The decision tree below maps market signals to the appropriate Phase 2 option. Only one option should be pursued initially; pivot if conditions change.

```
If installs > 100/month AND user feedback requests variants:
  -> Phase 2A (Harness Variants)
     Cost: $90-150K | Timeline: 4-6 months
     Best when: Technical demand is clear, users want optimization

Else if installs > 500/month AND revenue model proven:
  -> Phase 2B (Custom Marketplace)
     Cost: $200-500K | Timeline: 6-12 months
     Best when: Scale justifies infrastructure, funding available

Else if community authority strong AND consulting demand growing:
  -> Phase 2C (Curation + Consulting)
     Cost: $25-60K/year | Timeline: Ongoing
     Best when: Trust > technology, revenue via services not platform

Else:
  -> Continue Phase 1 (optimize messaging, expand platform coverage, deepen community)
```

---

## Budget Summary

### Phase 1 (4 Weeks)

| Track | Cost |
|-------|------|
| Track A: Distribution Platform Expansion | $5-10K |
| Track B: Community & Authority Building | $1-2K |
| **Phase 1 Total** | **$6-12K** |

### Phase 2 (Conditional — Only If Triggered)

| Option | Cost | Timeline |
|--------|------|----------|
| Option A: Harness Variants | $90-150K | 4-6 months |
| Option B: Custom Marketplace | $200-500K + $50-100K/yr ops | 6-12 months |
| Option C: Curation + Consulting | $25-60K/year | Ongoing |

### Cost Comparison

Phase 1 costs 2-5% of Phase 2B (custom marketplace) but achieves 80% of the distribution reach. This asymmetry is the core strategic insight: invest minimally to validate demand, then scale investment only where data confirms ROI.

| Scenario | Investment | Expected Reach | Cost per Install |
|----------|-----------|----------------|-----------------|
| Phase 1 only | $6-12K | 10-20 installs | $300-1,200 |
| Phase 1 + 2A (Variants) | $96-162K | 100-500 installs | $192-1,620 |
| Phase 1 + 2B (Marketplace) | $206-512K | 1,000-5,000 installs | $41-512 |
| Phase 1 + 2C (Curation) | $31-72K | 50-200 installs | $155-1,440 |

Phase 2B has the lowest cost-per-install at scale but requires the highest upfront investment and the strongest market validation signals.

---

## Risk Mitigation

| Risk | Impact | Likelihood | Mitigation Strategy |
|------|--------|-----------|---------------------|
| Agent Skills spec adoption slows | Phase 1 reach limited — fewer platforms support SKILL.md format | Medium | Maintain Claude Code Plugin format as fallback. If Agent Skills adoption stalls, dual-publish in both formats. Monitor spec repository activity monthly. |
| Platform rejects Kernel submission | Distribution blocked on one or more platforms | Low | Build relationship with Anthropic team directly. Ensure submission meets all stated requirements before first attempt. Have backup platform list (npm, VS Code marketplace). |
| Competitors build harness variants faster | Market share captured before Phase 2 can launch | Medium | Execute Phase 1 in exactly 4 weeks, not 6. Monitor competitor activity weekly. If competitor launches variants, accelerate Phase 2A timeline by 2 weeks. First-mover in Agent Skills ecosystem matters. |
| Harness optimization niche has limited demand | Phase 2A investment wasted on low-demand variants | Medium | Phase 2A is gated by trigger criteria (>100 installs/month + variant feedback). Don't over-invest; build one variant first, measure adoption, then build remaining variants only if first succeeds. |
| Custom marketplace cost exceeds budget | Phase 2B becomes infeasible | High | Trigger only if revenue model proven AND funding available. Consider open-source marketplace framework (reduce build cost 50-70%). Phase 2C (curation) is always available as lower-cost alternative. |
| Community engagement fails to gain traction | Track B success criteria missed | Medium | Double content output in weeks 2-3. Partner with existing harness authors for cross-promotion. If still failing at week 4, pivot Track B to focus on developer tooling (CLI helpers, scaffolding) instead of content. |
| Revenue model never materializes | Phase 2 options all depend on eventual monetization | Medium | Phase 2C (curation + consulting) can generate revenue independent of platform monetization. Consulting is viable at any scale. If no platform monetization emerges within 6 months, default to Phase 2C. |

---

## Appendix: Phase 2 Trigger Monitoring Setup

To ensure Phase 2 triggers are evaluated consistently, set up the following monitoring during Phase 1 Week 4:

1. **Install tracking spreadsheet** — One row per platform per week. Columns: platform, views, installs, uninstalls, net installs, cumulative.
2. **Feedback aggregation** — GitHub Issues label: `user-feedback`. Reddit/HN bookmark folder. Weekly review of all feedback mentioning "variants," "optimization," or "platform-specific."
3. **Community metrics** — GitHub stars, followers, forks. claudemarketplaces.com follower count. dev.to article views and reactions.
4. **Revenue model watch** — Set Google Alert for "Anthropic marketplace monetization," "Claude Code plugins revenue," "agent skills monetization." Weekly check of Anthropic blog and changelog.
5. **Monthly trigger review** — First Friday of each month, review all 5 trigger criteria against thresholds. Document decision in `projects/claude-code-harness-distribution/trigger-reviews/YYYY-MM.md`.

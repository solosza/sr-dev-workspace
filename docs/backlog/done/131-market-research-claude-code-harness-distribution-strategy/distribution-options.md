# Distribution Options — 4 Strategies with Effort/Benefit Analysis

## Status
Research Complete

## Option 1: List on Existing Platforms (RECOMMENDED)

### Strategy
Publish Isagawa Kernel on 4-6 existing distribution channels without building custom marketplace.

### Platforms (Priority Order)
1. **Claude Code Plugins Official** — Highest discoverability, Anthropic endorsement
2. **Agent Skills Hub (skills.sh)** — Multi-harness portability (30+ agents), future-proof
3. **GitHub Direct** — Version control home, auto-indexed by all platforms
4. **claudemarketplaces.com** — High community reach, low friction
5. **claudeskills.info** — Skills-specific discovery
6. *Optional:* Claude Marketplace (wait for Phase 2 traction)

### Effort
- **Time:** 2-3 weeks engineering + documentation
- **Cost:** $5K-10K (consulting for compliance/submission)
- **Ongoing:** 4-8 hours/month maintenance (updates, support)

### Benefits
- Access to 100K+ users across platforms
- Zero infrastructure cost
- Multi-harness support (Claude Code, Cursor, Copilot, Codex CLI, Gemini CLI, community tools)
- Anthropic endorsement via official channels
- Future-proof via Agent Skills standard (portable across new harnesses)

### Risks
- Organic discoverability limited (depends on platform algorithms)
- No custom branding or control
- Platform policy changes affect visibility
- Revenue model unknown (pending on most platforms)

### Timeline
- **Week 1:** Refactor to Agent Skills SKILL.md spec
- **Week 2:** Submit to Claude Code Plugins Official, skills.sh, claudemarketplaces.com, GitHub
- **Week 3:** Polish documentation, handle initial feedback
- **Week 4+:** Monitor adoption metrics, iterate

---

## Option 2: Build Custom Marketplace (NOT RECOMMENDED AT THIS TIME)

### Strategy
Create custom web UI + backend for discovering and installing Claude Code harnesses. Model on wshobson/agents (multi-harness) or claudemarketplaces.com.

### Scope
- **Discovery UI:** Search, filters, ratings, installation guides
- **Backend:** Harness registry, version management, analytics
- **Community:** Discussion forums, reviews, contributor onboarding
- **Harness Variants:** Claude Code, Cursor, Copilot versions of kernel

### Effort
- **Time:** 6-12 months
- **Cost:** $200K-500K
- **Team:** 3-5 engineers + designer + community manager
- **Ongoing:** $50K-100K/year operations

### Benefits
- **Full control:** Branding, features, monetization
- **Harness specialization:** Offer Cursor-optimized, Claude Code-optimized variants
- **Community building:** Direct relationship with users
- **Data:** First-party analytics on harness adoption

### Risks
- **High sunk cost:** $200K+ upfront before validating market
- **Infrastructure burden:** Servers, CI/CD, monitoring, security
- **Market fragmentation:** Competing against established platforms (claudemarketplaces.com, skills.sh already exist)
- **Community cold start:** Need 100+ harnesses to be valuable vs existing platforms with 1000+
- **Monetization unclear:** No proven revenue model for harness marketplaces yet

### When This Makes Sense
- If you have **50+ proprietary harnesses** (not applicable yet)
- If you have **vertical specialization** (e.g., 50 healthcare-specific harnesses)
- If you're **VC-funded** and target enterprise market
- If existing platforms block you (unlikely)

### Decision Framework
**Don't build custom marketplace now.** Defer to Phase 2 only if:
- Option 1 drives >100 installs/month
- User feedback shows strong need for harness variants per-platform
- Revenue model becomes clear on existing platforms

---

## Option 3: Become Curator on Existing Platform (HYBRID APPROACH)

### Strategy
Instead of building custom platform, become trusted expert curator on claudemarketplaces.com + agentskills.io.

### What This Means
1. **Vet harnesses** for production readiness, security, performance
2. **Create curated collections** ("Enterprise-Grade Harnesses", "Healthcare Harnesses", "Finance Harnesses")
3. **Write tutorials & guides** for using kernel + selected plugins together
4. **Moderate community** — answer questions, help troubleshoot
5. **Contribute to standards** — help evolve Agent Skills spec

### Scope
- **Time:** 10-15 hours/week (consultant/volunteer model)
- **Cost:** $0-5K (tools, analytics)
- **Revenue:** Potential sponsor/consulting work downstream

### Benefits
- Leverage existing platform's infrastructure (100K+ users)
- Position self as harness expert (high credibility)
- Minimal technology cost
- Can scale to multiple platforms (skills.sh, claudemarketplaces.com, GitHub)
- Vertical specialization is easier (curate by industry, not by building separate platform)

### Risks
- Dependent on platform health (if claudemarketplaces.com dies, curation dies)
- Less control than custom platform
- Revenue model still pending

### Example Output
```
Isagawa Kernel Curator Collections (on claudemarketplaces.com)
├── Enterprise-Grade Harnesses
│   ├── Isagawa Kernel (core)
│   ├── Review Command Plugin
│   ├── Audit Workflow Plugin
│   └── Production Test Plugin
├── Healthcare Harnesses
│   ├── HIPAA-aware Kernel variant
│   ├── Patient data anonymization skill
│   ├── Compliance audit skill
│   └── etc.
├── Finance Harnesses
│   ├── SOX-compliance Kernel
│   ├── Audit trail skill
│   └── etc.
```

### Timeline
- Can start immediately (parallel with Option 1)
- 2-4 weeks to establish curator role + first collection
- Ongoing curation: 10-15 hours/week

---

## Option 4: Multi-Format Distribution (HYBRID + TECHNICAL)

### Strategy
Publish Isagawa Kernel in multiple formats simultaneously, optimized for each harness + platform.

### Formats
1. **SKILL.md (Agent Skills Standard)**
   - For: Claude Code, Cursor, Copilot, Codex CLI, Gemini CLI, community tools
   - Distribution: skills.sh, agentskills.io, GitHub
   - Effort: Refactor once, publish once

2. **Plugin (Claude Code Native)**
   - For: Claude Code Plugins Official, claudemarketplaces.com
   - Distribution: Official Anthropic marketplace
   - Effort: Wrapper + manifest

3. **MCP Server (Model Context Protocol)**
   - For: Claude Desktop, future integrations
   - Distribution: Claude Desktop registry
   - Effort: MCP interface implementation

4. **Harness Variants (Platform-Specific Optimizations)**
   - Claude Code version (context strategy A)
   - Cursor version (context strategy B)
   - Copilot version (context strategy C)
   - Effort: 2-3x base effort (later, in Phase 2)

### Effort
- **Phase 1 (Now):** SKILL.md + Plugin + GitHub
  - Time: 3 weeks
  - Cost: $10K-15K
- **Phase 2 (3-6 months):** Harness variants
  - Time: 4-6 weeks per variant
  - Cost: $20K-30K per variant

### Benefits
- Maximum reach (30+ agents + all platforms)
- Harness optimization by platform (future-proof for Phase 2)
- Portable (can move between harnesses easily)
- Standards-compliant (SKILL.md open standard)

### Risks
- More maintenance burden (multiple formats to maintain)
- Testing complexity (verify across platforms)
- Variant divergence risk (code versions drifting)

---

## Comparison Matrix

| Strategy | Effort | Cost | Reach | Control | Timeline | Risk |
|----------|--------|------|-------|---------|----------|------|
| **Option 1: List on Existing** | 2-3 weeks | $5-10K | 100K+ | Low | 1 month | Medium |
| **Option 2: Custom Marketplace** | 6-12 months | $200-500K | Organic | High | 6+ months | High |
| **Option 3: Become Curator** | 10-15h/week | $0-5K | 100K+ (indirect) | Medium | 2-4 weeks | Medium |
| **Option 4: Multi-Format** | 3-4 weeks (Phase 1) | $10-15K | 100K+ (multiple) | Medium | 1 month | Low-Medium |

---

## Recommended Approach: Hybrid Option 1 + Option 3

### Phase 1 (Immediate: 4 weeks)
**Execute Option 1 (List on Existing Platforms):**
- Refactor to Agent Skills SKILL.md spec
- Submit to Claude Code Plugins Official, skills.sh, claudemarketplaces.com, GitHub
- Target: Kernel live on 4 platforms by end of Q2 2026

### Phase 1.5 (Parallel: 2-4 weeks)
**Start Option 3 (Become Curator):**
- Establish "Isagawa Enterprise Harnesses" collection on claudemarketplaces.com
- Write integration guides for Kernel + ecosystem plugins
- Build community presence (forum, Discord, GitHub discussions)

### Phase 2 (Conditional: 3-6 months if >100 installs/month)
**Evaluate Option 2 vs. Option 4:**
- If market signals strong demand: Invest in harness variants (Option 4 Phase 2)
- If vertical specialization proven valuable: Enhance curator role with industry-specific collections
- If nothing works: Defer all custom work, focus on community curation

### Phase 3 (12+ months)
**Revisit custom marketplace** only if:
- >1000 installs/month on existing platforms
- Clear revenue model (Poe creator payments or similar)
- User demand for custom UI features
- Team available for 6-month project

---

## Final Recommendation

**Do Option 1 + Option 3 in parallel. Skip Option 2 for now.**

- **Option 1 gets you market access** (100K+ users, multiple platforms)
- **Option 3 builds your authority** (trusted curator, high credibility)
- **Together: 90% of custom marketplace benefit, 10% of the cost**
- **Option 2 later:** Only if market signals demand AND you have resources

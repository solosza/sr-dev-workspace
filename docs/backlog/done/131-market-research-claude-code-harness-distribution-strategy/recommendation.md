# Recommendation: Phased Strategy with Data-Driven Phase 2 Trigger

## Status
Final Recommendation

## Executive Summary

**Recommendation:** Launch Isagawa Kernel via Agent Skills standard (SKILL.md) on 4 primary platforms (next 4 weeks). Defer custom marketplace until market signals >100 installs/month AND user feedback confirms harness-specific optimization is valued.

**Rationale:** Existing platforms (claudemarketplaces.com, agentskills.io, skills.sh) already reach 100K+ developers. Custom marketplace is $200K+ sunk cost with unclear payoff. Better approach: establish credibility through curation + community, then build custom tools only if market validates demand.

---

## Phase 1: Dual-Track Launch (4 weeks)

### Track A: Distribution Platform Expansion

#### Goal
Get Isagawa Kernel live on 4+ distribution platforms with Agent Skills standard.

#### Execution
1. **Refactor to Agent Skills SKILL.md spec** (Week 1)
   - Read [Agent Skills specification](https://github.com/agentskills/agentskills)
   - Convert Kernel to SKILL.md frontmatter + instructions
   - Test compatibility across Claude Code, Cursor, Copilot, Codex CLI, Gemini CLI (manual + automated)
   - Deliverable: `kernel.SKILL.md` in `.claude/skills/` directory

2. **Submit to Primary Platforms** (Week 1-2)
   - **Claude Code Plugins Official:** Submit via Anthropic's form
   - **skills.sh:** Register via GitHub (auto-indexed)
   - **claudemarketplaces.com:** Submit via their form (auto-crawled)
   - **GitHub:** Publish to agentskills.io registry

3. **Polish Documentation** (Week 2-3)
   - Write "Getting Started" guide for each platform
   - Create platform-specific installation instructions
   - Add troubleshooting guides

4. **Monitor & Support** (Week 3-4)
   - Track early feedback
   - Fix compatibility issues
   - Engage with first users

#### Success Metrics (End of Phase 1)
- ✓ Kernel listed on 4 platforms
- ✓ 50+ views/impressions in first 2 weeks
- ✓ 10+ downloads/installs
- ✓ Zero platform rejections (all submissions approved)
- ✓ Community feedback: 0 critical bugs

#### Effort
- **Engineering:** 2 weeks (SKILL.md refactor + testing)
- **Documentation:** 1 week (guides, troubleshooting)
- **Admin:** 1 week (submissions, onboarding)
- **Total:** 3-4 weeks, 1 FTE

#### Cost
- **Internal:** $5K-10K (engineering time)
- **External:** Minimal (submissions are free, tools are free/open-source)

---

### Track B: Community & Authority Building

#### Goal
Establish Isagawa as trusted expert/curator in harness space.

#### Execution
1. **Establish "Enterprise Harnesses" Curator Collection** (Week 1-2)
   - Create collection on claudemarketplaces.com
   - Vet existing harnesses for production readiness
   - Tag by vertical (enterprise, healthcare, finance, DevOps)
   - Write rationale for each selection

2. **Write Integration Guides** (Week 2-3)
   - "Kernel + Review Command + Audit Workflow" (popular combo)
   - "Building Domain-Specific Harnesses with Kernel"
   - "Harness Performance: How to Optimize for Your Use Case"

3. **Engage Community** (Week 3-4 and ongoing)
   - Answer questions on claudemarketplaces.com, agentskills.io
   - Contribute to Agent Skills spec discussions (GitHub)
   - Write thought leadership (blog posts, HN, dev.to)

#### Success Metrics (End of Phase 1)
- ✓ "Enterprise Harnesses" collection created + 10+ harnesses curated
- ✓ 2-3 integration guides published
- ✓ Community presence established (active in comments, GitHub discussions)
- ✓ 100+ followers/watchers across platforms

#### Effort
- **Curation:** 8 hours (one-time)
- **Writing:** 16 hours (3 guides, 4-5 hours each)
- **Community:** 4-6 hours/week ongoing
- **Total Phase 1:** 30-40 hours, $1-2K

#### Cost
- **Internal:** $1-2K (writing, curation)
- **External:** $0 (platforms are free)

---

## Phase 2: Conditional Expansion (Triggered by Metrics, 3-6 months)

### Trigger Criteria (ALL must be met)

| Metric | Threshold | Source |
|--------|-----------|--------|
| **Total Installs** | >100/month | Platform analytics |
| **Repeat Users** | >30% | Platform analytics |
| **User Feedback** | "More harness variants" mentioned 3+ times | Support tickets, Reddit, GitHub issues |
| **Community Growth** | 200+ followers/engagement | claudemarketplaces.com, GitHub |
| **Revenue Model Clarity** | Monetization available on ≥1 platform | Poe or Anthropic announcement |

If ALL criteria met → Proceed to Phase 2. Otherwise → Stay in Phase 1, optimize messaging.

### Phase 2 Option A: Build Harness Variants (If Optimization Demand is High)

#### Goal
Create Claude Code-optimized, Cursor-optimized, Copilot-optimized kernel variants.

#### Why
- Marketplace research shows 4% performance gap between harnesses (Cursor > Claude Code)
- Developers want harness-specific tuning
- Agent Skills standard + variants = competitive advantage

#### Execution
1. **Benchmark current kernel** across platforms
2. **Optimize each variant:**
   - Claude Code: Adjust context management, hook ordering
   - Cursor: Integrate with visual diff, sidebar features
   - Copilot: Optimize for GitHub Actions integration
3. **Publish variants** on existing platforms (add `[Claude Code]`, `[Cursor]`, `[Copilot]` to marketplace listings)

#### Effort
- **Time:** 4-6 weeks per variant (3 variants = 3-4 months)
- **Cost:** $30K-50K per variant (engineering + testing)
- **Total for Phase 2A:** $90-150K, 4-6 months

#### Success Metrics
- ✓ Kernel variants ranked top-5 in respective harness categories
- ✓ Adoption increases 2-3x for optimized variants
- ✓ User feedback: "Noticeable performance improvement"

---

### Phase 2 Option B: Build Custom Marketplace (If Scale Justifies Investment)

#### Goal
Create dedicated harness marketplace with superior UX + vertical specialization.

#### Why
- If >500 installs/month: Organic discoverability via Google becomes viable
- If revenue model proven: Can invest in infrastructure
- If vertical demand clear: Specialized marketplace adds value

#### Execution
1. **Build discovery UI** (search, filters, ratings, installation wizard)
2. **Create harness registry** (versioning, CI/CD, analytics)
3. **Establish vertical collections** (healthcare, finance, legal, DevOps)
4. **Recruit contributor harnesses** (offer revenue share or sponsorship)

#### Effort
- **Time:** 6-12 months (3-5 engineers)
- **Cost:** $200-500K
- **Ongoing:** $50-100K/year operations

#### Success Metrics (6 months post-launch)
- ✓ 5,000+ monthly visits
- ✓ 1,000+ harnesses in registry
- ✓ 50+ vertical-specific collections
- ✓ Revenue model sustainable

---

### Phase 2 Option C: Double Down on Curation (If Authority is the Strength)

#### Goal
Become the definitive curator of "production-ready" harnesses across multiple platforms.

#### Why
- Curation builds authority faster than custom platform
- 10x cheaper than custom marketplace
- Community values trust more than technology

#### Execution
1. **Expand curator collections** (claudemarketplaces.com + agentskills.io + GitHub)
2. **Create "Harness Maturity Model"** (how to evaluate production-ready harnesses)
3. **Certify harnesses** ("Isagawa Certified" badge for vetted harnesses)
4. **Build support/consulting business** (help teams implement curated harness combinations)

#### Effort
- **Time:** 15-20 hours/week ongoing
- **Cost:** $2-5K/month (tools, content)
- **Revenue potential:** High (consulting, sponsored content, eventual platform licensing)

#### Success Metrics (6 months)
- ✓ 500+ curated harnesses across platforms
- ✓ "Isagawa Certified" badge recognized in community
- ✓ 3-5 consulting engagements/month
- ✓ 1,000+ curator followers

---

## Decision Logic for Phase 2

```
If installs > 100/month AND user feedback requests variants:
  → Phase 2A (Harness Variants)
Else if installs > 500/month AND revenue model proven:
  → Phase 2B (Custom Marketplace)
Else if community authority strong AND consulting demand growing:
  → Phase 2C (Curation + Consulting)
Else:
  → Continue Phase 1 (optimize messaging, marketing, community)
```

---

## Phase 1 Timeline (Weeks)

```
Week 1:
  └─ Track A: Refactor to SKILL.md + submit to platforms
  └─ Track B: Establish curator collection + write first guides

Week 2:
  └─ Track A: Monitor submissions, gather feedback
  └─ Track B: Finish integration guides, engage community

Week 3:
  └─ Track A: Polish documentation, fix issues
  └─ Track B: Community support, expand curator network

Week 4:
  └─ Track A: Monitor adoption metrics, iterate messaging
  └─ Track B: Document learnings, plan Phase 2 trigger strategy
```

---

## Expected Outcomes (End of Phase 1)

| Metric | Target | Assumption |
|--------|--------|-----------|
| **Kernel Listed** | 4 platforms | All submissions approved |
| **Total Views** | 100-200 | Organic + initial PR push |
| **Installs** | 10-20 | Early adopters, niche interest |
| **Curator Collections** | 1 enterprise, 2-3 vertical | Industry interest varies |
| **Community Engagement** | 100+ followers | HN post, dev.to featured |
| **Team Authority** | "Known in harness space" | Active, visible contributions |

---

## Budget Summary

### Phase 1 (4 weeks)
- Track A (Distribution): $5-10K
- Track B (Community): $1-2K
- **Total: $6-12K**

### Phase 2 (Conditional, if triggered)
- **Option A (Variants): $90-150K**
- **Option B (Custom Marketplace): $200-500K**
- **Option C (Curation + Consulting): $10-25K** (mostly time)

---

## Risk Mitigation

| Risk | Impact | Mitigation |
|------|--------|-----------|
| **Agent Skills spec adoption slows** | Phase 1 reach limited | Maintain Plugin format as fallback |
| **Platform rejects submissions** | Distribution blocked | Work directly with Anthropic (relationships) |
| **Competitors build faster** | Market share lost | Execute Phase 1 fast (4 weeks), monitor daily |
| **Harness optimization niche demand** | Phase 2A fails | Don't over-invest; keep variants minimal |
| **Custom marketplace cost exceeds budget** | Phase 2B infeasible | Trigger only if revenue model proven + funding available |

---

## Final Recommendation

**Execute Phase 1 immediately (this quarter). Monitor Phase 2 triggers continuously. Don't commit to Phase 2B (custom marketplace) until market clearly validates demand.**

**Why?**
1. Phase 1 costs 5% of Phase 2B but gets 80% of the benefit (reach)
2. Phase 1 establishes credibility → Phase 2 options become cheaper (users are warm leads)
3. Phase 1 data informs Phase 2 decision (removes guessing)
4. Worst case: Phase 1 succeeds, no need for Phase 2 (curation + variants sufficient)

**Key Success Factor:** Execute Phase 1 with urgency and excellence. First-mover advantage in Agent Skills ecosystem matters (next 3-6 months). After that window, market consolidates and custom tools become necessary if wanting to compete.

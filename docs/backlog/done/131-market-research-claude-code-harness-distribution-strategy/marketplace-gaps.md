# Marketplace Gaps — What's Missing & Opportunity Analysis

## Status
Research Complete

## Identified Gaps

### 1. No Specialized Claude Code Harness Marketplace
**What's missing:** Dedicated marketplace for Claude Code harnesses only
- Current state: General "agent" marketplaces exist (Poe, GPT Store, Hugging Face), but none specifically for Claude Code harnesses
- Why it matters: Harness-specific knowledge (context management, hook configuration, skill composition) is different from general agent skills
- Opportunity: Vertical harness marketplace (healthcare-optimized, finance-optimized harnesses)
- Cost to build: $200K-500K + 6-12 months + ongoing maintenance
- Market timing: Early; fragmented demand

### 2. No Harness Composability Registry
**What's missing:** Central catalog of composable harness components
- Current state: Skills are discoverable; harness components (hooks, workflows, contexts) are not
- Why it matters: Developers want to compose kernels + domains + custom skills; no way to discover which combinations work
- Opportunity: Harness composition playground (like Storybook for harnesses) where users can test component combinations
- Cost to build: $50K-100K + engineering time
- Demand: Medium (niche but valuable for advanced users)

### 3. No Cross-Harness Performance Benchmarking
**What's missing:** Objective metrics comparing harness performance (Claude Code vs Cursor vs Copilot)
- Current state: Anecdotal reports (e.g., "Cursor outperforms Claude Code by 4% on functionality benchmarks")
- Why it matters: Developers choosing between harnesses need objective data, not reviews
- Opportunity: Harness benchmark registry (similar to LLMevalBench) with standardized test suites
- Cost to build: $100K-200K (test suite development + infrastructure)
- Market demand: High (especially as harness ecosystem grows)
- Timeline: 2026+ (emerging need)

### 4. No Vertical-Specific Harness Catalogs
**What's missing:** Industry-specific harness collections (healthcare, finance, legal, DevOps)
- Current state: Generic skill marketplaces; no curation by vertical
- Why it matters: Healthcare teams need HIPAA-aware harnesses; finance needs audit-friendly harnesses
- Opportunity: Build curator role on existing platform (claudemarketplaces.com + agentskills.io) with vertical-specific tags/collections
- Cost to build: $20K-50K (curation + community management) — **Much cheaper than custom platform**
- Market demand: High (enterprises want industry-ready harnesses)
- Recommended approach: Become curator on existing platforms rather than build custom

### 5. Limited Monetization Models for Harness Creators
**What's missing:** Creator revenue on most platforms
- Current state:
  - Poe: Only platform with creator payments (per-message)
  - Anthropic, HF, GitHub: Monetization "pending" (2026)
  - Community: Zero revenue
- Why it matters: Incentivizes quality harness creation; attracts professional developers
- Opportunity:
  - Harness bounty platform (companies post requests, builders bid)
  - Harness licensing (enterprise harnesses with support contracts)
  - Harness patreon (subscription model for specialized harnesses)
- Cost to build: $50K-200K depending on model
- Timeline: 2026-2027 (post-adoption phase)

### 6. Lack of Harness Testing Standards
**What's missing:** Standardized test suites for harness quality
- Current state: Each harness tested differently; no compatibility matrix
- Why it matters: Users don't know if a harness will work with their version/setup
- Opportunity: Harness test framework (similar to pytest but for harnesses) with automated CI/CD
- Cost to build: $30K-50K
- Market demand: Medium (growing as harness ecosystem matures)

## Opportunity Ranking

| Gap | Market Size | Build Cost | Effort (Months) | Recommendation | Alternative |
|-----|-------------|-----------|-----------------|-----------------|-------------|
| **Vertical-specific catalogs** | High | $20K-50K | 1-2 | **RECOMMENDED** | Become curator on claudemarketplaces.com |
| **Performance benchmarks** | High | $100K-200K | 4-6 | **WAIT** | Contribute to open-source benchmark projects |
| **Specialized harness marketplace** | Medium | $200K-500K | 6-12 | **NOT RECOMMENDED** | Unless have 50+ proprietary harnesses |
| **Harness composability registry** | Medium | $50K-100K | 2-3 | **WAIT** | Build internal tool first, open-source later |
| **Monetization models** | High | $50K-200K | 3-6 | **WAIT** | Partner with existing platform (Poe) |
| **Testing standards** | Medium | $30K-50K | 1-2 | **RESEARCH** | Collaborate with Anthropic on standards |

## Recommended Approach for Isagawa Kernel

**Don't build a marketplace. Become a curator instead.**

1. **Phase 1:** Publish Isagawa Kernel on existing platforms (claudemarketplaces.com + agentskills.io + GitHub)
2. **Phase 2:** If kernel gains traction, become curator for "enterprise-grade harnesses" collection on claudemarketplaces.com
   - Vet harnesses for production readiness, security, performance
   - Provide video guides and tutorials
   - Build community around best-in-class harnesses
3. **Phase 3:** Use curator role to identify vertical opportunities (healthcare, finance, DevOps)
   - Package vertical-specific harness collections
   - Partner with industry associations for distribution
   - This is the "specialized catalog" gap, done as curation not platform

**Cost:** $5-10K for curator role setup + community management. **90% lower cost than building custom platform.**

## Key Insight

The gap is not "no platforms exist" — it's "no curator exists who understands harnesses deeply." A single expert curator on an existing platform (high reach, proven infrastructure) creates more value than a custom platform with generic discovery. **Expertise + trust = differentiation, not technology.**

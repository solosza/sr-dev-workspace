# Business Model

## Pricing Benchmarks from Comparable Platforms

### LLM Eval Platforms
| Platform | Free Tier | Paid Tier | Model |
|----------|-----------|-----------|-------|
| **DeepEval / Confident AI** | 5 test runs/week, 1GB storage | Starter $19.99/user/mo (20K traces, unlimited runs) | Per-user + trace-based |
| **Braintrust** | 1M spans, unlimited users, 10K scores | Pro $249/mo (unlimited spans + users) | Flat monthly + data overages |
| **LangSmith** | 5K traces/mo | Plus $39/user/mo (10K traces, 400-day retention) | Per-user + trace-based |
| **Arize Phoenix** | Open-source | Commercial pricing on request | Enterprise negotiated |

### Compliance SaaS Platforms
| Platform | Entry Price | Model |
|----------|------------|-------|
| **Qualys VMDR** | $199/asset/yr | Asset-based |
| **Qualys WAS** | $1,995/yr (25 web apps) | Module-based |
| **Wiz** | ~$300K+/yr | Enterprise only |
| **Chef InSpec** | Part of Progress Chef suite | Enterprise bundled |

### QA SaaS Platforms
| Platform | Entry Price | Model |
|----------|------------|-------|
| **Testim** | Essentials $450/mo | Tier-based |
| **Mabl** | Custom (~$450/mo+) | Credit-based |
| **Katalon** | Free (basic); Enterprise pricing | Freemium + enterprise |

### Dev Tool Compute Platforms
| Platform | Pricing | Model |
|----------|---------|-------|
| **GitHub Actions** | Free (2K min/mo); $0.008/min (Linux) | Per-minute compute |
| **Replit** | Free (basic); Core $25/mo | Subscription + compute |
| **CodeSandbox** | Free (basic); Pro $12/user/mo | Per-user |

## Pricing Model Comparison

### Option 1: Per-Run Pricing (GitHub Actions model)
- Charge per container execution minute
- **Pros:** Direct cost alignment, users pay for what they use, simple to understand
- **Cons:** Revenue unpredictable, users may self-limit to control costs, no recurring revenue floor

### Option 2: Subscription Tiers (Braintrust model)
- Monthly subscription with run limits per tier
- **Pros:** Predictable revenue, users commit upfront, tiers encourage upgrades
- **Cons:** Users may over-provision or under-use, free tier costs money with no conversion guarantee

### Option 3: Freemium + Per-Run (Recommended)
- Free tier with limited runs, paid tiers with higher limits + per-run pricing for overages
- **Pros:** Low barrier to entry, organic growth, revenue scales with usage, predictable base from subscriptions
- **Cons:** Free tier infrastructure cost, potential for abuse

### Recommended Pricing Structure

| Tier | Monthly Price | Included Runs | Overage Rate | Concurrent Jobs | Features |
|------|-------------|---------------|-------------|-----------------|----------|
| **Free** | $0 | 50 runs/mo | N/A (hard limit) | 1 | Single vertical, basic results |
| **Pro** | $49/mo | 500 runs/mo | $0.10/run | 3 | All verticals, detailed results, component contribution credit |
| **Team** | $199/mo | 2,000 runs/mo | $0.08/run | 5 | Team dashboard, shared results, priority queue |
| **Enterprise** | Custom | Unlimited | Negotiated | 10+ | Dedicated infrastructure, SLA, SSO, data residency |

## Per-Vertical Cost Analysis

Different verticals have different platform-side costs (user pays their own LLM costs via BYOK):

| Vertical | Platform LLM Cost | Container Compute | Total Platform Cost/Run |
|----------|-------------------|-------------------|------------------------|
| **LLM Eval** | $0.05-0.20 (agent uses Claude for eval orchestration) | $0.02-0.05 (2-5 min @ Cloud Run) | $0.07-0.25 |
| **Compliance** | $0.02-0.05 (lighter agent usage, mostly rule checking) | $0.01-0.03 (1-3 min) | $0.03-0.08 |
| **QA Generation** | $0.10-0.30 (agent generates tests + runs browser) | $0.03-0.10 (3-10 min, browser overhead) | $0.13-0.40 |

**Insight:** Compliance testing is the cheapest vertical to operate — the agent does mostly rule matching, not heavy LLM inference. This makes it a good candidate for a generous free tier to drive adoption.

**Unified vs per-vertical pricing:** Unified pricing recommended for simplicity. Per-vertical pricing adds confusion and administrative overhead. The cost differences can be absorbed into the margin — LLM Eval's higher cost is offset by QA Generation's willingness to pay more.

## Unit Economics Estimate

### Cost Per Run (LLM Eval, average case)
| Component | Cost |
|-----------|------|
| Cloud Run compute (3 min @ 2 vCPU, 4GB) | $0.03 |
| Claude API (agent orchestration, ~5K tokens) | $0.08 |
| PostgreSQL storage (results) | $0.001 |
| Cloud Storage (artifacts, logs) | $0.001 |
| **Total platform cost per run** | **~$0.11** |

### Break-Even Analysis
| Scenario | Monthly Runs | Revenue | Platform Cost | Margin |
|----------|-------------|---------|---------------|--------|
| **10 Pro users** | 5,000 | $490 | $550 | -$60 (subsidized by growth) |
| **50 Pro users** | 25,000 | $2,450 | $2,750 | -$300 (near break-even) |
| **100 Pro + 10 Team** | 70,000 | $6,890 | $7,700 | -$810 (still growing) |
| **200 Pro + 50 Team + 5 Enterprise** | 200,000+ | $25,000+ | $22,000 | +$3,000 (profitable) |

**Insight:** The platform reaches profitability at ~200K runs/month with a mix of Pro, Team, and Enterprise customers. Enterprise customers are the margin driver — high revenue, negotiated rates, lower per-run cost due to dedicated infrastructure efficiencies.

### Hidden Revenue: Component Library Licensing
The component library itself becomes a monetizable asset. Enterprise customers may pay for access to the full component library (all verticals) even without running evaluations — similar to how Snyk charges for vulnerability database access. This creates a second revenue stream independent of compute costs.

## Pricing Recommendation

**Launch with Freemium + Per-Run model.** The free tier drives adoption and demonstrates value. The Pro tier ($49/mo) is positioned below DeepEval's per-user pricing and well below compliance SaaS pricing, making it accessible to individual developers and small teams. The Team tier ($199/mo) competes with Braintrust's $249/mo but includes more runs. Enterprise pricing is custom and includes the high-margin features (dedicated infrastructure, SLA, component library access).

**Key differentiator:** Users pay their own LLM costs (BYOK). The platform charges only for infrastructure + intelligence. This is materially cheaper than platforms that mark up API costs or require platform-specific tokens.

## Sources

- [LLMOps Tools Pricing Comparison 2026](https://coverge.ai/blog/llmops-tools-pricing-comparison)
- [Braintrust Pricing 2026](https://coverge.ai/blog/braintrust-pricing)
- [LangSmith Pricing 2026](https://pecollective.com/blog/langsmith-pricing/)
- [Qualys Pricing 2026](https://underdefense.com/industry-pricings/qualys-pricing-ultimate-guide-for-security-products/)
- [Mabl vs Testim 2026](https://aisotools.com/compare/mabl-vs-testim)

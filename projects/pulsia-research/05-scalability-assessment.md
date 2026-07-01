# Scalability Assessment — Pulsia Autonomous Platform via Harness Design Pattern

## Overview

This assessment analyzes how a harness-based implementation of a Pulsia-equivalent system would scale from 10 companies to 10,000+ companies. It identifies infrastructure bottlenecks, token cost projections, gate/hook complexity challenges, and proposes mitigation strategies for each.

The analysis uses Pulsia's disclosed operational data as a baseline: 2,000+ active companies generating 25,444 tasks and 16,325 messages per day, with $1.5M/month in API bills at scale.

---

## Scaling Tiers

### Tier 1: 10 Companies (Proof of Concept)

At 10 companies, the system operates comfortably within a single-machine deployment. Each company runs one nightly CEO cycle, delegating to 2-5 primitive loops per cycle. Total daily task volume is approximately 125 tasks (based on Pulsia's ~12.7 tasks/company/day average). A single LLM API subscription handles all inference. State files are local, tenant isolation is directory-based, and the cron scheduler runs as a simple job queue.

No meaningful bottlenecks exist at this scale. The primary concern is validating the loop composition model — ensuring gate contracts enforce correctly across orchestrator-to-primitive handoffs and that tenant state isolation holds under concurrent execution.

### Tier 2: 100 Companies (Early Production)

At 100 companies, daily task volume reaches approximately 1,270 tasks. The nightly CEO cycle window becomes a constraint — if each CEO cycle takes 3-5 minutes of LLM inference time, 100 sequential cycles require 5-8 hours. This exceeds a reasonable overnight window unless cycles run concurrently.

Infrastructure requirements shift:
- **Compute:** 5-10 concurrent harness loop runners needed
- **State management:** Directory-based state still viable but requires file locking or database migration
- **LLM throughput:** API rate limits become relevant; multiple API keys or a dedicated inference tier needed
- **Scheduling:** Simple cron insufficient; need a distributed job scheduler with retry logic

### Tier 3: 1,000 Companies (Growth Stage)

At 1,000 companies, daily tasks reach ~12,700 and the system hits multiple simultaneous bottlenecks. This is the critical scaling threshold where architectural decisions made at Tier 1-2 either hold or break.

### Tier 4: 10,000 Companies (Platform Scale)

At 10,000 companies, daily tasks approach 127,000. The system requires a fundamentally distributed architecture — no single-machine or simple multi-process model survives. This tier demands production-grade infrastructure comparable to what Pulsia has built with its $30M Series A funding.

---

## Bottleneck Analysis

### Bottleneck 1: LLM Token Throughput and Cost

**The Problem:** Each CEO cycle requires strategic reasoning (high-token operations using the most capable model tier). At 1,000 companies with an estimated 4,000-6,000 tokens per CEO assessment step and 2,000-4,000 tokens per primitive loop invocation, daily token consumption reaches 25M-50M tokens. At current Claude API pricing (~$15/M input tokens, ~$75/M output tokens for Opus-tier), monthly costs reach $200K-$500K for inference alone.

Pulsia's disclosed $1.5M/month API bill at ~2,000 active companies confirms this projection. Their per-company API cost is approximately $750/month — far exceeding the $49/month subscription price, which explains why the platform operates at a loss on pure subscription revenue.

**At 10,000 companies:** Monthly token costs would project to $7.5M/month at Pulsia's observed per-company rate, or $2.5M-$5M with optimization. This is the single largest scaling challenge.

**Mitigation Strategies:**
- **Model tiering:** Use cheaper models (Haiku/Sonnet) for routine primitive loops (marketing content, support responses) and reserve Opus for CEO-level strategic reasoning. This reduces average per-token cost by 60-80%.
- **Token caching:** Cache common assessments, template outputs, and shared lesson lookups. Anthropic's prompt caching can reduce input token costs by 90% for repeated context.
- **Batch inference:** Aggregate multiple tenant assessments into batch API calls during off-peak hours at discounted rates.
- **Self-hosted inference:** At 5,000+ companies, self-hosted GPU clusters become cost-competitive. Pulsia is pursuing this path with their GPU infrastructure buildout.
- **Cycle frequency optimization:** Not every company needs a nightly cycle. Dormant or low-activity companies could shift to weekly cycles, reducing active inference load by 40-60%.

### Bottleneck 2: Concurrent State Management

**The Problem:** The harness design pattern uses file-based state (session_state.json, workflow.json). At 10+ concurrent company cycles, file system contention creates race conditions. The tenant-scoped state model (`state/{tenant_id}/`) prevents cross-tenant conflicts, but the shared lessons aggregation layer and platform-level state (scheduler metadata, cost tracking, billing) become contention points.

At 1,000 companies with 50-100 concurrent cycles, the shared lessons write path could see 50+ concurrent appends. File-based state cannot handle this without corruption risk.

**At 10,000 companies:** Every shared resource becomes a bottleneck — lessons aggregation, billing state, scheduler metadata, platform metrics, and audit logs.

**Mitigation Strategies:**
- **Database migration for shared state:** Move shared lessons, billing, and platform metadata to a database (PostgreSQL/Neon) while keeping tenant-specific state in scoped files or per-tenant database schemas.
- **Write-ahead logging:** For tenant state, use append-only logs (like actions.jsonl) with periodic compaction rather than in-place JSON updates.
- **Event-driven lesson aggregation:** Replace synchronous shared lesson writes with an event queue (Redis, SQS). Primitive loops emit lesson candidates; a background aggregation worker processes them asynchronously.
- **Sharded tenant state:** Partition tenants across multiple state storage backends by hash prefix, distributing I/O load.

### Bottleneck 3: Infrastructure Provisioning at Scale

**The Problem:** Each Pulsia company gets provisioned infrastructure: Render web server, Neon database, GitHub repo, Stripe account, Meta ad account, email service. At 10 companies this is manageable. At 1,000 companies, provisioning becomes a combinatorial explosion of API calls, credentials, and third-party rate limits.

GitHub API rate limits (5,000 requests/hour for authenticated users), Render's deployment limits, and Neon's connection pooling all impose hard ceilings. Provisioning 100 companies in a burst (e.g., a marketing campaign drives signups) could exhaust API quotas within minutes.

**At 10,000 companies:** Third-party provider costs alone (Render hosting, Neon databases, GitHub repos) could reach $50K-$100K/month in raw infrastructure fees, separate from LLM costs.

**Mitigation Strategies:**
- **Lazy provisioning:** Don't provision infrastructure at signup. Provision components on first use — create the GitHub repo when the first engineering task runs, not when the company launches.
- **Shared infrastructure pools:** Use multi-tenant shared resources where isolation isn't critical. Shared database clusters with schema-per-tenant instead of database-per-tenant. Shared hosting with container isolation instead of separate Render instances.
- **Provisioning queue:** Rate-limit provisioning requests through a managed queue that respects third-party API limits, with exponential backoff and retry.
- **Infrastructure tiering:** Free/basic tiers get shared infrastructure; premium tiers get dedicated resources.

### Bottleneck 4: Gate and Hook Complexity

**The Problem:** The harness design pattern enforces quality through gate contracts (input/output validation at every step boundary) and hooks (PreToolUse/PostToolUse enforcement). At 10 companies with 6 loops each, the system evaluates approximately 240 gate checks per nightly cycle (4 steps × 2 gates × 6 loops × 10 companies). At 1,000 companies, this reaches 24,000 gate evaluations per night.

Gate evaluation itself is lightweight (JSON schema validation), but the cascading failure mode is the real concern. When a gate blocks execution (e.g., cost threshold exceeded), the blocked state must be persisted, the escalation loop invoked, and the CEO loop must handle the partial completion during its next cycle. At scale, 5-10% of cycles hitting gate blocks means 50-100 blocked states to manage per night at 1,000 companies.

The hook system adds overhead per action. If each primitive loop step triggers 3-5 hook evaluations (state validation, cost tracking, tenant isolation check, actions logging), 1,000 companies generate 72,000-120,000 hook invocations per night. Hook execution must complete in <100ms to avoid becoming a throughput bottleneck.

**At 10,000 companies:** Gate evaluations reach 240,000/night and hook invocations reach 720,000-1.2M/night. Hook infrastructure must be horizontally scalable.

**Mitigation Strategies:**
- **Hook tiering:** Classify hooks as critical (must run synchronously — tenant isolation, cost limits) and advisory (can run asynchronously — analytics, lesson submission). Only critical hooks block execution.
- **Compiled gate contracts:** Pre-compile gate contract schemas into fast validators (e.g., compiled JSON Schema) rather than interpreting them at runtime. This reduces per-gate evaluation from ~10ms to <1ms.
- **Gate result caching:** For idempotent gates (e.g., "does this tenant have budget remaining?"), cache results with a short TTL (5 minutes) to avoid redundant database queries.
- **Distributed hook execution:** Run hooks as lightweight serverless functions (Lambda/Cloud Functions) that scale independently of the loop runners.

### Bottleneck 5: Shared Lessons (Hive Mind) at Scale

**The Problem:** Pulsia's hive mind system distributes learned strategies across all tenants. At 10 companies, the shared lessons corpus is small and every lesson is relevant. At 1,000+ companies operating across diverse industries (SaaS, e-commerce, services, content), the lessons corpus grows into thousands of entries, most of which are irrelevant to any given tenant.

The CEO loop's assessment step reads shared lessons as input — passing 5,000 lesson entries as context to every CEO cycle wastes tokens and degrades reasoning quality. But filtering lessons requires understanding each tenant's business domain, which itself requires LLM inference.

**At 10,000 companies:** The lessons corpus could reach 50,000+ entries. Unfiltered ingestion is impossible; filtered ingestion requires a search/retrieval layer.

**Mitigation Strategies:**
- **Lesson categorization and tagging:** Tag lessons by domain (SaaS, e-commerce), function (marketing, engineering), and effectiveness score. Filter by relevance before passing to CEO cycles.
- **Embedding-based retrieval:** Embed lessons and tenant contexts into a vector database. Retrieve the top-K most relevant lessons per tenant per cycle instead of passing the full corpus.
- **Lesson decay:** Age out lessons that haven't been validated by recent outcomes. A lesson that boosted conversions 6 months ago may be stale due to platform algorithm changes.
- **Tiered propagation:** New lessons go to a staging pool. Only lessons validated across 5+ tenants get promoted to the global pool.

---

## Comparative Analysis: Harness vs. Traditional Architectures

| Dimension | Harness Pattern | Microservices + Task Queue |
|-----------|----------------|---------------------------|
| **State management** | File-based, tenant-scoped | Database-native, horizontally sharded |
| **Orchestration** | Agent reads specification, decides at runtime | Predefined workflows (Temporal, Airflow) |
| **Gate enforcement** | Schema-validated at every boundary | API contract validation, circuit breakers |
| **Scaling model** | Add loop runners, shard by tenant | Add service instances, shard by function |
| **Cost visibility** | Gate contracts track per-step costs | Requires separate cost monitoring layer |
| **Failure recovery** | Escalation loop + next-cycle retry | Dead letter queues, saga pattern rollback |
| **Learning/adaptation** | Shared lessons corpus, agent reasoning | Feature flags, A/B testing frameworks |

The harness pattern's advantage is adaptability — the agent can reason about novel situations without predefined workflow paths. The disadvantage is predictability — LLM-based decision-making introduces latency variance, cost variance, and occasional reasoning errors that deterministic workflows avoid.

At scale, a hybrid approach is likely optimal: use the harness pattern for strategic decision-making (CEO orchestrator) and routine but variable tasks (marketing content, support responses), while using deterministic workflows for well-understood pipelines (deployment, billing, provisioning).

---

## Cost Projection Summary

| Scale | Daily Tasks | Monthly Token Cost | Monthly Infra Cost | Total Monthly |
|-------|------------|-------------------|-------------------|---------------|
| 10 companies | 125 | $1,500-$3,000 | $500 | $2,000-$3,500 |
| 100 companies | 1,270 | $15,000-$30,000 | $5,000 | $20,000-$35,000 |
| 1,000 companies | 12,700 | $150,000-$500,000 | $30,000-$50,000 | $180,000-$550,000 |
| 10,000 companies | 127,000 | $1.5M-$5M | $100,000-$300,000 | $1.6M-$5.3M |

These projections assume Opus-tier models for CEO reasoning and Sonnet-tier for primitive loops, with prompt caching applied. Without model tiering and caching, costs at 1,000+ companies would be 2-3x higher.

---

## Conclusion

The harness design pattern can scale to 100-500 companies with moderate architectural investment (database-backed shared state, concurrent loop runners, model tiering). Beyond 1,000 companies, the pattern requires significant infrastructure extensions — distributed state management, embedding-based lesson retrieval, horizontally scalable hook execution, and self-hosted inference. The core loop composition model (orchestrator calls primitives via gate contracts) remains sound at any scale, but the infrastructure beneath it must evolve from single-machine file-based state to distributed cloud-native systems.

The most critical bottleneck is LLM token cost — it dominates total operating expense at every scale tier and directly determines unit economics viability. Pulsia's $1.5M/month API bill at 2,000 active companies ($750/company/month against $49/month subscription) demonstrates that the current cost structure is unsustainable without significant optimization or revenue model changes.

---

## Sources

- Pulsia architecture analysis (`projects/pulsia-research/02-architecture.md`)
- Pulsia company overview (`projects/pulsia-research/01-company-overview.md`)
- Architectural blueprint (`projects/pulsia-research/04-architectural-blueprint.md`)
- Harness applicability assessment (`projects/pulsia-research/03-harness-applicability.md`)

# Enterprise Adoption Trends — Frontier vs Chinese vs On-Prem (2025-2026)

## Market Share Snapshot (Mid-2026)

| Provider/Category | Enterprise LLM Spend Share | Change from 2024 |
|---|---|---|
| Anthropic (Claude) | 32-40% | +25pp (was ~15%) |
| OpenAI (GPT) | 20-27% | -28pp (was ~55%) |
| Google (Gemini) | 20-21% | +13pp (was ~7%) |
| Meta (Llama) | 9% | +6pp |
| DeepSeek | 1-6% | New entrant |
| Qwen (Alibaba) | 9-12% global usage | New entrant |
| Other (Cohere, Mistral, etc.) | ~3% | Stable |

**Source:** Menlo Ventures 2025 Mid-Year LLM Market Update; multiple corroborating sources.

## Key Findings

### 1. Frontier Models Still Dominate Enterprise

87% of enterprise LLM workloads run on proprietary models (up from 81% in early 2025). Open-source share declined to 13%, down from 19%. Three companies (Anthropic, OpenAI, Google) account for 88% of enterprise LLM API usage.

### 2. Anthropic Displaced OpenAI as Enterprise Leader

Anthropic overtook OpenAI as the top enterprise LLM provider in 2025. Claude's strength in coding (SWE-bench leadership), safety positioning, and enterprise features (longer context, tool use) drove the shift. OpenAI's market share dropped from 55% (Jan 2025) to 27-40% (mid-2026).

### 3. Chinese Models: Developer Adoption ≠ Enterprise Adoption

DeepSeek and Qwen combined represent ~15% of global AI market — up from <1% at start of 2025. However, enterprise adoption remains limited:
- **Geopolitical risk:** US enterprises in regulated industries (banking, defense, healthcare) largely avoid Chinese-origin models
- **Data sovereignty concerns:** Data routing through Chinese infrastructure creates compliance exposure
- **Developer adoption is strong:** Chinese open-source models rose from 1.2% to ~30% of weekly token usage in some weeks of 2025, but primarily among developers and startups, not enterprise production

**Notable exception:** Airbnb CEO Brian Chesky publicly stated the company "heavily relies on Alibaba's Qwen model" for production workloads, citing speed, quality, and cost-effectiveness.

### 4. Enterprise Use Case Segmentation

| Use Case | Dominant Model Type | Notes |
|---|---|---|
| Complex reasoning | Frontier (Claude, GPT-5) | Quality premium justified |
| Code generation | Frontier + Open-weight | Open-weight closing gap |
| Classification/extraction | Open-weight preferred | Cost optimization |
| Summarization | Open-weight preferred | Good-enough quality |
| Translation | Open-weight preferred | Cost-sensitive, high volume |
| Regulated/sensitive | On-prem open-weight | Data sovereignty requirement |

### 5. The Routing Architecture Emerges

The optimal 2026 enterprise architecture is a model routing layer:
- **80% of requests** (classification, extraction, summarization) → open-weight models at 1/20th cost
- **20% of requests** (complex reasoning, novel code generation) → frontier models where quality premium justifies cost

This is partial migration, not wholesale replacement.

## Enterprise LLM Market Size

- Enterprise LLM spend reached $8.4B by mid-2025
- Projected $15B by end of 2026
- Proprietary LLMs hold 42.62% of total market (by type segment) in 2025

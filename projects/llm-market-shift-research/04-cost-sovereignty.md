# Cost, Latency, and Sovereignty Drivers (2025-2026)

## API Pricing Comparison (July 2026)

### Flagship Models (per 1M tokens: input/output)

| Model | Input | Output | Relative Cost |
|---|---|---|---|
| GPT-5.5 | $5.00 | $30.00 | Baseline |
| GPT-5.4 Pro | $30.00 | $180.00 | 6x premium |
| Claude Opus 4.8 | $5.00 | $25.00 | ~0.8x |
| Gemini 3.1 Pro | $2.00 | $12.00 | ~0.4x |
| DeepSeek V4 Flash | $0.14 | $0.28 | ~0.01x (100x cheaper) |
| DeepSeek R1 | $0.55 | $2.19 | ~0.07x |

### Budget/Value Tier

| Model | Input | Output | Notes |
|---|---|---|---|
| GPT-5.4 mini | $0.40 | $1.60 | OpenAI budget |
| Claude Sonnet 5 | $2.00 | $2.00 | Mid-tier |
| Gemini 3.1 Flash-Lite | $0.10 | $0.40 | Cheapest proprietary |
| DeepSeek V4 Flash | $0.14 | $0.28 | Cheapest overall |

### Self-Hosted (Approximate)

| Model | Cost/M Tokens | Notes |
|---|---|---|
| Llama 4 Maverick (self-hosted) | $0.20-0.50 | Requires GPU infrastructure |
| Qwen 3 72B (self-hosted) | $0.30-0.80 | Multi-GPU required |
| Mistral Small 3 (self-hosted) | $0.10-0.30 | Single GPU |

## Why Companies Switch

### 1. Cost at Scale

- **Uber** exhausted its annual token budget in 4 months
- **Salesforce** faces $300M in Anthropic costs in 2026
- At scale, API costs become a P&L line item, not an experiment budget
- DeepSeek V3.2 output tokens: $0.28/M vs GPT-5's $30/M = **107x cheaper**
- Even vs GPT-4.1 ($8/M output), DeepSeek is **29x cheaper**

### 2. Hidden Cost Multipliers

- **Reasoning tokens:** Models like GPT-5 and DeepSeek R1 generate internal "thinking" tokens billed as output. Can make actual cost 3-10x the headline price
- **Context window costs:** Longer contexts = more input tokens per request
- **Retry/error costs:** Failed API calls still consume tokens
- **Vendor lock-in:** Switching costs increase over time (prompt engineering, fine-tuning, evaluation infrastructure)

### 3. Data Sovereignty

- **EU AI Act** (Aug 2026): High-risk AI obligations including logging, conformity assessment, FRIA
- **US CLOUD Act:** Even EU-hosted data on US cloud providers subject to US government access
- **China data laws:** Enterprises using Chinese APIs face reciprocal data exposure concerns
- **True sovereignty** requires providers fully within the jurisdiction

### 4. Latency

- Self-hosted models: 10-50ms first token (depends on hardware)
- API providers: 100-500ms first token (network + queue + inference)
- For real-time applications (trading, robotics, gaming), latency difference is material

### 5. Regulatory Compliance

- Financial services: Data residency, model auditability, explainability
- Healthcare: HIPAA, patient data cannot leave controlled environments
- Government: Classification levels, ITAR, FedRAMP
- Penalties: Up to 35M EUR or 7% global revenue (EU AI Act)

## Enterprise Case Studies

| Company | Action | Reason |
|---|---|---|
| Airbnb | Adopted Qwen for production | Speed, quality, cost |
| Uber | Hit token budget in 4 months | Cost at scale |
| Salesforce | $300M Anthropic costs | Cost pressure |
| Financial services (sector) | On-prem Llama/Mistral | Data residency |
| EU enterprises | Sovereign cloud + open-weight | EU AI Act compliance |

## The Routing Pattern

The dominant enterprise strategy in 2026 is **intelligent model routing**:
- **Tier 1 (frontier):** Complex reasoning, novel code gen → Claude/GPT-5 ($5-30/M)
- **Tier 2 (mid-range):** Moderate tasks → Gemini/Claude Sonnet ($2-12/M)
- **Tier 3 (budget):** Classification, extraction, summarization → DeepSeek/Llama ($0.14-0.50/M)

This 80/20 split (80% budget, 20% frontier) can reduce LLM costs by 70-90% while maintaining quality where it matters.

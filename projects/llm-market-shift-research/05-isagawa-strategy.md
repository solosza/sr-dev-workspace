# Isagawa Strategy Recommendations

## Context

Isagawa builds:
1. **Isagawa Kernel** — self-building, self-improving agent framework (MIT license)
2. **QA Platform** — Selenium-based test automation with AI agent orchestration
3. **Eval Harness** — DeepEval-based evaluation framework for agent quality

Existing assets:
- Model router research complete (backlog 087/091)
- Multi-model routing architecture designed
- Eval harness benchmarks against single provider (Anthropic/Claude)

## Strategic Assessment

### Where Isagawa Wins Regardless of Model Choice

The kernel's value proposition is **model-agnostic by design:**
- Protocol-driven agent behavior (hooks, gates, lessons) works with ANY underlying LLM
- The kernel doesn't generate code — it orchestrates, enforces quality, and self-improves
- Eval harness measures agent behavior quality, not raw model capability
- The routing pattern (frontier for complex, open-weight for routine) is exactly the architecture Isagawa should enable

**Key insight:** As model commoditization accelerates, the value shifts from "which model" to "how you orchestrate models." This is Isagawa's core competency.

## Recommendations

### 1. Support Multi-Model Backends (HIGH PRIORITY)

**Action:** Activate the model router (backlog 087/091) as a first-class kernel feature.

**Rationale:**
- 80/20 routing pattern is becoming enterprise standard
- Enterprises need to route by task complexity, not just model preference
- Cost optimization (70-90% reduction) is a compelling sales argument
- Data sovereignty requirements mean some requests MUST go to on-prem models

**Implementation:**
- Tier 1 (frontier): Complex reasoning, agentic coding → Claude/GPT-5
- Tier 2 (mid-range): Moderate tasks → Gemini/Claude Sonnet
- Tier 3 (budget/sovereign): Classification, extraction → DeepSeek/Llama/self-hosted
- Routing criteria: task complexity score, data sensitivity classification, cost budget

**Risk:** LOW — Model router already researched. Architecture is additive, not a rewrite.

### 2. Eval Harness Cross-Provider Benchmarking (HIGH PRIORITY)

**Action:** Extend eval harness to benchmark agent behavior across providers.

**Rationale:**
- Enterprises evaluating model switches need quality assurance
- "Does our agent perform the same with Llama as with Claude?" is a critical question
- SWE-bench contamination concerns make provider-specific benchmarks unreliable
- Isagawa's eval harness already measures agent behavior (not raw model capability) — this is the right abstraction level

**Implementation:**
- Add provider parameter to eval runs: `--provider anthropic|openai|deepseek|ollama`
- Run identical eval scenarios across providers
- Generate comparison reports: quality delta, cost delta, latency delta
- Flag tasks where open-weight models underperform (these stay on frontier)

**Risk:** MODERATE — Requires API keys for multiple providers. DeepSeek API may have availability issues. Self-hosted evaluation requires GPU infrastructure or cloud GPU access.

### 3. Position as Model-Agnostic Orchestration Layer (STRATEGIC)

**Action:** Marketing and architecture messaging should emphasize model independence.

**Rationale:**
- The market is fragmenting — no single model will dominate
- Enterprises need frameworks that survive model switches
- "Works with any LLM" is a durable competitive advantage
- Open-source kernel (MIT) + model-agnostic design = maximum adoption surface

**Positioning:**
- "Isagawa Kernel: The operating system for AI agents — bring your own model"
- Emphasize: protocol enforcement, self-improvement, quality gates work regardless of model
- Case study potential: "Same kernel, 90% cost reduction by routing to open-weight for routine tasks"

**Risk:** LOW — This is already true. Just needs explicit messaging.

### 4. On-Prem / Sovereign Deployment Support (MEDIUM PRIORITY)

**Action:** Ensure kernel + eval harness work with self-hosted models via Ollama/vLLM.

**Rationale:**
- 71% of AI infrastructure runs outside public cloud
- EU AI Act (Aug 2026) creates compliance demand for sovereign AI
- Financial services, healthcare, government are high-value verticals
- Self-hosted Llama 4 + Isagawa Kernel = complete sovereign AI agent stack

**Implementation:**
- Test kernel with Ollama (local) and vLLM (production) backends
- Document deployment guide: "Isagawa Kernel on sovereign infrastructure"
- Ensure eval harness works with local model endpoints

**Risk:** MODERATE — Requires testing with various model sizes. Smaller models may not meet quality thresholds for complex agentic tasks.

## Risk Assessment Summary

| Strategy | Priority | Risk | Investment | Payoff Timeline |
|---|---|---|---|---|
| Multi-model router | HIGH | LOW | Medium (activate existing research) | 1-2 months |
| Cross-provider eval | HIGH | MODERATE | Medium (extend eval harness) | 2-3 months |
| Model-agnostic positioning | STRATEGIC | LOW | Low (messaging + docs) | Immediate |
| On-prem/sovereign support | MEDIUM | MODERATE | High (testing + docs) | 3-6 months |

## What NOT To Do

1. **Don't double down on frontier-only.** The market is fragmenting. Locking to one provider is a business risk.
2. **Don't build a model.** Isagawa's value is orchestration, not model training. The model layer is commoditizing.
3. **Don't ignore Chinese models.** Despite geopolitical concerns, DeepSeek/Qwen are technically competitive. Support them as backend options even if not recommended for regulated workloads.
4. **Don't chase benchmarks.** SWE-bench scores are scaffold-dependent and contamination-prone. Isagawa's eval harness should measure real-world agent behavior, not synthetic benchmarks.

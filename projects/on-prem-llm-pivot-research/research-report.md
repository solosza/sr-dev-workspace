# On-Prem LLM Pivot — Research Report

**Date:** 2026-07-13
**Author:** Isagawa Research Pipeline (Backlog 197)
**Inputs:** [01-trend-validation.md](01-trend-validation.md), [02-solution-landscape.md](02-solution-landscape.md), [03-isagawa-pivot-analysis.md](03-isagawa-pivot-analysis.md), [04-personal-skill-path.md](04-personal-skill-path.md)

---

## Executive Summary

The enterprise shift toward on-premises LLM deployment is a validated, accelerating trend driven by IP protection incidents, regulatory mandates (HIPAA, SOC2, EU AI Act), and the rapid maturation of open-weight models that now match frontier API capabilities for most production use cases. On-prem GPU infrastructure is the fastest-growing deployment segment (15.7% CAGR), 75% of enterprises have implemented or are considering bans on public LLM APIs, and open-weight models like DeepSeek V4 Pro have reached 80.6% on SWE-Bench Verified — effectively closing the gap with proprietary models for coding and reasoning tasks.

Isagawa is well-positioned to profit from this shift. The Isagawa Kernel — a production-grade agent governance framework with enforcement hooks, self-improvement loops, and autonomous cycling — has no direct competitor. Orchestration frameworks (LangGraph, CrewAI, AutoGen) help build agents; the Kernel ensures agents stay safe and correct. Combined with the existing QA/eval platform (DeepEval integration), healthcare domain expertise (HMSA, RT automation), and battle-tested pipeline orchestration (170+ backlogs executed), Isagawa holds a differentiated position at the intersection of agent governance, model evaluation, and regulated-industry deployment.

The primary gap is execution speed: the Kernel needs a model-agnostic inference adapter (currently hardcoded to `claude -p`), and Alain needs hands-on GPU infrastructure and model serving skills. Both gaps are closable within 30-60 days.

---

## Recommendation: GO

**Position:** Invest in the on-prem LLM pivot. The market demand is real, Isagawa's assets are differentiated, and the skills gap is bridgeable. The risk of inaction — watching the market mature while competitors build governance layers — outweighs the execution risk.

**Evidence chain:**

1. **Market demand is validated** (01-trend-validation): $247B enterprise GPU infrastructure market growing at 15.7% CAGR. 75% of companies restricting public LLM APIs. Samsung incident triggered industry-wide bans across finance, tech, defense, healthcare. Shadow AI crisis (90%+ employees using personal AI accounts with zero corporate controls) will force enterprises toward managed private deployments.

2. **The solution landscape is mature enough** (02-solution-landscape): Five deployment tiers (own hardware, private cloud/VPC, open-weight models, inference stacks, enterprise platforms) are all production-ready. vLLM is the established production serving standard. NVIDIA NIM provides enterprise-grade packaging. Open-weight models (DeepSeek V4 Pro, Qwen3-Coder, Kimi K2) are competitive with frontier APIs for most tasks. The infrastructure to self-host is no longer experimental.

3. **Isagawa has differentiated assets** (03-isagawa-pivot-analysis): The Kernel's enforcement loop (protocol → hooks → anchor → learn → self-improve) is unique. No competing framework provides agent governance — they provide orchestration. The QA/eval platform architecture transfers directly to model evaluation. Healthcare domain knowledge (HMSA, RT automation) opens regulated-industry doors. Three complementary offerings form a reinforcing sequence: consulting generates case studies, Kernel generates platform moat, eval platform generates recurring revenue.

4. **The skill path is feasible** (04-personal-skill-path): Primary target roles (AI Platform Engineer $180-310K, LLMOps Engineer $145-250K, Production LLM Infrastructure Engineer $145-320K) align with existing strengths in agent orchestration and evaluation. The on-prem LLM skills (model serving, quantization, fine-tuning) are acquirable in 60-90 days with consumer hardware and cloud GPU rentals. Three portfolio projects reuse existing Isagawa assets and simultaneously build the business offerings.

**What this recommendation is NOT:** It is not a recommendation to abandon cloud APIs or Claude. The market is moving toward hybrid deployments (regulated workloads on-prem, experimental workloads on cloud APIs). The pivot extends Isagawa's capabilities to cover both sides of that split — not to replace one with the other.

---

## Top 3 Isagawa Opportunities

### 1. Kernel-Governed Agent Harness for Private LLMs

The highest-differentiation play. Package the Kernel as the governance layer for agentic AI running on open-weight models. Enterprises that banned cloud LLM APIs still need agentic automation — the Kernel solves "agents are unreliable" without requiring cloud API access. No competitor has enforcement hooks, anchor protocols, self-improvement loops, and autonomous cycling. LangGraph, CrewAI, and AutoGen are orchestrators; the Kernel is a governance framework. MIT license removes procurement friction. Open-core revenue model: Kernel free, enterprise features (SSO, audit dashboard, multi-team orchestration) paid. Critical gap: model-agnostic inference adapter (4-8 weeks to MVP). First client path: open-source community adoption → healthcare pilot → enterprise sales. See [03-isagawa-pivot-analysis.md](03-isagawa-pivot-analysis.md) §Candidate A for full analysis.

### 2. Private Model QA/Eval Platform

A self-hosted evaluation platform for organizations deploying open-weight models. Every company running Llama 4, DeepSeek V4, or Qwen3 needs to answer "is this model good enough?" — and the existing cloud eval platforms (Humanloop, Braintrust) contradict the on-prem thesis by being cloud-hosted. The DeepEval integration, multi-interface QA architecture, and gate contract pattern already exist. Needs standalone packaging and model-specific eval templates (6-10 weeks). Revenue model: open-core or license per deployment. See [03-isagawa-pivot-analysis.md](03-isagawa-pivot-analysis.md) §Candidate B.

### 3. On-Prem Healthcare LLM Consulting

Fastest path to revenue — requires no product build, just packaged expertise. The combination of healthcare domain knowledge (HMSA), agent governance (Kernel), QA/eval capability, and self-hosted deployment expertise is unique among small consultancies. The RT automation project is the natural pilot. Revenue model: project-based consulting ($150-250/hr) or fixed-fee engagements ($25K-$75K per deployment). Time to first revenue: 1-3 months. Best used as a revenue bridge while building offerings #1 and #2. See [03-isagawa-pivot-analysis.md](03-isagawa-pivot-analysis.md) §Candidate C.

---

## Personal 30-60-90 Plan Summary

The skill path bridges Alain's current strengths (agent governance, LLM evaluation, healthcare domain, pipeline orchestration) to the on-prem LLM skills the market demands (model serving, quantization, fine-tuning, private RAG). Three phases, three portfolio projects:

**Phase 1 (Days 1-30): Local Model Serving & Agent Adapter.** Install Ollama and vLLM, serve open-weight models locally, build the Kernel's model-agnostic inference adapter, run a full backlog through the Kernel loop on a local model. Publish Portfolio Project 1: "Kernel + Ollama Local Agent Loop." This directly closes the #1 gap (model-agnostic adapter) from the pivot analysis.

**Phase 2 (Days 31-60): Quantization, Fine-Tuning & Eval Pipeline.** Hands-on with GGUF/AWQ quantization formats, LoRA/QLoRA fine-tuning via Unsloth, and extraction of the DeepEval integration into a standalone self-hosted eval pipeline. Publish Portfolio Project 2: "Self-Hosted LLM Evaluation with Gate Contracts." Resume now includes optimization and evaluation skills.

**Phase 3 (Days 61-90): Production Deployment & Healthcare Specialization.** Production-grade vLLM deployment (load balancer, monitoring), private RAG system (vector DB + retrieval pipeline), and healthcare compliance validator (HIPAA audit trail, PHI detection, access control gates). Publish Portfolio Project 3: "Healthcare LLM Compliance Validator." Target senior roles: AI Platform Engineer ($180-310K), Production LLM Infrastructure Engineer ($145-320K).

Full plan with weekly breakdowns and learning resources: [04-personal-skill-path.md](04-personal-skill-path.md).

---

## What Would Change the Recommendation

Re-evaluate if any of these trigger conditions materialize:

| Trigger | Impact | Action |
|---------|--------|--------|
| **Frontier APIs close the governance gap** — a major provider (OpenAI, Anthropic, Google) ships a built-in agent governance framework with enforcement hooks, self-improvement, and audit trails | Reduces Kernel's differentiation for cloud-API deployments. On-prem governance value persists (vendor-independent), but the moat narrows | Re-assess Kernel positioning — shift emphasis to vendor-independent, multi-model governance rather than cloud-vs-local |
| **Open-weight model quality plateaus** — the capability gap with frontier APIs stops narrowing or widens (e.g., GPT-6 creates a new capability jump that open-weight models can't match for 12+ months) | Weakens the case for on-prem as primary deployment. Hybrid with heavier cloud reliance becomes dominant | Pivot emphasis to private-cloud/VPC tier (Tier B) rather than own-hardware (Tier A). Consulting and eval platform value persists regardless |
| **Regulatory rollback** — HIPAA AI requirements or EU AI Act enforcement delays reduce compliance pressure on enterprises | Slows enterprise urgency to move on-prem. Extends the timeline for consulting revenue from regulated industries | Deprioritize healthcare consulting; accelerate open-source community adoption for Kernel and eval platform instead |
| **A direct competitor ships agent governance for private LLMs** — LangChain, Microsoft (AutoGen), or a funded startup releases an enforcement-loop framework targeting the same market | First-mover advantage erodes. Must compete on maturity and battle-tested record (170+ backlogs, MIT license) | Accelerate Kernel adapter timeline. Publish benchmarks comparing governance quality. Lean into community adoption and healthcare specialization as defensible niches |
| **Consumer GPU costs spike** — tariffs, supply constraints, or NVIDIA pricing changes make self-hosting significantly more expensive | Shifts cost equation back toward cloud APIs for all but the most regulated workloads | Emphasize private-cloud tier (AWS Bedrock, Azure OpenAI with VPC) in consulting. Kernel and eval platform remain valuable regardless of hosting tier |
| **Personal hardware insufficient** — Alain's current machine cannot run even 7-8B models locally, and cloud GPU rental costs exceed $200/month for Phase 1-2 work | Slows the 30-60-90 plan; portfolio projects delayed | Budget for a consumer GPU upgrade (RTX 4070 Ti 16GB ~$750, or RTX 4090 24GB ~$1,600). The investment pays for itself in portfolio value and target role salary increase |

---

## Methodology

This report synthesizes four research deliverables produced by the Isagawa Kernel's execute-pipeline:

1. **Trend Validation** (01) — Web research across enterprise adoption data, IP protection incidents, vendor moves, regulated industry drivers, and counter-evidence (API mitigations). 15+ sourced data points.
2. **Solution Landscape** (02) — Five-tier analysis of deployment options with GPU pricing, TCO calculations, framework comparisons, and capability gap assessment. 25+ sources.
3. **Isagawa Pivot Analysis** (03) — Asset inventory mapped to four candidate offerings, ranked by differentiation and asset fit, with gap analysis and strategic sequencing.
4. **Personal Skill Path** (04) — Skill inventory mapped to landscape tiers, target job titles with salary ranges, three portfolio projects reusing existing assets, and phased 30-60-90 learning plan.

All claims in this report trace to sourced evidence in the input documents. No new research was conducted for this synthesis.

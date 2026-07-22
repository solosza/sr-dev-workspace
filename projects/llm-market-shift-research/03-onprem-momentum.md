# On-Prem / Self-Hosted LLM Momentum (2025-2026)

## Key Models for Enterprise Self-Hosting

| Model | Parameters | License | GPU Requirement | Notes |
|---|---|---|---|---|
| Llama 4 Scout | 17B active (MoE) | Llama 4 Community | Single GPU | Matches GPT-4o on most benchmarks |
| Llama 4 Maverick | 17B active (larger MoE) | Llama 4 Community | Multi-GPU | Competitive with frontier |
| Mistral Small 3 | 22B | Apache 2.0 | Single GPU | Consumer + enterprise |
| Mistral Large | Commercial | Commercial | Multi-GPU | Enterprise-focused |
| Qwen 2.5/3 | Various (7B-72B) | Apache 2.0 | Varies | Strong coding variants |
| DeepSeek V4 | Various | MIT | Multi-GPU | Cost leader |
| Falcon 2 | 11B | Apache 2.0 | Single GPU | Permissive licensing favorite |
| Phi-3/4 (Microsoft) | 3.8B-14B | MIT | Consumer GPU | Small but capable |

## Infrastructure Stack (2026 Standard)

**Serving engines:**
- **vLLM** — emerged as the production standard for LLM inference serving
- **SGLang** — competitive alternative, growing adoption
- **TGI (Hugging Face)** — moved to maintenance mode (Dec 2025), effort redirected upstream to vLLM/SGLang

**Hardware:**
- NVIDIA H100/H200 — enterprise standard
- AMD MI300X — competitive alternative, growing ecosystem
- NVIDIA TensorRT-LLM — optimization framework
- DeepSpeed — distributed inference

## Adoption Data

- **71% of AI infrastructure** ran outside public cloud by 2025, driven by financial services data-residency requirements and enforceable AI regulation
- Self-hosting costs: **$0.20-0.50/M tokens** for Llama 4 Maverick vs. $2-15/M for frontier APIs
- **Breakeven point:** Self-hosting becomes cheaper at 10M-30M tokens/day depending on model size and infrastructure
- Open-weight models hold ~11-13% of enterprise market share overall, but growing in regulated sectors

## Regulatory Drivers

- **EU AI Act** fully enforceable August 2, 2026 — high-risk AI obligations, logging requirements, conformity assessments
- Penalties: up to 35M EUR or 7% of global revenue for prohibited practices
- **US CLOUD Act exposure:** Data in US cloud provider (even EU data center) remains subject to US government access. Microsoft acknowledged this limitation (July 2025)
- **True sovereignty** requires providers headquartered and operated entirely within EU/EFTA

## Sector-Specific Adoption

| Sector | On-Prem Adoption | Primary Driver |
|---|---|---|
| Financial services | HIGH | Data residency, regulatory compliance |
| Healthcare | HIGH | HIPAA, patient data sovereignty |
| Government/Defense | HIGH | National security, data classification |
| Telecommunications | MODERATE-HIGH | Regulatory requirements |
| Tech/Startups | LOW | Prefer API convenience |
| Retail/E-commerce | LOW | Cost optimization at scale |

## Key Trend

The shift is not "on-prem vs cloud" — it's "sovereign infrastructure vs third-party APIs." Organizations increasingly want control over their AI stack, whether that means on-prem hardware, sovereign cloud, or private VPC deployments. The open-weight model ecosystem now provides quality sufficient for 80% of use cases, making self-hosting a viable option where it wasn't 18 months ago.

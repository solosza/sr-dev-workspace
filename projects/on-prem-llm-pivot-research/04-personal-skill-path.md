# Personal Skill Path — On-Prem LLM Skills for Job Hunting

**Date:** 2026-07-13
**Inputs:** 02-solution-landscape.md, web research on job market (July 2026)

---

## 1. Skill Inventory (Mapped to Landscape Tiers)

Each skill maps to one or more tiers from 02-solution-landscape (A=Own Hardware, B=Private Cloud/VPC, C=Open-Weight Models, D=Inference Stacks, E=Enterprise Platforms).

| Skill | Tier(s) | Current Level | Gap |
|-------|---------|---------------|-----|
| **GPU infrastructure basics** (CUDA, driver stack, multi-GPU, VRAM budgeting) | A, D | Low — no hands-on GPU infra work | Large — need hardware access + practice |
| **Model serving (vLLM, Ollama, NIM)** | D | Low — used Ollama briefly; no vLLM or NIM | Medium — can learn on consumer GPU + cloud rental |
| **Quantization (GGUF, AWQ, GPTQ)** | C, D | None | Medium — conceptual, needs hands-on with llama.cpp/Unsloth |
| **Fine-tuning (LoRA, QLoRA)** | C | None | Medium — Unsloth + QLoRA on single consumer GPU is accessible |
| **Private RAG** | B, D, E | Medium — built RAG-adjacent patterns in Kernel pipeline, no vector DB deployment | Small — architecture transfers, needs vector DB hands-on |
| **Security/compliance for AI deployments** | A, B, E | Medium — HIPAA-adjacent from HMSA, SOC2 awareness, no hands-on AI compliance auditing | Small — domain knowledge exists, needs AI-specific compliance framework |
| **Agent orchestration & governance** | All | High — Kernel is production-grade, 170+ backlogs executed | None — this is the differentiator |
| **Evaluation/testing for LLMs** | All | High — DeepEval integration, gate contracts, multi-interface QA | Small — needs model-specific eval templates |
| **Python ML ecosystem** (PyTorch, transformers, HuggingFace) | C, D | Medium — Python proficient, limited direct ML library use | Medium — needs hands-on with transformers library |
| **Docker/containerization for ML** | A, D, E | Medium — Docker user, not ML-specific container builds | Small — extend existing Docker skills to vLLM/NIM containers |

### Strengths to Lead With
- Agent governance (unique — no competitor framework has enforcement hooks + self-improvement)
- LLM evaluation/QA methodology (DeepEval + multi-interface architecture)
- Healthcare domain (HIPAA, EMR integration, compliance workflows)
- Autonomous pipeline orchestration (Kernel cycling, task decomposition, sub-agent spawning)

### Skills to Acquire
- GPU infrastructure + model serving (vLLM, Ollama, NIM) — the deployment layer
- Quantization + fine-tuning (GGUF, LoRA/QLoRA) — the model optimization layer
- Vector databases + private RAG (Qdrant, Chroma, Weaviate) — the retrieval layer

---

## 2. Target Job Titles & Market Demand

### Primary Targets (Highest Overlap with Existing Skills)

**AI Platform Engineer / AI Infrastructure Engineer**
- Salary: $180K–$310K base (mid-to-senior US)
- What they do: Model gateways, evaluation infrastructure, RAG pipelines, agent runtimes, prompt versioning, cost/latency observability
- Why it fits: The Kernel IS an agent runtime + evaluation infrastructure. The role is the Kernel's natural organizational home
- Overlap with agent-harness positioning: Near-total. "AI Platform Engineer" is essentially "Agent Harness Engineer" with infrastructure scope added
- Sample postings: LinkedIn "Platform Engineer (AI/LLM Infrastructure)" via Dice; LinkedIn "Senior GenAI Platform Engineer / Senior LLM Infrastructure Engineer (On-Prem AI Platform)" at AsceticVoyage
- Sources: [JobsByCulture AI Platform Engineer Career Path 2026](https://jobsbyculture.com/blog/ai-platform-engineer-career-path-2026), [Acceler8 In-Demand ML Roles 2026](https://www.acceler8talent.com/resources/blog/the-most-in-demand-machine-learning-roles-in-2026--managing-the-ai-talent-frontier/)

**LLMOps Engineer / AI Ops Engineer**
- Salary: $145K–$250K base
- What they do: Own prompt, eval, RAG, and guardrail infrastructure — sit closer to product than data platform. "MLOps but for LLMs"
- Why it fits: The Kernel's loop (session-start → anchor → work → complete) IS an LLMOps lifecycle. DeepEval integration IS eval infrastructure
- Overlap with agent-harness positioning: Strong. LLMOps is the operational layer; agent harness is the execution layer. Same person in many orgs
- Sources: [MLOps vs LLMOps UK 2026](https://machinelearningjobs.co.uk/career-advice/mlops-vs-llmops-engineer-uk-2026), [Ivan Turkovic AI Job Titles 2026](https://www.ivanturkovic.com/2026/04/24/ai-job-titles-2026-naming-chaos/)

**Production LLM Infrastructure Engineer**
- Salary: $145K–$320K base (25-40% premium over comparable ML engineer)
- What they do: Own the retrieval layer, eval harness, prompt versioning, cost monitoring, latency budgets, on-call for model deployment issues
- Why it fits: Direct match for someone who builds and operates LLM-powered systems in production. The Kernel's enforcement loop is a production reliability mechanism
- Overlap: The "production" qualifier filters for people who've shipped — the 170+ backlogs and cycling runs are evidence
- Sources: [KORE1 How to Hire LLM Engineers 2026](https://www.kore1.com/hire-llm-engineers-2026/), [ZipRecruiter LLM Engineer Jobs](https://www.ziprecruiter.com/Jobs/Llm-Engineer)

### Secondary Targets (Require More Skill Acquisition)

**ML Infrastructure Engineer**
- Salary: $200K–$350K base at major companies
- What they do: GPU cluster management, training pipelines, distributed systems for ML workloads
- Gap: Requires deeper GPU/CUDA/distributed training experience than current portfolio demonstrates
- Path: Build GPU infra skills in Phase 1-2, then target these roles

**AI Solutions Architect**
- Salary: $160K–$280K base
- What they do: Design AI deployment architectures for enterprise clients — model selection, infrastructure sizing, compliance mapping
- Why it fits: The research from this very pipeline (trend validation, solution landscape, pivot analysis) IS solutions architecture work. Healthcare domain adds vertical expertise
- Gap: Needs cloud certification (AWS/Azure AI) and reference deployments to credentialize

### Title Chaos Context

The AI job title landscape in 2026 is described as "the worst naming disaster the industry has produced since we decided 'DevOps' was a person rather than a practice." In a single week, roles were posted for 25+ distinct AI engineering titles that overlap heavily. The practical implication: search broadly across title variations, and lead with skill keywords (vLLM, agent orchestration, LLM evaluation, on-prem deployment) rather than exact title matches.

Source: [Ivan Turkovic AI Job Titles 2026](https://www.ivanturkovic.com/2026/04/24/ai-job-titles-2026-naming-chaos/)

---

## 3. Pipeline 029 Overlap Analysis

Pipeline 029 targets "AI harness roles" — the overlap with on-prem LLM skills is substantial:

| Pipeline 029 Target | On-Prem LLM Skill Overlap | Resume Enhancement |
|---------------------|--------------------------|-------------------|
| OpenAI Agent Infrastructure (10/10) | Agent governance, orchestration, eval | Add: model-agnostic agent execution (open-weight models via vLLM) |
| Google Agents Infrastructure (10/10) | Agent lifecycle management, testing | Add: private deployment of agent systems on-prem |
| Cohere Applied AI Engineer (9/10) | Applied AI, model integration | Add: self-hosted model serving, quantization for deployment |
| Other AI infra roles | Platform engineering, DevOps for AI | Add: GPU infrastructure basics, Docker for ML, vLLM serving |

The on-prem LLM skills don't replace the agent-harness positioning — they extend it. The resume story becomes: "I build and govern agent systems, AND I can deploy them on private infrastructure where your data never leaves your network." This is a strictly stronger position in the job market, especially for regulated-industry employers.

---

## 4. Portfolio Projects (Reusing Isagawa Assets)

### Project 1: Kernel + Ollama Local Agent Loop

**What:** Run the Isagawa Kernel's full enforcement loop (session-start → anchor → work → learn → complete) against a local open-weight model via Ollama instead of Claude. Demonstrate that the governance framework is model-agnostic by executing a multi-task backlog through the cycling protocol using DeepSeek V4 or Llama 4 running locally.

**Isagawa assets reused:**
- Isagawa Kernel (MIT) — the entire governance framework
- Existing backlogs — replay a known-good backlog through the loop with a local model
- run-task.sh cycling infrastructure — proves autonomous execution works on local models

**What it demonstrates:**
- Agent governance on private infrastructure (no cloud API dependency)
- Model-agnostic design (same governance, different LLM backend)
- Production-grade agent orchestration (enforcement hooks, self-improvement, autonomous cycling)

**Hardware assumption:** Single consumer GPU (RTX 3060 12GB or better) running Ollama with a 7-8B model (Llama 4 Scout quantized, DeepSeek V4 Flash). Upgrade to 70B model with dual RTX 5090 for impressive demo.

**Publishable artifact:** GitHub repo with adapter code + blog post / README documenting the process and benchmark results (task completion rate, quality comparison vs Claude). This directly addresses the #1 gap from 03-isagawa-pivot-analysis (model-agnostic inference adapter).

**Effort:** 2-3 weeks (adapter code + one backlog replay + writeup)

---

### Project 2: Self-Hosted LLM Eval Pipeline

**What:** Deploy a self-hosted evaluation pipeline that tests open-weight models against the Isagawa QA platform's gate contract pattern. Use the existing DeepEval integration to run systematic evaluations (hallucination detection, coherence scoring, A/B comparison) on locally-served models via vLLM, with results orchestrated through the Kernel pipeline.

**Isagawa assets reused:**
- DeepEval integration (platform-deepeval) — custom metrics, LLM-as-judge pattern
- Gate contract pattern — acceptance criteria framework from Kernel
- Execute-pipeline skill — orchestrates eval runs through the Kernel loop
- QA platform architecture — role-based, interface-driven testing pattern

**What it demonstrates:**
- Self-hosted model evaluation (no cloud eval platform dependency)
- Systematic QA methodology applied to LLMs (not just ad-hoc prompting)
- Production pipeline orchestration for model testing
- Regression detection across model versions/quantization levels

**Hardware assumption:** Consumer GPU for inference (RTX 3060+ for 7-8B models via vLLM). LLM-as-judge can use either local model or API fallback. Full pipeline runs on a single workstation.

**Publishable artifact:** GitHub repo with eval pipeline + report showing model comparison results (e.g., DeepSeek V4 Flash Q4 vs Q8 vs full-precision on a standard eval suite). Blog post: "pytest for LLMs: Self-Hosted Model Evaluation with Gate Contracts."

**Effort:** 3-4 weeks (vLLM setup + eval template extraction + pipeline integration + writeup)

---

### Project 3 (Bonus): Healthcare LLM Compliance Validator

**What:** Build a compliance validation tool that checks whether a locally-deployed LLM meets HIPAA requirements for healthcare use — audit trail generation, data handling verification, PHI detection in prompts/responses, access control validation. Uses the Kernel's enforcement hooks to ensure compliance gates are met before any model interaction processes patient data.

**Isagawa assets reused:**
- Kernel enforcement hooks — gate compliance checks
- Healthcare domain knowledge (HMSA background)
- QA platform validation patterns

**What it demonstrates:**
- HIPAA-compliant AI deployment expertise
- Regulatory compliance automation (AI-specific)
- Healthcare + AI intersection (rare combination)

**Hardware assumption:** Any machine that can run a local model. Compliance validation is lightweight — the heavy lift is the model inference, not the compliance checking.

**Effort:** 4-6 weeks (compliance framework design + hook implementation + validation suite)

**Note:** This project is the bridge between the personal skill path and the Isagawa business pivot (Candidate C from 03-isagawa-pivot-analysis). Building it for the portfolio simultaneously builds the consulting offering.

---

## 5. 30-60-90 Day Plan

### Hardware Assumptions

**Current machine (assumed):** Consumer desktop/laptop. Specific GPU unknown — plan is written for two scenarios:

| Scenario | Hardware | What's Feasible |
|----------|----------|----------------|
| **No discrete GPU** | CPU-only or integrated graphics | Ollama with 1-3B models (Phi-3, TinyLlama). Can learn concepts, can't do serious serving/fine-tuning |
| **Consumer GPU (8-24GB VRAM)** | RTX 3060 12GB, RTX 4070 Ti 16GB, RTX 4090 24GB | Ollama/vLLM with 7-8B models. QLoRA fine-tuning of 7-8B models. Quantized 70B models (Q4) on 24GB. Enough for all portfolio projects |

**Cloud GPU rental** (when needed): RunPod, Lambda Labs, or Vast.ai — $0.50-$2.00/hr for A100 40GB. Budget $50-100/month for Phase 2 fine-tuning experiments.

---

### Phase 1: Days 1-30 — Local Model Serving & Agent Adapter

**Goal:** Get hands dirty with local model serving. Build Portfolio Project 1 (Kernel + Ollama). Establish the "model-agnostic agent governance" credential.

**Week 1: Local Model Fundamentals**
- [ ] Install Ollama, pull 2-3 models (DeepSeek V4 Flash, Llama 4 Scout 8B, Qwen3-8B)
- [ ] Run each model, compare outputs on a standard prompt set (10 prompts covering reasoning, coding, instruction following)
- [ ] Install vLLM (requires NVIDIA GPU + CUDA). Serve the same models via vLLM's OpenAI-compatible API
- [ ] Compare: Ollama (single-user, simple) vs vLLM (multi-user, production). Note throughput, latency, VRAM usage differences
- [ ] Read: [Red Hat vLLM vs Ollama](https://www.redhat.com/en/topics/ai/vllm-vs-ollama), [Spheron Ollama vs vLLM](https://www.spheron.network/blog/ollama-vs-vllm/)

**Week 2: Kernel Model-Agnostic Adapter**
- [ ] Design the adapter interface: replace `claude -p` calls with configurable backend (Ollama API, vLLM OpenAI-compatible API, direct HTTP)
- [ ] Implement adapter for Ollama (simplest — REST API, localhost)
- [ ] Test: run a simple 3-task backlog through the Kernel loop using Ollama backend
- [ ] Document: what works, what breaks, where open-weight models struggle vs Claude (instruction following, tool use, long context)

**Week 3: Full Cycling Test**
- [ ] Run a real backlog (pick a completed research backlog) through Kernel cycling with Ollama backend
- [ ] Track: task completion rate, anchor compliance, quality of outputs
- [ ] Implement adapter for vLLM (OpenAI-compatible API — should be drop-in if Ollama adapter uses OpenAI format)
- [ ] Compare: same backlog, Ollama vs vLLM vs Claude. Document results

**Week 4: Publish & Apply**
- [ ] Write up results as a GitHub README + blog post: "Running the Isagawa Kernel on Local Models"
- [ ] Push adapter code to isagawa-kernel repo (or separate repo)
- [ ] Update resume: add "Model-Agnostic Agent Governance — deployed Kernel enforcement loop on local open-weight models (DeepSeek V4, Llama 4) via vLLM and Ollama"
- [ ] Start applying to AI Platform Engineer / LLMOps Engineer roles with updated portfolio

**Phase 1 Deliverables:**
- Working Kernel adapter for Ollama and vLLM
- Benchmark comparison (local model vs Claude on Kernel tasks)
- Published blog post / GitHub repo
- Updated resume with on-prem LLM skills

---

### Phase 2: Days 31-60 — Quantization, Fine-Tuning & Eval Pipeline

**Goal:** Learn the model optimization stack (quantization, LoRA). Build Portfolio Project 2 (Self-Hosted Eval Pipeline). Move from "I can serve models" to "I can optimize and evaluate them."

**Week 5: Quantization Hands-On**
- [ ] Learn GGUF format: download a model in multiple quantization levels (Q4_K_M, Q5_K_M, Q8_0, F16) from HuggingFace
- [ ] Run same eval prompts across quantization levels. Measure: quality delta, VRAM usage, tokens/second
- [ ] Learn AWQ: install AutoAWQ, quantize a 7B model. Compare AWQ vs GGUF on same hardware
- [ ] Read: [Digital Applied GGUF vs AWQ vs GPTQ 2026](https://www.digitalapplied.com/blog/gguf-vs-awq-vs-gptq-vs-mlx-llm-quantization-formats-2026), [TensorRigs Quantization Guide](https://tensorrigs.com/blog/llm-quantization-guide/)

**Week 6: LoRA Fine-Tuning**
- [ ] Install Unsloth (simplest LoRA/QLoRA framework)
- [ ] Fine-tune a 7B model on a small domain-specific dataset (e.g., 500 examples of Kernel-style task decomposition, or healthcare charting templates)
- [ ] Evaluate fine-tuned model vs base model using DeepEval metrics
- [ ] Read: [Meta Intelligence LoRA/QLoRA Guide 2026](https://www.meta-intelligence.tech/en/insight-lora-finetuning), [Spheron Fine-Tune LLMs 2026](https://www.spheron.network/blog/how-to-fine-tune-llm-2026/)

**Week 7-8: Self-Hosted Eval Pipeline (Portfolio Project 2)**
- [ ] Extract DeepEval eval patterns from platform-deepeval into standalone pipeline
- [ ] Create eval templates: coding accuracy, instruction following, domain correctness, hallucination rate
- [ ] Wire eval pipeline through Kernel's execute-pipeline (eval run = backlog → tasks → results)
- [ ] Run: evaluate 3+ models at multiple quantization levels. Produce comparison report
- [ ] Publish: GitHub repo + blog post "Self-Hosted LLM Evaluation with Gate Contracts"

**Phase 2 Deliverables:**
- Hands-on quantization experience (GGUF, AWQ) with benchmark data
- Completed LoRA fine-tuning of a domain-specific model
- Self-hosted eval pipeline (Portfolio Project 2) published
- Updated resume: add quantization, fine-tuning, LLM evaluation skills

---

### Phase 3: Days 61-90 — Production Deployment & Healthcare Specialization

**Goal:** Move from experiments to production-grade deployment patterns. Build the healthcare compliance credential. Position for senior AI Platform Engineer / AI Infrastructure Engineer roles.

**Week 9: Production Serving Patterns**
- [ ] Deploy vLLM behind a load balancer (nginx or Traefik) — simulate multi-user production serving
- [ ] Implement basic observability: request logging, latency tracking, token counting, error rates
- [ ] Learn NVIDIA NIM: deploy a model via NIM container (free dev tier, up to 16 GPUs). Compare NIM vs raw vLLM
- [ ] Container packaging: create a Dockerfile that bundles model + vLLM + monitoring into a deployable unit

**Week 10: Private RAG System**
- [ ] Deploy a vector database (Qdrant or Chroma — both self-hosted, open-source)
- [ ] Build a RAG pipeline: document ingestion → embedding → vector store → retrieval → LLM generation
- [ ] Use the Kernel to orchestrate the RAG pipeline (ingest = task, retrieve+generate = task, evaluate = task)
- [ ] Test with a realistic dataset (healthcare documentation, or Kernel's own docs as the corpus)

**Week 11: Healthcare Compliance (Portfolio Project 3)**
- [ ] Design HIPAA compliance checklist for on-prem LLM deployments (audit trail, PHI detection, access control)
- [ ] Implement basic compliance hooks in the Kernel (pre-inference PHI scan, post-inference audit log, access control gate)
- [ ] Connect to RT automation project context — the compliance validator IS the infrastructure for the consulting offering
- [ ] Draft reference architecture document: "HIPAA-Compliant On-Prem LLM Deployment with Kernel Governance"

**Week 12: Consolidate & Target Senior Roles**
- [ ] Update resume with full on-prem LLM stack: serving (vLLM, Ollama, NIM), optimization (GGUF, AWQ, LoRA), evaluation (DeepEval pipeline), RAG (vector DB + retrieval), compliance (HIPAA), governance (Kernel)
- [ ] Publish consolidated portfolio page: all 3 projects with links, blog posts, benchmark data
- [ ] Target senior roles: AI Platform Engineer ($180K-$310K), Production LLM Infrastructure Engineer ($200K-$320K), AI Solutions Architect ($160K-$280K)
- [ ] Leverage healthcare specialization for regulated-industry roles (healthcare, finance, defense)

**Phase 3 Deliverables:**
- Production-grade model serving deployment (vLLM + load balancer + monitoring)
- Working private RAG system
- Healthcare compliance validator (Portfolio Project 3)
- Reference architecture document
- Fully updated resume and portfolio targeting senior AI infra roles

---

## 6. Learning Resources (Curated)

| Topic | Resource | Format |
|-------|----------|--------|
| vLLM | [vLLM Documentation](https://docs.vllm.ai/) | Docs |
| Ollama | [Ollama GitHub](https://github.com/ollama/ollama) | Docs |
| Quantization | [Digital Applied GGUF vs AWQ vs GPTQ 2026](https://www.digitalapplied.com/blog/gguf-vs-awq-vs-gptq-vs-mlx-llm-quantization-formats-2026) | Blog |
| LoRA/QLoRA | [Meta Intelligence LoRA Guide 2026](https://www.meta-intelligence.tech/en/insight-lora-finetuning) | Guide |
| Fine-tuning | [Spheron Fine-Tune LLMs 2026](https://www.spheron.network/blog/how-to-fine-tune-llm-2026/) | Guide |
| AI Platform Engineer path | [JobsByCulture Career Path 2026](https://jobsbyculture.com/blog/ai-platform-engineer-career-path-2026) | Career guide |
| LLM Engineer roadmap | [KDnuggets LLM Engineer Roadmap 2026](https://www.kdnuggets.com/the-roadmap-to-becoming-an-llm-engineer-in-2026) | Roadmap |
| AI skills in demand | [Futurense AI Skills 2026](https://futurense.com/blog/ai-skills-in-demand) | Market report |
| Job title landscape | [Ivan Turkovic AI Job Titles 2026](https://www.ivanturkovic.com/2026/04/24/ai-job-titles-2026-naming-chaos/) | Analysis |

---

## Sources

- [KORE1: How to Hire LLM Engineers 2026](https://www.kore1.com/hire-llm-engineers-2026/)
- [Acceler8 Talent: In-Demand ML Roles 2026](https://www.acceler8talent.com/resources/blog/the-most-in-demand-machine-learning-roles-in-2026--managing-the-ai-talent-frontier/)
- [JobsByCulture: AI Platform Engineer Career Path 2026](https://jobsbyculture.com/blog/ai-platform-engineer-career-path-2026)
- [Ivan Turkovic: AI Job Titles 2026](https://www.ivanturkovic.com/2026/04/24/ai-job-titles-2026-naming-chaos/)
- [MLOps vs LLMOps UK 2026](https://machinelearningjobs.co.uk/career-advice/mlops-vs-llmops-engineer-uk-2026)
- [Futurense: AI Skills in Demand 2026](https://futurense.com/blog/ai-skills-in-demand)
- [KDnuggets: LLM Engineer Roadmap 2026](https://www.kdnuggets.com/the-roadmap-to-becoming-an-llm-engineer-in-2026)
- [ZipRecruiter: LLM Engineer Jobs](https://www.ziprecruiter.com/Jobs/Llm-Engineer)
- [ZipRecruiter: vLLM Jobs](https://www.ziprecruiter.com/Jobs/Vllm)
- [Red Hat: vLLM vs Ollama](https://www.redhat.com/en/topics/ai/vllm-vs-ollama)
- [Spheron: Ollama vs vLLM](https://www.spheron.network/blog/ollama-vs-vllm/)
- [Digital Applied: GGUF vs AWQ vs GPTQ vs MLX 2026](https://www.digitalapplied.com/blog/gguf-vs-awq-vs-gptq-vs-mlx-llm-quantization-formats-2026)
- [Meta Intelligence: LoRA/QLoRA Fine-Tuning Guide 2026](https://www.meta-intelligence.tech/en/insight-lora-finetuning)
- [Spheron: Fine-Tune LLMs 2026](https://www.spheron.network/blog/how-to-fine-tune-llm-2026/)
- [TensorRigs: LLM Quantization Guide](https://tensorrigs.com/blog/llm-quantization-guide/)
- [TechnoVids: AI Engineer Skills 2026](https://technovids.com/ai-engineer-skills)
- [AY Automate: AI Engineer Skills 2026](https://www.ayautomate.com/blog/ai-engineer-skills-2026)

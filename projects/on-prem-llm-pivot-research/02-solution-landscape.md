# Private-LLM Solution Landscape (July 2026)

Research output for backlog 197 — task 002.

---

## Landscape Table

| Tier | Examples | Who It Fits | Cost Order-of-Magnitude | Operational Burden | Maturity |
|------|----------|-------------|------------------------|-------------------|----------|
| **A. Own Hardware On-Prem** | NVIDIA H100/H200 servers, Dell PowerEdge, HPE ProLiant Gen 12 | Regulated enterprises (finance, healthcare, defense) with sustained high-volume inference (80%+ GPU utilization), strict data sovereignty, 3+ year commitment | **$250K-$500K** upfront per 8-GPU node + **$120K+/yr** opex (power, cooling, 1.5-2 FTE). Break-even vs cloud at ~50-83% utilization over 3 years | **High** — procurement (2-8 week lead times), rack/power/cooling, OS/driver/CUDA stack, model serving, monitoring, security patching, 1.5-2 FTE MLOps | **Mature** — GPU supply constraints easing; H100 SXM secondary market $15-20K (down from $25K+ in early 2025). Dual RTX 5090s match H100 on 70B models at ~25% cost |
| **B. Private Cloud / VPC-Hosted** | AWS Bedrock (PrivateLink), Azure OpenAI (Private Endpoints), GCP Vertex AI (VPC Service Controls) | Enterprises wanting data isolation without hardware ownership; regulated industries needing FedRAMP/HIPAA; multi-model strategy | **$0.50-$15 per 1M tokens** (model-dependent) + VPC/networking costs. Provisioned throughput: $50K-$200K/yr for dedicated capacity | **Low-Medium** — provider manages GPU fleet, model updates, scaling. Customer manages VPC config, IAM, compliance controls | **Mature** — AWS Bedrock and Azure OpenAI have FedRAMP High. Vertex AI FedRAMP High in progress (not GA as of June 2026). All three support PrivateLink/private endpoints |
| **C. Open-Weight Models** | Llama 3.3/4 (Meta, custom license), Mistral Large 2 (Apache 2.0), Qwen3-Coder-480B (Apache 2.0), DeepSeek V4/V4 Pro (MIT), Kimi K2.6/K2.7 (~1T MoE), GLM-5.2 (open) | Any org wanting model control, fine-tuning, or zero vendor lock-in. Pairs with Tiers A, B, or D for deployment | **Free** (model weights). Deployment cost depends on chosen infrastructure tier. Fine-tuning: $500-$5K per run on cloud GPUs | **Varies** — model selection, evaluation, fine-tuning, prompt engineering, version management. Easier than 2024 due to standardized tooling | **Rapidly maturing** — DeepSeek V4 Pro hits 80.6% SWE-Bench Verified. Qwen3-Coder at 69.6%. GLM 5.2 beats GPT-5.5 on several long-horizon coding benchmarks. Gap with frontier APIs narrowing fast |
| **D. Inference/Serving Stacks** | vLLM, SGLang, TensorRT-LLM, llama.cpp, Ollama, NVIDIA NIM/Triton, NVIDIA Dynamo | DevOps/MLOps teams deploying open-weight models on own or cloud GPUs. Choice depends on scale and hardware | **Free** (OSS) or **$4,500/GPU/yr** (NVIDIA AI Enterprise for NIM production). NIM dev tier free up to 16 GPUs | **Medium** — production serving requires load balancing, autoscaling, monitoring, model versioning. NIM simplifies with pre-packaged containers | **Mature** — vLLM is production standard for multi-user serving. TGI archived (March 2026). TensorRT-LLM 15-30% faster than vLLM on H100s. NIM catalog expanding post-GTC 2026 |
| **E. Enterprise Platforms** | Databricks (SDS Ecosystem), Red Hat OpenShift AI + Dell Private Cloud, HPE Private Cloud, Nutanix GPT-in-a-Box | Large enterprises wanting turnkey private AI with existing vendor relationships. Orgs with on-prem data estates wanting LLMs without data movement | **$100K-$1M+/yr** depending on scale (platform licensing + infrastructure). Databricks: consumption-based. Dell/HPE: hardware + support bundles | **Low-Medium** — vendor-managed stack, integrated security, compliance tooling. Trade operational burden for vendor lock-in and higher cost | **Maturing** — Databricks SDS Ecosystem (zero-copy on-prem LLMs) announced mid-2026 with Cohesity, HPE, NetApp, Nutanix integrations. Dell+Red Hat OpenShift AI validated designs available. HPE unified VM/container management GA Q3 2026 |

---

## Tier A: Own Hardware On-Prem

### GPU Options and Cost Ranges

| GPU | VRAM | Street Price (mid-2026) | Performance Notes |
|-----|------|------------------------|-------------------|
| NVIDIA H100 SXM5 | 80 GB HBM3 | $15,000-$20,000 (secondary market) | Production standard; 2-6 week lead time |
| NVIDIA H200 | 141 GB HBM3e | $25,000-$35,000 | 1.4-1.9x H100 on large models; 4-8 week lead time |
| NVIDIA RTX 5090 | 32 GB GDDR7 | $2,000-$2,500 | Dual 5090s match H100 on 70B models at ~25% cost |
| NVIDIA A6000 Ada | 48 GB GDDR6 | $4,500-$5,500 | Good balance for smaller models and fine-tuning |

### Total Cost of Ownership (8x H100 Server)

| Component | Annual Cost |
|-----------|------------|
| Hardware amortization (3-year) | ~$80,000-$100,000 |
| Electricity (~10 kW at $0.12/kWh) | ~$10,500 |
| Cooling overhead (30-40% on power) | ~$3,500-$4,200 |
| Networking (InfiniBand) | ~$15,000-$30,000 (amortized) |
| Staffing (1.5-2 FTE fractional) | ~$36,000-$72,000 |
| Software/licensing (NVIDIA AI Enterprise) | ~$36,000 |
| **Total annual** | **~$180,000-$250,000** |

### Break-Even vs Cloud

- At **< 70% GPU utilization**: cloud wins on TCO
- At **80%+ sustained utilization over 3 years**: on-prem wins, often by 50-85% lower blended cost
- US tariffs on imported server hardware (2025-2026) add cost unpredictability
- Most production inference teams operate at 40-65% utilization due to traffic variability

---

## Tier B: Private Cloud / VPC-Hosted

### AWS Bedrock

- **Isolation**: Model runs in customer VPC via AWS PrivateLink; model providers have no access to customer accounts or logs
- **Compliance**: FedRAMP High authorized (GovCloud, May 2025); HIPAA eligible
- **Models**: Claude, Llama, Mistral, Cohere, Amazon Titan, custom fine-tuned
- **Cost**: Pay-per-token or Provisioned Throughput ($50K-$200K/yr for dedicated capacity)

### Azure OpenAI

- **Isolation**: Private Endpoints keep traffic within VNet; data processing options for zero data retention
- **Compliance**: FedRAMP High authorized; strong for Microsoft-stack enterprises
- **Models**: GPT-4o, GPT-5, o-series reasoning models, plus open-weight models via Azure AI
- **Cost**: Pay-per-token; Provisioned Throughput Units for guaranteed capacity

### GCP Vertex AI

- **Isolation**: VPC Service Controls — strongest native exfiltration defense of the three clouds
- **Compliance**: FedRAMP High in progress (not GA as of June 2026); data residency across 13+ regions
- **Models**: Gemini family, open-weight models (Llama, Mistral) via Model Garden
- **Cost**: Consumption-based; Provisioned Throughput available

### When to Choose Private Cloud

- Need data isolation but not hardware ownership
- Regulatory requirements met by cloud certifications (FedRAMP, HIPAA, SOC 2)
- Variable or growing workloads (hard to predict GPU utilization)
- Multi-model strategy (swap models without hardware changes)

---

## Tier C: Open-Weight Models

### Leading Models (July 2026)

| Model | Parameters | License | SWE-Bench Verified | Best For |
|-------|------------|---------|-------------------|----------|
| Kimi K2.6 / K2.7 | ~1T MoE (active ~32B) | Open | 71.6% (multi-attempt) | Agentic coding, tool use, 256K context |
| DeepSeek V4 Pro | MoE | MIT | 80.6% | Hard reasoning, agentic coding, long-context analysis |
| DeepSeek V4 Flash | MoE | MIT | — | High-volume chat, basic coding (34x cheaper than frontier) |
| Qwen3-Coder-480B | 480B | Apache 2.0 | 69.6% | Coding tasks, fully permissive license |
| GLM 5.2 | Large | Open | — | Long-horizon coding (beats GPT-5.5 on several benchmarks) |
| Llama 4 Maverick | 400B MoE | Custom (permissive) | — | General-purpose, Meta ecosystem |
| Mistral Large 2 | 123B | Apache 2.0 | — | European sovereignty requirements, multilingual |

### License Landscape

- **Apache 2.0** (fully permissive): Qwen3, Mistral
- **MIT** (fully permissive): DeepSeek V4
- **Custom permissive**: Meta Llama 4 (free for < 700M MAU), Kimi K2
- Key concern: DeepSeek models — MIT licensed but Chinese origin may trigger compliance review in some regulated sectors

---

## Tier D: Inference/Serving Stacks

### Framework Comparison

| Stack | Type | Throughput | Best For | Status (mid-2026) |
|-------|------|-----------|----------|-------------------|
| **vLLM** | Production server | High (187 tok/s aggregate on A100 under concurrent load) | Multi-user production serving; standard choice | **Active** — production standard |
| **SGLang** | Production server | Comparable to vLLM, faster on structured generation | Production serving with structured output needs | **Active** — rising fast |
| **TensorRT-LLM** | NVIDIA-optimized engine | 15-30% faster than vLLM on H100s; 1,000 tok/s/user on Blackwell | Maximum throughput on NVIDIA hardware | **Active** — NVIDIA flagship |
| **llama.cpp** | C++ runtime | Best single-user latency on CPU+GPU | Edge, embedded, CPU-only, Mac deployment | **Active** — broad hardware support |
| **Ollama** | Local wrapper (over llama.cpp) | Good single-user; degrades under concurrency | Developer local setup, prototyping | **Active** — simplest onramp |
| **NVIDIA NIM** | Pre-packaged containers | Optimized per-GPU (auto-selects TensorRT-LLM/vLLM/SGLang) | Enterprise production with NVIDIA support | **Active** — $4,500/GPU/yr for production; free dev tier up to 16 GPUs |
| **NVIDIA Triton** | Model serving orchestrator | Multi-model, multi-framework | Serving multiple models with routing | **Active** — pairs with TensorRT-LLM |
| **NVIDIA Dynamo** | Multi-GPU orchestrator | Splits work across GPUs | Large model distribution across GPU clusters | **Active** — new in 2026 |
| **TGI (HuggingFace)** | Production server | Was competitive | — | **Archived** (March 21, 2026). HF recommends vLLM, SGLang, llama.cpp |

### Practical Decision Tree

1. **Single developer, local**: Ollama (simplest) or llama.cpp (most flexible)
2. **Team serving, multi-user**: vLLM (standard) or SGLang (if structured output heavy)
3. **Maximum NVIDIA throughput**: TensorRT-LLM + Triton
4. **Enterprise with support contract**: NVIDIA NIM ($4,500/GPU/yr)
5. **Multi-model routing**: Triton Inference Server + any backend

---

## Tier E: Enterprise Platforms

### Databricks

- **SDS Ecosystem** (announced mid-2026): Zero-copy architecture runs Databricks Intelligence Platform directly on on-prem data estates — no data movement required
- **Partners**: Cohesity, Commvault, HPE, NetApp, Nutanix, Rubrik building native integrations (expected by end of 2026)
- **Fit**: Orgs with existing Databricks investment and large on-prem data lakes wanting to add LLM capabilities

### Dell + Red Hat OpenShift AI

- **Dell Private Cloud for Red Hat OpenShift**: Validated design for deploying LLMs with RAG on-prem
- **Fit**: Enterprises with Dell infrastructure and Red Hat expertise wanting turnkey AI stack
- **Cost**: Hardware bundle + Red Hat OpenShift subscription + Dell support

### HPE Private Cloud

- **ProLiant Gen 12**: Unified management of VMs and containers (GA Q3 2026)
- **Fit**: HPE-committed shops wanting to add AI workloads to existing private cloud
- **Cost**: Hardware + HPE GreenLake consumption-based pricing

### Nutanix GPT-in-a-Box

- **Turnkey**: Pre-configured HCI appliance with GPU, serving stack, and model catalog
- **Fit**: Mid-market enterprises wanting simplest on-prem AI path
- **Cost**: Appliance pricing (~$100K-$300K depending on GPU config)

---

## Capability Gap: Open-Weight vs Frontier APIs

### Where Open-Weight Models Are Already Good Enough (mid-2026)

- **Coding**: DeepSeek V4 Pro (80.6% SWE-Bench Verified) and Kimi K2.6 (71.6%) are competitive with top closed models on multi-turn coding tasks
- **Text classification, summarization, extraction**: Best open-weight models perform comparably to GPT-4o and Claude Sonnet
- **Structured data extraction and routing**: Smaller fine-tuned open models often outperform larger frontier models
- **Multilingual**: Qwen3 and Mistral strong in non-English languages

### Where Frontier APIs Still Lead

- **Hardest reasoning tasks**: Claude Opus 4.8 and GPT-5.5 still hold an edge on the most complex multi-step reasoning, though GLM 5.2 is closing fast
- **Long agentic workflows (50+ tool calls)**: Frontier models maintain better reliability over very long chains; open-weight models degrade more on error recovery
- **Novel/creative problem solving**: Frontier models show better generalization to unseen problem types
- **Safety/alignment tuning**: Closed model providers invest more in alignment; open models vary in safety properties
- **Multimodal (vision + code + reasoning)**: Frontier models still lead on combined multimodal-reasoning tasks

### Gap Trajectory

The gap is **closing rapidly**. In January 2025, the best open-weight model scored ~45% on SWE-Bench Verified vs ~55% for frontier. By July 2026, open-weight (DeepSeek V4 Pro at 80.6%) is essentially at parity with frontier models on coding benchmarks. For most enterprise use cases (not cutting-edge research), open-weight models deployed on private infrastructure are now a viable primary option, with frontier API access as a fallback for the hardest tasks.

### Practical Recommendation

The emerging enterprise pattern is a **hybrid portfolio**:
1. **Open-weight on private infrastructure** for high-volume, privacy-sensitive, or cost-sensitive workloads
2. **Frontier API** (via private cloud VPC endpoints) for the hardest reasoning/agentic tasks
3. **Small specialized models** for routing, classification, and extraction (runs on CPU or minimal GPU)

---

## Sources

- [Spheron: LLM Inference On-Premise vs Cloud 2026](https://www.spheron.network/blog/llm-inference-on-premise-vs-cloud/)
- [Iternal: How to Deploy LLM On-Premise 2026](https://iternal.ai/how-to-deploy-llm-on-premise)
- [AI Superior: Cost of Running Local LLM 2026](https://aisuperior.com/cost-of-running-local-llm/)
- [SitePoint: Self-Hosted LLM Costs 2026](https://www.sitepoint.com/self-hosted-llm-costs-2026/)
- [AI Superior: Open Source LLM Deployment Cost 2026](https://aisuperior.com/open-source-llm-deployment-cost/)
- [PremAI: On-Premise LLM Deployment Real Costs](https://blog.premai.io/on-premise-llm-deployment-the-real-costs-trade-offs-decision-framework/)
- [VRLA Tech: LLM Inference On-Premise vs Cloud 2026](https://vrlatech.com/llm-inference-on-premise-vs-cloud-cost-2026/)
- [Hivenet: vLLM vs TGI vs TensorRT-LLM vs Ollama](https://www.hivenet.com/post/vllm-vs-tgi-vs-tensorrt-llm-vs-ollama)
- [VRLA Tech: LLM Inference Engine Comparison 2026](https://vrlatech.com/llm-inference-engine-comparison-2026/)
- [n1n.ai: Comprehensive LLM Inference Engine Comparison](https://explore.n1n.ai/blog/llm-inference-engine-comparison-vllm-tgi-tensorrt-sglang-2026-03-13)
- [BIZON: Best LLM Inference Engines 2026](https://bizon-tech.com/blog/best-llm-inference-engines)
- [Spheron: vLLM vs TensorRT-LLM vs SGLang H100 Benchmarks](https://www.spheron.network/blog/vllm-vs-tensorrt-llm-vs-sglang-benchmarks/)
- [Dev.to: AWS Bedrock vs Azure OpenAI vs Vertex AI 2026](https://dev.to/ciroveldran/aws-bedrock-vs-azure-openai-vs-vertex-ai-2026-enterprise-comparison-4no5)
- [Internative: Vertex vs Bedrock vs Foundry 2026](https://internative.net/insights/blog/enterprise-ai-platform-comparison-vertex-bedrock-foundry-2026)
- [HuggingFace: Best Open-Source LLM Models 2026](https://huggingface.co/blog/daya-shankar/open-source-llms)
- [AceCloud: Best Open Source LLMs 2026](https://acecloud.ai/blog/best-open-source-llms/)
- [Kingy AI: Best Open-Weight AI Models 2026](https://kingy.ai/news/best-open-weight-ai-models-in-2026-glm-5-2-vs-deepseek-v4-vs-kimi-k2-6-vs-qwen-vs-mistral/)
- [MindStudio: Open-Weight Models Enterprise Automation](https://www.mindstudio.ai/blog/open-weight-ai-models-enterprise-automation)
- [IntuitionLabs: On-Prem AI Infrastructure Comparison](https://intuitionlabs.ai/articles/on-prem-ai-infrastructure-comparison)
- [Databricks: Security and Compliance at Data+AI Summit 2026](https://www.databricks.com/blog/whats-new-databricks-platform-security-and-compliance-data-ai-summit-2026)
- [HPE: Unified Private Clouds May 2026](https://www.hpe.com/us/en/newsroom/press-release/2026/05/hpe-delivers-unified-private-clouds-and-data-platforms-to-accelerate-enterprise-modernization-and-ai-data-readiness.html)
- [Spheron: NVIDIA NIM Self-Host Deployment Guide](https://www.spheron.network/blog/nvidia-nim-self-host-deployment-guide/)
- [CostBench: NVIDIA NIM Pricing 2026](https://costbench.com/software/llm-api-providers/nvidia-nim/)
- [Lenovo: On-Premise vs Cloud GenAI TCO 2026](https://lenovopress.lenovo.com/lp2368.pdf)
- [SixFive Media: On-Premise AI Enterprise Strategy 2026](https://www.sixfivemedia.com/blog/on-premise-ai-for-enterprise-strategy-costs-and-vendor-selection-in-2026)

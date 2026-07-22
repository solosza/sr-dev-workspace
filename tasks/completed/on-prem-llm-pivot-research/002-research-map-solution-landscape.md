# Map the Private-LLM Solution Landscape

## Context
If enterprises want LLMs without sharing IP, several solution shapes compete: own-GPU on-prem, private cloud/VPC, open-weight models, managed private platforms. Mapping this landscape grounds both the Isagawa pivot options (003) and the personal skill list (004). Produces `projects/on-prem-llm-pivot-research/02-solution-landscape.md`.

## Type
RESEARCH

## Execution
inline

## Dependencies
- None

## Requirements
- Web research with sources
- Map solution tiers: (a) own hardware on-prem (GPU options, cost ranges for realistic enterprise setups), (b) private cloud / VPC-hosted (AWS Bedrock private, Azure OpenAI private endpoints, GCP), (c) open-weight models and their licenses (Llama, Mistral, Qwen, DeepSeek, gpt-oss, etc.), (d) inference/serving stacks (vLLM, TGI, Ollama, llama.cpp, NVIDIA NIM/Triton), (e) enterprise platforms bundling this (Databricks, Red Hat, Dell/HPE offerings)
- For each tier: who it fits, cost order-of-magnitude, operational burden, maturity
- Capability-gap honesty: how far open-weight models lag frontier APIs for agentic/coding work, and where they're already good enough
- Write `projects/on-prem-llm-pivot-research/02-solution-landscape.md` with a landscape table + per-tier notes

## Acceptance Criteria
- [ ] `projects/on-prem-llm-pivot-research/02-solution-landscape.md` exists
- [ ] Covers ≥ 3 serving stacks by name (vLLM/Ollama/llama.cpp/TGI/NIM)
- [ ] Each tier has cost order-of-magnitude and fit notes
- [ ] Capability-gap section present

## Gates Satisfied
- RSCH-03, RSCH-04

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.

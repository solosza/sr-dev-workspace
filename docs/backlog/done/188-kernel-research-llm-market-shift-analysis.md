# LLM Market Shift Analysis — Frontier vs Chinese vs On-Prem

## Status
Open

## Priority
Medium — strategic positioning decision; informs kernel architecture and eval harness direction

## Summary
Research whether enterprises are moving away from frontier LLMs (OpenAI, Anthropic, Google) toward Chinese LLMs (DeepSeek, Qwen) or on-prem/open-weight models (Llama, Mistral). Determine if code generation quality has reached parity, what's driving the shift (cost, latency, data sovereignty), and what Isagawa should do — support multi-model backends, benchmark across providers in eval harness, or double down on frontier.

## Requirements
- Enterprise adoption trends: frontier vs Chinese LLMs vs on-prem (2025-2026 data)
- Code generation quality parity claims — DeepSeek Coder, Qwen Coder vs GPT-4/Claude/Gemini benchmarks
- On-prem/self-hosted momentum — Llama 3/4, Mistral, Phi adoption in enterprise
- Cost/latency/sovereignty drivers — why companies switch
- Strategic implications for Isagawa:
  - Should the kernel support multi-model backends (model router already exists — backlog 087/091)?
  - Should eval harness benchmark across providers?
  - Positioning recommendations — where does Isagawa win regardless of model choice?

## References
- Backlog 087 (done): multi-model routing research
- Backlog 091 (done): sync model router to workspaces
- DeepSeek Coder V2/V3, Qwen 2.5 Coder benchmarks
- Llama 3.1/4, Mistral Large adoption reports

## Task Builder Input
- **Deliverable:** Research report with market analysis, benchmark comparison, and Isagawa strategy recommendations
- **Location:** subproject:llm-market-shift-research
- **Scope:** RESEARCH
- **Constraints:** Use web search for current data (2025-2026), cross-reference multiple sources, include concrete benchmark numbers where available

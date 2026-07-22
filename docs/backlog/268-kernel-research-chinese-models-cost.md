# Research: Chinese Models (GLM, Kimi, et al.) for Pipeline Cost Savings

## Status
Open

## Priority
Medium-High — directly follows the router work (262 fix + config bump); pipeline execution cost is a live concern (owner switched to credits). A cheaper capable model on run-task.sh tasks could cut cost materially.

## Summary
Evaluate whether top Chinese open/hosted models (GLM, Kimi, and other leaders) should be used as cheaper execution tiers for the owner's work — especially the kernel's autonomous `run-task.sh` / execute-pipeline batches, where most tasks are bounded build/test/research. Two parts: (1) a capability + cost comparison of the leading Chinese models against Claude (Opus 4.8 / Sonnet 5 / Haiku 4.5), and (2) a concrete "how to wire them into Claude Code" guide, since the owner has done this before with an older GLM model.

## Requirements
- **Model landscape:** cover the models the owner named — **GLM** (Zhipu, e.g. GLM-4.6 / GLM-4.5 family) and **Kimi** (Moonshot, e.g. Kimi K2) — plus the other current top Chinese models: **DeepSeek** (V3 / R1), **Qwen** (Alibaba, Qwen 2.5 / 3 / Coder), **MiniMax**, **Doubao** (ByteDance), **Yi** (01.AI), and any newer leaders as of the research date. For each: provider, latest model, open-weight vs API-only, context window.
- **Scores vs Claude:** tabulate benchmark scores against Claude Opus 4.8 / Sonnet 5 / Haiku 4.5 — coding/agentic benchmarks are the priority (SWE-bench Verified, LiveCodeBench, Aider polyglot, Terminal-Bench, tool-use/agentic evals) plus general reasoning (MMLU-Pro, GPQA). Use the LATEST published numbers, cited with source + date; distinguish self-reported from independent (e.g. Artificial Analysis, LMArena, third-party leaderboards).
- **Cost comparison:** input/output $/1M tokens for each model (API pricing) side-by-side with Claude tiers; and open-weight self-host option where relevant. Compute a rough "cost per typical run-task.sh task" delta.
- **Claude Code integration (the how-to):** research and document how to point Claude Code / the `claude -p` runner at these models — via `ANTHROPIC_BASE_URL` + an Anthropic-compatible endpoint, provider proxies (OpenRouter, or GLM/Moonshot's own Anthropic-compatible APIs), or a local gateway (LiteLLM/one-api). The owner did this before with an older GLM model — capture the exact working pattern and any gotchas (tool-use fidelity, streaming, `--model` naming, auth). Note how this would slot into `lib/model-routing-config.json` / `lib/model-router.sh` as an added tier.
- **Fitness for OUR workload specifically:** the kernel tasks are contract-driven build/test/research with strict gate validation. Assess whether a cheaper model can pass the gates (agentic tool-use + instruction-following are the binding constraints, not raw reasoning). Recommend which task tiers (haiku-equivalent scaffolding? sonnet-equivalent builds?) are safe to route to a Chinese model vs. which should stay on Claude.
- **Recommendation:** a clear go/no-go per use case (interactive orchestration vs. fleet execution), a proposed router-config change if go, and the risks (data/IP considerations of sending code to a Chinese-hosted API, reliability, gate pass-rate).

## References
- Owner prior art: previously configured Claude Code with an older GLM model (capture that setup)
- Sibling: `lib/model-routing-config.json`, `lib/model-router.sh` (the tier config the router work just updated), backlog 262 (runner/routing hardening)
- Benchmark aggregators: Artificial Analysis, LMArena, SWE-bench leaderboard, Aider LLM leaderboard (verify live during research)

## Task Builder Input
- **Deliverable:** Research report in `projects/chinese-models-cost/` — model comparison table (scores + pricing vs Claude), a Claude Code integration how-to, a workload-fitness assessment, and a go/no-go recommendation with a proposed router-config change
- **Location:** subproject:chinese-models-cost
- **Scope:** RESEARCH
- **Constraints:** Web research required (pricing + benchmarks change fast — cite source + date, flag self-reported vs independent). Include the IP/data-residency consideration of routing proprietary code (kernel, QA platform) through a Chinese-hosted API — this is a real decision factor, not just cost. No config changes in this backlog; produce the recommendation + proposed diff for a separate BUILD backlog if go.

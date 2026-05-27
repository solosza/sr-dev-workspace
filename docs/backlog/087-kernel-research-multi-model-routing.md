# Intelligent Model Routing for Kernel Task Execution

## Status
Open

## Priority
Medium — cost optimization and scale unlock, not blocking current work

## Summary
Refactor run-task.sh to select the best Claude model per task automatically. Since each task is its own isolated session (`claude -p` one-shot), model selection is trivially feasible — just pass `--model` per invocation. The router analyzes task metadata (type, precision needs, complexity) and picks Opus for architecture/precision work, Sonnet for standard builds, Haiku for scaffolding/formatting/simple writes. Stays entirely within Claude's ecosystem — no external model integration needed, no governance gaps.

## Key Insight
External models (Kimi K2.6, Cloudflare) were considered but rejected. Claude Haiku at $0.80/M input is nearly the same price as Kimi ($0.60/M) while preserving: same CLI, same tool format, same hook enforcement, same governance. No new integration, no provider management, no governance gaps from agents running outside the kernel.

## Requirements
- Add `--model` flag to run-task.sh (pass through to `claude -p --model`)
- Build routing logic that reads task metadata and selects model:
  - Task type (BUILD, TEST, RESEARCH) as primary signal
  - Task complexity markers (file count, dependencies, precision keywords)
  - Explicit override in task frontmatter (optional)
- Define model tiers within Claude family:
  - **Opus** — architecture decisions, complex code, production precision, multi-file coordination
  - **Sonnet** — standard builds, test writing, research synthesis, moderate complexity
  - **Haiku** — file scaffolding, data formatting, simple edits, copy tasks, structural gates
- Implement routing config (e.g., `lib/model-router.sh` or task frontmatter field)
- Measure cost reduction: estimate savings from routing 40-60% of tasks to Haiku/Sonnet
- Ensure gate contracts still enforce quality regardless of model (gates are model-agnostic)
- Fallback: if a task fails on a cheaper model, retry on the next tier up

## Architecture

```
run-task.sh receives task file
  → reads task metadata (type, complexity, explicit model override)
  → model-router decides: opus | sonnet | haiku
  → spawns: claude -p --model [selected] < task_prompt
  → gate contract validates output (model-agnostic)
  → if gate fails + model was not opus → retry with next tier
```

Each task = own session. No state leaks between models. Governance (hooks, gates, attestation) stays intact because it's all still `claude -p` under the kernel.

## References
- Current kernel: run-task.sh spawns `claude -p` one-shot agents
- Claude model IDs: claude-opus-4-6, claude-sonnet-4-6, claude-haiku-4-5-20251001
- Backlog 045: agent swarms research (context on why external models were deprioritized)
- Kimi K2.6 comparison: $0.60/M input, 300 sub-agents — but no governance integration

## Task Builder Input
- **Deliverable:** Working model router in run-task.sh + routing config + cost analysis report
- **Location:** workspace:lib/
- **Scope:** BUILD
- **Constraints:** Must not break existing task execution. Gate contracts remain model-agnostic enforcers. Opus stays default for any task without clear routing signal. Rollout can be opt-in via flag initially.

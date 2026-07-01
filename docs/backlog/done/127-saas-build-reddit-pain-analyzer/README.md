# Backlog 127 — Reddit Pain Analyzer Harness

**Status:** Refactored for harness design pattern (2026-06-13)

This backlog has been restructured to build Reddit Pain Analyzer as a **harness** using loop-based orchestration, not as a traditional SaaS app.

## What Changed

**Before:** Frontend (Next.js) + Backend (FastAPI) + Database + Workers
**After:** Harness (commands + skills + gate contracts + state)

## Design Documents (Harness Pattern)

| Document | Purpose |
|----------|---------|
| `product-spec.md` | What the harness does (user flows, outcomes) |
| `harness-architecture.md` | Outer loop → inner loops → gate contracts |
| `reddit-data-pipeline.md` | Skill: fetch Reddit posts, extract text |
| `ai-analysis-engine.md` | Skill: LLM analysis (pain points, ideas, scores) |
| `results-processor.md` | Skill: validate, store, export JSON + MD |
| `gate-contracts.md` | Data contracts between phases |
| `commands-design.md` | Entry points (analyze, status, export) |
| `references-design.md` | Soft constraints (protocol, philosophy) |
| `hooks-design.md` | Hard constraints (mechanical enforcement) |
| `deliverables-design.md` | Output format (JSON + Markdown) |

## Key Pattern Elements

✅ **Outer loop:** `/reddit-pain/analyze [subreddit-url]`
✅ **Inner loops:** Three skills (reddit-data-pipeline, ai-analysis-engine, results-processor)
✅ **Gate contracts:** Validation at each phase boundary
✅ **Soft gates:** Protocol + lessons guide behavior
✅ **Hard gates:** Hooks enforce rules mechanically
✅ **State-driven:** All behavior from state files, no code branching
✅ **Autonomous:** No human pauses during execution
✅ **Deliverables:** results.json + results.md (same source)

## File Structure

```
reddit-pain-analyzer-harness/
├── .claude/
│   ├── commands/reddit-pain/
│   │   ├── analyze.md
│   │   ├── status.md
│   │   └── export.md
│   ├── skills/
│   │   ├── reddit-data-pipeline/SKILL.md + references/
│   │   ├── ai-analysis-engine/SKILL.md + references/
│   │   └── results-processor/SKILL.md + references/
│   ├── references/ (soft constraints)
│   ├── protocols/reddit-pain-analyzer-protocol.md
│   ├── hooks/ (hard constraints)
│   └── state/ (session + workflow)
├── lib/ (Python utility libraries)
│   ├── reddit_client.py (PRAW wrapper)
│   ├── llm_client.py (OpenAI wrapper)
│   └── state_manager.py (state file CRUD)
└── docs/ (harness design docs)
```

## Next Step

Read `harness-architecture.md` to see how the outer/inner loops are orchestrated.

# Pipeline

## Status
NEW

## Overview
How the portfolio site build executes through the execute pipeline. Four phases, each broken into atomic tasks that run linearly via `run-task.sh`. Each spawned agent inherits Playwright MCP from `.mcp.json`.

## Execution Flow

```
/kernel/execute-pipeline 041
       |
       v
task-builder decomposes → 70 atomic tasks
       |
       v
run-task.sh spawns each task as `claude -p`
       |
       v
Phase 1: CLONE (tasks 001-020)
  ├── Navigate to Suero → screenshot → extract sections
  ├── Navigate to Shader → screenshot → extract styles
  └── Each extraction = 1 atomic task with Playwright MCP
       |
       v
Phase 2: MERGE (tasks 021-030)
  ├── Read extractions → populate design tokens
  ├── Write CSS variables (colors, typography, spacing)
  └── Write component tokens (buttons, cards, badges)
       |
       v
Phase 3: BUILD (tasks 031-060)
  ├── Create output directory structure
  ├── Write HTML skeleton + nav
  ├── Build each section (1 task per section)
  ├── Write styles.css with all tokens applied
  └── Integrate content from content-spec + catalog-data
       |
       v
Phase 4: POLISH (tasks 061-070)
  ├── Add responsive breakpoints
  ├── Visual QA via Playwright (screenshot + verify)
  └── Final validation
```

## Key Pipeline Constraints

| Constraint | Detail |
|-----------|--------|
| Execution mode | Linear (sequential via run-task.sh, NOT swarm) |
| MCP inheritance | Spawned agents get Playwright MCP from `.mcp.json` |
| Timeout | May need 600s for extraction tasks (default 300s) |
| Output location | `D:\my_ai_projects\isagawa-portfolio-site` |
| One-shot mode | Each spawned agent runs with `one_shot: true` (skips anchor) |

## Phase Dependencies

```
Phase 1 (CLONE) → Phase 2 (MERGE) → Phase 3 (BUILD) → Phase 4 (POLISH)
     |                   |                  |
     |                   |                  └── Depends on design tokens + content spec
     |                   └── Depends on extracted CSS values from both donors
     └── Independent (Suero and Shader extraction can interleave)
```

## Task Atomicity Rules

- Each Playwright navigation = its own task (navigate, screenshot, extract)
- Each section HTML = its own task
- Each CSS concern = its own task (variables, layout, components, responsive)
- No task should take more than 2-3 minutes
- Each task writes to a specific file or set of files — no overlapping writes

## Error Handling

- If a donor site is down, extraction tasks fail gracefully with error report
- Build tasks use extracted data from prior tasks — if extraction is incomplete, build proceeds with available data
- Visual QA tasks take screenshots for manual review — they don't block completion

## Dependencies
- Requires Playwright MCP configured in `.mcp.json`
- Requires website cloner skill for extraction task patterns
- Content comes from `content-spec.md` and `catalog-data.md` sub-documents
- Design tokens come from `design-tokens.md` sub-document

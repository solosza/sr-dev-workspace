# Research: Skill-as-App Architecture vs Traditional App Building

## Status
Open

## Priority
Medium — architectural research that could change how all future apps are built

## Summary
When the kernel builds an app (portfolio site, fraud detector, etc.), it currently decomposes into atomic tasks that each tell a spawned agent what to write. The agent is a code generator following instructions — but there's no reusable generation skill. Each task reinvents the "read context → produce code → verify" pattern. The question: should we build apps by writing traditional code (HTML/CSS/React/Python), or by building skills that orchestrate agents as the app? Is the kernel's skill/task model itself an app framework?

## The Observation

Portfolio site build (backlog 041) exposed this pattern:
- 70 tasks, each one says "write this HTML" or "add this CSS"
- The extraction skill (website-cloner) works well — structured pipeline, reusable
- But the generation side has no skill — each task is a one-off instruction
- A "site-builder" skill could encode: tokens + content + architecture → section HTML + section CSS
- That skill would be reusable across any static site build

## Research Questions

1. **Skill-as-app vs code-as-app:**
   - Traditional: write React components, deploy to Vercel. Agent writes the code, humans use the app.
   - Skill-based: write a skill that agents execute on demand. No deployed app — the agent IS the runtime.
   - When does each approach win? What are the trade-offs?

2. **Generation skills gap:**
   - The kernel has extraction skills (website-cloner) but no generation skills
   - A generation skill would take structured input (tokens, content, architecture) and produce structured output (HTML, CSS, config)
   - Is this just a template engine, or is there something more powerful about agent-mediated generation?

3. **Composability:**
   - Can skills compose? (extractor → transformer → generator, like Unix pipes)
   - The execute-pipeline already chains backlog → task-builder → run-task.sh
   - Could a "build-static-site" skill chain website-cloner → design-token-merger → section-generator → responsive-polisher?

4. **When traditional wins:**
   - Interactive apps (user clicks buttons, real-time state) — agents can't be the runtime
   - High-performance requirements — agent invocation is slow
   - Apps that need to run without the kernel — deployed independently

5. **When skill-based wins:**
   - One-off or infrequent generation tasks (build a site, generate a report)
   - Tasks where the "app" is really a workflow (compliance audit, test automation)
   - When the output IS code/documents, not a running service

6. **Hybrid model:**
   - Agent builds the app (skill-orchestrated), then the app runs traditionally
   - This is what the portfolio site does — agent produces static HTML/CSS, browser renders it
   - Is this the right default? When should the agent remain in the loop at runtime?

## Gaps to Investigate

- No generation skill pattern exists in the kernel — extraction is solved, generation is ad-hoc
- Task descriptions carry too much inline content — should reference structured inputs instead
- No skill composability model — skills are standalone, not pipeable
- No decision framework for "skill vs traditional" — currently ad-hoc per project

## Test Subjects

Use these two as concrete case studies — one skill-based, one traditional app:

### Test Subject 1: Website Cloner (skill-based)
- Location: `.claude/skills/website-cloner/SKILL.md`
- Pattern: Extraction skill with structured pipeline (navigate → screenshot → extract → generate)
- Uses Playwright MCP tools as the runtime
- Reusable — works on any URL
- Agent IS the runtime — no deployed app, just a skill an agent follows
- **Analyze:** What makes this work as a skill? What would break if we tried to make it a traditional app?

### Test Subject 2: Government Fraud Detector (traditional app, backlog 025)
- Location: `docs/backlog/done/025-domain-build-government-spending-tracker.md`
- Sub-docs: `docs/backlog/025-domain-build-government-spending-tracker/` (gaps-analysis, reporting-channels)
- Pattern: Traditional app — Python scanner, pattern library, fixtures, pytest
- Agent builds the code, but the code runs independently
- **Analyze:** Could this have been a skill instead? What would that look like? What would be lost?

## References
- Portfolio site build: `docs/backlog/041-market-build-portfolio-site.md` (70-task case study — hybrid: agent builds, browser renders)
- Website cloner skill: `.claude/skills/website-cloner/SKILL.md` (pure skill-based approach)
- Fraud detector: `docs/backlog/done/025-domain-build-government-spending-tracker.md` (traditional app approach)
- Execute pipeline: `.claude/skills/execute-pipeline/SKILL.md` (orchestration pattern)
- Task builder: `.claude/skills/task-builder/SKILL.md` (decomposition pattern)

## Task Builder Input
- **Deliverable:** Research document with decision framework for skill-as-app vs traditional, plus design sketch for generation skills. Must analyze both test subjects (website-cloner and fraud detector) as concrete examples.
- **Location:** subproject:kernel-architecture
- **Scope:** RESEARCH
- **Constraints:** Should be informed by the portfolio site build experience (041). Must analyze both test subjects in depth — not abstract theorizing. May lead to new backlog items for generation skills and skill composability.

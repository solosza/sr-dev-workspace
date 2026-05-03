# Skill-as-App Architecture Research — Final Report

**Backlog:** 043-kernel-research-skill-as-app-architecture
**Date:** 2026-04-26
**Scope:** Architecture research — when to build skills vs traditional apps vs hybrids

---

## Executive Summary

Analysis of three real kernel projects — the website-cloner (pure skill), the government fraud detector (traditional app), and the portfolio site (hybrid) — reveals a clear architectural boundary: if a deliverable is a **workflow producing artifacts**, build it as a skill; if it's a **running service with persistent state**, build it as a traditional app; if the **agent builds a static artifact that serves itself**, use the hybrid model.

The kernel has a structural gap: extraction skills are mature (website-cloner) but no generation skills exist. This means the "structured input to output" half of any hybrid build is ad-hoc — 75 bespoke tasks in the portfolio build had zero skill coverage. Closing this gap with a generation skill architecture (input contracts, staged pipeline, manifest-on-disk output) would make hybrid builds repeatable instead of one-off.

Skill composability (piping extraction into generation) is architecturally sound but premature to build as a general framework. The immediate priorities are: (1) generation skill design with structured I/O contracts, (2) manifest-on-disk pattern for inter-skill data passing, and (3) state scoping to eliminate contention. A general orchestrator can wait until a second composition pattern emerges beyond execute-pipeline.

---

## Test Subject 1: Website Cloner (Skill-Based)

**Location:** `.claude/skills/website-cloner/SKILL.md`
**Architecture:** Pure skill — agent IS the runtime

The website-cloner is a 6-stage extraction+generation pipeline invoked via `/clone <url>`. It uses Playwright MCP as its runtime — the agent calls browser tools in sequence to extract page data and produce a self-contained HTML/CSS clone.

### Pipeline

| Stage | Action | Output |
|-------|--------|--------|
| 1 | Navigate & screenshot | Reference screenshots (desktop + mobile) |
| 2 | Extract page structure | DOM tree, computed styles, fonts, breakpoints |
| 3 | Generate HTML/CSS | `index.html`, `styles.css` from extracted data |
| 4 | Download assets | `assets/images/`, `assets/fonts/` |
| 5 | Assemble output | Complete self-contained directory |
| 6 | Visual QA | Comparison screenshots, iterative fixes |

### Why Skill Is Correct

- **No runtime independence needed** — invoke agent, get output, done
- **Agent judgment IS the value** — identifying hero sections, choosing CSS tokens vs incidental values, handling canvas/SVG edge cases
- **Reusable** — same skill, any URL, zero modification
- **Stateless** — each invocation starts fresh

### What Would Break as a Traditional App

Building this as a traditional app would require ML models for DOM classification, CSS optimization algorithms, image diffing libraries, a server running Playwright, a job queue, and deployment infrastructure — all to replicate what the agent does natively through judgment calls.

### Weakness

Composability is low. The skill is monolithic — all 6 stages or nothing. There's no way to call "just the extraction stage" from another skill. The output contract is implicit (a directory with `index.html` + `styles.css` + `assets/`) rather than declared via a manifest.

---

## Test Subject 2: Fraud Detector (Traditional App)

**Location:** `D:\my_ai_projects\fraud-detection-app`
**Architecture:** Traditional Python app — 34 source files, 6 packages, 7-layer pipeline

The government fraud detector is a Python application that scans USASpending.gov, IRS 990, SAM.gov, and OFAC data to detect fraud patterns and generate evidence packages for qui tam whistleblower filings. Built across 39 tasks in 10 phases.

### Architecture

```
fraud-detection-app/
  src/apis/        — 4 API clients with shared rate limiting, retries, caching
  src/patterns/    — 22+ fraud patterns, scanner, check functions
  src/scoring/     — Risk scorer (composite) + materiality filter (3-tier)
  src/entity/      — Entity profiler + network analyzer
  src/evidence/    — Archiver, package builder, FinCEN tip generator
  src/pipeline/    — 7 layers (L0-L6) + orchestrator
```

### Why Traditional Is Correct

- **Runtime independence** — runs on cron without agent invocation
- **Persistent state** — scan history, evidence packages, API cache accumulate across runs
- **Performance** — batch API processing at scale; agent tool calls ~100x slower than `requests.get()`
- **Determinism** — fraud scoring must be reproducible for legal proceedings
- **Auditability** — Python code can be reviewed by attorneys; agent reasoning traces cannot
- **Standard testing** — pytest with deterministic fixtures

### What Would Break as a Skill

Can't schedule agent conversations. No persistent history between invocations. Non-deterministic scoring fails legal auditability requirements. Pattern matching through agent reasoning is slower and less reliable than direct Python execution.

### Hybrid Opportunity

Layers 0 (pattern discovery) and 6 (case builder) are where agent judgment would add the most value — discovering new fraud patterns from news/PACER, and writing compelling evidence narratives. These could be skill-augmented layers while keeping L1-L5 as deterministic code.

---

## Test Subject 3: Portfolio Site (Hybrid)

**Location:** Backlogs 047 (70 tasks) + 053 (25 tasks)
**Architecture:** Hybrid — agent builds it, static artifact serves itself

The portfolio site was built across two pipelines: an initial 70-task build and a 25-task visual refactor. The extraction phase used the website-cloner skill (29% of tasks). The generation phase was entirely ad-hoc (71% of tasks).

### The Extraction-Generation Split

| Phase | Tasks | Type | Coverage |
|-------|-------|------|----------|
| Clone Suero (structure) | 001-010 | Extraction (skill-based) | Website-cloner |
| Clone Shader (visual) | 011-020 | Extraction (skill-based) | Website-cloner |
| Merge tokens | 021-030 | Generation (ad-hoc) | No skill |
| Build HTML/CSS | 031-060 | Generation (ad-hoc) | No skill |
| Polish + QA | 061-070 | Generation + QA | No skill |

### Key Finding: The Generation Gap

Build 2 (backlog 053, 25 tasks) exists entirely because the extraction-generation boundary had no quality gate. Shader's canvas-rendered typography produced garbage token values (`16px/400` defaults). The agent extracted them and moved on. 25 refactor tasks were needed to fix aesthetic failures that a token validation gate would have caught.

### Why Hybrid Is Correct

- Agent judgment for aesthetic decisions during build (choosing typography scales, spacing rhythms, color application)
- Zero runtime dependency — static HTML/CSS on any server
- No ongoing agent involvement after build completes

### The Gap It Exposed

75 ad-hoc generation tasks with no skill coverage means the process is invented from scratch for each site build. The next site build can't reuse any of the generation process. This is the kernel's most significant architectural gap.

---

## Generation Skills Gap and Proposed Architecture

### The Asymmetry

| Capability | Skill Exists? | Maturity |
|-----------|--------------|----------|
| Extraction (URL → tokens) | Yes — website-cloner | High — 6-stage pipeline, fallbacks, visual QA |
| Generation (tokens → site) | No | N/A — 75 ad-hoc tasks per project |
| Execution (tasks → done) | Yes — task-builder, run-task.sh | High — decompose, gate, spawn, validate |

### Proposed Generation Skill: Site-Builder

A 6-stage pipeline mirroring extraction's shape:

| Stage | Name | Input | Output | Agent Judgment |
|-------|------|-------|--------|----------------|
| 1 | Foundation | DesignTokens | CSS custom properties, reset, grid | Which tokens → variables vs constants |
| 2 | Scaffold | ArchitectureSpec | Semantic HTML skeleton | Section ordering, containers, landmarks |
| 3 | Populate | ContentSpec + scaffold | HTML with real content | Hierarchy, emphasis, truncation |
| 4 | Style | Tokens + populated HTML | Per-section CSS | Spacing rhythm, color application, visual weight |
| 5 | Responsive | Breakpoints + styled page | Media queries, fluid typography | Reflow, stack, hide decisions per breakpoint |
| 6 | Visual QA | Output + references | Iterative fixes | What "close enough" means |

### Input/Output Contracts

**Input:** Structured JSON files on disk (not context-window data)
- `tokens.json` — DesignTokens (from extraction or manual)
- `content.json` — ContentSpec (sections, headings, body, CTAs)
- `architecture.json` — ArchitectureSpec (layout, grid, responsive strategy)

**Output:** Directory with manifest
- `site/index.html`, `site/styles.css`, `site/assets/`
- `site/manifest.json` — typed output contract for downstream consumption

### Token Validation Gate

A critical addition: validate extraction output before generation begins. Check required fields exist, values are valid CSS, no duplicates. This prevents the portfolio build's failure mode where bad extraction output caused 25 rework tasks.

### Fallback Strategies

Unlike ad-hoc generation (where failures are improvised), the skill documents fallbacks per stage:
- Token conflict → priority rules (later source wins)
- Content overflow → truncate or split
- Typography scale fails at small viewports → fluid `clamp()` by default
- Visual weight off → spacing multiplier adjustment

---

## Skill Composability Model

### Current State: Standalone Monoliths

Every kernel skill is standalone. There is no concept of piping one skill's output into another's input. Execute-pipeline is the closest thing — it chains backlog → task-builder → run-task.sh — but this is orchestration with intimate knowledge of each step's internals, not generic composition.

### Barriers to Composability

1. **Shared mutable state** — Skills share `session_state.json` and `workflow.json`, creating contention (documented in state-contention lesson)
2. **Context window limits** — Chaining skills means both contexts must fit, or one must be externalized
3. **Tool availability** — Different skills need different MCP tools
4. **Error propagation** — Skills have richer failure modes than Unix exit codes

### Design: Manifests on Disk

The recommended composition mechanism: each skill writes output to a directory with a `manifest.json`. The next skill reads from that manifest, not from shared state or context windows. This avoids state contention, survives process boundaries, and enables inspection.

```
[website-cloner] → extraction/manifest.json → [site-builder] → site/manifest.json
```

### Verdict: Not Yet, But Prepare the Ground

A general composition framework is premature — only one composition pattern exists (execute-pipeline). Build these foundations instead:

1. **Skill interface specs** in each SKILL.md (input/output types, error classifications)
2. **Manifest-on-disk pattern** for artifact-producing skills
3. **State scoping** to eliminate shared mutable state contention

Generalize the orchestrator when a second composition pattern emerges.

---

## Decision Framework Summary

### Three Questions

1. **Does it need to run without you?** → Yes: traditional or hybrid
2. **Is the output a workflow or a thing?** → Workflow: skill. Thing: traditional or hybrid
3. **Will humans interact in real-time?** → Yes: traditional. View-only: hybrid

### Decision Tree

```
Does it need to run WITHOUT an agent present?
  YES → Does it need real-time user interaction?
          YES → TRADITIONAL APP (React, API, database)
          NO  → HYBRID (agent builds, static artifact serves itself)
  NO  → Is it a structured workflow producing artifacts?
          YES → SKILL (agent follows pipeline, reusable across inputs)
          NO  → Does it need persistent state?
                  YES → TRADITIONAL APP
                  NO  → SKILL
```

### Anti-Patterns

| Anti-Pattern | Correct Choice |
|-------------|----------------|
| Scheduled scanner as a skill | Traditional app with cron |
| One-time extraction as a traditional app | Skill |
| Static site with React build toolchain | Hybrid |
| Converting traditional app to skill "for simplicity" | Keep traditional |

---

## Recommended Next Steps

### 1. Adopt Decision Framework as Standard Practice

Add "Build Model" classification (skill / traditional / hybrid) to the backlog item template. Apply the three-question test before decomposition begins.

### 2. Build a Generation Skill (Site-Builder)

The most actionable finding. The generation skill design in this research provides input/output contracts, a 6-stage pipeline, fallback strategies, and composability with extraction skills. Implement as `.claude/skills/site-builder/`.

### 3. Build Token-Merger Transform Skill

Lightweight skill (1 SKILL.md + 1 reference) that merges multiple CSS variable files with conflict resolution. Enables multi-source extraction feeding into generation.

### 4. Standardize Skill Interface Specs

Add typed input/output contracts and error classifications to existing SKILL.md files. This improves documentation immediately and prepares the ground for future composability.

### 5. Validate with a Second Hybrid Build

Run one more hybrid build using the generation skill on a simpler target (single-page marketing site) before investing heavily in generation infrastructure.

### 6. Do Not Convert Traditional Apps to Skills

The fraud detector analysis confirms: apps needing runtime independence, persistent state, or real-time interaction should remain traditional. The skill model is complementary, not universal.

---

## Open Questions

1. **JavaScript interactivity boundary** — Where does interactivity push a project from hybrid to traditional? Is there an `interaction-generator` skill, or does any JS requirement mean traditional?

2. **Content spec authoring** — Who writes the structured content specs? If users must author detailed JSON per section, the "low development cost" advantage of skills erodes.

3. **Skill versioning** — As skills evolve, how do we version them? Does the indexed protocol pattern handle this naturally?

4. **Agent judgment vs template determinism** — Is agent-mediated generation actually better than Jinja/Handlebars? What's the quality/consistency trade-off?

5. **Cross-project token reuse** — Can tokens from multiple extractions feed a shared library? Requires a token normalization standard.

6. **Composability beyond web** — Does extraction → transform → generation generalize to other domains (report generation, config generation, test generation)?

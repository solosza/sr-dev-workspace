# Skill-as-App Architecture Research

## Executive Summary

The kernel's skill-based architecture is a legitimate app-building paradigm — not just a code generation convenience. Analysis of three real projects (website-cloner, fraud detector, portfolio site) reveals a clear decision boundary: if the deliverable is a **workflow that produces artifacts** (reports, static sites, configs), build it as a skill; if the deliverable is a **running service with persistent state and real-time interaction**, build it as a traditional app. A third hybrid model — agent builds it, artifact runs independently — covers static sites and generated documentation.

The kernel has a gap: extraction skills exist (website-cloner) but no generation skills. This means the "produce output from structured input" half of the pipeline is ad-hoc. Closing this gap with a section-generator skill and a composability model (extraction → transform → generation) would make the hybrid model scalable and repeatable. The decision framework and generation skill design in this document provide the architectural basis for these next steps.

## Test Subject Analysis

### Website Cloner — Skill-Based (Correct Choice)

The website-cloner validates the skill model. It takes a URL, navigates with Playwright MCP, screenshots pages, extracts design tokens (colors, typography, spacing, components) via `getComputedStyle` and DOM traversal, and produces structured CSS variable files. Every invocation follows the same pipeline. The agent IS the runtime — there is no deployed service, no infrastructure, no maintenance burden. The skill is reusable across any URL with zero modification.

**Why skill wins here:** No runtime independence needed. Output is artifacts (token files, screenshots). Stateless — each invocation starts fresh. No user interaction beyond invoking the agent. High reusability. Building this as a traditional app would require a web UI, a server running Playwright, a job queue, and deployment infrastructure — all overhead for what is fundamentally a structured extraction workflow.

### Fraud Detector — Traditional App (Correct Choice)

The government spending fraud detector validates the traditional model. It's a Python scanner with a pattern library (NGO grants, healthcare, government finance, political corruption), test fixtures, and pytest-based validation. The scanner needs to run on schedules without agent invocation, maintain persistent state (scan history, evidence packages), and perform efficient batch processing against the USASpending API.

**Why traditional wins here:** Runtime independence is required — the scanner runs on its own. Persistent state accumulates across runs. Performance matters for batch API processing. The agent's role was to build the code, not to be the runtime. Converting this to a skill would mean every scan requires an agent conversation, with no persistent history and slower execution through agent reasoning rather than direct Python.

### Portfolio Site — Hybrid (Correct Choice, Exposed a Gap)

The portfolio site (70 tasks, decomposed by task-builder, executed by run-task.sh) validated the hybrid model and exposed the generation skills gap. The extraction phase worked well — website-cloner produced structured design tokens from reference sites. But the generation phase was ad-hoc: each "write this HTML section" task was a one-off instruction with no reusable pattern. The agent built the site, and the static HTML/CSS artifact runs independently in any browser.

**The gap:** Extraction is structured and reusable. Generation is not. A generation skill (tokens + content spec → section HTML + section CSS) would make the build phase as repeatable as the extraction phase. This is the missing piece for scaling the hybrid model.

## Decision Framework

Use this framework to decide whether a new project should be built as a **traditional app**, a **kernel skill**, or a **hybrid** (agent builds, artifact runs independently).

### Decision Matrix

| # | Criterion | Skill | Traditional | Hybrid |
|---|-----------|-------|-------------|--------|
| 1 | **Runtime independence** — Does the deliverable need to run without an agent? | No — agent IS the runtime | Yes — deployed app runs on its own | Agent builds it, then it runs alone |
| 2 | **Output type** — Is the output code/documents, or a running service? | Output is artifacts (HTML, reports, configs) | Output is a running service (API, UI, scanner) | Agent produces artifacts that serve themselves (static site) |
| 3 | **Execution frequency** — One-time/infrequent, or continuous? | One-time or on-demand generation | Continuous or scheduled execution | One-time build, continuous serving |
| 4 | **Persistent state** — Does the app need state between runs? | No — each invocation is stateless | Yes — database, caches, session state | Build is stateless; artifact may have state |
| 5 | **Interactive UI** — Do humans interact in real-time? | No — humans invoke the agent, receive output | Yes — buttons, forms, real-time feedback | No runtime interaction; humans view static output |
| 6 | **Reusability** — Is the workflow reusable across different inputs? | High — same skill, different inputs (any URL, any spec) | Low-to-medium — app is purpose-built | Medium — build pipeline reusable, output is custom |
| 7 | **Performance requirements** — Is latency critical? | No — agent invocation is slow (seconds to minutes) | Yes — sub-second response times required | Build can be slow; serving must be fast |

### Decision Tree

```
Start: What are you building?
  |
  +-- Does it need to run WITHOUT an agent present?
  |     |
  |     +-- YES --> Does it need real-time user interaction?
  |     |             |
  |     |             +-- YES --> TRADITIONAL APP
  |     |             |           (React, API, database)
  |     |             |
  |     |             +-- NO --> HYBRID
  |     |                        (Agent builds static artifact,
  |     |                         artifact serves itself)
  |     |
  |     +-- NO --> Is the deliverable a workflow or generation task?
  |                 |
  |                 +-- YES --> SKILL
  |                 |           (Agent follows structured pipeline,
  |                 |            reusable across inputs)
  |                 |
  |                 +-- NO --> Does it need persistent state?
  |                             |
  |                             +-- YES --> TRADITIONAL APP
  |                             +-- NO --> SKILL
```

### Trade-Off Analysis

| Factor | Skill Approach | Traditional Approach | Hybrid Approach |
|--------|---------------|---------------------|-----------------|
| **Development cost** | Low — write skill spec, agent does the work | Medium-high — write actual application code | Medium — skill for build pipeline, code for artifact |
| **Deployment** | None — no infrastructure | Full stack — servers, CI/CD, monitoring | Static hosting only (Netlify, S3) |
| **Maintenance** | Update skill spec | Update code, dependencies, infrastructure | Update skill; artifact is immutable |
| **Scalability** | Limited by agent invocation speed | Scales with infrastructure | Artifact scales independently |
| **Testability** | Gate contracts + L1/L2/L3 within kernel | Standard testing (pytest, Jest, etc.) | Both — skill gates for build, standard tests for artifact |
| **Composability** | Skills can chain (extractor → generator) | Microservices, but heavier | Build pipeline composes; artifact is standalone |

### Test Subject Analysis

#### Website Cloner — Pure Skill (correct choice)

The website cloner is the canonical example of when skill-based wins:
- **No runtime independence needed** — you invoke the agent, it clones a site, you get output
- **Output is artifacts** — screenshots, extracted tokens, generated HTML/CSS
- **Reusable** — same skill works on any URL
- **No persistent state** — each clone is a fresh invocation
- **No UI** — the agent is the interface

What would break as a traditional app: would need a web UI, a server to run Playwright, a queue for jobs, deployment infrastructure. All overhead for a task that an agent handles in one conversation.

#### Fraud Detector — Traditional App (correct choice)

The government spending fraud detector is the canonical example of when traditional wins:
- **Runtime independence required** — scanner needs to run on schedules, without agent invocation
- **Persistent state** — pattern library, scan history, evidence packages accumulate over time
- **Output is a running service** — not a one-time generation, but an ongoing scanner
- **Performance** — scanning USASpending API data requires efficient batch processing

What would break as a skill: no ability to run on a schedule without agent invocation; each scan would require spinning up an agent conversation; no persistent scan history between invocations; pattern matching would be slower through agent reasoning than through direct Python execution.

#### Portfolio Site — Hybrid (correct choice, with a gap)

The portfolio site exposed the hybrid model and the generation skills gap:
- **Agent builds it** — 70 tasks decomposed by task-builder, executed by run-task.sh
- **Artifact runs independently** — static HTML/CSS served by any web server
- **Extraction skill worked** — website-cloner provided structured design token extraction
- **Generation had no skill** — each "write this HTML section" task was ad-hoc, not following a reusable pattern

The gap: a **generation skill** (input: tokens + content spec + section ID → output: section HTML + section CSS) would make the build phase as structured and reusable as the extraction phase. This is the missing piece for the hybrid model to scale.

### Quick Reference

Given a new project, answer these three questions:

1. **Does it need to run without you?** → If yes, you're building traditional or hybrid.
2. **Is the output a workflow or a thing?** → Workflow = skill. Thing = traditional or hybrid.
3. **Will humans interact with it in real-time?** → If yes, traditional. If they just view output, hybrid.

## Generation Skills

The kernel has extraction skills (website-cloner: URL → structured data) but no generation skills (structured data → output files). This section designs the generation skill pattern and sketches a concrete example.

### The Pattern Gap

Extraction skills follow a clear pipeline:

```
URL → navigate → screenshot → extract (getComputedStyle, DOM) → structured data (JSON tokens)
```

The website-cloner produces design tokens, typography scales, color palettes, spacing systems, and component inventories — all as structured JSON or CSS variables. But when the portfolio site needed to _use_ those tokens to build sections, each task was ad-hoc: "write the hero HTML," "write the hero CSS." No reusable pattern. No structured pipeline. The agent improvised each section from scratch.

Generation skills would mirror extraction:

```
Structured data (tokens + content spec) → transform → produce → output files (HTML + CSS)
```

### Section-Generator Skill Design

A concrete generation skill that takes extracted tokens and a content specification and produces a single page section.

**Identity:**
- Skill name: `section-generator`
- Type: Generation
- Entry point: invoked by task-builder as a step reference, not directly by user

**Input contract:**

| Input | Source | Format |
|-------|--------|--------|
| Design tokens | Extraction skill output or hand-authored | CSS custom properties file (`:root { --color-primary: ...; }`) |
| Content spec | Task file or content document | Markdown with frontmatter: `section_id`, `section_type`, `heading`, `body`, `items[]`, `cta` |
| Section ID | Task parameter | String identifier (e.g., `hero`, `features`, `pricing`) |
| Target files | Task parameter | Paths to `index.html` and `styles.css` to append to |

**Output contract:**

| Output | Format | Destination |
|--------|--------|-------------|
| Section HTML | Semantic HTML (`<section id="...">`) | Appended to `index.html` inside `<main>` |
| Section CSS | Scoped CSS (`#section-id .class { }`) | Appended to `styles.css` |

**Pipeline:**

| Step | Action | Detail |
|------|--------|--------|
| 1 | Read tokens | Parse CSS variables file, extract color/type/spacing tokens |
| 2 | Read content spec | Parse content markdown, extract section metadata and content |
| 3 | Map section type → HTML template | `hero` → `<section>` with `h1` + subtitle + CTA; `features` → grid of cards; `pricing` → comparison table |
| 4 | Generate semantic HTML | Apply tokens as CSS class references, inject content, use semantic elements |
| 5 | Generate scoped CSS | Write styles using `var(--token-name)` references, scoped to `#section-id` |
| 6 | Append to target files | Insert HTML into `<main>`, append CSS to stylesheet |

**Section type registry:**

| Type | HTML Pattern | Key Elements |
|------|-------------|-------------|
| `hero` | Full-width section, centered content | `h1`, subtitle `p`, CTA `a.button`, optional background |
| `features` | Grid layout | Heading, card grid with icon + title + description |
| `pricing` | Comparison columns | Plan cards with name, price, feature list, CTA |
| `testimonials` | Carousel or grid | Quote, attribution, optional avatar |
| `cta-banner` | Full-width colored section | Heading, subtext, button |
| `footer` | Multi-column layout | Nav links, social icons, copyright |

### Composability: Extraction → Generation Chain

The full pipeline chains three skill types:

```
website-cloner          token-merger           section-generator
(extraction)            (transform)            (generation)

URL ──→ navigate ──→    tokens A ──→           tokens + spec ──→
        extract ──→     tokens B ──→  merge    generate HTML ──→
        tokens          tokens C      ──→      generate CSS ──→
                        unified       output   append to files
                        token set
```

**Step 1 — Extract:** Website-cloner visits one or more reference sites, produces structured token files (colors, typography, spacing, components).

**Step 2 — Transform:** A token-merger (new, lightweight) takes multiple token files, resolves conflicts (e.g., two sites define `--color-primary` differently), and produces a single unified token set. This is the simplest skill — it's a merge + conflict resolution on CSS variables.

**Step 3 — Generate:** Section-generator takes the unified tokens + a content spec for each section and produces the actual HTML/CSS output.

**Chaining mechanism:** Each skill's output contract matches the next skill's input contract. No intermediate human step needed. The task-builder decomposes the project into extraction tasks → transform tasks → generation tasks, and `run-task.sh` executes them sequentially.

### Reusability Assessment

**Is section-generator portfolio-specific or general-purpose?**

General-purpose, with constraints:

| Aspect | Reusable? | Notes |
|--------|-----------|-------|
| Token consumption | Yes | Any CSS custom properties file works as input |
| Content spec format | Yes | Markdown + frontmatter is generic |
| Section types | Partially | The type registry is extensible — add new types as reference files |
| HTML output | Yes | Semantic HTML works for any static site |
| CSS scoping | Yes | `#section-id` scoping prevents conflicts regardless of site |
| Framework dependency | No dependency | Pure HTML/CSS output, no React/Vue/etc. |

**Limitation:** The skill produces static HTML/CSS. Sites needing JavaScript interactivity (animations, dynamic filtering, SPAs) would need a separate `interaction-generator` skill or a traditional app approach.

**Reusability scenarios:**
- Clone a SaaS marketing site → extract tokens → generate a new marketing site with different content
- Clone a restaurant site → extract tokens → generate a similar restaurant site for a different client
- Clone multiple award-winning sites → merge best design tokens → generate a new site combining best patterns

### What's Needed to Build This

| Deliverable | Type | Path |
|-------------|------|------|
| Skill folder | Directory | `.claude/skills/section-generator/` |
| SKILL.md | Spec file | `.claude/skills/section-generator/SKILL.md` |
| Token reader reference | Step file | `.claude/skills/section-generator/references/read-tokens.md` |
| Content parser reference | Step file | `.claude/skills/section-generator/references/parse-content.md` |
| HTML generator reference | Step file | `.claude/skills/section-generator/references/generate-html.md` |
| CSS generator reference | Step file | `.claude/skills/section-generator/references/generate-css.md` |
| Section type registry | Reference | `.claude/skills/section-generator/references/section-types.md` |
| Token-merger skill | Separate skill | `.claude/skills/token-merger/` (lightweight — 1 SKILL.md + 1 reference) |
| Command wrapper | Command | `.claude/commands/kernel/generate-section.md` |
| MCP tools | None needed | Pure file I/O — no browser automation for generation |

**Estimated complexity:** Medium. The section-generator has more reference files than website-cloner (6 vs 2) because generation requires type-specific templates. But each reference file is focused and small — the skill follows the same indexed pattern as all kernel skills.

## Recommendations

### 1. Adopt the Decision Framework as Standard Practice

Every new project entering the backlog should be classified using the decision tree (skill / traditional / hybrid) before decomposition begins. This prevents the current ad-hoc approach where the build model is discovered mid-project. Add the classification to the backlog item template.

**Potential backlog item:** Update `/kernel/backlog` command to include a "Build Model" field (skill / traditional / hybrid) with the three-question quick reference.

### 2. Build the Section-Generator Skill

The generation skills gap is the most actionable finding. The section-generator design in this document is concrete enough to implement directly. This would make the hybrid model (agent builds static site) repeatable and structured rather than ad-hoc.

**Potential backlog item:** Build `.claude/skills/section-generator/` — SKILL.md, 6 reference files, section type registry, command wrapper.

### 3. Build the Token-Merger Transform Skill

The composability chain (extraction → transform → generation) needs the middle link. Token-merger is lightweight — one SKILL.md, one reference file — and enables multi-source extraction to feed into generation.

**Potential backlog item:** Build `.claude/skills/token-merger/` — merge multiple CSS variable files with conflict resolution.

### 4. Do Not Convert Traditional Apps to Skills

The fraud detector analysis confirms: apps that need runtime independence, persistent state, or real-time interaction should remain traditional. The skill model is not a universal replacement — it's a complementary paradigm for workflow-oriented deliverables.

### 5. Validate with a Second Hybrid Build

The portfolio site was the first hybrid project. Before investing heavily in generation skills infrastructure, run one more hybrid build using the section-generator to confirm the pattern holds. Pick a simpler site (single-page marketing site) as the validation target.

**Potential backlog item:** Clone + generate a single-page marketing site using website-cloner → token-merger → section-generator pipeline.

## Open Questions

1. **JavaScript interactivity boundary** — The section-generator produces static HTML/CSS. Where does interactivity fit? A separate `interaction-generator` skill? Or does interactivity always push a project from hybrid to traditional?

2. **Content spec authoring** — Who writes the content specs that feed the section-generator? The user? Another skill? If the user must author detailed markdown specs per section, the "low development cost" advantage of skills erodes.

3. **Skill versioning** — As skills evolve (new section types, improved token parsing), how do we version them? The kernel has no skill versioning model. Does the indexed protocol pattern (SKILL.md → references) handle this naturally, or do we need explicit version tracking?

4. **Agent reasoning vs template determinism** — The section-generator lets the agent reason about how to map tokens to HTML. A pure template engine would be deterministic but rigid. Is agent-mediated generation actually better than Jinja/Handlebars templates? What's the quality/consistency trade-off?

5. **Cross-project token reuse** — If multiple projects extract tokens from different sites, can those tokens feed into a shared token library? This would enable "clone the best of 5 sites" workflows but requires a token normalization standard.

6. **Skill composability beyond web** — The extraction → transform → generation chain works for static sites. Does the pattern generalize to other domains (report generation, config generation, test generation)? Or is it web-specific?

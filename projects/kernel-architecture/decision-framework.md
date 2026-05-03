# Decision Framework: Skill-as-App vs Traditional App vs Hybrid

## Purpose

Structured framework for choosing the right build model when a new project enters the backlog. Apply this before decomposition begins — the build model determines task shape, testing strategy, and deployment.

## Decision Criteria Table

| # | Criterion | Skill-as-App | Traditional App | Hybrid |
|---|-----------|-------------|-----------------|--------|
| 1 | **Runtime independence** | No — agent IS the runtime | Yes — runs unattended (cron, server, daemon) | Agent builds it, then it runs alone |
| 2 | **Output type** | Artifacts (tokens, reports, configs, screenshots) | Running service (API, scanner, UI) | Static artifact that serves itself (HTML site, PDF, generated codebase) |
| 3 | **Execution frequency** | On-demand or one-time | Continuous, scheduled, or event-driven | One-time build, continuous serving |
| 4 | **Persistent state** | None — each invocation starts fresh | Yes — database, filesystem, caches | Build is stateless; artifact may have state |
| 5 | **Real-time interactivity** | None — invoke agent, receive output | Yes — buttons, forms, WebSocket, real-time feedback | No runtime interaction; humans view static output |
| 6 | **Reusability** | High — same skill, any input (any URL, any spec) | Low-to-medium — purpose-built for one domain | Medium — build pipeline reusable, output is custom |
| 7 | **Performance** | Slow — agent reasoning adds seconds-to-minutes per step | Fast — sub-second response, batch processing, connection pooling | Build can be slow; serving must be fast |
| 8 | **Determinism** | Low — agent judgment varies between runs | High — same input produces same output | Build varies; artifact is static once produced |
| 9 | **Testability** | Gate contracts + visual QA within kernel | Standard frameworks (pytest, Jest, Playwright) | Both — skill gates for build, standard tests for artifact |
| 10 | **Deployment** | None — no infrastructure | Full stack (servers, CI/CD, monitoring) | Static hosting only (GitHub Pages, S3, Netlify) |

## Decision Flowchart

```
Start: What are you building?
  |
  +-- Does the deliverable need to run WITHOUT an agent present?
  |     |
  |     +-- NO --> Is it a structured workflow producing artifacts?
  |     |           |
  |     |           +-- YES --> SKILL-AS-APP
  |     |           |           Examples: website-cloner, token extraction,
  |     |           |           report generation, config auditing
  |     |           |
  |     |           +-- NO --> Does it need persistent state between runs?
  |     |                       |
  |     |                       +-- YES --> TRADITIONAL APP
  |     |                       +-- NO --> SKILL-AS-APP
  |     |
  |     +-- YES --> Does it need real-time user interaction?
  |                   |
  |                   +-- YES --> TRADITIONAL APP
  |                   |           Examples: fraud scanner with API,
  |                   |           dashboard with live data, SPA
  |                   |
  |                   +-- NO --> Is the output static files that serve themselves?
  |                               |
  |                               +-- YES --> HYBRID
  |                               |           Examples: portfolio site, marketing page,
  |                               |           generated documentation site
  |                               |
  |                               +-- NO --> TRADITIONAL APP
  |                                           Examples: scheduled scanner,
  |                                           batch processor, CLI tool
```

## Quick Reference (Three Questions)

1. **Does it need to run without you?** If yes: traditional or hybrid.
2. **Is the output a workflow or a thing?** Workflow = skill. Thing = traditional or hybrid.
3. **Will humans interact with it in real-time?** If yes: traditional. If they just view output: hybrid.

## When to use Skill-Based

A skill is correct when the agent's judgment IS the product — there is no separate runtime, no deployed service, no infrastructure. The agent follows a structured pipeline and produces artifacts.

| Example | Why Skill Wins | What Breaks as Traditional |
|---------|---------------|---------------------------|
| **Website cloner** (extract design tokens from any URL) | Agent judgment identifies hero sections, chooses which CSS values are tokens vs incidental, handles canvas/SVG edge cases | Would need ML model for DOM classification, CSS optimization algorithms, image diffing library — all to replicate what the agent does natively |
| **Config auditor** (scan SSH configs against compliance frameworks) | Agent reads framework docs, maps directives to rules, produces structured findings | Would need manually coded rule engine for each framework, updated whenever standards change |
| **Report generator** (structured data → formatted analysis) | Agent synthesizes narrative from data, makes editorial judgment calls | Template engine produces deterministic but rigid output; agent adds insight |

**Skill signals:** No deployment. Stateless. Output is files, not a service. Reusable across inputs. Agent judgment adds value over deterministic code.

## When to Use Traditional App

A traditional app is correct when the deliverable must run independently, maintain state, or meet performance requirements that agent invocation cannot satisfy.

| Example | Why Traditional Wins | What Breaks as Skill |
|---------|---------------------|---------------------|
| **Fraud detector** (scan USASpending API daily for fraud patterns) | Runs on cron without agent. Persistent scan history. Batch API processing at scale. Evidence packages with SHA-256 hashes for legal proceedings. | Can't schedule agent invocations. No persistent state between conversations. Agent tool calls 100x slower than `requests.get()`. Non-deterministic scoring fails legal auditability. |
| **API service** (serve data via REST endpoints) | Sub-second response times. Concurrent request handling. Database-backed. | Agent reasoning adds seconds per request. No concurrency model. |
| **CLI tool** (parse files, transform data, produce output) | Deterministic. Runs in CI/CD. Composable with other tools via stdin/stdout. | Agent invocation is heavy for a pipeline step. Non-deterministic output breaks CI. |

**Traditional signals:** Scheduled/continuous execution. Persistent state. Performance-critical. Deterministic output required. Real-time UI. Runs in CI/CD.

## When to Use Hybrid

Hybrid is correct when the agent builds the deliverable (using skills for extraction, ad-hoc tasks for generation) but the output runs independently as a static artifact.

| Example | Why Hybrid Wins | Extraction vs Generation Split |
|---------|----------------|-------------------------------|
| **Portfolio site** (clone reference sites → extract tokens → build static HTML/CSS) | Agent judgment for aesthetic decisions during build. Zero runtime dependency — static files on any server. | 29% skill-based extraction (website-cloner), 71% ad-hoc generation (HTML sections, CSS, responsive layout) |
| **Documentation site** (scan codebase → extract API signatures → generate reference docs) | Agent understands code intent better than autodoc tools. Static output deploys to GitHub Pages. | Extraction: parse source files. Generation: write explanatory prose, organize navigation. |
| **Marketing page** (clone award-winning design → merge tokens → generate new site with different content) | Reuses extraction pipeline. Custom content per client. Static hosting. | Extraction: website-cloner. Generation: section-generator (future skill). |

**Hybrid signals:** Agent builds it once, artifact serves itself forever. No runtime agent dependency. Static hosting sufficient. Extraction skills apply but generation is bespoke.

**Known gap:** The kernel has mature extraction skills but no generation skills. The 71% ad-hoc generation in the portfolio build is evidence of this gap. A section-generator skill would shift hybrid builds from mostly-ad-hoc to mostly-skill-covered.

## Trade-Off Summary

| Factor | Skill | Traditional | Hybrid |
|--------|-------|-------------|--------|
| **Dev cost** | Low — write skill spec | Medium-high — write application code | Medium — skill for extraction, ad-hoc for generation |
| **Maintenance** | Update markdown instructions | Update code + dependencies + infrastructure | Update skill; artifact is immutable |
| **Scalability** | Limited by agent invocation speed | Scales with infrastructure | Artifact scales; build doesn't need to |
| **Composability** | Currently low (standalone monoliths) | High (import modules, microservices) | Build pipeline composes; artifact is standalone |
| **Modification** | Edit prose instructions | Code change → test → deploy | Re-run build pipeline with new inputs |
| **Quality assurance** | Gate contracts + agent visual QA | Standard test frameworks (deterministic) | Both layers |

## Anti-Patterns

| Anti-Pattern | Why It Fails | Correct Choice |
|-------------|-------------|----------------|
| Building a scheduled scanner as a skill | Can't cron-schedule agent conversations. No persistent history between invocations. | Traditional app with cron. |
| Building a one-time extraction as a traditional app | Web UI, server, job queue — all overhead for a single conversation workflow. | Skill. |
| Building a static site as a traditional app | React build toolchain, Node server, CI/CD — overkill for files that don't change. | Hybrid (agent builds, static hosting serves). |
| Assuming skill = no code | Skills can produce code as output (fraud detector was built by task-builder). The distinction is agent-as-runtime vs agent-as-builder. | Classify by runtime model, not output format. |
| Converting a traditional app to a skill "for simplicity" | Loses runtime independence, persistent state, performance, determinism. | Keep traditional. Skills are complementary, not universal. |

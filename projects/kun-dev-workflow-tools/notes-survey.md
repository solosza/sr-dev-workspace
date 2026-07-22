# Notes — Full Repo Survey of kunchenguid

## Search Queries Used

1. `kunchenguid axi "agent experience interface" design principles github`
2. `kunchenguid gnhf "good night have fun" agent hands-off companion mode`
3. `kunchenguid firstmate agent crew worktree session multi-agent`
4. `kunchenguid no-mistakes git push gate review TUI`
5. `kunchenguid chrome-devtools-axi browser automation CDP agent`
6. `kunchenguid gh-axi github CLI agent 100% task success benchmark`
7. `KunAgent Kun AI agent workspace code design write mode`
8. `site:github.com/kunchenguid repos 2026 wheelhouse herdr`

---

## Repo Catalog

### 1. treehouse

- **URL:** https://github.com/kunchenguid/treehouse
- **Tagline:** "Manage worktrees without managing worktrees."
- **What it does:** Git worktree pool manager. Manages a pool of git worktrees per repository under a configured root. Features: state recovery via atomic file writes, dirty detection (tracked + untracked), safe pruning (only idle worktrees merged into default branch with clean tree). Prune is dry-run by default. `--global` inspects all pools.
- **Language:** Go
- **Stars:** ~682 | **Forks:** 71
- **License:** MIT
- **Maintenance:** Active — has releases page, CLAUDE.md, third-party fork (treehouse-worktree MCP variant by mark-hingston).
- **Sources:** https://github.com/kunchenguid/treehouse, https://context7.com/kunchenguid/treehouse

#### Workflow Fit Verdicts

| Hook | Verdict | Notes |
|------|---------|-------|
| Kernel loop (session-start/anchor/learn/complete) | **No direct fit** | Treehouse manages git worktrees, not agent session state. Kernel loop is protocol-level, treehouse is filesystem-level. |
| execute-pipeline / run-task.sh | **HIGH** | Each pipeline run could get its own treehouse worktree, eliminating `.claude/state/` contention between interactive sessions and background agents. Directly addresses backlog 123. |
| Worktree isolation (backlog 123) | **HIGH — PRIMARY CANDIDATE** | This IS the worktree isolation tool. Pool management, safe pruning, dirty detection — exactly what backlog 123 needs. Replaces raw `git worktree add/remove` with lifecycle management. |
| Code review flow | **Moderate** | Worktrees enable parallel review (review in one worktree while developing in another), but treehouse doesn't have review-specific features. |
| Claude Code day-to-day | **Moderate** | Claude Code has built-in `EnterWorktree` tool; treehouse would be an external alternative with pool management. Useful if managing many worktrees across repos. |

---

### 2. lavish-axi

- **URL:** https://github.com/kunchenguid/lavish-axi
- **Tagline:** "HTML is the new markdown. Lavish is the new editor for your HTML artifacts."
- **What it does:** Visual HTML artifact editor. Converts agent output (plans, comparisons, diagrams, tables, diffs, reports) into rich, reviewable HTML with inline annotation/feedback. CLI: `npx -y lavish-axi`. Installable as Agent Skill.
- **Language:** TypeScript/Node
- **Stars:** ~1,800
- **License:** MIT
- **Maintenance:** Active — npm package (v0.1.32), listed on mcpservers.org Agent Skills, trending on trendshift.io.
- **Sources:** https://github.com/kunchenguid/lavish-axi, https://libraries.io/npm/lavish-axi, https://mcpservers.org/agent-skills/kunchenguid/lavish

#### Workflow Fit Verdicts

| Hook | Verdict | Notes |
|------|---------|-------|
| Kernel loop | **No fit** | Kernel loop is session/anchor/learn protocol. Lavish is a visualization tool. |
| execute-pipeline / run-task.sh | **Low** | Pipeline produces reports; Lavish could render them as HTML, but current workflow uses markdown reports which work fine. |
| Worktree isolation (backlog 123) | **No fit** | Unrelated to git worktrees. |
| Code review flow | **Moderate** | Could visualize review findings as interactive HTML artifacts with inline annotation. More useful for human review of large diffs or architecture changes. |
| Claude Code day-to-day | **Moderate** | Useful for visualizing complex plans, design docs, or research reports during interactive sessions. Nice-to-have, not critical. |

---

### 3. axi (Agent eXperience Interface)

- **URL:** https://github.com/kunchenguid/axi
- **Website:** https://axi.md/
- **Tagline:** "Design principles for agent ergonomics. Higher accuracy with lower token cost than both MCP and regular CLI."
- **What it does:** A design philosophy + specification for building agent-native CLI tools. 10 design principles: token-efficient TOON output format (~40% savings over JSON), minimal default schemas (3-4 fields per list item), content truncation with size hints, contextual next-step disclosure, pre-computed fields eliminating round trips. Reference implementations: gh-axi, chrome-devtools-axi. Benchmarked: 100% task success, lowest cost.
- **Language:** Markdown/spec (+ benchmark code)
- **Stars:** Not found in search (spec repo, not a tool)
- **License:** MIT (inferred from implementations)
- **Maintenance:** Active — benchmark studies published, Medium article, implementations shipping.
- **Sources:** https://github.com/kunchenguid/axi, https://axi.md/, https://kunchenguid.medium.com/i-benchmarked-github-cli-vs-mcp-vs-tool-search-vs-code-mode-turns-out-the-best-solution-is-none-93528d5039e4

#### Workflow Fit Verdicts

| Hook | Verdict | Notes |
|------|---------|-------|
| Kernel loop | **No fit** | AXI is a CLI design spec, not a session protocol. |
| execute-pipeline / run-task.sh | **Low** | Pipeline doesn't expose CLI tools to agents; agents use Claude Code tools. |
| Worktree isolation (backlog 123) | **No fit** | Unrelated. |
| Code review flow | **Low** | AXI principles could inform how review commands output results, but we're not building new CLIs. |
| Claude Code day-to-day | **Moderate — DESIGN REFERENCE** | AXI's TOON format and token-efficient principles are relevant when designing agent-facing output (e.g., reports, summaries). Not a tool to install but a design reference to study. |

---

### 4. gnhf (Good Night, Have Fun)

- **URL:** https://github.com/kunchenguid/gnhf
- **Tagline:** "Before I go to bed, I tell my agents: good night, have fun"
- **What it does:** Autonomous overnight orchestrator. Runs incremental code transformations while you sleep — each iteration makes one small, committed, documented change. Modes: Hands-Off (bounded overnight), Companion (outer agent steers). Features: incremental unsigned commits (cherry-pick/revert individual changes), failure rollback via git reset, resume support on existing gnhf/ branches, exit summary.
- **Language:** TypeScript/Node (npm package)
- **Stars:** 1,000+ (hit 1K milestone per X post)
- **License:** MIT (inferred)
- **Maintenance:** Active — npm (v0.1.41), regular releases, X posts.
- **Sources:** https://github.com/kunchenguid/gnhf, https://libraries.io/npm/gnhf, https://x.com/kunchenguid/status/2048978455107383456

#### Workflow Fit Verdicts

| Hook | Verdict | Notes |
|------|---------|-------|
| Kernel loop | **Moderate — PARALLEL PATTERN** | gnhf's iteration loop (do work → commit → next) is structurally similar to kernel's work loop (action → anchor → complete). Study for design patterns, not direct integration. |
| execute-pipeline / run-task.sh | **HIGH — ALTERNATIVE ORCHESTRATOR** | gnhf does what execute-pipeline + run-task.sh does: iterate through tasks, commit each, handle failures, resume. Key differences: gnhf uses git commits as checkpoints (vs. state files), is npm-based (vs. bash), and has simpler lifecycle. Could be an alternative or complement to run-task.sh for simpler pipelines. |
| Worktree isolation (backlog 123) | **Moderate** | gnhf creates its own branches but doesn't use worktree isolation. However, gnhf + treehouse would be a powerful combination. |
| Code review flow | **Low** | Not review-specific. |
| Claude Code day-to-day | **HIGH** | Perfect for overnight batch work: "run these 20 backlogs while I sleep." Currently we do this with run-task.sh + background agents; gnhf is a polished alternative with better resume and commit semantics. |

---

### 5. firstmate

- **URL:** https://github.com/kunchenguid/firstmate
- **Tagline:** "Talk to one agent. Ship with a crew."
- **What it does:** Multi-agent crew orchestrator ("agent distro"). You talk to a single first mate agent, which routes requests to crewmates — each in its own session endpoint and git worktree (via treehouse). Features: zero-token event-driven watcher, ship tasks (deliver changes) vs scout tasks (investigate/audit/report), secondmates (persistent domain supervisors), supports tmux/herdr/zellij/Orca/cmux backends.
- **Language:** Shell/Markdown (agent distro = instructions + skills + scripts, no app to install)
- **Stars:** Not found in search
- **License:** MIT (inferred from CONTRIBUTING.md)
- **Maintenance:** Active — AGENTS.md, CLAUDE.md, CONTRIBUTING.md, pull requests, docs.
- **Sources:** https://github.com/kunchenguid/firstmate, https://github.com/kunchenguid/firstmate/blob/main/AGENTS.md

#### Workflow Fit Verdicts

| Hook | Verdict | Notes |
|------|---------|-------|
| Kernel loop | **Moderate** | Firstmate's ship/scout task model is analogous to kernel's BUILD/RESEARCH task types. Design pattern overlap but different execution model. |
| execute-pipeline / run-task.sh | **HIGH — ALTERNATIVE ARCHITECTURE** | Firstmate IS a pipeline executor: routes tasks to crewmates in isolated worktrees, supervises, collects results. vs. execute-pipeline which uses run-task.sh + one-shot agents. Firstmate adds: visible session backends (tmux tabs), worktree isolation via treehouse, zero-token supervision. Major architectural alternative. |
| Worktree isolation (backlog 123) | **HIGH** | Firstmate uses treehouse for worktree isolation by design. Each crewmate gets its own worktree. This is backlog 123 solved at the orchestration layer. |
| Code review flow | **Moderate** | Scout tasks could be used for review (investigate/audit/report). Not a dedicated review tool. |
| Claude Code day-to-day | **HIGH** | Could replace the current spawn-subagent pattern. Instead of spawning background agents, use firstmate to manage a crew with visible sessions. |

---

### 6. no-mistakes

- **URL:** https://github.com/kunchenguid/no-mistakes
- **Website:** https://kunchenguid.github.io/no-mistakes/
- **Tagline:** "git push no-mistakes"
- **What it does:** Local git proxy + quality gate. Push to `no-mistakes` remote instead of origin → spins up disposable worktree → runs AI validation pipeline (review, tests, lint, docs) → forwards upstream only when all checks pass → opens PR automatically. Three modes: `git push no-mistakes` (committed branch), TUI wizard (uncommitted changes), `/no-mistakes` agent skill (task + gate). Agent-agnostic: claude, codex, rovodev, opencode, pi, acp.
- **Language:** Go
- **Stars:** Not found in search
- **License:** MIT (inferred)
- **Maintenance:** Active — docs site, issues, releases.
- **Sources:** https://github.com/kunchenguid/no-mistakes, https://kunchenguid.github.io/no-mistakes/concepts/gate-model/

#### Workflow Fit Verdicts

| Hook | Verdict | Notes |
|------|---------|-------|
| Kernel loop | **Moderate — GATE PATTERN OVERLAP** | no-mistakes' gate model (run checks → pass/fail → forward/block) is analogous to kernel's anchor/complete gates. Design reference for gate mechanics. |
| execute-pipeline / run-task.sh | **Moderate** | Could be used as the push gate after pipeline completion: pipeline produces branch → push through no-mistakes → validated PR. Currently we don't auto-push. |
| Worktree isolation (backlog 123) | **Moderate** | Uses disposable worktrees for validation (similar concept to pipeline isolation), but designed for push gating, not pipeline execution. |
| Code review flow | **HIGH — PRIMARY CANDIDATE** | This IS a code review gate tool. AI-driven validation pipeline runs review, tests, lint, docs. Directly useful for the review-queue / orchestrator gate validation flow. Could replace or complement the current manual orchestrator validation. |
| Claude Code day-to-day | **HIGH** | Drop-in quality gate for pushes. Instead of pushing and hoping CI passes, validate locally first. The `/no-mistakes` agent skill integrates directly with Claude Code. |

---

### 7. gh-axi

- **URL:** https://github.com/kunchenguid/gh-axi
- **Tagline:** "GitHub CLI for agents — designed with AXI."
- **What it does:** AXI-compliant GitHub CLI. Commands: dashboard, list issues, view PRs, list workflow runs. Benchmarked: 100% task success (vs raw gh 86%), 7% lower cost ($4.26 vs $4.58), 66% cheaper than GitHub MCP, 74% fewer input tokens. Averages 15.7s/46K input tokens per task.
- **Language:** Go
- **Stars:** Trending on trendshift.io
- **License:** MIT (inferred from axi ecosystem)
- **Maintenance:** Active — benchmark results published, trending.
- **Sources:** https://github.com/kunchenguid/gh-axi, https://trendshift.io/repositories/69174, https://github.com/kunchenguid/axi/blob/main/bench-github/published-results/STUDY.md

#### Workflow Fit Verdicts

| Hook | Verdict | Notes |
|------|---------|-------|
| Kernel loop | **No fit** | GitHub operations aren't part of the kernel loop. |
| execute-pipeline / run-task.sh | **Low** | Pipeline doesn't interact with GitHub API directly. |
| Worktree isolation (backlog 123) | **No fit** | Unrelated. |
| Code review flow | **Moderate** | Could be used for PR operations in review flow (create PR, list checks, post comments) with better token efficiency than raw gh or GitHub MCP. |
| Claude Code day-to-day | **HIGH** | Drop-in replacement for `gh` CLI when agents do GitHub operations. 100% success vs 86% for raw gh, lower cost. Install as agent skill. |

---

### 8. chrome-devtools-axi

- **URL:** https://github.com/kunchenguid/chrome-devtools-axi
- **Tagline:** "The most agent-ergonomic browser automation"
- **What it does:** AXI-compliant browser automation via CDP. Auto-lifecycle (bridge process, PID file, stale target recycling). TOON-encoded output (-40% tokens vs JSON). Combines operations (navigate + snapshot + suggestions). Benchmarked: 100% success at $0.074/task, 21.5s, 4.5 turns. 57% fewer input tokens vs raw chrome-devtools-mcp.
- **Language:** TypeScript/Node
- **Stars:** Not found
- **License:** MIT (inferred)
- **Maintenance:** Active — listed on LobeHub Skills Marketplace, LinkedIn post, benchmark data.
- **Sources:** https://github.com/kunchenguid/chrome-devtools-axi, https://github.com/kunchenguid/axi/blob/main/bench-browser/published-results/report.md

#### Workflow Fit Verdicts

| Hook | Verdict | Notes |
|------|---------|-------|
| Kernel loop | **No fit** | Browser automation isn't part of the kernel loop. |
| execute-pipeline / run-task.sh | **Low** | Pipeline tasks don't do browser automation. |
| Worktree isolation (backlog 123) | **No fit** | Unrelated. |
| Code review flow | **No fit** | Review flow is code-level, not browser-level. |
| Claude Code day-to-day | **Moderate** | Alternative to Playwright MCP for browser automation. We currently use Playwright MCP (lesson #42 confirms it works). CDP-based approach is different but benchmarks well. Worth evaluating if Playwright MCP has issues. |

---

### 9. wheelhouse

- **URL:** https://github.com/kunchenguid/wheelhouse
- **Tagline:** "Steer your open-source maintenance from one place."
- **What it does:** Portable IssueOps command center. Cross-repo decision cards driven by GitHub Actions. Decisions by checkbox or plain English.
- **Language:** Not determined
- **Stars:** Not found
- **License:** Not determined
- **Maintenance:** Active (referenced in profile).
- **Sources:** https://github.com/kunchenguid/wheelhouse

#### Workflow Fit Verdicts

| Hook | Verdict | Notes |
|------|---------|-------|
| Kernel loop | **No fit** | IssueOps is GitHub-level, not session-level. |
| execute-pipeline / run-task.sh | **No fit** | Different orchestration model (GitHub Actions vs local). |
| Worktree isolation (backlog 123) | **No fit** | Unrelated. |
| Code review flow | **Low** | Cross-repo decision cards could inform multi-repo review, but our repos are few and managed locally. |
| Claude Code day-to-day | **Low** | Designed for open-source maintainers with many repos. Our workspace has 2-3 repos. |

---

### 10. dotfiles

- **URL:** https://github.com/kunchenguid/dotfiles
- **Tagline:** "Kun's dotfiles for agentic engineering"
- **What it does:** Machine config: nix-darwin + home-manager. Includes configs for Neovim, WezTerm, herdr, Claude settings, shared AGENTS.md. Bootstrap.sh applies everything.
- **Language:** Nix/Shell
- **Stars:** Not found
- **License:** Not determined
- **Maintenance:** Active.
- **Sources:** https://github.com/kunchenguid/dotfiles

#### Workflow Fit Verdicts

| Hook | Verdict | Notes |
|------|---------|-------|
| Kernel loop | **No fit** | Machine config, not agent protocol. |
| execute-pipeline / run-task.sh | **No fit** | Unrelated. |
| Worktree isolation (backlog 123) | **No fit** | Unrelated. |
| Code review flow | **No fit** | Unrelated. |
| Claude Code day-to-day | **Low — REFERENCE ONLY** | Interesting to study his Claude settings and AGENTS.md for ideas, but not installable as a tool. Mac-only (nix-darwin). |

---

### 11. KunAgent/Kun

- **URL:** https://github.com/KunAgent/Kun
- **Website:** https://www.kun-agent.com/
- **Tagline:** "AI agent workspace with Code Write and Design modes built into your application."
- **What it does:** Full agent workspace GUI. Requirement-first workflow: Requirement → Design → Plan → Code → Verify. Modes: Code (edit real codebases), Design (generate prototypes, design systems), Write (markdown workspaces). Uses DeepSeek as default model.
- **Language:** TypeScript (assumed)
- **Stars:** Not found
- **License:** Not determined
- **Maintenance:** Active — website, releases, README in Chinese + English.
- **Sources:** https://github.com/KunAgent/Kun, https://www.kun-agent.com/

#### Workflow Fit Verdicts

| Hook | Verdict | Notes |
|------|---------|-------|
| Kernel loop | **No fit** | A full IDE/workspace, not a protocol component. |
| execute-pipeline / run-task.sh | **No fit** | Different paradigm (GUI vs CLI pipeline). |
| Worktree isolation (backlog 123) | **No fit** | Unrelated. |
| Code review flow | **No fit** | Internal review in Kun's own workflow, not extensible to ours. |
| Claude Code day-to-day | **No fit** | Competing paradigm to Claude Code, not complementary. Uses DeepSeek, not Claude. |

---

## Summary: Usefulness Ranking

| Rank | Repo | Primary Hook | Verdict |
|------|------|-------------|---------|
| 1 | **treehouse** | Worktree isolation (backlog 123) | **HIGH** — Primary candidate for pipeline worktree isolation |
| 2 | **firstmate** | execute-pipeline + worktree isolation | **HIGH** — Alternative architecture for pipeline orchestration with built-in worktree isolation |
| 3 | **gnhf** | execute-pipeline + day-to-day | **HIGH** — Alternative/complement to run-task.sh for overnight batch work |
| 4 | **no-mistakes** | Code review + day-to-day | **HIGH** — Quality gate for pushes, review pipeline |
| 5 | **gh-axi** | Day-to-day | **HIGH** — Drop-in improvement for GitHub CLI operations |
| 6 | **axi** | Day-to-day (reference) | **Moderate** — Design spec worth studying for token efficiency |
| 7 | **chrome-devtools-axi** | Day-to-day | **Moderate** — Alternative to Playwright MCP |
| 8 | **lavish-axi** | Day-to-day (visualization) | **Moderate** — Nice-to-have for rich output |
| 9 | **dotfiles** | Reference | **Low** — Study Claude settings, not installable |
| 10 | **wheelhouse** | None | **Low** — OSS maintainer tool, not our use case |
| 11 | **KunAgent/Kun** | None | **No fit** — Competing paradigm |

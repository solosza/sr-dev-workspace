# Research Report — 231 "Kun" Dev-Workflow Tools

Backlog: docs/backlog/231-kernel-research-kun-dev-workflow-tools.md
Sources: notes-identity.md, notes-survey.md

---

## Developer

**Name:** Kun Chen
**GitHub handle:** `kunchenguid`
**Profile:** https://github.com/kunchenguid
**X/Twitter:** https://x.com/kunchenguid
**Background:** Former L8 engineer at Meta, Microsoft, and Atlassian.

**Evidence trail:**
- GitHub profile confirms "Kun Chen": https://github.com/kunchenguid
- Threads post by @petergyang credits Kun as builder of Lavish: https://www.threads.com/@petergyang/post/DZU_B_9lCGM/
- X post from @kunchenguid confirms Lavish authorship: https://x.com/kunchenguid/status/2061653260231143923
- Dotfiles repo described as "Kun's dotfiles for agentic engineering": https://github.com/kunchenguid/dotfiles

**Match confidence:** HIGH — single candidate. The user's fuzzy "Kun" maps directly to Kun Chen (`kunchenguid`). Both remembered repos confirmed under this handle.

---

## Confirmed Repos

### 1. "Lavish" → lavish-axi

- **URL:** https://github.com/kunchenguid/lavish-axi
- **Purpose:** Visual HTML artifact editor for agent workflows. Converts agent output (plans, comparisons, diagrams, tables, diffs, reports) into rich, reviewable HTML with inline annotation/feedback.
- **CLI:** `npx -y lavish-axi` (zero-install). Also installable as Agent Skill: `npx skills add kunchenguid/lavish-axi --skill lavish`
- **Stars:** ~1,800
- **License:** MIT
- **Maintenance:** Active — npm v0.1.32, listed on mcpservers.org Agent Skills, trending on trendshift.io.
- **Sources:** https://github.com/kunchenguid/lavish-axi, https://libraries.io/npm/lavish-axi, https://mcpservers.org/agent-skills/kunchenguid/lavish

### 2. "Worktree" → treehouse

- **URL:** https://github.com/kunchenguid/treehouse
- **Purpose:** Git worktree pool manager. Manages a pool of git worktrees per repository under a configured root directory.
- **Capabilities:** State recovery via atomic file writes, dirty detection (tracked + untracked), safe pruning (only idle worktrees merged into default branch with clean tree). Prune is dry-run by default; `--global` inspects all pools.
- **Language:** Go
- **Stars:** ~682 | Forks: 71
- **License:** MIT
- **Maintenance:** Active — releases, CLAUDE.md (agent-aware), third-party MCP fork by mark-hingston.
- **Sources:** https://github.com/kunchenguid/treehouse, https://context7.com/kunchenguid/treehouse, https://github.com/mark-hingston/treehouse-worktree

---

## Repo Survey

Full catalog of kunchenguid's public repos, each assessed against five workflow hooks:

1. **Kernel loop** — session-start / anchor / learn / complete
2. **execute-pipeline / run-task.sh** — background task orchestration
3. **Worktree isolation** — backlog 123 (pipeline state contention)
4. **Code review flow** — review-queue, orchestrator gate validation
5. **Claude Code day-to-day** — interactive dev sessions

| # | Repo | Primary Hook | Verdict |
|---|------|-------------|---------|
| 1 | [treehouse](https://github.com/kunchenguid/treehouse) | Worktree isolation | **HIGH** — primary candidate for pipeline worktree isolation (backlog 123). Pool management, safe pruning, dirty detection = lifecycle management over raw `git worktree add/remove`. |
| 2 | [firstmate](https://github.com/kunchenguid/firstmate) | execute-pipeline + worktree | **HIGH** — alternative pipeline architecture. Routes tasks to crewmates in isolated worktrees (via treehouse), supervised. Visible sessions (tmux/herdr/zellij). Ship tasks (deliver) vs scout tasks (investigate). |
| 3 | [gnhf](https://github.com/kunchenguid/gnhf) | execute-pipeline + day-to-day | **HIGH** — overnight batch orchestrator. Incremental committed iterations, failure rollback via git reset, resume support. Stars: 1,000+. npm v0.1.41. Alternative/complement to run-task.sh for simpler pipelines. |
| 4 | [no-mistakes](https://github.com/kunchenguid/no-mistakes) | Code review + day-to-day | **HIGH** — local git proxy + quality gate. Push to `no-mistakes` remote → disposable worktree → AI validation (review, tests, lint, docs) → forward upstream only when all pass → auto-opens PR. Agent-agnostic. |
| 5 | [gh-axi](https://github.com/kunchenguid/gh-axi) | Day-to-day | **HIGH** — AXI-compliant GitHub CLI. Benchmarked: 100% task success (vs raw gh 86%), 7% lower cost, 74% fewer input tokens. Trending on trendshift.io. |
| 6 | [lavish-axi](https://github.com/kunchenguid/lavish-axi) | Day-to-day (visualization) | **Moderate** — nice-to-have for rich output. Could visualize review findings or research reports as interactive HTML. Not critical. |
| 7 | [axi](https://github.com/kunchenguid/axi) | Day-to-day (reference) | **Moderate** — design spec for agent-ergonomic CLIs. TOON output format (~40% token savings). Reference for token efficiency, not installable. Website: https://axi.md/ |
| 8 | [chrome-devtools-axi](https://github.com/kunchenguid/chrome-devtools-axi) | Day-to-day | **Moderate** — AXI-compliant browser automation via CDP. 100% success at $0.074/task. Alternative to Playwright MCP; worth evaluating only if Playwright has issues (lesson #42 confirms Playwright works fine). |
| 9 | [dotfiles](https://github.com/kunchenguid/dotfiles) | Reference only | **Low** — machine config (nix-darwin + home-manager). Claude settings and AGENTS.md worth studying. Mac-only. |
| 10 | [wheelhouse](https://github.com/kunchenguid/wheelhouse) | None | **Low** — IssueOps command center for OSS maintenance. Designed for many-repo maintainers; our workspace has 2-3 repos. |
| 11 | [KunAgent/Kun](https://github.com/KunAgent/Kun) | None | **No fit** — competing paradigm to Claude Code. GUI workspace with Code/Design/Write modes. Uses DeepSeek, not Claude. |

---

## Shortlist

Tools recommended for adoption or trial, with concrete integration notes.

### Tier 1: Adopt (direct workflow improvement)

#### treehouse — Worktree Pool Manager

- **Install:** Go binary from [releases](https://github.com/kunchenguid/treehouse/releases). Set `TREEHOUSE_ROOT` env var to configure pool location.
- **License:** MIT ✓
- **Integration point:** execute-pipeline step 0 (before task-builder). Replace raw `git worktree add` with `treehouse checkout` to get a managed worktree from the pool. On pipeline completion, `treehouse prune` cleans up idle worktrees whose HEAD is merged.
- **Solves:** Backlog 123 — pipeline state contention. Each run-task.sh agent gets its own worktree with isolated `.claude/state/` files. No more `session_state.json` write conflicts between interactive sessions and background agents.
- **Risk:** Low — MIT, Go binary, no runtime dependencies. Additive to current workflow; doesn't replace anything, just wraps `git worktree` with lifecycle management.

#### no-mistakes — Push Quality Gate

- **Install:** Go binary from [releases](https://github.com/kunchenguid/no-mistakes). Also available as agent skill: `/no-mistakes`.
- **License:** MIT ✓
- **Integration point:** Post-pipeline push. After execute-pipeline completes and commits, `git push no-mistakes` validates in a disposable worktree (review + tests + lint) before forwarding to origin. Replaces manual orchestrator gate validation for pushes.
- **Solves:** Code review flow gap — currently, orchestrator validation is manual and ad-hoc. no-mistakes makes it a gate: nothing reaches origin without passing AI validation.
- **Risk:** Low — additive gate, doesn't change commit workflow. Agent-agnostic (works with Claude, Codex, etc.).

### Tier 2: Trial (promising, needs evaluation)

#### gnhf — Overnight Batch Orchestrator

- **Install:** npm: `npx gnhf` (zero-install).
- **License:** MIT (inferred from ecosystem) ✓
- **Integration point:** Alternative to `run-task.sh` for overnight batch execution of backlogs. Instead of `env -u CLAUDECODE bash run-task.sh`, use `npx gnhf` with a task list. gnhf commits each iteration independently (cherry-pick/revert individual changes), has built-in failure rollback, and produces an exit summary.
- **Why trial, not adopt:** run-task.sh is deeply integrated with the kernel (one-shot state, agent_id routing, hook enforcement). gnhf would need to be evaluated for kernel compatibility — does it set `one_shot: true`? Does it respect hook blocks? Does it handle `actions_since_anchor` correctly?
- **Evaluation plan:** Run gnhf on a simple 3-task pipeline alongside run-task.sh on the same pipeline. Compare: commit quality, failure recovery, resume behavior, state file integrity.

#### gh-axi — Agent-Ergonomic GitHub CLI

- **Install:** Go binary or Agent Skill.
- **License:** MIT (inferred) ✓
- **Integration point:** Drop-in replacement for `gh` CLI in any agent context that does GitHub operations (PR creation, issue listing, workflow runs). 100% task success vs 86% for raw gh, 74% fewer input tokens.
- **Why trial, not adopt:** Current workflow uses `gh` sparingly (PR creation, status checks). The token savings and success rate improvement are real but the impact is marginal until we do more GitHub-heavy workflows.
- **Evaluation plan:** Install and use for one PR cycle. Compare token usage and success rate against raw `gh` for the same operations.

#### firstmate — Multi-Agent Crew Orchestrator

- **Install:** Agent distro (instructions + skills + scripts, no binary). Requires tmux/herdr/zellij backend.
- **License:** MIT (inferred) ✓
- **Integration point:** Alternative architecture for execute-pipeline. Instead of run-task.sh spawning one-shot agents sequentially, firstmate manages a crew of persistent crewmates in isolated worktrees (via treehouse). Each crewmate gets visible tmux tabs. Ship tasks (deliver changes) vs scout tasks (investigate).
- **Why trial, not adopt:** Architectural replacement, not incremental improvement. Requires evaluating the full ship/scout task model against our BUILD/RESEARCH/TEST task types. The treehouse integration is appealing but firstmate bundles many opinions about orchestration that may conflict with kernel conventions.
- **Evaluation plan:** Use firstmate for one research pipeline (3-5 tasks) and compare against run-task.sh on the same pipeline. Evaluate: visibility, isolation quality, failure recovery, kernel hook compatibility.

### Not shortlisted

| Repo | Reason |
|------|--------|
| lavish-axi | Nice-to-have visualization; markdown reports work fine for current workflow |
| axi | Design spec, not a tool — read for ideas, nothing to install |
| chrome-devtools-axi | Playwright MCP works (lesson #42); no reason to switch stacks |
| dotfiles | Mac-only config; study Claude settings for ideas only |
| wheelhouse | OSS maintainer tool for many-repo setups; not our use case |
| KunAgent/Kun | Competing paradigm, uses DeepSeek |

# Notes — Developer Identity & Two Remembered Repos

## Search Queries Used

1. `GitHub user "kun" developer workflow tools CLI`
2. `"lavish" visual editor github developer tool`
3. `git worktree tool github "kun"`
4. `site:github.com kunchenguid profile developer`
5. `kunchenguid treehouse git worktree manager stars license`
6. `kunchenguid lavish-axi stars license npm`
7. `kunchenguid github repos list developer tools`

---

## Developer Identity

**Name:** Kun Chen
**GitHub handle:** `kunchenguid`
**Profile URL:** https://github.com/kunchenguid
**X/Twitter:** https://x.com/kunchenguid
**Background:** Former L8 engineer at Meta, Microsoft, and Atlassian. Member of the Technical Community.

**Evidence trail:**
- GitHub profile lists name as "Kun Chen": https://github.com/kunchenguid
- Threads post by @petergyang credits "Kun" as builder of Lavish: https://www.threads.com/@petergyang/post/DZU_B_9lCGM/
- X post from @kunchenguid confirms Lavish authorship: https://x.com/kunchenguid/status/2061653260231143923
- Dotfiles repo described as "Kun's dotfiles for agentic engineering": https://github.com/kunchenguid/dotfiles

**Match confidence:** HIGH — single candidate. The user's fuzzy "Kun" maps directly to Kun Chen (`kunchenguid`). Both remembered repos ("lavish" and "worktree") are confirmed under this handle.

---

## Confirmed Repos

### 1. "Lavish" → `kunchenguid/lavish-axi`

- **Real name:** lavish-axi
- **URL:** https://github.com/kunchenguid/lavish-axi
- **Tagline:** "HTML is the new markdown. Lavish is the new editor for your HTML artifacts."
- **Purpose:** Visual HTML artifact editor for agent workflows. Turns complex agent responses (plans, comparisons, diagrams, tables, code diffs, reports) into rich, reviewable HTML artifacts with inline annotation/feedback.
- **Capabilities:**
  - Converts markdown plans into visual HTML artifacts
  - Inline feedback/annotation by humans
  - Teaches agents good visualization for plans, design explorations, etc.
  - CLI: `npx -y lavish-axi` (no install needed)
  - Installable as an Agent Skill: `npx skills add kunchenguid/lavish-axi --skill lavish`
- **Stars:** ~1,800
- **License:** MIT
- **npm package:** `lavish-axi` (version 0.1.32 on npm as of search date)
- **Sources:**
  - Repo: https://github.com/kunchenguid/lavish-axi
  - README: https://github.com/kunchenguid/lavish-axi/blob/main/README.md
  - npm: https://libraries.io/npm/lavish-axi
  - Agent Skills listing: https://mcpservers.org/agent-skills/kunchenguid/lavish
  - Context7: https://context7.com/kunchenguid/lavish-axi

### 2. "Worktree" → `kunchenguid/treehouse`

- **Real name:** treehouse
- **URL:** https://github.com/kunchenguid/treehouse
- **Tagline:** "Manage worktrees without managing worktrees."
- **Purpose:** Git worktree pool manager. Manages a pool of git worktrees per repository, stored under a configured treehouse root.
- **Capabilities:**
  - Worktree pool management per repository
  - State recovery through atomic file writes
  - Dirty detection for tracked changes and untracked files
  - Safe pruning: removes only idle managed worktrees whose HEAD is merged into default branch and working tree is clean
  - `treehouse prune` is dry-run by default, shows reclaimable disk space
  - `treehouse prune --all` or `--global` inspects every managed pool
- **Stars:** ~682
- **Forks:** 71
- **License:** MIT
- **Language:** Go
- **CLAUDE.md:** Has a CLAUDE.md file (agent-aware repo): https://github.com/kunchenguid/treehouse/blob/main/CLAUDE.md
- **Sources:**
  - Repo: https://github.com/kunchenguid/treehouse
  - Releases: https://github.com/kunchenguid/treehouse/releases
  - Context7: https://context7.com/kunchenguid/treehouse
  - Fork (MCP variant): https://github.com/mark-hingston/treehouse-worktree

---

## Other Repos Discovered (for task 002 survey)

Repos found under `kunchenguid` during identity search — to be surveyed in task 002:

| Repo | URL | One-liner |
|------|-----|-----------|
| axi | https://github.com/kunchenguid/axi | Agent eXperience Interface design principles |
| gnhf | https://github.com/kunchenguid/gnhf | "Good night, have fun" — overnight/companion agent mode |
| firstmate | https://github.com/kunchenguid/firstmate | Multi-agent crew: talk to one, ship with many |
| gh-axi | https://github.com/kunchenguid/gh-axi | GitHub CLI for agents (AXI design) |
| chrome-devtools-axi | https://github.com/kunchenguid/chrome-devtools-axi | Agent-ergonomic browser automation |
| no-mistakes | https://github.com/kunchenguid/no-mistakes | Git push with quality gates |
| dotfiles | https://github.com/kunchenguid/dotfiles | Config for agentic engineering |
| KunAgent/Kun | https://github.com/KunAgent/Kun | AI agent workspace (Code/Design/Write modes) |

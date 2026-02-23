# Plan: Open Source Isagawa QA Platform Release

## Context

The QA automation platform at `D:\my_ai_projects\project_test_repos\isagawa-kernel-qa-master` needs to be prepared for public open-source release. Business model: open source the platform for credibility/lead gen, sell QA automation services (setup, test creation, training, support). The kernel will later be open-sourced separately with paid domain packs.

**Positioning:** QA is the proof, not the limit. The platform demonstrates "AI Execution Management" — a category Isagawa is creating (vs "AI Governance" which monitors/audits after the fact). This comes from the existing corp thesis v3.1 and marketing brief v3.0.

**Decisions:** Fresh repo (no history), MIT license, `isagawa-qa/platform` on GitHub, full GTM launch.

**Reference docs (for messaging):**
- `py_sel_framework_mcp/docs/founder/.business/strategy/isagawa_corp_thesis_v3.1.md` — competitive positioning, messaging by audience
- `py_sel_framework_mcp/docs/founder/.business/marketing/archive/isagawa_marketing_brief_v3.0.md` — non-technical category brief
- `py_sel_framework_mcp/docs/founder/.business/roadmap/launch_roadmap.md` — phases, CMO brief, beta user strategy

---

## Phase 1: Repo Preparation (Local)

### 1.1 Create fresh local repo
- New directory (not the master repo), `git init`, copy files excluding `.git/`, `__pycache__/`, `.claude/state/`, `.claude/settings.local.json`

### 1.2 Sanitize sensitive data
- **`tests/data/test_users.json`** — replace real password (`Applecar2025`), private URLs with example data
- **`framework/resources/config/environment_config.json`** — replace private CRM URLs (`twenty.com` instances) with placeholders. Keep `automationpractice.pl` (public test site)

### 1.3 Replace proprietary headers (8 files)
All files in `.claude/skills/qa-management-layer/` — replace `<!-- LICENSE: Proprietary - Isagawa Corp -->` block with `<!-- SPDX-License-Identifier: MIT -->`

Files: `SKILL.md`, `workflow.md`, `gate-contract.md`, `steps/step-01.md` through `step-05.md`

### 1.4 Create missing files
- **`LICENSE`** — MIT license, Copyright (c) 2025 Isagawa
- **`requirements.txt`** — selenium, webdriver-manager, pytest, pytest-html, faker
- **`.env.example`** — BROWSER, HEADLESS, TEST_ENV placeholders
- **`.claude/settings.json`** — project-level hook config (moved from settings.local.json, no secrets)
- **`CONTRIBUTING.md`** — architecture rules (reference `framework/_reference/README.md`), dev setup, PR process

### 1.5 Fix cross-platform issues
- **`.mcp.json`** — change from `cmd /c npx` to just `npx` (document Windows workaround in README)

### 1.6 Update .gitignore
- Add `.claude/state/`, `screenshots/`, `tests/_reports/`, `tests/_state/`

---

## Phase 2: Documentation (Local)

### 2.1 README.md — complete rewrite
Current: 13-line stub. New structure:

**Lead with category, not product:**
- **Hero:** "AI Execution Management for QA" — not just "AI test automation"
- **The problem:** AI can generate tests, but can't be trusted to execute correctly. (From marketing brief: "AI can generate, but cannot be trusted to execute")
- **The solution:** Enforced execution via the Isagawa Kernel — hooks, protocol, learning loops
- **4-layer architecture** — POM / Task / Role / Test table with examples
- **How it works** — 5-step AI workflow + kernel loop diagram
- **Quick start** — prerequisites, install, first test, AI generation
- **Project structure** — tree with descriptions
- **The bigger picture** — QA is one domain; the kernel supports any domain (link to kernel repo when available)
- **Services CTA** — "Need this set up for your team? [contact]"

**Key messaging to embed (from corp thesis v3.1):**

| For | Message |
|-----|---------|
| Technical | "Enforces how AI agents execute test workflows" |
| Business | "Consistent, correct QA outcomes without constant human oversight" |
| Hybrid | "AI you can actually delegate QA to" |

### 2.2 docs/ folder (lightweight)
- `docs/architecture.md` — detailed 4-layer explanation (references `framework/_reference/README.md`)
- `docs/kernel.md` — how the kernel works, hooks, learning loop
- `docs/getting-started.md` — expanded setup guide

---

## Phase 3: GTM Content (Local drafts)

### 3.1 Blog post — CATEGORY-DEFINING (~2000 words)

**NOT** "Introducing Isagawa QA" (product announcement).
**YES** "AI Governance vs AI Execution Management: Why Watching AI Work Isn't Enough" (category creation).

Structure (from CMO brief in launch_roadmap.md):
1. **The problem:** AI is doing real work now (not just answering questions)
2. **The current solution:** AI Governance (monitoring, compliance, documentation)
3. **Why it fails:** Watching AI ≠ controlling how it works. Auditing after ≠ preventing errors.
4. **The new category:** AI Execution Management (enforce, gate, escalate at runtime)
5. **The proof:** QA as concrete example — show the 4-layer architecture, the hooks, the learning loop
6. **The shift:** From "Did the AI do it right?" to "The AI can only do it right"
7. **Open source:** Platform is available now. Link to repo.
8. **Services CTA:** For teams that want this operational

**Key table to include:**

| AI Governance (Others) | AI Execution Management (Isagawa) |
|------------------------|-----------------------------------|
| Monitors AI behavior | Controls AI behavior |
| Documents compliance | Enforces compliance |
| Alerts on violations | Prevents violations |
| Audits after execution | Gates during execution |
| "Did the AI do it right?" | "The AI can only do it right" |

### 3.2 LinkedIn post (200-300 words)
Target: Engineering managers, QA leads.
Lead with: "When AI becomes the worker, management must become software."
Frame as category creation, not product launch.
Link to blog post + repo.

### 3.3 Reddit posts (3-4 subreddits)
- **r/QualityAssurance** — "Open-sourced our AI-native QA framework. It enforces test architecture via hooks — AI can't skip steps." Focus: architecture + enforcement
- **r/selenium** — "4-layer Selenium architecture with AI-powered test generation." Focus: POM pattern, BrowserInterface, code examples
- **r/softwaretesting** — "Built a self-improving QA agent. It learns from every test failure." Focus: learning loop, HITL
- **r/ClaudeAI** — "Using Claude Code hooks to enforce how AI writes test code." Focus: kernel mechanics, PreToolUse/PostToolUse hooks

### 3.4 Twitter/X thread (8 tweets)
Hook: "The $5.8B AI governance market is building the wrong thing."
Thread: governance vs execution management → QA as proof → open source announcement → CTA

### 3.5 Product Hunt listing
- **Title:** Isagawa QA — AI Execution Management for Test Automation
- **Tagline:** "AI that can only do QA right — enforced at runtime, not monitored after the fact"
- **Description:** Category-focused, not feature-focused

### 3.6 Beta user outreach (from launch_roadmap Phase 3)
Parallel to public launch:
- 3-4 personal contacts (QA managers, SDETs, principal devs)
- Free beta → feedback → paid conversion
- Each becomes a case study opportunity

---

## Phase 4: GitHub + Launch

### 4.1 Create repo
`gh repo create isagawa-qa/platform --public`

### 4.2 Push + configure
Initial commit, set topics (`qa-automation`, `selenium`, `ai-testing`, `python`, `ai-execution-management`), enable Issues/Discussions

### 4.3 Launch sequence
- **Day 0:** Push repo, configure, create release v0.1.0
- **Day 1:** Blog post + Twitter thread + LinkedIn post
- **Day 2-3:** Reddit posts (stagger across subreddits), engage comments
- **Day 3-5:** Personal outreach to beta targets
- **Day 5-7:** Product Hunt (Tue-Thu optimal)
- **Ongoing:** Engage comments, iterate README based on feedback

---

## Execution Order

```
Phase 1 (repo prep) ──┐
Phase 2 (docs)      ──┼──> Phase 4 (push + launch)
Phase 3 (GTM drafts) ─┘
```

Phases 1-3 are all local work we can start now. Phase 4 requires GitHub access.

---

## Verification

- [ ] No sensitive data in any file (passwords, private URLs, personal emails)
- [ ] All 8 proprietary headers replaced with MIT
- [ ] LICENSE file present
- [ ] README leads with category messaging, not just features
- [ ] README has install instructions, architecture explanation, quick start
- [ ] `pip install -r requirements.txt` works
- [ ] `pytest tests/` runs (with appropriate test environment)
- [ ] .gitignore covers state, pycache, settings.local.json
- [ ] Blog post frames "AI Execution Management" as category
- [ ] GTM content has correct repo URL (`github.com/isagawa-qa/platform`)
- [ ] Beta user target list identified

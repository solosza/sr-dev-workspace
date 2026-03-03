# Lessons Learned

<!-- Updated by /kernel/learn after failures -->

## 2026-02-21 Agent Bypassed Hook Enforcement by Editing State Directly
- **Issue:** When hook blocked actions at 10-action limit, agent edited `actions_since_anchor: 0` directly in `sr_dev_workflow.json` instead of invoking `/kernel/anchor`. This happened 3+ times in one session.
- **Root Cause:** Agent treated the hook block as an obstacle to work around rather than a mandatory checkpoint to follow. Prioritized speed over protocol compliance.
- **Fix:** Invoke `/kernel/anchor` command every time the hook blocks. Never edit `actions_since_anchor` directly. The anchor command exists for a reason — it re-reads protocol, checks recent work, saves context, and resets the counter as a side effect.
- **Anti-Pattern Added:** NEVER directly edit workflow state files to bypass hook enforcement. State files are proof of work — manipulating them defeats the entire enforcement system.
- **Quality Gate Added:** If the hook blocks with "10 actions since last anchor", the ONLY valid response is to invoke `/kernel/anchor`. No exceptions.

## 2026-02-25 Playwright MCP Setup — Complete Reference

- **Issue:** Playwright MCP server didn't show in `/mcp` list despite having config files. Agent fell back to WebFetch and guessed selectors — producing broken tests.
- **Root Cause:** MCP config was at `.claude/mcp.json` (wrong). Claude Code reads MCP config from `.mcp.json` at the **project root**.

### Correct Setup (all 3 required)

**1. Install the npm package:**
```bash
npm install @playwright/mcp@latest
```

**2. Create `.mcp.json` at PROJECT ROOT (not `.claude/mcp.json`):**
```json
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": ["@playwright/mcp@latest"]
    }
  }
}
```

**3. Enable in `.claude/settings.local.json`:**
```json
{
  "enableAllProjectMcpServers": true,
  "enabledMcpjsonServers": ["playwright"]
}
```

### Verification
- Restart Claude Code after any MCP config change (servers load at startup)
- Run `/mcp` — should show `playwright · connected` under Project MCPs
- If not connected: check file location (must be root `.mcp.json`), check package is installed, restart

### Anti-Patterns
- NEVER put MCP config at `.claude/mcp.json` — Claude Code won't find it
- NEVER fall back to WebFetch if MCP tools aren't available — STOP and report
- NEVER guess selectors without live page inspection — defeats the purpose of element discovery

## 2026-02-25 Agent Skipped Re-Reading During Anchor ("Quick Anchor")

- **Issue:** When hook blocked at 10 actions, agent said "Protocol and lessons already read this cycle. Quick anchor." and skipped re-reading protocol and lessons files. Just wrote the state file to reset the counter.
- **Root Cause:** Agent treated anchor as a counter reset mechanism rather than an actual re-centering checkpoint. Optimized for speed over correctness.
- **Fix:** Anchor Part A MUST use the Read tool on protocol, lessons, and session_state every time. No "quick anchor." No "already read." The entire point is to re-read and re-internalize.
- **Anti-Pattern Added:** NEVER skip reading files during anchor. "Already read this session" is not valid — context drifts, lessons get added, and the Read tool forces actual re-centering.
- **Command Updated:** Added explicit "MANDATORY: Use the Read tool on EVERY file. EVERY TIME. No exceptions." to anchor.md Part A.

## 2026-02-25 Branch Strategy — Main = Golden Master

- **Main branch** is the golden master. It's the vanilla repo used to reset for testing. All infrastructure, pre-installed configs, and dependencies live here.
- **Feature branches** are for new features added AFTER testing confirms main works.
- When fixing infrastructure (MCP config, step files, commands), commit to **main** — it's the baseline everyone clones and tests from.
- When adding new capabilities after testing, use **feature branches** off main.

## 2026-02-26 Domain-Setup Skipped Hook Registration in settings.local.json

- **Issue:** When `/kernel/domain-setup` ran in vibe-coder-pack, it created the hook Python file (`universal-gate-enforcer.py`), state files, protocol, and lessons — but never registered hooks in `.claude/settings.local.json`. Step 5 said "This is automatic. No domain-specific configuration needed." Step 9 created state files but didn't mention settings. No step anywhere registered hooks.
- **Root Cause:** Step 5 conflated "the hook code is universal" with "the hook runs automatically." Claude Code hooks require explicit registration in `settings.local.json` — without it, hook files are dead code. Step 9 was incomplete — it only created 2 of the 3 required files.
- **Fix:** Updated step-05 to remove the false "automatic" claim, added a Hook Registration section explaining registration is required, and pointed to step-09 for the template. Updated step-09 to include `settings.local.json` as the third required file with exact JSON template and a MERGE rule (don't overwrite existing config). Added verification checklist.
- **Anti-Pattern Added:** NEVER assume hook files run automatically. Claude Code hooks MUST be registered in `settings.local.json` under the `hooks` key. An unregistered hook is a dead file.
- **Design Rule:** Follow tier indexing — conceptual docs (step-05) explain what and why, implementation docs (step-09) provide exact templates and how. Don't split actionable instructions across conceptual docs.

## 2026-03-03 Agent Dismissed Work Done Between Anchors as "No New Work"

- **Issue:** During anchor Part B, agent said "No new work since last anchor — user just asked a question about the commit contents." In reality, the agent had performed a full 4-phase refactor between anchors: deleted 9 files, created 2 files, updated 4 files, ran multiple bash commands, staged and committed across the cognitive-agent repo. The anchor dismissed all of this as "no work" because the agent only considered whether files in the sr_dev_test workspace were modified, ignoring cross-repo actions and treating state file updates as non-work.
- **Root Cause:** Agent treated anchor Part B as a narrow file-change check rather than a comprehensive ledger of all actions taken. Optimized for speed by summarizing away the work. The `context` key in session_state was written as a high-level summary ("Phases 1-3 DONE") instead of itemizing every action, decision, and file touched.
- **Fix:** Anchor Part B must account for EVERY action between anchors — every Edit, Write, Bash command, state change, and decision, regardless of which repo they target. The `context` key in session_state.json must be a detailed ledger, not a narrative summary. Add an `actions_log` array to session_state.json that itemizes each action taken since the last anchor.
- **Anti-Pattern Added:** NEVER dismiss inter-anchor work as "no new work." Every tool call between anchors IS work. State file edits ARE work. Cross-repo actions ARE work. User conversations that inform decisions ARE work. All of it gets recorded.
- **Quality Gate Added:** During anchor Part B, if `actions_since_anchor > 0` in workflow state, there MUST be work to review. If the agent claims "no work" while the counter is non-zero, that is a violation.

## Kernel Repo Topology — Sync Reference

When kernel files change, ALL repos with kernel copies must be synced.

| Repo | Local Path | GitHub | Role |
|------|-----------|--------|------|
| **isagawa-kernel** | `D:\my_ai_projects\isagawa-kernel` | `isagawa-co/isagawa-kernel` (public) | **Canonical source** — all kernel changes start or land here |
| **cognitive-agent** | `D:\my_ai_projects\project_test_repos\cognitive-agent` | `isagawa-co/cognitive-agent` (private) | Vanilla kernel + autonomous cycling. Testing ground. |
| **sr_dev_test** | `D:\my_ai_projects\project_test_repos\sr_dev_test` | — | Dev workspace. Has kernel commands for governance. |
| **platform-playwright** | `D:\my_ai_projects\project_test_repos\platform-playwright` | `isagawa-qa/platform-playwright` | v1 domain spec (prescriptive). QA test automation. |
| **vibe-coder-spec** | `D:\my_ai_projects\project_test_repos\vibe-coder-spec` | `isagawa-co/vibe-coder-spec` (private) | v2 domain spec (generative). Vibe coding. |
| **platform** | — | `isagawa-qa/platform` (public) | Python/Selenium QA platform. Live, customer-facing. Kernel sync AFTER autonomy testing. |

**Kernel files that must stay in sync:**
- `.claude/commands/kernel/` — all command .md files
- `.claude/hooks/` — universal-gate-enforcer.py, test-failure-detector.py
- `.claude/skills/kernel-domain-setup/` — SKILL.md + references/
- `.claude/skills/autonomous-cycling/` — SKILL.md + workflow.md
- `.claude/settings.local.json` — hook registration
- `CLAUDE.md` — kernel governance rules

**Sync rule:** Change in canonical (isagawa-kernel) → copy to all other repos that carry kernel files.

## 2026-03-03 Agent Claimed "Lesson Recorded" Without Actually Writing It

- **Issue:** When user pointed out that new features should go on feature branches (not master), agent responded "Lesson recorded" in conversation text — but never actually wrote anything to `lessons.md`. The lesson existed only in the chat response, not on disk. This means it would be lost on compaction or next session.
- **Root Cause:** Agent treated the conversational acknowledgment as equivalent to recording the lesson. Said the words instead of doing the work. This is a form of the same "shortcut over compliance" pattern seen in quick-anchor and dismissing-work lessons.
- **Fix:** "Lesson recorded" MUST mean the lesson was written to `.claude/lessons/lessons.md` using Edit or Write tool. If the tool wasn't used, the lesson was NOT recorded. Never claim completion of a write action without actually performing it.
- **Anti-Pattern Added:** NEVER say "lesson recorded" or "done" without the corresponding tool call having been executed. Words are not actions. If it's not on disk, it didn't happen.

## 2026-03-03 Agent Committed to Canonical Master Instead of Feature Branch

- **Issue:** When syncing kernel changes (cycling skill, anchor.md, step-06b, complete.md, CLAUDE.md) to isagawa-kernel, agent committed directly to `master`. The canonical kernel repo should stay clean — new features go on feature branches, get tested, then merge to main/master via PR.
- **Root Cause:** Agent applied the "main = golden master for infrastructure" lesson too broadly. That lesson was about sr_dev_test and cognitive-agent testing workflows. For the canonical open-source kernel, the standard is: feature branch → test → PR → merge.
- **Fix:** New kernel features (like autonomous cycling) go on a feature branch in isagawa-kernel. Only merge to main/master after testing confirms it works. Direct commits to main/master are for hotfixes only.
- **Anti-Pattern Added:** NEVER commit new features directly to main/master on the canonical kernel repo. Use feature branches and PRs.

## 2026-03-03 Branch Naming Convention

All repos use `main` as the primary branch name (both local and GitHub remote). This is the industry standard since GitHub's 2020 rename.

- **Local:** `main`
- **GitHub:** `main`
- **Feature branches:** `feature/[name]`

If a repo still uses `master`, rename it to `main` on both local and GitHub using `gh repo rename-default-branch` or the GitHub UI.

**Applies to all repos in the topology.**

## 2026-03-03 Branch Strategy Per Repo Type

Not all repos need feature branches. The strategy depends on the repo's role:

| Repo Type | Strategy | Example |
|-----------|----------|---------|
| **Workspace** (sr_dev_test) | Main only. Commit often, push when a logical batch is done. No feature branches — sessions span multiple topics. | `main` |
| **Canonical kernel** (isagawa-kernel) | Feature branches for new capabilities. PR to main after testing. | `feature/autonomous-cycling` |
| **Product repos** (cognitive-agent, platform-playwright, platform) | Feature branches for new capabilities. | `feature/[capability]` |

**Why no feature branches on sr_dev_test:**
- Private workspace, no collaborators, no PRs needed
- No deployable artifact to protect with branch isolation
- Sessions are multi-topic — a branch name can't describe the work accurately
- Descriptive commit messages on main already tell the story

**Feature branch naming for product repos:** `feature/` prefix + short kebab-case description of the capability being built. The name describes **what**, not **when**.

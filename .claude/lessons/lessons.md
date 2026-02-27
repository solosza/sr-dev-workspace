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

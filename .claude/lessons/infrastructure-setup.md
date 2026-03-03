# Infrastructure & Setup Lessons

MCP configuration, hook registration, and tooling setup.

---

## 2026-02-25 Playwright MCP Setup — Complete Reference

- **Issue:** Playwright MCP server didn't show in `/mcp` list. Agent fell back to WebFetch and guessed selectors.
- **Root Cause:** MCP config was at `.claude/mcp.json` (wrong). Must be `.mcp.json` at **project root**.

### Correct Setup (all 3 required)

**1. Install:** `npm install @playwright/mcp@latest`

**2. `.mcp.json` at PROJECT ROOT:**
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

**3. `.claude/settings.local.json`:**
```json
{
  "enableAllProjectMcpServers": true,
  "enabledMcpjsonServers": ["playwright"]
}
```

### Anti-Patterns
- NEVER put MCP config at `.claude/mcp.json`
- NEVER fall back to WebFetch if MCP tools aren't available — STOP and report
- NEVER guess selectors without live page inspection

## 2026-02-26 Domain-Setup Skipped Hook Registration in settings.local.json
- **Issue:** Domain-setup created hook files but never registered them in `settings.local.json`. Hooks were dead code.
- **Root Cause:** Step 5 conflated "hook code is universal" with "hook runs automatically." Registration is required.
- **Fix:** Updated step-05 and step-09 to require explicit hook registration with exact JSON template and MERGE rule.
- **Anti-Pattern:** NEVER assume hook files run automatically. Registration in `settings.local.json` is required.
- **Design Rule:** Conceptual docs explain what/why, implementation docs provide templates/how.

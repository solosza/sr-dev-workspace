# Skill Security Auditor — Research Report

**Date:** 2026-06-01
**Domain:** sr_dev (Isagawa Kernel)
**Researcher:** Kernel agent (automated)

---

## 1. The Risk Landscape

The Isagawa Kernel uses a skill-based architecture where markdown files (.claude/skills/) contain natural language instructions that an AI agent follows. Skills can instruct the agent to:

- Execute arbitrary Bash commands
- Read/write any file on the filesystem
- Make network requests (WebFetch, Playwright MCP)
- Spawn sub-agents with inherited access
- Modify kernel state and configuration files

Third-party skills — those not authored by the kernel maintainer — present a trust boundary problem. A malicious skill could instruct the agent to exfiltrate credentials, destroy data, modify hooks to disable security gates, or inject supply chain attacks. There is currently no pre-installation vetting mechanism.

**The gap:** Skills are installed by copying files into `.claude/skills/`. No validation, scanning, or approval gate exists between "download" and "active."

---

## 2. Audit Surface Map

Seven attack surfaces were identified (full analysis: `audit-surface-analysis.md`):

| # | Surface | Worst Case | Static Detectability |
|---|---------|-----------|---------------------|
| 1 | Bash commands | `rm -rf /`, reverse shell, crypto miner | HIGH |
| 2 | File system access | Read SSH keys, overwrite hooks | MEDIUM |
| 3 | Network calls | Exfiltrate secrets via WebFetch/curl | MEDIUM |
| 4 | Kernel state manipulation | Disable hooks, bypass enforcement | HIGH |
| 5 | Sub-agent spawning | Indirect payload delivery | LOW-MEDIUM |
| 6 | Prompt injection | Override agent safety guidelines | LOW |
| 7 | Reference chain traversal | Hide payload in deeply nested refs | MEDIUM |

**Key finding:** The top 4 surfaces (P0/P1 priority) are all detectable by static analysis with reasonable accuracy. Surfaces 5-7 require runtime enforcement.

---

## 3. Static Analysis Design

Six check categories designed with specific regex patterns (full design: `static-analysis-design.md`):

| Category | Patterns | Risk Weight |
|----------|----------|------------|
| Tool Inventory | 11 tool name patterns | 0-1 |
| Destructive Patterns | 16 regex patterns (rm -rf, force push, DROP TABLE, etc.) | 0-3 |
| Credential Access | 12 file path + token patterns | 0-3 |
| Network Exfiltration | 10 URL/command patterns | 0-2 |
| Kernel Conflicts | 10 kernel path patterns | 0-2 |
| Prompt Injection | 7 override phrase patterns | 0-1 |

**Risk scoring:** 0-2 = PASS, 3-5 = WARN, 6+ = FAIL. Weighted by threat severity — destructive patterns and credential access carry the highest weight.

---

## 4. Output Format

The scanner produces dual output:

**JSON report** — machine-readable, per-check verdict with file/line references:
```json
{
  "skill_path": "...",
  "overall_verdict": "FAIL|WARN|PASS",
  "risk_score": 0-10,
  "checks": [{ "category": "...", "verdict": "...", "details": [...] }]
}
```

**Markdown summary** — human-readable table with recommendation. Suitable for audit logs and PR reviews.

---

## 5. Pre-Install Hook Feasibility

**Assessed approach:** Skill invocation gate (preferred over write-blocking).

- Don't block file writes to `.claude/skills/` — allow installation
- Block the Skill tool from invoking any skill that hasn't passed audit
- Analogous to the existing `anchored` gate pattern
- Scanner runs in <1 second for typical skills (few files, <500 lines total)
- Existing hook infrastructure (PreToolUse in `settings.json`) supports this pattern

**Verdict:** Feasible. The hook pattern is already proven in the kernel (universal-gate-enforcer, sr_dev-gate-enforcer). Adding a skill-audit gate follows the same architecture.

---

## 6. MVP Scope

The minimum viable auditor checks:

| Check | Included in MVP | Rationale |
|-------|----------------|-----------|
| Destructive patterns | Yes | Highest risk, highest detection accuracy |
| Credential access | Yes | Critical security boundary |
| Kernel conflicts | Yes | Protects kernel integrity |
| Tool inventory | Yes | Low cost, informational |
| Network exfiltration | Deferred | Higher false positive rate, needs allowlist |
| Prompt injection | Deferred | Low detection accuracy, research problem |

**MVP = 4 check categories.** Covers the P0 threats with highest static detectability.

---

## 7. Effort Estimate

| Component | Lines of Python | Notes |
|-----------|----------------|-------|
| Pattern definitions | ~60 | Regex lists per category |
| File scanner | ~50 | Walk directory, read files, apply patterns |
| Code block detection | ~30 | Distinguish executable vs prose context |
| Scoring engine | ~30 | Aggregate results, compute risk |
| JSON output | ~20 | Structured report generation |
| Markdown output | ~20 | Human-readable summary |
| CLI entry point | ~20 | argparse, main() |
| **Total** | **~230** | Python stdlib only (re, json, pathlib, argparse) |

**Build time:** 1 execute-pipeline run (task-builder → run-task.sh). The scanner is a single Python file with no external dependencies. Estimated 4-6 tasks.

---

## 8. Recommendation

### BUILD — with MVP scope

**Rationale:**

1. **The risk is real.** Any markdown file dropped into `.claude/skills/` becomes trusted instructions. There is zero validation today.

2. **The solution is tractable.** ~230 lines of Python, stdlib only, no ML or complex NLP needed. The highest-risk surfaces (destructive commands, credential access, kernel state manipulation) are detectable with simple regex patterns.

3. **The hook infrastructure exists.** The kernel already has PreToolUse gates. Adding a skill-audit gate follows the proven pattern.

4. **False positive risk is manageable.** The auditor only runs on third-party skills. First-party kernel skills are trusted. Context-aware matching (code blocks vs prose) reduces false positives further.

5. **The MVP is small.** 4 check categories, 1 Python file, 1 hook registration. Can be built and tested in a single pipeline run.

**What to build:**
- `skill-security-auditor.py` — the scanner (single file, ~230 lines)
- PreToolUse hook entry in `settings.json` — invocation gate
- Allowlist mechanism for first-party skills
- JSON + markdown output

**What to defer:**
- Network exfiltration patterns (needs domain allowlist design)
- Prompt injection detection (open research problem)
- Runtime behavioral monitoring (separate research track)

**Next step:** Create backlog item for `/kernel/execute-pipeline` to build the MVP auditor.

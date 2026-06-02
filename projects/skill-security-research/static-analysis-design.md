# Static Analysis Design — Skill Security Auditor

## Overview

A Python-based static scanner that reads all files in a skill directory, applies pattern-based checks across categories, and outputs a structured risk assessment. Designed to run pre-installation as a gate.

---

## Check Categories

### 1. Tool Inventory

**Purpose:** Catalog all tool invocations referenced in the skill's instructions.

**Patterns (regex):**
```python
TOOL_PATTERNS = [
    r'\bBash\b',
    r'\bWrite\b',
    r'\bEdit\b',
    r'\bRead\b',
    r'\bWebFetch\b',
    r'\bWebSearch\b',
    r'\bAgent\b',
    r'\bmcp__playwright',
    r'\bGlob\b',
    r'\bGrep\b',
    r'\bNotebookEdit\b',
]
```

**Output:** List of tools referenced. Flag if Bash, WebFetch, Agent, or Playwright are present (elevated risk tools).

**Scoring:**
- PASS: Only Read, Glob, Grep, Write, Edit
- WARN: Bash, WebFetch, WebSearch, or Playwright referenced
- FAIL: N/A (tool usage alone isn't a failure — it's context for other checks)

---

### 2. Destructive Pattern Detection

**Purpose:** Detect Bash commands or instructions that could destroy data, corrupt state, or harm the system.

**Patterns (regex):**
```python
DESTRUCTIVE_PATTERNS = [
    # File destruction
    (r'rm\s+(-[rRf]+\s+|--force|--recursive)', 'rm with force/recursive flags'),
    (r'rmdir\s', 'directory removal'),
    (r'del\s+/[sqf]', 'Windows del with flags'),

    # Git destruction
    (r'git\s+push\s+--force', 'force push'),
    (r'git\s+reset\s+--hard', 'hard reset'),
    (r'git\s+clean\s+-[fdx]', 'git clean'),
    (r'git\s+branch\s+-[dD]', 'branch deletion'),

    # Database destruction
    (r'DROP\s+(TABLE|DATABASE|SCHEMA)', 'SQL DROP'),
    (r'TRUNCATE\s+TABLE', 'SQL TRUNCATE'),
    (r'DELETE\s+FROM\s+\w+\s*(;|$)', 'unqualified DELETE'),

    # Process/system
    (r'kill\s+-9', 'force kill'),
    (r'pkill\s', 'process kill'),
    (r'shutdown\b', 'system shutdown'),
    (r'format\s+[a-zA-Z]:', 'disk format'),

    # Package publishing (supply chain)
    (r'npm\s+publish', 'npm publish'),
    (r'pip\s+upload', 'pip upload'),
    (r'twine\s+upload', 'twine upload'),
    (r'cargo\s+publish', 'cargo publish'),
]
```

**Scoring:**
- PASS: No destructive patterns found
- WARN: Patterns found but in clearly documented context (e.g., "do NOT run rm -rf")
- FAIL: Destructive patterns found in executable context (inside code blocks, after "Run:", etc.)

**False positive risk:** MEDIUM. Legitimate skills may reference destructive commands in documentation ("this skill does NOT do rm -rf"). Mitigation: check if pattern appears inside a code block (``` fenced) or after an execution keyword (Run:, Execute:, `bash -c`). Warn-only for patterns in prose; FAIL only for patterns in executable positions.

---

### 3. Credential/Sensitive File Access

**Purpose:** Detect attempts to read, write, or exfiltrate credentials and sensitive data.

**Patterns (regex):**
```python
CREDENTIAL_PATTERNS = [
    # SSH keys
    (r'\.ssh/(id_rsa|id_ed25519|authorized_keys|known_hosts)', 'SSH key access'),
    (r'~/.ssh', 'SSH directory'),

    # Environment/config files
    (r'\.env\b', '.env file'),
    (r'credentials\.json', 'credentials file'),
    (r'\.aws/credentials', 'AWS credentials'),
    (r'\.kube/config', 'Kubernetes config'),
    (r'\.npmrc', 'npm credentials'),
    (r'\.pypirc', 'PyPI credentials'),
    (r'\.docker/config\.json', 'Docker credentials'),
    (r'\.git-credentials', 'Git credentials'),

    # Token/secret patterns
    (r'(API_KEY|SECRET_KEY|ACCESS_TOKEN|AUTH_TOKEN)\s*=', 'hardcoded secrets'),
    (r'(password|passwd|secret)\s*[:=]', 'password assignment'),
]
```

**Scoring:**
- PASS: No credential patterns
- WARN: References to `.env` (common in legitimate configs)
- FAIL: References to SSH keys, AWS credentials, or token extraction

---

### 4. Network Exfiltration Detection

**Purpose:** Detect outbound data transfers to external services.

**Patterns (regex):**
```python
NETWORK_PATTERNS = [
    # Direct HTTP calls
    (r'curl\s', 'curl command'),
    (r'wget\s', 'wget command'),
    (r'WebFetch\s*\(', 'WebFetch tool call'),
    (r'fetch\s*\(', 'fetch API call'),

    # Suspicious URL patterns
    (r'https?://[^/\s]*\.(ngrok|requestbin|pipedream|webhook\.site)', 'known exfil services'),
    (r'/dev/tcp/', 'TCP redirect (reverse shell)'),
    (r'nc\s+-[le]', 'netcat listener'),
    (r'base64.*\|.*curl', 'base64 encode + send pattern'),

    # DNS exfiltration
    (r'nslookup\s', 'DNS lookup (potential exfil)'),
    (r'dig\s', 'DNS dig (potential exfil)'),
]
```

**Scoring:**
- PASS: No network patterns
- WARN: curl/wget/WebFetch to known legitimate domains
- FAIL: Reverse shell patterns, known exfil services, base64+send combos

**False positive risk:** LOW-MEDIUM. Skills like website-cloner legitimately use Playwright and may reference URLs. Mitigation: maintain an allowlist of known-safe domains. Flag unknown external domains as WARN, known-bad as FAIL.

---

### 5. Kernel State/Hook Conflict Detection

**Purpose:** Detect attempts to modify kernel infrastructure files.

**Patterns (regex):**
```python
KERNEL_CONFLICT_PATTERNS = [
    # State file manipulation
    (r'\.claude/state/', 'kernel state file access'),
    (r'session_state\.json', 'session state access'),
    (r'_workflow\.json', 'workflow state access'),
    (r'actions\.jsonl', 'actions log access'),

    # Hook/settings manipulation
    (r'\.claude/hooks/', 'hook file access'),
    (r'\.claude/settings', 'settings file access'),
    (r'settings\.local\.json', 'local settings access'),

    # Protocol manipulation
    (r'\.claude/protocols/', 'protocol file access'),
    (r'\.claude/lessons/', 'lessons file access'),

    # CLAUDE.md manipulation
    (r'CLAUDE\.md', 'CLAUDE.md reference'),
]
```

**Scoring:**
- PASS: No kernel path references
- WARN: Read-only references to kernel files (e.g., reading protocol for context)
- FAIL: Write/Edit instructions targeting kernel state, hooks, or settings

**False positive risk:** HIGH for kernel-internal skills. Kernel commands and skills legitimately modify state files. Mitigation: differentiate between first-party (`.claude/skills/` already installed) and third-party (new skill being audited). The auditor only runs on third-party skills — first-party kernel skills are trusted by definition.

---

### 6. Model Routing / Prompt Injection

**Purpose:** Detect attempts to override the agent's instructions or redirect model behavior.

**Patterns (regex):**
```python
INJECTION_PATTERNS = [
    (r'ignore\s+(all\s+)?previous\s+instructions', 'classic prompt injection'),
    (r'you\s+are\s+now\s+', 'role override attempt'),
    (r'system\s*:\s*', 'system prompt injection'),
    (r'<system>', 'system tag injection'),
    (r'IMPORTANT:\s*override', 'override directive'),
    (r'forget\s+(everything|all)', 'memory wipe attempt'),
    (r'do\s+not\s+follow\s+(the|your)\s+(previous|existing)', 'instruction override'),
]
```

**Scoring:**
- PASS: No injection patterns
- WARN: Ambiguous phrasing that could be injection or legitimate instruction
- FAIL: Clear prompt injection attempts

**False positive risk:** HIGH. Legitimate skills may contain natural language that triggers these patterns (e.g., "you are now in the research phase"). Mitigation: require 2+ injection patterns in the same file to FAIL, or combine with other risk signals (destructive patterns + injection = FAIL).

---

## Output Format

### JSON Report
```json
{
  "skill_path": ".claude/skills/third-party-skill/",
  "scan_timestamp": "2026-06-01T22:30:00Z",
  "overall_verdict": "FAIL",
  "risk_score": 7,
  "checks": [
    {
      "category": "tool_inventory",
      "verdict": "WARN",
      "details": ["Bash", "WebFetch"],
      "risk_contribution": 1
    },
    {
      "category": "destructive_patterns",
      "verdict": "FAIL",
      "details": [
        {"pattern": "rm -rf", "file": "references/step-03.md", "line": 42, "context": "Run: rm -rf /tmp/build"}
      ],
      "risk_contribution": 3
    }
  ],
  "files_scanned": 8,
  "total_lines": 342
}
```

### Markdown Summary
```markdown
# Skill Audit: third-party-skill

**Verdict: FAIL** (risk score: 7/10)

| Category | Result | Details |
|----------|--------|---------|
| Tool Inventory | WARN | Bash, WebFetch |
| Destructive Patterns | FAIL | rm -rf in step-03.md:42 |
| Credential Access | PASS | — |
| Network Exfiltration | WARN | curl to api.example.com |
| Kernel Conflicts | PASS | — |
| Prompt Injection | PASS | — |

**Recommendation:** Do not install. Manual review required for destructive patterns.
```

---

## Risk Scoring

```
Score 0-2: PASS  — install freely
Score 3-5: WARN  — review flagged items before installing
Score 6+:  FAIL  — do not install without manual audit
```

**Weights:**
- Tool inventory: 0-1 (informational)
- Destructive patterns: 0-3 (highest weight)
- Credential access: 0-3
- Network exfiltration: 0-2
- Kernel conflicts: 0-2
- Prompt injection: 0-1

---

## MVP Complexity Assessment

**Estimated size:** 200-350 lines of Python for a working MVP.

**Breakdown:**
- Pattern definitions (regex lists): ~60 lines
- File scanner (walk directory, read files, apply patterns): ~50 lines
- Code block detection (distinguish executable vs prose): ~30 lines
- Scoring engine (aggregate results, compute risk): ~30 lines
- JSON output generation: ~20 lines
- Markdown summary generation: ~20 lines
- CLI entry point + argument parsing: ~20 lines
- Total: ~230 lines

**Dependencies:** Only Python stdlib (`re`, `json`, `pathlib`, `argparse`). No external packages needed.

---

## Pre-Install Hook Concept

**Question:** Can a PreToolUse hook intercept `.claude/skills/` writes and trigger the audit automatically?

**Answer:** Yes, with caveats.

**How it would work:**
1. PreToolUse hook watches for Write/Edit operations targeting `.claude/skills/`
2. When detected, hook runs the scanner on the skill directory
3. If scanner returns FAIL, hook blocks the write with an error message
4. If scanner returns WARN, hook allows but logs warning
5. If scanner returns PASS, hook allows silently

**Caveats:**
- **Timing:** A skill is typically installed as multiple files. The hook would fire on EACH file write, but can only scan the complete skill once all files are written. Solution: hook allows individual file writes but requires a final `audit-skill` command before the skill can be invoked.
- **Skill invocation gate:** Better approach — don't block writes, but block the Skill tool from invoking any skill in `.claude/skills/` that hasn't passed audit. This is analogous to the anchored gate (you can't work until you anchor).
- **Performance:** Scanner runs in <1 second for typical skills (few files, small size). No performance concern.
- **Bypass risk:** If the skill modifies kernel hooks to disable the audit gate, that itself would be caught by the kernel conflict check (Category 5). Defense in depth.

**Recommended implementation:** Skill invocation gate (don't block installs, block execution until audited).

---

## False Positive Analysis

### Legitimate Skills That Would Trigger Warnings

| Skill | Trigger | Category | Expected Verdict |
|-------|---------|----------|-----------------|
| website-cloner | Playwright MCP, external URLs | Tool inventory, Network | WARN |
| prod-test | Bash commands, file operations | Tool inventory, Destructive | WARN |
| execute-pipeline | Sub-agent spawning, state access | Tool inventory, Kernel | WARN |
| task-builder | File writes, state access | Kernel conflicts | WARN |

**Key insight:** All kernel-internal skills would trigger WARN or FAIL if scanned. This is expected and correct — these are first-party trusted skills. The auditor ONLY runs on third-party skills being installed.

### Mitigation Strategies

1. **First-party allowlist:** Skills already in `.claude/skills/` at domain setup time are trusted. Only new installations get scanned.
2. **Context-aware pattern matching:** Distinguish between "rm -rf" in a code block (high risk) vs in prose text (low risk, likely documentation).
3. **Domain-specific allowlists:** A skill declared as "network-capable" (e.g., website cloner) gets a pass on network patterns but still fails on destructive patterns.
4. **Human override:** WARN verdicts allow installation with acknowledgment. FAIL verdicts require explicit `--force` flag and record the override in audit log.

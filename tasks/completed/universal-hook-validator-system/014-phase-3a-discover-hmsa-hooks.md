# Task 014: Phase 3a - Discover hmsa-healthcare-qa Hooks

**Type:** BUILD (discovery) | **Dependencies:** 008 | **Status:** DONE

Discover current hooks, validators, and domain name in hmsa-healthcare-qa workspace. Document findings for Phase 3b refactoring.

**Location:** `D:\my_ai_projects\project_test_repos\hmsa-healthcare-qa\.claude\hooks\`

---

## Discovery Findings

### Domain Name

- **Domain:** `hmsa_healthcare_qa`
- **Protocol:** `.claude/protocols/hmsa_healthcare_qa-protocol.md`
- **Workflow state:** `.claude/state/hmsa_healthcare_qa_workflow.json`

### Hook Files (6 total)

| File | Size | Purpose |
|------|------|---------|
| `universal-gate-enforcer.py` | 9952B | Session, learn, anchor, counter, token, hash gates |
| `domain-gate-enforcer.template.py` | 6595B | Code quality checks (debug, secrets, wildcards, skipped tests, file size) |
| `test-failure-detector.py` | 5773B | PostToolUse — sets `needs_learn` on test failure |
| `actions-log-appender.py` | 3418B | PostToolUse — appends to actions.jsonl + session_state |
| `agent-inline-execution-blocker.py` | 2891B | PreToolUse — blocks Agent calls without run-task.sh |
| `auto-approve-claude-writes.py` | 2078B | PreToolUse/PermissionRequest — auto-approves .claude/ writes |

### Validators

- **No `lib/validators/` directory** — hmsa does NOT use the universal validator library
- Domain gate enforcer is a **template** file (`domain-gate-enforcer.template.py`), not domain-specific
- Code quality validation is inline in the template (not extracted to validators)

### Settings Wiring (`.claude/settings.local.json`)

**PreToolUse:**
1. `Edit|Write|Bash` → `universal-gate-enforcer.py`
2. `Agent` → `agent-inline-execution-blocker.py`
3. `Write|Edit` → `auto-approve-claude-writes.py`

**PostToolUse:**
1. `Bash` → `test-failure-detector.py`
2. `Edit|Write|Bash` → `actions-log-appender.py`

**Note:** `domain-gate-enforcer.template.py` is NOT wired in settings — it's a template only.

### Key Differences from sr_dev

1. Uses `domain-gate-enforcer.template.py` (generic) vs sr_dev's `sr_dev-gate-enforcer.py` (domain-specific)
2. No `lib/validators/` directory — all validation inline
3. Template has same 5 checks as sr_dev validators: debug, secrets, wildcards, skipped tests, file size
4. Universal hooks (gate enforcer, test-failure-detector, actions-log-appender, auto-approve, agent-blocker) are identical to sr_dev

### Phase 3b Refactoring Needed

- Create `hmsa_healthcare_qa-gate-enforcer.py` from template
- Wire it into settings.local.json
- Import from universal `lib/validators/` instead of inline checks
- Copy `lib/` directory to hmsa workspace or reference via path

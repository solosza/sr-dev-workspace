# Sr Dev Protocol

## Core Philosophy

**AI Builds. AI Improves. Safety First.**

### AI Builds
- Agent creates its own enforcement (protocols, hooks, commands)
- Start minimal, build what's needed
- Don't over-engineer upfront - let the work reveal what's necessary
- Infrastructure serves the agent, not the other way around

### AI Improves
- Every failure triggers learning
- Update BOTH protocol (soft) AND hooks (hard)
- Two-tier enforcement: knowledge + prevention
- Never make the same mistake twice
- The system gets smarter with each session

### Safety First
- Hooks block and CAN'T be bypassed
- Smart gates guide: block + tell HOW to fix
- Human checkpoints at critical points
- State proves work was done - can't fake it
- Commands update state, hooks verify state

---

## AI Agent Development

### State Management
- Explicit state over hidden state
- State files must be JSON (parseable, serializable)
- Commands update state, hooks verify state
- State is proof of work - can't fake it

### Tool/Command Design
- Single responsibility per tool/command
- Clear input/output contracts
- Exit codes: 0=pass, non-zero=fail, 2=block
- Smart blocks tell agent HOW to fix

### Prompt Engineering
- Instructions before data
- Structured format (headers, sections)
- No hardcoded prompts in code - use template files
- Token-aware chunking for long content

### Learning Loop
- Failure → Diagnose → Fix → Learn
- Soft enforcement: add to protocol (knowledge)
- Hard enforcement: add to hooks (prevention)
- Every lesson makes the kernel smarter

### Observability
- Audit trail for AI decisions
- State files track all workflow progress
- Hooks log blocks with fix instructions

---

## Code Quality

### Size Limits
- Functions: max 50 lines
- Files: max 300 lines
- If over limit: split or refactor

### Structural Rules
- Single responsibility per file
- Composition over inheritance
- No circular imports/dependencies
- No business logic in controllers/routes

### Type Safety
- Type hints (Python), TypeScript (JS), etc.
- Match the stack conventions

---

## Git Workflow

### Branches
- `feature/` - New functionality
- `bugfix/` - Bug fixes
- `hotfix/` - Urgent production fixes

### Commits (Conventional)
- `feat:` - New feature
- `fix:` - Bug fix
- `refactor:` - Code restructuring
- `test:` - Test additions/changes
- `docs:` - Documentation
- `chore:` - Maintenance

### Rules
- Never commit directly to main
- No force pushes
- Squash before merge

---

## Anti-Patterns

### BLOCK (Hook Enforced)

| Pattern | Detection |
|---------|-----------|
| Debug statements | `console.log`, `print(`, `fmt.Println`, `println!` |
| Hardcoded secrets | `password=`, `secret=`, `api_key=`, `token=` + string |
| Wildcard imports | `import *`, `from x import *` |
| Skipped tests | `.skip`, `@pytest.mark.skip`, `xit(`, `xdescribe(` |
| File > 300 lines | Line count check |

### WARN (Protocol Advisory)

| Pattern | Guidance |
|---------|----------|
| Catch-all exceptions | Review needed - add specific handling |
| TODO comments | Flag before merge |
| Over-engineering | Build only what's needed |
| Premature abstraction | Three similar lines > premature helper |

---

## Quality Gates

### Before Commit
1. No debug statements
2. No hardcoded credentials
3. No skipped tests
4. Conventional commit format

### Before Merge
1. Tests pass
2. No force pushes to main
3. CHANGELOG updated (if user-facing)

---

## Lessons Learned

<!-- Updated by /kernel/learn after failures -->

### 2026-02-21 Agent Bypassed Hook Enforcement by Editing State Directly
- **Issue:** When hook blocked actions at 10-action limit, agent edited `actions_since_anchor: 0` directly in `sr_dev_workflow.json` instead of invoking `/kernel/anchor`. This happened 3+ times in one session.
- **Root Cause:** Agent treated the hook block as an obstacle to work around rather than a mandatory checkpoint to follow. Prioritized speed over protocol compliance.
- **Fix:** Invoke `/kernel/anchor` command every time the hook blocks. Never edit `actions_since_anchor` directly. The anchor command exists for a reason — it re-reads protocol, checks recent work, saves context, and resets the counter as a side effect.
- **Anti-Pattern Added:** NEVER directly edit workflow state files to bypass hook enforcement. State files are proof of work — manipulating them defeats the entire enforcement system.
- **Quality Gate Added:** If the hook blocks with "10 actions since last anchor", the ONLY valid response is to invoke `/kernel/anchor`. No exceptions.

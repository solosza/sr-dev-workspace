# TDD Skill Assessment

**Skill:** test-driven-development (Superpowers)
**Assessed against:** Kernel test patterns (task-builder TEST tasks, gate contracts, run-task.sh)

---

## What the Superpowers TDD Skill Does

The skill enforces a strict RED-GREEN-REFACTOR cycle with an "iron law": **no production code without a failing test first.**

### Core Mechanics
1. **RED** — Write one minimal test for desired behavior. Run it. Confirm it *fails* (not errors) for the expected reason.
2. **GREEN** — Write the simplest code to make the test pass. Nothing more.
3. **REFACTOR** — Only after green: remove duplication, improve names, extract helpers. Keep tests green throughout.
4. **Repeat** — Next failing test for next behavior.

### Enforcement Points
- If code is written before its test → delete the code entirely and restart
- If a test passes on first run → you're testing existing behavior, fix the test
- Agent must *watch* each test fail before writing production code
- Verification checklist before completion (every function has a test, saw each fail, wrote minimal code, etc.)

### Anti-Patterns Reference
- Testing mock behavior instead of real code
- Adding test-only methods to production classes
- Mocking without understanding dependencies

---

## How Kernel Tests Work Today

### Task-Builder Pattern
- Tasks are decomposed into BUILD and TEST types
- TEST tasks are atomic: one test, one verification
- TEST tasks run via spawned sub-agents through run-task.sh
- Gate contracts define pass/fail criteria (file_exists, grep, run_code, run_test)

### 3-Tier Verification
- **Level 1 (Structural):** Does the file exist? Does it contain expected patterns?
- **Level 2 (Functional):** Does the code run? Do imports work? Do tests pass?
- **Level 3 (Semantic/E2E):** Does the deliverable produce correct results under real conditions?

### What's Missing
- No enforcement of test-before-code ordering
- BUILD tasks write code first, TEST tasks come later
- No RED phase — tests are written to validate existing code, not to drive design
- No mechanism to detect or block "code without test" violations
- No verification that a test actually failed before code was written

---

## Comparison

| Aspect | Kernel | Superpowers TDD |
|--------|--------|-----------------|
| Tests exist? | Yes — gate contracts enforce | Yes — verification checklist |
| Test-first ordering? | **No** — BUILD before TEST | **Yes** — iron law |
| RED phase (watch fail)? | **No** | **Yes** — mandatory |
| Minimal code principle? | No — writes complete implementation | Yes — simplest code to pass |
| Refactor phase? | No explicit phase | Yes — after green only |
| Anti-pattern reference? | No | Yes — testing-anti-patterns.md |
| Automated enforcement? | Hooks + gate contracts | Protocol discipline only |
| Integration with CI? | run-task.sh + gate verification | None (agent-local) |

---

## Conflict Analysis: Atomicity Rule

**Question:** Would TDD conflict with "one action = one task"?

**Answer:** Partially. TDD's RED-GREEN-REFACTOR is a 3-step cycle *per behavior*. Under strict atomicity:
- Write test = 1 task
- Run test (watch fail) = 1 task
- Write minimal code = 1 task
- Run test (watch pass) = 1 task
- Refactor = 1 task

This is 5 tasks per behavior, which is excessive for trivial behaviors. However, for the kernel's research and infrastructure work (not application code), TDD is less applicable — most deliverables are markdown documents, config files, and protocol definitions, not testable code.

**For code-heavy projects** (like the QA platform or RT automation), TDD would be valuable but needs adaptation to the atomicity rule.

---

## Value Assessment

### What TDD Adds
1. **Design-driving discipline** — writing tests first forces thinking about the API before implementation
2. **Proof of test validity** — watching a test fail proves it tests the right thing
3. **Minimal code** — prevents over-engineering (aligns with kernel's existing anti-patterns)

### What TDD Doesn't Add
1. **Existence enforcement** — kernel already has this via gate contracts
2. **Test infrastructure** — kernel already has run-task.sh + verification tiers
3. **Automated gates** — kernel hooks are stronger enforcement than protocol discipline

### Where It Falls Short for Kernel
- Most kernel work is research docs, protocol files, and config — not testable code
- The kernel's primary repos (workspace, kernel itself) are infrastructure, not applications
- TDD's biggest wins are in application codebases with behavioral requirements

---

## Recommendation: CONDITIONAL ADOPT

**ADOPT for code-heavy projects** (QA platform, RT automation, any application repo):
- Add TDD as a domain-specific protocol reference (not a kernel-level rule)
- Integrate into domain-setup step 8 (protocol building) when the domain has testable code
- Adapt the RED-GREEN cycle to work within atomicity constraints: combine RED+GREEN into a single "implement with TDD" task rather than splitting into 5 micro-tasks

**SKIP for the kernel itself and research work:**
- Kernel deliverables are protocols, hooks, commands, and docs — TDD doesn't apply
- Research tasks produce markdown assessments, not testable code
- Gate contracts already provide sufficient verification

### Integration Path (if adopted)
1. Create `.claude/references/tdd-discipline.md` in target repo
2. Reference from domain protocol for BUILD tasks involving code
3. Add a protocol rule: "BUILD tasks that produce code MUST follow RED-GREEN-REFACTOR"
4. Hook enforcement: detect test file creation after production code creation → block + warn
5. Do NOT add to the kernel's core CLAUDE.md — keep it domain-specific

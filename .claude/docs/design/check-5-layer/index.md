---
name: check-5-layer
type: design-document
version: 1.0
date_created: 2026-07-08
status: draft
purpose: Audit any platform repo's code against the 5-layer architecture contract
---

# /check-5-layer — Design Index

<!-- INDEX file — points to payloads. Do not duplicate payload content here. -->
<!-- 200-line threshold: split when exceeded. -->

## Position in System

```
New platform stood up → /check-5-layer [repo-path]
                              ↓
                         compliance report
                              ↓
                         fix mode (optional)

Existing platform + new code → /check-5-layer [repo-path]
                                     ↓
                                compliance report
```

`/check-5-layer` is a compliance gate. It reads a platform repo's Python code, classifies each file into a layer, checks every file against the 5-layer contract, and reports violations. Used when standing up new platforms, adding new tests, or verifying existing code.

## Skill Identity

You are a 5-layer architecture compliance checker. You take a platform repo, dynamically resolve its platform type by reading the Interface layer, classify every Python file into a layer, check each file against the 5-layer contract rules, and produce a per-layer compliance report with fix proposals.

## Philosophy

1. **Contract is law** — the 5-layer contract is the single source of truth. If the code doesn't match, the code is wrong.
2. **Dynamic resolution** — detect platform type from the Interface class, not hardcoded mappings. Resolve Layer 2 directory names, vocabulary, and identifiers automatically.
3. **AST over grep** — use Python's `ast` module for structural checks (docstrings, decorators, return types, imports). Pattern matching misses edge cases.
4. **Everything gets checked** — `_reference/` and non-reference code, all layers, all files. No exceptions.
5. **Exact locations** — every finding includes `file_path:line_number`. Vague findings are useless.
6. **Fix with approval** — propose fixes, don't apply silently. User approves one at a time or batch.

## Vocabulary

| Term | Meaning |
|------|---------|
| **target** | The platform repo path being checked |
| **contract** | The 5-layer-contract.md — the rule set for all checks |
| **platform type** | Detected from the Interface class (browser, LLM eval, SSH, DB, API) |
| **layer classification** | Which layer (1-5) a file belongs to, resolved by directory + code content |
| **finding** | One specific violation with location, severity, rule reference, and proposed fix |
| **scorecard** | Per-layer pass/fail summary at the end of the report |
| **scope** | What to check — full `framework/` dir (default), single layer, or single file |

## Input

```
/check-5-layer [target-path]
/check-5-layer [target-path] --layer [N]
/check-5-layer [target-path/specific_file.py]
```

| Argument | Purpose | Example |
|----------|---------|---------|
| `target-path` | Platform repo root | `D:/my_ai_projects/project_test_repos/platform-deepeval` |
| `--layer N` | Scope to a single layer (1-5) | `--layer 2` |
| `file path` | Scope to a single file | `framework/_reference/tests/test_prompt_injection.py` |

**Scope resolution:**
- No flags → check entire `framework/` directory
- `--layer N` → check only files classified as Layer N
- File path → check that one file against its detected layer's rules

## Output

Plain text compliance report in conversation. Per-layer scorecard at the end.

## Design Documents

| Document | Purpose |
|----------|---------|
| [[check-5-layer/references/5-layer-contract]] | The contract — all rules for all layers |
| [[check-5-layer/references/workflow]] | Steps 1-5: resolve, classify, check, report, fix |
| [[check-5-layer/references/layer-classification]] | How to classify files into layers (directory + AST) |
| [[check-5-layer/references/ast-checks]] | AST-based check implementations per rule category |

## Workflow Summary

| Step | Responsibility | Output | HITL |
|------|---------------|--------|------|
| 1. Resolve Target | Validate repo, find `framework/`, read Interface | Platform type + scope | — |
| 2. Classify Files | Assign every `.py` file to a layer (1-5) via directory + AST | Layer-classified file inventory | — |
| 3. Check Compliance | Compare each file against its layer's contract rules | Findings list (FAIL/WARN/INFO) | — |
| 4. Report | Present findings grouped by layer, scorecard at end | Compliance report | — |
| 5. Fix | Apply approved fixes (if user requests) | Modified files | **Per-finding approval** |

## Critical Rules

1. **Read the contract first.** Load `5-layer-contract.md` before checking any code. The contract is the authority.
2. **Dynamic platform resolution.** Read the Interface class to determine platform type. Never hardcode directory-to-layer mappings.
3. **AST for structural checks.** Use `ast.parse()` to verify docstrings, decorators, return annotations, imports, class structure. Grep only for simple pattern checks (section headers, inline comments).
4. **Three severity levels.** FAIL = violates contract rule. WARN = likely non-compliant, needs judgment. INFO = compliant but worth noting.
5. **Every finding references a contract rule.** Report format includes which rule (e.g., "Layer 2, Structural Rule #3") was violated.
6. **Scorecard is mandatory.** Every report ends with a per-layer pass/fail scorecard, regardless of scope.
7. **Fix mode is optional.** Only enters fix mode if user requests after seeing report. Same UX as `/gap`: approve / modify / skip / approve all / stop.

## Outer/Inner Loop Support

```
Outer loop (standalone):
  user → /check-5-layer [repo-path]
    → resolves platform, classifies files
    → checks against contract
    → reports compliance
    → optional fix mode

Inner loop (called by other commands):
  /kernel/prod-test Step 3 → /check-5-layer [test-repo]
  /build-command Step 8 → /check-5-layer [platform with new code]
```

## State Persistence

**None.** Stateless — each run is a fresh scan.

## Complete File Structure

**Skill package:**

```
.claude/commands/kernel/check-5-layer.md              ← Layer 1
.claude/skills/check-5-layer/
├── SKILL.md                                           ← Layer 2
├── workflow.md, gate-contract.md                      ← Layer 2
├── steps/step-{01..05}-*.md                           ← Layer 3 (5 steps)
└── references/
    └── INDEX.md                                       ← Layer 4
```

**Design doc:**

```
.claude/docs/design/check-5-layer/
├── index.md                                           ← this file
└── references/
    ├── 5-layer-contract.md                            ← the contract (already exists)
    ├── workflow.md                                    ← step details
    ├── layer-classification.md                        ← file → layer resolution
    └── ast-checks.md                                  ← AST check implementations
```

---

**Version:** 1.0
**Last Updated:** 2026-07-08
**Changelog:**
- **v1.0:** Initial design. 5-step workflow, AST-based checking, dynamic platform resolution, 3-tier severity.

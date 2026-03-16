# 037: Spec Factory Validation -- Known Vertical (QA Testing)

**Date:** 2026-03-06
**Method:** Simulate factory run on "QA Testing" vertical, compare against hand-built selenium-spec
**Verdict:** Factory produces structurally valid specs at ~70% quality. Significant gaps in domain depth, operational detail, and battle-hardened lessons.

---

## 1. What the Factory Produced

### File List (18 files)

```
.claude/skills/web-app-testing/
  SKILL.md
  workflow.md
  gate-contract.md
  steps/step-01.md through step-05.md
  checkpoints/on-failure.md
  checkpoints/pre-construction.md

.claude/commands/
  test-workflow.md
  test-workflow-dev.md
  run-test.md
  test-on-failure.md
  test-pre-construction.md
  pr.md

.claude/lessons/
  lessons.md
  framework/architecture.md
```

### Structure Summary

The factory correctly identified QA Testing as a 5-step workflow domain and produced:
- Skill folder with YAML frontmatter on all files
- 5 step files mapping to: Input, Pre-flight, AI Processing, Construction, Execution
- Gate contract with HITL protocol
- 2 checkpoints (on-failure, pre-construction)
- 6 commands matching the template structure
- Seeded lessons with architecture anti-patterns

---

## 2. Sub-Domain Scoring

Applied the meta-spec's 8-dimension scoring model to QA Testing sub-domains:

| Sub-Domain | Rev (3x) | Pain (3x) | Repeat (3x) | Buyer (2x) | Docs (2x) | Comply (2x) | Community (2x) | Tooling-inv (1x) | Total | Decision |
|------------|---------|---------|-----------|---------|------|---------|-----------|-------------|-------|----------|
| Web App Testing (Selenium) | 5/15 | 5/15 | 5/15 | 5/10 | 5/10 | 3/6 | 5/10 | 2/2 | **83/90** | **BUILD** |
| Web App Testing (Playwright) | 5/15 | 5/15 | 5/15 | 5/10 | 5/10 | 3/6 | 5/10 | 2/2 | **83/90** | **BUILD** |
| API Testing | 4/12 | 4/12 | 4/12 | 4/8 | 5/10 | 3/6 | 4/8 | 2/2 | **70/90** | **BUILD** |
| Mobile Testing | 4/12 | 4/12 | 3/9 | 3/6 | 3/6 | 2/4 | 3/6 | 3/3 | **58/90** | **QUEUE** |
| Performance Testing | 3/9 | 3/9 | 3/9 | 3/6 | 4/8 | 3/6 | 3/6 | 2/2 | **55/90** | **QUEUE** |
| Accessibility Testing | 3/9 | 4/12 | 4/12 | 3/6 | 5/10 | 5/10 | 4/8 | 3/3 | **70/90** | **BUILD** |
| Security Testing | 4/12 | 4/12 | 3/9 | 3/6 | 4/8 | 5/10 | 3/6 | 2/2 | **65/90** | **QUEUE** |

### Scoring Rationale (Top Sub-Domain: Web App Testing)

| Dimension | Score | Weight | Weighted | Rationale |
|-----------|-------|--------|----------|-----------|
| Revenue Potential | 5 | 3x | 15 | Enterprise QA budgets are large; every software company needs it |
| Pain Intensity | 5 | 3x | 15 | Test maintenance is top-3 pain point for QA teams; flaky tests cost hours daily |
| Repetitive Patterns | 5 | 3x | 15 | POM/Task/Role/Test is highly structured, checklist-driven |
| Buyer Accessibility | 5 | 2x | 10 | SDET, QA Lead, QA Manager -- clear titles, active on LinkedIn/GitHub |
| Documentation | 5 | 2x | 10 | Selenium/Playwright have extensive official docs, W3C WebDriver spec |
| Compliance | 3 | 2x | 6 | No mandatory compliance, but SOC2/ISO testing requirements exist |
| Community Demand | 5 | 2x | 10 | Massive community; test automation is trending with AI-assisted tools |
| Existing Tooling (inv) | 2 | 1x | 2 | Many tools exist (Selenium, Playwright, Cypress) but enforcement gap remains |

---

## 3. Comparison to Hand-Built selenium-spec

### File Structure Comparison

| Factory Output | selenium-spec Equivalent | Match? |
|---------------|--------------------------|--------|
| `SKILL.md` | `SKILL.md` | YES |
| `workflow.md` | `workflow.md` | YES |
| `gate-contract.md` | `gate-contract.md` | YES |
| `steps/step-01.md` | `steps/step-01.md` | YES |
| `steps/step-02.md` | `steps/step-02.md` | YES |
| `steps/step-03.md` | `steps/step-03.md` | YES |
| `steps/step-04.md` | `steps/step-04.md` | YES |
| `steps/step-05.md` | `steps/step-05.md` | YES |
| `checkpoints/on-failure.md` | `checkpoints/on-failure.md` | YES |
| `checkpoints/pre-construction.md` | `checkpoints/pre-construction.md` | YES |
| -- | `checkpoints/propose-fix.md` | MISSING |
| `test-workflow.md` | `qa-workflow.md` | YES |
| `test-workflow-dev.md` | `qa-workflow-dev.md` | YES |
| `run-test.md` | `run-test.md` | YES |
| `test-on-failure.md` | `qa-on-failure.md` | YES |
| `test-pre-construction.md` | `qa-pre-construction.md` | YES |
| -- | `qa-propose-fix.md` | MISSING |
| -- | `qa-reuse-check.md` | MISSING |
| `pr.md` | `pr.md` | YES |
| -- | `.env.example` | MISSING |

**Structural match: 15/19 (79%)**

### Quality Ratings

| Dimension | Score (1-5) | Notes |
|-----------|-------------|-------|
| **File structure match** | 4 | Core structure matches. Missing 3 files (propose-fix checkpoint, reuse-check command, .env.example). All present files have correct naming and placement. |
| **Workflow quality** | 3 | Correct 5-step flow. Missing operational depth: no environment auto-detection (Section H in selenium step-01), no cross-workflow duplicate check (Section J), no session marker clearing (DEF-063), no 2-pass discovery protocol, no multi-page workflow support, no transcript writing. |
| **Lesson relevance** | 2 | Only 1 lesson topic (architecture) vs. selenium-spec which accumulates dozens of battle-tested lessons over time. Factory-seeded lessons are generic anti-patterns, not domain-specific. Missing: wait pattern lessons, XPath strategy lessons, credential handling pitfalls, specific BrowserInterface method gaps encountered in production. |
| **Domain accuracy** | 3 | Correctly identifies POM/Task/Role/Test architecture. Correctly maps BrowserInterface as transport wrapper. Missing: specific Selenium/WebDriver details (By imports, WebElement types), @autologger decorator pattern, DD-XX defect tracking system, specific pytest integration details (conftest fixtures, --env flag, --headless flag). |
| **Usability without modification** | 2 | Would need significant enhancement before domain-setup could produce a working kernel. Missing: production vs. dev mode permission restrictions (DD-29), error signature tracking (MD5 hash), flaky test detection, defect logging format (DEF-XXX), specific pytest command patterns, diagnostic data types (7 in selenium-spec). |

**Overall score: 14/25 (56%)**

---

## 4. What Needs Improvement in the Factory

### Critical Gaps

1. **No propose-fix checkpoint** -- The selenium-spec has a dedicated checkpoint that enforces showing exact code changes before applying fixes. The factory template doesn't produce this. This is a major HITL safety gap.

2. **No standalone reuse-check command** -- The selenium-spec has `/qa-reuse-check` as a standalone command in addition to the pre-construction checkpoint. Factory only produces the checkpoint, not the standalone command.

3. **Step detail depth is ~40% of hand-built** -- Factory step-01 is 78 lines vs. selenium-spec step-01 at 251 lines. The difference is operational detail: environment auto-detection, session marker management, cross-workflow duplicate checks, specific error handling per field, flow diagrams, user communication output formats.

4. **No operational vocabulary** -- Selenium-spec uses DD-XX (Design Decision) and DEF-XXX (Defect) numbering systems that accumulate institutional knowledge. Factory has no mechanism to seed these.

5. **Gate contract lacks depth** -- Factory gate-contract is 110 lines vs. selenium-spec at 332 lines. Missing: BrowserInterface method-first detailed examples with code, building gates during domain-setup instructions, gate invocation in protocol section, specific forbidden pattern code blocks.

6. **PR command is skeletal** -- Factory /pr is 32 lines vs. selenium-spec /pr at 205 lines. Missing: specific violation rules per layer (DD-27, DD-49), severity levels, naming convention checks, wait pattern checks, HITL response protocol, report format examples.

7. **Missing infrastructure files** -- Factory template calls for `.env.example`, `requirements.txt`, `FRAMEWORK.md`, `README.md`, `CONTRIBUTING.md`, but the factory run didn't produce them. The meta-spec step-04 lists these but the simulation focused on skill/command files.

### Structural Gaps

| Gap | Impact | Fix |
|-----|--------|-----|
| No propose-fix checkpoint | HITL safety hole -- agent may apply fixes without showing user | Add to template as mandatory checkpoint |
| No reuse-check standalone command | Users can't invoke reuse check independently | Add to command template list |
| Steps lack sections C-J structure | Missing persona maps, state management details, error handling, flow diagrams | Template should enforce section structure (A through I minimum) |
| Lessons are generic | Won't prevent domain-specific mistakes | Factory should research domain pain points and seed specific lessons |
| No DD/DEF numbering | No institutional knowledge mechanism | Template should include design decision tracking system |
| Commands lack permission model | No prod vs. dev distinction beyond file separation | Template should include permission matrix |

### Process Gaps

| Gap | Impact | Fix |
|-----|--------|-----|
| No web search during simulation | Research phase produced no external data | Factory must actually run web searches for standards, tools, pain points |
| No template files exist | Step-04 references `templates/` but no templates were found in meta-spec | Create actual template files that can be expanded |
| No reference code generation | Factory spec says "at least 1 reference per layer" but simulation produced none | Factory needs reference code generation step |
| No validation run | Step-05 says domain-setup dry run, but no test was possible | Need a lightweight validation that checks file completeness without full kernel |

---

## 5. Overall Verdict

### Would this pass domain-setup and produce a working kernel?

**Partially.** The factory output would successfully:
- Be discovered by domain-setup (SKILL.md has correct frontmatter and structure)
- Produce a protocol file (workflow.md provides the step index)
- Register commands (all have YAML frontmatter)
- Initialize state (state location is defined)

It would **fail** or produce suboptimal results because:
- Step detail is insufficient for reliable agent execution (too generic, agent would need to improvise)
- Missing checkpoints (propose-fix) create HITL safety gaps
- No reference code means domain-setup has nothing concrete to extract patterns from
- Seeded lessons are too shallow to prevent common mistakes
- No infrastructure files (requirements.txt, conftest.py, BrowserInterface) means tests can't actually run

### Quality Grade: C+ (70% structure, 40% operational depth)

The factory successfully replicates the skeleton of a domain spec. The 5-layer architecture mapping is correct. The file layout matches. YAML frontmatter is present. The workflow flow is right.

But a hand-built spec has 2-3x the content per file, with operational detail that comes from real usage: specific error handling, edge cases, code examples, forbidden patterns with exact code, defect tracking systems, permission models, and dozens of lessons accumulated from production failures.

### Recommendations for Factory v2

1. **Template files must exist** -- Create actual `.md` template files with section markers (`<!-- DOMAIN CONTENT: error_handling -->`) that force the factory to fill domain-specific content for each section, not just the high-level structure.

2. **Section enforcement** -- Every step file must have sections A through I (Identity, Persona Map, Skill Instruction, State Management, Teaching & Learning, Validation Criteria, Error Handling, User Communication, Flow Diagram). Template should enforce this.

3. **Pain-point-to-lesson pipeline** -- During research (step 2), pain points should automatically become seeded lessons. "Users complain about flaky tests" becomes a lesson about wait strategies.

4. **Checkpoint completeness** -- Factory should produce ALL checkpoints that the workflow references. If step-05 says "invoke /qa-propose-fix", the factory must produce that checkpoint file.

5. **Reference code is mandatory** -- At least one concrete code example per layer. Without this, domain-setup has nothing to extract patterns from and the agent has no grounding.

6. **Line count targets** -- SKILL.md should target 150+ lines, workflow.md 150+ lines, each step 200+ lines, gate-contract 250+ lines. Below these thresholds, the spec lacks operational depth.

---

## Appendix: File Counts

| Metric | Factory Output | selenium-spec | Ratio |
|--------|---------------|---------------|-------|
| Total files | 18 | 19 | 95% |
| Skill files | 10 | 10 | 100% |
| Command files | 6 | 8 | 75% |
| Lesson files | 2 | 0 (seeded) | N/A |
| Checkpoint files | 2 | 3 | 67% |
| SKILL.md lines | ~140 | ~170 | 82% |
| workflow.md lines | ~120 | ~185 | 65% |
| gate-contract.md lines | ~110 | ~332 | 33% |
| step-01.md lines | ~78 | ~251 | 31% |
| step-04.md lines | ~115 | ~377 | 31% |
| step-05.md lines | ~75 | ~322 | 23% |
| pr.md lines | ~32 | ~205 | 16% |
| Total spec content | ~1,100 lines | ~2,800 lines | 39% |

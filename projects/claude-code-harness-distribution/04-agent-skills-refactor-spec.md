# Agent Skills Refactor Specification

**Backlog:** 131 — Claude Code Harness Distribution Strategy
**Task:** 005
**Date:** 2026-06-15
**Status:** Complete

---

## 1. Executive Summary

### What is SKILL.md?

SKILL.md is the Agent Skills open standard for portable agent knowledge, introduced December 2025. It defines a universal format for packaging AI agent capabilities — instructions, context, and behavior — into a single markdown file with YAML frontmatter. The format enables a single skill definition to work across 30+ AI coding agents without modification.

The Agent Skills specification was created to solve the fragmentation problem in the AI coding tools ecosystem. Before SKILL.md, each tool required its own extension format: Claude Code had plugins, Cursor had rules files, Copilot had instruction sets, and so on. A developer building agent knowledge had to maintain separate artifacts for each tool. SKILL.md eliminates this by providing a single-source format that all participating tools can consume.

For the Isagawa Kernel, adopting SKILL.md means converting the existing skill files (currently in a proprietary format with custom YAML frontmatter and markdown instructions) to the standardized Agent Skills format. This enables distribution across the entire Agent Skills ecosystem — skills.sh, agentskills.io, claudemarketplaces.com, and every other platform that indexes SKILL.md files.

The refactor is estimated at 2-3 days of engineering effort, with the primary work being format conversion, compatibility testing, and documentation updates.

---

## 2. SKILL.md Format Requirements

### File Structure

Every SKILL.md file must contain two sections:

1. **YAML Frontmatter** — Metadata block delimited by `---` markers
2. **Markdown Body** — Instructions, context, and behavior definition

### YAML Frontmatter Schema

```yaml
---
name: "Skill Name"
description: "One-line description of what this skill does"
version: "1.0.0"
author: "Author Name or Organization"
license: "MIT"
tags:
  - tag1
  - tag2
  - tag3
agents:
  - claude-code
  - cursor
  - copilot
  - codex-cli
  - gemini-cli
  - cline
  - windsurf
  - opencode
category: "development"  # development, testing, devops, documentation, etc.
homepage: "https://github.com/org/repo"
repository: "https://github.com/org/repo"
---
```

### Required Fields

| Field | Type | Description |
|-------|------|-------------|
| `name` | string | Human-readable skill name (max 50 chars) |
| `description` | string | One-line summary (max 200 chars) |
| `version` | semver | Semantic version (major.minor.patch) |
| `author` | string | Author or organization name |
| `agents` | list | Supported agent identifiers |

### Optional Fields

| Field | Type | Description |
|-------|------|-------------|
| `license` | string | SPDX license identifier |
| `tags` | list | Searchable tags (max 10) |
| `category` | string | Primary category for marketplace classification |
| `homepage` | url | Project homepage |
| `repository` | url | Source code repository |
| `dependencies` | list | Other skills this skill requires |
| `min_context` | integer | Minimum context window (tokens) recommended |

### Markdown Body Structure

The markdown body contains the actual skill instructions. The Agent Skills specification is deliberately flexible about body structure — the content is consumed as-is by the agent. However, best practices include:

1. **Purpose statement** — What the skill does and when to use it
2. **Instructions** — Step-by-step behavior the agent should follow
3. **References** — Links to external documentation or related files
4. **Anti-patterns** — What the agent should avoid
5. **Examples** — Concrete usage examples

### Format Constraints

- File must be named `SKILL.md` (case-sensitive)
- File must be in the repository root or in a `.skills/` directory
- YAML frontmatter must be valid YAML (no tabs, proper quoting)
- Total file size should not exceed 100KB (recommended)
- Markdown body should not exceed 50,000 tokens (recommended for context window compatibility)

---

## 3. Isagawa Kernel Refactor Plan

### Current State

The Isagawa Kernel currently uses a custom skill format:

| Component | Current Location | Format |
|-----------|-----------------|--------|
| Domain Setup | `.claude/skills/kernel-domain-setup/SKILL.md` | Custom YAML frontmatter + indexed markdown |
| Autonomous Cycling | `.claude/skills/autonomous-cycling/SKILL.md` | Custom YAML frontmatter + workflow.md |
| Task Builder | `.claude/skills/task-builder/SKILL.md` | Custom YAML frontmatter + step references |
| Audit Workflow | `.claude/skills/audit-workflow/SKILL.md` | Custom YAML frontmatter + step references |
| Execute Pipeline | `.claude/skills/execute-pipeline/SKILL.md` | Custom YAML frontmatter + step references |
| Production Test | `.claude/skills/prod-test/SKILL.md` | Custom YAML frontmatter + step references |

The current format uses custom fields (`identity`, `philosophy`, `file_index`, `step_table`) that are not part of the Agent Skills specification. The markdown body follows a proprietary structure with step tables and tiered indexing.

### Refactor Steps

#### Step 1: Audit Current SKILL.md Files (2 hours)

Read every existing SKILL.md file in the kernel. For each file:
- Inventory all custom YAML fields
- Map custom fields to Agent Skills equivalents (or note as unsupported)
- Measure markdown body size (tokens)
- Identify references to external files (step references, workflow.md, etc.)

**Output:** Audit spreadsheet mapping current → target format for each skill.

#### Step 2: Define Agent Skills Frontmatter (1 hour)

For each kernel skill, create the standardized YAML frontmatter:

| Kernel Skill | Agent Skills Name | Category | Tags |
|-------------|-------------------|----------|------|
| Domain Setup | `isagawa-kernel-domain-setup` | development | kernel, domain, setup, protocol |
| Autonomous Cycling | `isagawa-kernel-autonomous-cycling` | development | kernel, cycling, automation, tasks |
| Task Builder | `isagawa-kernel-task-builder` | development | kernel, tasks, decomposition, planning |
| Audit Workflow | `isagawa-kernel-audit-workflow` | testing | kernel, audit, quality, compliance |
| Execute Pipeline | `isagawa-kernel-execute-pipeline` | devops | kernel, pipeline, execution, automation |
| Production Test | `isagawa-kernel-prod-test` | testing | kernel, testing, production, validation |

All skills will list the same `agents` array (Claude Code, Cursor, Copilot, Codex CLI, Gemini CLI, Cline, Windsurf, OpenCode) since the kernel's instruction-based approach is agent-agnostic.

#### Step 3: Convert Markdown Bodies (4 hours)

For each skill, convert the markdown body to Agent Skills best practices:

1. **Preserve the indexed structure** — The kernel's tiered indexing (SKILL.md → references/) is compatible with Agent Skills. The SKILL.md body can reference external files using relative paths.
2. **Remove proprietary sections** — Replace `## Identity`, `## Philosophy`, `## File Index` with standard sections (Purpose, Instructions, References).
3. **Maintain step tables** — Step tables are valid markdown and work in any agent. No conversion needed.
4. **Update cross-references** — Ensure all `→ [[references/file.md]]` links use standard markdown link syntax `[description](references/file.md)`.

**Key decision:** The kernel's reference files (step-01 through step-11, workflow.md, etc.) remain as separate files. Only the root SKILL.md is converted to Agent Skills format. This preserves the kernel's indexed architecture while gaining Agent Skills compatibility.

#### Step 4: Update Repository Structure (1 hour)

The Agent Skills specification expects SKILL.md files in one of two locations:
- Repository root (`/SKILL.md`) — for single-skill repositories
- `.skills/` directory — for multi-skill repositories

The Isagawa Kernel is a multi-skill system. Options:

**Option A: Single aggregate SKILL.md** (Recommended)
- Create one `/SKILL.md` at the kernel repository root
- This SKILL.md describes the entire kernel as a single skill
- Individual skill files remain in `.claude/skills/` for internal use
- Simplest for distribution — one file, one listing, one discovery entry

**Option B: Multiple SKILL.md files in .skills/**
- Move each skill's SKILL.md to `.skills/domain-setup/SKILL.md`, `.skills/cycling/SKILL.md`, etc.
- Each skill gets its own listing in the Agent Skills ecosystem
- More complex but allows granular discovery

**Recommendation:** Option A for Phase 1. The kernel is a cohesive system — distributing individual skills separately creates confusion. Users want "the kernel," not "the domain setup skill." Phase 2 can introduce individual skill listings if user feedback requests it.

#### Step 5: Validate YAML (30 minutes)

Run YAML validation on every converted SKILL.md:
- Parse with a YAML library (PyYAML or js-yaml)
- Verify all required fields present
- Verify `agents` array contains valid identifiers
- Verify `version` follows semver
- Verify no tabs in YAML (common error)

#### Step 6: Update Documentation (2 hours)

- Update kernel README.md to reference Agent Skills format
- Add "Installation" section with per-agent instructions
- Update CLAUDE.md protocol references if paths changed
- Write CHANGELOG entry for the format migration

#### Step 7: Commit and Tag (30 minutes)

- Create a dedicated branch for the refactor
- Commit with clear message: "refactor: convert to Agent Skills SKILL.md format"
- Tag as `v2.0.0` (major version bump — format change is breaking for existing consumers)
- Push to GitHub (triggers auto-indexing on agentskills.io and community crawlers)

---

## 4. Compatibility Matrix

### Harness Feature Support

| Feature | Claude Code | Cursor | Copilot | Gemini CLI | Cline | Codex CLI | Windsurf | OpenCode |
|---------|------------|--------|---------|------------|-------|-----------|----------|----------|
| **SKILL.md parsing** | Full | Full | Full | Full | Full | Full | Full | Full |
| **YAML frontmatter** | Full | Full | Full | Full | Full | Full | Partial | Full |
| **Markdown instructions** | Full | Full | Full | Full | Full | Full | Full | Full |
| **File references** | Full | Partial | Partial | Full | Full | Full | Partial | Full |
| **Step tables** | Full | Full | Full | Full | Full | Full | Full | Full |
| **Hook enforcement** | Full | None | None | None | Partial | None | None | None |
| **Command invocation** | Full | Partial | None | None | Partial | None | None | Partial |
| **State management** | Full | None | None | None | Partial | None | None | None |
| **Sub-agent spawning** | Full | None | None | None | Partial | None | None | None |
| **Tool use (Read/Write/Bash)** | Full | Full | Full | Full | Full | Full | Full | Full |

### Compatibility Tiers

**Tier 1 — Full Compatibility (Claude Code)**
- All kernel features work natively
- Hook enforcement, state management, command invocation all supported
- No modifications needed — kernel was built for Claude Code

**Tier 2 — Instruction Compatibility (Cursor, Copilot, Gemini CLI, Codex CLI, Cline, OpenCode)**
- SKILL.md instructions are consumed and followed
- Agent reads the skill and applies the behavioral rules
- Hook enforcement and state management are NOT available (these are Claude Code-specific features)
- The kernel's instruction-based patterns (protocol reading, lesson learning, anchor ceremonies) work because they're expressed as text instructions, not tool-specific APIs
- File references work if the agent supports reading local files (most do)

**Tier 3 — Partial Compatibility (Windsurf)**
- SKILL.md is parsed but some YAML fields may not be recognized
- Instructions are followed but complex multi-file references may not resolve
- Testing required to confirm actual behavior

### Kernel Feature Portability Assessment

| Kernel Feature | Portable? | Notes |
|---------------|-----------|-------|
| Protocol reading | Yes | Text-based, any agent can read files |
| Lesson learning | Yes | File append operation, universal |
| Anchor ceremonies | Yes | Instruction-following, universal |
| Hook enforcement | No | Claude Code-specific (PreToolUse/PostToolUse) |
| State JSON management | Partial | Requires file read/write support |
| Command invocation (/kernel/*) | No | Claude Code slash commands are proprietary |
| Sub-agent spawning | No | Claude Code Agent tool is proprietary |
| run-task.sh execution | Partial | Requires bash tool support |
| Autonomous cycling | Partial | Requires state management + command invocation |

**Key insight:** The kernel's core value proposition — self-building, self-improving protocols with lesson learning — is portable because it's instruction-based. The enforcement layer (hooks, commands, state) is Claude Code-specific. For non-Claude-Code agents, the kernel operates in "honor system" mode: the agent follows the instructions because they're in the SKILL.md, but there's no mechanical enforcement.

---

## 5. Testing Plan

### Level 1: Format Validation (Automated, 30 minutes)

| Test | Method | Pass Criteria |
|------|--------|---------------|
| YAML parsing | `python3 -c "import yaml; yaml.safe_load(open('SKILL.md'))"` | No parse errors |
| Required fields present | Script checking name, description, version, author, agents | All fields present |
| Semver validation | Regex match on version field | Valid semver format |
| Markdown rendering | Render with CommonMark parser | No rendering errors |
| File size check | `wc -c SKILL.md` | Under 100KB |
| Token count | tiktoken or approximation | Under 50,000 tokens |

### Level 2: Agent Consumption (Manual, 2 hours)

For each Tier 1 and Tier 2 agent, manually verify:

| Agent | Test | Pass Criteria |
|-------|------|---------------|
| Claude Code | Install skill via `/skill` command | Skill loads, instructions appear in context |
| Claude Code | Run a task with skill active | Agent follows kernel protocol |
| Cursor | Add SKILL.md to project rules | Cursor reads and applies instructions |
| Copilot | Include SKILL.md in workspace | Copilot references instructions in responses |
| Gemini CLI | Point Gemini at SKILL.md | Gemini reads and follows instructions |
| Cline | Add SKILL.md to Cline config | Cline loads skill instructions |

### Level 3: End-to-End Workflow (Manual, 3 hours)

For Claude Code (Tier 1 — full compatibility):

| Test | Steps | Pass Criteria |
|------|-------|---------------|
| Fresh domain setup | Install kernel skill → `/kernel/domain-setup` on a test repo | Protocol created, hooks installed, state initialized |
| Anchor cycle | Make 10 edits → verify anchor fires | Hook blocks at action limit, anchor ceremony completes |
| Lesson learning | Introduce a test failure → fix → `/kernel/learn` | Lesson recorded in lessons.md, block cleared |
| Autonomous cycling | Create 3 tasks → `/kernel/autonomous-cycle` | All 3 tasks completed without manual intervention |
| Complete gate | Run `/kernel/complete` after task | State updated, cycling continues to next task |

For Cursor/Copilot (Tier 2 — instruction compatibility):

| Test | Steps | Pass Criteria |
|------|-------|---------------|
| Instruction following | Open project with SKILL.md → ask agent to "follow kernel protocol" | Agent reads protocol, applies rules |
| File operations | Ask agent to "create a protocol file following the kernel pattern" | Agent creates file matching kernel structure |
| Lesson recording | Ask agent to "record a lesson about X" | Agent appends to lessons.md in correct format |

### Level 4: Platform Indexing (Automated, 1 hour)

After publishing to GitHub:

| Platform | Test | Pass Criteria |
|----------|------|---------------|
| agentskills.io | Check auto-index within 24 hours | Kernel appears in registry |
| skills.sh | Search for "isagawa-kernel" | Kernel listed with correct metadata |
| claudemarketplaces.com | Submit or wait for crawl | Kernel listed with correct metadata |
| GitHub | Search "isagawa-kernel SKILL.md" | Repository appears in search results |

---

## 6. Deployment Timeline

### Day 1: Audit and Convert (8 hours)

| Hour | Task | Output |
|------|------|--------|
| 1-2 | Audit all existing SKILL.md files | Audit spreadsheet |
| 2-3 | Define Agent Skills frontmatter for each skill | YAML templates |
| 3-7 | Convert markdown bodies (6 skills) | Converted SKILL.md files |
| 7-8 | Create aggregate root SKILL.md | `/SKILL.md` |

### Day 2: Test and Document (8 hours)

| Hour | Task | Output |
|------|------|--------|
| 1-1.5 | Level 1 format validation | Automated test results |
| 1.5-3.5 | Level 2 agent consumption testing | Manual test report |
| 3.5-6.5 | Level 3 end-to-end workflow testing | E2E test report |
| 6.5-8 | Update documentation (README, CHANGELOG, installation guides) | Updated docs |

### Day 3: Deploy and Monitor (4 hours)

| Hour | Task | Output |
|------|------|--------|
| 1-1.5 | Create branch, commit, tag v2.0.0 | Git artifacts |
| 1.5-2 | Push to GitHub | Auto-indexing triggered |
| 2-3 | Submit to Claude Code Plugins Official | Submission confirmation |
| 3-4 | Level 4 platform indexing verification | Platform listing confirmations |

**Total engineering effort: 20 hours across 3 days.**

---

## 7. Risk Assessment

### High Risk

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|-----------|
| Agent Skills spec changes after refactor | Medium | High — requires re-conversion | Pin to specific spec version in frontmatter; monitor spec repository for breaking changes; maintain conversion script for rapid re-conversion |
| Hook enforcement lost on non-Claude-Code agents | Certain | High — kernel's safety guarantees degraded | Document "honor system" mode clearly; recommend Claude Code for production use; explore agent-specific enforcement for Tier 2 agents in Phase 2 |

### Medium Risk

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|-----------|
| Aggregate SKILL.md exceeds context window on smaller agents | Medium | Medium — skill partially consumed | Measure token count; create a "lite" version with core instructions only for agents with smaller context windows |
| Platform rejection (Claude Code Plugins Official) | Low | Medium — delays official channel distribution | Prepare Plugin format as fallback; submit early to discover requirements |
| Existing kernel users disrupted by format change | Low | Medium — breaking change for current consumers | Tag as v2.0.0 (major version); maintain v1.x branch for existing users; write migration guide |

### Low Risk

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|-----------|
| YAML frontmatter parsing differences across agents | Low | Low — metadata not consumed consistently | Test on all target agents; use only standard YAML features (no anchors, no merge keys) |
| Community platforms stop crawling or shut down | Low | Low — GitHub remains canonical | GitHub Direct is the permanent source; all other platforms are additive |
| Competitor publishes similar kernel before Isagawa | Low | Medium — first-mover advantage lost | Execute Phase 1 within 4 weeks; differentiate on quality (lesson learning, protocol enforcement) |

### Risk Summary

The highest-impact risk is the loss of hook enforcement on non-Claude-Code agents. This is an inherent limitation of the multi-agent approach — Claude Code's enforcement model (PreToolUse/PostToolUse hooks) has no equivalent in other agents. The mitigation is clear documentation and positioning Claude Code as the "production" tier while other agents get the "instruction-following" tier.

The refactor itself is low-risk. The kernel's instruction-based architecture was designed for portability (text instructions, not API calls), and the format conversion is mechanical rather than architectural.

---

## References

### Source Documents

- Design doc: `docs/backlog/131-market-research-claude-code-harness-distribution-strategy/recommendation.md` (Phase 1 Track A)
- Platforms inventory: `projects/claude-code-harness-distribution/01-platforms-inventory-and-comparison.md`
- Agent Skills specification: https://github.com/agentskills/agentskills

### Kernel Source Files

- Domain Setup: `.claude/skills/kernel-domain-setup/SKILL.md`
- Autonomous Cycling: `.claude/skills/autonomous-cycling/SKILL.md`
- Task Builder: `.claude/skills/task-builder/SKILL.md`
- Audit Workflow: `.claude/skills/audit-workflow/SKILL.md`
- Execute Pipeline: `.claude/skills/execute-pipeline/SKILL.md`
- Production Test: `.claude/skills/prod-test/SKILL.md`

---

*Generated for Backlog 131 — Task 005*
*Kernel domain: sr_dev*
*Date: 2026-06-15*

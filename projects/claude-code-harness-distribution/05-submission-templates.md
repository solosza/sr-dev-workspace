# Submission Templates — Platform Distribution Guide

**Backlog:** 131 — Claude Code Harness Distribution Strategy
**Task:** 006
**Date:** 2026-06-15
**Status:** Complete

---

## Overview

This document provides ready-to-use submission templates for each distribution platform identified in the research phase. Each template includes the required fields, description guidelines, keyword/category recommendations, and step-by-step submission instructions.

**Platforms covered:**
1. Claude Code Plugins Official (claudepluginhub.com)
2. Agent Skills Hub (skills.sh / agentskills.io)
3. claudemarketplaces.com
4. GitHub Direct Registration
5. claudeskills.info (bonus — skills-specific discovery)

**How to use:** Copy the relevant template, fill in the bracketed fields with your skill's specifics, and follow the submission instructions. Each template is designed for Isagawa Kernel skills that have been refactored to SKILL.md format per the Agent Skills Refactor Spec (deliverable 04).

---

## Claude Code Plugins Official

### Platform Details

| Field | Value |
|-------|-------|
| URL | [claudepluginhub.com](https://www.claudepluginhub.com/marketplaces/anthropics-claude-plugins-official) |
| Discovery | Built-in `/plugin` command → "Discover" tab |
| Reach | 100K+ Claude Code users |
| Review Timeline | 2-4 weeks |
| Cost | Free |

### Submission Template

```
PLUGIN NAME: [skill-name]
DISPLAY NAME: [Human-Readable Skill Name]
AUTHOR: Isagawa Co.
AUTHOR URL: https://github.com/isagawa-co
LICENSE: MIT

CATEGORY: [Select one: Developer Tools | Workflow Automation | Code Quality | Testing | Project Management]

SHORT DESCRIPTION (max 120 chars):
[One-line value proposition. Example: "Self-building AI agent kernel — automated protocol enforcement, domain setup, and autonomous task cycling."]

LONG DESCRIPTION (max 500 words):
[Paragraph 1: What the skill does and who it's for.]
[Paragraph 2: Key capabilities — list 3-5 features.]
[Paragraph 3: How it integrates with Claude Code — mention SKILL.md compatibility.]
[Paragraph 4: Link to documentation and source repo.]

KEYWORDS (max 10):
[keyword-1], [keyword-2], [keyword-3], ...
Example: agent-kernel, autonomous-cycling, protocol-enforcement, domain-setup, task-builder, self-improving-agent, ai-workflow, quality-gates

SCREENSHOTS:
- [screenshot-1.png]: Overview of skill in action (terminal output showing kernel loop)
- [screenshot-2.png]: Protocol enforcement example (hook blocking + resolution)
- [screenshot-3.png]: Task cycling output (autonomous task execution)

GITHUB REPO: https://github.com/isagawa-co/[repo-name]
SKILL.MD PATH: .claude/skills/[skill-name]/SKILL.md

INSTALLATION COMMAND:
claude plugin install [plugin-id]
```

### Submission Instructions

1. Navigate to [claudepluginhub.com/submit](https://www.claudepluginhub.com/submit)
2. Sign in with GitHub account (must be org owner or collaborator on isagawa-co)
3. Fill in all fields from the template above
4. Upload 2-3 screenshots (PNG, max 2MB each, 1200x800 recommended)
5. Link the GitHub repository (must be public)
6. Submit for review — Anthropic team reviews within 2-4 weeks
7. Monitor email for approval, revision requests, or rejection
8. Once approved, verify listing appears in `/plugin discover` command

### Description Guidelines

- Lead with the user benefit, not the technology
- Use active voice: "Automates protocol enforcement" not "Protocol enforcement is automated"
- Mention Claude Code compatibility explicitly
- Include "SKILL.md compatible" for cross-harness discovery
- Avoid jargon unfamiliar to the target audience
- Keep paragraphs short (2-3 sentences max)

---

## skills.sh / agentskills.io (Agent Skills Hub)

### Platform Details

| Field | Value |
|-------|-------|
| URL | [skills.sh](https://inference.sh/blog/skills/agent-skills-overview) / [agentskills.io](https://agentskills.io) |
| Discovery | Primary SKILL.md discovery hub, auto-indexes GitHub repos |
| Reach | 30+ AI coding agents (Claude Code, Cursor, Copilot, Codex CLI, Gemini CLI, etc.) |
| Review Timeline | Immediate (auto-indexed on GitHub publish) |
| Cost | Free |

### Submission Template — SKILL.md File

The submission IS the SKILL.md file itself. No separate form required — publishing a conformant SKILL.md to a public GitHub repo triggers auto-indexing.

```yaml
---
name: "[Skill Name]"
description: "[One-line description — max 120 chars]"
version: "1.0.0"
author: "Isagawa Co."
author_url: "https://github.com/isagawa-co"
license: "MIT"
tags:
  - [tag-1]
  - [tag-2]
  - [tag-3]
agents:
  - claude-code
  - cursor
  - copilot
  - codex-cli
  - gemini-cli
  - cline
  - windsurf
  - opencode
  - aider
repository: "https://github.com/isagawa-co/[repo-name]"
documentation: "https://github.com/isagawa-co/[repo-name]/blob/main/README.md"
---

# [Skill Name]

## Purpose

[2-3 sentences: What this skill does and why it matters.]

## Capabilities

- [Capability 1: concrete action the skill performs]
- [Capability 2]
- [Capability 3]
- [Capability 4]

## Usage

[How to install/activate the skill in Claude Code or other agents.]

## File Index

| File | Purpose |
|------|---------|
| `SKILL.md` | Skill identity, capabilities, file index |
| `[file-1]` | [purpose] |
| `[file-2]` | [purpose] |

## Requirements

- [Prerequisite 1, e.g., "Claude Code v1.0+"]
- [Prerequisite 2, e.g., "Git installed"]
```

### Submission Template — GitHub Registry Entry

For explicit registration with agentskills.io (beyond auto-indexing):

```json
{
  "name": "[skill-name]",
  "description": "[One-line description]",
  "repository": "https://github.com/isagawa-co/[repo-name]",
  "skill_path": ".claude/skills/[skill-name]/SKILL.md",
  "author": "isagawa-co",
  "license": "MIT",
  "tags": ["[tag-1]", "[tag-2]", "[tag-3]"],
  "agents": ["claude-code", "cursor", "copilot", "codex-cli", "gemini-cli"],
  "version": "1.0.0"
}
```

### Submission Instructions

1. Ensure SKILL.md is in the correct location: `.claude/skills/[skill-name]/SKILL.md`
2. Validate YAML frontmatter with a YAML linter (no tabs, proper quoting)
3. Push to public GitHub repository under isagawa-co org
4. Auto-indexing: skills.sh and agentskills.io crawl public repos with SKILL.md files
5. Explicit registration (optional): Submit a PR to the agentskills.io registry repo with the JSON entry above
6. Verify listing at agentskills.io within 24-48 hours
7. Test portability: install in at least 2 different agents (Claude Code + one other)

### Auto-Indexing Requirements

- Repository must be **public**
- SKILL.md must be at a discoverable path (root or `.claude/skills/*/SKILL.md`)
- YAML frontmatter must include `name`, `description`, `version`, `author`
- No binary files in the skill directory (text-only)
- README.md in repo root should reference the skill

---

## claudemarketplaces.com

### Platform Details

| Field | Value |
|-------|-------|
| URL | [claudemarketplaces.com](https://claudemarketplaces.com/) |
| Discovery | Community-curated index, daily GitHub crawler |
| Reach | 100K+ community members |
| Review Timeline | 1-2 days (automated crawler + community voting) |
| Cost | Free |

### Submission Template

```
LISTING TYPE: [Plugin | Skill | Tool]

TITLE: [Human-Readable Name]
SLUG: [url-friendly-name]

AUTHOR: Isagawa Co.
AUTHOR GITHUB: https://github.com/isagawa-co

CATEGORY: [Select one: AI Agents | Developer Tools | Workflow Automation | Code Quality | Testing]
SUBCATEGORY: [Select one: Agent Frameworks | Task Automation | Quality Assurance | Protocol Enforcement]

SHORT DESCRIPTION (max 160 chars):
[One-line pitch optimized for search and browsing.]

FULL DESCRIPTION (markdown supported, max 1000 words):
## What It Does
[2-3 sentences on the core value proposition.]

## Key Features
- [Feature 1 with brief explanation]
- [Feature 2]
- [Feature 3]
- [Feature 4]

## Getting Started
[3-step quickstart: install, configure, run.]

## Compatibility
- Claude Code: ✓ Native
- Cursor: ✓ Via SKILL.md
- Copilot: ✓ Via SKILL.md
- [Other agents as applicable]

## Links
- [GitHub Repository](https://github.com/isagawa-co/[repo-name])
- [Documentation](https://github.com/isagawa-co/[repo-name]/blob/main/README.md)
- [License: MIT](https://github.com/isagawa-co/[repo-name]/blob/main/LICENSE)

TAGS (max 15):
[tag-1], [tag-2], [tag-3], ...
Example: claude-code, agent-skills, kernel, autonomous-agent, protocol-enforcement, task-automation, self-improving, SKILL.md, MIT, open-source

GITHUB URL: https://github.com/isagawa-co/[repo-name]
DEMO URL: [optional — link to demo video or walkthrough]
```

### Submission Instructions

1. Navigate to [claudemarketplaces.com/submit](https://claudemarketplaces.com/submit)
2. Sign in with GitHub account
3. Select listing type (Skill recommended for SKILL.md format)
4. Fill in all template fields — markdown is supported in the full description
5. Add tags (community uses these for filtering; more tags = more discovery)
6. Submit listing — automated crawler verifies GitHub repo within 24 hours
7. Community voting begins immediately after listing goes live
8. Monitor listing for comments and feedback; respond to build community trust

### Community Voting Tips

- A well-written description with clear use cases gets more upvotes
- Include a "Getting Started" section — users want to try before voting
- Respond to comments within 48 hours to show active maintenance
- Cross-link from GitHub README to the claudemarketplaces.com listing

---

## GitHub Direct Registration

### Platform Details

| Field | Value |
|-------|-------|
| URL | [github.com](https://github.com) |
| Discovery | Organic search, trending, topics, auto-indexed by agentskills.io |
| Reach | Unlimited (internet-wide) |
| Review Timeline | Immediate |
| Cost | Free |

### README Template

```markdown
# [Skill Name]

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Agent Skills](https://img.shields.io/badge/Agent_Skills-SKILL.md-blue.svg)](https://agentskills.io)
[![Claude Code](https://img.shields.io/badge/Claude_Code-Compatible-purple.svg)]()

> [One-line description — same as SKILL.md description field]

## Overview

[2-3 paragraphs: what the skill does, who it's for, why it exists.]

## Features

- [Feature 1]
- [Feature 2]
- [Feature 3]
- [Feature 4]

## Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/isagawa-co/[repo-name].git

# Or add as a skill to your project
cp -r [repo-name]/.claude/skills/[skill-name] .claude/skills/
```

### Usage

[3-5 lines showing how to use the skill in Claude Code]

## Compatibility

| Agent | Status | Method |
|-------|--------|--------|
| Claude Code | ✓ Native | Built-in SKILL.md support |
| Cursor | ✓ Compatible | SKILL.md auto-detection |
| GitHub Copilot | ✓ Compatible | SKILL.md support |
| Codex CLI | ✓ Compatible | SKILL.md support |
| Gemini CLI | ✓ Compatible | SKILL.md support |
| Cline | ✓ Compatible | SKILL.md support |
| Windsurf | ✓ Compatible | SKILL.md support |
| OpenCode | ✓ Compatible | SKILL.md support |
| Aider | ✓ Compatible | SKILL.md support |

## Documentation

- [SKILL.md](.claude/skills/[skill-name]/SKILL.md) — Skill specification
- [Architecture](docs/architecture.md) — System design
- [Contributing](CONTRIBUTING.md) — How to contribute

## License

MIT — see [LICENSE](LICENSE) for details.

## Author

[Isagawa Co.](https://github.com/isagawa-co) — Building AI agent infrastructure.
```

### Repository Topics/Tags

Add these topics to the GitHub repository settings:

```
claude-code
agent-skills
skill-md
ai-agent
autonomous-agent
protocol-enforcement
task-automation
mit-license
```

### Submission Instructions

1. Create or update the GitHub repository under isagawa-co org
2. Add the README using the template above
3. Add repository topics via Settings → General → Topics
4. Ensure SKILL.md is at the correct path (`.claude/skills/[skill-name]/SKILL.md`)
5. Create a GitHub Release with semantic versioning (e.g., v1.0.0)
6. Write release notes summarizing capabilities and breaking changes
7. Verify auto-indexing: check agentskills.io for listing within 48 hours
8. Add badges to README for discoverability (License, Agent Skills, Claude Code)

### Release Process

```bash
# Tag the release
git tag -a v1.0.0 -m "Initial release: [skill-name]"
git push origin v1.0.0

# Create GitHub release (using gh CLI)
gh release create v1.0.0 \
  --title "[Skill Name] v1.0.0" \
  --notes "Initial release. See README for features and installation."
```

---

## claudeskills.info

### Platform Details

| Field | Value |
|-------|-------|
| URL | [claudeskills.info](https://claudeskills.info/) |
| Discovery | Skills-focused community directory, daily updates |
| Reach | 50K+ community |
| Review Timeline | 1-2 days (automated) |
| Cost | Free |

### Submission Template

```
SKILL NAME: [Human-Readable Name]
SLUG: [url-friendly-name]
AUTHOR: Isagawa Co.
GITHUB: https://github.com/isagawa-co/[repo-name]

CATEGORY: [Agent Frameworks | Developer Productivity | Code Quality | Automation]

DESCRIPTION (max 300 chars):
[Concise pitch focused on what the skill enables.]

FEATURES:
1. [Feature with one-line explanation]
2. [Feature with one-line explanation]
3. [Feature with one-line explanation]

COMPATIBILITY: Claude Code, Cursor, Copilot, Codex CLI, Gemini CLI, Cline, Windsurf, OpenCode, Aider

SKILL.MD LOCATION: .claude/skills/[skill-name]/SKILL.md

TAGS: [tag-1], [tag-2], [tag-3], [tag-4], [tag-5]
```

### Submission Instructions

1. Navigate to claudeskills.info submission page
2. Fill in the template fields
3. Link to the public GitHub repository
4. Submit — automated crawler verifies repo structure within 24 hours
5. Listing appears in the skills directory after verification

---

## Cross-Platform Keyword Strategy

### Primary Keywords (use on ALL platforms)

| Keyword | Purpose |
|---------|---------|
| `claude-code` | Platform-specific discovery |
| `agent-skills` | Standard format discovery |
| `skill-md` | Format-specific search |
| `ai-agent` | Broad category |
| `autonomous-agent` | Capability differentiator |

### Secondary Keywords (use on 2+ platforms)

| Keyword | Purpose |
|---------|---------|
| `protocol-enforcement` | Feature-specific |
| `task-automation` | Use case |
| `self-improving` | Capability |
| `domain-setup` | Feature-specific |
| `quality-gates` | Feature-specific |
| `open-source` | Trust signal |
| `MIT` | License clarity |

### Platform-Specific Keywords

| Platform | Additional Keywords |
|----------|-------------------|
| Claude Code Plugins | `plugin`, `claude-plugin`, `developer-tools` |
| skills.sh | `portable-skill`, `multi-harness`, `cross-agent` |
| claudemarketplaces.com | `community`, `trending`, `new-release` |
| GitHub | `hacktoberfest` (seasonal), `good-first-issue` (contributor), `ai-tools` |

---

## Submission Checklist

Before submitting to any platform, verify:

- [ ] SKILL.md format validated (YAML frontmatter + markdown body)
- [ ] All required fields populated (name, description, version, author, tags)
- [ ] GitHub repository is public
- [ ] README.md includes badges, quickstart, and compatibility table
- [ ] LICENSE file present (MIT)
- [ ] At least one GitHub Release created with semantic versioning
- [ ] Screenshots prepared (if required by platform)
- [ ] Description optimized for search (keywords in first sentence)
- [ ] Cross-agent compatibility tested (Claude Code + at least one other agent)
- [ ] All links verified (no broken URLs)

### Submission Order (Recommended)

1. **GitHub** (first — establishes permanent home, triggers auto-indexing)
2. **Agent Skills Hub** (second — auto-indexed from GitHub, verify listing)
3. **Claude Code Plugins Official** (third — highest discoverability, longest review)
4. **claudemarketplaces.com** (fourth — community reach, fast listing)
5. **claudeskills.info** (fifth — additional skills-focused discovery)

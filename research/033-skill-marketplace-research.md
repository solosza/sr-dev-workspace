# Skill Marketplace Research

**Task:** 033-research-skill-marketplaces
**Date:** 2026-03-06

---

## 1. Marketplace Comparison Table

| Marketplace | Status | Format | Revenue Share | Submission Process | Audience |
|-------------|--------|--------|---------------|-------------------|----------|
| **Anthropic Skills (anthropics/skills)** | Live (Dec 2025+) | Agent Skills standard (SKILL.md) | None — open source (Apache 2.0) | PR to `anthropics/skills` GitHub repo | Claude Code users |
| **skills.sh (Vercel)** | Live (Jan 2026) | Agent Skills standard (SKILL.md) | None — free, open | `npx skills add <owner>/<repo>` — auto-indexed from GitHub | 30+ agents (Claude, Codex, Cursor, Copilot, Windsurf, etc.) |
| **SkillsMP** | Live (community) | Agent Skills standard (SKILL.md) | None — aggregator | Auto-scraped from public GitHub repos | Claude Code, Codex CLI users |
| **Cursor Marketplace** | Live (Feb 2026) | Plugin bundles (MCP servers, skills, subagents, hooks, rules) | Unknown — curated partners only | Invite-only at launch; `/add-plugin` in editor | Cursor users |
| **VS Code / GitHub Copilot** | Live (GA Feb 2026) | Agent Skills standard (SKILL.md) | None — open standard | Drop skill folder into `.github/skills/` or install via CLI | Copilot + VS Code users |
| **Windsurf** | Minimal | VS Code extensions + MCP; no dedicated skill marketplace | N/A | No formal submission; uses VS Code extension marketplace | Windsurf users |
| **LobeHub** | Live (community) | Agent Skills standard | None — aggregator | Submit via GitHub | Multi-agent |
| **GitHub Marketplace** | Live (Actions/Apps) | GitHub Actions / Apps format | GitHub terms | Standard GitHub Marketplace submission | GitHub ecosystem |

---

## 2. The Agent Skills Standard (agentskills.io)

Published by Anthropic (Dec 2025). Adopted by OpenAI (Codex CLI), Microsoft (Copilot), Vercel, and 30+ agents.

### Format Requirements

```
my-skill/
├── SKILL.md          # Required — YAML frontmatter + markdown instructions
├── scripts/          # Optional — supporting scripts
├── references/       # Optional — reference docs
└── assets/           # Optional — images, templates, etc.
```

### SKILL.md Structure

```markdown
---
name: my-skill-name          # Required. Lowercase, hyphens, max 64 chars
description: What it does     # Required. Max 1024 chars. Include when to use it.
license: Apache-2.0          # Optional
compatibility:               # Optional — only if env-specific deps
  platforms: [linux, macos]
metadata:                    # Optional — custom key/value pairs
  author: isagawa-co
---

# Skill Instructions

(Markdown body — no format restrictions. Keep under 500 lines / 5000 tokens recommended.)
```

### Key Constraints
- `name`: lowercase letters, numbers, hyphens only. No leading/trailing hyphens. No consecutive hyphens.
- `description`: must describe what AND when. Max 1024 chars.
- Body: loaded when skill activates. Keep concise for token efficiency.

---

## 3. Format Mapping — Our Specs vs Marketplace Requirements

| Our Spec Component | Agent Skills Standard | Gap | Action Needed |
|-------------------|----------------------|-----|---------------|
| `SKILL.md` | `SKILL.md` | None — already compliant | None |
| `workflow.md` | Part of skill folder | None — references/ supported | None |
| `references/` | `references/` | None — standard supports this | None |
| `lessons/` (seeded) | Not in standard | Minor — non-standard but harmless | Keep as-is; agents ignore unknown dirs |
| `templates/` | `assets/` or custom | Naming convention differs | Optional rename to `assets/` |
| YAML frontmatter | Required: name, description | May be missing in some specs | Add frontmatter to all SKILL.md files |
| `compatibility` field | Optional in standard | Not currently set | Add if platform-specific (e.g., Docker spec needs Docker) |

### Verdict
Our specs are **95% compatible** with the Agent Skills standard. Only change needed: ensure YAML frontmatter (name + description) exists in every SKILL.md. The rest of our structure (references/, workflow.md, lessons/) is valid — the standard allows arbitrary subdirectories.

---

## 4. Distribution Channels Ranked

### Primary: skills.sh (Vercel)

**Why:**
- Largest cross-agent reach (30+ agents including Claude, Codex, Cursor, Copilot, Windsurf)
- Zero friction: `npx skills add isagawa-co/<spec-repo>` installs directly
- Auto-indexed from GitHub — no submission process, just publish repo
- Free, open ecosystem
- 20,000+ installs on top skills within hours of launch
- CLI-native (matches our target audience: developers using coding agents)

**Action:** Ensure each spec repo has compliant SKILL.md frontmatter. skills.sh auto-discovers from GitHub.

### Secondary: Anthropic Skills (anthropics/skills)

**Why:**
- Official Anthropic channel — credibility and visibility
- Claude Code users browse here first
- Skills 2.0 adds evals and A/B testing
- PR-based submission to `anthropics/skills` repo

**Action:** Submit PRs for each spec (playwright, selenium, docker, vibe-coder) to `anthropics/skills`.

### Tertiary: SkillsMP + LobeHub (auto-aggregators)

**Why:**
- Auto-scraped from public GitHub repos — zero effort if repos are public
- Additional discovery surface

**Action:** Ensure public repos have proper `anthropic-skills` or `agent-skills` GitHub topics for discoverability.

### Not Recommended (for now)

| Channel | Reason |
|---------|--------|
| **Cursor Marketplace** | Invite-only, curated partners. Not open for submission yet. Monitor for open access. |
| **GitHub Marketplace** | Actions/Apps format — doesn't map to skill folders. Overhead not justified. |
| **VS Code Marketplace** | Would need a wrapper extension. Overkill for skill distribution. |
| **Windsurf** | No dedicated skill marketplace. Uses VS Code extensions. |

---

## 5. Timeline — Available Now vs Coming Soon

| Channel | Status | Our Action |
|---------|--------|------------|
| skills.sh | Available NOW | Add frontmatter, publish repos |
| anthropics/skills | Available NOW | Submit PRs |
| SkillsMP | Available NOW (auto) | Make repos public with topics |
| LobeHub | Available NOW (auto) | Same as SkillsMP |
| Cursor Marketplace | Coming (open submission TBD) | Monitor for open access |
| VS Code skills | Available NOW (GA) | Works via `.github/skills/` — low priority |

---

## 6. Recommended Distribution Strategy

1. **Immediate:** Ensure all spec repos have Agent Skills-compliant SKILL.md frontmatter
2. **Week 1:** Publish specs to skills.sh via `npx skills` (auto-indexed from GitHub)
3. **Week 2:** Submit to `anthropics/skills` via PR for official visibility
4. **Ongoing:** Auto-aggregators (SkillsMP, LobeHub) pick up public repos automatically
5. **Monitor:** Cursor Marketplace for open submission access

### Revenue Note
No marketplace currently supports paid skills or revenue sharing. All distribution is free/open source. Monetization would need to happen through:
- Consulting/services built around specs
- Premium specs distributed through private channels (not marketplaces)
- Future marketplace features (none announced)

---

## Sources

- [Anthropic Skills Repo](https://github.com/anthropics/skills/)
- [Agent Skills Specification](https://agentskills.io/specification)
- [skills.sh — Vercel](https://skills.sh/docs/cli)
- [Vercel skills.sh Announcement](https://vercel.com/changelog/introducing-skills-the-open-agent-skills-ecosystem)
- [SkillsMP](https://skillsmp.com)
- [Cursor Marketplace Blog](https://cursor.com/blog/marketplace)
- [VS Code Agent Skills Docs](https://code.visualstudio.com/docs/copilot/customization/agent-skills)
- [Claude Code Skills Docs](https://code.claude.com/docs/en/skills)
- [Skills 2.0 — Geeky Gadgets](https://www.geeky-gadgets.com/anthropic-skill-creator/)

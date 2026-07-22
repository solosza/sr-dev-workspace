# Existing Infrastructure Inventory — Multi-Persona Architecture

**Task:** 001-research-existing-infrastructure
**Date:** 2026-07-07

---

## Persona → Existing Infrastructure Map

### 1. Developer Persona

**Status:** Fully operational — this IS the kernel.

| Capability | Location | Type |
|-----------|----------|------|
| Session lifecycle | `.claude/commands/kernel/session-start.md`, `anchor.md`, `complete.md` | Command |
| Domain setup | `.claude/skills/kernel-domain-setup/SKILL.md` (11 steps) | Skill |
| Task decomposition | `.claude/skills/task-builder/SKILL.md` (10 steps) | Skill |
| Autonomous cycling | `.claude/skills/autonomous-cycling/SKILL.md` | Skill |
| Pipeline execution | `.claude/skills/execute-pipeline/SKILL.md` | Skill |
| Code building | `.claude/skills/build-command/SKILL.md` | Skill |
| Design command | `.claude/skills/design-command/SKILL.md` | Skill |
| Loop template | `.claude/skills/loop-template/SKILL.md` | Skill |
| Self-improvement | `.claude/commands/kernel/learn.md`, `fix.md` | Command |
| Backlog management | `.claude/commands/kernel/backlog.md` | Command |
| Protocol enforcement | `.claude/hooks/universal-gate-enforcer.py`, `sr_dev-gate-enforcer.py` | Hook |
| Actions tracking | `.claude/hooks/actions-log-appender.py` | Hook |
| Test failure detection | `.claude/hooks/test-failure-detector.py` | Hook |
| Agent spawning | `.claude/skills/spawn-subagent/SKILL.md`, `spawn-agent-swarm/SKILL.md` | Skill |

**Gaps:** None — Developer is the foundational persona. All kernel governance applies here.

---

### 2. QA Persona

**Status:** Partially operational — 4 skills exist, no unified QA workflow.

| Capability | Location | Type |
|-----------|----------|------|
| Production testing | `.claude/skills/prod-test/SKILL.md` (8 steps) | Skill |
| Gap analysis | `.claude/skills/gap-check/SKILL.md` | Skill |
| Review queue | `.claude/skills/review-queue/SKILL.md` | Skill |
| Eval (test harness) | `.claude/skills/eval/SKILL.md` | Skill |
| Audit workflow | `.claude/skills/audit-workflow/SKILL.md` (8 steps) | Skill |
| Human check | `.claude/skills/human-check/SKILL.md` | Skill |
| Reference scanner | `.claude/skills/reference-scanner/SKILL.md` | Skill |
| DeepEval integration | `.deepeval/` + `projects/deepeval-security-behavior-research/` | Framework |
| SSH platform (QA) | `D:/my_ai_projects/project_test_repos/isagawa-qa-platform/` | Repo |

**Gaps:**
- No unified QA orchestrator loop (each skill runs independently, no "run all QA" command)
- No automated test scheduling (no cron/nightly QA pass)
- No QA-specific protocol or domain spec (QA skills live under Developer persona's protocol)
- No QA-specific lessons file (QA failures go to Developer lessons)
- No regression test suite management (tests exist but no catalog or priority ordering)

---

### 3. Sales Persona

**Status:** Partially operational — single command, domain-setup completed.

| Capability | Location | Type |
|-----------|----------|------|
| Job application | `D:/my_ai_projects/project_test_repos/job-application-spec/.claude/commands/job-apply.md` | Command |
| Resume (prose) | `job-application-spec/resumes/alain-ignacio-ai-agent-architect.md` + PDF | Asset |
| Profile config | `job-application-spec/profile.json` | Data |
| Kernel commands | `job-application-spec/.claude/commands/kernel/` (6 kernel commands) | Command |
| Job search pipeline | `projects/ai-harness-job-search/` (pipeline 029, dated runs) | Project |

**Gaps:**
- No CRM/pipeline tracking (no structured state for leads, applications, follow-ups)
- No outreach automation (no cold email, no LinkedIn automation)
- No interview prep skill (no mock interview, no company research automation)
- No sales-specific orchestrator (job-apply is standalone, not part of a sales workflow)
- No proposal/pitch generation skill
- No revenue tracking or deal pipeline

---

### 4. PM (Project Manager) Persona

**Status:** Minimal — backlog management exists, no strategic planning.

| Capability | Location | Type |
|-----------|----------|------|
| Backlog creation | `.claude/commands/kernel/backlog.md` | Command |
| Task builder | `.claude/skills/task-builder/SKILL.md` | Skill |
| Pipeline execution | `.claude/skills/execute-pipeline/SKILL.md` | Skill |
| Velocity research | `projects/velocity-management-research/` | Research |

**Gaps:**
- No "what to work on next" logic (no backlog prioritization algorithm)
- No roadmap generation or tracking
- No velocity/throughput metrics (research done, not implemented)
- No dependency tracking between backlogs
- No sprint planning or milestone management
- No stakeholder reporting (no automated status updates)
- No resource allocation across personas

---

### 5. Marketing Persona

**Status:** Minimal — website cloner exists, no content or SEO automation.

| Capability | Location | Type |
|-----------|----------|------|
| Website cloner | `.claude/skills/website-cloner/SKILL.md` | Skill |
| Architecture diagrams | `docs/architecture-diagrams/` (4 Mermaid diagrams, backlog 136) | Asset |
| Site improvement backlogs | `docs/backlog/` (backlogs 135-140: messaging, README, diagrams) | Backlog |
| Bookmark scanner | `.claude/commands/kernel/scan-bookmarks.md` | Command |

**Gaps:**
- No content generation skill (blog posts, technical articles, case studies)
- No SEO optimization skill
- No social media automation
- No site deployment pipeline (manual updates to isagawa.co)
- No analytics tracking or reporting
- No brand consistency enforcement
- No marketing-specific orchestrator

---

## Cross-Persona Infrastructure

Infrastructure that would be shared across all personas:

| Capability | Location | Status |
|-----------|----------|--------|
| Harness design pattern | `docs/harness-design-pattern/HARNESS-DESIGN-PATTERN.md` | Documented |
| Loop composability | `projects/loop-composability-research/recommendation.md` | Researched |
| Pulsia architecture | `projects/pulsia-research/research-report.md` | Researched (Pulsia = multi-persona reference) |
| Agent orchestration | `docs/backlog/done/127-kernel-build-agent-orchestration-framework.md` | Designed |
| Multi-agent state isolation | `.claude/state/agent-{id}-workflow.json` pattern | Shipped |
| Worktree isolation | `projects/worktree-research/` (backlog 183) | Researched |
| run-task.sh | `run-task.sh` | Shipped |

---

## Gap Summary by Persona

| Persona | Existing Commands/Skills | Key Gaps |
|---------|------------------------|----------|
| **Developer** | 14 commands, 11 skills, 4 hooks | None — fully operational |
| **QA** | 7 skills, 1 framework | No orchestrator, no scheduling, no own protocol |
| **PM** | 3 commands/skills | No prioritization, no roadmap, no velocity metrics |
| **Sales** | 1 command, 1 profile, 1 pipeline | No CRM, no outreach, no interview prep |
| **Marketing** | 1 skill, 1 command | No content gen, no SEO, no deployment pipeline |

---

## Key Findings

1. **Developer persona is 100% complete** — it IS the kernel. All other personas are extensions of or built on top of it.

2. **QA is ~60% there** — the skills exist but lack an orchestrator loop. This is the closest persona to being fully operational. Adding a QA orchestrator command that sequences prod-test → gap-check → review-queue → eval would make it functional.

3. **PM is ~30% there** — backlog and task-builder handle the execution side, but the strategic side (what to work on, why, in what order) is missing. The velocity-management-research provides a foundation.

4. **Sales is ~20% there** — job-apply works but is isolated. No pipeline management, no follow-up automation, no CRM.

5. **Marketing is ~10% there** — website-cloner and bookmark scanner are utilities, not a marketing workflow. Almost everything needs to be built.

6. **The Pulsia research (backlog 128) already designed the multi-persona architecture** at Pulsia scale with 6 loops. The current backlog (186) applies this specifically to Isagawa's 5 personas. The loop composability research (backlog 155) provides the dispatch mechanism (`## Primitive` tags + delegated run-task.sh).

7. **State isolation is solved** — per-agent workflow files (`agent-{id}-workflow.json`) and one-shot pre-init already handle multi-agent state. The worktree research (backlog 183) addresses branch isolation for concurrent work.

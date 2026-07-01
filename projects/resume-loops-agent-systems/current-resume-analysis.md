# Current Resume Analysis — What Failed

## Resume Under Review
`D:/my_ai_projects/project_test_repos/job-application-spec/resumes/alain-ignacio-ai-agent-architect.md`

## Section Catalog

| # | Section | Lines | Content Summary |
|---|---------|-------|----------------|
| 1 | Header | 1-8 | Title: "AI Agent Architect / Founder, Isagawa" + contact info, two GitHub orgs, portfolio link |
| 2 | Summary | 12-14 | 20+ years QA, abstracted into AI agent governance, Isagawa Kernel, healthcare/gov/telecom background |
| 3 | Isagawa: Founder & Systems Architect | 18-39 | Three subsections: Kernel, Agent Factory, Delivery Pipeline. Stats: 80+ runs, 800+ tasks, 9 repos |
| 4 | isagawa-qa: Production QA Platforms | 43-57 | 5 platforms: DeepEval, Playwright, Selenium, SSH Compliance, Docker Compliance |
| 5 | Also Shipped | 60-67 | Vibe Coder, AutoApply, Attestation Pipeline |
| 6 | Prior Experience: QA Architecture | 70-91 | HMSA (current), Helios Digital, Nakupuna, HMSA (9yr), IBM, Virgin Mobile, Sony |
| 7 | Technical Skills | 95-107 | 6 categories: AI Agent Eng, LLM Eval, Architecture, Test Automation, Compliance, Languages |

## Title Assessment: "AI Agent Architect"

**Problem:** Not a searchable or recognizable title. Job postings use:
- "Software Engineer, Agent Infrastructure" (OpenAI)
- "Staff SWE, Agentic AI" (Google)
- "Applied AI Engineer, Agentic Workflows" (Cohere)
- "Senior Frontier Agents Engineer" (Scale AI)

"AI Agent Architect" sounds self-invented. No company posts this title. Recruiters searching LinkedIn won't find it because nobody searches for it. "Architect" also signals enterprise/waterfall to many readers.

**Alternative titles that match market language:**
- AI Agent Infrastructure Engineer
- Agentic Systems Engineer
- Agent Infrastructure Architect (if keeping "architect")

## Language Mismatches with Target Roles

### Isagawa-Specific Terms vs Industry-Standard Terms

| Resume Uses | Industry Uses | Impact |
|------------|--------------|--------|
| "Isagawa Kernel" | agent runtime, agent infrastructure | ATS won't match. Recruiters don't know what a "kernel" is in this context |
| "mechanical enforcement" | guardrails, runtime enforcement | Not in any job posting |
| "anchor mechanism" | agent observability, drift detection | Custom jargon |
| "hook-based governance" | tool-call interception, runtime safety | Describes the same thing but with internal vocabulary |
| "autonomous cycling" | agent orchestration, agentic workflows | "Cycling" is not industry vocabulary |
| "Agent Factory" | agent harness factory, multi-agent system | Name means nothing without context |
| "kernel-governed" | runtime-governed, infrastructure-enforced | Circular reference to custom product name |
| "5-layer architecture" | layered test architecture | Specific enough but not matched by postings |

### Missing Industry Keywords Entirely

These terms appear in job postings and are absent from the resume:
- **multi-agent systems** (the kernel orchestrates multiple agents but never says so)
- **agent platform** (signals production-grade, which this is)
- **agentic** (the industry adjective — appears zero times)
- **guardrails** (industry standard for what the resume calls "enforcement")
- **agent runtime** (what the kernel literally is)
- **agent observability** (what the anchor mechanism provides)
- **agent protocol** (Google's term — the kernel creates protocols)

## Em Dashes and Formatting Issues

The resume markdown uses em dashes (---) for section dividers but does NOT use em dashes within prose. The prose is clean in this regard. However:

- Heavy use of periods at end of descriptive paragraphs makes it read like documentation, not a resume
- Paragraphs are long — some are 3-4 sentences of dense technical description
- The "Also Shipped" section title is informal and undersells the work

## Tone Comparison with isagawa.co

### isagawa.co Tone
- Declarative fragments: "Not configuration. Not templates. Not optional."
- Grounded specifics over claims: numbers, mechanisms, verifiable outputs
- Technical-casual: credible without being stiff
- Emphasis on mechanisms and systems, not aspirational language
- Confident but not boastful

### Resume Tone
- More formal and dense than the website
- Longer sentences, paragraph-style descriptions
- Uses phrases like "The core invention" (line 25) — slightly grandiose
- "The throughline is the same" (line 14) — literary tone that doesn't match isagawa.co's directness
- "The agent scans any repo, writes its own protocol..." (line 27) — good, matches website's mechanism-focused voice
- Overall: reads like a technical white paper, not a resume, and not like isagawa.co

### Specific Tone Mismatches
| Resume Phrase | Issue | isagawa.co Would Say |
|--------------|-------|---------------------|
| "The core invention" | Grandiose | Just describe what it does |
| "The throughline is the same" | Literary | Cut — let the reader see the pattern |
| "a self-reinforcing loop" | Jargon without proof | "The kernel governs the agent that builds kernel-governed harnesses" |
| "No vibes, no spreadsheets" | Casual slogan in an otherwise formal document | Either commit to this tone everywhere or remove it |

## Structural Issues

### Loops Framing is Missing
The kernel IS a loop system: session-start -> anchor -> work -> learn -> complete -> repeat. The resume describes "autonomous task cycling" and "delivery pipeline" but never frames the kernel as a loop architecture. "Loop" does not appear in the resume at all. This is the central insight that should drive the rewrite.

### Agent Systems Framing is Buried
The resume leads with "AI Agent Architect" but structures content around individual tools/platforms. The Agent Factory section describes multi-agent system construction but is a subsection under "Isagawa." The QA platforms are each described individually rather than as "5 production agent systems built on the same runtime."

### QA Dominance in Prior Experience
Lines 70-91 are 100% QA-titled roles. For agent infrastructure positions, this reads as "QA person trying to pivot." The prior experience should reframe QA as quality systems engineering — the discipline that led naturally to agent governance. The test automation work IS agent infrastructure work (building systems that enforce correctness at runtime).

### Technical Skills Section Ordering
"AI Agent Engineering" is first (good) but "Test Automation" and "Compliance and Security" take up equal space. For agent infrastructure roles, agent-relevant skills should dominate.

## Opportunities

1. **Reframe title** to match searchable industry terms
2. **Lead with loops** — the kernel loop is the differentiator, make it the organizing principle
3. **Add industry keywords** naturally throughout — agent infrastructure, agentic, guardrails, multi-agent, agent runtime, agent observability
4. **Shorten paragraphs** — match isagawa.co's declarative fragment style
5. **Reframe QA history** as quality systems engineering that led to agent governance
6. **Consolidate QA platforms** — describe as "5 production agent systems" rather than listing each one
7. **Remove grandiose phrases** — "the core invention," "the throughline is the same"
8. **Add "loop" as first-class concept** — currently absent entirely

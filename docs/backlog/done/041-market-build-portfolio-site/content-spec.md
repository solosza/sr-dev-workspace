# Content Spec

## Status
NEW

## Section 1: Hero

**Headline:** The AI Management Layer

**Subheadline:** Manages AI agents across any domain — mechanically enforced, not advisory.

**Supporting line:** One kernel governs. One factory compiles. 27+ managed agents ship.

**CTA Button:** "See the architecture" (scrolls to section 2)

**Design note:** Full viewport. Terminal/code feel. Possible subtle animation — cursor blink, typing effect, or code-like background pattern.

## Section 2: Architecture Diagram

**Heading:** How It Connects

**Visual:** Flow diagram showing the connected system:

```
ISAGAWA KERNEL (governance runtime)
       |
       v
SPEC FACTORY (compiler)
       |
       v
MANAGED AGENTS (domain specs)
  |         |         |         |         |         |
  IT    Healthcare   QA     DevOps   Real Estate  Creative
```

**Below diagram — three output type cards:**

| BUILD | WORKSPACE | OPERATE |
|-------|-----------|---------|
| Produces executable code, tests, infrastructure | Produces project configuration, environment setup | Produces workflow guidance, process orchestration |
| QA platforms, game engine, Docker images | DevOps pipelines, compliance audit environments | Claims processing, EDI transactions, incident response |

## Section 3: Kernel Mechanisms

**Heading:** The Kernel — Governance That Cannot Be Bypassed

**Subheading:** Four mechanisms that make AI agent governance mechanical, not advisory.

**Four cards:**

1. **Anchor Token**
   - Every 10 actions, the kernel forces re-centering on protocol
   - A UUID token proves the agent actually re-read its rules
   - The agent cannot fake compliance by flipping a state file

2. **Gate Enforcer**
   - Python hooks intercept every Write, Edit, and Bash command
   - Five gates checked before any action proceeds
   - Blocked actions get a specific fix instruction, not a generic error

3. **Learn Loop**
   - Every failure becomes a permanent lesson
   - Lessons promote into hard enforcement (hooks, not just docs)
   - The system gets permanently smarter after every mistake

4. **Self-Audit**
   - The kernel audits its own infrastructure for gaps
   - Scans commands, skills, hooks, protocol, state, testing
   - Auto-generates fix tasks when drift is detected

## Section 4: Spec Factory

**Heading:** The Spec Factory — Any Domain, 30 Minutes

**Subheading:** A compiler that turns a vertical name into a governed AI agent.

**Pipeline visual (condensed to 5 stages):**

```
INPUT          ANALYZE        DESIGN         BUILD          VALIDATE
vertical  →  decompose +  →  architecture  →  SKILL.md    →  L1/L2/L3
name         score (8dim)    + gate contract   workflow.md    production
                                               steps/         testing
                                               commands/
```

**Throughput proof line:** "27+ specs shipped. 13/week sustained. $15 per spec. One person."

**Three output types shown as badges/pills below the pipeline.**

## Section 5: Catalog by Vertical

**Heading:** Managed Agents — Every Domain

**Subheading:** Each spec is a governed agent. Each one was compiled by the factory, validated with production tests, and shipped.

**Content:** See [[041-market-build-portfolio-site/catalog-data]] for the full catalog organized by vertical group.

**Card format per spec:**
- Spec name
- Type badge (BUILD / WORKSPACE / OPERATE)
- One-line description
- Optional: gate count

## Section 6: QA Platforms

**Heading:** AI-Native Test Automation

**Subheading:** Five platforms. One architecture. Every testing layer covered.

**Five platform cards:**

| Platform | Testing Layer | Technology |
|----------|--------------|------------|
| Selenium | UI / Web | Python, Selenium WebDriver |
| Playwright | Browser | TypeScript, Playwright |
| Docker | Container Images | Python, Docker SDK |
| DeepEval | LLM Evaluation | Python, DeepEval |
| SSH | Infrastructure / Compliance | Python, Paramiko |

**Shared architecture visual:** The 5-layer architecture all platforms share:
```
Test (Arrange / Act / Assert)
  └── Role (user persona, multi-task workflow)
       └── Task (single domain operation)
            └── Page/Interface Object (one target, atomic actions)
                 └── BrowserInterface / SSHInterface / DockerInterface
```

**Key message:** "From UI testing to LLM evaluation to compliance scanning — all managed by the same kernel."

## Section 7: The Loop

**Heading:** The Compounding Flywheel

**Visual:** Circular flow diagram:

```
Kernel governs → Factory builds specs → Specs become managed agents
       ^                                           |
       |                                           v
Kernel improves ← Learn loop captures failures ← Agents produce work
```

**Key message:** "Every agent makes the next one better. Every failure becomes a permanent lesson. The system compounds."

## Section 8: CTA

**Heading:** What domain do you need managed?

**Subheading:** Whether it's compliance, QA, healthcare, DevOps, or something we haven't built yet — the factory can compile it.

**Contact:** alain@isagawa.co

**Links:** GitHub (isagawa-co) | LinkedIn

## Section 9: Footer

- Copyright 2025 Isagawa
- Links: GitHub, LinkedIn, Email
- "Built with the Isagawa Kernel"

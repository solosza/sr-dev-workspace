# Architectural Blueprint — Pulsia-Equivalent System via Harness Design Pattern

## Overview

This blueprint defines six harness loops that compose into a Pulsia-equivalent autonomous company operating system. Each loop follows the harness primitive: Command → Skill → Steps → References, with gate contracts at every boundary. The system operates as a multi-tenant platform where each company instance runs its own CEO orchestrator loop nightly, delegating to five specialized primitive loops.

The architecture applies the five extensions identified in the harness applicability assessment: tenant-scoped state, cron scheduling, shared lessons (hive mind), cost-aware gates, and infrastructure provisioning.

---

## Loop 1: CEO Orchestrator Loop (Core Autonomous Orchestrator)

The CEO loop is the strategic decision-maker. It wakes on a cron schedule, assesses business state across all dimensions, selects the highest-leverage action, delegates to specialized loops, and produces a morning report. This is an **orchestrator loop** — it calls primitive loops sequentially based on strategic reasoning.

The CEO loop embodies the harness principle that "the agent IS the runtime." It reads the company's state files, applies strategic reasoning using the company's background context and historical decisions, and produces a prioritized action plan. It does not execute work directly — it delegates to primitive loops that handle engineering, marketing, ads, and support.

### Specification

```yaml
loop:
  name: ceo-orchestrator
  type: orchestrator
  schedule:
    type: cron
    expression: "0 2 * * *"  # 2 AM daily
    trigger_condition: "last_execution_age > 20h"

  command: "/company/{tenant_id}/ceo-cycle"

  input_gate:
    schema:
      tenant_id: { type: string, required: true }
      company_background: { type: object, required: true }
      historical_decisions: { type: array, items: "decision_record" }
      current_metrics: { type: object, properties: { revenue_30d: number, active_users: number, pending_bugs: number, pending_messages: number, ad_spend_30d: number } }
      budget_remaining: { type: number, required: true }
      shared_lessons: { type: array, items: "lesson_entry" }

  state_variables:
    cycle_id: "uuid"
    assessment_complete: false
    selected_action: null
    delegated_to: null
    delegation_result: null
    report_sent: false
    total_cost_this_cycle: 0

  steps:
    - name: assess-state
      action: "Read all tenant state files, evaluate business health across revenue, support, engineering, marketing dimensions"
      output_gate:
        assessment: { type: object, required: true }
        priority_scores: { type: object, properties: { engineering: number, marketing: number, ads: number, support: number, growth: number } }

    - name: select-action
      action: "Apply strategic reasoning to priority scores. Select highest-leverage action considering cost budget, historical outcomes, and shared lessons."
      decision_points:
        - condition: "pending_bugs > 0 AND bug_severity == 'critical'"
          action: "delegate to engineering loop"
        - condition: "revenue_30d < target AND ad_budget_available"
          action: "delegate to ad-management loop"
        - condition: "pending_messages > 0"
          action: "delegate to support loop"
        - condition: "no_critical_issues AND growth_opportunity_detected"
          action: "delegate to marketing loop"
        - condition: "cost_exceeds_budget"
          action: "escalate to human via escalation loop"
      output_gate:
        selected_action: { type: string, enum: [engineering, marketing, ads, support, escalation] }
        action_rationale: { type: string, min_length: 50 }
        estimated_cost: { type: number }

    - name: delegate-execution
      action: "Invoke the selected primitive loop with tenant-scoped inputs. Pass cost budget constraint."
      calls:
        - loop: "feature-coding"
          when: "selected_action == 'engineering'"
        - loop: "marketing-automation"
          when: "selected_action == 'marketing'"
        - loop: "ad-management"
          when: "selected_action == 'ads'"
        - loop: "human-escalation"
          when: "selected_action == 'escalation' OR estimated_cost > budget_remaining"
      output_gate:
        execution_result: { type: object, required: true }
        actions_taken: { type: array, items: "action_record" }
        cost_incurred: { type: number }

    - name: generate-report
      action: "Compile morning email summarizing actions taken, results, metrics changes, and plans for next cycle."
      output_gate:
        report: { type: object, properties: { subject: string, body: string, metrics_delta: object, next_cycle_plan: string } }
        report_sent: { type: boolean, value: true }

    - name: update-shared-lessons
      action: "If execution produced a generalizable insight, anonymize and submit to shared lessons aggregation."
      output_gate:
        lesson_submitted: { type: boolean }
        lesson_content: { type: string, nullable: true }

  hard_gates:
    - name: cost-limit
      rule: "total_cost_this_cycle <= budget_remaining"
      action: "BLOCK — escalate to human-escalation loop"
    - name: tenant-isolation
      rule: "all state reads/writes scoped to state/{tenant_id}/"
      action: "BLOCK — reject cross-tenant access"
```

---

## Loop 2: Autonomous Deployment Loop (Code → Test → Deploy)

The deployment loop handles the full engineering pipeline from code changes through testing to production deployment. It is a **primitive loop** — self-contained but callable by the CEO orchestrator. The loop enforces a strict gate between testing and deployment: code cannot reach production without passing automated QA verification.

This loop manages the Render hosting infrastructure for each tenant, interacting with GitHub for source control and Render's API for deployment triggers. The QA verification step is itself a gate contract — the deployment step's input gate requires a passing test report.

### Specification

```yaml
loop:
  name: autonomous-deployment
  type: primitive
  command: "/company/{tenant_id}/deploy"

  input_gate:
    schema:
      tenant_id: { type: string, required: true }
      code_changes: { type: array, items: { file: string, diff: string } }
      test_suite: { type: string, required: true }
      deploy_target: { type: string, enum: [staging, production] }
      max_cost: { type: number, required: true }

  state_variables:
    commit_sha: null
    tests_passed: false
    test_report: null
    deployed: false
    deploy_url: null
    rollback_sha: null

  steps:
    - name: commit-changes
      action: "Apply code changes to tenant's GitHub repository. Create commit with structured message."
      output_gate:
        commit_sha: { type: string, pattern: "^[a-f0-9]{40}$" }
        files_changed: { type: number }

    - name: run-tests
      action: "Execute test suite against committed changes in sandbox environment."
      output_gate:
        tests_passed: { type: boolean, required: true }
        test_report: { type: object, properties: { total: number, passed: number, failed: number, errors: array } }
      decision_points:
        - condition: "tests_passed == false AND failed <= 2"
          action: "attempt auto-fix, re-run tests (max 2 retries)"
        - condition: "tests_passed == false AND retries_exhausted"
          action: "STOP — report failure to CEO loop, do not deploy"

    - name: deploy
      action: "Trigger deployment to target environment via Render API."
      input_gate:
        tests_passed: { type: boolean, value: true }
      output_gate:
        deployed: { type: boolean, value: true }
        deploy_url: { type: string, format: "uri" }
        rollback_sha: { type: string }

    - name: verify-deployment
      action: "Health check deployed application. Verify HTTP 200 on critical endpoints."
      output_gate:
        health_check_passed: { type: boolean }
        response_time_ms: { type: number }
      decision_points:
        - condition: "health_check_passed == false"
          action: "trigger rollback to rollback_sha, report failure"

  hard_gates:
    - name: no-deploy-without-tests
      rule: "deploy step BLOCKED unless run-tests output_gate has tests_passed: true"
      action: "BLOCK"
    - name: cost-budget
      rule: "total API tokens used <= max_cost"
      action: "BLOCK — return partial result to CEO loop"
```

---

## Loop 3: Feature Coding Loop (Specification → Generation → Validation)

The feature coding loop translates high-level feature requests into working code. It reads a feature specification, generates code using LLM, validates the output against acceptance criteria, and hands off to the deployment loop. This is a **primitive loop** that the CEO orchestrator calls when engineering work is the highest priority.

The key architectural decision is separating feature coding from deployment. The feature coding loop produces validated code changes; the deployment loop handles testing and shipping. This separation allows the CEO loop to batch multiple feature coding outputs before triggering a single deployment, or to route code through additional review gates.

### Specification

```yaml
loop:
  name: feature-coding
  type: primitive
  command: "/company/{tenant_id}/code-feature"

  input_gate:
    schema:
      tenant_id: { type: string, required: true }
      feature_spec: { type: object, properties: { title: string, description: string, acceptance_criteria: array, priority: string } }
      codebase_context: { type: object, properties: { repo_url: string, branch: string, tech_stack: array, existing_patterns: array } }
      max_cost: { type: number, required: true }

  state_variables:
    generated_files: []
    validation_passed: false
    iteration_count: 0
    max_iterations: 3

  steps:
    - name: analyze-codebase
      action: "Read existing codebase structure, identify relevant files, understand patterns and conventions."
      output_gate:
        relevant_files: { type: array, items: string }
        patterns_identified: { type: array, items: string }
        implementation_plan: { type: string, min_length: 100 }

    - name: generate-code
      action: "Generate implementation code following identified patterns. Produce file diffs."
      output_gate:
        generated_files: { type: array, items: { file: string, content: string, action: string } }
        estimated_tokens: { type: number }

    - name: validate-output
      action: "Check generated code against acceptance criteria. Verify syntax, pattern adherence, and completeness."
      output_gate:
        validation_passed: { type: boolean }
        criteria_results: { type: array, items: { criterion: string, passed: boolean, notes: string } }
      decision_points:
        - condition: "validation_passed == false AND iteration_count < max_iterations"
          action: "return to generate-code with validation feedback"
        - condition: "validation_passed == false AND iteration_count >= max_iterations"
          action: "STOP — report inability to satisfy criteria"

    - name: handoff-to-deployment
      action: "Pass validated code changes to autonomous-deployment loop."
      input_gate:
        validation_passed: { type: boolean, value: true }
      output_gate:
        deployment_triggered: { type: boolean }
        code_changes: { type: array }

  hard_gates:
    - name: iteration-limit
      rule: "iteration_count <= max_iterations"
      action: "BLOCK — prevent infinite generation loops"
    - name: cost-budget
      rule: "cumulative tokens <= max_cost"
      action: "BLOCK — return best-effort result"
```

---

## Loop 4: Marketing Automation Loop (Content → Publish → Analyze)

The marketing automation loop handles content generation, multi-channel publishing, and performance analytics. It operates as a **primitive loop** that generates marketing content (Twitter posts, email campaigns, landing page copy), publishes through platform integrations, and feeds performance data back into the CEO loop's decision-making state.

The loop's analytics step writes performance metrics to the tenant's state files, which the CEO loop reads during its next nightly assessment. This creates a feedback cycle: marketing actions produce measurable outcomes that inform future strategic decisions. The shared lessons aggregation captures generalizable marketing insights (e.g., "emoji subject lines increase open rates") and distributes them across all tenants.

### Specification

```yaml
loop:
  name: marketing-automation
  type: primitive
  command: "/company/{tenant_id}/marketing"

  input_gate:
    schema:
      tenant_id: { type: string, required: true }
      campaign_type: { type: string, enum: [twitter, email_outreach, landing_page, content_marketing] }
      brand_context: { type: object, properties: { voice: string, audience: string, value_prop: string, competitors: array } }
      historical_performance: { type: array, items: "campaign_record" }
      shared_lessons: { type: array, items: "marketing_lesson" }
      max_cost: { type: number, required: true }

  state_variables:
    content_generated: null
    compliance_checked: false
    published: false
    publish_ids: []
    performance_snapshot: null

  steps:
    - name: generate-content
      action: "Create marketing content using brand context, historical performance data, and shared lessons. Apply learnings from cross-tenant insights."
      output_gate:
        content: { type: object, properties: { text: string, media: array, channel: string, scheduled_time: string } }
        content_type: { type: string }

    - name: compliance-check
      action: "Verify content meets platform rules — email unsubscribe buttons present, cold email limit (1/day), no prohibited claims, Meta/Anthropic compliance."
      output_gate:
        compliance_passed: { type: boolean, required: true }
        violations: { type: array, items: string }
      decision_points:
        - condition: "compliance_passed == false"
          action: "revise content to fix violations, re-check (max 2 retries)"

    - name: publish
      action: "Push content to target channel via API integration (Twitter API, AgentMail, Render for landing pages)."
      input_gate:
        compliance_passed: { type: boolean, value: true }
      output_gate:
        published: { type: boolean, value: true }
        publish_ids: { type: array, items: string }
        channel: { type: string }

    - name: collect-analytics
      action: "After publication window (24h for email, 48h for social), collect performance metrics and write to tenant state."
      output_gate:
        performance: { type: object, properties: { impressions: number, clicks: number, conversions: number, cost: number, roi: number } }
        lesson_candidate: { type: string, nullable: true }

  hard_gates:
    - name: email-rate-limit
      rule: "cold_emails_sent_today <= 1"
      action: "BLOCK — rate limit exceeded"
    - name: compliance-required
      rule: "publish step BLOCKED unless compliance_passed: true"
      action: "BLOCK"
```

---

## Loop 5: Ad Management Loop (Performance → Optimization → Bidding)

The ad management loop handles Meta ad campaigns across multiple countries. It analyzes current campaign performance, optimizes targeting and creative, adjusts bidding strategies, and manages UGC video generation (via Sora 2 integration). This is a **primitive loop** with a strong cost-awareness gate — ad spend directly impacts the tenant's budget, and the 20% revenue share on ad spend makes cost control architecturally critical.

The loop's optimization step uses historical performance data and shared lessons to make bid adjustments. Cross-tenant learning is especially valuable here: a targeting strategy that works for similar businesses in one market can be applied to new tenants entering the same space.

### Specification

```yaml
loop:
  name: ad-management
  type: primitive
  command: "/company/{tenant_id}/ads"

  input_gate:
    schema:
      tenant_id: { type: string, required: true }
      ad_accounts: { type: array, items: { platform: string, account_id: string, countries: array } }
      active_campaigns: { type: array, items: "campaign_object" }
      performance_history: { type: array, items: "daily_metrics" }
      budget_allocation: { type: object, properties: { daily_max: number, monthly_max: number, remaining: number } }
      shared_lessons: { type: array, items: "ads_lesson" }
      max_cost: { type: number, required: true }

  state_variables:
    analysis_complete: false
    optimizations_applied: []
    bids_adjusted: false
    creative_generated: false
    spend_this_cycle: 0

  steps:
    - name: analyze-performance
      action: "Pull current campaign metrics from Meta API. Calculate ROAS, CPA, CTR by country and creative variant."
      output_gate:
        campaign_metrics: { type: array, items: { campaign_id: string, roas: number, cpa: number, ctr: number, spend: number, conversions: number } }
        underperforming: { type: array, items: string }
        top_performers: { type: array, items: string }

    - name: optimize-targeting
      action: "Adjust audience targeting based on performance data and shared lessons. Reallocate budget from underperforming to top-performing segments."
      output_gate:
        optimizations: { type: array, items: { campaign_id: string, change_type: string, old_value: object, new_value: object } }
        projected_improvement: { type: number }
      decision_points:
        - condition: "all campaigns ROAS > 2.0"
          action: "maintain current targeting, increase budget allocation"
        - condition: "campaign ROAS < 0.5 for 7+ days"
          action: "pause campaign, reallocate budget"
        - condition: "new market opportunity detected via shared lessons"
          action: "create test campaign with small budget"

    - name: generate-creative
      action: "If creative refresh needed, generate new ad creative. For video ads, invoke Sora 2 UGC generation."
      output_gate:
        creatives_generated: { type: array, items: { type: string, content: object, estimated_cost: number } }
      decision_points:
        - condition: "creative_fatigue_detected (CTR declining 3+ days)"
          action: "generate new creative variants"
        - condition: "video_budget_available AND top_performer_identified"
          action: "generate UGC video ad via Sora 2"

    - name: adjust-bidding
      action: "Update bid strategies across all active campaigns based on optimization results."
      output_gate:
        bids_adjusted: { type: boolean, value: true }
        total_daily_budget: { type: number }
        budget_within_limits: { type: boolean, value: true }

  hard_gates:
    - name: budget-ceiling
      rule: "total_daily_budget <= budget_allocation.daily_max"
      action: "BLOCK — cap at daily maximum"
    - name: monthly-budget
      rule: "monthly_spend + projected_daily <= budget_allocation.monthly_max"
      action: "BLOCK — pause all campaigns until next billing cycle"
    - name: minimum-roas
      rule: "no new campaign creation if portfolio ROAS < 1.0"
      action: "BLOCK — optimize existing before expanding"
```

---

## Loop 6: Human Escalation Loop (Flag → Notify → Wait → Resume)

The human escalation loop is the safety valve for the entire system. It handles decisions that exceed agent authority, cost thresholds that require approval, and strategic inflection points where human judgment is needed. This is a **primitive loop** with a unique characteristic: it is the only loop in the system that intentionally pauses execution and waits for human input.

The escalation loop is called by any other loop when a hard gate blocks execution due to cost, authority, or confidence thresholds. It compiles the context of the blocked decision, sends a structured notification to the user, and writes a pending-decision record to tenant state. The CEO loop checks for resolved pending decisions during its next cycle and resumes the blocked workflow.

This loop preserves Pulsia's "action before permission" philosophy while providing a controlled escape hatch. The default mode is autonomous execution — escalation happens only when mechanical gates trigger, not when the agent is uncertain. Uncertainty is handled by the shared lessons system; escalation is reserved for authority boundaries.

### Specification

```yaml
loop:
  name: human-escalation
  type: primitive
  command: "/company/{tenant_id}/escalate"

  input_gate:
    schema:
      tenant_id: { type: string, required: true }
      escalation_reason: { type: string, enum: [cost_threshold, authority_boundary, strategic_inflection, repeated_failure, compliance_risk] }
      blocked_loop: { type: string, required: true }
      blocked_step: { type: string, required: true }
      context: { type: object, properties: { decision_needed: string, options: array, recommendation: string, cost_impact: number, risk_assessment: string } }
      urgency: { type: string, enum: [low, medium, high, critical] }

  state_variables:
    notification_sent: false
    notification_channel: null
    pending_decision_id: null
    user_response: null
    resolved: false

  steps:
    - name: compile-context
      action: "Gather full context of the blocked decision — what was attempted, why it was blocked, what options exist, and what the agent recommends."
      output_gate:
        decision_package: { type: object, properties: { summary: string, blocked_action: string, reason: string, options: array, recommendation: string, deadline: string } }

    - name: notify-user
      action: "Send structured notification via email (AgentMail) and dashboard alert. Include decision package with clear action options."
      output_gate:
        notification_sent: { type: boolean, value: true }
        notification_channel: { type: string }
        pending_decision_id: { type: string }

    - name: write-pending-decision
      action: "Write pending decision record to tenant state. CEO loop checks this during next cycle."
      output_gate:
        decision_record: { type: object, properties: { id: string, created: string, status: "pending", expires: string } }

    - name: check-response
      action: "Called by CEO loop during subsequent cycles. Check if user has responded via email reply or dashboard."
      output_gate:
        resolved: { type: boolean }
        user_decision: { type: string, nullable: true }
        resume_action: { type: string, nullable: true }
      decision_points:
        - condition: "user_responded == true"
          action: "mark resolved, pass user_decision back to blocked loop for resumption"
        - condition: "deadline_passed AND urgency != 'critical'"
          action: "apply agent recommendation, mark auto-resolved"
        - condition: "deadline_passed AND urgency == 'critical'"
          action: "maintain block, send follow-up notification"

  hard_gates:
    - name: no-auto-resolve-critical
      rule: "critical escalations cannot be auto-resolved"
      action: "BLOCK — must wait for human response"
```

---

## Loop Composition and Inter-Loop Communication

### Composition Architecture

The six loops compose in a hub-and-spoke pattern with the CEO orchestrator at the center:

```
                    ┌─────────────────────┐
                    │   CEO Orchestrator   │
                    │   (cron: nightly)    │
                    └─────────┬───────────┘
                              │
              ┌───────┬───────┼───────┬──────────┐
              │       │       │       │          │
              ▼       ▼       ▼       ▼          ▼
         ┌────────┐┌──────┐┌─────┐┌──────┐┌──────────┐
         │Feature ││Market││ Ad  ││Deploy││ Human    │
         │Coding  ││Auto  ││Mgmt ││      ││Escalation│
         └───┬────┘└──────┘└─────┘└──────┘└──────────┘
             │                       ▲
             └───────────────────────┘
             (code changes → deploy)
```

### Communication Pattern

Loops communicate exclusively through **tenant-scoped state files** and **gate contract outputs**. There is no direct inter-loop messaging or shared memory bus. This design ensures:

1. **Tenant isolation** — All state reads and writes are scoped to `state/{tenant_id}/`. No loop can access another tenant's data.

2. **Deterministic handoff** — The CEO loop's `delegate-execution` step passes structured input that satisfies the target loop's input gate. If the gate rejects the input, execution fails cleanly rather than producing undefined behavior.

3. **Asynchronous composition** — The feature coding loop produces code changes that the deployment loop consumes. The CEO loop can batch multiple feature outputs before triggering deployment, or trigger deployment immediately. The composition is orchestrated, not hardwired.

4. **Cost propagation** — Every loop receives a `max_cost` input and reports `cost_incurred` in its output gate. The CEO loop tracks cumulative cost across all delegated loops and triggers escalation if the total exceeds the cycle budget.

5. **Lesson propagation** — Each loop can submit lesson candidates to the shared lessons aggregation. The CEO loop reads shared lessons during its assessment step and passes relevant lessons to primitive loops via their input gates. This creates a two-way knowledge flow: bottom-up (primitive loops discover insights) and top-down (CEO loop distributes cross-tenant knowledge).

### State Flow Between Cycles

```
Cycle N                           Cycle N+1
────────                          ────────
CEO assesses state ──────────────→ CEO reads updated state
  ↓                                  ↑
Delegates to loops                   │
  ↓                                  │
Loops execute, write results ────────┘
  ↓
Loops submit lessons ────→ Shared lessons aggregation
                                     ↓
                           CEO reads shared lessons ──→ passes to loops
```

Each cycle is self-contained: the CEO loop reads state, acts, and writes results. The next cycle reads the updated state. There is no persistent connection between cycles — the state files are the only continuity mechanism. This matches Pulsia's nightly cycle model where each CEO instance "wakes up" fresh and evaluates the current state without assuming anything about prior cycles.

---

## Feasibility Assessment

The harness design pattern supports this architecture without fundamental changes to its core model. The six loops use standard harness primitives — commands, skills, steps, gate contracts, and state files. The five extensions (tenant scoping, cron scheduling, shared lessons, cost gates, provisioning) add capabilities without replacing existing mechanisms.

Key feasibility indicators:

- **Tenant isolation** is a namespace extension to existing state management — no new primitives needed
- **Cron scheduling** adds a trigger mechanism but the loop execution model is unchanged
- **Cost-aware gates** extend the existing gate contract schema with one additional field
- **Shared lessons** reuse the existing lessons infrastructure with an aggregation layer on top
- **Loop composition** follows the orchestrator-calls-primitive pattern already documented in the harness spec

The architecture demonstrates that the harness design pattern — specification-first, agent-driven orchestration via composable loops — scales from single-session developer tooling to multi-tenant autonomous business operations. The gap is not in the pattern's expressiveness but in the infrastructure layer (multi-tenant state, scheduling, cross-tenant aggregation) that sits beneath the specification layer.

---

## Sources

- Harness Design Pattern documentation (`docs/harness-design-pattern/`)
- Pulsia architecture analysis (`projects/pulsia-research/02-architecture.md`)
- Pulsia company overview (`projects/pulsia-research/01-company-overview.md`)
- Harness applicability assessment (`projects/pulsia-research/03-harness-applicability.md`)

# Use Case Scenario

A real-world walkthrough: building a QA platform with Isagawa Kernel governance. Shows the end-to-end flow from defining a domain to shipping a governed, self-improving automation platform.

**Audience:** Business stakeholders, decision-makers

```mermaid
journey
    title Building a QA Platform with Kernel Governance
    section 1. Define Domain
        Write domain spec with compliance rules: 5: Team Lead
        Specify test patterns and allowed selectors: 4: Team Lead
        Define quality gates and anti-patterns: 4: Team Lead
    section 2. Set Up Kernel
        Run /kernel/domain-setup: 5: Kernel
        Protocol, hooks, commands auto-generated: 5: Kernel
        Enforcement active from first action: 5: Kernel
    section 3. Build Features
        Task-builder decomposes into atomic tasks: 5: Kernel
        Run-task.sh executes each task autonomously: 5: Kernel
        Every action logged and gate-checked: 4: Kernel
    section 4. Enforce Compliance
        Hook blocks non-compliant code automatically: 5: Hooks
        Agent receives remediation guidance: 4: Hooks
        No manual code review needed for compliance: 5: Hooks
    section 5. Learn from Failures
        Test failure detected by hook: 5: Kernel
        Lesson recorded with root cause: 4: Kernel
        Hooks updated to prevent recurrence: 5: Kernel
    section 6. Ship with Confidence
        Prod-test validates complete platform: 5: Kernel
        All gates passed, compliance verified: 5: Kernel
        Audit trail available in actions log: 5: Kernel
```

## Business Value at Each Stage

```mermaid
graph LR
    subgraph "Without Kernel"
        A1["Manual code review"] --> A2["Inconsistent standards"]
        A2 --> A3["Repeated mistakes"]
        A3 --> A4["Slow delivery"]
    end

    subgraph "With Kernel"
        B1["Automated enforcement"] --> B2["Consistent from day one"]
        B2 --> B3["Self-improving rules"]
        B3 --> B4["Fast, confident delivery"]
    end

    style A1 fill:#8b1a1a,stroke:#cd3333,color:#fff
    style A2 fill:#8b1a1a,stroke:#cd3333,color:#fff
    style A3 fill:#8b1a1a,stroke:#cd3333,color:#fff
    style A4 fill:#8b1a1a,stroke:#cd3333,color:#fff
    style B1 fill:#2d5016,stroke:#4a8c2a,color:#fff
    style B2 fill:#2d5016,stroke:#4a8c2a,color:#fff
    style B3 fill:#2d5016,stroke:#4a8c2a,color:#fff
    style B4 fill:#2d5016,stroke:#4a8c2a,color:#fff
```

## Key Outcomes

| Metric | Without Kernel | With Kernel |
|--------|---------------|-------------|
| Compliance enforcement | Manual review (hours) | Automatic (milliseconds) |
| Knowledge retention | Tribal / undocumented | Lessons file + protocol updates |
| Onboarding new agents | Re-learn everything | Inherit all lessons automatically |
| Failure recurrence | Common (same mistakes) | Rare (hooks updated after each) |
| Audit trail | None or manual | Complete (actions.jsonl) |
| Delivery confidence | Uncertain | All gates passed |

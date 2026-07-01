# Cross-Harness Testing Architecture Design

## Status
NEW — Research phase, designing framework architecture

## Location
`workspace:docs/harness-design-pattern` (research documentation)

## Purpose

Design the architecture of a testing framework that can evaluate and compare multiple AI harnesses in a systematic, scalable, and reproducible way. The framework should support: running test cases against multiple harnesses in parallel, collecting metrics, generating comparative reports, and identifying performance deltas.

## Key Questions

- What does the system architecture look like (components, data flow)?
- How do we provision multiple harnesses in a testbed?
- How do we execute tests in parallel without interference?
- How do results get aggregated and compared?
- What deployment model (cloud, local, CI/CD)?
- How do we handle closed-source harnesses vs. open-source?

## Research Areas

### 1. System Architecture

**Status:** NEW — needs design

High-level components:
```
Test Orchestrator
  ├─ Test Loader (reads test cases from library)
  ├─ Test Scheduler (distributes to workers)
  ├─ Harness Manager (provisions, monitors)
  └─ Results Aggregator (collects metrics, compares)

Testbed Layer
  ├─ Harness Instance 1 (provisioned with deps)
  ├─ Harness Instance 2 (isolated environment)
  ├─ Model Layer (LLM backend, shared or isolated?)
  └─ Context Manager (state, token tracking)

Metrics Collection
  ├─ Logger (harness events, decisions, errors)
  ├─ Meter (token count, timing, quality scores)
  ├─ Aggregator (per-test, per-harness, per-metric)
  └─ Comparator (delta calculation, statistical analysis)

Reporting
  ├─ Report Generator (HTML, JSON, tables)
  ├─ Dashboard (real-time progress, results)
  └─ Archive (historical data, trend analysis)
```

**Design questions:**
- Monolithic vs. microservices?
- Synchronous vs. async execution?
- Single process vs. distributed?

### 2. Harness Provisioning Strategy

**Status:** NEW — needs specification

For each harness type:

**Claude Code (open source):**
- Git clone, local installation
- Inject instrumentation
- Configure via settings
- Run locally or containerized

**Cursor (closed source):**
- API integration (if available)
- Behavioral testing (black-box)
- No instrumentation possible
- Requires auth/licensing

**Custom harnesses (internal):**
- Custom loaders
- Instrumentation capability
- Full access to internals
- Can run in same process

**Deployment options:**
- Local processes (simplest, limited concurrency)
- Docker containers (isolation, scalability)
- Kubernetes pods (production scaling)
- Cloud VMs (access to closed-source tools)

### 3. Test Execution Model

**Status:** NEW — needs design

Test execution flow:
```
1. Load test cases from library
2. For each test case:
   a. Initialize testbed (provision harnesses, warm up)
   b. Execute test against harness A (collect logs, metrics)
   c. Execute test against harness B (collect logs, metrics)
   d. Cleanup (state reset, resource cleanup)
3. Aggregate results per-harness
4. Calculate deltas (A vs. B performance)
5. Generate report
6. Archive results (for trend analysis)
```

**Concurrency considerations:**
- Can we run tests in parallel against same harness? (No — shared state)
- Can we run same test against different harnesses in parallel? (Maybe — depends on model sharing)
- How do we handle test ordering (some tests depend on prior state)?

### 4. Metrics Collection & Comparison

**Status:** NEW — needs specification

**Per-test metrics collected:**
- Input: prompt, test case parameters
- Execution: time, token count, turns, errors
- Output: result quality, decision accuracy, context usage
- Errors: failure type, recovery success

**Aggregation levels:**
- Per-test (single test case, single harness)
- Per-harness (all tests, one harness)
- Comparative (test A: harness X vs. harness Y)
- Dimensional (e.g., all context-management tests)

**Comparison methods:**
- Absolute delta (A score - B score)
- Relative delta (A score / B score)
- Statistical significance (is delta real or noise?)
- Trend (how does gap evolve over time?)

**Report structure:**
```
Executive Summary
├─ Overall performance delta (X.X points)
├─ Key findings (biggest gaps, quick wins)
└─ Recommendation (priority improvements)

Detailed Analysis
├─ Per-dimension breakdown (context, decision-making, etc.)
├─ Per-test results (which tests expose the gap?)
├─ Statistical summary (confidence, variance)
└─ Failure analysis (error types, recovery patterns)

Comparative Tables
├─ Metric matrix (all metrics × all harnesses)
├─ Test results (pass/fail, score distribution)
└─ Trend history (how gaps changed over time)

Appendix
├─ Test case definitions
├─ Environment details (model, temperature, etc.)
└─ Raw data (detailed logs for drill-down)
```

### 5. Data Storage & Retrieval

**Status:** NEW — needs specification

What to store:
- Test definitions (code + metadata)
- Test execution logs (per-harness, per-test)
- Metrics snapshots (pre-aggregated summaries)
- Reports (generated analyses)
- Metadata (timestamp, harness version, model version, environment)

Storage options:
- File system (JSON/CSV for simple cases)
- Database (PostgreSQL for relational queries)
- Time-series DB (InfluxDB for trends)
- Data warehouse (for large-scale analysis)

Querying patterns:
- "What tests show the biggest delta between harness A and B?"
- "How has harness X's score on metric Y changed over time?"
- "Which tests are most flaky (high variance)?"
- "What's the trend in context management efficiency?"

### 6. CI/CD Integration

**Status:** NEW — needs strategy

Integration points:
- **Pre-commit:** Run harness tests locally (fast subset)
- **PR validation:** Full comparative testing (baseline vs. variant)
- **Nightly:** Full suite + all harnesses (comprehensive)
- **Release:** Archive results for historical comparison

**Automation:**
- Test trigger (on code change, manual trigger, scheduled)
- Harness provisioning (auto-update, version pinning)
- Result archival (persist to database)
- Alert on regression (notify if score drops)

## Output

- **Architecture diagram:** Components, data flow, interaction patterns
- **Deployment models:** Local, containerized, cloud options with trade-offs
- **Test execution specification:** Flow, concurrency, state management
- **Metrics collection design:** What to collect, aggregation levels, comparison methods
- **Data schema:** How results are stored and queried
- **CI/CD integration plan:** Where testing fits in development workflow
- **Tool requirements:** What would need to be built vs. reused
- **Timeline estimate:** How long to build each component

## Dependencies

Depends on: [[134-kernel-research-cross-harness-testing/harness-testing-patterns]] (what to test)

## Notes

Focus on feasibility — what's achievable with current tools vs. what requires custom development.

# External Governance Models — Applicable Patterns

**Backlog:** 151 — Governance Depth Over Breadth
**Task:** 004-research-external-governance-models
**Constraint:** No new features. Extract applicable patterns for deepening existing kernel mechanisms.

---

## 1. Unix Philosophy — Governance Through Composition

### Model Summary

Unix achieves system-wide governance through small, single-purpose tools composed via pipes. Key principles:
- Do one thing well
- Expect output to become input for another program
- Fail loudly and immediately (non-zero exit codes)
- Text as universal interface

### Governance Mechanism

Unix doesn't have a central governance authority. Instead, governance emerges from:
- **Convention enforcement** — file permissions, PATH resolution, standard streams
- **Composition contracts** — stdin/stdout/stderr as universal interface
- **Failure propagation** — `set -e` in scripts means first failure stops everything
- **Minimal privilege** — each tool only accesses what it needs

### Applicable Pattern → Kernel

**Composition over control.** The kernel's 4 hooks are already Unix-like: each does one thing (gate, log, detect, approve). The lesson is that governance depth comes from making each hook's single responsibility sharper, not from adding hooks.

**Specific application:**
- The universal-gate-enforcer currently checks 5 gates in one hook. Unix would say: 5 checks = 5 hooks. But the kernel constraint says no new hooks. Resolution: the 5 gates are stages within a single pipeline (acceptable — like `awk` having multiple pattern/action pairs).
- Failure propagation is already correct: hook blocks → agent can't proceed.
- **Gap:** Unix has no concept of "learning from failure." Failure stops execution; it doesn't improve the system. The kernel's learn loop is a governance innovation beyond Unix's model.

---

## 2. Microkernel OS Design (seL4, L4, QNX)

### Model Summary

Microkernels minimize the trusted computing base (TCB). Only essential services run in kernel space: IPC, memory management, scheduling. Everything else (drivers, filesystems, networking) runs in user space with capability-based access control.

Key properties:
- **Minimal TCB** — fewer lines of code in kernel = fewer bugs = provable correctness (seL4 is formally verified)
- **Capability-based security** — processes hold unforgeable tokens granting specific access
- **Fault isolation** — user-space crash doesn't bring down the kernel
- **Message passing** — all inter-process communication through IPC, no shared memory

### Governance Mechanism

- **Capability delegation** — parent process grants capabilities to children; capabilities cannot be manufactured
- **Kernel as referee** — kernel only validates capability tokens, never makes policy decisions
- **Policy in user space** — governance rules live outside the kernel, enforced by the kernel's capability checks

### Applicable Pattern → Kernel

**The kernel should validate tokens, not make decisions.** seL4's insight: the kernel checks that you HAVE a capability, not whether you SHOULD have it. Policy lives elsewhere.

**Specific application:**
- The universal-gate-enforcer currently checks `session_started`, `needs_learn`, `anchored`, `actions_since_anchor`, `anchor_token_confirmed`. These are capability-like checks: "do you hold the token?"
- The kernel doesn't decide WHAT to learn or WHEN to anchor (policy) — it only validates that learning/anchoring happened (mechanism).
- **This is already correct.** The kernel's hook design is microkernel-aligned: mechanism (hook validates state) separated from policy (commands decide what to do).
- **Gap:** The kernel lacks **fault isolation between governance states.** If `session_state.json` corrupts, all governance fails. seL4 would isolate each capability's state. Currently mitigated by per-agent state files (lesson from multi-agent orchestration), but kernel-level governance still depends on single shared state.

**Deepening opportunity:** The anchor token (`pending_anchor_token` → `anchor_token_confirmed`) IS a capability token. It's unforgeable (set by hook, cleared by anchor command). This pattern could be formalized: every governance transition produces a token that the next gate validates.

---

## 3. Erlang/OTP Supervisors — Let-It-Crash Governance

### Model Summary

Erlang's governance model assumes failure is inevitable and governs through structured recovery:
- **Supervision trees** — hierarchical process management
- **Let it crash** — processes don't handle errors defensively; they crash and supervisors restart them
- **Restart strategies** — one-for-one, one-for-all, rest-for-one
- **Intensity/period** — maximum N restarts in T seconds before escalating to parent supervisor

### Governance Mechanism

- **Escalation** — if a child crashes too often, the supervisor itself crashes, escalating to its parent
- **Isolation** — one process crash doesn't affect siblings (unless using one-for-all strategy)
- **Declarative recovery** — restart rules are declared at configuration time, not runtime
- **Idempotent initialization** — processes must be restartable from any state (via `init/1`)

### Applicable Pattern → Kernel

**Structured failure escalation with intensity limits.** The kernel's current model: test fails → fix → learn. But there's no escalation if the agent keeps failing.

**Specific application:**
- The kernel currently allows infinite fix-learn cycles. Erlang would say: if the same test fails 3 times in the same anchor period, ESCALATE (stop the agent, surface to user).
- The `attempts_on_current` field in workflow state already tracks this. But the threshold is 3 → skip. Erlang's model suggests: 3 → escalate (report failure + ask for direction), not skip.
- **Let-it-crash maps to the hook block model.** When a hook blocks, the agent "crashes" — it can't proceed. The recovery path is explicit (invoke the command the hook tells you). This IS the OTP pattern.
- **Gap:** No restart intensity tracking across anchors. An agent could fail 2x per anchor indefinitely without triggering escalation. Erlang would track failures over a time window, not just within a single task attempt.

**Deepening opportunity:** The learn command could track failure frequency. If the same lesson trigger recurs 3+ times across anchors, the learn output should flag: "recurring failure — requires architectural fix, not behavioral fix."

---

## 4. Kubernetes Admission Controllers — Layered Enforcement Without API Expansion

### Model Summary

Kubernetes admission controllers intercept API requests between authentication and persistence. They validate or mutate resources without expanding the Kubernetes API:
- **Mutating admission** — modifies the request (adds defaults, injects sidecars)
- **Validating admission** — accepts or rejects the request
- **Webhook-based** — external services can hook into the admission chain
- **Ordered chain** — controllers execute in sequence; any rejection stops the chain

### Governance Mechanism

- **Pre-persistence interception** — governance checks happen BEFORE state changes
- **Chain composition** — multiple independent validators, each checking one concern
- **No API expansion** — new governance rules add webhooks, not new API endpoints
- **Fail-closed** — if a webhook is unreachable, the request is rejected (safe default)

### Applicable Pattern → Kernel

**Pre-write interception is the correct enforcement point.** The kernel already does this: PreToolUse hooks intercept Write/Edit/Bash before execution. This is the admission controller pattern exactly.

**Specific application:**
- The universal-gate-enforcer is a mutating+validating admission controller: it checks state (validating) and produces block messages that redirect behavior (mutating — telling the agent what to do next).
- **Chain ordering matters.** Kubernetes executes mutating before validating. The kernel runs gates 1-5 sequentially in one hook — any failing gate blocks. This is correct.
- **Fail-closed is already implemented.** If state files are missing or corrupt, the hook blocks rather than allowing. This is the safe default.
- **Gap:** Kubernetes admission controllers are independently deployable (webhooks). The kernel's gates are monolithic (one file). If a gate has a bug, all enforcement fails. Kubernetes would isolate each gate as a separate webhook. Within the "no new hooks" constraint, this means: each gate function within universal-gate-enforcer.py should be independently testable, with its own failure mode (not a shared try/catch).

**Deepening opportunity:** The PostToolUse hook (actions-log-appender) is analogous to an audit webhook — it observes but doesn't block. The test-failure-detector is a validating admission for Bash specifically. The pattern is already layered correctly. Depth comes from making each layer's checks more precise, not from adding layers.

---

## 5. Governance Research — Minimal Effective Governance & Principal-Agent Theory

### Model Summary

From organizational governance and economics:
- **Minimal effective governance** (Ostrom) — governance rules should be the minimum necessary to prevent commons destruction
- **Principal-agent problem** — the agent (executor) has different incentives than the principal (owner), creating moral hazard
- **Mechanism design** — design rules so that the agent's self-interest aligns with the principal's goals
- **Credible commitment** — governance is only effective if enforcement is credible (violators actually face consequences)

### Governance Mechanism

- **Ostrom's 8 principles** — clear boundaries, proportional costs/benefits, collective choice, monitoring, graduated sanctions, conflict resolution, local autonomy, nested governance
- **Self-enforcing contracts** — rules that are cheaper to follow than to break
- **Transparency** — observable actions reduce moral hazard
- **Graduated sanctions** — first violation gets a warning, repeat violations get escalation

### Applicable Pattern → Kernel

**The kernel IS a principal-agent governance system.** The user (principal) delegates to the AI agent. The agent has "incentives" to skip steps (speed, context window pressure). Governance must make compliance cheaper than violation.

**Specific application:**
- **Credible commitment** — hooks make enforcement credible. The agent literally cannot bypass them. This is stronger than human governance (where enforcement is probabilistic).
- **Self-enforcing contracts** — the anchor command is self-enforcing: it provides value (context recovery, protocol refresh) AND is mandatory. Good design: compliance has intrinsic benefit.
- **Graduated sanctions** — currently missing. The kernel has binary enforcement: blocked or allowed. Erlang/OTP's intensity model and Ostrom's graduated sanctions both suggest: first violation = block + message, repeated violations = stronger response (e.g., require manual user intervention, not just a learn cycle).
- **Transparency** — the actions.jsonl log provides full transparency. The anchor Part B review is the monitoring mechanism. This is well-aligned with Ostrom's monitoring principle.
- **Gap:** No proportional governance. Complex tasks and simple tasks face the same governance overhead (anchor every 10 actions). Ostrom would say: governance burden should be proportional to the risk of the action. A Write to a state file and a Write to production code carry different risk but identical governance cost.

**Deepening opportunity:** The `actions_limit` (currently 10) could be context-sensitive. If all actions since last anchor are reads/state updates, the limit could be higher. If actions include production code writes, the limit could be lower. This is proportional governance without new mechanisms — just smarter thresholds in the existing hook.

---

## Comparison Table

| Model | Core Mechanism | Kernel Equivalent | Gap / Deepening Opportunity |
|-------|---------------|-------------------|----------------------------|
| **Unix** | Composition of single-purpose tools + failure propagation | 4 hooks, each single-purpose; hook block = failure propagation | No learning from failure (Unix stops; kernel learns) — kernel already surpasses |
| **seL4 Microkernel** | Capability tokens + mechanism/policy separation | Anchor token = capability; hooks = mechanism, commands = policy | No fault isolation between governance states; single state file dependency |
| **Erlang/OTP** | Supervision trees + restart intensity + escalation | attempts_on_current + fix→learn cycle | No cross-anchor failure intensity tracking; no escalation beyond skip |
| **K8s Admission** | Pre-persistence interception chain + fail-closed | PreToolUse gates + ordered checks + block-on-missing-state | Monolithic gate function (not independently testable per gate) |
| **Ostrom/Principal-Agent** | Minimal rules + proportional cost + graduated sanctions + monitoring | Minimal hooks + actions.jsonl + anchor review | No proportional governance (all actions equal cost); no graduated sanctions |

---

## Governance Problems the Current Kernel Cannot Solve

1. **Cascading state corruption** — If `session_state.json` becomes inconsistent (e.g., `needs_learn: true` but no trigger recorded), all governance gates may block permanently. No self-healing mechanism exists. (seL4 would isolate; Erlang would restart from known good state.)

2. **Repeated behavioral failure without escalation** — An agent can fix→learn the same mistake indefinitely. No mechanism detects "this is the 5th time the same lesson has been recorded" and escalates to architectural intervention. (Erlang's intensity/period would catch this.)

3. **Disproportionate governance overhead** — A 10-action research task (all reads) faces the same anchor ceremony as a 10-action production code change. This incentivizes the agent to batch risky actions to "get more done" between anchors. (Ostrom's proportionality principle says: match governance to risk.)

4. **No governance over governance** — Who validates that the hooks themselves are correct? A bug in universal-gate-enforcer.py could silently disable all enforcement. No meta-governance mechanism exists. (Kubernetes uses admission controller testing + canary deployments; seL4 uses formal verification.)

5. **Binary enforcement without nuance** — Current model: allowed or blocked. No "warn and continue" mode for low-risk violations. No "block and require user approval" for high-risk violations. All violations are treated identically. (Ostrom's graduated sanctions; K8s has warn vs. deny admission modes.)

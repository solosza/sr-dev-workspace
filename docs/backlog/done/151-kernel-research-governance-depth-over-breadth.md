# Research: Improve Governance Depth Within Minimal Kernel

## Status
Open

## Priority
Medium — depends on backlog 150 (feature freeze decision). Once the boundary is locked, this research defines how to make the remaining features better rather than adding new ones.

## Summary
Given the feature freeze from backlog 150, the kernel's remaining surface area is small: the loop (session-start, anchor, work, learn, complete), enforcement hooks, domain-setup, and lessons. Instead of adding features, research how to make these governance primitives deeper, more reliable, and more powerful. How can each existing piece be improved without expanding scope? What does world-class governance look like within these constraints?

## Research Questions

### The Loop
- Is the current loop shape (session-start, anchor, work, learn, complete) optimal, or should steps be merged/reordered?
- Is the anchor interval (every 10 actions) the right cadence? Should it be adaptive based on task complexity?
- How does the learn mechanism compare to other self-improving systems? What's missing from the feedback loop?
- Should complete have stronger verification before allowing task closure?

### Enforcement Hooks
- Are the current 4 hooks (gate enforcer, actions log, test failure detector, auto-approve writes) sufficient for governance?
- Should enforcement be more granular (per-file, per-domain rules) without adding new hooks?
- How do other governance systems (Kubernetes admission controllers, Git hooks, CI gates) handle enforcement depth?
- What's the failure mode analysis for the current hooks? Where can agents still drift?

### Domain Setup
- Is the current self-building approach (scan repo, extract patterns, write protocol) the best way to bootstrap governance?
- How can protocol quality improve without adding steps?
- Should domain-setup produce stronger initial enforcement (tighter gates by default)?

### Lessons System
- Is the current lesson format (issue, root cause, fix, anti-pattern, quality gate) capturing enough signal?
- How should lessons compound over time? Decay? Promote to hard rules?
- What's the relationship between lessons and hook updates? Should lessons auto-generate enforcement?

### General
- What does the governance research literature say about minimal effective governance?
- How do other minimal systems (Unix philosophy, microkernel OS design, Erlang/OTP supervisors) achieve depth without breadth?
- What governance problems exist that the current kernel cannot solve without adding features?

## Requirements
- Research each governance primitive in isolation
- Compare against external systems (K8s admission controllers, OTP supervisors, Git hook pipelines)
- Identify improvement opportunities that don't add new files or commands
- Produce concrete recommendations: what to tighten, what to make adaptive, what to remove
- Stay within the "kernel governs, extensions do everything else" principle from backlog 150

## References
- Backlog 150: `docs/backlog/150-kernel-refactor-minimalize-kernel.md` (feature freeze policy)
- Backlog 147: `docs/backlog/147-kernel-refactor-define-kernel-boundary.md` (what's core)
- isagawa-kernel repo (the actual implementation to improve)
- Backlog 145 (done): production readiness critiques (external assessment of kernel gaps)
- Backlog 146 (done): state isolation and CI solutions

## Task Builder Input
- **Deliverable:** Research report with concrete improvement recommendations for each governance primitive, constrained to minimal kernel boundary
- **Location:** subproject:kernel-governance-depth
- **Scope:** RESEARCH
- **Constraints:** No new features, no new commands, no new hooks. Improvements must deepen existing mechanisms only. Backlog 150 feature freeze is the hard constraint.

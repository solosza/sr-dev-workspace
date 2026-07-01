# Credibility Fixes: Remove Overstated Claims

## Claim 1: "Cannot be bypassed" Language
**Location:** Kernel README + site references
**Current:** "They cannot be bypassed. Not by the agent, not by prompt engineering, not by editing state files."
**Issue:** Sounds like marketing hype to skeptical engineers
**Replace with:** "The kernel blocks normal agent tool use when required protocol, validation, or learning steps are incomplete."
**Rationale:** More precise, still strong, technically accurate

## Claim 2: "Mechanically can't violate" / "Physically cannot skip"
**Location:** Kernel README, potential site messaging
**Current:** "The agent mechanically can't violate the spec" / "physically cannot skip checks"
**Issue:** Too absolute, sounds like marketing
**Replace with:** Same as Claim 1 replacement
**Rationale:** Hooks block tool use, not "physically" prevent violations

## Claim 3: "No human intervention between start and finish"
**Location:** Self-Extension section, "90+ pipelines" card (index.html line 141)
**Current:** "90+ completed pipelines across 50+ repos. No human intervention between start and finish."
**Issue:** Misleading — architecture includes HITL where needed
**Replace with:** "90+ completed pipelines across 50+ repos. Autonomous for deterministic execution; HITL for approvals, failures, and judgment points."
**Rationale:** Accurate and mature-sounding. Shows we understand when human judgment is needed.

## Claim 4: "Natural Language" as Feature
**Location:** Multiple sections (hero, growth, self-extension)
**Current:** Emphasized in marketing as key feature
**Issue:** Overstates NL capability, suggests LLM-driven features
**Replace with:** Use "intent" instead, focus on the spec-driven architecture
**Rationale:** More honest about what the system actually does

## Summary
All fixes maintain strength while improving credibility. The goal: sound like mature infrastructure, not AI hype.

# Legal and IP Analysis

## Component Ownership

### The Core Question

When the agent builds a component from `_reference/` patterns during a user's evaluation run, who owns that component? Three parties are involved:

1. **The platform** — owns the `_reference/` patterns, the agent, and the kernel
2. **The user** — submitted the artifact that triggered component creation
3. **The AI agent** — generated the code (not a legal person, cannot hold IP)

### Legal Landscape (2026)

The U.S. Copyright Office maintains that works generated entirely by AI without meaningful human authorship are not eligible for copyright registration. However, code produced with substantial human direction, review, and modification is more likely to qualify for copyright protection. The key factors are selection, coordination, arrangement, revision, curation, testing, and integration choices made by human engineers.

**Implication for our platform:** Agent-generated components are built from platform-owned `_reference/` patterns using platform-owned agent instructions. The user's artifact is the trigger but not the source material. The component is a derivative of platform IP, not user IP.

### Recommended Ownership Model

**Platform owns all generated components.** Rationale:

1. **Source material:** Components are derived from `_reference/` patterns owned by the platform, not from user submissions. The user's artifact triggers creation but doesn't contribute source code to the component.
2. **Human direction:** Platform engineers designed the `_reference/` patterns, the agent's component-building instructions, and the quality gates. This constitutes the "meaningful human authorship" required for copyright.
3. **Precedent:** Anthropic's terms of service assign Claude Code outputs to the user who directed the work. In this case, the platform is the "user" directing Claude via the Agent SDK — the end-user submitted an artifact, but the platform directed the agent's component-building behavior.
4. **Clean IP boundary:** If components were co-owned or user-owned, the component library would have fragmented IP — each component potentially encumbered by different user claims. This makes the library unlicensable and unusable.

### Risk Mitigation

- **Terms of Service:** Explicitly state that components generated during evaluation are platform property
- **No user code in components:** Agent instructions must never copy user submission code into a component — components are built from `_reference/` patterns only, with the user's artifact providing context (what needs to be tested) not content (code to incorporate)
- **Contributor License Agreement (CLA):** If a user explicitly contributes a component (not auto-generated), they sign a CLA assigning IP to the platform

## User Submission Boundaries

### Data Flow Contract

Users must understand exactly what enters the container, what leaves, and what gets retained:

| Data Type | Enters Container | Leaves Container | Retained |
|-----------|-----------------|-----------------|----------|
| User artifact (code, config, spec) | Yes (read-only mount) | No (destroyed with container) | No (unless user opts in) |
| User API keys | Yes (memory-only) | No | Never |
| Evaluation results (scores, pass/fail) | Generated inside | Yes (returned to user + stored) | Yes (user's dashboard) |
| Agent-generated components | Generated inside | Yes (enters curation queue) | Yes (if approved, joins library) |
| Container logs | Generated inside | Yes (platform debugging) | 30 days |

### Opt-In Contribution Model

By default, agent-generated components enter the curation queue. Users can opt out:

- **Default (opted in):** "Components generated during your evaluation may be added to the shared library after quality review. You will be credited as the trigger user."
- **Opt out:** "Your evaluation will still use existing library components, but any new components generated will be discarded after your run."
- **Enterprise override:** Enterprise customers can opt out at the account level for all runs.

**Incentive to opt in:** Users who contribute components get credit in the library (visible contribution count) and priority queue access. This aligns incentives — users want the library to grow because it makes their future evaluations better.

## Terms of Service Framework

Essential ToS clauses for the platform:

### License Grant
- User grants platform a limited, non-exclusive license to process submitted artifacts for the purpose of evaluation
- License terminates when the container is destroyed (artifacts are not retained)
- Platform may retain evaluation results for user dashboard display

### Liability Disclaimer
- Platform provides evaluation results "as-is" — no guarantee of accuracy or completeness
- Platform is not liable for decisions made based on evaluation results
- User is responsible for their own API key usage and costs

### API Key Usage
- User acknowledges that their API keys are used to make LLM API calls during evaluation
- Platform commits to never storing, logging, or transmitting API keys outside the container execution context
- Platform is not liable for API costs incurred during evaluation

### Component Library
- Components generated during evaluation are platform property (as established in Ownership section)
- User receives credit attribution for triggered components
- Platform may modify, version, or remove components from the library at its discretion

### DMCA / Takedown Process
- If a user believes a library component infringes their IP, they can submit a DMCA takedown request
- Platform will remove disputed components within 72 hours pending investigation
- Counter-notice process available for platform to dispute removal

### Account Termination
- Platform may suspend or terminate accounts for ToS violations, abuse, or malicious submissions
- User data (results, history) deleted within 72 hours of account termination
- User may export data before termination

## Open Source Licensing Analysis

### Dual Licensing Approach (Recommended)

| Component | License | Rationale |
|-----------|---------|-----------|
| **Isagawa Kernel** | MIT (existing) | Maximizes adoption, community trust |
| **Platform specs** | MIT or Apache 2.0 | Encourages community vertical development |
| **Web platform code** | BSL 1.1 (Business Source License) | Prevents competitors from hosting a competing service |
| **Component library** | Platform proprietary | The moat — not open source |

### Why BSL 1.1 for the Web Platform

HashiCorp's move to BSL and MongoDB's SSPL both addressed the same problem: cloud providers hosting competing services using open-source code. BSL 1.1 allows:
- Copying, modification, and redistribution
- Non-commercial use
- Commercial use under specific conditions (e.g., not offering a competing hosted service)
- Automatic conversion to open source (e.g., Apache 2.0) after a specified period (typically 4 years)

**Advantages over SSPL:** BSL is more permissive and better understood. SSPL's Section 13 (requiring release of entire service infrastructure) is considered too restrictive and is not recognized as open source by OSI. BSL is source-available with clear commercial restrictions.

### Fork Risk Assessment

- **Kernel fork:** MIT license means anyone can fork. Mitigated by: kernel is the execution engine, not the product. The product is the hosted platform + component library. A kernel fork without the platform is just infrastructure.
- **Platform fork:** BSL prevents commercial hosting of the platform code. Non-commercial forks (research, education) are fine and actually help with adoption.
- **Component library fork:** Proprietary license means no legal fork path. The library is the true moat.

**Precedent:** GitLab operates on this model — open-source core (MIT), commercial features in a proprietary tier, hosted platform as the primary revenue driver. The open-source core drives adoption; the commercial layer monetizes.

## Sources

- [AI Code Ownership: Navigating IP Rights in 2026](https://thecodersblog.com/legal-ownership-of-ai-generated-code-2026/)
- [Who Owns Claude's Code? UK IP Guide for CTOs](https://talkthinkdo.com/blog/who-owns-ai-written-code-what-ctos-developers-and-procurement-teams-need-to-know/)
- [AI and IP Laws 2026: Authorship and Ownership](https://analystip.com/ai-and-ip-laws-2026-authorship-ownership-explained/)
- [Terms of Service for AI Products 2026](https://toslawyer.com/terms-of-service-for-ai-products-what-your-agreement-must-include-in-2026/)
- [Dual Licensing: Open Source and Commercial](https://www.termsfeed.com/blog/dual-license-open-source-commercial/)
- [Legal Risks of Source-Available Licenses: SSPL, BSL](https://www.termsfeed.com/blog/legal-risks-source-available-licenses/)
- [HashiCorp Adopts BSL](https://www.hashicorp.com/en/blog/hashicorp-adopts-business-source-license)

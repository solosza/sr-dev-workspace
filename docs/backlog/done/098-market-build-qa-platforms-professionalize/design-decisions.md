# Design Decisions

## Licensing
**Decision:** Proprietary Evaluation (same as platform-ssh)
**Rationale:** Enterprise clients (like CIQ) evaluate the code but need a commercial license for production use. MIT lets them use it for free. Proprietary Evaluation protects revenue.

## Compatibility Claims
**Decision:** "Built for Claude Code" only
**Rationale:** The platforms currently work exclusively with Claude Code. Claiming compatibility with Cursor, Windsurf, or other agents is inaccurate. If porting happens in the future, update the claim then. Do not say "porting under development" unless it actually is.

## README Style
**Decision:** Follow platform-ssh pattern exactly
**Rationale:** Consistency across all repos signals a real platform company. Each README must be tailored to the specific platform (not copy-paste with find-replace) but follow the same structure: badges, problem, solution, architecture, quick start, project structure, contact, license.

## Em-Dashes and AI Style
**Decision:** No em-dashes, no AI filler text anywhere
**Rationale:** User explicitly flagged this. Enterprise readers notice AI-generated text. Use periods, commas, and colons instead.

## platform-deepeval Visibility
**Decision:** TBD (needs user input during execution)
**Options:**
- Make `platform-deepeval` public and include in landing page
- Keep private and only list the 4 public platforms
- Use `test-platform-deepeval` (already public) as the public-facing repo

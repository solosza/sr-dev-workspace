# Format Contract — The Seven-Part Explanation

Parent: [[../index.md]]

This is the heart of the command. The format was extracted from a live session (2026-07-13, conftest bootstrap walkthrough) that the user asked to preserve verbatim as a repeatable behavior. Changes to this contract change the product.

## The Seven Parts, in Order

| # | Part | Job | Plain | Terse |
|---|------|-----|:-----:|:-----:|
| 1 | **Plain-English purpose** | What this section's thing is FOR — the job it does, zero jargon | ✓ | — |
| 2 | **Visual flow** | ASCII diagram of the runtime/causal sequence, annotated | ✓ | — |
| 3 | **Why each piece exists** | Piece by piece: what breaks without it (consequence-of-absence framing) | ✓ | — |
| 4 | **Grounding** | What the user's actual repos/docs do here — named files, named divergences, anti-patterns flagged | ✓ | ✓ |
| 5 | **Recommendation** | Best practice + what fits THIS user's case, with the reasoning | ✓ | ✓ |
| 6 | **Mental model** | One metaphor that compresses the whole section | ✓ | — |
| 7 | **Confirm / settle prompt** | State the decision this section needs; invite pushback | ✓ | ✓ |

## Per-Part Rules

**1. Plain-English purpose.** Written for someone smart who has never seen this domain. No term used before it's explained. The test: could the user repeat it to someone else in their own words?

**2. Visual flow.** An ASCII diagram of what happens at runtime (or causally), in order, with inline annotations (`◄── this runs first`). Show WHERE in the flow each piece acts. One diagram, not three.

**3. Why each piece exists.** For every line/element in the section: what concrete failure appears if you delete it (`without this line, the first import dies with ModuleNotFoundError`). Consequence-of-absence, not restatement-of-presence.

**4. Grounding.** Cite the user's real files by name: "v2 does X (line-level detail), platform-selenium does Y, hmsa does Z." Divergences between references are the interesting part — say which is the anti-pattern and why. This part is why Step 2 (Ground) is mandatory; if grounding fell back to external-only, SAY SO here.

**5. Recommendation.** Two layers: what the industry does, then what fits this user's use case — which may deliberately diverge from industry practice (with the reason, e.g. "editable install is the modern way, but path-insert survives your prod-test repo copies"). End with the concrete proposal.

**6. Mental model.** One metaphor, one short paragraph ("bootstrap is the stage crew before a play"). It should compress parts 1–3, not add new information.

**7. Confirm / settle prompt.** Name the decision explicitly ("Good with the 3-line bootstrap, or dig into the installable-package alternative first?"). For no-decision sections, ask for confirmation of understanding instead.

## Hard Rules

1. Exactly ONE section per message. The prompt in part 7 ends the turn.
2. Part order is fixed in plain mode. Terse mode renders 4 → 5 → 7 only.
3. No forward references to unexplained sections ("we'll see later" is fine; depending on later material is not).
4. Code snippets small and inline — show the line being discussed, not the whole file.
5. Headers per part are optional style; the CONTENT of each part is not.

## Anti-Patterns

| Anti-pattern | Why it kills the format |
|--------------|------------------------|
| Batching sections "to be efficient" | Removes the discussion space — the entire reason the loop exists |
| Explaining from memory | Ungrounded claims about the user's files; RULE ZERO violation |
| Neutral textbook survey with no recommendation | The user asked what's best for THEIR case, not a literature review |
| Metaphor that introduces new mechanics | Mental model must compress, never extend |
| Ending without the settle prompt | Section can't be recorded; loop position becomes ambiguous |

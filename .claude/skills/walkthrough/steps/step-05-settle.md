# Step 5: Settle

## Purpose

Discussion until the user lands the section's decision. This step IS the conversation — it blocks on the user by contract.

## Input

- User responses to the Step 4 explanation
- `.claude/docs/design/walkthrough/references/depth-modes.md` (mid-loop dial phrases)

## Output

- A settled decision: a stated choice, an accepted recommendation, or explicit "understood, no decision needed" — or a DEFER

## Acceptance Criteria

- [ ] Decision comes from the user's words — never assumed from silence or inferred from a nod to something else
- [ ] Follow-ups answered; depth dialed on request ("slow down", "terse from here")
- [ ] Deferred sections marked DEFERRED with the open question noted — revisited before exit
- [ ] No nudging toward speed; the user sets the tempo

## References

- `.claude/docs/design/walkthrough/references/depth-modes.md`
- `.claude/docs/design/walkthrough/references/format-contract.md` (re-render rules when dialing depth)

## Procedure

1. Answer follow-ups; go deeper or terser per dial phrases.
2. When the user states the outcome, restate it in one sentence for confirmation if there is ANY ambiguity.
3. On "come back to this" — mark DEFERRED, proceed.

## Verification

The settled text that will enter the ledger is either the user's words or a restatement they confirmed.

## Failure Recovery

| Situation | Action |
|-----------|--------|
| Discussion surfaces a missing section | Insert into map after cursor (user approves), continue current section |
| User challenges the grounding | Re-read the source live; correct the explanation; the file wins |
| Discussion drifts to another section's topic | Note it for that section, steer back — one section at a time |

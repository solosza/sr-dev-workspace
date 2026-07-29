# Step 02 — Survey the library

List what already exists, so "build new" is only ever chosen after looking. A wide survey prevents
"nothing fits" from being a memory guess.

## Read first
- the parsed need (its purpose + scope)

## Procedure
1. Enumerate the **search-locations discovery (step 01) identified** with your tools (Glob / Read). Do
   not hardcode the kernel skills; use what discovery found. For a command / skill need those are:
   - commands: `.claude/commands/kernel/*.md`
   - skills: `.claude/skills/*/SKILL.md`
   - their contracts: `.claude/skills/*/contracts/*.json`
   - on a client engagement: that client's library **and** the shared platform library.
2. For each capability, capture from its SKILL.md / command:
   - `name`
   - one-line `purpose` (its Identity)
   - the `scope`(s) it serves (from its contracts)
   - its output `contract`
3. Do not filter yet. Survey wide; matching happens next.

## Output
A list of library capabilities `{name, purpose, scope, contract}` — the candidate pool.

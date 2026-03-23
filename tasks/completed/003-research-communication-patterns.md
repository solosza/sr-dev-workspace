# Research Communication Patterns for Lease Option Wholesaling

## Context
The system sends emails on behalf of the investor via Gmail. Communication must feel personal, knowledgeable, and appropriate to the recipient's situation. Different voices for sellers vs tenant-buyers.

## Dependencies
- **001** — seller objections and deal structure for context
- **002** — buyer segments for messaging differentiation

## Requirements
- Use **WebSearch** to research real estate investor email outreach best practices, lease option communication, and speed-to-lead messaging
- Document **seller communication voice**:
  - Tone: empathetic but direct, positions lease option as a solution to their problem
  - What to say: acknowledge their situation, explain the structure simply, offer next step
  - What NEVER to say: pressure language, "we buy houses" generic, anything that sounds like a script
  - Example tone paragraph
- Document **tenant-buyer communication voice**:
  - Tone: encouraging, educational, positions lease option as a path to homeownership
  - What to say: validate their goal, explain how it works, remove fear of the unknown
  - What NEVER to say: "you can't get a mortgage" framing, condescending language
  - Example tone paragraph
- Document **first-touch email patterns** (at least 2 variants per side):
  - Seller first touch: personalized based on lead source + property data
  - Tenant-buyer first touch: personalized based on deal match + buyer segment
  - Each template: subject line, opening hook, body structure, CTA, signature
- Document **follow-up cadence** with specific timing:
  - Day 1: first touch (immediate)
  - Day 3: follow-up #1 (different angle)
  - Day 7: follow-up #2 (value add — market data, neighborhood info)
  - Day 14: follow-up #3 (soft close or move to nurture)
  - When to escalate to investor (hot signals)
  - When to stop (hard bounces, unsubscribe, explicit no)
- Document **objection handling responses** (at least 5 per side):
  - Seller: "I need to sell now" / "What's the catch?" / "I don't want renters in my house" / "My agent says this won't work" / "I need all cash"
  - Tenant-buyer: "What's the option fee?" / "What if I can't buy at the end?" / "Is this a scam?" / "Why can't I just rent?" / "What happens to my money if I walk?"
- Document **assignment education sequence**: multi-step email flow (3-5 emails) explaining lease option wholesaling to a tenant-buyer who's never heard of it
  - Email 1: What is a lease option (simple explanation)
  - Email 2: How the money works (option fee, monthly, purchase price)
  - Email 3: Your timeline and what you need to do (credit repair path)
  - Email 4: FAQ / common concerns addressed
  - Email 5: Next steps / schedule a call

## Output
- File: `D:\my_ai_projects\project_test_repos\sr_dev_test\research\003-communication-patterns.md`

## Validation (check ALL before completing)
- [ ] File exists at the output path
- [ ] Seller voice guidelines documented with example tone and "never say" list
- [ ] Tenant-buyer voice guidelines documented with example tone and "never say" list
- [ ] At least 2 first-touch email templates per side with subject lines and CTAs
- [ ] Follow-up cadence documented with specific day numbers and content per touch
- [ ] Escalation triggers defined (when to surface to investor)
- [ ] Stop triggers defined (when to stop outreach)
- [ ] At least 5 seller objections with responses
- [ ] At least 5 tenant-buyer objections with responses
- [ ] Assignment education sequence documented as 3-5 email flow with content per email

## Completion Signal
When ALL validation checks pass, invoke `/kernel/complete`.

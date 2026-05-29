# Multi-Stream Business Structure

## Summary

Analyzing whether a single LLC can cover multiple revenue streams: government contracting, QA consulting/platforms, RT automation, and AI agent licensing. The goal is liability isolation without unnecessary complexity.

## Revenue Streams

| Stream | Type | Revenue Model | Risk Profile |
|--------|------|--------------|--------------|
| Government contracting | Services | Contract-based | Medium (FAR compliance, set-aside rules) |
| QA platform licensing | Software | SaaS / license | Low (IP, standard terms) |
| SSH compliance platform | Software | SaaS / license | Low (IP, standard terms) |
| RT automation | Services + software | Consulting + SaaS | Medium-High (healthcare compliance, HIPAA) |
| AI agent factory (kernel) | Software | License / consulting | Low (IP, standard terms) |

## Options Analysis

### Option A: Single LLC

**Structure:** One LLC, multiple "DBAs" or business lines

**Pros:**
- Simplest to manage — one tax return, one bank account, one set of books
- Lowest cost — one formation, one annual report
- Can file multiple Schedule Cs for different business activities
- Shared expenses easily allocated

**Cons:**
- No liability isolation — a lawsuit from one stream exposes assets from all streams
- Govcon has specific requirements that may conflict with other lines
- Healthcare (RT automation) carries HIPAA liability that could spill over
- Mixed NAICS codes may complicate set-aside eligibility

**Verdict:** Acceptable for early stage, but risky once healthcare revenue starts.

### Option B: Multiple Separate LLCs

**Structure:** Separate LLC per major stream

**Pros:**
- Full liability isolation between streams
- Clean separation for investors (if seeking funding for one line)
- Each LLC can have its own NAICS code and set-aside profile

**Cons:**
- Expensive — multiple formations, annual reports, registered agents, bank accounts
- Complex — multiple tax returns, separate bookkeeping
- Overkill for early-stage with minimal revenue

**Verdict:** Too much overhead before you have significant revenue.

### Option C: Series LLC (Recommended)

**Structure:** One parent LLC with segregated "series" for each business line

**Pros:**
- Liability isolation between series without forming separate entities
- Single formation filing, single annual report
- Each series can have its own bank account, contracts, and assets
- Wyoming supports Series LLCs

**Cons:**
- Not recognized in all states (but Wyoming's is well-established)
- More complex operating agreement
- Some banks may not understand series LLCs (workaround: open separate accounts)
- Hawaii may not recognize series liability protection for HI-sourced activity

**Verdict:** Best balance of protection and simplicity.

## Govcon-Specific Structure Requirements

### SAM.gov Registration
- Register the LLC (or the govcon series) in SAM.gov
- Primary NAICS code: 541511 (Custom Computer Programming Services) or 541512 (Computer Systems Design Services)
- Secondary NAICS codes for consulting activities
- Small business size standard: $34M revenue (NAICS 541511) — easily qualifiable

### Set-Aside Eligibility
- **Small Business:** Automatic if under revenue threshold
- **8(a):** Requires SBA certification, disadvantaged status
- **HUBZone:** Requires principal office in a HUBZone area (check Hawaii zones)
- **SDVOSB:** Requires service-disabled veteran ownership
- Standard small business set-aside is the most accessible path

### FAR Compliance
- FAR 52.219-14 (Limitations on Subcontracting): On service contracts, the contractor must perform at least 50% of the work with its own employees
- This constrains the "bid and subcontract everything" model from backlog 092
- For software/IT contracts: the 50% rule applies to labor costs, not materials

## Recommended Structure

**Phase 1 (Now — first $100K revenue):**
Single Wyoming LLC. All revenue streams under one entity. Simple, cheap, fast.

**Phase 2 (When healthcare revenue starts):**
Convert to Wyoming Series LLC. Create series for:
- Series A: Government contracting
- Series B: Software licensing (QA platforms, SSH compliance, kernel)
- Series C: Healthcare services (RT automation) — isolates HIPAA liability

**Phase 3 (When any single stream exceeds $500K):**
Evaluate spinning out high-revenue streams into standalone LLCs if investor interest or regulatory pressure warrants it.

## Sources

- [TurboTax — Multiple Businesses Under Single LLC](https://ttlc.intuit.com/community/business-taxes/discussion/multiple-businesses-under-single-llc/00/1707603)
- [Insogna CPA — Multiple LLCs Tax Simplification](https://insognacpa.com/blog/are-multiple-llcs-complicating-your-taxes-heres-how-to-simplify-the-process)
- [Small Biz Pulse — Managing Multiple Income Streams](https://smallbizpulse.com/llc/llc-formation-management/managing-multiple-streams-of-income-how-to-organize-and-protect-your-earnings/)

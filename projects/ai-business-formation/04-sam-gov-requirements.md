# SAM.gov Registration Requirements

## Summary

Step-by-step requirements for registering a new LLC in SAM.gov for federal government contracting. Directly supports backlog 092 (govcon AI app).

## Prerequisites (Before SAM.gov)

| Prerequisite | How to Get It | Timeline | Cost |
|-------------|---------------|----------|------|
| LLC formed | Wyoming Secretary of State | 1-2 days | $100 |
| EIN (Employer Identification Number) | IRS.gov online application | Same day | Free |
| Business bank account | Any bank (need EIN + LLC docs) | 1-3 days | Free-$25/month |
| Physical business address | Home office qualifies (no P.O. boxes) | Immediate | Free |
| **Wait 14+ days after EIN** | EIN must propagate to IRS databases | 14 days minimum | N/A |

**Critical:** EINs less than 14 days old often fail SAM.gov's IRS verification. There is no workaround. Wait at least 14 days.

## SAM.gov Registration Process

### Step 1: Get Your UEI
- Unique Entity Identifier (UEI) — 12-character alphanumeric ID
- Replaced DUNS numbers in April 2022
- Assigned automatically during SAM.gov entity validation
- **Free** — no third-party service needed

### Step 2: Entity Validation
SAM.gov validates your business against IRS records:
- Legal business name must match IRS records **character-for-character** (including "LLC" suffix)
- Physical address must be USPS-validated format
- EIN must match

### Step 3: Core Registration
Required information:
- Legal business name and DBA (if any)
- Physical address (USPS format, no P.O. boxes)
- EIN
- Business type (LLC)
- Business start date
- Company division/office information
- Congressional district

### Step 4: NAICS Codes
Select primary and secondary NAICS codes:

| NAICS Code | Description | Size Standard |
|-----------|-------------|---------------|
| **541511** | Custom Computer Programming Services | $34M revenue |
| **541512** | Computer Systems Design Services | $34M revenue |
| **541519** | Other Computer Related Services | $34M revenue |
| **541330** | Engineering Services | $25.5M revenue |
| **541690** | Other Scientific/Technical Consulting | $19.5M revenue |

**Recommendation:** Primary NAICS 541512 (Computer Systems Design Services) — covers AI agent development, compliance automation, QA platforms. $34M size standard means you qualify as small business until well past first few years.

### Step 5: Representations and Certifications
Self-certify business characteristics:
- Small business status (based on NAICS size standard)
- Ownership demographics (optional for set-aside eligibility)
- No debarment/suspension history

### Step 6: Points of Contact
Designate:
- Government business POC
- Electronic business POC
- Both can be the same person for a single-member LLC

## Set-Aside Eligibility

| Program | Requirement | Applicable? |
|---------|------------|-------------|
| **Small Business** | Under NAICS size standard ($34M) | Yes — automatic |
| **8(a) Business Development** | Socially/economically disadvantaged, SBA certified | Research needed — requires SBA application |
| **HUBZone** | Principal office in designated HUBZone | Check Hawaii HUBZone map |
| **SDVOSB** | Service-disabled veteran owned 51%+ | Only if applicable |
| **WOSB** | Woman-owned 51%+ | Only if applicable |
| **EDWOSB** | Economically disadvantaged WOSB | Only if applicable |

**Priority:** Start with standard Small Business designation. Research 8(a) eligibility separately — it provides significant competitive advantage for set-asides but requires a formal SBA application process.

## Timeline: LLC Formation to Active SAM.gov Registration

| Week | Action |
|------|--------|
| Week 1 | Form Wyoming LLC ($100, 1-2 days). Apply for EIN (same day, free). |
| Week 1 | Draft operating agreement. Open business bank account. |
| Week 3 | (14+ days after EIN) Begin SAM.gov registration. |
| Week 4-5 | SAM.gov processes registration (10-15 business days). |
| Week 5-6 | Registration active. Can respond to solicitations. |

**Total: ~6 weeks from decision to active SAM.gov registration.**

## Annual Maintenance

- SAM.gov registration expires every **365 days** — must renew annually
- Renewal is free
- Update any changes (address, NAICS codes, POC) during renewal
- Set calendar reminder 30 days before expiration

## Cross-Reference with Backlog 092

The govcon AI app (backlog 092) requires:
- Active SAM.gov registration (this document)
- LLC formed (covered in 01-llc-formation.md)
- FAR compliance understanding (covered in 092 phase 1 research)
- Solicitation scanning capability (092 phase 2 build)

## Sources

- [SAM.gov — Entity Registration](https://sam.gov/entity-registration)
- [SLED.AI — SAM.gov Registration Guide 2026](https://www.sledai.com/blog/registering-with-sam-step-by-step/)
- [SamSearch — SAM.gov Registration Guide 2026](https://samsearch.co/guides/sam-gov-registration)
- [FedBiz Access — 7 Critical SAM.gov Facts 2026](https://fedbizaccess.com/7-essential-things-small-business-owners-must-know-about-sam-gov-in-2026/)
- [SBA — Basic Requirements](https://www.sba.gov/federal-contracting/contracting-guide/basic-requirements)
- [Gallium — SAM.gov Registration Without Rejections](https://www.galliumsolutions.co/post/sam-gov-registration-2026-the-complete-step-by-step-guide-without-the-rejections)

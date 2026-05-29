# SAM.gov API — Opportunity Pipeline Feasibility

## Research Date
2026-05-28

## Executive Summary

The SAM.gov Opportunities API is **free, publicly accessible, and supports automated opportunity scanning**. It provides filtering by NAICS code, set-aside type, agency, location, and date range. Rate limits (1,000 requests/day for registered users) are sufficient for daily pipeline scanning. Solicitation document downloads require additional steps. Building an automated opportunity scanner is **feasible and practical**.

---

## 1. API Access

### How to Get an API Key
1. Create a SAM.gov account (free)
2. Navigate to Account Details page
3. Request a Public API Key
4. Key is issued immediately
5. **Key expires every 90 days** — must be renewed

### Cost
**Free.** No fees for API access at any tier.

### Rate Limits

| Access Tier | Requests/Day | Who |
|------------|-------------|-----|
| Public (no key) | 10 | Anyone |
| Registered (API key) | **1,000** | SAM.gov account holders |
| Federal system | 10,000 | Government users |

When rate limit is hit, API returns `429 Too Many Requests` with `Retry-After` header pointing to midnight UTC.

**1,000 requests/day is more than sufficient** for daily opportunity scanning — a typical scan would use 5-20 requests (paginated results for filtered queries).

---

## 2. Opportunities API

### Primary Endpoint
```
GET https://api.sam.gov/prod/opportunities/v2/search
```

### Authentication
```
Header: X-Api-Key: <your-api-key>
```

### Available Filter Parameters

| Parameter | Description | Example Values |
|-----------|-------------|----------------|
| `postedFrom` / `postedTo` | Date range for posting date | `01/01/2026`, `05/28/2026` |
| `ptype` | Procurement type | `p` (presolicitation), `o` (solicitation), `k` (combined synopsis/solicitation) |
| `deptname` | Department/agency name | `Department of Defense`, `Department of Health and Human Services` |
| `naics` | NAICS code filter | `541511`, `541512`, `541519` |
| `setaside` | Set-aside type | See table below |
| `state` | Place of performance state | `HI`, `CA`, `DC` |
| `zip` | Place of performance ZIP | `96813` |
| `solnum` | Solicitation number | Specific solicitation ID |
| `title` | Keyword in title | `artificial intelligence`, `software` |
| `limit` | Results per page | `10`, `25`, `100` |
| `offset` | Pagination offset | `0`, `100`, `200` |

### Set-Aside Type Values

| Code | Description |
|------|-------------|
| `SBA` | Total Small Business Set-Aside |
| `SBP` | Partial Small Business Set-Aside |
| `8A` | 8(a) Business Development |
| `8AN` | 8(a) Sole Source |
| `HZC` | HUBZone Set-Aside |
| `HZS` | HUBZone Sole Source |
| `SDVOSBC` | Service-Disabled Veteran-Owned Set-Aside |
| `SDVOSBS` | SDVOSB Sole Source |
| `WOSB` | Women-Owned Small Business |
| `WOSBSS` | WOSB Sole Source |
| `EDWOSB` | Economically Disadvantaged WOSB |

### Response Data
Each opportunity record includes:
- Title, solicitation number, notice type
- Agency/department
- Posted date, response deadline
- Place of performance (state, city, zip)
- Set-aside type
- NAICS code
- Point of contact information
- Description/synopsis
- Links to attachments (solicitation documents)

### Dollar Range Filtering
The official SAM.gov API does **not** have a direct `value_min`/`value_max` parameter for filtering by dollar amount. Award value information is available in **award notice records** but not as a filter on active solicitations. Workaround: filter client-side after fetching results, or use third-party APIs (GovCon API, Apify scrapers) that add this capability.

---

## 3. Solicitation Documents

### Can You Download PDFs via API?
**Partially.** The API returns links to attached documents (including solicitation PDFs), but downloading them requires:
1. Following the attachment URL from the API response
2. Making a separate HTTP request to download the file
3. Some attachments may be behind SAM.gov authentication

### Alternative: SAM.gov Bulk Data
SAM.gov provides bulk data extracts that can be downloaded for offline processing. These include opportunity data but may not include all solicitation attachments.

---

## 4. Volume of Opportunities

### At Any Given Time
- **Thousands** of active opportunities across all agencies
- IT services (NAICS 541511, 541512, 541519) are among the most frequently posted categories
- New opportunities posted daily; most have 15-45 day response windows
- Q4 (July-September) sees highest volume due to fiscal year-end spending

### Estimated Relevant Opportunities
For a query filtering on:
- NAICS: 541511, 541512, 541519
- Set-aside: SBA (Total Small Business)
- Posted in last 30 days

Expect **50-200 active opportunities** at any given time nationwide, depending on fiscal period.

---

## 5. Alternatives to the Official API

### If API Is Limited

| Alternative | Pros | Cons |
|------------|------|------|
| **GovCon API** (govconapi.com) | Enhanced filtering (dollar range), better docs | Third-party, may have cost |
| **Apify SAM.gov Scrapers** | Pre-built scrapers, structured output | Apify platform costs, fragile if SAM.gov changes |
| **SAM.gov RSS Feeds** | Real-time notifications, no API key needed | Limited filtering |
| **SAM.gov Email Alerts** | Built-in, no coding required | Not programmable, manual review |
| **FPDS (Federal Procurement Data System)** | Historical award data, spending analytics | Not for active opportunities |
| **USAspending.gov API** | Award data, spending trends | Post-award only |

### Recommended Approach
1. **Primary:** SAM.gov official API (free, 1,000 req/day, covers all needs)
2. **Supplement:** SAM.gov email alerts for real-time notifications
3. **Analytics:** USAspending.gov API for market research (who's winning, at what prices)
4. **Future:** Build a custom scanner that queries daily, scores opportunities by fit, and surfaces top candidates

---

## 6. Automated Scanner Architecture (Phase 2 Concept)

### Daily Pipeline Scanner
```
Schedule: Daily at 6 AM
1. Query SAM.gov API for new opportunities
   - Filter: NAICS 541511, 541512, 541519
   - Filter: Set-aside SBA, 8A, SDVOSB
   - Filter: Posted in last 24 hours
2. Score each opportunity:
   - Dollar range fit (sweet spot: $50K-$250K)
   - Technical alignment (AI, software, data analytics)
   - Location (remote-friendly vs. on-site)
   - Response deadline (enough time to prepare?)
3. Store in local database
4. Surface top candidates for review
5. Track bid/no-bid decisions and outcomes
```

### Feasibility: HIGH
- API is free and well-documented
- 1,000 requests/day is more than enough
- Filtering by NAICS + set-aside covers the primary use case
- Python + requests library is sufficient for implementation
- Can be built as a kernel-managed tool in Phase 2

---

## 7. Verdict: API Feasibility

| Question | Answer |
|----------|--------|
| API accessible? | **Yes** — free, API key from SAM.gov account |
| Filtering sufficient? | **Yes** — NAICS, set-aside, agency, location, date |
| Rate limits adequate? | **Yes** — 1,000/day is more than enough |
| Solicitation downloads? | **Partial** — links provided, download requires extra step |
| Dollar range filter? | **No** — not in official API, available in third-party alternatives |
| Automated scanner feasible? | **Yes** — straightforward Python implementation |

---

## Sources
- [SAM.gov Get Opportunities Public API](https://open.gsa.gov/api/get-opportunities-public-api/)
- [SAM.gov Opportunity Management API](https://open.gsa.gov/api/opportunities-api/)
- [SAM.gov Data Services](https://sam.gov/data-services)
- [GovCon API Guide](https://govconapi.com/sam-gov-api-guide)
- [SAM.gov API Rate Limits](https://govconapi.com/sam-gov-rate-limits-reality)
- [SAM.gov API Complete Guide](https://govconapi.com/sam-gov-api-complete-guide)
- [SAM.gov Entity Management API](https://open.gsa.gov/api/entity-api/)

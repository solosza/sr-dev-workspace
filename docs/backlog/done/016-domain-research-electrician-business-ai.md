# Research Agentic AI System for Electrician Business

## Status
Open

## Priority
Medium

## Summary
Research and design an agentic AI system for electrician/electrical contractor operations. Identify pain points, repetitive workflows, and customer interaction patterns that AI agents can automate. Goal: build a system that can be sold to other electrician businesses.

## Research Areas

### Operations
- Job scheduling and dispatch (assign electricians to jobs, route optimization)
- Permit management (pull permits, track inspections, compliance deadlines)
- Material estimation (wire, breakers, panels — calculate from job specs)
- Inventory tracking (truck stock, warehouse supplies, reorder triggers)
- Code compliance checking (NEC code lookup, local amendments)

### Customer Service
- Lead intake (phone/web inquiries, job description capture, photo upload)
- Quote generation (labor + materials estimate from job description)
- Appointment scheduling (customer-facing booking, confirmation, reminders)
- Job status updates (en route, in progress, complete, invoice sent)
- Follow-up automation (satisfaction survey, maintenance reminders)

### Business Management
- Invoice generation and payment tracking
- Job costing (actual vs estimated, profit margin per job)
- Technician performance (jobs completed, callbacks, customer ratings)
- Recurring maintenance contracts (annual inspections, panel upgrades)
- License and insurance renewal tracking

### AI Agent Opportunities
- **Lead qualification agent** — intake call/form, assess scope, provide rough estimate, schedule
- **Estimating agent** — take job description + photos, generate material list + labor estimate
- **Dispatch agent** — optimize daily schedule based on location, skill level, job priority
- **Code compliance agent** — check plans against NEC + local codes, flag violations
- **Invoice agent** — generate invoice from completed job data, send to customer, track payment

## Key Questions
- What CRM/scheduling software do electricians typically use? (ServiceTitan, Housecall Pro, Jobber?)
- What's the typical tech adoption level? (smartphone app? Paper invoices?)
- What are the biggest time sinks for an electrician business owner?
- What would an electrician business pay monthly for this?

## Output
- Research document with findings
- System architecture proposal
- MVP scope definition
- Pricing model

## References
- User has domain knowledge of the business
- Same kernel infrastructure as mailbox store system (backlog 015)

## Task Builder Input
- **Deliverable:** Research document (operations analysis, AI opportunity assessment, MVP scope, pricing model)
- **Scope:** RESEARCH
- **Constraints:** User has domain knowledge. Web research + user interview. Output to `docs/research/`

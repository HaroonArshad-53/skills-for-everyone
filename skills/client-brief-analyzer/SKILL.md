---
name: client-brief-analyzer
description: Turn a messy client message, job post, or voice-note transcript into a clear project brief with scope, deliverables, missing information, red flags, and questions to ask before accepting the work. Use when a user pastes a client message or job post and asks what the client wants, whether to take the job, or what to ask the client. Also use when the user says analyze this job post, what is this client asking, or make a brief.
---

# Client Brief Analyzer

## When to use this skill
- A client message or job post is pasted and it is vague, long, or confusing
- Before replying to or accepting a freelance job
- When a project later went wrong because scope was never clear

## Workflow
1. Read the whole message twice. Separate facts the client actually stated from things you are guessing - never mix them.
2. Extract: the problem the client has, the exact deliverables they named, deadline, budget (if stated), tools and platforms mentioned, and who approves the work.
3. List every missing piece that changes price or effort: quantity, revisions, source files, access needed, format, timeline, payment method.
4. Scan for red flags: unpaid test work that is a full job, no clear payment method, scope that grows inside the message, unrealistic deadline for the budget, requests to work off-platform against that platform rules.
5. Draft the clarification questions a professional would ask before quoting - grouped as Scope, Timeline, Money, Access.
6. Give a verdict: Clear / Workable after questions / Risky - with the one-sentence reason.

## Rules - never break these
- Never invent a budget, deadline, or deliverable the client did not state. Mark unknowns as UNKNOWN.
- Never advise accepting work that requires breaking a platform terms or doing unpaid full work as a test.
- Keep the client original wording for key requirements in quotes, so nothing is lost in paraphrase.
- Ask questions in the output - do not answer them on the client behalf.

## Output format
- One-line summary - what this job actually is
- Deliverables - bullet list, only what was stated
- Known facts - deadline / budget / tools, or UNKNOWN
- Missing information - what must be asked
- Red flags - or none found
- Questions to send the client - ready to copy-paste
- Verdict - Clear / Workable after questions / Risky + reason

## Example
**User:** Analyze this job post: Need someone to fix my website, it is slow and some pages broken, need it done ASAP, budget is small, maybe more work later...

**Good output (excerpt):** Verdict: Workable after questions. Missing: which pages are broken, current platform and hosting access, what ASAP means in days, and the actual budget range. Red flag: more work later is used to justify a low first budget - quote this job on its own value.

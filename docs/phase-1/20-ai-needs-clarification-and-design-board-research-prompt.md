You are a senior research analyst working on an AI architecture product. Your task is to perform a professional, evidence-based market research study on how AI can be used to clarify customer needs in architecture and construction workflows, and how those clarified needs should be translated into a professional, client-ready design board and requirement-locking package.

## Decision To Support

We need to decide what a professional `AI-assisted needs clarification workflow` should look like for an architecture product, so that the product can:

1. ask the right questions,
2. reduce vague or contradictory client inputs,
3. turn messy conversations into a clear and usable project brief,
4. align the client and architect on scope before design generation,
5. produce a high-quality design board / requirement board that feels credible, premium, and industry-aligned,
6. and hand off structured requirements to downstream 2D / 3D generation systems.

This research is not about generic chatbot UX. It is about defining a market-valid, architecture-specific workflow for discovery, clarification, alignment, and design-direction locking.

## Context

The current product can collect user inputs, but the quality of requirement clarification and design-direction locking is not yet strong enough. We need to understand:

- how architecture firms, design-build companies, and residential design services clarify client needs,
- what documents or artifacts they use to lock requirements,
- how visual preference alignment is usually handled,
- what a professional design board should contain,
- how to avoid ambiguity before concept generation,
- and what a realistic P1/P2 AI-assisted workflow should be.

## Your Mission

Research the market deeply and produce a decision-grade report that answers:

1. How professionals in architecture and construction clarify customer needs in early stages.
2. What information must be collected before a concept, schematic plan, or design board can be considered reliable.
3. How AI should assist this process:
   - what AI should ask,
   - what AI should infer,
   - what AI should summarize,
   - what AI should never assume without confirmation.
4. What a high-quality `design board / requirement board` should include for client alignment.
5. What market-standard or best-practice artifacts exist today:
   - client brief forms,
   - programming questionnaires,
   - space requirement templates,
   - inspiration boards,
   - material boards,
   - concept boards,
   - adjacency matrices,
   - scope alignment documents,
   - and any other early-stage alignment tools.
6. What concrete product requirements should be handed to engineering so we can build this capability correctly.

## Research Standard

Your work must be evidence-based, current, and professional.

### Required source quality

Prioritize:

- official architecture firm onboarding or client briefing examples,
- published project brief templates from architecture, interior design, residential design, or design-build firms,
- academic or professional sources on architectural programming and briefing,
- official software vendor references for client briefing, design programming, BIM requirement capture, or design presentation workflows,
- reputable examples of concept board / material board / mood board practices in architecture and interior design,
- recognized AEC workflow references,
- public sample PDFs, templates, or worksheets used in real practice.

Avoid:

- low-quality SEO blogs,
- generic AI assistant articles with no architecture relevance,
- purely aesthetic inspiration collections with no professional workflow value,
- low-confidence forum opinions unless clearly labeled as weak evidence.

### Research behavior

- Distinguish between:
  - residential architecture,
  - renovation / remodeling,
  - custom home design,
  - interior design briefing,
  - design-build preconstruction discovery,
  - and permit-stage documentation.
- Do not confuse `design preference collection` with `project requirement clarification`.
- Separate:
  - business requirements,
  - spatial/program requirements,
  - technical/site constraints,
  - lifestyle preferences,
  - visual style preferences,
  - and budget/schedule constraints.
- Explicitly identify what should be captured by structured fields, what should be captured by conversation, and what should be confirmed through visual boards.

## Scope

Focus on the most relevant market for an AI-first architecture product:

- residential architecture,
- home renovation / extension,
- custom house design,
- small-to-mid architecture firms,
- design-build residential workflows,
- premium client-facing early-stage design services,
- adjacent interior design workflows where useful for visual preference clarification.

You may use adjacent references from commercial architecture only when they help explain process rigor, but the main recommendation must stay grounded in residential and small-to-mid project workflows.

## Specific Questions To Answer

Answer the following with evidence and explicit reasoning:

### A. How professionals clarify needs

- What is the standard early-stage process used by architecture and design-build teams to clarify client needs?
- What are the typical stages from first intake to signed-off brief?
- Which artifacts are created at each stage?
- Which questions are essential, and which are optional?
- Where do misunderstandings most often happen?

### B. What information must be locked before design starts

- What minimum information is required before a design team can responsibly generate concepts or floor plans?
- Which items are mandatory to confirm:
  - site / lot information,
  - room program,
  - occupancy and household profile,
  - lifestyle and usage patterns,
  - budget,
  - schedule,
  - style preference,
  - material preference,
  - must-haves / must-not-haves,
  - local constraints or assumptions,
  - revision and approval expectations.
- Which items are often unknown initially, and how are they handled professionally?

### C. AI role definition

- Which parts of the clarification workflow are well-suited for AI assistance?
- Which parts should remain explicitly user-confirmed?
- What question strategy should AI use:
  - progressive questioning,
  - contradiction detection,
  - gap detection,
  - prioritization,
  - scenario testing,
  - summary confirmation.
- What should AI output after each stage?
- How should AI decide when the brief is still incomplete versus ready to lock?

### D. Requirement-locking artifacts

- What artifact or artifact set best represents a professional locked brief in this market?
- Compare at least 3 approaches, such as:
  - structured brief form,
  - architectural program sheet,
  - design brief PDF,
  - annotated concept board,
  - requirement matrix,
  - client sign-off checklist.
- Recommend one best-fit P1 artifact set and explain why.

### E. Design board / requirement board standard

- What should a high-quality architecture design board include if the goal is to align expectations before design generation?
- Cover:
  - project overview,
  - client goals,
  - spatial priorities,
  - style references,
  - material references,
  - color direction,
  - mood / atmosphere,
  - precedent images,
  - constraints,
  - do / do-not directions,
  - program summary,
  - site assumptions,
  - approval status.
- What makes a design board feel premium and professional rather than vague or decorative?
- What is the difference between:
  - a mood board,
  - a concept board,
  - a material board,
  - a requirement board,
  - and a client-approved design direction pack?

### F. Example files and reference packs

- Provide links to real, public, legally shareable examples of:
  - client questionnaires,
  - project brief templates,
  - architectural programming worksheets,
  - sample design boards,
  - sample concept boards,
  - sample material boards,
  - sample requirement matrices,
  - sample project brief PDFs,
  - sample pre-design checklists,
  - and any related professional reference artifacts.
- For each example, explain:
  - what it is,
  - what stage it belongs to,
  - why it is useful,
  - what we should adopt,
  - and what is out of scope for our product.

### G. Product implications

- Translate findings into explicit product requirements.
- Define the target workflow from:
  - intake,
  - AI clarification,
  - contradiction/gap detection,
  - requirement summarization,
  - design board creation,
  - client confirmation,
  - and scope lock.
- Define what the product must generate at each stage.
- Define what must be manually editable.
- Define acceptance criteria for product, design, and engineering.

## Mandatory Output Files

Produce the following files in English Markdown:

1. `docs/phase-1/21-ai-needs-clarification-market-research-report.md`
2. `docs/phase-1/22-ai-needs-clarification-product-requirements.md`
3. `docs/phase-1/23-ai-needs-clarification-reference-pack-index.md`

## Required Structure For File 1

`21-ai-needs-clarification-market-research-report.md`

Use this structure exactly:

1. Executive Summary
2. Research Objective and Decision Framing
3. Market Segment and Scope
4. Research Method and Source Quality Notes
5. Current Professional Workflow for Client Need Clarification
6. Deliverable and Artifact Comparison
7. Recommended AI-Assisted Clarification Workflow
8. Recommended Requirement-Locking Artifact Set
9. Recommended Design Board Standard
10. Risks, Gaps, and Open Questions
11. Conclusion
12. Source List

## Required Structure For File 2

`22-ai-needs-clarification-product-requirements.md`

Use this structure exactly:

1. Goal of the Capability
2. Target User and Use Case
3. Recommended End-to-End Workflow
4. Required Input Data
5. Required AI Behaviors
6. Required User Confirmation Steps
7. Required Output Artifacts
8. Required Design Board Elements
9. Required Scope-Lock Elements
10. What Is Explicitly Out of Scope
11. Acceptance Criteria
12. Implementation Notes for Product and Engineering
13. Suggested Next-Phase Extensions

## Required Structure For File 3

`23-ai-needs-clarification-reference-pack-index.md`

Use this structure exactly:

1. Purpose of the Reference Pack
2. How To Use These References
3. Client Questionnaires and Intake Forms
4. Architectural Briefs and Programming Templates
5. Design Boards, Mood Boards, and Concept Boards
6. Requirement Matrices and Scope-Lock Artifacts
7. Public Sample PDFs and Sheet Sets
8. Software / Vendor Workflow References
9. Recommended Shortlist for Immediate Study
10. Source List

For each referenced item, include:

- title,
- link,
- source type,
- project stage,
- why it matters,
- and key takeaways.

## Quality Bar For The Report

Your output must:

- reflect real market practice instead of generic AI-product assumptions,
- separate evidence from inference,
- include confidence levels where uncertainty exists,
- recommend one clear P1/P2 direction rather than a vague menu of options,
- define concrete artifacts instead of abstract workflow language,
- and be directly usable by product, UX, and engineering teams.

## Required Evaluation Lens

When making recommendations, balance all five dimensions:

1. Market credibility
2. Client trust and impression
3. Requirement clarity
4. Feasibility for near-term implementation
5. Risk of overpromising or false precision

## Important Constraint

Do not recommend a workflow that assumes AI can fully replace architect judgment, site verification, code compliance analysis, or professional sign-off.

We want AI to strengthen requirement clarity and alignment, not to make irresponsible assumptions.

## Final Deliverable Expectation

At the end of the report, I should be able to answer:

- What the best AI-assisted client clarification workflow should be
- What artifacts we should use to lock needs professionally
- What a high-quality architecture design board should contain
- Which public reference files we should study first
- What product requirements engineering should implement next

Be rigorous, concrete, and commercially realistic.
```
# P1 2D Deliverable Market Research Prompt

Use the prompt below as-is with a dedicated research agent. The prompt is designed to produce a market-grounded report and a concrete product requirement package for `P1: professional 2D deliverables`.

## Ready-To-Use Prompt

```md
You are a senior research analyst working on an AI architecture product. Your task is to perform a professional, evidence-based market research study that defines what `P1: professional 2D deliverables` must look like for this product to be credible in the architecture and construction market.

## Decision To Support

We need to decide what our first truly professional 2D deliverable standard should be, so the product can generate outputs that:

1. are aligned with real market expectations in architecture / residential design / design-build workflows,
2. are strong enough to show to paying clients,
3. look professional and impressive rather than AI-placeholder-like,
4. are specific enough to be translated into product requirements and engineering implementation.

This research is not about generic AI image quality. It is about defining a market-valid 2D deliverable contract.

## Context

The current product can produce basic concept-like visual outputs, but they are not yet acceptable as professional architectural deliverables. We need to understand:

- what a customer-ready 2D package should contain,
- what level of drafting quality is expected by the market,
- which files and formats are standard,
- what visual and technical elements distinguish amateur outputs from professional outputs,
- and what the minimum viable professional standard should be for Phase P1.

## Your Mission

Research the market deeply and produce a decision-grade report that answers:

1. What kinds of 2D deliverables are commonly provided in the market at each stage:
   - concept design,
   - schematic design,
   - design development,
   - client proposal / sales package,
   - permit / construction documentation.
2. Which of those levels is the correct target for our `P1` if we want:
   - a deliverable that is professional and impressive,
   - but still feasible for an AI-first product to produce reliably in the near term.
3. What exact components must be present in a high-quality P1 deliverable package.
4. What output files, sheet types, drawing conventions, annotations, symbols, title blocks, dimensions, and styling rules are expected.
5. What reference examples exist in the real market that demonstrate the quality bar we should target.
6. What product requirements and acceptance criteria should be handed to engineering after the research is complete.

## Research Standard

Your work must be evidence-based, current, and professional.

### Required source quality

Prioritize:

- official architecture firm deliverable examples,
- published sample drawing sets from firms, builders, design-build companies, or residential plan providers,
- BIM / CAD platform documentation and sample output guidance,
- university / professional architecture documentation standards,
- recognized AEC workflow references,
- reputable examples of client-facing concept and schematic design packages,
- official examples from architecture software vendors where relevant.

Avoid:

- low-quality SEO blogs,
- AI-generated listicles,
- unverified social media opinions unless used only as weak supporting context,
- generic design inspiration boards without clear professional context.

### Research behavior

- Browse broadly enough to reflect the market, not one firm's style.
- Distinguish clearly between:
  - luxury presentation standards,
  - mainstream residential standards,
  - permit/construction standards,
  - and marketing-only visuals.
- Do not assume that "more sheets" always means "better P1".
- Identify the best market-fit target, not the most maximal target.
- Explicitly call out what should **not** be included in P1.

## Scope

Focus the research on the most relevant market for an AI-first architecture product that needs to impress clients early:

- residential architecture,
- home design / renovation,
- concept-to-schematic client presentation packages,
- small-to-mid architecture firms,
- design-build residential workflows,
- online custom home design services if they provide credible deliverable examples.

You may reference adjacent markets such as interior design presentation sets or pre-construction visualization packages only when they help clarify expectations.

## Specific Questions To Answer

Answer the following with evidence and explicit reasoning:

### A. Market expectation

- What does a client expect to receive from a professional early-stage 2D package?
- What does an architect or design-build firm expect internally before a package is considered client-ready?
- Which elements create trust and perceived professionalism?
- Which elements most strongly influence whether a client feels impressed?

### B. Deliverable tiers

- Compare at least 3 deliverable tiers:
  - minimal concept set,
  - strong client-facing schematic set,
  - permit / construction set.
- For each tier, define:
  - typical purpose,
  - typical contents,
  - audience,
  - file formats,
  - visual standard,
  - effort/complexity,
  - why it is or is not suitable for P1.

### C. Output package design

- Define the recommended P1 package:
  - exact sheet list,
  - exact file outputs,
  - expected annotations,
  - dimension strategy,
  - title block expectations,
  - furniture / zoning / area schedule expectations,
  - plot or site boundary expectations,
  - revision labeling,
  - branding/presentation expectations,
  - minimum export formats.

### D. Visual and drafting quality bar

- What makes a drawing look professional instead of generated or amateur?
- Cover:
  - line weights,
  - typography,
  - room labels,
  - wall hierarchy,
  - symbols,
  - sheet composition,
  - scale indicators,
  - north arrow,
  - title block,
  - legends,
  - dimensions,
  - consistency across sheets.
- Define the difference between:
  - a presentable client concept drawing,
  - and a true technical drawing.

### E. Reference examples

- Provide links to real examples of strong output packages or sample sheets.
- Include examples across:
  - concept presentation packages,
  - schematic floor plan sets,
  - sample residential drawing sheets,
  - sample PDF plan sets,
  - vendor or firm sample outputs,
  - and any legally shareable public references that illustrate quality.
- For each example, explain:
  - what stage it represents,
  - why it is relevant,
  - which specific qualities we should adopt,
  - and which qualities are out of scope for P1.

### F. Product implications

- Translate findings into explicit product requirements.
- Define what the product must generate to meet the chosen P1 standard.
- Define what the product must not claim yet.
- Define acceptance criteria that engineering, design, and QA can verify objectively.

## Mandatory Output Files

Produce the following files in English Markdown:

1. `docs/phase-1/18-p1-2d-deliverable-market-research-report.md`
2. `docs/phase-1/19-p1-2d-deliverable-product-requirements.md`

## Required Structure For File 1

`18-p1-2d-deliverable-market-research-report.md`

Use this structure exactly:

1. Executive Summary
2. Research Objective and Decision Framing
3. Market Segment and Scope
4. Research Method and Source Quality Notes
5. Deliverable Tier Comparison
6. Recommended P1 Deliverable Standard
7. Detailed P1 Sheet and File Package
8. Drafting and Presentation Quality Standards
9. Reference Examples and Benchmark Links
10. Risks, Gaps, and Open Questions
11. Conclusion
12. Source List

## Required Structure For File 2

`19-p1-2d-deliverable-product-requirements.md`

Use this structure exactly:

1. Goal of P1
2. Target User and Use Case
3. Recommended Deliverable Contract
4. Required Output Files
5. Required Sheet Types
6. Required Drawing Elements
7. Required Presentation Elements
8. Required Metadata and Revision Elements
9. What Is Explicitly Out of Scope for P1
10. Acceptance Criteria
11. Implementation Notes for Product and Engineering
12. Suggested Next-Phase Extensions

## Quality Bar For The Report

Your output must:

- reflect real market practice rather than generic assumptions,
- separate evidence from inference,
- include confidence levels where uncertainty exists,
- recommend one clear P1 standard instead of listing endless options,
- avoid vague phrases like "high quality" unless defined concretely,
- be directly usable by product, design, and engineering teams.

## Required Evaluation Lens

When making recommendations, balance all four dimensions:

1. Market credibility
2. Customer impression
3. Feasibility for near-term product implementation
4. Risk of overpromising

## Important Constraint

Do not recommend a P1 scope that silently assumes licensed architect stamping, full construction-document completeness, or jurisdiction-specific compliance unless you explicitly label those as out of scope.

We want a professional and impressive client-facing 2D deliverable standard, not a misleading claim of permit-ready documentation unless the evidence strongly supports that scope.

## Final Deliverable Expectation

At the end of the report, I should be able to answer:

- What exact 2D package we should build first
- Why this package matches the market
- What concrete quality bar the output must meet
- Which reference examples define that bar
- What engineering requirements follow next

Be rigorous, concrete, and commercially realistic.
```

## Notes

- This prompt is intentionally strict. It is designed to force a professional research result, not a generic AI summary.
- The target outcome is a decision-grade package that can directly feed the next implementation phase.

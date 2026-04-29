# Concept 2D Market Quality Rubric

Status: C2DQ1 baseline

This rubric defines market-quality acceptance for Concept 2D packages after the
technical live integration has already passed. It is intentionally stricter than
artifact existence/openability checks, but it remains concept-only. Passing this
rubric must never be described as construction, permit, code, structural, MEP,
geotechnical, fire-safety, legal, or final material readiness.

## Evidence Baseline

Required evidence read for this rubric:

- `docs/codex-workflow/concept-2d-market-quality-v2/context-and-acceptance-contract.md`
- `docs/codex-workflow/concept-2d-market-quality-v2/plan.md`
- `docs/codex-workflow/concept-2d-market-quality-v2/operating-model.md`
- `docs/codex-workflow/concept-2d-live-integration/fresh-full-flow-acceptance.md`
- `docs/codex-workflow/concept-2d-live-integration/closeout-report.md`
- `/Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/output/concept-2d-acceptance-audit/10-loop-findings.md`

Evidence note:

- The audit file was not present inside the C2DQ1 worktree output directory.
- It was present in the main project output directory listed above.
- The manual 10-loop audit rejected the output as a market-quality deliverable
  because the drawings were sparse, schematic, weakly styled, and too
  mechanically generated.
- The later browser-driven 20-case audit showed the product path can generate
  technically openable concept-review packages. This rubric preserves that
  distinction: technical readiness is necessary, but not sufficient for market
  presentation quality.

## Acceptance Decision Terms

Use these terms consistently in worker reports, evidence templates, and final
closeout:

- `ready`: The dimension is review-useful for a homeowner and credible for
  architect critique, with only minor polish gaps that do not block feedback.
- `partial`: The artifact is technically correct and can start a conversation,
  but usefulness is weak, incomplete, or inconsistent.
- `failed`: The artifact is misleading, unreadable, stale, blocked, wrong in
  geometry, unsafe in claims, or too placeholder-like to support useful review.

C2DQ6 final decisions:

- `PASS`: all hard gates pass, all seven market dimensions are `ready` or have
  documented minor gaps accepted as non-blocking, and the 20-case matrix evidence
  supports the decision.
- `NEEDS_REVIEW`: all hard gates pass and the package is broadly review-useful,
  but one non-critical visual or wording issue remains.
- `BLOCKED`: generation fails, selected-version truth fails, unsafe readiness
  claims appear, or a repeated product/design decision is needed before safe
  implementation can continue.

## Hard Gates

These gates are not optional and must not be weakened by C2DQ2-C2DQ6.

### Geometry And Source Truth

`ready` requires:

- lot width, lot depth, floor count, room count, selected option, and version id
  match the selected live product version;
- no stale golden-case dimensions, especially no accidental `5 m x 15 m` labels
  when the selected case is `5 m x 20 m`;
- sheet metadata, PDF text, DXF sheets, and quality report agree on the same
  geometry;
- inferred values are marked as assumptions, not verified facts.

`failed` if:

- any sheet contradicts selected-version dimensions;
- old fallback geometry appears;
- room/floor counts drift from the selected design;
- the package silently invents site facts such as exact setbacks, road widths, or
  neighboring buildings as verified truth.

### Artifact Openability And Sheet Completeness

`ready` requires:

- PDF renders nonblank pages;
- DXF files open with `ezdxf` and have usable units, layers, and nonempty model
  space;
- expected sheet categories are present: cover, site, floor plans, elevation,
  section, schedules, assumptions/style notes, and review guidance;
- Review and Delivery expose the PDF, DXF sheets, and quality report links.

`partial` is allowed only for known non-Concept-2D bundle limitations such as a
local DWG converter skip, and the UI/report must clearly explain that the Concept
2D package itself is ready or not ready.

`failed` if:

- PDF or DXF artifacts are missing, blank, corrupt, or mismatched;
- UI links point to the wrong version or stale artifacts;
- quality status marks `customer_ready=true` when the visual/design checks below
  fail.

### Concept-Only Safety

`ready` requires:

- each package states that drawings are concept review artifacts only;
- the package does not claim construction, permit, code, structural, MEP,
  geotechnical, fire-safety, legal, or final material readiness;
- assumptions, defaults, and style interpretations are clearly labeled;
- reference-image descriptors are treated as homeowner style hints, not measured
  image analysis.

`failed` if:

- any output says or implies the package is ready for construction, permitting,
  code approval, structural design, MEP coordination, legal use, or final material
  procurement;
- disclaimers are absent from customer-visible PDF/report evidence;
- generated text hides important assumptions.

## Market Dimensions

Each generated package must be evaluated across these seven dimensions.

## 1. Homeowner Readability

Question:

```text
Can a low-communication homeowner understand the concept, recognize the home they
asked for, and give useful feedback without technical handholding?
```

`ready` requires:

- the cover or summary identifies the brief in plain language: lot/apartment
  size, household, style, priorities, and selected option;
- drawings make the main concept easy to see: entrance, parking/service areas
  where relevant, living/social zones, bedrooms, wet areas, storage, outdoor
  spaces, and vertical movement;
- room labels are customer-readable and consistent in language;
- assumptions and tradeoffs are plain, specific, and useful;
- the package asks actionable next review questions, such as whether to prioritize
  storage, open kitchen, elder access, facade warmth, or garden/parking balance.

`partial` means:

- rooms are identifiable but the design story is thin;
- assumptions are generic;
- the customer could comment on room names but not confidently on flow,
  furniture, storage, or lifestyle fit.

`failed` if:

- the package reads like a technical scaffold or box diagram;
- the design intent is not understandable from the sheets;
- labels are raw, mixed-language, or confusing;
- the homeowner would likely ask "where is the design idea?" rather than respond
  with specific feedback.

Evidence to capture:

- PDF page references for the summary, plans, assumptions, and review questions;
- short homeowner-readability note in the evidence template;
- at least one example of an actionable review question.

Primary downstream owners:

- C2DQ2 for room/program clarity;
- C2DQ3 for layout and text readability;
- C2DQ5 for review questions and revision loop evidence.

## 2. Architect Plausibility

Question:

```text
Would an architect consider this a credible first-pass concept drawing set worth
critiquing, rather than a placeholder that must be redrawn before client review?
```

`ready` requires:

- sheet set structure resembles a concept package: site, plans, elevation,
  section, schedules, notes, and assumptions;
- plans show believable zoning, circulation, wet-core logic, openings, and
  furniture/fixture intent;
- elevation and section explain the concept, not just generic rectangles and
  floor lines;
- schedules are polished enough for review and avoid raw internal data;
- title blocks, legends, dimensions, and sheet names are coherent.

`partial` means:

- the sheet set exists and is technically correct, but some drawings remain too
  schematic or sparse for confident architect critique.

`failed` if:

- plans look algorithmically zoned with unrealistic room areas;
- elevation/section are placeholder-level;
- drawings lack basic line hierarchy, dimensions, and annotation craft;
- an architect would need to redraw the set before presenting it.

Evidence to capture:

- architect review notes for plan, site, elevation, section, and schedules;
- screenshot or rendered PDF page references for the strongest and weakest sheet;
- any `NEEDS_ARCHITECT_DECISION` item where deterministic rules would become
  design judgment.

Primary downstream owners:

- C2DQ2 for plausibility of the design model;
- C2DQ3 for drawing craft;
- C2DQ4 for facade, section, and style expression.

## 3. Spatial Planning

Question:

```text
Do rooms, circulation, stairs, wet cores, storage, openings, furniture, and
multi-floor relationships feel plausible for the requested home type?
```

`ready` requires:

- room sizes are plausible for lot/apartment type, floor count, and household;
- circulation is legible from entrance to living areas, stairs, bedrooms, wet
  areas, service zones, balconies/terraces, and parking where relevant;
- stair/core placement is believable for narrow lots, multi-generation homes, and
  shophouse privacy splits;
- wet areas stack or align where the concept claims they do;
- furniture and fixture symbols fit without obvious collisions;
- storage, laundry, service, and flexible work areas appear when requested;
- low-communication briefs use conservative defaults with provenance.

`partial` means:

- the main rooms are present but some room sizes, furniture placement, storage, or
  circulation logic remain weak.

`failed` if:

- rooms are implausibly large or small for the typology;
- stairs, bathrooms, doors, fixtures, or furniture collide semantically;
- no internal dimensions exist where needed to judge fit;
- vertical stacking contradicts itself across floors;
- requested critical priorities such as elder access, garage, business frontage,
  storage, or work-from-home space are absent.

Evidence to capture:

- room schedule with areas;
- plan page references for circulation and core placement;
- notes on any inferred default;
- failure signal if a case triggers unrealistic areas similar to the audit
  examples: oversized kitchens/bedrooms on narrow townhouses or unusably tiny
  laundry/service zones.

Primary downstream owner:

- C2DQ2.

## 4. Drawing Craft

Question:

```text
Are PDF and DXF sheets composed, scaled, annotated, and polished enough for review?
```

`ready` requires:

- drawings use enough page area to be legible without excessive whitespace;
- plan/elevation/section viewports are centered and scaled consistently;
- line hierarchy distinguishes site boundary, walls, openings, furniture,
  fixtures, dimensions, annotations, and reference/context lines;
- dimensions include overall dimensions plus useful internal dimensions;
- labels, tags, leaders, dimensions, legends, and title blocks do not overlap;
- schedules are formatted as customer-facing tables, not raw object dumps;
- PDF render QA and DXF openability checks both support the same sheet set.

`partial` means:

- sheets are readable but have isolated over-density, whitespace, or annotation
  polish issues that do not block review.

`failed` if:

- drawings are too small on the sheet;
- important labels or dimensions collide;
- sheets are dominated by empty space without a reason;
- raw data such as dictionaries, enum names, or internal field names appears;
- DXF files open but lack useful entity richness for concept CAD review.

Evidence to capture:

- rendered PDF page images or contact sheet;
- page-level notes for viewport fit, collisions, dimensions, and whitespace;
- DXF summary including entity counts, layers, units, and sheet parity.

Primary downstream owner:

- C2DQ3.

## 5. Style Expression

Question:

```text
Does the selected style visibly change the concept package in facade, elevation,
material notes, shading, opening language, and explanatory tone?
```

`ready` requires:

- style affects facade rhythm, massing cues, openings, shading, material zones,
  balcony/terrace treatment, and notes;
- material palettes are described as concept intent, not final specifications;
- modern tropical, minimal warm, Indochine, and modern minimalist outputs are
  distinguishable;
- explicit dislikes suppress conflicting features;
- reference descriptors influence style fields without claiming real image
  measurement or analysis;
- style assumptions are visible to the customer and traceable to the brief.

`partial` means:

- style appears in notes and limited facade marks, but drawings still feel
  somewhat generic.

`failed` if:

- all styles look the same except for a text label;
- elevation is just rectangular massing with generic windows;
- dislikes are ignored, such as adding a glassy/dark facade when the brief asks
  for less glass or a warmer expression;
- reference descriptors are ignored or overclaimed.

Evidence to capture:

- style input fields or descriptors;
- facade/elevation page reference;
- material/style notes page reference;
- before/after note for revision cases that change style.

Primary downstream owner:

- C2DQ4.

## 6. Revision Usefulness

Question:

```text
When a homeowner gives natural-language feedback or reference descriptors, does
the product preserve original truth while changing the right concept assumptions
and regenerating traceable sheets?
```

`ready` requires:

- feedback is interpreted into explicit changed fields;
- original lot geometry, floor count, fixed room requirements, and selected
  version truth are preserved unless the customer explicitly changes them;
- generated package states what changed, why, and which assumptions remain;
- changes are visible in plans, notes, schedules, or style expression as
  applicable;
- ambiguous or unsafe requests produce clarification or concept-only language
  instead of silent overreach.

`partial` means:

- feedback is captured and some output changes, but traceability or design impact
  is weak.

`failed` if:

- revisions discard original requirements;
- feedback changes only text while drawings remain unchanged where they should
  change;
- the system treats reference images as measured plans or verified product data;
- unsafe scope requests are accepted as construction/permit/code promises.

Evidence to capture:

- original brief;
- feedback text or reference descriptors;
- changed-field summary;
- before/after artifact ids;
- reviewer note showing the change is visible and useful.

Primary downstream owner:

- C2DQ5.

## 7. Safety And Truthfulness

Question:

```text
Does the package stay honest about what is known, inferred, and out of scope?
```

`ready` requires:

- concept-only warning appears in PDF/report evidence;
- assumptions are specific and customer-readable;
- the package distinguishes known brief facts, system defaults, and design
  suggestions;
- quality/readiness labels do not overstate the artifact;
- safety-critical, legal, and engineering domains remain out of scope.

`partial` means:

- disclaimers exist, but assumptions or readiness language need clearer wording.

`failed` if:

- customer-visible output contains unsafe readiness claims;
- quality status says market/customer ready while major visual/design gates fail;
- generated assumptions are hidden or stated as verified facts.

Evidence to capture:

- exact page/report location of the concept-only warning;
- readiness field values from quality report;
- assumption notes page reference;
- any unsafe language found and the blocking decision.

Primary downstream owners:

- C2DQ2-C2DQ5 for their own generated text and metadata;
- C2DQ6 for final integrated truth.

## Readiness Semantics

Use readiness words narrowly:

- `technical_ready`: artifacts exist, open, render, link correctly, and preserve
  selected-version geometry.
- `concept_review_ready`: artifacts are good enough for a homeowner/architect to
  review and provide useful feedback.
- `market_presentation_ready`: artifacts are persuasive enough to represent a
  market-quality first-pass concept package.
- `construction_ready`: must remain `false`.

C2DQ2-C2DQ5 should not mark `concept_review_ready` or
`market_presentation_ready` by existence alone. C2DQ6 owns final integrated
acceptance.

## Evidence Minimums By Session

C2DQ2 Spatial Planning:

- focused tests for room sizing, circulation, stair/core, wet-core, storage,
  openings, furniture, and low-communication assumptions;
- matrix cases exercised or represented for narrow lots, larger lots,
  apartments, elder access, garage, garden, and home business;
- report every unresolved product/design judgment as `NEEDS_ARCHITECT_DECISION`.

C2DQ3 Drawing Craft:

- PDF render checks for sheet tokens, page nonblankness, viewport fit, dimensions,
  label collision signals, title blocks, legends, and schedules;
- DXF checks for sheet parity, units, layers, and entity richness;
- no raw object/string leaks in customer-visible tables.

C2DQ4 Style:

- tests proving distinct outputs for minimal warm, modern tropical, Indochine,
  modern minimalist, explicit dislikes, and reference descriptors;
- visible facade/elevation/material-note changes;
- no claim of real image analysis.

C2DQ5 Revision:

- before/after evidence for natural-language feedback and reference descriptors;
- original-requirement preservation;
- changed-field summary and regenerated artifact metadata;
- unsafe-scope handling.

C2DQ6 Integrated Closeout:

- verify C2DQ1-C2DQ5 are merged before running;
- run integrated API/Web technical gates required by the contract;
- generate 20-case evidence or an integrator-approved representative subset plus
  the required fresh live flow;
- manually inspect at least 5 generated PDFs as homeowner and architect;
- open DXFs with `ezdxf`;
- inspect Review and Delivery console/network;
- write final decision without using worker evidence as final truth.

## Blocking Product Decisions

Use `NEEDS_ARCHITECT_DECISION` when deterministic implementation would otherwise
invent a design standard. Examples:

- unavoidable tradeoff between garage depth, stair position, and living area on a
  narrow lot;
- whether an elder bedroom must replace a garage/service zone;
- whether a corner lot should prioritize two active facades or privacy;
- whether a style conflict should follow the selected style or explicit dislikes;
- whether a low-communication brief needs a clarification prompt before
  generation.

Do not resolve these by claiming code, permit, structural, MEP, legal, or final
professional validation.

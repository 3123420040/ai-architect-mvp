# Concept 2D Market Quality V2 Context And Acceptance Contract

## Context

Previous technical integration is accepted:

- API commit: `e273bb1 feat(concept-2d): harden live package quality`
- Web commit: `4906e71 fix(concept-2d): clean live delivery UI states`
- Docs acceptance commit: `3cb344e docs(phase-2): add fresh concept 2d flow acceptance`
- Fresh browser flow project: `954ed846-ce1d-4974-8bd7-a6d823c04505`
- Fresh browser flow version: `7b89f8e5-7cef-450a-a2bc-f115e08df32e`

The accepted baseline generates a 10-page Concept 2D PDF and 10 DXF sheets from the live selected version. The remaining problem is market quality, not technical openability.

## Product Standard For This Phase

The output should be:

- clear enough for a homeowner to review and request changes;
- credible enough for an architect to treat as a first-pass concept design package;
- detailed enough to show site, rooms, openings, circulation, dimensions, schedules, style intent, and assumptions;
- honest enough to remain concept-only.

The output should not claim:

- construction readiness;
- permit/code compliance;
- structural, MEP, geotechnical, fire-safety, or legal validation;
- final material specification;
- architect/engineer approval.

## Mandatory Evidence Sources

Agents must read:

- `/Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/docs/codex-workflow/concept-2d-live-integration/fresh-full-flow-acceptance.md`
- `/Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/docs/codex-workflow/concept-2d-live-integration/closeout-report.md`
- `/Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/output/concept-2d-acceptance-audit/10-loop-findings.md`

If any file is missing, record the missing evidence and continue only with the available equivalent evidence.

## Acceptance Rubric

Each generated package should be scored as:

- `ready`: review-useful with only minor polish gaps;
- `partial`: technically correct but client/architect usefulness is weak;
- `failed`: misleading, unreadable, stale, blocked, or wrong geometry.

Rubric dimensions:

1. Geometry truth
   - lot dimensions match selected version;
   - north/orientation shown where available;
   - room/floor counts match selected design;
   - no stale golden dimensions.

2. Spatial planning
   - rooms are sized plausibly;
   - circulation is legible;
   - stair/wet core placement is believable;
   - openings match room use;
   - furniture/fixtures fit without collisions;
   - multi-floor vertical logic is coherent.

3. Drawing readability
   - plans are scaled and centered;
   - labels do not collide;
   - dimensions are visible and not over-dense;
   - legends and title blocks are readable;
   - schedules are useful rather than filler;
   - pages are not dominated by empty whitespace unless intentional.

4. Style expression
   - style affects facade/elevation and notes;
   - material palette is visible as concept intent;
   - dislikes suppress conflicting features;
   - reference descriptors influence the result without pretending real image analysis.

5. Client review usefulness
   - package states what changed and why;
   - assumptions are plain-language;
   - tradeoffs are visible;
   - next review questions are actionable.

6. Safety and truthfulness
   - concept-only warning present;
   - no construction/permit/MEP/legal claims;
   - inferred/default values are marked as assumptions.

## Required Technical Reruns

API:

```bash
cd /Users/nguyenquocthong/project/ai-architect/ai-architect-api
PYTHONPATH=. .venv/bin/python -m pytest tests/professional_deliverables -q
PYTHONPATH=. .venv/bin/python -m pytest tests/test_foundation.py tests/test_flows.py tests/test_briefing.py -q
make sprint3-ci-linux
```

Web if touched:

```bash
cd /Users/nguyenquocthong/project/ai-architect/ai-architect-web
pnpm lint
pnpm build
```

Manual/browser:

- Run fresh UI flow from intake to delivery.
- Generate artifacts for the case matrix.
- Download/render PDFs.
- Open DXFs with `ezdxf`.
- Inspect Review and Delivery console/network for errors.

## Decision Points

Stop and ask the integrator/user if:

- the rubric requires a stricter market-quality definition than this contract;
- a fix requires construction-ready or code-compliance behavior;
- a product decision is needed between design quality and deterministic simplicity;
- 20-case generation reveals a repeated architectural assumption that must be decided, not guessed.

# Concept 2D Market Quality Evidence Template

Status: C2DQ1 baseline

Use this template for C2DQ2-C2DQ6 reports when generating, testing, or manually
reviewing Concept 2D market-quality artifacts. Keep the language concept-only.
Do not claim construction, permit, code, structural, MEP, geotechnical,
fire-safety, legal, or final material readiness.

## Single Case Evidence

```text
## Case Evidence

Case:
- ID:
- Title:
- Session:
- Reviewer role: homeowner | architect | integrator | mixed
- Date/time:
- Repo/branch/commit:

Input:
- Source: UI | API fixture | unit fixture | revision fixture
- Original brief:
- Structured inputs:
  - Typology:
  - Lot/area:
  - Orientation/context:
  - Floors:
  - Bedrooms:
  - Bathrooms:
  - Household:
  - Style:
  - Priorities:
  - Dislikes:
  - Reference descriptors:
  - Budget/timeline:
- Inferred assumptions:
- Unsafe/out-of-scope requests rejected or reframed:

Generated artifacts:
- Project id:
- Selected version id:
- Revision id, if applicable:
- Job/bundle id:
- PDF URL/path:
- Rendered PDF pages path:
- DXF URLs/paths:
- Quality report URL/path:
- Review URL:
- Delivery URL:

Technical gates:
- PDF renders nonblank:
- PDF page count:
- Expected sheet tokens present:
- DXF count:
- DXF open with ezdxf:
- DXF units:
- DXF entity/layer summary:
- Review UI links present:
- Delivery UI links present:
- Console/network errors:

Geometry/source truth:
- Selected lot/area:
- PDF lot/area tokens:
- Quality report lot/area:
- DXF geometry check:
- Stale geometry absent:
- Room/floor count preserved:
- Result: ready | partial | failed
- Notes:

Homeowner readability:
- Result: ready | partial | failed
- What a homeowner can understand:
- Actionable next review questions:
- Failure signals observed:

Architect plausibility:
- Result: ready | partial | failed
- Plan critique:
- Site critique:
- Elevation critique:
- Section critique:
- Schedule/notes critique:
- Failure signals observed:

Spatial planning:
- Result: ready | partial | failed
- Room sizing:
- Circulation:
- Stair/core:
- Wet areas:
- Openings:
- Furniture/fixtures:
- Storage/service:
- Vertical logic:
- Failure signals observed:

Drawing craft:
- Result: ready | partial | failed
- Viewport scale:
- Page whitespace:
- Line hierarchy:
- Labels/tags:
- Dimensions:
- Legends/title blocks:
- Schedule formatting:
- PDF/DXF parity:
- Failure signals observed:

Style expression:
- Result: ready | partial | failed
- Selected style:
- Visible facade/elevation/interior-equivalent changes:
- Material/palette notes as concept intent:
- Dislikes suppressed:
- Reference descriptors handled as hints:
- Failure signals observed:

Revision usefulness, if applicable:
- Result: ready | partial | failed | not_applicable
- Original requirements preserved:
- Feedback interpreted into changed fields:
- Before artifact id:
- After artifact id:
- Visible drawing/note changes:
- Ambiguity handling:
- Failure signals observed:

Safety and truthfulness:
- Result: ready | partial | failed
- Concept-only warning location:
- construction_ready value:
- Assumptions labeled:
- Unsupported readiness claims absent:
- Reference descriptors not overclaimed:
- Failure signals observed:

Decision:
- Case decision: ready | partial | failed
- Final rationale:
- NEEDS_ARCHITECT_DECISION:
- Known gaps:
```

## Session Report Evidence

```text
Decision: PASS | NEEDS_REVIEW | BLOCKED

Scope:
- Session:
- Branch/worktree:
- Owned files changed:
- Shared files changed:

Summary:
- Implemented:
- Not implemented:
- Deferred:

Matrix coverage:
- Cases executed:
- Cases represented by focused tests:
- Cases not executed:
- Justification for any subset:

Market-quality coverage:
- Homeowner readability:
- Architect plausibility:
- Spatial planning:
- Drawing craft:
- Style expression:
- Revision usefulness:
- Safety/truthfulness:

Technical verification:
- Commands run:
- Focused tests:
- PDF render evidence:
- DXF openability evidence:
- Browser evidence:
- Quality report evidence:

Residual risk:
- Flakes:
- Known gaps:
- Product/design decisions:

Contract compliance:
- No product code changes outside owned scope:
- No unsafe readiness claims:
- No construction/permit/code/structural/MEP/legal/final-material claims:
- Selected-version geometry preserved:
- Any NEEDS_ARCHITECT_DECISION:

Known issues:
-
```

## Manual Review Checklist

Use this checklist during visual inspection of rendered PDFs and browser pages.

Hard gates:

- PDF/DXF artifacts are from the selected live version.
- PDF pages render and are nonblank.
- DXFs open with `ezdxf`.
- Sheet count and sheet names match metadata.
- Lot/apartment geometry is consistent.
- Stale fallback dimensions are absent.
- Concept-only warning is visible.
- `construction_ready` remains false.
- No unsafe readiness claims appear.

Homeowner readability:

- Can identify entrance or apartment entry.
- Can identify living, kitchen/dining, bedrooms, bathrooms, storage/service, and
  outdoor/terrace zones where relevant.
- Can understand main design idea from summary and drawings.
- Can see assumptions and tradeoffs.
- Can answer or respond to next review questions.

Architect plausibility:

- Site plan has useful context for the typology.
- Floor plans show plausible zoning and circulation.
- Stairs/wet cores/furniture/openings are believable.
- Elevation expresses more than a rectangle with windows.
- Section explains vertical relationships at concept level.
- Schedules and notes are polished, not raw internal output.

Drawing craft:

- Drawings are not tiny relative to page size.
- Labels, tags, leaders, and dimensions do not overlap.
- Line hierarchy is visible.
- Overall and useful internal dimensions are readable.
- Legends/title blocks support review.
- Schedules are formatted for customers and architects.

Style and revision:

- Selected style changes facade/elevation/notes.
- Dislikes suppress conflicting features.
- Reference descriptors are reflected as hints.
- Revision cases show visible before/after changes.
- Original requirements and geometry are preserved during revision.

Safety:

- Assumptions are explicit.
- Unknowns are not presented as verified facts.
- No permit/code/structural/MEP/legal/final-material readiness is claimed.

## Quality Report Fields To Capture

When available, record these fields exactly:

```text
artifact_state:
customer_ready:
technical_ready:
concept_review_ready:
market_presentation_ready:
construction_ready:
concept_package.enabled:
concept_package.readiness:
concept_package.source:
concept_package.sheet_count:
concept_package.fallback_reason:
qa_bounds.lot_width_m:
qa_bounds.lot_depth_m:
qa_bounds.area_m2:
qa_bounds.floors:
qa_bounds.rooms:
qa_bounds.openings:
```

If a field does not exist yet, write `field_not_available` instead of inventing a
value.

## Failure Signal Bank

Use these standard failure labels in evidence so downstream reports can be
compared:

- `STALE_GEOMETRY`
- `WRONG_SELECTED_VERSION`
- `MISSING_CONCEPT_ONLY_WARNING`
- `UNSAFE_READINESS_CLAIM`
- `PDF_BLANK_OR_CORRUPT`
- `DXF_OPENABILITY_FAILURE`
- `UI_LINK_MISSING_OR_STALE`
- `ROOM_AREA_IMPLAUSIBLE`
- `CIRCULATION_UNCLEAR`
- `STAIR_CORE_IMPLAUSIBLE`
- `WET_CORE_INCOHERENT`
- `FURNITURE_FIXTURE_COLLISION`
- `OPENINGS_GENERIC_OR_WRONG`
- `STORAGE_PRIORITY_IGNORED`
- `SITE_CONTEXT_TOO_THIN`
- `VIEWPORT_TOO_SMALL`
- `EXCESSIVE_WHITESPACE`
- `LABEL_OR_DIMENSION_COLLISION`
- `RAW_INTERNAL_DATA_LEAK`
- `SCHEDULE_NOT_CUSTOMER_READABLE`
- `ELEVATION_PLACEHOLDER`
- `SECTION_PLACEHOLDER`
- `STYLE_NOT_VISIBLE`
- `DISLIKE_NOT_SUPPRESSED`
- `REFERENCE_DESCRIPTOR_OVERCLAIM`
- `REFERENCE_DESCRIPTOR_IGNORED`
- `REVISION_NOT_TRACEABLE`
- `REVISION_GEOMETRY_DRIFT`
- `ORIGINAL_REQUIREMENT_LOST`
- `ASSUMPTION_NOT_LABELED`
- `NEEDS_ARCHITECT_DECISION`

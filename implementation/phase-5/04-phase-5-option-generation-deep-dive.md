# Phase 5 Option Generation Deep Dive

## Purpose

This document expands the Phase 5 contract specifically for the option-generation lane.

It exists because production truth shows a mismatch:

- the upstream intake and brief clarification are becoming richer,
- but the downstream generated options still feel too template-driven, too generic, and not differentiated enough to create a premium client impression.

This document defines:

1. the current `as-is` architecture,
2. the `target architecture`,
3. and the checkpoint breakdown that must be folded into existing Phase 5 checkpoints.

It does not replace the main Phase 5 docs.

It sharpens the generation quality requirements that sit inside CP4, CP5, and CP6.

## 1. As-Is

### 1.1 Current flow

Today the generation flow is:

1. `DesignsClient` requests generation,
2. `generation.py` calls `gpu_client.generate_floorplans(...)`,
3. `gpu_client.py` calls the GPU service `/generate/floor-plan`,
4. the GPU service returns deterministic SVG/PNG placeholder options,
5. `generation.py` then rebuilds canonical geometry using `ensure_geometry_v2(...)`,
6. `build_sheet_bundle(...)` turns that geometry into preview sheets,
7. `save_svg(...)` persists the preview,
8. and `projects.py` returns serialized versions to the frontend.

### 1.2 Modules currently involved

#### Frontend

- `../ai-architect-web/src/components/designs-client.tsx`

#### API orchestration

- `../ai-architect-api/app/api/v1/generation.py`
- `../ai-architect-api/app/api/v1/projects.py`

#### Generation boundary

- `../ai-architect-api/app/services/gpu_client.py`
- `../ai-architect-gpu/api/server.py`

#### Canonical geometry and preview packaging

- `../ai-architect-api/app/services/geometry.py`
- `../ai-architect-api/app/services/exporter.py`
- `../ai-architect-api/app/services/storage.py`

#### Persistence and state

- `../ai-architect-api/app/models.py`
- `../ai-architect-api/app/services/state_machine.py`

### 1.3 What is actually driving option differences today

The current geometry lane is mainly driven by:

- lot width,
- lot depth,
- floor count,
- style,
- and `option_index`.

That means option variation is still shallow.

Many clarified inputs are not materially shaping the generated options yet, including:

- `space_requests`,
- `spatial_preferences`,
- `must_haves`,
- `must_not_haves`,
- `occupant_count`,
- `household_profile`,
- `budget_vnd`,
- and `timeline_months`.

### 1.4 Why the result still feels generic

The current generator is good enough to create a working flow, but not yet a premium design exploration experience.

Current weaknesses:

- option labels are generic: `Option A`, `Option B`, `Option C`
- option descriptions are generic: `Phuong an X cho <project_id>`
- generation logic does not yet express strong strategic differences between options
- preview quality is more technical than aspirational
- rationale is mostly absent
- the user cannot see why one option fits the brief better than another

### 1.5 Product consequence

Even if the system is technically generating three options, the end user will still experience them as:

- variants of a template,
- not as curated architectural directions.

That weakens:

- trust,
- perceived intelligence,
- architect credibility,
- and the sense that the product is premium.

## 2. Target Architecture

### 2.1 Design principle

The system should stop treating option generation as:

- `generate image -> save version`

and move toward:

- `understand brief -> synthesize program -> define option strategy -> generate geometry -> package rationale -> present options for decision`.

### 2.2 Target layered architecture

#### Layer A — Brief Gate

Generation should only proceed when:

- required brief sections are complete,
- no active conflicts remain,
- and the brief is explicitly locked.

This prevents weak upstream data from polluting the option lane.

#### Layer B — Program Synthesis

Introduce an internal synthesis step that converts the brief into:

- room program,
- adjacency priorities,
- circulation priorities,
- privacy requirements,
- daylight priorities,
- parking or garden requirements,
- and special-use constraints.

This layer should absorb richer brief fields that are currently underused.

#### Layer C — Option Strategy Profiles

The system should define option strategies intentionally.

Instead of `Option A/B/C` as index-only variants, each option should come from a strategy profile such as:

- `daylight_first`
- `privacy_first`
- `efficiency_first`
- `garden_priority`
- `garage_priority`
- `multi_generation_separation`

The exact strategies should depend on project type and brief.

#### Layer D — Geometry Generation

`geometry.py` should consume:

- the synthesized program,
- the selected strategy profile,
- lot/site constraints,
- typology rules,
- and hard user constraints.

This layer should produce geometry that is still rule-based and deterministic enough for Phase 5, but materially more responsive to the brief than it is today.

#### Layer E — Preview Packaging

Preview generation should produce two parallel outputs:

- technical preview for architectural confidence,
- client-facing hero preview for emotional impact.

At minimum:

- use the best available raster preview where available,
- keep technical SVG preview for review flow,
- and avoid exposing raw placeholder-like descriptions to the end user.

#### Layer F — Quality Scoring

Before an option is shown as ready, the system should score it on:

- program fit,
- circulation clarity,
- daylight potential,
- privacy logic,
- typology compliance,
- and missing-assumption risk.

Phase 5 can keep this rule-based.

It does not need ML scoring yet.

#### Layer G — Decision Metadata

Each option returned to the frontend should include:

- strategy name,
- short rationale,
- key metrics,
- strengths,
- caveats,
- and a short `why this fits your brief` explanation.

This is essential for the `Designs` page to feel professional.

### 2.3 End-user quality target

For an end user to feel the product is excellent, options should feel:

- intentionally different,
- clearly explained,
- architecturally credible,
- and visually polished.

The user should think:

- `the system understood my priorities`
- not
- `the system showed me three generic variants`.

## 3. Concrete Target Output Contract

### 3.1 Generation response should move toward

Each option should eventually expose:

- `option_key`
- `option_title_vi`
- `option_strategy`
- `option_summary_vi`
- `hero_preview_url`
- `technical_preview_url`
- `geometry_summary`
- `strengths`
- `caveats`
- `fit_reasons`
- `quality_score`
- `generation_source`

### 3.2 Minimum Phase 5 contract

Phase 5 does not need the full target state, but it must deliver:

- stronger naming,
- stronger descriptions,
- stronger metadata,
- strategy-aware differentiation,
- and frontend presentation that exposes those improvements.

## 4. Checkpoint Breakdown

This deep-dive does not add a new top-level checkpoint.

It extends the existing Phase 5 checkpoints.

### CP4 — Designs Sequence and State Correction

CP4 must additionally cover:

1. separate `options generated` from `under review`
2. ensure generation metadata can support richer option cards later
3. stop treating generation completion as a review milestone
4. prepare the API contract for strategy-aware option metadata

CP4 acceptance additions:

- project state reflects generated options before review
- version payload can carry richer generation metadata
- audit trail clearly separates generation completion from option selection

### CP5 — Designs Decision Workspace

CP5 must additionally cover:

1. show strategy-aware titles and summaries
2. surface key metrics and rationale
3. show strengths and caveats
4. support compare mode using that metadata
5. eliminate raw placeholder-style copy from the UI

CP5 acceptance additions:

- option cards are no longer generic
- compare mode uses meaningful metadata
- the user can understand why options differ

### CP6 — Production Validation and Polish

CP6 must additionally cover:

1. validate at least one real generated-options project
2. assess whether options feel meaningfully differentiated
3. note any remaining placeholder behavior honestly
4. capture screenshot evidence and sequence evidence

CP6 acceptance additions:

- production notes explicitly evaluate option quality, not only page stability
- final audit records whether options feel premium enough for client-facing use

## 5. Priority Recommendation

If the team cannot do everything in one pass, the order should be:

1. fix sequence and gating first
2. improve metadata and naming second
3. improve strategy differentiation third
4. improve hero preview quality fourth
5. add scoring and deeper synthesis fifth

This order preserves delivery safety while still improving what the end user feels first.

## 6. Phase 5 Decision

Phase 5 should treat option generation as a product-quality problem, not just a backend pipeline problem.

The goal is not only:

- `create 3 options`

The goal is:

- `create 3 options that feel intentionally different, explainable, and professionally presented`.

That is the standard the phase should optimize for.

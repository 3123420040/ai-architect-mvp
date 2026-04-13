# Phase 6 - 3D Module Input Contracts

## 1. Goal

This document defines the **best-practice input standard** for each module required to produce a market-grade 3D deliverable that can be shown directly to end users.

The target output is:

- design-faithful 3D scene,
- curated still renders,
- client-facing walkthrough video,
- and an approved delivery package.

This contract assumes a **package-centric** architecture:

`locked brief -> approved canonical 2D design -> presentation scene spec -> render/video generation -> QA gate -> client delivery`

## 2. Module List

| Module | Role | Required input quality | Mock file |
|---|---|---|---|
| Intake Clarification Workspace | Capture and normalize client intent | Discovery-grade, complete, contradiction-aware | [01-intake-clarification-input.json](/Users/nguyenquocthong/project/ai-architect-mvp/implementation/phase-6/mock-inputs/01-intake-clarification-input.json) |
| Brief Lock Contract | Freeze design-relevant requirements | Architect-confirmed, generation-safe | [02-brief-lock-input.json](/Users/nguyenquocthong/project/ai-architect-mvp/implementation/phase-6/mock-inputs/02-brief-lock-input.json) |
| Canonical 2D Design State | Hold the approved spatial truth | Geometry-complete enough for scene derivation | [03-canonical-2d-design-input.json](/Users/nguyenquocthong/project/ai-architect-mvp/implementation/phase-6/mock-inputs/03-canonical-2d-design-input.json) |
| Style and Material Mapper | Turn design direction into deterministic visual rules | Palette-safe, room-aware, facade-aware | [04-style-material-mapper-input.json](/Users/nguyenquocthong/project/ai-architect-mvp/implementation/phase-6/mock-inputs/04-style-material-mapper-input.json) |
| Presentation Scene Spec Builder | Build the normalized 3D scene contract | Deterministic and renderer-ready | [05-presentation-scene-spec.json](/Users/nguyenquocthong/project/ai-architect-mvp/implementation/phase-6/mock-inputs/05-presentation-scene-spec.json) |
| Render and Video Engine | Produce stills and walkthrough | Camera-authored, asset-bound, quality-configured | [06-render-video-request.json](/Users/nguyenquocthong/project/ai-architect-mvp/implementation/phase-6/mock-inputs/06-render-video-request.json) |
| 3D QA Validator | Verify 3D matches approved design truth | Rule-based, evidence-driven, gateable | [07-qa-validator-input.json](/Users/nguyenquocthong/project/ai-architect-mvp/implementation/phase-6/mock-inputs/07-qa-validator-input.json) |
| Delivery and Viewer Bundle | Package client-facing output | Approved-only, presentation-safe | [08-client-delivery-package.json](/Users/nguyenquocthong/project/ai-architect-mvp/implementation/phase-6/mock-inputs/08-client-delivery-package.json) |

## 3. Per-Module Input Standard

### 3.1 Intake Clarification Workspace

Input must contain:

- project type and mode,
- site or apartment context,
- household and occupancy,
- room program,
- lifestyle priorities,
- design goals,
- material and color direction,
- budget and timeline,
- must-haves and must-not-haves,
- presentation intention,
- reference image notes.

Quality bar:

- no unresolved contradictions,
- no missing mandatory fields,
- explicit client-facing priorities,
- and enough context for the architect to lock the brief without guessing.

If this module is weak, every downstream 3D result becomes decorative instead of reliable.

### 3.2 Brief Lock Contract

Input must be a normalized structured brief, not free text.

Mandatory:

- `project_type`
- `project_mode`
- `lot`
- `floors`
- `rooms`
- `occupant_count`
- `household_profile`
- `style`
- `budget_vnd`
- `timeline_months`
- `must_haves`
- `special_requests`

Quality bar:

- architect-confirmed,
- generation-safe,
- no active conflicts,
- enough for option generation and downstream scene planning.

### 3.3 Canonical 2D Design State

This is the most important upstream source for professional 3D.

Input must contain:

- approved version metadata,
- issued package metadata,
- levels,
- walls,
- openings,
- stairs,
- roof,
- room polygons,
- facade orientation,
- site boundary / footprint,
- design approval references.

Quality bar:

- geometry must be structurally complete enough to reconstruct the building massing,
- room semantics must be explicit,
- floor-to-floor heights must be known,
- and facade/opening logic must already be stable.

### 3.4 Style and Material Mapper

Input must contain:

- style family,
- architectural keywords,
- facade identity,
- material palette by zone,
- color palette,
- lighting mood,
- staging policy,
- landscape / entourage policy.

Quality bar:

- rule-based and deterministic,
- no prompt-only ambiguity,
- no visual direction that can contradict approved design intent.

### 3.5 Presentation Scene Spec Builder

This module must receive:

- canonical geometry,
- room semantics,
- style/material mapping,
- shot priorities,
- staging and lighting presets,
- output requirements.

It must output a normalized scene contract with:

- scene hierarchy,
- material assignments,
- room staging rules,
- camera shot list,
- walkthrough sequence,
- output resolution and format targets.

Quality bar:

- renderer-independent,
- deterministic,
- traceable back to locked design truth.

### 3.6 Render and Video Engine

Input must contain:

- `scene_spec`
- renderer config
- still render list
- video shot list
- format and resolution targets
- degraded fallback policy

Quality bar:

- reproducible,
- supports GLB export,
- supports curated stills,
- supports MP4 walkthrough,
- does not improvise geometry not present in the design truth.

### 3.7 3D QA Validator

Input must contain:

- canonical 2D references,
- scene spec,
- generated scene outputs,
- mandatory check list,
- tolerance policy.

Quality bar:

- rule-based first,
- clear pass/fail,
- blocks “client-ready” if geometry, facade, room, or output completeness is off.

### 3.8 Delivery and Viewer Bundle

Input must contain:

- approved scene asset references,
- still render list,
- video asset reference,
- manifest,
- revision and approval metadata,
- branding and disclaimer policy.

Quality bar:

- approved-only,
- presentation-safe,
- linkable,
- ready for client viewing without exposing internal draft artifacts.

## 4. Best-Possible Mock Strategy

The mock inputs in `mock-inputs/` are intentionally written at a higher quality level than the current live system can fully consume.

That is deliberate.

They are meant to show:

1. the **minimum real contract** needed to achieve a professional 3D outcome,
2. not just the smaller contract that the current placeholder pipeline can accept.

## 5. Demo Strategy

The accompanying demo does two things:

1. validates that the mock input chain is structurally complete for the target architecture,
2. runs a real demo through the **current production system** using the `brief lock -> generate -> approve -> derive-3d` path.

This means the demo honestly separates:

- target architecture readiness,
- from current production capability.

## 6. Demo Files

- Demo script: [phase6_3d_mock_demo.py](/Users/nguyenquocthong/project/ai-architect-mvp/scripts/phase6_3d_mock_demo.py)
- Demo report output: [artifacts/phase6-demo/](/Users/nguyenquocthong/project/ai-architect-mvp/artifacts/phase6-demo)

## 7. Important Constraint

Even with ideal input mocks, the **current production implementation** will not yet output:

- walkthrough MP4,
- panorama set,
- or a true client presentation viewer.

Those remain target outputs for the next implementation phase.

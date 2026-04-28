---
title: Output Quality Uplift Implementation Guide and Agent Prompt
phase: 2
status: ready-to-copy
date: 2026-04-28
owner: Codex Coordinator
related_files:
  - 10-remediation-implementation-contract.md
  - 11-remediation-execution-playbook.md
  - 13-output-quality-remediation-plan.md
  - 14-artifact-input-process-quality-contract.md
  - 15-current-artifact-generation-order-and-inputs.md
  - 16-pipeline-orchestration-refactor-implementation.md
  - 17-pipeline-orchestration-refactor-agent-prompt.md
---

# Output Quality Uplift Implementation Guide and Agent Prompt

This file is a standalone handoff for the implementation/testing team that will improve the quality of the generated professional deliverables after the pipeline orchestration refactor is complete.

The purpose is to make the generated files usable as Phase 2 concept deliverables, not merely present on disk or technically openable.

## 1. Background

The current Phase 2 product flow generates the required broad artifact types:

- PDF drawing bundle
- DXF sheets
- DWG or explicit local skip
- GLB model
- FBX model
- USDZ package
- master_4k.mp4
- gate summary JSON/MD

However, current outputs are not yet reliable customer/architect deliverables.

Observed example:

- Project: `3b00f863-3144-4223-b04d-dec825c894d8`
- Version: `b0f39796-d4ba-43f8-92e8-058004ce64d6`
- PDF URL: `http://localhost:18000/media/professional-deliverables/projects/3b00f863-3144-4223-b04d-dec825c894d8/versions/b0f39796-d4ba-43f8-92e8-058004ce64d6/2d/bundle.pdf`
- Observed PDF problem:
  - PDF opens and has pages.
  - But it contains stale hardcoded dimensions such as `5.00 m`, `15.00 m`, and `Ranh đất 5 m x 15 m`.
  - The actual project/version input uses a different geometry, including a `5m x 20m` site boundary in the inspected V4 data.
  - Elevation content overlaps and reads like a generic drawing rather than a generated concept drawing set.

Root cause:

- The raw `DesignVersion.geometry_json` contains more useful design data than the current output preserves.
- The current `DrawingProject` adapter drops too much semantic data.
- PDF/DXF exporters draw from a thin model and still contain hardcoded golden dimensions.
- 3D scene generation is simplified into box primitives.
- Existing gates focus too much on existence/openability and not enough on semantic correctness and visual usefulness.

Quality principle:

```text
exists != valid
valid != usable
usable = selected-version geometry + meaningful content + semantic QA + visual QA + customer-readable readiness
```

## 2. Preconditions

Do not start this output quality uplift until the pipeline orchestration refactor is either complete or explicitly out of scope for the current branch.

Expected orchestration state before this work:

- Product task no longer runs Sprint 4 outputs.
- Product task generates Sprint 2 exactly once.
- Product task does not call `generate_project_ar_video_bundle(...)` directly when generating product bundles.
- `export_usdz` stage corresponds to real USDZ generation.
- `render_video` stage corresponds to real MP4 generation.

If those are not true, stop and report `BLOCKED_BY_PIPELINE_ORCHESTRATION`.

## 3. Objective

Improve the generated artifact quality so the Phase 2 product path produces usable concept deliverables:

- PDF and DXF must use the selected `DesignVersion.geometry_json`, not stale golden dimensions.
- PDF and DXF must show clear concept drawings with site, floor plans, dimensions, room labels, openings, and title blocks.
- GLB/FBX/USDZ must represent the selected design clearly enough for review.
- MP4 must be playable, non-black, collision-safe, and visually useful.
- Gate summaries must report artifact readiness truthfully.

This is still Phase 2. Do not turn this into a construction-document, BIM, permit, IFC, ISO 19650, TCVN/QCVN, or marketing-output project.

## 4. Development Strategy

Do not optimize each exporter independently first.

The correct implementation strategy is:

```text
DesignVersion.geometry_json
  -> ProfessionalDeliverableSourceModel
  -> NormalizedDeliverableModel
  -> DrawingSheetModel / SceneModel / StoryboardModel
  -> Exporter
  -> Technical validation
  -> Semantic validation
  -> Visual QA
  -> Artifact readiness
```

Start with 2D quality because the current wrongness is objective and easy to verify:

1. First source file to inspect/change:
   - `app/services/professional_deliverables/geometry_adapter.py`
2. First new model layer to add:
   - `app/services/professional_deliverables/deliverable_source_model.py`
   - or an equivalent focused module if the codebase already has a better local pattern.
3. First exporters to improve:
   - `app/services/professional_deliverables/pdf_generator.py`
   - `app/services/professional_deliverables/dxf_exporter.py`
4. First tests to add:
   - `tests/professional_deliverables/test_output_quality_2d.py`

Do not start with MP4 or GLB polish. If the shared input model is wrong, 3D and video will inherit poor geometry.

## 5. Scope

In scope:

- Enrich the deliverable input model.
- Preserve more fields from `geometry_json`.
- Remove hardcoded golden dimensions from project outputs.
- Improve PDF/DXF concept drawing quality first.
- Add semantic and visual QA gates for PDF/DXF.
- Then improve GLB/FBX/USDZ/video in later slices using the same normalized input.
- Add artifact-level readiness states in JSON/MD quality reports.
- Preserve existing golden commands and tests.

Out of scope:

- Remote push, PR creation, or commits unless explicitly asked later.
- ADR-001 changes.
- PRD-05 acceptance relaxation.
- Sprint 4 product outputs.
- IFC.
- Pascal Editor integration.
- ISO 19650 process compliance.
- TCVN/QCVN implementation.
- Specular-Glossiness.
- Procedural materials.
- External model upload/import.
- Main API heavy tooling changes.
- Synchronous heavy rendering inside FastAPI requests.
- UI redesign, unless a small API response addition is required for artifact readiness.

## 6. Target Architecture

Recommended modules:

```text
app/services/professional_deliverables/
  deliverable_source_model.py
  deliverable_normalizer.py
  drawing_sheet_model.py
  drawing_layout_engine.py
  drawing_quality_gates.py
  scene_quality_gates.py
  video_quality_gates.py
  artifact_quality_report.py
```

Use this structure pragmatically. If the codebase already has a suitable module, extend it instead of creating unnecessary abstraction.

Core contracts:

- `ProfessionalDeliverableSourceModel`
  - parsed, loss-minimized source model from `DesignVersion.geometry_json` plus `Project.brief_json`.
- `NormalizedDeliverableModel`
  - stable, unit-normalized geometry model for all artifacts.
- `DrawingSheetModel`
  - sheet-specific drawing entities, dimensions, annotations, and layout constraints.
- `SceneModel` or enriched `SceneContract`
  - semantic 3D scene derived from the normalized model.
- `StoryboardModel`
  - shot/camera intent for MP4 generation.
- `ArtifactQualityReport`
  - per-artifact readiness and gate evidence.

## 7. Minimum Input Contract

Before exporting artifacts, the normalized model must preserve or derive:

Project metadata:

- `project_id`
- `version_id`
- `project_name`
- `issue_date`
- `revision_label`
- `brief_summary`
- concept note: `Bản vẽ khái niệm - không dùng cho thi công`

Site:

- boundary polygon
- lot width
- lot depth
- lot area
- north angle
- orientation
- access/front edge if available
- setbacks if available

Levels:

- level id
- floor number
- finished floor elevation
- floor-to-floor height
- clear height
- slab thickness

Rooms:

- room id
- floor/level
- Vietnamese label
- original type
- polygon
- area
- perimeter
- category if available
- finish set if available

Walls:

- wall id
- level
- start/end or polygon
- thickness
- height
- exterior/interior flag
- structural category if available

Openings:

- opening id or schedule mark
- type: door/window
- wall id if available
- position along wall
- width
- height
- sill height
- swing/sliding/fixed operation if available

Fixtures/furniture:

- id
- type
- room id
- position
- dimensions
- rotation
- Vietnamese label/icon mapping

Roof/envelope:

- roof type
- roof outline
- top elevation
- terrace/parapet info if available

Grid/dimensions:

- grid axes
- overall dimension chains
- room/internal dimension chains
- opening dimension chains
- elevation vertical dimension chains

Style/materials:

- category materials
- finish set per room if available
- style direction/palette

## 8. Implementation Slices

## Slice Q0 - Stop Objectively Wrong 2D Outputs

Goal:

Prevent misleading PDF/DXF outputs.

Files likely changed:

- `app/services/professional_deliverables/geometry_adapter.py`
- `app/services/professional_deliverables/pdf_generator.py`
- `app/services/professional_deliverables/dxf_exporter.py`
- `tests/professional_deliverables/test_output_quality_2d.py`

Requirements:

- Remove hardcoded `5.00 m`, `15.00 m`, and `Ranh đất 5 m x 15 m` from project output paths.
- Use actual site boundary and lot dimensions.
- Use actual north angle.
- Fail clearly if site geometry is missing.
- Never silently substitute golden dimensions.

Tests:

- `test_pdf_uses_actual_lot_dimensions_for_project_geometry`
- `test_pdf_does_not_contain_stale_golden_dimensions`
- `test_dxf_uses_actual_lot_dimensions_for_project_geometry`
- `test_dxf_extents_match_site_boundary`

Acceptance:

- A non-golden `5m x 20m` project does not show `5m x 15m`.
- A `7m x 25m` fixture/project shows `7.00 m` and `25.00 m` where appropriate.
- DXF extents match the source site boundary.

## Slice Q1 - Build 2D Drawing Model and Layout

Goal:

Make PDF/DXF concept-usable, not just technically openable.

Files likely added:

- `app/services/professional_deliverables/drawing_sheet_model.py`
- `app/services/professional_deliverables/drawing_layout_engine.py`
- `app/services/professional_deliverables/drawing_quality_gates.py`

Files likely changed:

- `app/services/professional_deliverables/sheet_assembler.py`
- `app/services/professional_deliverables/pdf_generator.py`
- `app/services/professional_deliverables/dxf_exporter.py`

Requirements:

- Generate one site sheet.
- Generate one floor plan sheet per floor.
- Generate concept elevation and section sheets.
- Add title block fields:
  - project name
  - version/revision
  - issue date
  - sheet number/title
  - scale
  - concept-only note
- Add room labels in Vietnamese.
- Add room area labels.
- Add basic dimension chains:
  - overall site width/depth
  - building/room dimensions where available
- Add door/window symbols.
- Add fixture/furniture symbols where available.
- Add page-fit scale calculation.
- Prevent drawing content from overlapping title blocks.

PDF gates:

- `PDF_PAGE_COUNT`
- `PDF_DYNAMIC_DIMENSIONS`
- `PDF_SITE_BOUNDARY_MATCH`
- `PDF_FLOOR_COUNT`
- `PDF_ROOM_LABELS`
- `PDF_ROOM_AREAS`
- `PDF_DIMENSION_CHAINS`
- `PDF_NO_TITLE_OVERLAP`
- `PDF_PAGE_RENDER_NONBLANK`
- `PDF_ELEVATION_LAYOUT`

DXF gates:

- `DXF_OPENABLE`
- `DXF_UNITS_METERS`
- `DXF_REQUIRED_LAYERS`
- `DXF_PROJECT_EXTENTS_MATCH`
- `DXF_DIMENSIONS_MATCH`
- `DXF_ROOM_LABELS`
- `DXF_OPENING_SYMBOLS`
- `DXF_NO_STALE_GOLDEN_LABELS`

Acceptance:

- PDF opens and each page renders to PNG.
- PDF page previews are non-blank.
- Room labels and areas are present.
- Elevation/section sheets do not overlap title block or each other.
- DXF opens with `ezdxf`.
- DXF has expected layers, units, extents, room labels, openings, and dimensions.

## Slice Q2 - Add Artifact Quality Report

Goal:

Make readiness explicit and machine-readable.

Files likely added:

- `app/services/professional_deliverables/artifact_quality_report.py`

Requirements:

- Introduce per-artifact quality dimensions:
  - `exists`
  - `format_valid`
  - `semantic_valid`
  - `visual_qa`
  - `customer_ready`
- Report artifact state:
  - `ready`
  - `partial`
  - `failed`
  - `skipped`
- Include:
  - project id
  - version id
  - bundle id if available
  - artifact role
  - path
  - byte size
  - sha256
  - gate code
  - severity
  - user-facing message
  - technical detail

Acceptance:

- Gate summary JSON can tell UI/devs which files are usable.
- Gate summary MD can be read by PM/architect without raw logs.
- DWG local skip is explicit and not confused with failure.

## Slice Q3 - Improve GLB/FBX Semantic Scene Quality

Goal:

Make the 3D model review-usable.

Files likely changed:

- `app/services/professional_deliverables/scene_builder.py`
- `app/services/professional_deliverables/sprint2_demo.py`
- `app/services/professional_deliverables/fbx_exporter.py` or equivalent

Requirements:

- Generate wall solids with thickness and height.
- Segment wall geometry around openings or otherwise make openings visually clear.
- Generate room floor surfaces.
- Generate floor slabs per storey.
- Generate roof/envelope from source geometry.
- Add semantic object names and metadata.
- Improve fixture/furniture primitives by type.
- Add GLB QA thumbnails:
  - isometric
  - top
  - front

Gates:

- `GLB_VALIDATOR_PASS`
- `GLB_BOUNDS_MATCH_SITE`
- `GLB_FLOOR_COUNT_MATCH`
- `GLB_ROOM_SURFACES_PRESENT`
- `GLB_WALL_OPENINGS_PRESENT`
- `GLB_MATERIALS_ASSIGNED`
- `GLB_QA_THUMBNAILS_NONBLANK`
- `FBX_BLENDER_IMPORT`
- `FBX_EXTENTS_MATCH_GLB`
- `FBX_UNITS_SCALE_VALID`
- `FBX_OBJECT_NAMES_SEMANTIC`

Acceptance:

- GLB loads in viewer.
- GLB represents the selected version, not a generic mass.
- Object counts/bounds match the normalized source.
- FBX imports into Blender at correct scale/orientation.

## Slice Q4 - Improve USDZ and MP4

Goal:

Make AR/video artifacts trustworthy after the 3D scene is semantically useful.

USDZ requirements:

- Use the improved GLB/scene.
- Validate with `usd-core==26.5`.
- Check scale, origin, ground plane, material parity, texture budget, and size budget.

MP4 requirements:

- Build a storyboard from the normalized model.
- Generate camera-safe zones.
- Rank important rooms.
- Run camera path preflight before rendering.
- Fail early with `CAMERA_PATH_UNSAFE` if no safe path exists.
- Validate MP4 immediately after render.
- Generate keyframes/contact sheet.

Video gates:

- `VIDEO_CAMERA_PREFLIGHT`
- `VIDEO_RENDER_COMPLETED`
- `VIDEO_FFPROBE_VALID`
- `VIDEO_DECODE_CLEAN`
- `VIDEO_NONBLACK_KEYFRAMES`
- `VIDEO_CAMERA_COLLISION_FREE`
- `VIDEO_CONTACT_SHEET_GENERATED`

Acceptance:

- USDZ opens as a USD stage.
- MP4 is valid, playable, 4K, non-black, and collision-free.
- Invalid MP4 is never exposed as ready.

## 9. Required Verification Commands

API focused:

```bash
cd /Users/nguyenquocthong/project/ai-architect/ai-architect-api
PYTHONPATH=. .venv/bin/python -m pytest tests/professional_deliverables/test_output_quality_2d.py
PYTHONPATH=. .venv/bin/python -m pytest tests/professional_deliverables
PYTHONPATH=. .venv/bin/python -m pytest tests/test_foundation.py tests/test_flows.py
make sprint3-ci-linux
```

If 3D/video quality code changes:

```bash
cd /Users/nguyenquocthong/project/ai-architect/ai-architect-api
PYTHONPATH=. .venv/bin/python -m pytest tests/professional_deliverables/test_sprint3_camera_and_video.py
PYTHONPATH=. .venv/bin/python -m pytest tests/professional_deliverables/test_sprint3_usdz.py
```

Web is only required if API response shape or Delivery UI changes:

```bash
cd /Users/nguyenquocthong/project/ai-architect/ai-architect-web
pnpm lint
pnpm build
```

Manual artifact checks:

- Open the generated PDF and inspect all pages.
- Render PDF pages to PNG and inspect non-blank previews.
- Open DXF with `ezdxf.readfile`.
- Check extracted PDF text for stale golden dimensions.
- Check artifact quality JSON/MD for customer-readable readiness.

## 10. Agent Prompt

Copy and send this prompt to the implementation/testing agent.

```text
You are the Implementation and Verification Agent for AI Architect Phase 2 Professional Deliverables Output Quality Uplift.

You have access to the current source code for all three repos. Implement the work, add focused tests, run verification, and report back. Do not stop at analysis unless you hit a true blocker.

Work from the shared project root:

cd /Users/nguyenquocthong/project/ai-architect

Repos:
- API repo: /Users/nguyenquocthong/project/ai-architect/ai-architect-api
- Web repo: /Users/nguyenquocthong/project/ai-architect/ai-architect-web
- Docs/compose repo: /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp

Read these documents first, in this order:

Core context:
1. /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/docs/phase-2/03-adr-001-standards-combo.md
2. /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/docs/phase-2/05-prd-deliverables.md
3. /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/docs/phase-2/07-local-git-verification-protocol.md

Remediation context:
4. /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/docs/phase-2/handoffs/ui-e2e-professional-deliverables/10-remediation-implementation-contract.md
5. /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/docs/phase-2/handoffs/ui-e2e-professional-deliverables/11-remediation-execution-playbook.md
6. /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/docs/phase-2/handoffs/ui-e2e-professional-deliverables/13-output-quality-remediation-plan.md
7. /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/docs/phase-2/handoffs/ui-e2e-professional-deliverables/14-artifact-input-process-quality-contract.md
8. /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/docs/phase-2/handoffs/ui-e2e-professional-deliverables/15-current-artifact-generation-order-and-inputs.md
9. /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/docs/phase-2/handoffs/ui-e2e-professional-deliverables/16-pipeline-orchestration-refactor-implementation.md
10. /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/docs/phase-2/handoffs/ui-e2e-professional-deliverables/18-output-quality-uplift-implementation-guide-and-agent-prompt.md

Primary objective:

Improve the quality of generated Phase 2 professional deliverables so they are usable concept deliverables, not merely files that exist or pass technical openability checks.

The first implementation target is 2D quality:

- normalized deliverable input model;
- PDF drawing bundle;
- DXF sheets;
- 2D semantic and visual QA gates;
- artifact readiness reporting.

Do not start with GLB/video polish. The shared input model and 2D outputs are currently the first correctness bottleneck.

Regression evidence:

- Project: 3b00f863-3144-4223-b04d-dec825c894d8
- Version: b0f39796-d4ba-43f8-92e8-058004ce64d6
- Example PDF: http://localhost:18000/media/professional-deliverables/projects/3b00f863-3144-4223-b04d-dec825c894d8/versions/b0f39796-d4ba-43f8-92e8-058004ce64d6/2d/bundle.pdf
- Known issue: generated PDF contains stale hardcoded `5m x 15m` and `5.00 m` / `15.00 m` labels even when selected version geometry differs.
- Known issue: elevation layout overlaps and does not read as a usable concept sheet.

Precondition:

Before implementing quality uplift, confirm the pipeline orchestration refactor is complete or not relevant on the current branch:

- Product path does not run Sprint 4 outputs.
- Product path generates Sprint 2 exactly once.
- export_usdz stage corresponds to USDZ generation.
- render_video stage corresponds to MP4 generation.

If this is false, report BLOCKED_BY_PIPELINE_ORCHESTRATION and do not mix orchestration refactor with quality uplift.

Hard non-goals:

- No remote push.
- No PR.
- No commit unless explicitly asked later.
- No ADR-001 changes.
- No PRD-05 acceptance relaxation.
- No Sprint 4 product outputs.
- No IFC.
- No Pascal Editor integration.
- No ISO 19650 process compliance.
- No TCVN/QCVN implementation.
- No Specular-Glossiness.
- No procedural materials.
- No external model upload/import.
- Do not replace or weaken the golden fixture pipeline.
- Do not run heavy generation synchronously inside a FastAPI request.
- Do not add heavy toolchains to the main API image.
- Do not do broad UI redesign in this task.

Implementation plan:

Step 1 - Inspect current input loss
- Read geometry_adapter.py and identify which fields from ai-architect-geometry-v2 are currently dropped.
- Read pdf_generator.py and dxf_exporter.py to locate all hardcoded site/dimension labels.
- Read sheet_assembler.py to understand current sheet set.
- Record current gaps in the final report.

Step 2 - Add or extend normalized deliverable input model
- Add ProfessionalDeliverableSourceModel or extend the existing DrawingProject in a way that preserves:
  - project/version metadata;
  - site boundary, lot width/depth/area, north angle;
  - levels with heights/elevations;
  - rooms with Vietnamese label, polygon, area, perimeter;
  - walls with thickness/height/exterior-interior flag where available;
  - openings with width/height/sill/swing/schedule where available;
  - fixtures/furniture with type/position/dimensions/rotation;
  - roof/envelope;
  - grid and dimension chains;
  - style/material hints.
- Do not silently use golden fallback data.
- Fail clearly if critical geometry is missing.

Step 3 - Add 2D drawing sheet/layout model
- Add DrawingSheetModel and layout helpers if no equivalent exists.
- Represent:
  - site plan;
  - floor plans;
  - elevations;
  - sections;
  - title blocks;
  - dimensions;
  - annotations;
  - viewport/page-fit constraints.
- Keep it small and focused. Do not overbuild a CAD engine.

Step 4 - Fix PDF first
- Remove all hardcoded golden dimensions from PDF output.
- Use actual site boundary and lot dimensions.
- Add title block fields and concept-only note.
- Add room labels and room areas.
- Add overall dimensions.
- Add north arrow from source north angle.
- Add door/window/fixture symbols where available.
- Fix elevation/section layout so content does not overlap title block or other frames.
- Render PDF pages to PNG for QA where local dependencies allow.

Step 5 - Fix DXF using the same drawing model
- Remove all hardcoded golden dimensions from DXF output.
- Use actual extents and dimensions.
- Preserve meters units.
- Preserve required layers.
- Add basic blocks/symbols for doors/windows/fixtures/north arrow if practical.
- Add semantic checks for extents, labels, openings, and dimensions.

Step 6 - Add quality gates and readiness
- Add PDF gates:
  - PDF_PAGE_COUNT
  - PDF_DYNAMIC_DIMENSIONS
  - PDF_SITE_BOUNDARY_MATCH
  - PDF_FLOOR_COUNT
  - PDF_ROOM_LABELS
  - PDF_ROOM_AREAS
  - PDF_DIMENSION_CHAINS
  - PDF_NO_TITLE_OVERLAP
  - PDF_PAGE_RENDER_NONBLANK
  - PDF_ELEVATION_LAYOUT
- Add DXF gates:
  - DXF_OPENABLE
  - DXF_UNITS_METERS
  - DXF_REQUIRED_LAYERS
  - DXF_PROJECT_EXTENTS_MATCH
  - DXF_DIMENSIONS_MATCH
  - DXF_ROOM_LABELS
  - DXF_OPENING_SYMBOLS
  - DXF_NO_STALE_GOLDEN_LABELS
- Add artifact readiness dimensions:
  - exists
  - format_valid
  - semantic_valid
  - visual_qa
  - customer_ready
- Use states:
  - ready
  - partial
  - failed
  - skipped

Step 7 - Add tests
- Add or update tests under:
  /Users/nguyenquocthong/project/ai-architect/ai-architect-api/tests/professional_deliverables/
- Required tests:
  - test_pdf_uses_actual_lot_dimensions_for_project_geometry
  - test_pdf_does_not_contain_stale_golden_dimensions
  - test_pdf_renders_pages_nonblank
  - test_pdf_room_labels_and_areas_present
  - test_pdf_elevation_frames_do_not_overlap
  - test_dxf_uses_actual_lot_dimensions_for_project_geometry
  - test_dxf_extents_match_site_boundary
  - test_dxf_required_layers_and_units
  - test_dxf_room_labels_and_openings_present
  - test_quality_report_contains_artifact_readiness
- Preserve existing golden tests.

Step 8 - Only then continue to 3D/video quality if time remains
- Improve GLB/FBX semantic scene quality only after 2D gates pass.
- Improve USDZ after GLB is semantically useful.
- Improve MP4 after scene/camera input is reliable.
- If you do not reach these slices, report them as deferred rather than mixing partial work.

Likely files to change:

API:
- app/services/professional_deliverables/geometry_adapter.py
- app/services/professional_deliverables/deliverable_source_model.py
- app/services/professional_deliverables/deliverable_normalizer.py
- app/services/professional_deliverables/drawing_sheet_model.py
- app/services/professional_deliverables/drawing_layout_engine.py
- app/services/professional_deliverables/drawing_quality_gates.py
- app/services/professional_deliverables/pdf_generator.py
- app/services/professional_deliverables/dxf_exporter.py
- app/services/professional_deliverables/demo.py
- app/services/professional_deliverables/orchestrator.py
- tests/professional_deliverables/

Do not change Web unless the API response shape for readiness must be exposed.

Verification commands:

cd /Users/nguyenquocthong/project/ai-architect/ai-architect-api
PYTHONPATH=. .venv/bin/python -m pytest tests/professional_deliverables/test_output_quality_2d.py
PYTHONPATH=. .venv/bin/python -m pytest tests/professional_deliverables
PYTHONPATH=. .venv/bin/python -m pytest tests/test_foundation.py tests/test_flows.py
make sprint3-ci-linux

If Web changes are made:

cd /Users/nguyenquocthong/project/ai-architect/ai-architect-web
pnpm lint
pnpm build

Manual verification:

1. Generate a professional deliverables bundle for project 3b00f863-3144-4223-b04d-dec825c894d8.
2. Open 2d/bundle.pdf.
3. Confirm stale `5m x 15m`, `5.00 m`, and `15.00 m` do not appear unless they match actual geometry.
4. Confirm the site plan dimensions match the selected version geometry.
5. Confirm floor sheets include room names, room areas, openings, dimensions, and title blocks.
6. Confirm elevation/section pages are not visibly overlapped.
7. Open generated DXF files with ezdxf.
8. Confirm DXF units, extents, layers, room labels, openings, and dimensions.
9. Inspect quality report JSON/MD and confirm artifact readiness is customer-readable.

Final report format:

Decision: PASS | BLOCKED | NEEDS_REVIEW

Repos:
- API repo:
- API branch:
- API dirty status:
- Web repo:
- Web branch:
- Web dirty status:
- Docs repo:
- Docs branch:
- Docs dirty status:

Summary:
- Fixed:
- Not fixed:
- Deferred:

Precondition:
- Pipeline orchestration refactor status:
- Sprint 4 product outputs absent:
- Product stage order preserved:

Input model coverage:
- Project/version metadata:
- Site:
- Levels:
- Rooms:
- Walls:
- Openings:
- Fixtures/furniture:
- Roof/envelope:
- Grid/dimensions:
- Style/materials:

PDF quality coverage:
- Dynamic dimensions:
- No stale golden labels:
- Site boundary match:
- Floor count:
- Room labels:
- Room areas:
- Dimension chains:
- No title overlap:
- Page render QA:
- Elevation/section layout:

DXF quality coverage:
- Openable:
- Units:
- Required layers:
- Project extents:
- Dimensions:
- Room labels:
- Opening symbols:
- No stale golden labels:

Artifact readiness:
- Quality report JSON:
- Quality report MD:
- ready/partial/failed/skipped semantics:
- DWG skip handling:

Files changed:
- API:
- Web:
- Docs/compose:

Commands run:
1.
2.
3.

Test results:
- test_output_quality_2d:
- full tests/professional_deliverables:
- foundation/flows:
- sprint3-ci-linux:
- web lint/build, if run:

Manual evidence:
- Project id:
- Version id:
- Bundle/job id:
- PDF path:
- DXF paths:
- Quality report paths:
- Before/after stale dimension result:

Known issues:
-

Scope compliance:
- No remote push:
- No PR:
- No Sprint 4 product outputs:
- No deferred roadmap items:
- No main API heavy toolchain:
- No synchronous render request:
- Golden fixture pipeline preserved:

Return PASS only if:
- PDF/DXF no longer contain stale golden dimensions for non-golden project outputs.
- PDF/DXF use the selected version geometry.
- PDF pages render and are inspectable.
- DXF opens and has correct units/extents/layers.
- 2D semantic gates pass.
- Artifact readiness is explicit in JSON/MD.
- Existing golden and professional deliverables tests pass.

Return NEEDS_REVIEW if:
- 2D correctness is fixed but a non-critical visual polish detail remains.
- 3D/video quality remains deferred by design after 2D pass.

Return BLOCKED if:
- Pipeline orchestration precondition is false.
- The source geometry lacks mandatory data and no safe fallback is allowed.
- Required local dependencies prevent even focused 2D verification from running.
```

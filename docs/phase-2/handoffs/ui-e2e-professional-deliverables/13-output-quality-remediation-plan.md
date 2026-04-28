---
title: Professional Deliverables Output Quality Remediation Plan
phase: 2
status: ready-for-implementation-planning
date: 2026-04-28
owner: Codex Coordinator
related_files:
  - 09-retro-action-plan.md
  - 10-remediation-implementation-contract.md
  - 11-remediation-execution-playbook.md
  - 12-remediation-agent-prompt.md
---

# Professional Deliverables Output Quality Remediation Plan

This document defines how to raise the quality of each generated professional deliverable file so the outputs are not merely "created" or "format-valid", but actually usable for customer review, architect handoff, and local Phase 2 acceptance.

The current pipeline already has several useful gates, but the gates are still too format-oriented. A PDF can have embedded Vietnamese fonts and still be unusable if dimensions are hardcoded. A GLB can pass glTF validation and still be unusable if the house is just simplified boxes. A 4K MP4 can be valid H.264 and still be unusable if it is visually uninformative or camera paths collide with walls.

## Quality Principle

For every artifact, separate three levels:

1. **Exists**: file was produced and is non-empty.
2. **Valid**: file can be opened by standard tools and passes technical validators.
3. **Usable**: file represents the selected `DesignVersion.geometry_json` accurately, communicates useful architectural information, and has enough visual/document quality for a customer or architect to act on.

Phase 2 remediation should move each artifact from `exists/valid` to at least `usable concept deliverable`. It does not need to become a construction-permit or ISO 19650 deliverable.

## Current Quality Problems Observed

### Cross-artifact problems

- Some outputs are generated from simplified drawing/scene contracts that do not preserve enough design fidelity.
- PDF/DXF generation contains hardcoded 5m x 15m labels and site geometry in places, which makes real project outputs wrong.
- 3D outputs use mostly box meshes and do not cut real openings through walls.
- Gates focus on file existence, technical openability, and some material/video checks, but not enough on semantic correctness or visual usefulness.
- Failed or partial outputs were previously hidden from UI, making it difficult to inspect quality.
- There is no artifact-level visual QA report showing thumbnails/previews for PDF pages, DXF sheets, GLB/USDZ views, and video keyframes.

### Important distinction

The existing golden output can pass technical gates, but that does not prove product quality for generated project geometry. The remediation must add project-specific semantic and visual quality gates.

## Output Quality Targets By File

## 1. PDF Drawing Bundle

Expected file:

- `2d/bundle.pdf`

Current likely issues:

- Dimension labels can be hardcoded as `5.00 m` and `15.00 m` instead of using `project.lot_width_m` and `project.lot_depth_m`.
- Site drawing can contain hardcoded 5m x 15m boundary text and geometry.
- Layout may not adapt to different lot sizes.
- Floor plans are schematic and may not have enough hierarchy: wall thickness, room area labels, door swings, windows, furniture, fixtures, north orientation, scale bar, legend.
- Elevations and sections are generic schematic boxes, not derived from actual openings/roof/room arrangement.
- No visual QA renders of each page are produced for quick inspection.

Quality target:

- PDF is a clean Vietnamese concept drawing set, not a construction document.
- Every sheet uses the selected version geometry and project metadata.
- No hardcoded lot dimensions, sheet labels, or site extents.
- Page layout is stable for common lot sizes.
- Text does not overlap drawing content or title blocks.
- Vietnamese labels render correctly.
- Scale and dimension annotations match actual geometry.

Required sheet content:

- Cover/title information in title block:
  - project name
  - version number/id if available
  - issue date
  - sheet number
  - scale
  - explicit note: `Bản vẽ khái niệm - không dùng cho thi công`
- Site plan:
  - lot boundary from geometry
  - roof/building footprint
  - north arrow from `north_angle`
  - lot dimensions
  - setback/context placeholders only if available
- Floor plans:
  - one sheet per floor
  - walls with clear lineweight
  - room names in Vietnamese
  - room area labels
  - doors/windows with usable symbols
  - fixtures/furniture where available
  - dimension strings from actual geometry
  - scale bar
- Elevations:
  - concept elevations derived from storeys, wall/opening positions, roof outline
  - floor level lines
  - basic openings aligned to floor geometry when possible
- Sections:
  - concept cross/long section
  - floor-to-floor heights
  - slab/roof indication

Implementation guidance:

- Refactor PDF drawing into a reusable `DrawingLayoutModel`.
- Replace all hardcoded dimensions with dynamic values:
  - `project.lot_width_m`
  - `project.lot_depth_m`
  - `project.storeys`
  - `project.roof_outline`
- Add a page-fit strategy:
  - compute scale from available drawing frame
  - use declared scale if it fits
  - otherwise choose a documented fallback scale such as 1:150/1:200 and label it
- Add room area calculations.
- Add text collision checks for room labels and title block.
- Generate PNG previews for every PDF page as QA artifacts.

Suggested validators:

- `pdfinfo` or Python PDF parser confirms page count and metadata.
- Text extraction confirms Vietnamese text and no replacement characters.
- Render pages to PNG and verify non-blank content.
- Dynamic dimension test confirms a 7m x 25m project never shows `5.00 m` / `15.00 m`.
- Pixel/geometry check confirms title block and drawing content do not overlap.
- Sheet inventory gate confirms expected sheets exist.

Acceptance criteria:

- PDF opens locally.
- Every page renders to PNG.
- All dimensions match the project geometry.
- No hardcoded golden dimensions appear in a non-golden project.
- The PDF is acceptable as a concept review drawing bundle.

## 2. DXF Sheets

Expected files:

- `2d/*.dxf`

Current likely issues:

- Dimensions and site boundary labels can be hardcoded.
- Geometry uses simple lines/polylines and text instead of proper CAD dimensions/blocks.
- Modelspace only may be acceptable for first slice, but it is less usable for architect handoff.
- Door arcs, window symbols, fixture blocks, hatches, linetypes, and lineweights are very basic.
- Elevations/sections are generic rather than meaningfully derived.

Quality target:

- DXF files are CAD-usable concept drawings.
- They open cleanly in common CAD tools.
- Units, layers, lineweights, and entity organization are predictable.
- The geometry is accurate enough for downstream review and editing.

Required improvements:

- Remove hardcoded lot dimensions and site extents.
- Use actual project geometry for all sheet types.
- Use CAD `DIMENSION` entities or at least consistent dimension layer/text placement.
- Add reusable blocks for:
  - door
  - window
  - toilet/sink basic plumbing fixture
  - furniture placeholder
  - column
  - north arrow
- Use hatches or layer styles for walls/slabs where appropriate.
- Add paper/layout support if feasible:
  - layout title block
  - viewport or scaled model content
- Keep AIA-like layer dictionary consistent.

Suggested validators:

- `ezdxf.readfile()` can open every DXF.
- `$INSUNITS` is meters.
- Required layers exist.
- Required sheet entities exist:
  - walls
  - room boundaries
  - room labels
  - dimensions
  - openings
  - title note
- No text contains stale golden dimensions for non-golden projects.
- Bounding boxes fit expected project extents.

Acceptance criteria:

- Each DXF opens with ezdxf without repair.
- A 7m x 25m project has CAD extents and dimension labels matching 7m x 25m.
- Architect can identify rooms, walls, openings, dimensions, and sheet purpose.

## 3. DWG

Expected files:

- `2d/*.dwg`

Local PM decision:

- DWG may be skipped locally when ODA is unavailable.
- Skip must be explicit and customer-readable.

Current likely issues:

- No DWG is produced locally without ODA.
- When produced, quality depends entirely on DXF quality.

Quality target:

- If ODA is configured, DWG is a faithful conversion of the DXF sheet set.
- If ODA is not configured, the system reports a clear skip reason and does not mark DWG as failed unless DWG is required in that environment.

Required improvements:

- Make DWG status explicit per artifact:
  - `ready`
  - `skipped`
  - `failed`
- If ODA exists:
  - convert all DXF sheets
  - audit open by converting DWG back to DXF or using ODA audit
  - verify file count matches DXF count
- If ODA missing:
  - record skip reason: `ODA/DWG converter unavailable locally`
  - expose skip in Delivery UI

Suggested validators:

- ODA command exit code.
- File count parity with DXF.
- Re-open or roundtrip audit.
- Non-zero file size.

Acceptance criteria:

- Local: DWG skipped with explicit reason.
- ODA environment: DWG files open and preserve layers/units.

## 4. GLB

Expected file:

- `3d/model.glb`

Current likely issues:

- Scene is mostly box meshes: slabs, walls, openings represented as boxes, fixtures as boxes.
- Openings are not actually cut through walls.
- Materials are technically valid but not necessarily visually convincing.
- Geometry may pass glTF validation while still lacking architectural clarity.
- Scale/origin may be correct, but usability depends on navigation and semantic object naming.

Quality target:

- GLB is a usable architectural preview model for the selected design version.
- It should show the building massing, floors, walls, openings, roof, fixtures/furniture placeholders, and basic material differentiation.
- It should be lightweight enough for web viewing.

Required improvements:

- Improve scene generation from `DrawingProject`:
  - walls with real thickness and height
  - openings cut or visually subtracted from walls
  - slabs/floors per storey
  - roof outline from geometry
  - stairs if geometry provides them
  - room floor surfaces with semantic names
  - basic furniture/fixture shapes by type, not all generic boxes
- Use stable object names and IDs:
  - room/floor/wall/opening ids must trace back to geometry
  - useful for viewer inspection later
- Add viewer-friendly metadata:
  - project id
  - version id
  - units
  - north angle
  - floors
  - generated timestamp
- Generate QA thumbnails from canonical camera angles.

Suggested validators:

- glTF validator: errors 0, warnings acceptable only if documented.
- Scene semantic validator:
  - expected floors count
  - expected room count
  - expected wall count
  - expected opening count
  - no NaN/zero-size major elements
  - bounding box matches lot/building dimensions
- Visual render smoke:
  - front/isometric/top thumbnails are non-blank
  - model is centered and framed
- Web viewer smoke:
  - GLB loads in browser
  - camera framing is usable

Acceptance criteria:

- GLB loads in Viewer.
- Model communicates the design, not just a generic mass.
- Object count and bounds match the selected geometry.
- Valid GLB from partial bundles can be viewed with a warning.

## 5. FBX

Expected file:

- `3d/model.fbx`

Current likely issues:

- FBX may technically import in Blender, but may not be optimized for downstream DCC/BIM-adjacent workflows.
- Materials, units, axes, object names, UVs, and hierarchy need stronger QA.

Quality target:

- FBX is a clean handoff model for common 3D tools such as Blender/Twinmotion-style workflows.

Required improvements:

- Preserve units and axis orientation:
  - meters source
  - documented export scale
  - Z-up expected in downstream tools
- Preserve semantic object names.
- Preserve material assignments.
- Avoid duplicate or orphan meshes/materials.
- Ensure UV0 exists for textured materials.
- Include a small import report.

Suggested validators:

- Blender import smoke:
  - imports without errors
  - expected mesh count
  - expected material count
  - bounding box in expected units
  - no extreme scale factor
  - no missing UVs for textured materials
- Compare GLB vs FBX:
  - approximate extents match
  - material names match or are mapped

Acceptance criteria:

- FBX imports in Blender cleanly.
- Scale and orientation are correct.
- Mesh/material hierarchy remains understandable.

## 6. USDZ

Expected file:

- `3d/model.usdz`

Current likely issues:

- USDZ can pass structure/size/material gates but still inherit weak geometry from GLB.
- Local worker previously missed `usd-core`, which weakens USDZ validation.
- AR usability depends on correct scale, origin, materials, and package size.

Quality target:

- USDZ is a usable AR preview package of the same architectural model represented by GLB.

Required improvements:

- Ensure professional worker has `usd-core==26.5`.
- Keep GLB/USDZ material parity.
- Preserve scale and orientation.
- Keep package size within AR budget.
- Include AR-friendly origin:
  - model centered appropriately
  - ground plane at Z=0
  - no giant offsets
- Add quick-look metadata if supported by toolchain.

Suggested validators:

- `Usd.Stage.Open` succeeds.
- Compliance checker passes or reports only documented non-blocking warnings.
- Package texture payload is complete.
- Max texture size within policy.
- Triangle count and file size within budget.
- GLB/USDZ material parity passes.
- AR smoke report confirms bounding box and units.

Acceptance criteria:

- USDZ opens as a USD stage.
- Package size and texture budget pass.
- Model appears at correct scale in AR-capable viewers.

## 7. Master 4K MP4

Expected file:

- `video/master_4k.mp4`

Current known issues:

- One real project produced a 48-byte invalid MP4 with `moov atom not found`.
- Another produced a valid 4K MP4 but failed camera collision sanity.
- Current video can be technically valid while still being visually weak or unhelpful.

Quality target:

- MP4 is a real 4K walkthrough/review video that communicates the design.
- It must be valid, playable, non-black, properly framed, and free of camera-wall collisions.

Required improvements:

- Validate immediately after render:
  - ffprobe format
  - duration
  - dimensions
  - fps
  - codec
  - moov atom
  - decoder pass
- Fail at `render_video` or `validate` if invalid.
- Do not run derivative or later processing on invalid MP4.
- Improve camera planning:
  - pre-check camera path against wall bounding boxes before render
  - maintain safe offsets
  - fallback camera routes for tight rooms
  - avoid clipping through walls/ceilings
- Improve visual storytelling:
  - exterior establishing shot
  - top/floor plan context if useful
  - major rooms
  - vertical/floor transition
  - ending overview
- Add keyframe thumbnails/contact sheet for QA.

Suggested validators:

- ffprobe:
  - width `3840`
  - height `2160`
  - fps `30`
  - duration near `60s`
  - codec H.264 or approved codec
- ffmpeg decode:
  - no decode errors
- frame QA:
  - first/middle/last frames non-black
  - frame hashes deterministic for same inputs
  - brightness/contrast within reasonable range
  - camera target in frame
- collision QA:
  - no keyframe intersects walls
  - no camera route goes outside valid bounds unless exterior shot is intentional

Acceptance criteria:

- MP4 plays locally.
- `ffprobe` passes.
- No invalid 48-byte MP4 can be exposed as ready or partial.
- Camera path does not collide on known V4 regression geometry.
- Video tells the design story clearly enough for customer review.

## 8. Gate Summary JSON

Expected files:

- `2d/sprint1_gate_summary.json`
- `3d/sprint2_gate_summary.json`
- `sprint3_gate_summary.json`
- Product-level gate summary JSON if introduced.

Current likely issues:

- Gate summaries are technically useful but not enough for product-level quality.
- They mix low-level tool gates with acceptance logic.
- Failed gates are not always surfaced in UI in customer-readable form.

Quality target:

- JSON is machine-readable evidence for every artifact.
- It should explain exactly which gates passed, failed, skipped, or produced warnings.

Required improvements:

- Add artifact-level gates:
  - `artifact_exists`
  - `format_valid`
  - `semantic_valid`
  - `visual_qa`
  - `customer_ready`
- Include:
  - project id
  - version id
  - bundle id
  - generator version/hash if available
  - artifact inventory with paths, byte sizes, sha256
  - gate results with stable codes
  - user-facing summary
  - technical detail
- Keep skipped gates explicit.
- Separate allowed local skip from product failure.

Suggested schema:

```json
{
  "status": "pass|partial|fail",
  "project_id": "...",
  "version_id": "...",
  "bundle_id": "...",
  "artifacts": [
    {
      "role": "pdf",
      "path": "2d/bundle.pdf",
      "status": "ready|partial|failed|skipped",
      "byte_size": 123,
      "sha256": "...",
      "quality": {
        "exists": true,
        "format_valid": true,
        "semantic_valid": true,
        "visual_qa": true,
        "customer_ready": true
      }
    }
  ],
  "gates": [
    {
      "code": "PDF_DYNAMIC_DIMENSIONS",
      "name": "PDF dynamic dimensions",
      "status": "pass",
      "severity": "required",
      "user_message": "Drawing dimensions match the project geometry.",
      "technical_detail": "Expected 7.00m x 25.00m; found matching labels."
    }
  ]
}
```

Acceptance criteria:

- UI can show customer-readable failure/partial state from JSON data.
- Dev can debug tool-level failures from technical detail.
- Every artifact has a clear readiness state.

## 9. Gate Summary Markdown

Expected files:

- `2d/sprint1_gate_summary.md`
- `3d/sprint2_gate_summary.md`
- `sprint3_gate_summary.md`
- Product-level gate summary MD if introduced.

Current likely issues:

- Markdown is short and gate-oriented.
- It does not serve as a useful QA review report for non-developers.

Quality target:

- Markdown is a human-readable QA report.
- It should be useful to the PM, architect, and implementation agent.

Required content:

- Executive status:
  - `Ready`
  - `Partial`
  - `Failed`
- Artifact inventory table:
  - role
  - path
  - status
  - size
  - customer-ready yes/no
- Failed/skipped gates with user message.
- Technical details section.
- Visual QA links:
  - PDF page previews
  - GLB thumbnails
  - video contact sheet
- Known local skips:
  - DWG/ODA

Acceptance criteria:

- A human can read the MD and understand what is usable and what is not.
- It does not require reading raw logs to understand the bundle state.

## 10. Additional QA Preview Artifacts

These are not product deliverables, but they should be generated for verification/debugging:

- `qa/pdf/page-001.png`, `page-002.png`, ...
- `qa/dxf/A-101-preview.png` if DXF rendering tool is available.
- `qa/3d/glb-isometric.png`
- `qa/3d/glb-top.png`
- `qa/3d/usdz-bounds.json`
- `qa/video/contact-sheet.jpg`
- `qa/video/keyframes/frame-0000.jpg`, middle, last.
- `qa/report.json`
- `qa/report.md`

These QA artifacts should not be confused with Sprint 4 outputs. They are internal verification evidence, not customer marketing deliverables.

## 11. Recommended Implementation Order

### Q0 - Stop wrong outputs

- Prevent invalid MP4 from being exposed.
- Prevent hardcoded 5m x 15m labels in project outputs.
- Prevent current project/version mismatch.
- Prevent Sprint 4 outputs from product path.

### Q1 - Dynamic 2D correctness

- Refactor PDF/DXF to use actual project geometry everywhere.
- Add semantic validators for dimensions, layers, sheet inventory, labels.
- Add PDF page render previews.

### Q2 - 3D semantic quality

- Improve GLB scene generation beyond generic boxes.
- Add real openings or credible visual voids.
- Add semantic object metadata and QA thumbnails.
- Ensure FBX/USDZ inherit the improved scene.

### Q3 - Video usefulness

- Add camera preflight.
- Add fallback routes.
- Add contact sheet QA.
- Add storyboard coverage checks.

### Q4 - Product-level QA report

- Produce a product-level JSON/MD quality report summarizing all artifact readiness.
- Register QA summaries in the bundle.
- Surface readiness in Delivery UI.

## 12. Suggested Tests To Add

API tests:

- `test_pdf_uses_project_dimensions_not_golden_dimensions`
- `test_dxf_uses_project_dimensions_not_golden_dimensions`
- `test_pdf_pages_render_nonblank`
- `test_dxf_required_layers_and_entities`
- `test_glb_semantic_counts_match_drawing_project`
- `test_glb_visual_thumbnail_nonblank`
- `test_fbx_import_extents_match_glb`
- `test_usdz_openusd_validation_required_when_usd_core_available`
- `test_invalid_mp4_is_not_registered_as_ready`
- `test_video_contact_sheet_generated`
- `test_product_quality_report_marks_partial_bundle`

Manual tests:

- Open PDF and verify dimensions visually.
- Open DXF in a CAD viewer or ezdxf inspection.
- Load GLB in Viewer.
- Import FBX in Blender.
- Open USDZ with USD tooling or AR viewer when available.
- Play MP4 locally.
- Read gate MD and confirm a non-developer can understand status.

## 13. Output-specific Pass Rules

### PDF pass

- Opens.
- Renders all pages.
- Correct project dimensions.
- Vietnamese text correct.
- No content/title overlap.
- Concept drawing set is understandable.

### DXF pass

- Opens with ezdxf.
- Correct units/layers.
- Correct project extents.
- Required entities present.
- No stale golden labels.

### DWG pass or local skip

- ODA available: converted and audited.
- ODA missing: skipped with explicit reason.

### GLB pass

- glTF validator pass.
- Loads in Viewer.
- Bounds and semantic counts match project.
- Visual QA thumbnails nonblank.

### FBX pass

- Imports in Blender.
- Scale/orientation/materials acceptable.
- Extents match GLB.

### USDZ pass

- Opens with USD tooling.
- Size/material/texture gates pass.
- Scale/origin AR-friendly.

### MP4 pass

- ffprobe/decoder pass.
- 3840x2160, 30fps, 60s unless product config changes.
- Non-black frames.
- No camera collision.
- Contact sheet useful.

### Gate JSON/MD pass

- Machine-readable and human-readable.
- Contains artifact status.
- Clear failed/skipped reasons.
- UI can use it without parsing raw logs.

## 14. How To Report Quality

The final remediation report should not only say "file exists". It must include:

- Artifact path.
- Byte size.
- Open/validator result.
- Semantic correctness result.
- Visual QA result.
- Customer readiness:
  - `ready`
  - `partial`
  - `failed`
  - `skipped`
- Known limitation.
- Smallest next fix if not ready.

Example:

```text
PDF:
- path: .../2d/bundle.pdf
- status: partial
- format: pass
- semantic: fail, dimensions still show 5m x 15m on A-100
- visual: pass, all pages render nonblank
- next fix: remove hardcoded site dimensions in pdf_generator._draw_site and _draw_dimensions
```

## 15. Key Code Areas

Likely files to modify:

- `app/services/professional_deliverables/pdf_generator.py`
- `app/services/professional_deliverables/dxf_exporter.py`
- `app/services/professional_deliverables/drawing_contract.py`
- `app/services/professional_deliverables/geometry_adapter.py`
- `app/services/professional_deliverables/scene_builder.py`
- `app/services/professional_deliverables/gltf_authoring.py`
- `app/services/professional_deliverables/fbx_exporter.py`
- `app/services/professional_deliverables/usdz_converter.py`
- `app/services/professional_deliverables/usdz_validators.py`
- `app/services/professional_deliverables/camera_path.py`
- `app/services/professional_deliverables/video_renderer.py`
- `app/services/professional_deliverables/video_validators.py`
- `app/services/professional_deliverables/validators.py`
- `app/tasks/professional_deliverables.py`
- `tests/professional_deliverables/`

Do not make quality improvements by weakening gates. Improve generators and add stronger gates.

---
title: Current Professional Deliverables Artifact Generation Order and Inputs
phase: 2
status: current-code-analysis
date: 2026-04-28
owner: Codex Coordinator
related_files:
  - 12-remediation-agent-prompt.md
  - 13-output-quality-remediation-plan.md
  - 14-artifact-input-process-quality-contract.md
---

# Current Professional Deliverables Artifact Generation Order and Inputs

This document describes the artifact generation pipeline that exists in the current API codebase. It answers:

- Which files are generated.
- In what order they are generated.
- What input each generator currently receives.
- What input is missing for high-quality outputs.

Primary code paths inspected:

- `app/tasks/professional_deliverables.py`
- `app/services/professional_deliverables/geometry_adapter.py`
- `app/services/professional_deliverables/demo.py`
- `app/services/professional_deliverables/sprint2_demo.py`
- `app/services/professional_deliverables/sprint3_demo.py`
- `app/services/professional_deliverables/sheet_assembler.py`
- `app/services/professional_deliverables/orchestrator.py`

## 1. Current Top-level Job Order

The async Celery task is:

`professional_deliverables.run_project_bundle`

Entrypoint:

`app/tasks/professional_deliverables.py::run_professional_deliverable_bundle_task(job_id)`

Current order:

```text
1. Load job, bundle, DesignVersion, Project from DB
2. Create output root:
   storage/professional-deliverables/projects/{project_id}/versions/{version_id}/
3. Remove stale Sprint 4 product outputs if present
4. Stage adapter 10%
5. Convert DesignVersion.geometry_json + Project.brief_json -> DrawingProject
6. Stage export_2d 25%
7. Generate Sprint 1 / 2D bundle
8. Register PDF/DXF/DWG skip/Sprint 1 gate summaries as partial assets
9. Stage export_3d 50%
10. Generate Sprint 2 / GLB + FBX + textures + 3D reports
11. Register GLB/FBX as partial assets
12. Stage export_usdz 65%
13. Stage render_video 85%
14. Generate Sprint 3 / internally regenerates Sprint 2, then USDZ + MP4 + Sprint 3 gates
15. Validate master_4k.mp4 boundary
16. Register USDZ, MP4 if valid, Sprint 3 gate summaries as partial assets
17. Stage validate 95%
18. Validate required product outputs and gates
19. Mark registered partial assets ready if validation passes
20. Mark job ready 100%
```

Important current behavior:

- Sprint 3 currently calls `generate_project_3d_bundle(...)` internally, so the 3D bundle is generated twice for the same `project_dir`.
- The task marks `export_usdz` before calling Sprint 3, but actual USDZ generation happens inside Sprint 3 after stage `render_video` is already set.
- Sprint 4 product outputs are no longer part of the current task path, and stale Sprint 4 files are removed at task start.

## 2. Common Source Input

Every artifact starts from the same DB state:

```text
job_id
  -> ProfessionalDeliverableJob
  -> ProfessionalDeliverableBundle
  -> Project
  -> DesignVersion
```

Main source fields:

- `Project.id`
- `Project.name`
- `Project.brief_json`
- `DesignVersion.id`
- `DesignVersion.geometry_json`

Then:

```text
geometry_to_drawing_project(
  project_id=Project.id,
  project_name=Project.name,
  brief_json=Project.brief_json,
  geometry_json=DesignVersion.geometry_json
)
```

The current adapter requires:

- `geometry_json["$schema"] == ai-architect-geometry-v2`
- floor `levels`
- `site.boundary`
- `rooms`
- `walls`
- `openings`
- `fixtures`
- `roof`

The adapter returns a `DrawingProject`.

## 3. Current DrawingProject Input Shape

Current `DrawingProject` contains:

- `project_id`
- `project_name`
- `lot_width_m`
- `lot_depth_m`
- `storeys`
- `style`
- `issue_date`
- `rooms`
- `walls`
- `openings`
- `fixtures`
- `roof_outline`
- `north_angle_degrees`

Current `Room` contains:

- `id`
- `floor`
- `name`
- `polygon`

Current `WallSegment` contains:

- `floor`
- `start`
- `end`
- `layer`

Current `Opening` contains:

- `floor`
- `kind`
- `start`
- `end`
- `label`

Current `Fixture` contains:

- `floor`
- `kind`
- `center`
- `size`
- `label`

Important dropped data:

- room `area_m2`
- room `perimeter_m`
- finishes
- grid axes
- dimension chains
- wall thickness/height/structural metadata beyond layer
- opening width/height/sill/swing/panel/frame metadata after span conversion
- setbacks/access points/utilities/landscape zones
- floor elevations/clear heights
- stair geometry
- facade/elevation model
- section cut model

This is the main reason technically valid files can still look poor or arbitrary.

## 4. Sheet Set Order

`assemble_sheet_set(project)` creates sheets in this order:

```text
1. A-100-site
2. A-101-F{floor}-floorplan for each floor
3. A-201-elevations
4. A-301-sections
```

For a 3-storey project, expected 2D sheets are:

```text
2d/A-100-site.dxf
2d/A-101-F1-floorplan.dxf
2d/A-101-F2-floorplan.dxf
2d/A-101-F3-floorplan.dxf
2d/A-201-elevations.dxf
2d/A-301-sections.dxf
2d/bundle.pdf
2d/sprint1_gate_summary.json
2d/sprint1_gate_summary.md
```

DWG files are only created if ODA conversion is available or required.

## 5. Artifact-by-artifact Order And Inputs

## 5.1 PDF Bundle

Output:

- `2d/bundle.pdf`

Current generator:

- `write_pdf_bundle(project, sheets, two_d_dir / "bundle.pdf")`

Current input:

- `DrawingProject`
- `SheetSpec` tuple from `assemble_sheet_set`

Current generation order:

```text
1. Register BeVietnamPro fonts
2. Create A3 landscape ReportLab canvas
3. For each SheetSpec:
   3.1 Draw title block
   3.2 Draw page heading
   3.3 If site: draw site
   3.4 If floorplan: draw floorplan
   3.5 If elevations: draw elevations
   3.6 If sections: draw sections
   3.7 showPage()
4. save()
```

Current validators:

- Vietnamese diacritics
- font embedding
- 1:100 scale calibration segment
- max file size

Current missing input for quality:

- room area labels
- dimension chains
- wall thickness/polygons
- openings with height/sill/swing
- grids
- setbacks/access points
- actual elevation projection model
- section cut definition
- layout constraints/no-overlap model
- visual QA previews

Known current defect:

- PDF/DXF drawing code still has hardcoded `5.00 m`, `15.00 m`, and `Ranh đất 5 m x 15 m` paths in drawing functions.

## 5.2 DXF Sheets

Outputs:

- `2d/A-100-site.dxf`
- `2d/A-101-F{floor}-floorplan.dxf`
- `2d/A-201-elevations.dxf`
- `2d/A-301-sections.dxf`

Current generator:

- `write_dxf_sheets(project, sheets, two_d_dir)`

Current input:

- `DrawingProject`
- `SheetSpec` tuple

Current generation order:

```text
For each SheetSpec:
1. Create ezdxf R2018 document
2. Set INSUNITS to meters
3. Apply AIA layer dictionary
4. Draw sheet content by kind:
   - site
   - floorplan
   - elevations
   - sections
5. Draw title note
6. Save DXF
```

Current validators:

- DXF can be opened by ezdxf
- AIA layer dictionary and entity layer validation

Current missing input for quality:

- CAD dimension entity model
- blocks for doors/windows/fixtures/north arrow
- wall polygon/thickness model
- paper/layout viewport model
- grid axes
- elevation/section derived geometry
- semantic extents checks

Known current defect:

- Site/dimensions in DXF also have hardcoded 5m/15m logic in drawing helpers.

## 5.3 DWG

Outputs:

- `2d/*.dwg`, if ODA conversion succeeds.
- Otherwise a skipped `dwg` artifact row is registered.

Current generator:

- `convert_dxf_directory_to_dwg(temp_input_dir, temp_dir, require_binary=require_dwg)`

Current input:

- DXF files copied to a temporary directory.
- ODA converter binary availability.
- Expected DXF stems from `SheetSpec`.

Current generation order:

```text
1. Copy generated DXF files into temp input dir as .DXF
2. Run ODA DXF -> DWG conversion
3. Copy converted DWGs back to 2d/
4. Validate/audit DWG clean open when possible
5. If ODA missing and require_dwg=False, register DWG as skipped
```

Current validators:

- DWG clean-open via ODA audit when available.
- Otherwise skipped with ODA unavailable reason.

Current missing input for quality:

- None independent from DXF. DWG quality depends on DXF quality.
- Needs conversion profile and roundtrip layer/unit checks when ODA exists.

## 5.4 Sprint 1 Gate Summary JSON/MD

Outputs:

- `2d/sprint1_gate_summary.json`
- `2d/sprint1_gate_summary.md`

Current generator:

- `write_gate_outputs(two_d_dir, gate_results, inventory)`

Current input:

- Sprint 1 gate results.
- File inventory for DXF, DWG, PDF.

Current generation order:

```text
1. Collect Sprint 1 gates
2. Build file inventory with size and sha256
3. Write JSON payload:
   - status
   - gates
   - file_inventory
4. Write Markdown table
```

Current missing input for quality:

- semantic drawing quality results
- visual QA page previews
- artifact-level readiness
- customer-facing messages separate from technical details

## 5.5 GLB

Output:

- `3d/model.glb`

Current generator:

- `generate_project_3d_bundle(...)`
- internally:
  - `build_scene_from_project(project)`
  - `write_source_textures(...)`
  - `write_source_gltf(...)`
  - `encode_material_textures(...)`
  - `write_geometry_glb(...)`
  - `export_glb_with_gltf_transform(...)`
  - `embed_ktx_textures_in_glb(...)`

Current input:

- `DrawingProject`
- derived `SceneContract`
- material registry
- generated source textures
- KTX2 encoder
- glTF Transform tool

Current generation order:

```text
1. Build SceneContract from DrawingProject
2. Clean/create 3d/ and textures/
3. Author source PNG textures
4. Write source glTF
5. Encode KTX2 textures
6. Write source geometry GLB
7. Run glTF Transform Draco compression
8. Embed KTX textures into final model.glb
```

Current validators:

- glTF Validator
- material workflow
- metallic/roughness packing
- texture resolution policy

Current missing input for quality:

- room floor surfaces with metadata
- real wall solids with opening voids
- stairs/vertical circulation geometry
- facade/roof details
- semantic object hierarchy tied to source geometry
- visual QA thumbnails

## 5.6 FBX

Output:

- `3d/model.fbx`

Current generator:

- `export_fbx(scene, authored, fbx_path, require_binary=require_external_tools)`

Current input:

- Same `SceneContract` as GLB.
- Authored source textures.
- Blender exporter.

Current generation order:

```text
1. Use SceneContract
2. Use authored textures
3. Run Blender FBX export script
4. Write model.fbx
5. Validate Blender import
```

Current validators:

- Blender import report
- mesh/material/extents/UV checks

Current missing input for quality:

- same missing semantic geometry as GLB
- export hierarchy/profile for downstream tools
- stronger GLB-vs-FBX extents/material parity checks

## 5.7 Sprint 2 Metadata And Gate Summaries

Outputs:

- `3d/sprint2_model_metadata.json`
- `3d/gltf-validator-report.json`
- `3d/fbx-import-report.json`
- `3d/sprint2_gate_summary.json`
- `3d/sprint2_gate_summary.md`
- `textures/*.ktx2`

Current input:

- `SceneContract`
- KTX/glTF/Blender validation outputs
- file inventory

Current generation order:

```text
1. Write sprint2_model_metadata.json from SceneContract
2. Produce validator reports during gates
3. Build inventory of GLB/FBX/metadata/reports/textures
4. Write sprint2 gate summary JSON/MD
```

Current missing input for quality:

- semantic model quality gates
- visual thumbnails
- per-artifact readiness status

## 5.8 USDZ

Output:

- `3d/model.usdz`
- often also intermediate/report files:
  - `3d/model_lite.usd`
  - `3d/model_lite.usdz`
  - `3d/usdz-*.json`

Current generator:

- `generate_project_ar_video_bundle(...)`
- internally:
  - calls `generate_project_3d_bundle(...)` again
  - `export_usdz_from_glb(scene, sprint2.glb_path, textures_dir, three_d_dir, ...)`

Current input:

- `DrawingProject`
- regenerated `SceneContract`
- `3d/model.glb`
- KTX2 textures
- KTX tool
- USD/Blender tooling inside converter path

Current generation order:

```text
1. Regenerate Sprint 2 GLB/FBX/textures
2. Build SceneContract again
3. Discover KTX tool
4. Export USDZ from GLB and textures
5. Validate USDZ budget, structure, material parity, texture payload
```

Current validators:

- USDZ size budget
- USDZ structural integrity
- USDZ material parity
- USDZ texture payload

Current missing input for quality:

- AR origin/ground-plane config
- AR scale validation
- semantic geometry quality inherited from GLB
- Quick Look/AR preview metadata if desired

## 5.9 Master MP4

Output:

- `video/master_4k.mp4`

Current generator:

- `render_master_video(glb_path, scene, camera_path, video_dir, work_dir, ...)`

Current input:

- `3d/model.glb`
- `SceneContract`
- `CameraPath` from `build_camera_path(scene)`
- Blender render script
- ffmpeg
- render profile:
  - 3840x2160
  - 30 fps
  - 60 seconds
  - H.264

Current generation order:

```text
1. Build camera path from SceneContract
2. Check camera collision warnings
3. Write video/camera_path.json
4. Convert GLB to Blender-readable preview GLB
5. Run Blender script to render still frames
6. Write video/render_stills_report.json
7. Run ffmpeg to encode stills into video/master_4k.mp4
8. Render a second video in temp dir for determinism check
9. Validate video format, integrity, determinism
```

Current validators:

- camera collision sanity
- ffprobe master video format
- ffmpeg decode/video integrity
- camera path determinism

Current missing input for quality:

- storyboard model
- room importance ranking
- safe camera zones
- shot list
- lighting profile
- contact sheet/keyframe QA
- visual usefulness checks beyond non-black/deterministic

## 5.10 Sprint 3 Gate Summary JSON/MD

Outputs:

- `sprint3_gate_summary.json`
- `sprint3_gate_summary.md`

Current input:

- Sprint 3 gates:
  - camera collision
  - USDZ gates
  - video gates
- inventory paths:
  - GLB
  - FBX
  - USDZ
  - USDZ reports
  - MP4
  - camera path
  - video reports

Current generation order:

```text
1. Run USDZ validators
2. Run MP4 validators
3. Build inventory
4. Write Sprint 3 gate summary JSON/MD at project root
```

Current missing input for quality:

- per-artifact customer readiness
- visual QA previews/contact sheet
- semantic GLB/USDZ/video usefulness status

## 6. Actual File Dependency Graph

Current dependency graph:

```text
Project + DesignVersion.geometry_json
  -> DrawingProject

DrawingProject
  -> SheetSpec[]
  -> DXF sheets
  -> DWG conversion/skip
  -> PDF bundle
  -> Sprint 1 gate summary

DrawingProject
  -> SceneContract
  -> source textures
  -> KTX2 textures
  -> source GLB
  -> Draco/KTX final GLB
  -> FBX
  -> Sprint 2 metadata/reports/gate summary

DrawingProject
  -> Sprint 3 calls Sprint 2 again
  -> regenerated GLB/FBX/textures
  -> USDZ
  -> CameraPath
  -> Blender stills
  -> MP4 via ffmpeg
  -> Sprint 3 reports/gate summary

All valid or partial artifacts
  -> ProfessionalDeliverableAsset rows
  -> Delivery/Review API response
```

## 7. Current Generated File Types

Phase 2 product-required artifacts:

- PDF: `2d/bundle.pdf`
- DXF: `2d/*.dxf`
- DWG: `2d/*.dwg` or skipped artifact
- GLB: `3d/model.glb`
- FBX: `3d/model.fbx`
- USDZ: `3d/model.usdz`
- MP4: `video/master_4k.mp4`
- Gate JSON: `2d/sprint1_gate_summary.json`, `3d/sprint2_gate_summary.json`, `sprint3_gate_summary.json`
- Gate MD: `2d/sprint1_gate_summary.md`, `3d/sprint2_gate_summary.md`, `sprint3_gate_summary.md`

Intermediate/support artifacts:

- `textures/*.ktx2`
- `3d/sprint2_model_metadata.json`
- `3d/gltf-validator-report.json`
- `3d/fbx-import-report.json`
- `3d/usdz-*.json`
- `3d/model_lite.usd`
- `3d/model_lite.usdz`
- `video/camera_path.json`
- `video/render_stills_report.json`
- `video/ffprobe-master-report.json`
- `video/video-integrity-report.json`
- `video/video-determinism-report.json`

Forbidden in Phase 2 product path:

- final `manifest.json`
- Sprint 4 gate summaries
- reel/social video
- hero still
- preview GIF

## 8. Main Pipeline Gaps

The current pipeline can produce files in the right broad order, but the input model is too thin for high-quality artifacts.

Largest gaps:

1. `DrawingProject` drops many useful fields from `geometry_json`.
2. PDF/DXF exporters still include hardcoded golden dimensions in drawing helpers.
3. Sprint 3 regenerates Sprint 2 instead of reusing the Sprint 2 result from the task.
4. Stage `export_usdz` is not aligned with actual USDZ generation timing.
5. 3D scene generation uses simplified box primitives.
6. Gate summaries do not yet express artifact-level customer readiness.
7. Visual QA artifacts are not part of the current output flow.

## 9. What Better Input Should Feed The Existing File Types

To make current file types usable, the shared input should evolve from `DrawingProject` to a richer normalized model containing:

- project/version metadata
- full site model
- level model with heights/elevations
- room model with area/perimeter/finish/category
- wall model with thickness/height/exterior/interior
- opening model with width/height/sill/swing/frame
- fixture/furniture model with type/rotation/symbol
- roof/envelope model
- grid/dimension model
- material/style model
- drawing layout constraints
- scene/camera/storyboard constraints

This richer model should then feed artifact-specific models:

- PDF/DXF: drawing sheet model + layout model
- GLB/FBX/USDZ: semantic scene model
- MP4: storyboard + camera-safe path model
- Gate summaries: artifact quality report model

## 10. Short Answer

Current generation order:

```text
adapter
-> DXF
-> DWG conversion/skip
-> PDF
-> Sprint 1 gates
-> GLB
-> FBX
-> Sprint 2 gates
-> regenerate GLB/FBX/textures inside Sprint 3
-> USDZ
-> camera_path
-> MP4
-> Sprint 3 gates
-> DB asset registration / ready or failed state
```

Current primary input:

```text
Project.brief_json + DesignVersion.geometry_json
-> geometry_adapter
-> DrawingProject
```

Main problem:

```text
DrawingProject is too thin and exporters draw too directly from it.
The pipeline needs a richer normalized deliverable model plus artifact-specific layout/scene/video models.
```

---
title: Professional Deliverables Artifact Input and Process Quality Contract
phase: 2
status: ready-for-implementation
date: 2026-04-28
owner: Codex Coordinator
related_files:
  - 10-remediation-implementation-contract.md
  - 11-remediation-execution-playbook.md
  - 13-output-quality-remediation-plan.md
source_pdf_url: http://localhost:18000/media/professional-deliverables/projects/3b00f863-3144-4223-b04d-dec825c894d8/versions/b0f39796-d4ba-43f8-92e8-058004ce64d6/2d/bundle.pdf
source_project_id: 3b00f863-3144-4223-b04d-dec825c894d8
source_version_id: b0f39796-d4ba-43f8-92e8-058004ce64d6
---

# Professional Deliverables Artifact Input and Process Quality Contract

Tài liệu này trả lời câu hỏi: để đầu ra từng loại file không còn "vẽ lung tung", mỗi exporter cần thêm **input gì**, **process gì**, và **quality gates gì**.

Ví dụ kiểm tra thực tế với PDF:

`http://localhost:18000/media/professional-deliverables/projects/3b00f863-3144-4223-b04d-dec825c894d8/versions/b0f39796-d4ba-43f8-92e8-058004ce64d6/2d/bundle.pdf`

Kết quả kiểm tra:

- PDF trả `200 OK`, dung lượng khoảng `43KB`, có 6 trang A3 landscape.
- Text extract cho thấy:
  - A-100 ghi `Ranh đất 5 m x 15 m`
  - các trang mặt bằng ghi `5.00 m`, `15.00 m`
- Trong DB, version V4 geometry/brief có lot `5m x 20m`, `site.boundary` từ `(0,0)` đến `(5,20)`, `orientation_north_deg = 180`, rooms có `area_m2`, openings có width/height/sill/schedule, fixtures, finishes, roof, grids.
- PDF A-201 elevation bị chồng hình, bố cục không đạt mức dùng được.

Kết luận: input thô đang có nhiều dữ liệu tốt hơn output. Lỗi chính là thiếu lớp chuẩn hóa input chuyên cho deliverables và thiếu process dựng bản vẽ/model/video theo chuẩn.

## 1. Nguyên Tắc Chung

Mỗi artifact không được xuất trực tiếp từ `geometry_json` bằng primitive drawing đơn giản. Cần pipeline trung gian:

```text
DesignVersion.geometry_json
  -> SourceGeometryModel
  -> NormalizedDeliverableModel
  -> Artifact-specific Sheet/Scene/Video Model
  -> Layout/Camera/Export Plan
  -> Exporter
  -> Technical Validation
  -> Semantic Validation
  -> Visual QA
  -> Customer Readiness State
```

Trong đó:

- `SourceGeometryModel`: dữ liệu gốc đã parse từ system-generated geometry.
- `NormalizedDeliverableModel`: geometry đã chuẩn hóa, có units, levels, walls, openings, rooms, schedules, style/materials, dimensions.
- `Artifact-specific model`: model riêng cho PDF/DXF/3D/video, không dùng chung một model quá nghèo nàn.
- `Visual QA`: render preview/keyframes để kiểm mắt hoặc kiểm pixel.
- `Customer readiness`: `ready`, `partial`, `failed`, `skipped`.

## 2. Minimum Input Contract Cho Mọi Artifact

Trước khi xuất bất kỳ file nào, adapter phải tạo được một `ProfessionalDeliverableSourceModel` hoặc mở rộng `DrawingProject` hiện tại với các nhóm dữ liệu sau.

### Project metadata

Bắt buộc:

- `project_id`
- `version_id`
- `project_name`
- `client_name` nếu có
- `issue_date`
- `revision_label` hoặc version number
- `brief_summary`
- `concept_note`: ví dụ `Bản vẽ khái niệm - không dùng cho thi công`

### Site model

Bắt buộc:

- `site.boundary`: polygon thật, không giả định rectangle 5x15.
- `lot_width_m`
- `lot_depth_m`
- `lot_area_m2`
- `north_angle_degrees`
- `orientation`
- `setbacks`
- `access_points`

Nên có:

- utilities
- landscape zones
- adjacent road/front edge
- buildable envelope

### Level model

Bắt buộc:

- floor id: `L1`, `L2`, ...
- floor number
- finished floor elevation
- floor-to-floor height
- clear height
- slab thickness

### Room model

Bắt buộc:

- `room_id`
- Vietnamese room label
- original room type
- polygon
- area
- perimeter
- floor/level

Nên có:

- finish set
- daylight/ventilation flags
- wet/dry room category
- privacy/public category

### Wall model

Bắt buộc:

- wall id
- level
- start/end or polygon/solid
- thickness
- height
- structural/non-structural category if available
- exterior/interior flag

### Opening model

Bắt buộc:

- opening id / schedule mark
- type: door/window
- wall id
- face/orientation
- position along wall
- width
- height
- sill height
- swing/sliding/fixed operation where available

### Fixture/furniture model

Bắt buộc nếu có trong geometry:

- id
- type
- room id
- position
- dimensions
- rotation if available
- Vietnamese label/icon mapping

### Roof/envelope model

Bắt buộc:

- roof type
- roof outline/footprint
- parapet/terrace info if available
- top elevation

### Grid/dimension model

Bắt buộc cho drawing quality:

- grid axes x/y
- overall dimension chains
- room/internal dimension chains
- opening dimension chains
- elevation vertical dimension chains

Nếu geometry có `dimensions_config`, phải dùng nó thay vì bỏ qua.

### Style/material model

Bắt buộc cho 3D/video:

- material per wall/floor/roof/opening/fixture category
- finish set per room if available
- palette/style direction

## 3. PDF Drawing Bundle

### Vì sao PDF hiện tại chưa dùng được

Với file kiểm tra:

- Lot thật trong input là `5m x 20m`, nhưng PDF ghi `5m x 15m`.
- `pdf_generator._draw_dimensions()` hardcode `5.00 m` và `15.00 m`.
- `pdf_generator._draw_site()` hardcode site boundary và text `Ranh đất 5 m x 15 m`.
- Elevation sheet vẽ generic rectangles, không layout theo sheet frames nên bị chồng.
- Rooms thiếu diện tích, thiếu dimension chains, thiếu legend, thiếu door/window schedule.
- Title block ổn ở mức cơ bản nhưng sheet content chưa đạt concept drawing.

### PDF cần thêm input gì

Ngoài `DrawingProject` hiện tại, PDF cần thêm:

- `sheet_set`: danh sách sheet cần xuất, title, number, scale, viewport intent.
- `drawing_units`: meters, mm paper scale.
- `site_plan_model`:
  - lot boundary polygon
  - building footprint
  - setback lines
  - access points
  - north angle
  - landscape zones
- `floor_plan_model` cho từng floor:
  - wall polygons/thickness, không chỉ wall centerline
  - room polygons + area label
  - door/window symbols with swing/operation
  - fixtures/furniture symbols
  - grid axes
  - dimension chains
  - section/elevation callout markers
- `elevation_model`:
  - facade extents per direction
  - floor level lines
  - openings projected by facade
  - roof/parapet lines
  - material/finish indication
- `section_model`:
  - cut line source
  - cut direction
  - floor/roof/slab heights
  - stair/void if available
- `annotation_model`:
  - title labels
  - room labels
  - area labels
  - dimensions
  - warnings/notes
- `layout_constraints`:
  - page size
  - margins
  - title block box
  - viewport boxes
  - min text size
  - no-overlap rules

### PDF process phải thêm gì

Thay vì vẽ trực tiếp trong `pdf_generator.py`, cần process:

1. **Normalize geometry**
   - Parse `site.boundary`, `rooms`, `walls`, `openings`, `fixtures`, `grids`, `roof`, `dimensions_config`.
   - Fail nếu thiếu critical geometry, không fallback golden.

2. **Build drawing sheet models**
   - `SiteSheetModel`
   - `FloorPlanSheetModel`
   - `ElevationSheetModel`
   - `SectionSheetModel`
   - mỗi sheet có `viewport`, `scale`, `entities`, `annotations`.

3. **Compute scales and viewports**
   - Không hardcode 1:100 nếu không fit.
   - Nếu 1:100 không fit, chọn 1:150/1:200 và ghi rõ.
   - Tất cả drawing content phải nằm trong content frame, không đè title block.

4. **Generate annotation placement**
   - Room label đặt trong polygon.
   - Area label dòng dưới room name.
   - Nếu phòng quá hẹp, dùng leader/callout.
   - Dimensions đặt ngoài lot/building bounds.

5. **Draw with layer/style system**
   - wall: lineweight đậm
   - room boundary: nhẹ
   - dimension: đỏ hoặc chuẩn annotation
   - opening: door/window symbol rõ
   - furniture/fixture: symbol đơn giản nhưng đúng loại

6. **Render visual QA**
   - Render từng page thành PNG.
   - Lưu vào `qa/pdf/page-001.png`, ...
   - Tạo `qa/pdf/report.json`.

7. **Semantic QA**
   - Extract text từ PDF.
   - Assert không có stale dimensions.
   - Assert expected dimensions xuất hiện.
   - Assert sheet count đúng.

### PDF quality gates cần thêm

- `PDF_PAGE_COUNT`: đúng sheet count.
- `PDF_DYNAMIC_DIMENSIONS`: text không chứa hardcoded golden dimensions với non-golden project.
- `PDF_SITE_BOUNDARY_MATCH`: site drawing bounds match `site.boundary`.
- `PDF_FLOOR_COUNT`: có sheet cho từng floor.
- `PDF_ROOM_LABELS`: mỗi room có label tiếng Việt.
- `PDF_ROOM_AREAS`: mỗi room có diện tích.
- `PDF_DIMENSION_CHAINS`: có overall dimension width/depth.
- `PDF_NO_TITLE_OVERLAP`: drawing không đè title block.
- `PDF_PAGE_RENDER_NONBLANK`: mọi page render được và nonblank.
- `PDF_ELEVATION_LAYOUT`: elevation frames không overlap.

### PDF pass criteria

PDF chỉ `ready` nếu:

- Mọi page render được.
- Lot dimensions đúng theo project.
- Không còn `5m x 15m` stale nếu input không phải 5x15.
- Floor plans có room names + area + openings + dimensions.
- Elevation/section không overlap và không chỉ là generic rectangles vô nghĩa.

## 4. DXF Sheets

### DXF cần thêm input gì

DXF cần cùng drawing model với PDF nhưng giàu CAD hơn:

- exact units and scale
- layers with colors/lineweights
- block definitions:
  - door
  - window
  - toilet
  - sink
  - stair
  - furniture placeholder
  - north arrow
- CAD dimension chain model:
  - overall
  - grid
  - opening
  - room/internal
- title block model
- optional paperspace/layout viewport model

### DXF process phải thêm gì

1. Build CAD entity graph, không vẽ rời rạc trong exporter.
2. Generate layers from AIA-like layer dictionary.
3. Generate blocks once, insert block references.
4. Use real CAD dimension entities where feasible.
5. Add model extents check.
6. Add optional paperspace layouts.
7. Run `ezdxf.readfile()` open check.
8. Run semantic entity count check.

### DXF gates

- `DXF_OPENABLE`
- `DXF_UNITS_METERS`
- `DXF_REQUIRED_LAYERS`
- `DXF_PROJECT_EXTENTS_MATCH`
- `DXF_DIMENSIONS_MATCH`
- `DXF_ROOM_LABELS`
- `DXF_OPENING_SYMBOLS`
- `DXF_NO_STALE_GOLDEN_LABELS`

## 5. DWG

### DWG cần thêm input gì

DWG không cần input mới riêng; nó phụ thuộc DXF. Cần thêm:

- ODA tool availability
- conversion profile
- expected sheet list

### DWG process phải thêm gì

1. Convert every DXF to DWG if ODA exists.
2. Audit open/roundtrip.
3. Compare count and file names with DXF.
4. If ODA missing, register artifact state `skipped`, not silent missing.

### DWG gates

- `DWG_ODA_AVAILABLE_OR_SKIPPED`
- `DWG_FILE_COUNT_MATCH`
- `DWG_AUDIT_OPEN`
- `DWG_ROUNDTRIP_LAYERS`

## 6. GLB Model

### GLB hiện chưa đủ dùng vì sao

Current `scene_builder.py` tạo chủ yếu:

- site ground box
- slab boxes
- wall boxes
- opening boxes đặt lên wall, không cut void
- fixture boxes
- roof box

Nó có thể pass glTF validator nhưng vẫn không phải model kiến trúc đủ rõ.

### GLB cần thêm input gì

- wall solids with thickness and opening voids
- opening schedules with exact width/height/sill
- room floor surfaces
- stair/vertical circulation geometry
- roof/parapet/terrace geometry
- facade material assignments
- room/element metadata
- style/material palette
- furniture/fixture primitive library by type

### GLB process phải thêm gì

1. Build semantic scene model from normalized geometry.
2. Generate real wall solids.
3. Apply opening subtraction or create segmented wall pieces around openings.
4. Generate room floor meshes and optional ceiling/slab.
5. Generate basic stairs if geometry includes circulation/stair.
6. Apply material mapping from finishes.
7. Add metadata extras to nodes.
8. Generate QA renders:
   - isometric
   - top
   - front
9. Validate semantic counts and bounds.

### GLB gates

- `GLB_VALIDATOR_PASS`
- `GLB_BOUNDS_MATCH_SITE`
- `GLB_FLOOR_COUNT_MATCH`
- `GLB_ROOM_SURFACES_PRESENT`
- `GLB_WALL_OPENINGS_PRESENT`
- `GLB_MATERIALS_ASSIGNED`
- `GLB_VIEWER_LOAD_SMOKE`
- `GLB_QA_THUMBNAILS_NONBLANK`

## 7. FBX Model

### FBX cần thêm input gì

FBX dùng cùng semantic scene model với GLB, thêm:

- export axis profile
- unit scale profile
- material bake/mapping profile
- object hierarchy profile

### FBX process phải thêm gì

1. Export from same semantic scene source as GLB.
2. Import back into Blender.
3. Check object counts, material counts, extents.
4. Compare extents with GLB.
5. Verify no extreme scaling.

### FBX gates

- `FBX_BLENDER_IMPORT`
- `FBX_EXTENTS_MATCH_GLB`
- `FBX_UNITS_SCALE_VALID`
- `FBX_MATERIALS_PRESENT`
- `FBX_OBJECT_NAMES_SEMANTIC`

## 8. USDZ AR Package

### USDZ cần thêm input gì

USDZ dùng semantic scene model + material model, thêm:

- AR scale/origin config
- texture budget
- package metadata
- USD Preview Surface material mapping

### USDZ process phải thêm gì

1. Convert from GLB/USD with stable material mapping.
2. Validate with `usd-core==26.5`.
3. Check package size and textures.
4. Check origin/ground plane.
5. Verify GLB/USDZ material parity.

### USDZ gates

- `USDZ_STAGE_OPEN`
- `USDZ_COMPLIANCE`
- `USDZ_SIZE_BUDGET`
- `USDZ_TEXTURE_BUDGET`
- `USDZ_MATERIAL_PARITY`
- `USDZ_AR_ORIGIN_VALID`

## 9. Master 4K MP4

### MP4 cần thêm input gì

Video không nên chỉ nhận GLB + camera path. Cần:

- storyboard intent:
  - exterior establish
  - floor/room overview
  - important rooms
  - ending overview
- camera-safe zones
- room importance ranking
- collision geometry
- target points per room
- lighting profile
- render quality profile
- fallback camera path profile

### MP4 process phải thêm gì

1. Build storyboard from project type and rooms.
2. Generate camera path candidates.
3. Run preflight collision checks before render.
4. Pick safe path or fallback.
5. Render stills/video.
6. Immediately ffprobe master MP4.
7. Decode check.
8. Generate contact sheet and keyframes.
9. Run visual QA:
   - non-black
   - no collision
   - framed subject
   - duration/fps/size

### MP4 gates

- `VIDEO_CAMERA_PREFLIGHT`
- `VIDEO_RENDER_COMPLETED`
- `VIDEO_FFPROBE_VALID`
- `VIDEO_DECODE_CLEAN`
- `VIDEO_NONBLACK_KEYFRAMES`
- `VIDEO_CAMERA_COLLISION_FREE`
- `VIDEO_CONTACT_SHEET_GENERATED`

## 10. Gate Summary JSON/MD

### Gate summary cần thêm input gì

- artifact inventory
- artifact role definitions
- readiness states
- semantic validator results
- visual QA artifact paths
- user-facing messages
- technical details

### Gate summary process phải thêm gì

1. Collect all artifact validators.
2. Normalize gate result codes.
3. Compute artifact readiness.
4. Compute bundle readiness.
5. Write machine-readable JSON.
6. Write human-readable MD.
7. Register both as artifacts.
8. Delivery UI reads state from API, not raw log strings.

### Gate summary gates

- `QA_JSON_SCHEMA_VALID`
- `QA_MD_HUMAN_READABLE`
- `QA_ARTIFACT_INVENTORY_COMPLETE`
- `QA_FAILED_GATES_ACTIONABLE`

## 11. New Process Architecture Required

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

Existing exporters should become consumers of prepared models:

```text
geometry_adapter.py
  -> deliverable_normalizer.py
  -> drawing_sheet_model.py
  -> pdf_generator.py
  -> dxf_exporter.py
  -> drawing_quality_gates.py
```

```text
geometry_adapter.py
  -> deliverable_normalizer.py
  -> scene_builder.py
  -> gltf/fbx/usdz exporters
  -> scene_quality_gates.py
```

```text
scene_builder.py + storyboard model
  -> camera_path.py
  -> video_renderer.py
  -> video_quality_gates.py
```

## 12. Implementation Priority

### P0 - Stop objectively wrong drawings

- Remove hardcoded `5m x 15m` from PDF/DXF.
- Use actual `site.boundary`, lot width/depth, and north angle.
- Add tests that fail if non-golden project outputs include stale golden dimensions.

### P1 - Make PDF/DXF concept-usable

- Add dynamic dimension chains.
- Add room area labels.
- Fix elevation layout collision.
- Add PDF page render QA.
- Add DXF entity/layer/extents QA.

### P2 - Make 3D model review-usable

- Segment walls around openings.
- Add room floor surfaces.
- Improve fixture/furniture primitives.
- Add GLB thumbnails and viewer smoke.

### P3 - Make video review-usable

- Add storyboard/camera preflight.
- Add contact sheet.
- Add collision-free fallback path.

### P4 - Make QA customer-readable

- Product-level artifact quality JSON/MD.
- Delivery UI shows artifact readiness based on quality results.

## 13. Tests That Must Exist

At minimum, add tests equivalent to:

```text
test_pdf_uses_actual_lot_dimensions_for_project_geometry
test_pdf_does_not_contain_stale_golden_dimensions
test_pdf_elevation_frames_do_not_overlap
test_dxf_uses_actual_lot_dimensions_for_project_geometry
test_dxf_extents_match_site_boundary
test_glb_semantic_counts_match_source_geometry
test_glb_has_opening_voids_or_segmented_wall_openings
test_usdz_opens_with_usd_core_when_available
test_master_video_invalid_file_is_not_ready
test_video_camera_path_prefight_catches_wall_collision
test_quality_report_contains_artifact_readiness
```

## 14. Definition Of Ready Per Artifact

An artifact is `ready` only if:

- It exists.
- It opens in the expected tool.
- It uses selected version geometry.
- It passes semantic gates.
- It passes visual QA or has a documented non-visual validator.
- It has customer-readable status in the API/UI.

If any of those fail:

- `partial`: artifact exists and is useful for inspection, but not final.
- `failed`: artifact is missing, invalid, misleading, or unsafe to expose.
- `skipped`: artifact intentionally not produced, with approved reason.

Do not mark a file `ready` merely because it exists.

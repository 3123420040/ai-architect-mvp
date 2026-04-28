---
title: PRD — Professional Deliverables (2D / 3D / Video)
phase: 2
status: ready-for-dev
date: 2026-04-27
revision: 2026-04-27 — Local-first verification protocol added; GitHub Actions/PR comments no longer mandatory acceptance transport
authors:
  - PM/Architect Agent (Claude)
  - Product Owner (evo-pm-vn@trustingsocial.com)
related:
  - docs/phase-2/01-discovery-summary.md
  - docs/phase-2/02-market-standards-research.md
  - docs/phase-2/03-adr-001-standards-combo.md
  - docs/phase-2/04-deferred-roadmap.md
  - docs/phase-2/07-local-git-verification-protocol.md
---

# PRD — Professional Deliverables Track

## Overview

AI Architect MVP nâng output từ "concept-stage visual" lên "professional grade theo chuẩn thị trường". Mỗi project tạo ra một bundle có 4 nhóm artifact: **2D drawings, 3D models, Videos, Manifest** — sẵn sàng cho client review, marketing reel, và engineer handoff.

**Stack chuẩn (theo ADR-001):** AIA layer + glTF 2.0 + FBX + USDZ + BIMForum LOD 200-300 + PBR Metal-Roughness + 4K H.264 video.

**Pipeline mode:** Async-first (OQ1). User submit → notification 15-60 phút khi bundle ready.

---

## Output Structure (canonical bundle per project)

```
/project-<id>/
  /2d/
    A-100-site.dwg                (AIA layer dictionary)
    A-101-F1-floorplan.dwg        (ground floor; one sheet per floor for multi-storey)
    A-101-F2-floorplan.dwg        (upper floor — repeat per floor)
    A-201-elevations.dwg          (4 elevations: N/S/E/W on one sheet)
    A-301-sections.dwg            (1 transverse + 1 longitudinal on one sheet)
    bundle.pdf              (full sheet set, NCS title block, VN labels)
  /3d/
    model.glb               (glTF 2.0, Metal-Rough, Draco+KTX2, hero)
    model.fbx               (Twinmotion preset, cm units, Y→Z, embed media)
    model.usdz              (Apple AR Quick Look, ≤8 MB, ≤200k tris)
  /video/
    master_4k.mp4           (60s walkthrough, 3840×2160, 30fps, H.264)
    reel_9x16_1080p.mp4     (20-30s, 1080×1920, derived from master)
  /textures/
    *.ktx2                  (2K default, 4K hero variants, 1K mobile)
  /derivatives/             (free, extracted from master video)
    hero_still_4k.png
    preview.gif             (6-10s loop)
  manifest.json             (LOD tags, material list, metadata, ISO 19650-style ID)
```

---

# PR-2D — Two-Dimensional Drawing Set

## PR-2D.1 Functional Requirements

| ID | Requirement | Type | Priority |
|---|---|---|---|
| F-2D-01 | Generate DWG file per drawing sheet (A-100, A-101, A-201, A-301) | Functional | Must |
| F-2D-02 | Apply AIA CAD Layer Guidelines layer dictionary (~25 layers, see Appendix A) | Functional | Must |
| F-2D-03 | Render PDF presentation set với NCS-style title block | Functional | Must |
| F-2D-04 | All labels in **Vietnamese** by default (OQ5 decision) | Functional | Must |
| F-2D-05 | Include scale, north arrow, dimension lines, room labels, door swings | Functional | Must |
| F-2D-06 | Title block contains: project name, sheet number, scale, date, KTS stamp placeholder | Functional | Must |
| F-2D-07 | Multi-storey buildings → one A-101-FN.dwg per floor (F1 = ground, F2, F3…). Filename pattern: `A-101-F<N>-floorplan.dwg`. | Functional | **Must** |
| F-2D-08 | Open-able and editable in AutoCAD 2020+ and Revit 2022+ without warnings | Non-functional | Must |
| F-2D-09 | Output validation passes Khronos-equivalent for DWG (LibreCAD opens cleanly) | Non-functional | Must |
| F-2D-10 | Generation time ≤ 30 seconds per drawing sheet on standard CPU instance | Non-functional | Should |

## PR-2D.2 Acceptance Criteria

### AC-2D-01 — DWG opens cleanly in AutoCAD with correct layer structure
**Given** a generated `A-101-floorplan.dwg` for a 2-storey 5×15m townhouse
**When** the file is opened in AutoCAD 2024
**Then**
- File opens without "drawing recovery" prompt
- Layer Manager shows ≥15 layers with AIA-compliant names (`A-WALL`, `A-DOOR`, `A-GLAZ`, `A-FURN`, `A-AREA`, `A-ANNO-DIMS`, `A-ANNO-TEXT`, `A-ROOF`, `S-COLS`)
- Each layer has correct color + lineweight per AIA defaults (A-WALL = white/0.50mm, A-ANNO-DIMS = red/0.25mm)
- All entities are on appropriate layers (walls on `A-WALL`, not on `0`)

### AC-2D-02 — PDF presentation looks professional
**Given** the 4-sheet PDF bundle (A-100, A-101, A-201, A-301)
**When** opened in any PDF viewer
**Then**
- Each page has NCS-style title block (project name, sheet number, scale "1:100", date, north arrow on plans)
- Drawings are scaled correctly (measure with PDF ruler tool: 1m drawing = 1cm at 1:100 scale)
- VN labels render correctly (no character mojibake — Vietnamese accents like "ô, ư, đ" display properly)
- Fonts embedded (no font fallback warning)
- File size < 10 MB

### AC-2D-03 — Engineer can pickup file in SketchUp/Revit
**Given** a generated `A-101.dwg`
**When** imported into SketchUp 2025 via "File → Import → DWG"
**Then**
- Layers preserved with correct names
- No geometry corruption (walls remain straight, no broken edges)
- Annotations are editable text (not flattened to lines)
- Engineer can extrude walls in <2 minutes without rebuilding

### AC-2D-04 — Failure case (must reject)
**Given** an incomplete generation (missing roof or partial floor)
**When** export attempted
**Then** generation fails with clear error message; partial DWG is NOT delivered to user.

## PR-2D.3 Out of Scope (Phase 1 MVP)

- ❌ Construction-grade detail drawings (sections at 1:20, large-scale details)
- ❌ Schedule tables (door schedule, window schedule, finish schedule) — Phase 2+
- ❌ Hatching for materials (decorative hatch patterns) — Phase 2+
- ❌ Notes blocks, general notes — Phase 2+
- ❌ Multi-language (EN labels) — DEF in Discovery OQ5

---

# PR-3D — Three-Dimensional Model Set

## PR-3D.1 Functional Requirements

| ID | Requirement | Type | Priority |
|---|---|---|---|
| F-3D-01 | Generate `model.glb` (glTF 2.0, Metal-Rough, Draco mesh + KTX2 textures) | Functional | Must |
| F-3D-02 | Generate `model.fbx` with Twinmotion preset (cm units, Y→Z axis convert, embed media) | Functional | Must |
| F-3D-03 | Generate `model.usdz` for iOS AR Quick Look | Functional | Must |
| F-3D-04 | Tag each scene element with BIMForum LOD level (100/200/300) | Functional | Must |
| F-3D-05 | All materials use PBR Metal-Roughness workflow only | Functional | Must |
| F-3D-06 | Texture maps: BaseColor (sRGB), MetallicRoughness packed (G=rough, B=metal, linear), Normal (OpenGL +Y), AO, Emissive | Functional | Must |
| F-3D-07 | Default texture resolution 2K; auto-promote to 4K for surfaces > X m² in hero shots; auto-demote to 1K for USDZ | Functional | Must |
| F-3D-08 | USDZ enforced budget: ≤ 8 MB file, ≤ 200k triangles, ≤ 2K textures, 1 unit = 1 meter, pivot at floor center | Non-functional | Must |
| F-3D-09 | GLB file passes Khronos glTF Validator with no errors (warnings acceptable) | Non-functional | Must |
| F-3D-10 | FBX imports into Twinmotion 2024.1 + Lumion 2024 + 3ds Max + SketchUp 2025 without manual fixes | Non-functional | Must |
| F-3D-11 | All file sizes optimized (GLB < 50 MB hero; FBX < 100 MB; USDZ < 8 MB) | Non-functional | Should |

## PR-3D.2 Acceptance Criteria

### AC-3D-01 — GLB passes Khronos validator + renders in three.js
**Given** a generated `model.glb` for a 2-storey townhouse (LOD 300 walls, LOD 200 furniture)
**When** validated against `gltf-validator`
**Then**
- 0 errors, < 5 warnings (warnings only acceptable for unused vertex attributes)
- Validates as glTF 2.0 spec
- Loads in three.js via `GLTFLoader` without console errors
- Materials render Metal-Roughness correctly (test in https://gltf-viewer.donmccurdy.com)

### AC-3D-02 — FBX imports cleanly into Twinmotion
**Given** a generated `model.fbx` with Twinmotion preset
**When** drag-dropped into Twinmotion 2024.1
**Then**
- Import dialog shows "0 errors, 0 warnings"
- Geometry appears at correct scale (1 wall = 3m height, not 30cm or 300cm)
- Up axis correct (no model lying on its side)
- Materials assigned (no missing texture warnings)
- Lighting/sun study works (no degenerate normals causing flicker)

### AC-3D-03 — USDZ launches AR Quick Look on iPhone
**Given** a generated `model.usdz`
**When** opened on iPhone via Safari + AR Quick Look
**Then**
- Loads in < 3 seconds on 5G
- Model appears at scale 1:1 in AR (verified by placing virtual model next to a real-world meter stick)
- No invisible polygons (back-face culling correct)
- Materials render PBR (metallic surfaces reflect environment)
- Tap-and-drag rotates smoothly (60fps)

### AC-3D-04 — LOD tagging in manifest is correct
**Given** generated bundle's `manifest.json`
**When** parsed
**Then**
- Each top-level scene element has `lod` key (100, 200, or 300)
- Walls, columns, openings (doors/windows) tagged LOD 300
- Furniture, fixtures tagged LOD 200
- Site context (terrain, neighboring outline) tagged LOD 100-200
- Total element count matches scene graph node count

### AC-3D-05 — PBR materials are Metal-Rough only
**Given** any material in the model
**When** inspected via glTF Validator + visual check
**Then**
- All materials use `pbrMetallicRoughness` extension
- ZERO materials use `KHR_materials_pbrSpecularGlossiness` (rejected per ADR-001)
- MetallicRoughness texture is correctly packed: B=metallic (linear), G=roughness (linear), R unused
- BaseColor is sRGB-encoded

### AC-3D-06 — Failure case
**Given** a model with degenerate geometry (zero-area faces, NaN vertices, broken normals)
**When** export pipeline runs
**Then** export fails the required verification gate; bundle is NOT delivered.

## PR-3D.3 Out of Scope (Phase 1 MVP)

- ❌ IFC export (DEF-002, defer Phase 2+)
- ❌ NURBS/parametric geometry preservation
- ❌ Animation rigs (only static models)
- ❌ Procedural material generation (DEF-006, via ROOM project)
- ❌ Multi-LOD streaming (single LOD per element)

---

# PR-VID — Video Deliverables

## PR-VID.1 Functional Requirements

| ID | Requirement | Type | Priority |
|---|---|---|---|
| F-VID-01 | Generate **1 master walkthrough**: 60 seconds, 3840×2160 (4K), 16:9, 30fps, H.264 MP4 | Functional | Must |
| F-VID-02 | Auto-derive **1 marketing reel**: 20-30 seconds, 1080×1920 (9:16), 30fps, H.264 MP4, 10-15 Mbps | Functional | Must |
| F-VID-03 | Reel uses safe-area cropping from master 16:9 (no re-rendering) | Functional | Must |
| F-VID-04 | Master shows: exterior approach (10-15s) → interior key rooms walkthrough (35-40s) → exterior closing (5-10s) | Functional | Must |
| F-VID-05 | Render via Twinmotion 2024.1 OR Lumion 2024 (5-Star quality, RT 256 samples interior, rasterization exterior) | Functional | Must |
| F-VID-06 | Color grading ACES preferred, Rec.709 sRGB acceptable | Functional | Should |
| F-VID-07 | Audio: ambient soundtrack + soft sound design (royalty-free CC0 library) | Functional | Should |
| F-VID-08 | Auto-extract derivatives: 1 hero still 4K (best frame) + 1 GIF preview (6-10s loop) | Functional | Should |
| F-VID-09 | Render time ≤ 30 minutes per project on RTX 4090-equivalent GPU | Non-functional | Should |
| F-VID-10 | Master file size ≤ 200 MB; reel ≤ 30 MB | Non-functional | Should |

## PR-VID.2 Acceptance Criteria

### AC-VID-01 — Master walkthrough plays smoothly in 4K
**Given** a generated `master_4k.mp4`
**When** played in VLC / QuickTime / browser
**Then**
- Duration = 60s ± 2s
- Resolution = 3840×2160
- Frame rate = 30fps (no stutter, no dropped frames)
- Codec = H.264 (verify with `ffprobe`)
- Plays from start to finish without artifacts (no banding, no compression blocks visible at 100% zoom)
- Audio sync OK (if audio present)

### AC-VID-02 — Reel meets social media platform specs
**Given** a generated `reel_9x16_1080p.mp4`
**When** uploaded to YouTube Shorts, Instagram Reels, and TikTok (test all three)
**Then**
- Each platform accepts upload without "format unsupported" error
- Duration = 20-30s
- Resolution = 1080×1920
- Aspect = 9:16 vertical
- Bitrate 10-15 Mbps (verify with `ffprobe`)
- Important content stays in safe area (no critical elements cropped at top 13% or bottom 17% — TikTok UI overlay zone)

### AC-VID-03 — Master walkthrough has structured narrative
**Given** the master video
**When** reviewed by PO
**Then**
- 0:00-0:15 shows exterior approach (front facade reveal, drone-style camera)
- 0:15-0:50 shows interior walkthrough (living room → kitchen → bedrooms — at least 3 key rooms)
- 0:50-1:00 shows exterior closing shot (sunset/dusk lighting if Tropical VN style)
- Camera motion smooth (no jerky cuts, no whip pans)
- No text overlays in master (text overlays only in derived reel)

### AC-VID-04 — Derivatives extracted correctly
**Given** the master video
**When** derivative pipeline runs
**Then**
- `hero_still_4k.png` extracted from a frame between 0:08-0:12 (typical hero exterior moment), 3840×2160, sRGB
- `preview.gif` extracted from a 6-10s segment, ≤ 5 MB, plays loop seamlessly
- Both derivatives present in `/derivatives/` folder

### AC-VID-05 — Failure case
**Given** a render that produces black frames, encoding errors, or fails Twinmotion render queue
**When** pipeline detects failure
**Then** bundle is NOT delivered; user receives clear error notification.

## PR-VID.3 Out of Scope (Phase 1 MVP)

- ❌ Voiceover / narration (royalty-free music only)
- ❌ Multi-language subtitles
- ❌ Long-form walkthrough > 60s (constraint per OQ3)
- ❌ Mid-length 30-45s cut (rejected per OQ3 — only 2 cuts)
- ❌ Day/night cycle automation (single time-of-day per render)
- ❌ Custom branding/watermark per project (Phase 2+)

---

# PR-MAN — Manifest & Bundle

## PR-MAN.1 Functional Requirements

| ID | Requirement | Type | Priority |
|---|---|---|---|
| F-MAN-01 | Generate `manifest.json` per project with bundle metadata | Functional | Must |
| F-MAN-02 | Schema includes: project_id, generated_at, version, lod_summary (count per LOD), material_list, file_inventory (path + size + checksum SHA256), source_brief (text input), agent_provenance (which generation step produced what) | Functional | Must |
| F-MAN-03 | File naming follows ISO 19650-inspired pattern: `<Project>-<Originator>-<Type>-<Number>` (Originator = "AIA", Type = "DR" for drawing / "MOD" for model / "VID" for video) | Functional | Should |
| F-MAN-04 | Manifest validates against JSON Schema (provided in Appendix B) | Non-functional | Must |

## PR-MAN.2 Acceptance Criteria

### AC-MAN-01 — Manifest is parseable and complete
**Given** a generated `manifest.json`
**When** validated against schema
**Then**
- Passes JSON Schema validation
- All file paths in `file_inventory` exist on disk
- All checksums match actual file SHA256
- `lod_summary` element count matches scene graph

### AC-MAN-02 — Bundle is self-contained
**Given** the entire `/project-<id>/` folder
**When** zipped and moved to a different machine
**Then**
- All file paths in manifest resolve relatively
- No external dependencies (textures embedded or referenced relatively)
- glTF/FBX/USDZ all open standalone

---

# Cross-Cutting Non-Functional Requirements

| NFR | Spec |
|---|---|
| **Pipeline mode** | Async-first (OQ1). Job submitted → notification 15-60min when bundle ready. |
| **Throughput** | Target 100 projects/day on 3-6 RTX 4090-class GPUs (RunPod cloud). |
| **Failure handling** | Per-stage retry (max 3); on final failure, user notified with stage + reason. |
| **Storage** | S3-compatible bucket; signed URL for download; TTL 30 days for free tier. |
| **Audit** | Every job logs: input brief, agent decisions, render time per stage, output checksums. |
| **Cost cap (informational)** | < $5 GPU + storage cost per project at production volume. |

---

# Appendix A — AIA Layer Dictionary (subset for MVP)

| Layer | Color | Lineweight | Description |
|---|---|---|---|
| `A-WALL` | white | 0.50mm | Wall, full height |
| `A-WALL-PRHT` | gray | 0.35mm | Wall, partial height (knee wall) |
| `A-DOOR` | yellow | 0.25mm | Door symbols |
| `A-DOOR-IDEN` | yellow | 0.18mm | Door tag/ID |
| `A-GLAZ` | cyan | 0.25mm | Window/glazing |
| `A-FURN` | green | 0.18mm | Furniture |
| `A-FLOR-FIXT` | green | 0.18mm | Floor-mounted fixtures |
| `A-AREA` | magenta | 0.13mm | Room area boundary |
| `A-AREA-IDEN` | magenta | 0.13mm | Room name/area label |
| `A-ROOF` | white | 0.35mm | Roof outline |
| `A-ANNO-DIMS` | red | 0.25mm | Dimensions |
| `A-ANNO-TEXT` | red | 0.25mm | Text annotations |
| `A-ANNO-NPLT` | red (no plot) | — | Construction lines (not plotted) |
| `A-ANNO-TTLB` | white | 0.50mm | Title block |
| `A-ANNO-NORTH` | red | 0.25mm | North arrow |
| `A-ELEV-OTLN` | white | 0.50mm | Elevation outline |
| `A-SECT-MCUT` | white | 0.70mm | Section cut line (heavy) |
| `A-SECT-OTLN` | white | 0.50mm | Section outline beyond cut |
| `S-COLS` | white | 0.50mm | Structural columns |
| `S-BEAM` | white | 0.50mm | Beams |
| `S-FNDN` | white | 0.50mm | Foundation |
| `E-LITE` | yellow | 0.18mm | Lighting fixtures |
| `P-FIXT` | cyan | 0.18mm | Plumbing fixtures |
| `L-PLNT` | green | 0.18mm | Landscape/planting |
| `L-SITE` | brown | 0.25mm | Site boundary |

Reference PDF: https://facilities.duke.edu/sites/default/files/AIA%20CAD%20Layer%20Guidelines.pdf

# Appendix B — Manifest JSON Schema (sketch)

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "required": ["project_id", "generated_at", "version", "lod_summary", "material_list", "file_inventory"],
  "properties": {
    "project_id":   { "type": "string", "pattern": "^[a-zA-Z0-9-_]+$" },
    "generated_at": { "type": "string", "format": "date-time" },
    "version":      { "type": "string", "pattern": "^\\d+\\.\\d+\\.\\d+$" },
    "naming_convention": {
      "type": "object",
      "properties": {
        "pattern": { "const": "<Project>-<Originator>-<Type>-<Number>" },
        "originator": { "const": "AIA" }
      }
    },
    "lod_summary": {
      "type": "object",
      "properties": {
        "lod_100": { "type": "integer", "minimum": 0 },
        "lod_200": { "type": "integer", "minimum": 0 },
        "lod_300": { "type": "integer", "minimum": 0 }
      }
    },
    "material_list": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["name", "workflow", "textures"],
        "properties": {
          "name":     { "type": "string" },
          "workflow": { "const": "metallic-roughness" },
          "textures": {
            "type": "object",
            "properties": {
              "baseColor":         { "type": "string" },
              "metallicRoughness": { "type": "string" },
              "normal":            { "type": "string" },
              "ao":                { "type": "string" },
              "emissive":          { "type": "string" }
            }
          },
          "resolution": { "enum": ["1K", "2K", "4K"] }
        }
      }
    },
    "file_inventory": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["path", "size_bytes", "sha256"],
        "properties": {
          "path":       { "type": "string" },
          "size_bytes": { "type": "integer" },
          "sha256":     { "type": "string", "pattern": "^[a-f0-9]{64}$" }
        }
      }
    },
    "source_brief": { "type": "string" },
    "agent_provenance": { "type": "object" }
  }
}
```

---

# Definition of Done — Per Project Bundle

A project bundle is "done" when **ALL** of the following pass:

For this DoD, "CI gate" means the required verification gate executed under the active protocol in [`07-local-git-verification-protocol.md`](07-local-git-verification-protocol.md). GitHub Actions is optional; local Linux-equivalent verification is acceptable when it records reproducible commands, environment/tool versions, and JSON/Markdown gate summaries.

- [ ] All required DWG sheets generated per the sheet strategy (minimum 4 for single-storey; multi-storey produces one A-101-F<N> per floor — golden fixture = 5 sheets), AIA-compliant, open in AutoCAD without errors
- [ ] PDF presentation set generated, all pages have title block, VN labels render correctly
- [ ] `model.glb` passes Khronos glTF Validator (0 errors)
- [ ] `model.fbx` imports into Twinmotion 2024.1 without warnings
- [ ] `model.usdz` ≤ 8 MB, opens in iOS AR Quick Look at correct scale
- [ ] `master_4k.mp4` plays at 4K 30fps, duration 60s ± 2s
- [ ] `reel_9x16_1080p.mp4` accepted by YouTube/Instagram/TikTok upload
- [ ] Hero still + GIF derivatives extracted
- [ ] All textures KTX2-compressed, Metal-Rough workflow
- [ ] `manifest.json` validates against schema, all checksums match
- [ ] Bundle zips to single archive < 500 MB total
- [ ] Failure modes tested: bundle does NOT deliver if any required artifact fails its required verification gate

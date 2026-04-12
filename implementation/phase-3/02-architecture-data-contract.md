# Phase 3 - Architecture & Data Contract Specification

*Version: 1.0*
*Ngay tao: Apr 12, 2026*
*Audience: Tech Lead, Backend, AI Team, Solution Architect*
*Source: 00-market-standard-2d-output-requirements.md*
*Prerequisite: 11-phase2-layer2-full-deliverable.md (geometry schema)*

---

## 1. Nguyen tac kien truc

### 1.1 Canonical-source principle
Moi output (plan, elevation, section, schedule, DXF, IFC) phai derive tu CUNG 1 canonical geometry source. KHONG co sheet nao duoc tao doc lap.

### 1.2 Usability principle
Export file phai DUNG DUOC trong downstream workflow, khong chi "file ton tai". DXF phai mo duoc trong AutoCAD. IFC phai mo duoc trong BIM viewer.

### 1.3 Typology-extensible principle
Schema phai cho phep them typology moi ma khong pha vo export contracts hien co.

### 1.4 Verified-vs-assumed principle
Moi data point trong geometry phai carry `source` tag: `confirmed | inferred | default`.

---

## 2. End-to-End Pipeline Architecture

```
BRIEF INTAKE                PLANNING ENGINE              CANONICAL GEOMETRY
+------------------+       +-------------------+        +-------------------+
| Structured Brief |------>| Typology Router   |------->| Geometry Layer 2  |
| + typology       |       | + Rule Engine     |        | + source tags     |
| + room program   |       | + AI Suggestions  |        | + annotation      |
| + material dir.  |       | + Option Generator|        |   anchors         |
| + assumption     |       +-------------------+        +--------+----------+
|   rules          |                                             |
+------------------+                                             |
                                                                 |
                    +--------------------------------------------+
                    |                    |                    |
                    v                    v                    v
          DRAWING ENGINE         SCHEDULE ENGINE       INTEROP ENGINE
          +--------------+      +---------------+     +---------------+
          | FloorPlanRndr|      | DoorSchedule  |     | DXF Exporter  |
          | ElevationRndr|      | WindowSchedule|     | IFC Exporter  |
          | SectionRndr  |      | RoomSchedule  |     | CSV Exporter  |
          | SitePlanRndr |      | AreaSummary   |     +-------+-------+
          | DimensionEng |      +-------+-------+             |
          | AnnotationEng|              |                     |
          +------+-------+              |                     |
                 |                      |                     |
                 v                      v                     v
          SHEET COMPOSITOR        SCHEDULE SHEETS        EXPORT FILES
          +--------------+       +---------------+      +---------------+
          | Title Block   |      | SVG Tables    |      | .dxf          |
          | Sheet Frame   |      | PDF Tables    |      | .ifc          |
          | Visual Preset |      | CSV Data      |      | .csv          |
          +------+-------+      +-------+-------+      +-------+-------+
                 |                      |                       |
                 v                      v                       v
          +-------------------------------------------------------------+
          |                  PACKAGE ASSEMBLER                           |
          |  Combined PDF + Per-sheet SVG + PNG Previews                 |
          |  + DXF + IFC + CSV + Manifest JSON                          |
          |  -> export_packages table                                    |
          +-------------------------------------------------------------+
```

---

## 3. Geometry Layer 2 Data Contract

### 3.1 Schema version

```
$schema: "ai-architect-geometry-v2"
version: "2.0"
```

Moi geometry_json PHAI co `$schema` va `version` field. Export pipeline check version truoc khi render.

### 3.2 Top-level structure (bat buoc)

```
geometry_json: {
  $schema: string           // "ai-architect-geometry-v2"
  version: string           // "2.0"
  units: "metric"
  precision: 3              // decimal places

  project_info: ProjectInfo       // REQ-BRIEF-002
  grids: GridSystem               // REQ-GEO-002
  levels: Level[]                 // REQ-GEO-002
  site: SiteData                  // REQ-GEO-002
  walls: Wall[]                   // REQ-GEO-004
  openings: Opening[]             // REQ-GEO-005
  rooms: Room[]                   // REQ-GEO-003
  stairs: Stair[]                 // REQ-GEO-002
  fixtures: Fixture[]             // REQ-GEO-002
  roof: RoofData                  // REQ-GEO-002
  markers: MarkerSet              // REQ-GEO-006
  dimensions_config: DimConfig    // REQ-ANNO-003
}
```

### 3.3 Entity contracts

#### Wall contract (REQ-GEO-004)

```typescript
interface Wall {
  id: string                    // Stable ID, never changes across revisions
  level: string                 // Reference to Level.id
  start: [number, number]       // [x, y] in meters
  end: [number, number]
  type: "exterior" | "interior" | "party_wall" | "curtain_wall"
  assembly: {
    total_thickness_m: number
    layers: WallLayer[]         // From exterior to interior face
  }
  structural: boolean
  fire_rating: string | null    // "REI60", "REI90", etc.
  extends_levels: string[]      // If wall continues across multiple levels
  grid_reference: {             // Snap to grid for dimensioning
    axis: string
    offset: number
  } | null
  source: "confirmed" | "inferred" | "default"  // REQ-BRIEF-005
}

interface WallLayer {
  material: string              // "brick_100", "plaster", "insulation", "reinforced_concrete"
  thickness_m: number
  side: "exterior" | "interior" | null
  note: string | null
}
```

#### Opening contract (REQ-GEO-005)

```typescript
interface Opening {
  id: string
  wall_id: string              // Reference to Wall.id
  type: "door" | "window"
  subtype: string              // "entrance_double", "sliding", "casement", "fixed"
  position_along_wall_m: number
  width_m: number
  height_m: number
  sill_height_m: number
  level: string

  frame: {
    material: string           // "aluminum", "wood", "upvc", "steel"
    color: string
    profile: string            // "slim", "standard", "heavy"
  }

  // Door-specific
  panel?: {
    material: string
    type: string               // "swing", "sliding", "folding"
    swing_direction?: "inward" | "outward"
    leaves: number
  }
  hardware?: {
    handle: string
    lock: string
  }

  // Window-specific
  glazing?: {
    type: string               // "single", "double_low_e", "triple"
    thickness_mm: number
    u_value: number
    solar_heat_gain: number
  }
  operation?: {
    type: string               // "casement", "sliding", "fixed", "awning"
    hinge_side?: "left" | "right"
  }

  fire_rating: string | null
  schedule_mark: string        // "D01", "W01" - MUST be unique + cross-referenced
  schedule_group: string       // For grouping in schedule table
  source: "confirmed" | "inferred" | "default"
}
```

#### Room contract (REQ-GEO-003)

```typescript
interface Room {
  id: string
  name: string
  name_en: string
  type: string                 // "living", "kitchen", "bedroom", "bathroom", etc.
  level: string
  polygon: [number, number][]
  area_m2: number              // Computed from polygon
  perimeter_m: number          // Computed from polygon
  clear_height_m: number

  finishes: {
    floor: FinishSpec
    wall: FinishSpec
    ceiling: FinishSpec
    baseboard: FinishSpec | null
  }

  doors: string[]              // Opening IDs
  windows: string[]            // Opening IDs
  fixtures_refs: string[]      // Fixture IDs

  electrical?: {
    outlets: number
    switches: number
    lighting_points: number
  }
  plumbing?: {
    hot_water: boolean
    cold_water: boolean
    waste: boolean
    gas: boolean
  }

  source: "confirmed" | "inferred" | "default"
}

interface FinishSpec {
  material: string
  size?: string                // "600x600"
  color?: string
  code?: string                // "RAL9010"
  type?: string                // "flat", "coffered"
  height_m?: number            // For partial finishes like backsplash
  note?: string
}
```

#### Level contract

```typescript
interface Level {
  id: string
  name: string
  elevation_m: number          // From datum (ground = 0.0)
  type: "ground" | "floor" | "roof" | "basement"
  floor_to_floor_m?: number   // Only for type = "floor"
  slab_thickness_m?: number
  clear_height_m?: number
  ceiling_height_m?: number
}
```

#### Stair contract

```typescript
interface Stair {
  id: string
  from_level: string
  to_level: string
  type: "straight" | "l_turn" | "u_turn" | "spiral"
  position: [number, number][]  // Bounding polygon
  direction: "up"
  geometry: {
    run_count: number
    riser_height_mm: number
    tread_depth_mm: number
    width_m: number
    landing_depth_m: number
    turn_at_step: number | null
  }
  handrail: {
    material: string
    height_mm: number
    sides: ("left" | "right")[]
  }
  finish: { tread: string, riser: string }
  headroom_m: number
  code_compliance: {
    min_headroom_m: number
    max_riser_mm: number
    min_tread_mm: number
    status: "pass" | "fail" | "not_checked"
  }
}
```

### 3.4 Stable ID rules

| Rule | Chi tiet |
|------|----------|
| Format | `{type}_{sequence}` (vd: `w1`, `D01`, `r1`, `s1`) |
| Persistence | ID KHONG thay doi khi revision. D01 luon la D01 across versions. |
| Deletion | Neu opening bi xoa, ID do KHONG duoc reuse. |
| Cross-reference | schedule_mark dung chinh ID cua opening. Room.doors[] dung Opening.id. |
| Validation | Khong co 2 entity nao cung type co trung ID. |

### 3.5 Source tag contract (REQ-BRIEF-005)

Moi entity can support `source` field:

```json
{"source": "confirmed"}   // User nhap va xac nhan
{"source": "inferred"}    // AI suy ra
{"source": "default"}     // System default

// Aggregate: package co the show "3 confirmed, 12 inferred, 5 default"
// Gate: issue "design_development" package require >= 80% confirmed
```

---

## 4. Sheet System Contract

### 4.1 Sheet types va mapping

| Sheet type | Sheet number | Content | Scale | Data source |
|------------|-------------|---------|-------|-------------|
| cover | A0 | Title, index, preview, disclaimer | N/A | Package metadata |
| site | A1 | Boundary, footprint, north, scale | 1:200 | geometry.site + levels[0] |
| floor_plan | A2, A3, A4... | Walls, openings, fixtures, tags, dims | 1:100 | geometry.walls/openings/rooms per level |
| elevation | A6, A7 | Facade, openings, roof, levels, dims | 1:100 | geometry.walls/openings/roof per face |
| section | A8 | Cut, levels, slab/roof, stairs | 1:100 | geometry cross-section at marker |
| schedule_opening | A9 | Door + window tables | N/A | geometry.openings |
| schedule_room | A10 | Room table + area summary | N/A | geometry.rooms |
| key_detail | A11, A12 | Minimum DD key detail sheets (wall/roof/wet-area/stair/threshold) | 1:20 / 1:10 | canonical geometry + detail templates + metadata |
| notes | A13 | Legend, abbreviations, general notes | N/A | Template + geometry metadata |

### 4.2 Title block contract (REQ-GRAPHIC-004)

```
+---------------------------------------------------------------+
|  [KTC KTS WORDMARK] PROJECT: {project_info.name}              |
|                     PACKAGE: DESIGN DEVELOPMENT PACKAGE        |
|                     SHEET:   {sheet.title}         No: {sheet.number} |
|                     SCALE:   {sheet.scale}         PRESET: {package.deliverable_preset} |
|                     DATE:    {package.issue_date}  REV: {package.revision_label} |
|                     PREP:    KTC KTS              STATUS: {package.status} |
+---------------------------------------------------------------+
```

Fields:
- project_info.name -> tu geometry
- sheet.title -> tu sheet definition
- sheet.number -> tu sheet definition
- sheet.scale -> per sheet type
- package.issue_date -> tu export_packages
- package.revision_label -> tu export_packages
- package.deliverable_preset -> `technical_neutral` or `client_presentation`
- package.status -> `draft` | `review` | `issued` | `degraded_preview`
- organization name -> fixed as `KTC KTS` for Phase 3 issued packages
- Wordmark asset -> `assets/ktc-kts-wordmark.svg`

Title block policy:
- Both launch presets keep the same KTC KTS wordmark and wording.
- `technical_neutral` uses restrained monochrome treatment.
- `client_presentation` may apply the approved accent color, but field wording does not change.
- `degraded_preview` is valid for preview/export review only and cannot be used for issue.

### 4.3 Sheet metadata contract (REQ-SHEET-010)

```json
{
  "number": "A2",
  "title": "Floor Plan - Tang 1",
  "type": "floor_plan",
  "scale": "1:100",
  "orientation": "landscape",
  "source_level": "L1",
  "source_version_id": "uuid",
  "files": {
    "pdf_page": 3,
    "svg": "s3://bucket/packages/{id}/A2.svg",
    "png_preview": "s3://bucket/packages/{id}/A2.png"
  }
}
```

---

## 5. Annotation & Dimension Contract

### 5.1 Dimension style contract (REQ-ANNO-003)

```json
{
  "style": "architectural",
  "text_height_mm": 2.5,
  "arrow_type": "tick",
  "extension_line_gap_mm": 2,
  "extension_line_overshoot_mm": 2,
  "units": "mm",
  "precision": 0,
  "chain_offset_from_building_mm": 10,
  "chain_spacing_mm": 7
}
```

### 5.2 Dimension chain types (REQ-ANNO-002)

| Chain | Placement | Content |
|-------|-----------|---------|
| overall | Outermost, 4 sides | Total building width + depth |
| grid | Next chain in | Grid axis spacing |
| wall_to_wall | Next chain in | Major wall distances |
| opening | Innermost external | Opening positions + widths |
| room_internal | Inside rooms | Room width x depth |
| stair | At stair | Riser count x height = total rise |
| elevation_vertical | Side of elevation | Floor levels + total height |
| elevation_horizontal | Below elevation | Opening positions |

### 5.3 Symbol families (REQ-ANNO-005)

| Symbol | Used on | Standard |
|--------|---------|----------|
| North arrow | Site, plan sheets | Circle + N indicator |
| Section marker | Plan sheets | Circle with line + direction |
| Elevation marker | Plan sheets | Triangle with direction |
| Detail marker | Plan, elevation, section | Circle with sheet/detail ref |
| Stair up/down | Plan sheets | Arrow with UP/DN text |
| Door swing | Plan sheets | Arc from hinge point |
| Window symbol | Plan sheets | Parallel lines (glazing) |
| Schedule tag | Plan, elevation | Circle/hexagon with mark (D01, W01) |
| Level marker | Elevations, sections | Triangle with elevation value |
| Room tag | Plan sheets | Name + area in frame |

### 5.4 Label collision avoidance (REQ-ANNO-004)

```python
class AnnotationPlacer:
    """Place annotations avoiding overlap with geometry and other annotations."""
    
    def place_room_tag(self, room: Room, occupied_zones: list[Rect]) -> Position:
        # 1. Try room centroid
        # 2. If collision, try offset positions (4 quadrants)
        # 3. If still collision, try outside room with leader line
        # 4. Log warning if no valid position found
    
    def place_dimension_chain(self, chain: DimChain, occupied_zones: list[Rect]) -> list[Position]:
        # Fixed offset from building edge
        # Chains stack outward, never inward
        # Text always readable (not upside down)
```

---

## 6. DXF Export Contract

### 6.1 Format

| Property | Value |
|----------|-------|
| DXF version | R2018 (AC1032) |
| Units | Millimeters in model space |
| Coordinate system | Local project (origin = site corner or building corner) |

### 6.2 Layer contract (REQ-DXF-003)

Tham chieu day du: `11-phase2-layer2-full-deliverable.md` Section 4.2 (25+ layers)

Summary:
- `A-WALL-EXTR`: exterior walls, color 7, lineweight 50
- `A-WALL-INTR`: interior walls, color 7, lineweight 30
- `A-DOOR`: doors, color 3, lineweight 25
- `A-GLAZ`: windows, color 5, lineweight 25
- `A-ANNO-DIMS`: dimensions, color 2, lineweight 13
- `A-ANNO-ROOM`: room tags, color 4, lineweight 13
- (Full list in 11-phase2-layer2)

### 6.3 Model space contract

| Content | How |
|---------|-----|
| Floor plans | Each level at 1:1, offset vertically by `level_spacing` |
| Site plan | At 1:1, offset from floor plans |
| 4 Elevations | At 1:1, offset horizontally |
| 2 Sections | At 1:1, offset from elevations |

### 6.4 Paper space contract (REQ-DXF-005)

| Layout name | Viewport content | Scale |
|-------------|-----------------|-------|
| A0-COVER | Title block only | N/A |
| A1-SITE | Site plan viewport | 1:200 |
| A2-TANG1 | Floor plan L1 viewport | 1:100 |
| A2-TANG2...N | Floor plan L2..N viewport | 1:100 |
| A6-ELEV-SN | South + North elevations | 1:100 |
| A7-ELEV-EW | East + West elevations | 1:100 |
| A8-SECTIONS | Section A-A + B-B | 1:100 |
| A9-SCHEDULES | Schedule tables | N/A |

### 6.5 DXF validation criteria (REQ-DXF-004)

| Check | Tool | Pass criteria |
|-------|------|---------------|
| Opens without error | AutoCAD 2024 | No crash, no missing objects |
| Opens without error | LibreCAD | No crash, geometry visible |
| Opens without error | DraftSight | No crash, text readable |
| Layer structure | Any CAD | 25+ layers present, correctly named |
| Text legible | Visual check | All text readable, correct style |
| Dimensions editable | AutoCAD | Dims are DIMENSION entities, not exploded |
| Hatching correct | Any CAD | Wall poché visible on cut walls |

---

## 7. IFC Export Contract

### 7.1 IFC version

IFC 4x3 (ISO 16739-1:2024)

### 7.2 Entity coverage (REQ-IFC-002)

| IFC Entity | Source | Required Phase 3 | Phase 4+ |
|------------|--------|-------------------|----------|
| IfcProject | project_info | Yes | Yes |
| IfcSite | geometry.site | Yes (boundary only) | + topography |
| IfcBuilding | project_info | Yes | Yes |
| IfcBuildingStorey | geometry.levels | Yes (all floor levels) | Yes |
| IfcWall / IfcWallStandardCase | geometry.walls | Yes (position + type) | + assembly layers |
| IfcDoor | geometry.openings[door] | Yes (position + size) | + hardware Psets |
| IfcWindow | geometry.openings[window] | Yes (position + size) | + glazing Psets |
| IfcSpace | geometry.rooms | Yes (boundary + name + area) | + finish Psets |
| IfcSlab | geometry.levels | Yes (per level) | + edge detail |
| IfcStairFlight | geometry.stairs | Basic (bounding box) | + detailed geometry |
| IfcRoof | geometry.roof | Basic (outline) | + layers |

### 7.3 Property sets Phase 3

| Pset | Properties | Required |
|------|-----------|----------|
| Pset_WallCommon | Reference, IsExternal, FireRating | Yes |
| Pset_DoorCommon | Reference, FireRating, IsExternal | Yes |
| Pset_WindowCommon | Reference, IsExternal | Yes |
| Pset_SpaceCommon | Reference, Category, NetFloorArea | Yes |
| Qto_WallBaseQuantities | Length, Height, Width | Yes |
| Qto_SpaceBaseQuantities | NetFloorArea, GrossFloorArea, Height | Yes |

### 7.4 IFC validation (REQ-IFC-003)

| Check | Tool | Pass criteria |
|-------|------|---------------|
| Opens without error | Solibri Anywhere | Spatial structure visible |
| Opens without error | BIMvision | All entities present |
| Schema validation | IfcOpenShell validate | No critical errors |
| Spatial containment | Manual | Rooms in correct storey |

---

## 8. Package Manifest Contract V2

```json
{
  "manifest_version": "2.0",
  "package_id": "uuid",
  "project_id": "uuid",
  "version_id": "uuid",
  "issue_type": "design-development-package",
  "revision_label": "A",
  "status": "issued",
  "issue_date": "2026-04-12",
  "export_timestamp": "2026-04-12T10:30:00Z",
  "geometry_schema_version": "2.0",
  "export_pipeline_version": "3.1.0",

  "deliverable_preset": "technical_neutral",
  "typology": "townhouse",

  "sheets": [
    {
      "number": "A0",
      "title": "Cover / Issue Sheet",
      "type": "cover",
      "scale": null,
      "orientation": "landscape",
      "files": {
        "pdf_page": 1,
        "svg": "s3://...A0.svg",
        "png_preview": "s3://...A0_preview.png"
      }
    }
  ],
  "total_sheets": 12,

  "exports": {
    "combined_pdf": "s3://...package.pdf",
    "dxf": "s3://...project.dxf",
    "ifc": "s3://...project.ifc",
    "schedules_csv": {
      "door": "s3://...door_schedule.csv",
      "window": "s3://...window_schedule.csv",
      "room": "s3://...room_schedule.csv"
    }
  },

  "source": {
    "brief_version": 3,
    "geometry_version": "2.0",
    "canonical_version_id": "uuid",
    "canonical_locked_at": "2026-04-11T14:00:00Z"
  },

  "assumptions": {
    "total": 20,
    "confirmed": 15,
    "inferred": 3,
    "default": 2
  },

  "disclaimer": "DESIGN DEVELOPMENT PACKAGE. NOT FOR PERMIT, CONSTRUCTION, FABRICATION, OR SITE EXECUTION WITHOUT PROFESSIONAL VERIFICATION."
}
```

---

## 9. Database Changes

### 9.1 export_packages table upgrade

```sql
ALTER TABLE export_packages
    ADD COLUMN deliverable_preset VARCHAR(50),      -- technical_neutral | client_presentation | branded_studio
    ADD COLUMN typology VARCHAR(50),                 -- townhouse | villa | apartment_reno | shophouse | home_office
    ADD COLUMN geometry_schema_version VARCHAR(10),  -- "2.0"
    ADD COLUMN export_pipeline_version VARCHAR(20),  -- "3.1.0"
    ADD COLUMN assumptions_summary JSONB,            -- {total, confirmed, inferred, default}
    ADD COLUMN dxf_url TEXT,
    ADD COLUMN ifc_url TEXT,
    ADD COLUMN schedule_csv_urls JSONB;              -- {door: url, window: url, room: url}
```

### 9.2 Brief model upgrade

```sql
ALTER TABLE design_versions
    ADD COLUMN brief_schema_version VARCHAR(10) DEFAULT '1.0';

-- brief_json Phase 3 adds:
-- project_type, renovation_flag, survey_verified, room_priority_ranking,
-- adjacency_constraints, privacy_constraints, daylight_preference,
-- parking_type, facade_direction, material_direction,
-- target_package_type, expected_formats, assumption_rules
```

---

## 10. Non-Functional Requirements

### 10.1 Performance targets

| Operation | Target | Measurement |
|-----------|--------|-------------|
| Option generation (1 typology) | < 60s | Brief submit -> 3 options ready |
| Sheet composition (12+ sheets) | < 30s | Geometry -> all SVG sheets |
| PDF assembly (12+ pages) | < 10s | SVG sheets -> combined PDF |
| DXF export | < 20s | Geometry -> .dxf file |
| IFC export | < 15s | Geometry -> .ifc file |
| Full package (all formats) | < 120s | Trigger -> all files ready |
| Preview generation | < 5s per sheet | For draft preview before full export |

### 10.2 Reliability

- NFR-REL-001: Export REPEATABLE tu cung locked source. Cung geometry + cung pipeline version = cung output.
- NFR-REL-002: Degraded pipeline output phai MARK DEGRADED va block issue.

### 10.3 Traceability (NFR-TRACE-001)

Moi issued package phai traceable den:
- source_version_id (canonical)
- geometry_schema_version
- export_pipeline_version
- issue_timestamp
- brief_version

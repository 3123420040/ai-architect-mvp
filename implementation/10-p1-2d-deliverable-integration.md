# 10 - P1 2D Deliverable Integration Decision

*Version: 1.0 FINAL*
*Ngay chot: Apr 12, 2026*
*Input: 19-p1-2d-deliverable-product-requirements.md + 18-p1-2d-deliverable-market-research-report.md + 05-system-design.md*

---

## 1. Van de can giai quyet

Hai tai lieu moi (P1 2D Deliverable Market Research va Product Requirements) dinh nghia chuan "professional schematic design package" cho san pham. Chuan nay xung dot voi scope Phase 1 da chot trong 05-system-design.md o nhieu diem.

### Xung dot chinh

| Khia canh | 05-system-design.md (da chot) | P1 2D Deliverable (moi) |
|---|---|---|
| M5 output | Floor plan images (PNG 2048x2048) | Coordinated geometry cho plan + elevation + section |
| Geometry Phase 1 | Layer 1: basic metadata (rooms, areas) | Walls, openings, stairs, room polygons, levels |
| M8 Export | PDF concept package (WeasyPrint wrap images) | Sheet composition engine voi title blocks, 4-6 sheets |
| Elevation/Section | Khong co trong Phase 1 | 2 elevations + 1 section required |
| Site plan | Khong co trong Phase 1 | Site/plot sheet required |
| SVG | SVG export tu floor plan image | Sheet-native vector output |

---

## 2. Quyet dinh kien truc

**PHASED ADOPTION - 3 bac**

05-system-design.md VAN LA source of truth cho scope. P1 2D deliverable standard duoc tich hop theo 3 bac de khong pha vo timeline hien tai.

### Bac 1: Phase 1 MVP (Sprint 5-6) - Professional PDF, giu geometry Layer 1

**Nguyen tac:** Dung geometry_json hien tai (basic metadata) + floor plan images, nhung NANG CAP M8 Export tu "concept wrapper" len "professional sheet package".

**Thay doi cu the:**

```
TRUOC (current M8):
  WeasyPrint -> 1 file PDF chua: cover text + floor plan images + render images
  
SAU (upgraded M8):
  WeasyPrint + Jinja2 sheet templates -> multi-page PDF:
    Sheet A0: Cover/Issue (project name, sheet index, date, revision, branding, disclaimer)
    Sheet A2+: Floor Plan (floor plan IMAGE framed voi title block, room labels overlay tu geometry_json)
    Sheet R1: Renders (3D renders voi title block)
  + Package manifest JSON
  + Per-sheet SVG (floor plan image embedded in sheet frame)
  + Revision labeling tren moi sheet
```

**Tai sao khong vi pham 05-system-design.md:**
- Geometry van la Layer 1 (basic metadata)
- Van dung floor plan images tu M5
- Chi them professional framing cho PDF export (von nam trong scope M8)
- Title block, revision label, disclaimer la metadata - khong doi geometry

**Deliverable standard dat duoc:** Tier 1.5 - tot hon concept board, co sheet discipline, nhung chua co elevation/section

---

### Bac 2: Phase 1 MVP+ (Sprint 9-10) - Geometry Layer 1.5 + Full schematic package

**Nguyen tac:** Upgrade geometry de ho tro elevation/section derivation. Build sheet composition engine cho true vector output.

**Geometry Layer 1.5 schema:**

```json
{
  "levels": [
    {"id": "L1", "name": "Tang 1", "elevation_m": 0.0, "floor_to_floor_m": 3.3},
    {"id": "L2", "name": "Tang 2", "elevation_m": 3.3, "floor_to_floor_m": 3.3}
  ],
  "site": {
    "boundary": [[0,0], [5,0], [5,20], [0,20]],
    "orientation": "south",
    "setbacks": {"front": 3, "back": 2, "left": 0, "right": 0}
  },
  "walls": [
    {"id": "w1", "start": [0,0], "end": [5,0], "thickness": 0.2, "level": "L1", "type": "exterior"},
    {"id": "w2", "start": [0,0], "end": [0,8], "thickness": 0.2, "level": "L1", "type": "exterior"},
    {"id": "w3", "start": [0,4.8], "end": [5,4.8], "thickness": 0.1, "level": "L1", "type": "interior"}
  ],
  "openings": [
    {"id": "o1", "wall_id": "w1", "type": "door", "position_along_wall": 2.0, "width": 1.2, "height": 2.4},
    {"id": "o2", "wall_id": "w2", "type": "window", "position_along_wall": 1.5, "width": 1.5, "height": 1.5, "sill_height": 0.9}
  ],
  "rooms": [
    {"id": "r1", "polygon": [[0,0],[5,0],[5,4.8],[0,4.8]], "type": "living", "name": "Phong khach", "level": "L1", "area_m2": 24},
    {"id": "r2", "polygon": [[0,4.8],[5,4.8],[5,8],[0,8]], "type": "kitchen", "name": "Bep", "level": "L1", "area_m2": 16}
  ],
  "stairs": [
    {"id": "s1", "from_level": "L1", "to_level": "L2", "type": "straight", "position": [[4,6],[5,8]], "direction": "up"}
  ],
  "fixtures": [
    {"type": "kitchen_counter", "room_id": "r2", "polygon": [[0.1,5],[2,5],[2,5.6],[0.1,5.6]]},
    {"type": "toilet", "room_id": "r3", "position": [4.2, 3.5]}
  ],
  "roof": {
    "type": "flat",
    "parapet_height_m": 0.6,
    "total_height_m": 13.8
  },
  "markers": {
    "sections": [{"id": "S1", "start": [2.5,0], "end": [2.5,20], "direction": "east"}],
    "elevations": [
      {"id": "E1", "face": "south", "label": "Mat dung chinh"},
      {"id": "E2", "face": "east", "label": "Mat ben"}
    ]
  }
}
```

**Sheet composition engine output:**

```
Full P1 schematic design package:
  Sheet A0: Cover/Issue (project name, hero preview, sheet index, date, revision, branding, disclaimer)
  Sheet A1: Site/Plot (site boundary, building footprint, north arrow, scale bar, setbacks)
  Sheet A2+: Floor Plan per level (TRUE VECTOR from geometry, walls/openings/fixtures/room tags/dimensions)
  Sheet A4: Elevation (2 principal elevations derived from geometry, facade openings, roof line, grade line)
  Sheet A5: Section (1 key section, floor-to-floor, roof/ceiling, stair relationship)
+ Package manifest JSON
+ Per-sheet SVG (native vector)
+ Per-sheet PNG previews
+ Thumbnail contact-sheet
```

**Deliverable standard dat duoc:** Tier 2 - Full "Strong client-facing schematic design package" theo P1 deliverable spec

---

### Bac 3: Phase 2 - Full Layer 2 + expansion

- Full geometry Layer 2 (wall assemblies, material properties, detailed openings)
- 4 exterior elevations (thay vi 2)
- DXF export tu geometry
- Door/window schedules
- Enhanced dimensioning (full dimension chains)
- IFC export khi geometry du chi tiet

---

## 3. Impact len tung module

### M5 2D Generation Engine

| Sprint | Thay doi | Chi tiet |
|---|---|---|
| Sprint 3-4 (MVP) | Khong thay doi | Van generate floor plan images (PNG) tu brief |
| Sprint 9-10 (MVP+) | Output upgrade | Generate structured geometry Layer 1.5 KIEM floor plan images |

**Ghi chu:** M5 o MVP+ phai output BOTH:
- Floor plan image (cho visual display/gallery)
- Structured geometry JSON (cho sheet composition engine)

Cach lam: GPU service (ComfyUI) generate image -> post-processing pipeline extract geometry tu image (hoac generate geometry first, render image from geometry). Day la "canonicalization pipeline" da duoc identify trong rebuttal document.

### M8 Standards Export

| Sprint | Thay doi | Chi tiet |
|---|---|---|
| Sprint 5-6 (MVP) | Nang cap | WeasyPrint + Jinja2 sheet templates, title block system, package manifest |
| Sprint 9-10 (MVP+) | Major upgrade | Sheet composition engine, vector SVG renderer, elevation/section generator |

### M4 Canonical Design State

| Sprint | Thay doi | Chi tiet |
|---|---|---|
| Sprint 1-2 (MVP) | Khong thay doi | geometry_json van la basic metadata |
| Sprint 9-10 (MVP+) | Schema upgrade | geometry_json upgraded to Layer 1.5 |

---

## 4. Cac thanh phan ky thuat moi can build

### 4.1 Sheet Template System (Sprint 5-6, MVP)

```
Jinja2 templates:
  templates/
    sheets/
      base_sheet.html      <- Title block + sheet frame + margins
      cover_sheet.html     <- A0: hero image + metadata
      floor_plan_sheet.html <- A2: floor plan image + room label overlay
      render_sheet.html    <- Render images + title block
    components/
      title_block.html     <- Project name, sheet title, number, date, revision, scale, preparer
      disclaimer.html      <- "CONCEPT DESIGN - NOT FOR CONSTRUCTION"
      revision_label.html  <- Revision A/B/C + date
```

**Tech:** WeasyPrint renders HTML/CSS -> PDF. Moi sheet la 1 HTML page voi CSS @page rules.

### 4.2 Sheet Composition Engine (Sprint 9-10, MVP+)

```python
class SheetComposer:
    def compose_package(self, canonical_version: CanonicalVersion) -> Package:
        geometry = canonical_version.geometry_json  # Layer 1.5
        sheets = []
        
        sheets.append(self.compose_cover(canonical_version))
        sheets.append(self.compose_site_plan(geometry))
        
        for level in geometry["levels"]:
            sheets.append(self.compose_floor_plan(geometry, level))
        
        sheets.append(self.compose_elevations(geometry))
        sheets.append(self.compose_section(geometry))
        
        return Package(sheets=sheets, manifest=self.build_manifest(sheets))
    
    def compose_floor_plan(self, geometry, level) -> Sheet:
        # Generate SVG from wall/opening/room geometry
        svg = FloorPlanRenderer.render(geometry, level)
        # Add room tags, dimensions, fixtures
        svg = AnnotationOverlay.apply(svg, geometry, level)
        # Frame in sheet with title block
        return Sheet(type="floor_plan", svg=svg, title=f"Floor Plan - {level['name']}")
```

**Tech:**
- svgwrite hoac cairo cho vector rendering
- Custom FloorPlanRenderer: geometry JSON -> SVG paths
- Custom ElevationRenderer: geometry JSON -> SVG elevation view
- Custom SectionRenderer: geometry JSON -> SVG section cut

### 4.3 Package Manifest JSON

```json
{
  "package_id": "uuid",
  "project_id": "uuid",
  "version_id": "uuid",
  "issue_date": "2026-04-12",
  "issue_type": "schematic-design-package",
  "revision_label": "A",
  "status": "issued",
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
        "png_preview": "s3://...A0.png"
      }
    },
    {
      "number": "A2",
      "title": "Floor Plan - Tang 1",
      "type": "floor_plan",
      "scale": "1:100",
      "orientation": "landscape",
      "source_level": "L1",
      "files": {
        "pdf_page": 3,
        "svg": "s3://...A2.svg",
        "png_preview": "s3://...A2.png"
      }
    }
  ],
  "export_timestamp": "2026-04-12T10:30:00Z",
  "total_sheets": 5,
  "combined_pdf": "s3://...package.pdf"
}
```

---

## 5. Acceptance criteria cho tung bac

### Bac 1 (MVP) acceptance:
- [ ] PDF co multi-page voi sheet framing (khong phai image dump)
- [ ] Moi sheet co title block (project name, sheet title, number, date, revision)
- [ ] Cover sheet co disclaimer "SCHEMATIC DESIGN - NOT FOR CONSTRUCTION"
- [ ] Floor plan sheet co room labels overlay tu geometry_json
- [ ] Package manifest JSON ton tai va khop voi noi dung
- [ ] Revision label nhat quan giua manifest, title block, va metadata
- [ ] SVG export co sheet frame (du la image embedded)

### Bac 2 (MVP+) acceptance:
- [ ] 4-6 sheets trong package (Cover, Site, Floor Plans, Elevation, Section)
- [ ] Floor plan la TRUE VECTOR SVG tu geometry (khong phai bitmap)
- [ ] 2 principal elevations tu structured geometry
- [ ] 1 key section tu structured geometry
- [ ] Site plan voi boundary, footprint, north arrow, scale
- [ ] Wall hierarchy visible (exterior nang hon interior)
- [ ] Dimensions: overall + key room dimensions
- [ ] Room tags: name + area
- [ ] Consistent title block family across all sheets
- [ ] Line weight hierarchy theo P1 deliverable spec
- [ ] Typography consistent across package

---

## 6. Thay doi ve positioning/wording

### Dung cho UI va export:
- "Xuat ho so thiet ke so bo" (Issue schematic package)
- "Ban trinh bay khach hang" (Client presentation set)
- "Revision A / Revision B"
- "Khong dung cho xin phep xay dung" (Not for permit or construction)

### KHONG dung:
- "Ho so thi cong" (Construction documents)
- "Ho so xin phep" (Permit set)
- "San sang nop" (Ready for submission)

---

## 7. Tom tat quyet dinh

| Cau hoi | Quyet dinh |
|---|---|
| P1 deliverable co dung khong? | Co, day la chuan dung cho thi truong residential architecture |
| Ap dung nguyen vao Phase 1 MVP? | KHONG - pha vo scope da chot trong 05-system-design.md |
| Cach ap dung? | Phased: Bac 1 (MVP nang cap PDF), Bac 2 (MVP+ full schematic package), Bac 3 (Phase 2 expansion) |
| Geometry upgrade khi nao? | Layer 1.5 o Sprint 9-10 (MVP+), Layer 2 o Phase 2 |
| Elevation/section khi nao? | Sprint 9-10 (MVP+), sau khi co Layer 1.5 geometry |
| Title block/sheet discipline khi nao? | Sprint 5-6 (MVP) - ap dung ngay cho PDF export |
| Market positioning? | "Schematic Design Package" - khong claim permit-ready |

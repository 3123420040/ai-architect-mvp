# Phase 3 - Checkpoint-by-Checkpoint Execution Plan

*Version: 1.0*
*Ngay tao: Apr 12, 2026*
*Audience: PM, Tech Lead, All Implementation Teams*
*Source: 00-market-standard-2d-output-requirements.md + 02-architecture-data-contract.md*

---

## 1. Tong quan Phase 3

### Timeline: 8 Checkpoints, ~24 weeks

```
CP-3.1  Brief & Typology Engine          [Week 1-3]    BE + AI
CP-3.2  Geometry Layer 2 + Migration     [Week 4-6]    BE + AI
CP-3.3  Drawing Engine Upgrade           [Week 7-10]   BE
CP-3.4  Schedules & Enhanced Dimensions  [Week 11-13]  BE
CP-3.5  DXF Export                       [Week 14-16]  BE
CP-3.6  IFC Foundation                   [Week 17-18]  BE + AI
CP-3.7  Frontend & Delivery Upgrade      [Week 12-18]  FE (parallel)
CP-3.8  QA, Benchmark & Launch           [Week 19-24]  All
```

### Teams

| Team | Headcount (de xuat) | Primary CPs |
|------|---------------------|-------------|
| BE Team | 2-3 engineers | CP-3.1 den CP-3.6 |
| AI Team | 1-2 engineers | CP-3.1, CP-3.2, CP-3.6 |
| FE Team | 1-2 engineers | CP-3.7 |
| QA | 1 engineer | CP-3.8 (nhung tham gia tu CP-3.3) |
| DevOps | 0.5 (part-time) | CP-3.8 infra |

### Prerequisite

- [ ] CP7 (Schematic Package) da SHIPPED va on dinh
- [ ] Layer 1.5 geometry da dung trong production >= 2 weeks
- [ ] Sheet composition engine da ship 2 elevations + 1 section
- [ ] Khong co P0 bugs tu Phase 2
- [ ] AutoCAD, DraftSight, and Solibri access da duoc xac nhan cho QA/validation

---

### Execution note

Phase 3 duoc chot la hardening-first phase cho baseline Phase 2. Moi checkpoint Phase 3 phai uu tien dong nhung khoang trong cua prerequisite checklist tren cung code path truoc khi tinh la hoan tat checkpoint.

## CP-3.1: Brief & Typology Engine (Week 1-3)

### Muc tieu
He thong nhan brief co typology, room program day du, assumption tracking, clarification gate.

### BE Team

| # | Task | Priority | Definition of Done |
|---|------|----------|-------------------|
| BE-3.1.1 | Extended brief schema (project_type, renovation_flag, survey_verified, room_priority, adjacency, privacy, daylight, parking, facade_direction, material_direction) | P0 | brief_json v2 schema validated |
| BE-3.1.2 | Source tagging system (confirmed / inferred / default) per brief field | P0 | Every brief field carries source tag |
| BE-3.1.3 | Typology router (brief.project_type -> planning rules) | P0 | 5 typologies active: townhouse, villa, apartment_reno, shophouse, home_office |
| BE-3.1.4 | Typology-specific brief templates (required fields differ per type) | P0 | Required field profile differs across the 5 supported typologies |
| BE-3.1.5 | Clarification gate API (check brief completeness vs target_package_type) | P0 | Returns missing required fields |
| BE-3.1.6 | Assumption exposure endpoint (list all inferred + default values before issue) | P0 | GET /versions/{id}/assumptions |
| BE-3.1.7 | Brief v1 -> v2 migration (existing projects compatible) | P0 | Old briefs get default source tags |

### AI Team

| # | Task | Priority | Definition of Done |
|---|------|----------|-------------------|
| AI-3.1.1 | LLM brief extraction upgrade (extract typology, adjacency, material direction from chat) | P0 | 80%+ accuracy on 20 test cases |
| AI-3.1.2 | Room program suggestion engine (infer missing rooms per typology) | P0 | Townhouse 4T suggests default program |
| AI-3.1.3 | Assumption inference pipeline (LLM infers unspecified values with confidence score) | P1 | Each inferred value has explanation |

### Demo CP-3.1
- User nhap brief qua chat: "Nha pho 5x20, 4 tang, 3 phong ngu, phong cach hien dai"
- He thong phan loai typology = townhouse, fill default program
- Show "Required clarifications" neu thieu info cho design_development package
- Show assumptions list voi source tags
- User confirm -> brief v2 ready

---

## CP-3.2: Geometry Layer 2 + Migration (Week 4-6)

### Muc tieu
geometry_json upgrade tu Layer 1.5 len Layer 2. Canonicalization pipeline extract full assemblies.

### BE Team

| # | Task | Priority | Definition of Done |
|---|------|----------|-------------------|
| BE-3.2.1 | Layer 2 JSON Schema design + validation function | P0 | validate_geometry_v2() works on 5 sample files |
| BE-3.2.2 | Wall assembly model (layers, materials, fire_rating, structural flag) | P0 | Schema + 3 wall type samples |
| BE-3.2.3 | Opening detail model (frame, glazing/panel, hardware, schedule_mark) | P0 | Schema + door/window samples |
| BE-3.2.4 | Room finish model (floor/wall/ceiling finish specs, plumbing, electrical) | P0 | Schema + 5 room type samples |
| BE-3.2.5 | Structural grid system | P1 | Grid axes renderable |
| BE-3.2.6 | Source tag on every entity (confirmed/inferred/default) | P0 | Validation rejects entity without source |
| BE-3.2.7 | Stable ID system (no reuse, cross-reference validation) | P0 | ID uniqueness enforced |
| BE-3.2.8 | Layer 1.5 -> Layer 2 data migration script | P0 | Old projects get default assemblies + "default" source tags |
| BE-3.2.9 | Geometry diff service (compare 2 versions at Layer 2 detail) | P1 | Show what changed between V2 and V3 |

### AI Team

| # | Task | Priority | Definition of Done |
|---|------|----------|-------------------|
| AI-3.2.1 | Canonicalization pipeline upgrade: extract wall assemblies from AI generation | P0 | Exterior vs interior walls correctly classified |
| AI-3.2.2 | Opening detail extraction: door/window size + position + type from floor plan | P0 | 85%+ correct placement |
| AI-3.2.3 | Room finish inference from style direction in brief | P1 | Suggest finishes per room type based on style |
| AI-3.2.4 | Typology-aware option generation (townhouse stacking, villa spreading) | P0 | Options vary meaningfully per typology |

### Demo CP-3.2
- Generate townhouse 4T -> geometry Layer 2 with wall assemblies, opening details, room finishes
- Every entity has source tag
- Schedule marks assigned (D01..D08, W01..W15)
- Old Layer 1.5 project still loads and exports correctly
- Geometry diff: "V3 vs V2: living room +2m2, D03 added"

---

## CP-3.3: Drawing Engine Upgrade (Week 7-10)

### Muc tieu
4 elevations, 2 sections, enhanced rendering, visual presets, and mandatory DD key detail sheets.

### BE Team

| # | Task | Priority | Definition of Done |
|---|------|----------|-------------------|
| BE-3.3.1 | ElevationRendererV2: 4 faces (S, N, E, W) | P0 | 4 SVG elevations from geometry |
| BE-3.3.2 | Material tags on elevations (from wall assembly) | P0 | Exterior finish labels visible |
| BE-3.3.3 | Schedule mark tags on elevations (D01, W01) | P0 | Marks match plan sheets |
| BE-3.3.4 | Grid overlay on plan + elevation sheets | P0 | Structural axes shown |
| BE-3.3.5 | SectionRenderer upgrade: 2 sections (A-A + B-B) | P0 | 2 SVG sections, correct cut hierarchy |
| BE-3.3.6 | Slab/roof detail in sections (from Layer 2 data) | P0 | Slab thickness, roof layers visible |
| BE-3.3.7 | Visual preset system (technical_neutral, client_presentation) | P0 | Same geometry, different annotation density + style |
| BE-3.3.8 | Floor plan renderer upgrade: wall poché, fixture detail, furniture blocks | P1 | Cut walls hatched, fixtures recognizable |
| BE-3.3.9 | Site plan upgrade: utilities, landscape zones, access points | P1 | Beyond basic boundary + footprint |
| BE-3.3.10 | Level markers on elevations + sections | P0 | Elevation values ("+0.45", "+4.05") |
| BE-3.3.11 | KeyDetailSheetRenderer: minimum 2 DD detail sheets from approved template set | P0 | A11/A12 detail sheets generated for issue packages |

### Demo CP-3.3
- Townhouse 4T -> full sheet set: Cover, Site, 4 Floor Plans, 2 Elevation sheets, 1 Section sheet, key detail sheets
- Visual presets: switch between "technical" and "client presentation" -> same geometry, different look
- Schedule marks D01/W01 visible on BOTH plan and elevation sheets
- Grid lines overlay on plans

---

## CP-3.4: Schedules & Enhanced Dimensions (Week 11-13)

### Muc tieu
Door/window/room schedules, full dimension chains, schedule sheets in package.

### BE Team

| # | Task | Priority | Definition of Done |
|---|------|----------|-------------------|
| BE-3.4.1 | DoorScheduleRenderer (SVG table + PDF integration) | P0 | All doors listed with mark, room, type, size, frame, panel, hardware |
| BE-3.4.2 | WindowScheduleRenderer (SVG table + PDF integration) | P0 | All windows listed with mark, room, type, size, sill, frame, glazing |
| BE-3.4.3 | RoomScheduleRenderer (SVG table + level subtotals + building total) | P0 | All rooms, finishes, areas, subtotals |
| BE-3.4.4 | Schedule sheet(s) in PDF package (A9 + A10) | P0 | Sheets added to combined PDF |
| BE-3.4.5 | Schedule CSV export (door.csv, window.csv, room.csv) | P1 | Downloadable, correct data |
| BE-3.4.6 | Schedule mark cross-validation (plan marks match schedule rows) | P0 | Automated check, block issue if mismatch |
| BE-3.4.7 | Enhanced DimensionEngine: 6 chain types | P0 | Overall, grid, wall, opening, room, vertical |
| BE-3.4.8 | Dimension placement rules (chain offset, spacing, text orientation) | P0 | No overlapping dimensions |
| BE-3.4.9 | Stair dimensions (riser x count = rise) | P0 | Correct calculation |
| BE-3.4.10 | Elevation vertical dimensions (floor levels + total height) | P0 | Consistent with plan level markers |

### Demo CP-3.4
- Package now has 12+ sheets including schedules and key detail sheets
- Door schedule: D01-D08, correct room references
- Window schedule: W01-W15, correct glazing data
- Room schedule: per-level subtotals, building total 320m2
- Dimension chains on floor plan: 4 levels (overall, grid, wall, opening)
- CSV download works, data matches schedule tables

---

## CP-3.5: DXF Export (Week 14-16)

### Muc tieu
DXF file mo duoc trong AutoCAD, LibreCAD, DraftSight voi correct geometry, layers, text, dimensions.

### BE Team

| # | Task | Priority | Definition of Done |
|---|------|----------|-------------------|
| BE-3.5.1 | ezdxf integration + 25+ layer setup | P0 | All layers created correctly per contract |
| BE-3.5.2 | Floor plan DXF: walls, openings, fixtures, room tags | P0 | Opens in AutoCAD correctly |
| BE-3.5.3 | Wall poché/hatching in DXF (cut walls filled) | P0 | Exterior walls hatched |
| BE-3.5.4 | Opening symbols in DXF (door swings, window lines) | P0 | Standard CAD symbols |
| BE-3.5.5 | Elevation DXF: 4 faces in model space | P0 | Geometry correct |
| BE-3.5.6 | Section DXF: cut vs beyond correctly differentiated | P0 | Cut = heavy, beyond = light |
| BE-3.5.7 | Dimension entities (proper dimstyle, editable in CAD) | P0 | DIMENSION entities, not exploded text |
| BE-3.5.8 | Text styles setup (AI_ARCH_BODY, AI_ARCH_TITLE, AI_ARCH_DIM) | P0 | Consistent fonts |
| BE-3.5.9 | Paper space layouts with viewports + correct scale | P0 | Each sheet as named layout at 1:100/1:200 |
| BE-3.5.10 | Title block as DXF block/xref | P0 | Reusable across layouts |
| BE-3.5.11 | Schedule tables in DXF (text blocks or MText tables) | P1 | Readable in CAD |
| BE-3.5.12 | DXF validation: test in AutoCAD + LibreCAD + DraftSight | P0 | No critical errors in all 3 |

### Demo CP-3.5
- Click "Export DXF" -> .dxf file downloaded
- Open in AutoCAD: 25+ layers, correct colors/lineweights
- Model space: floor plans + elevations + sections at 1:1
- Paper space: named layouts (A0-COVER, A2-TANG1, A6-ELEV-SN, etc.)
- Dimensions editable (click dim -> modify in CAD)
- Wall hatching correct
- KTS confirm: "Toi co the lam viec tren file nay"

---

## CP-3.6: IFC Foundation (Week 17-18)

### Muc tieu
IFC4X3 file mo duoc trong BIM viewer voi correct spatial structure.

### BE Team

| # | Task | Priority | Definition of Done |
|---|------|----------|-------------------|
| BE-3.6.1 | IfcOpenShell integration + IFC4X3 project setup | P0 | Valid IFC file created |
| BE-3.6.2 | IfcBuildingStorey: 1 per level with correct elevation | P0 | Storey hierarchy correct |
| BE-3.6.3 | IfcWall / IfcWallStandardCase: all walls with type | P0 | Walls visible in viewer |
| BE-3.6.4 | IfcDoor: all doors with position + size | P0 | Doors in correct walls |
| BE-3.6.5 | IfcWindow: all windows with position + size | P0 | Windows in correct walls |
| BE-3.6.6 | IfcSpace: all rooms with boundary + name + area | P0 | Rooms clickable in viewer |
| BE-3.6.7 | IfcSlab: per level | P1 | Floor slabs present |
| BE-3.6.8 | Basic property sets (Pset_WallCommon, Pset_DoorCommon, Pset_SpaceCommon) | P1 | Properties queryable in viewer |
| BE-3.6.9 | Quantity sets (Qto_WallBaseQuantities, Qto_SpaceBaseQuantities) | P1 | Areas and lengths correct |
| BE-3.6.10 | IFC validation: Solibri Anywhere + BIMvision + IfcOpenShell validate | P0 | No critical errors |

### AI Team

| # | Task | Priority | Definition of Done |
|---|------|----------|-------------------|
| AI-3.6.1 | Wall type inference for IFC classification (IfcWallType) | P1 | Correct wall type assignment |

### Demo CP-3.6
- Click "Export IFC" -> .ifc file downloaded
- Open in Solibri Anywhere: building with 4 storeys visible
- Click room -> name + area shown
- Click wall -> type (exterior/interior) shown
- UI labels IFC as "Limited-scope interoperability export (foundation)"

---

## CP-3.7: Frontend & Delivery Upgrade (Week 12-18, parallel)

### Muc tieu
Frontend ho tro package browser, visual presets, schedule view, extended export UI.

### FE Team

| # | Task | Priority | Definition of Done |
|---|------|----------|-------------------|
| FE-3.7.1 | Package browser component (sheet thumbnails sidebar + main SVG view) | P0 | Navigate 12+ sheets smoothly |
| FE-3.7.2 | Sheet viewer upgrade: zoom, pan, crisp vector on all sheet types | P0 | Elevations + sections render correctly |
| FE-3.7.3 | Visual preset selector (technical / client) | P0 | Switch preset, sheets re-render |
| FE-3.7.4 | Schedule sheet viewer (table rendering in web) | P0 | Door/window/room schedules viewable |
| FE-3.7.5 | Export dialog upgrade: DXF + IFC options, per-format progress | P0 | Shows progress for each format |
| FE-3.7.6 | Assumption review UI (before issue: show confirmed/inferred/default counts) | P0 | User can review + confirm assumptions |
| FE-3.7.7 | Clarification gate UI (show missing required fields, block generate) | P0 | User must fill required fields |
| FE-3.7.8 | Brief v2 form (typology selector, room program editor, material direction) | P0 | All new brief fields editable |
| FE-3.7.9 | Package issue flow (draft -> review -> issued) with KTS approval gate | P0 | Cannot issue without KTS approval |
| FE-3.7.10 | DEGRADED preview state and issue blocking UI | P0 | Preview allowed, issue disabled until quality gates pass |
| FE-3.7.11 | Delivery UI: categorize exports (presentation / technical / CAD handoff / interop) | P1 | Clear labels per file type |
| FE-3.7.12 | Contact-sheet preview (thumbnail of all sheets in 1 image) | P1 | For gallery/selection UX |

### Demo CP-3.7
- Full package browser: navigate 12+ sheets, zoom into floor plan detail
- Switch visual preset: technical -> client presentation -> back
- Assumption review screen before issue
- Export dialog: checkboxes for PDF, SVG, DXF, IFC, CSV
- KTS clicks "Issue Package" -> approval gate -> status "issued"
- Package in degraded preview clearly shows issue blocked state

---

## CP-3.8: QA, Benchmark & Launch (Week 19-24)

### Muc tieu
Benchmark library, automated validation, visual regression, launch readiness.

### All Teams

| # | Task | Priority | Owner | Definition of Done |
|---|------|----------|-------|-------------------|
| QA-3.8.1 | Benchmark project library: 3 projects (townhouse 4T, villa 3T, apartment reno) | P0 | QA | 3 reference packages frozen |
| QA-3.8.2 | Automated schema validation (geometry v2, manifest v2) | P0 | BE | CI pipeline validates every package |
| QA-3.8.3 | Cross-sheet consistency checker (room names, level names, schedule marks match across all sheets) | P0 | BE | Automated, blocks issue if mismatch |
| QA-3.8.4 | SVG validity checker (well-formed SVG, correct viewBox) | P0 | BE | Part of CI |
| QA-3.8.5 | DXF openability test (automated: open in LibreCAD headless, check layer count) | P0 | BE | CI integration |
| QA-3.8.6 | IFC validation test (IfcOpenShell validate, check entity counts) | P0 | BE | CI integration |
| QA-3.8.7 | Export manifest completeness check (manifest references match actual files) | P0 | BE | Automated |
| QA-3.8.8 | Visual regression tests (screenshot compare per sheet type, 5% tolerance) | P0 | QA | Playwright + Percy or similar |
| QA-3.8.9 | Human review checklist template | P0 | QA | PDF checklist for manual review |
| QA-3.8.10 | Performance testing (full package < 120s for 4-floor townhouse) | P0 | BE | Load test passes |
| QA-3.8.11 | Regression testing (Layer 1.5 projects still export correctly) | P0 | BE | All old projects pass |
| QA-3.8.12 | KTS user testing: 3 architects review exported DXF + PDF | P0 | PM | Written feedback collected |
| QA-3.8.13 | Security audit (exported files dont leak internal data) | P0 | BE | No internal IDs, no server paths in exports |
| QA-3.8.14 | Documentation: update all implementation docs for Phase 3 | P1 | All | README, API docs, deployment guide |
| QA-3.8.15 | Production deployment + monitoring | P0 | DevOps | All new services running, Sentry configured |

---

## 2. Acceptance Criteria Matrix

### Package-level (AC-PACK)

| # | Criteria | Automated? | Owner |
|---|----------|-----------|-------|
| AC-PACK-001 | Package chua tat ca sheet types theo deliverable preset | Yes | BE |
| AC-PACK-002 | Tat ca sheets derive tu cung 1 locked canonical version | Yes | BE |
| AC-PACK-003 | Title block metadata consistent across all sheets | Yes | BE |
| AC-PACK-004 | Dimensioning hien dien (khong chi overall width/depth) | Manual | QA |
| AC-PACK-005 | Plans, elevations, sections, schedules dong bo (room names, levels, marks) | Yes | BE |
| AC-PACK-006 | Package KHONG trong nhu screenshot wrapper | Manual | QA |
| AC-PACK-007 | Manifest matches actual issued files | Yes | BE |

### Sheet-level (AC-SHEET)

| # | Sheet | Must include | Check |
|---|-------|-------------|-------|
| AC-SHEET-001 | Cover | Title, project name, revision, date, index, disclaimer, preview | Manual |
| AC-SHEET-002 | Site | Boundary, footprint, north arrow, scale, site-specific info | Manual |
| AC-SHEET-003 | Floor plan | Wall hierarchy, openings, stairs, fixtures, room tags, areas, multiple dim strings | Manual + Auto |
| AC-SHEET-004 | Elevation | Building outline, level cues, openings, roof/parapet, facade/material | Manual |
| AC-SHEET-005 | Section | Cut hierarchy, vertical relationships, slab/roof, heights/levels | Manual |
| AC-SHEET-006 | Schedule | Readable table, stable marks, values match canonical model | Auto |

### Export-level (AC-EXPORT)

| # | Format | Criteria | Check |
|---|--------|----------|-------|
| AC-EXPORT-001 | PDF | Printable, complete, page order correct | Manual |
| AC-EXPORT-002 | SVG | Crisp, structured, zoomable, annotatable | Manual |
| AC-EXPORT-003 | DXF | Opens in AutoCAD + LibreCAD + DraftSight, layers + text + dims correct | Auto + Manual |
| AC-EXPORT-004 | IFC | Opens in Solibri + BIMvision, spatial structure correct | Auto + Manual |
| AC-EXPORT-005 | Manifest | References all files accurately, metadata complete | Auto |
| AC-EXPORT-006 | CSV | Correct data, matches schedule tables, importable to Excel | Auto |

### Quality gates (NFR)

| # | Gate | When | Block issue? |
|---|------|------|-------------|
| NFR-Q-001 | Schema validation pass | Before export | Yes |
| NFR-Q-002 | Cross-sheet consistency pass | Before export | Yes |
| NFR-Q-003 | DXF openability pass | After export | Yes |
| NFR-Q-004 | IFC validation pass | After export | Yes |
| NFR-Q-005 | Manifest completeness pass | After export | Yes |
| NFR-Q-006 | Visual regression pass (no > 5% diff from baseline) | Before release | Yes |
| NFR-Q-007 | Performance pass (< 120s total) | Before release | Yes |
| NFR-Q-008 | KTS user testing feedback positive | Before launch | Yes (launch gate) |

---

## 3. Merge & Release Strategy

### Branch strategy

```
main (production)
  |
  +-- phase-3/cp-3.1-brief-typology
  +-- phase-3/cp-3.2-geometry-layer2
  +-- phase-3/cp-3.3-drawing-engine
  +-- phase-3/cp-3.4-schedules-dimensions
  +-- phase-3/cp-3.5-dxf-export
  +-- phase-3/cp-3.6-ifc-foundation
  +-- phase-3/cp-3.7-frontend-delivery    (long-running, parallel)
  +-- phase-3/cp-3.8-qa-launch
```

### Merge order

| CP | Merge to main | Prerequisite | Merge owner |
|---|--------------|-------------|-------------|
| CP-3.1 | After CP-3.1 demo pass | None (first) | BE Tech Lead |
| CP-3.2 | After CP-3.2 demo pass | CP-3.1 merged | BE Tech Lead |
| CP-3.3 | After CP-3.3 demo pass | CP-3.2 merged | BE Tech Lead |
| CP-3.4 | After CP-3.4 demo pass | CP-3.3 merged | BE Tech Lead |
| CP-3.5 | After CP-3.5 demo pass | CP-3.4 merged | BE Tech Lead |
| CP-3.6 | After CP-3.6 demo pass | CP-3.5 merged | BE Tech Lead |
| CP-3.7 | After CP-3.7 demo pass | CP-3.3 merged (minimum) | FE Tech Lead |
| CP-3.8 | Release branch | All CPs merged | PM + Tech Lead sign-off |

### Feature flags

```python
PHASE_3_FLAGS = {
    "TYPOLOGY_ENGINE": True,          # CP-3.1
    "GEOMETRY_LAYER_2": True,         # CP-3.2
    "FOUR_ELEVATIONS": True,          # CP-3.3
    "SCHEDULES": True,                # CP-3.4
    "DXF_EXPORT": True,              # CP-3.5
    "IFC_EXPORT": True,              # CP-3.6
    "VISUAL_PRESETS": True,           # CP-3.3
    "PACKAGE_CENTRIC_ISSUE_FLOW": True,
    "DEGRADED_PREVIEW_BLOCK_ISSUE": True,
    "BRANDED_STUDIO": False,          # Not a launch preset
    "APARTMENT_RENO_TYPOLOGY": True,  # In scope with manual QA until benchmark pack matures
    "SHOPHOUSE_TYPOLOGY": True,       # In scope with manual QA until benchmark pack matures
    "HOME_OFFICE_TYPOLOGY": True,     # In scope with manual QA until benchmark pack matures
}
```

---

## 4. Human Review Checklist (Manual QA)

Dung cho moi benchmark project truoc release:

### A. Graphic hierarchy
- [ ] Cut walls heavier than beyond
- [ ] Exterior walls heavier than interior
- [ ] Fixtures lighter than walls
- [ ] Furniture lightest
- [ ] Dashed lines for overhead/hidden

### B. Typography
- [ ] 1 font family throughout
- [ ] Sheet titles > room tags > dimensions > notes (size hierarchy)
- [ ] No random font changes
- [ ] No cropped text

### C. Annotations
- [ ] Room tags: name + area visible, no overlap with walls
- [ ] Dimensions: multiple chain levels, legible
- [ ] Schedule marks: D01/W01 visible on plans AND elevations
- [ ] Section/elevation markers on plan sheets

### D. Title blocks
- [ ] Present on every sheet
- [ ] Correct project name, sheet number, date, revision
- [ ] KTC KTS wordmark and approved preset treatment applied correctly
- [ ] Scale notation present
- [ ] Disclaimer visible on cover

### E. Cross-sheet consistency
- [ ] Room "Phong khach" called same name on plan + schedule
- [ ] Level "+4.05" matches between plan, elevation, section
- [ ] D01 on plan = D01 on elevation = D01 in door schedule
- [ ] Total area on room schedule = sum of per-room areas
- [ ] Package with `DEGRADED` label cannot be issued

### F. Export files
- [ ] PDF: all pages present, correct order
- [ ] DXF: opens in AutoCAD without errors
- [ ] IFC: opens in BIM viewer, rooms clickable
- [ ] CSV: data matches schedule tables
- [ ] Manifest: all files referenced, correct metadata

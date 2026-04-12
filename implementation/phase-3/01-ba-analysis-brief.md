# Phase 3 - BA Analysis Brief

*Version: 1.0*
*Ngay tao: Apr 12, 2026*
*Audience: PM, BA, Product Owner, Stakeholders*
*Source: 00-market-standard-2d-output-requirements.md*

---

## 1. Quyet dinh kinh doanh can tra loi

> Phase 3 nay can xuat ra deliverable gi de khach hang tin tuong day la san pham kien truc chuyen nghiep, KHONG phai AI concept tool?

---

## 2. Vi tri deliverable tren thi truong

### 2.1 Target market

| Phan khuc | Mo ta |
|-----------|-------|
| **Primary** | KTS nha o, cong ty thiet ke nha, design-build team, doi thiet ke preconstruction |
| **Secondary** | Chu nha tra phi, PM du an, drafter, collaborator noi/ngoai that, CAD/BIM operator |

### 2.2 Deliverable grade

```
[Concept board] --> [Schematic set] --> [DESIGN DEVELOPMENT] --> [Permit set] --> [Construction docs]
                                              ^
                                              |
                                     PHASE 3 TARGET
```

Phase 3 phai dat **"design-development-grade"** - manh hon schematic, chua claim permit/construction.

### 2.3 Cam nhan cua nguoi dung

Khach hang phai noi duoc:
- "Package nay nghiem tuc"
- "Plans, elevations, sections, schedules dong bo nhau"
- "File export dung duoc trong workflow thuc te"
- "Chi tiet du de review design va collaboration"

### 2.4 Khong duoc claim

| Khong claim | Ly do |
|-------------|-------|
| Permit-ready | Chua co jurisdiction-specific compliance |
| Stamped/sealed | Khong co licensed architect signing |
| Construction-ready | Chua co MEP, structural, framing |
| Engineer-reviewed | Khong co consultant coordination |
| Code-compliant | Chua validate theo building code cu the |

---

## 3. Scope Phase 3

### 3.1 Trong scope

| Area | Chi tiet |
|------|----------|
| Brief & Design Intent | Structured brief voi typology, room program, adjacency, material direction |
| Typology | Townhouse, villa, apartment reno, shophouse, home-office (5 loai) |
| Canonical Geometry | Layer 2: wall assemblies, material properties, detailed openings, finishes |
| Drawing Sheets | Cover, site, floor plans, 4 elevations, 2+ sections, schedules, minimum DD key detail sheets |
| Annotations | Full dimension chains, room tags, schedule marks, symbol families |
| Graphic Standards | Line weight hierarchy, typography system, visual presets |
| Schedules | Door, window, room/area - tu canonical geometry |
| Export | PDF + SVG + DXF + IFC (foundation) + CSV + manifest JSON |
| Versioning | Immutable issue records, revision chains, lineage tracking |
| Quality Gates | Automated + visual regression + manual review checklist |

### 3.2 Ngoai scope

| Khong lam | Phase nao? |
|-----------|-----------|
| Permit documentation package | Phase 4+ |
| Structural engineering plans | Phase 4+ |
| MEP plans (dien, nuoc, HVAC) | Phase 4+ |
| Reflected ceiling plans | Phase 4+ |
| Framing / foundation plans | Phase 4+ |
| Full construction detail library / permit-grade detail set | Phase 4+ |
| Consultant coordination package | Phase 4+ |
| Stamped/sealed workflow | Phase 4+ |
| Building code automation theo jurisdiction | Phase 4+ |

---

## 4. Yeu cau Brief & Design Intent

### 4.1 Brief phai co nhung gi

Phase 2 (da co): project name, lot size, orientation, floor count, room list, style, budget, special requests.

**Phase 3 THEM:**

| Field moi | Vi du | Tai sao |
|-----------|-------|---------|
| project_type | townhouse, villa, apartment_reno, shophouse, home_office | Khac nhau ve planning logic |
| renovation_flag | new_build / renovation | Anh huong constraints |
| survey_verified | true / false | Phan biet data xac nhan vs gia dinh |
| room_priority_ranking | [living > kitchen > master > ...] | Xep uu tien khi trade-off |
| adjacency_constraints | "kitchen next to dining" | Planning engine can |
| privacy_constraints | "master isolated from guest" | Planning engine can |
| daylight_preference | per room: high/medium/low | Anh huong opening placement |
| parking_type | garage / covered / none | Anh huong tang tret |
| facade_direction | modern_glass / traditional / industrial | Anh huong elevation render |
| material_direction | {exterior: "brick+glass", interior: "wood+white"} | Anh huong schedule + elevation |
| target_package_type | schematic / design_development / cad_handoff | Quyet dinh detail density |
| expected_formats | [pdf, svg, dxf, ifc] | Quyet dinh export pipeline |
| assumption_rules | "default 3.3m floor height if not specified" | Minh bach gia dinh |

### 4.2 Phan biet du lieu

**Bat buoc:** Moi field trong brief phai co tag:

| Tag | Nghia | Vi du |
|-----|-------|-------|
| `confirmed` | User nhap va xac nhan | "Lot width = 5m" (tu survey) |
| `inferred` | AI suy ra tu context | "Kitchen area ~12m2" (tu budget + room count) |
| `default` | Gia tri mac dinh cua he thong | "Floor height = 3.3m" (default cho nha pho) |

**Truoc khi issue package:** He thong phai show tat ca assumptions chua confirmed va cho user xac nhan hoac sua.

### 4.3 Clarification gate

Neu brief KHONG du thong tin cho muc output da chon (vd: chon "design_development" nhung chua co material direction) -> he thong phai hien "Required clarifications" truoc khi cho generate.

---

## 5. Yeu cau Typology

### 5.1 5 Typology bat buoc

| # | Typology | Dac trung planning |
|---|----------|-------------------|
| 1 | **Townhouse / Nha pho** | Hep (3-5m), nhieu tang (3-5), cau thang trung tam, gieng troi, mat tien 1 huong |
| 2 | **Villa / Biet thu** | Rong, 2-3 tang, san vuon, 2-4 mat thoang, garage, ho boi optional |
| 3 | **Apartment renovation** | Constraint co san (tuong chiu luc, ong ky thuat), doi noi that chinh |
| 4 | **Shophouse / Mixed-use** | Tang tret thuong mai, tang tren nha o, loi di rieng, mat tien rong |
| 5 | **Home-office hybrid** | Chia zone lam viec/song, am thanh, loi vao rieng, phong hop nho |

### 5.2 Moi typology can gi?

Moi typology phai co:
- Brief template rieng (fields bat buoc khac nhau)
- Planning rules rieng (stacking, zoning, circulation)
- Default values rieng (floor height, setback, material)
- Elevation style hints rieng

### 5.3 Option generation

Planning engine phai tao options khac nhau THUC SU (khong chi doi mau):
- Khac stacking strategy (bep tret vs bep lau 1)
- Khac stair placement (giua vs hong)
- Khac front-core-rear zoning
- Khac service placement (WC cluster vs distributed)
- Khac facade openness (kinh nhieu vs tuong nhieu)
- Khac terrace/yard relationship

Moi option phai co **machine-readable explanation**:
```json
{
  "option_id": "A",
  "strategy": {
    "program_allocation": "kitchen_ground_floor",
    "circulation": "central_stair_with_void",
    "zoning": "public_front_private_rear",
    "service_placement": "clustered_core",
    "facade_approach": "glass_dominant_south"
  },
  "assumptions": [
    {"field": "floor_height", "value": 3.3, "source": "default"}
  ]
}
```

---

## 6. Graphic & Presentation Standards

### 6.1 Line weight hierarchy (bat buoc)

| Element | Weight | Layer (DXF) |
|---------|--------|-------------|
| Section cut / wall poché | Heaviest (0.5mm) | A-SECT-CUT |
| Exterior walls | Heavy (0.35mm) | A-WALL-EXTR |
| Interior walls | Medium (0.25mm) | A-WALL-INTR |
| Openings | Medium-light (0.18mm) | A-DOOR, A-GLAZ |
| Fixtures | Light (0.13mm) | A-FLOR-FIXT |
| Furniture | Lightest (0.09mm) | A-FLOR-FURN |
| Annotations/dimensions | Light (0.13mm) | A-ANNO-* |
| Hidden/overhead | Dashed, light | A-FLOR-OVHD |

### 6.2 Typography

| Element | Size | Style |
|---------|------|-------|
| Sheet title | 5mm | Bold, UPPERCASE |
| Room tag - name | 3mm | Medium, Title Case |
| Room tag - area | 2.5mm | Regular |
| Dimension text | 2.5mm | Regular |
| Notes | 2mm | Regular |
| Title block text | 2-3mm | Regular |

**Rule:** 1 font family duy nhat (Arial hoac tuong duong). Toi da 2 size levels chenh nhau tren 1 sheet.

### 6.3 Visual presets

| Preset | Muc dich | Khac biet |
|--------|---------|-----------|
| **Technical neutral** | Handoff CAD, review ky thuat | Trang den, khong color fill, max annotation |
| **Client presentation** | Trinh bay khach hang | Nhe annotation, color fill rooms, material hints |
| **Branded studio** | Studio KTS branding | Logo, accent color, custom title block |

Tat ca presets dung CUNG canonical geometry. Chi khac annotation density va style.

---

## 7. Delivery & Review Requirements

### 7.1 Package = 1 issue set, KHONG phai list files

UI phai show package nhu 1 bo ho so co cau truc:
- Sheet browser (thumbnail sidebar + main view)
- Cover sheet summary
- Sheet-by-sheet navigation
- Phan loai: presentation / technical / CAD handoff / interop

### 7.2 Review truoc khi issue

- KTS phai review + annotate truoc khi package status = "issued"
- Annotation va issue gating BAT BUOC
- "Draft" package co the preview nhung KHONG duoc share voi client

### 7.3 Revision behavior

- Issued package = IMMUTABLE
- Revision moi = package moi (Revision B, C...)
- Revision label phai dong bo: title block, manifest, delivery UI, handoff bundle

---

## 8. Locked Decisions and Scope Freeze

These decisions are LOCKED for the Phase 3 documentation set and are normalized in `04-phase-3-scope-lock.md`.

| Area | Locked decision | Implementation consequence |
|------|-----------------|----------------------------|
| Phase execution mode | Phase 3 is a hardening-first phase for the Phase 2 baseline | Checkpoints must close remaining prerequisite gaps on the live code path |
| Typology catalog | Phase 3 supports townhouse, villa, apartment renovation, shophouse, and home-office | Brief v2, planning engine, QA, and exports must accept all 5 typologies |
| Release quality tier | Townhouse and villa are benchmark-critical in wave 1; the remaining 3 typologies require manual QA until benchmark packs are frozen | QA sequencing can prioritize 2 core typologies without removing the other 3 from scope |
| Deliverable presets | Launch presets are `technical_neutral` and `client_presentation` | `branded_studio` is not a release preset for this phase |
| DXF contract | Use the full architecture contract: paper space, editable dimensions, hatching, and 25+ layers | DXF becomes a real downstream handoff artifact |
| IFC contract | Adopt the architecture contract as written | IFC4x3, typed entities, and validation are in-scope |
| Detail sheets | Phase 3 includes mandatory but limited DD key detail sheets; this does NOT expand to a full construction-detail library | Minimum DD key details must exist on every issued package |
| Dimensioning strategy | Rule-based only in Phase 3 | No user-adjustable dimension editor in this phase |
| Workflow | Replace the current version-centric flow with package-centric `draft -> review -> issued`, with mandatory KTS approval | Package issue becomes the primary release event |
| Degraded mode | Preview exports may be labeled `DEGRADED`, but issue is blocked until quality gates pass | Teams can inspect unfinished output without shipping it |
| Rollout policy | Phase 3 applies to new projects created after the feature flag opens | No automatic migration requirement for existing projects in this phase |
| Brand system | Use KTC KTS as the fixed studio identity for Phase 3 issued packages | Title block, disclaimers, presets, and sheet branding must align to one standard |

---

## 9. Risk Assessment

| Risk | Xac suat | Impact | Mitigation |
|------|----------|--------|------------|
| Typology engine chua du tot cho 5 loai | Cao | Package chua dung typology = mat tin tuong | Uu tien benchmark coverage cho townhouse + villa, dung manual QA gate cho 3 typology con lai den khi benchmark pack du |
| Brief khong du chi tiet -> output yeu | Cao | Package trong so sai, thieu dimension | Clarification gate bat buoc. Block generate neu brief thieu |
| DXF khong mo duoc tren CAD tools | Trung binh | KTS khong dung duoc file | Test voi 3+ CAD tools. Chon format R2018 (compatible rong) |
| Detail sheet scope mo rong qua muc DD | Trung binh | Tre scope, nham sang permit/construction package | Gioi han detail scope o muc key DD details, khong lam full construction detail library |
| Schedule marks khong dong bo giua sheets | Trung binh | Mat chuyen nghiep | Automated cross-check truoc khi issue |
| Visual quality khong dat "professional" | Cao | Khach hang khong tin tuong | Visual regression tests + benchmark library + manual QA checklist |
| Over-promising design development khi chua du | Trung binh | Legal/commercial risk | Disclaimer text bat buoc. KHONG dung tu "permit" hay "construction" |

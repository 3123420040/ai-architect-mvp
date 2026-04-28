# 00 — Context

## 1. Van de kinh doanh

MVP dat Phase 1 goals (production-like 5-loop pass, public production candidate tren `kts.blackbirdzzzz.art` — xem [15-ecp-execution-status.md](../../../phase-1/15-ecp-execution-status.md)). Hai diem dau cua san pham van la:

1. **Revision loop dai.** KTS go feedback text → AI regenerate full design → mat 1 vong GPU per chinh sua nho. Target Phase 1 la < 3 vong revision, chua dat on dinh vi moi chinh sua nho (doi wall, doi noi that) deu tra mot vong regenerate.
2. **3D viewer khong du thong tin.** Hien dung Google `<model-viewer>` load qua CDN — chi orbit/zoom, khong co level stacked/exploded, khong highlight room, khong chinh sua duoc. KTS va khach hang khong co cong cu "tuong tac" voi thiet ke.

## 2. Co hoi

Pascal editor (`pascalorg/editor`, MIT) la 3D building editor dung React Three Fiber + WebGPU, co san:

- Scene graph kien truc: walls (mitering + cutouts), slabs, ceilings, rooms/zones, items placement.
- Level visualization stacked / exploded / solo.
- Undo/redo qua `zundo`.
- CSG qua `three-bvh-csg`.

Tich hop Pascal vao san pham tao ra 3 value loops:

| Loop | Truoc | Sau |
|------|-------|-----|
| Chinh sua nho (doi wall, move item) | Text feedback → GPU regenerate (~ phut, ton GPU) | KTS edit scene truc tiep → save revision (~ giay, khong GPU) |
| Client presentation | Orbit/zoom GLB | Level toggle, room zones, walkthrough |
| Bridge sang Phase 2 export | model_url GLB → khong reversible | Scene graph → derive DXF/IFC tu nodes |

## 3. Stakeholders

| Role | Quan tam |
|------|----------|
| Chu san pham | Revision cycle < 3, GPU cost per project giam, demo client an tuong hon |
| KTS reviewer | Cong cu chinh sua truc tiep, giam phu thuoc AI cho chinh sua nho |
| Khach hang | 3D view ro rang hon (levels, rooms), khong con "hinh 3D mu" |
| Engineering | Canonical-first bao toan, khong lock-in Pascal scene |

## 4. Constraints

- **Phase 2 locked** theo [implementation/11-phase2-layer2-full-deliverable.md](../../../../implementation/11-phase2-layer2-full-deliverable.md). CP7 la sub-track song song, KHONG lam cham cp1-geometry-layer2 → cp6-integration-qa.
- **Web app stack:** Next.js 16.2, React 19.2, tailwind v4. Hien KHONG co three.js / R3F deps — Pascal them deps lon, phai xet bundle impact va browser compat.
- **WebGPU requirement:** Pascal chinh dung WebGPU. Safari/Firefox cu chua ho tro day du → phai giu fallback.
- **License:** Pascal MIT → OK de vendor/fork; phai giu file LICENSE upstream va update NOTICE.
- **Canonical geometry:** Phase 2 CP1 dang nang `geometry_json` len Layer 2. CP7 PHAI chay tren Layer 2; KHONG thiet ke adapter cho Layer 1.

## 5. Success metrics

| Metric | Baseline | Target sau CP7 |
|--------|----------|----------------|
| Revision cycles per approved project | 3-5 (Phase 1 thuc te) | < 3, voi ≥ 40% revision la "pascal_edit" source (khong GPU) |
| GPU compute per project (minutes) | X (do tren staging 4 tuan) | Giam ≥ 30% |
| Viewer session tai client demo | "Thoi gian xem" trung binh Y phut | Tang ≥ 50% (level toggle + room highlight) |
| KTS satisfaction (internal survey) | — | ≥ 4/5 voi cau "cong cu chinh sua 3D da du" |

## 6. Non-goals

- **KHONG** thay ca 2D floor plan authoring surface trong CP7. 2D van do GPU pipeline sinh.
- **KHONG** export DXF/IFC tu Pascal trong CP7 — viec nay thuoc CP4/CP5 Phase 2 voi canonical geometry.
- **KHONG** mo edit cho client-side (share link). Client van xem readonly.
- **KHONG** chuyen toan bo viewer mac dinh sang Pascal trong CP7 — flag mac dinh off, rollout dan.

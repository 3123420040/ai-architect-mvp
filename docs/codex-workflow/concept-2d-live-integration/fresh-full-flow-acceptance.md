# Fresh Full-Flow Acceptance - Concept 2D Live Integration

Date: 2026-04-30

Decision: PASS

## Scope

- Flow: browser UI from intake brief lock through design generation, review approval, Professional Deliverables generation, Review UI verification, Delivery UI verification, and artifact inspection.
- API commit under test: `e273bb1 feat(concept-2d): harden live package quality`
- Web commit under test: `4906e71 fix(concept-2d): clean live delivery UI states`
- Docker runtime: rebuilt with `docker compose -f docker-compose.local.yml up -d --build` before acceptance.

## Fresh UI Flow Evidence

- User: `ui-check-1777478162@example.com`
- Project id: `954ed846-ce1d-4974-8bd7-a6d823c04505`
- Project name: `Fix Intake Verification 5x20`
- Selected version id: `7b89f8e5-7cef-450a-a2bc-f115e08df32e`
- Brief entered through UI: `Nhà phố 5x20m hướng Nam, 3 tầng, 3 phòng ngủ, 3 WC, phong cách modern minimal warm, ít bảo trì, nhiều lưu trữ, ngân sách 4 tỷ, hoàn thành trong 6 tháng`
- Intake summary verified:
  - Lot: `5.0m x 20.0m`
  - Orientation: `hướng Nam`
  - Style: `Tối giản ấm`
  - Program: `3 tầng, 3 phòng ngủ, 3 WC`
  - Budget: `4.0 tỷ VND`
  - Timeline: `6 tháng`
- Designs generated from UI: 3 options.
- Selected/approved option: V3, `Phương án ưu tiên gara`.
- Review state: V3 locked.
- Professional Deliverables job: created from the Review UI and completed.

## Review UI Acceptance

- URL: `http://localhost:3000/projects/954ed846-ce1d-4974-8bd7-a6d823c04505/review`
- Browser console errors: 0
- Network errors seen during final Review verification: 0
- Professional Deliverables status: `Một phần`
- Progress: `Ready`, `100%`
- Concept 2D package status: `Sẵn sàng`
- PDF link present: yes
- DXF sheet links present: 10/10
- Quality report links present: yes
- Expected partial reason: local DWG clean-open skipped because ODA/DWG converter is unavailable.

## Delivery UI Acceptance

- URL: `http://localhost:3000/projects/954ed846-ce1d-4974-8bd7-a6d823c04505/delivery`
- Browser console errors: 0
- Network errors seen during final Delivery verification: 0
- Professional Deliverables panel present: yes
- Concept 2D package status: `Sẵn sàng`
- PDF link present: yes
- DXF sheet links present: 10/10
- Quality report links present: yes
- Additional artifacts present: GLB, FBX, USDZ, MP4
- DWG row is readable and not duplicated:
  - `DWG`
  - `skipped because ODA/DWG converter is unavailable: ODA converter unavailable locally; CI runs the required DWG audit`
- Presentation 3D panel does not cause 404 probes; it remains explicitly `Chưa tạo`.

## Artifact Evidence

- PDF URL: `http://localhost:18000/media/professional-deliverables/projects/954ed846-ce1d-4974-8bd7-a6d823c04505/versions/7b89f8e5-7cef-450a-a2bc-f115e08df32e/2d/bundle.pdf`
- Local downloaded PDF evidence: `output/concept-2d-acceptance-audit/fresh-full-flow-bundle.pdf`
- Rendered PDF page PNGs: `output/concept-2d-acceptance-audit/fresh-full-flow-pages/`
- Delivery screenshot: `output/concept-2d-acceptance-audit/fresh-full-flow-delivery.png`
- Artifact quality report: `output/concept-2d-acceptance-audit/fresh-full-flow-artifact-quality-report.json`

PDF inspection:

- Page count: 10
- All pages render nonblank.
- Minimum non-white pixels at half-scale: 10128
- Required sheet tokens present:
  - `A-000`
  - `A-100`
  - `A-101-F1`
  - `A-101-F2`
  - `A-101-F3`
  - `A-201`
  - `A-301`
  - `A-601`
  - `A-602`
  - `A-901`
- Dynamic lot dimensions present:
  - `5.00 m`
  - `20.00 m`
- Stale golden dimensions absent:
  - `5 m x 15 m`
  - `15.00 m`
- Concept-only note present:
  - `Bản vẽ khái niệm - không dùng cho thi công`

DXF inspection:

- 10 DXF sheet files present.
- All 10 DXF files open with `ezdxf`.
- `$INSUNITS` is `6` for all inspected DXFs, meaning meters.
- DXF sheet filenames match the Concept 2D package sheet metadata.
- Nonempty modelspace entity counts verified for all 10 DXFs.

Quality report inspection:

- PDF artifact state: `ready`
- PDF `customer_ready`: `true`
- PDF `construction_ready`: `false`
- DXF artifact state: `ready`
- DXF `customer_ready`: `true`
- DXF `construction_ready`: `false`
- DWG state: `skipped`
- `concept_package.enabled`: `true`
- `concept_package.readiness`: `ready`
- `concept_package.source`: `product_concept_adapter`
- `concept_package.sheet_count`: 10
- `concept_package.fallback_reason`: `null`
- QA bounds:
  - lot width: 5.0
  - lot depth: 20.0
  - floors: 3
  - rooms: 14
  - openings: 17

## Verification Commands

Previously completed before this fresh UI pass:

1. `pnpm lint` in Web: passed with existing warnings only.
2. `pnpm build` in Web: passed.
3. `PYTHONPATH=. .venv/bin/python -m pytest tests/professional_deliverables -q`: `81 passed, 2 skipped`.
4. `PYTHONPATH=. .venv/bin/python -m pytest tests/test_foundation.py tests/test_flows.py tests/test_briefing.py -q`: `21 passed`.
5. `make sprint3-ci-linux`: passed; Sprint 2 and Sprint 3 Linux parity each reported `83 passed`.
6. `docker compose -f docker-compose.local.yml up -d --build`: passed.

Fresh UI/artifact commands completed after the commits:

1. Playwright UI flow: intake -> designs -> review -> approve -> create Professional Deliverables -> delivery.
2. Playwright Review console/network inspection.
3. Playwright Delivery console/network inspection.
4. `curl` download of PDF and artifact quality report.
5. PyMuPDF PDF text/page/render inspection.
6. `ezdxf` openability/unit/entity inspection for all Concept 2D DXFs.
7. Docker storage listing for generated 2D/3D/video artifacts.

## Residual Risk

- Overall Professional Deliverables status is still `partial` because DWG clean-open is skipped locally. This is expected and explicitly reported.
- Concept 2D package itself is `ready` and rendered from the live product path.
- Elevation and section drawings remain concept-level and suitable for customer review, not construction documentation.
- USDZ exporter still emits existing material localization warnings in worker logs; gates still pass and this is outside the Concept 2D acceptance scope.

## Final Acceptance

PASS.

The fresh browser flow successfully produced a locked design and a live Concept 2D Professional Deliverables package. Review and Delivery expose the correct PDF/DXF/report links with no console errors and no 404/500 network failures in the verified pages. The generated PDF/DXF artifacts preserve the selected 5m x 20m geometry, contain the expected concept sheet set, avoid stale 5m x 15m labels, and remain concept-only rather than construction-ready.

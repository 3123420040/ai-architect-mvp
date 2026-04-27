---
title: Sprint 1 Plan — 2D Pipeline Foundation
phase: 2
status: accepted
date: 2026-04-26
owner: Dev/Test Agent
track: Professional Deliverables
---

# Sprint 1 Plan — 2D Pipeline Foundation

Plan accepted and Sprint 1 completed. This file is retained as historical implementation scope.

## Context Ingestion Confirmation

| Required file | Evidence read from file |
|---|---|
| `06-sprint-brief-handoff.md` | Sprint 1 is limited to DWG/DXF exporter, PDF generator, sheet assembly, and CI gates; the pipeline is async-first and a bundle must not be delivered if any required artifact fails a gate. |
| `03-adr-001-standards-combo.md` | ADR-001 locks the AIA layer subset including `A-WALL`, `A-WALL-FULL`, `A-DOOR`, `A-GLAZ`, `A-FURN`, `A-ROOF`, `A-ANNO-DIMS`, `S-COLS`, and also locks Metal-Roughness only for later 3D work. |
| `05-prd-deliverables.md` | Appendix A specifies exact layer properties, including `A-WALL = white / 0.50mm` and `A-ANNO-DIMS = red / 0.25mm`; PR-2D requires Vietnamese labels, title block, scale, north arrow, dimension lines, room labels, and door swings. |
| `01-discovery-summary.md` | Resolved OQ5 says drawing labels are VN-only by default; resolved OQ3 says there are exactly two video cuts later: 60s master and 20-30s reel. |
| `02-market-standards-research.md` | AIA CAD Layer Guidelines are selected as the MVP best fit because they are free, recognized by VN engineers, and practical for AutoCAD/Revit/SketchUp handoff; IFC is over-specified for concept/schematic output. |
| `04-deferred-roadmap.md` | DEF-001 Pascal Editor, DEF-002 IFC export, DEF-003 full ISO 19650 process compliance, DEF-004 TCVN/QCVN compliance, DEF-006 AI procedural materials are deferred, and DEF-005 Spec-Glossiness is rejected permanently. |

## Goal

Implement a self-contained Sprint 1 2D export path for the golden townhouse fixture:

- Type: townhouse
- Footprint: 5 m x 15 m
- Storeys: 2
- Style: Tropical VN

Outputs:

- DWG/DXF sheets: `A-100-site`, `A-101-floorplan`, `A-201-elevations`, `A-301-sections`
- PDF bundle: NCS-style title block, Vietnamese labels, Be Vietnam Pro embedded, scale `1:100`
- Local reproducible demo command
- CI gates for DWG/DXF validity, AIA layer dictionary, PDF diacritics, and PDF scale

## Non-Goals

- No IFC export, IFC tests, or IFC schema work.
- No Pascal Editor integration.
- No TCVN/QCVN compliance checking.
- No construction schedules, notes blocks, hatching system, permit drawings, or shop/detail drawings.
- No English labels.
- No 3D/video/material implementation in Sprint 1 beyond preserving interfaces for later phases.

## Chosen Libraries and Tools

Use existing backend pins unless there is a specific gate need:

| Purpose | Tool/library | Version/pin |
|---|---|---|
| Backend orchestration | FastAPI | `0.115.0` existing |
| Async job execution | Celery + Redis | `celery[redis]==5.4.0` existing |
| DXF authoring | ezdxf | `1.3.4` existing, no upgrade for Sprint 1 unless tests expose a blocker |
| PDF generation | ReportLab | `4.2.5` existing |
| PDF text/vector validation | PyMuPDF | planned `1.27.2.3` |
| Font inspection/subset checks | fonttools | planned `4.62.1` |
| Tests | pytest | `8.3.3` existing |
| DXF to DWG conversion | ODA DWG-DXF Converter CLI | installed via CI runner/AppImage/package; binary path controlled by `ODA_FILE_CONVERTER_BIN` |
| DWG/DXF smoke open | ODA converter audit and LibreCAD under `xvfb-run` where available | CI environment package/tool |
| Font | Be Vietnam Pro | bundled `.ttf` committed under backend static assets after acceptance |

ODA's official converter page says the converter supports CLI mode, source/target directories, input filters, output version/type, recursive flag, and audit flag. The plan will wrap that CLI rather than shelling from request handlers.

## Proposed Module Structure

Primary code will live in `ai-architect-api/` because Sprint 1 is backend export/orchestration work.

```text
ai-architect-api/
  app/services/professional_deliverables/
    __init__.py
    aia_layers.py              # exact PRD Appendix A dictionary, one source of truth
    drawing_contract.py        # typed sheet/project dataclasses and validation
    golden_fixture.py          # 5m x 15m, 2-storey Tropical VN fixture builder
    sheet_assembler.py         # A-100/A-101/A-201/A-301 sheet list and naming
    dxf_exporter.py            # ezdxf model/paper space generation
    dwg_converter.py           # ODA CLI wrapper, env-driven, no request-thread blocking
    pdf_generator.py           # ReportLab sheet bundle, title block, VN labels, font embedding
    validators.py              # layer, clean-open, diacritic, scale gates
    demo.py                    # local golden bundle generation entry point
  app/tasks/professional_deliverables.py
  tests/professional_deliverables/
    test_aia_layers.py
    test_dxf_exporter.py
    test_pdf_generator.py
    test_sprint1_golden_bundle.py
  .github/workflows/sprint1-deliverables.yml
  Makefile                    # `make sprint1-demo`, if accepted
```

I will keep the new Sprint 1 path separate from the existing legacy `app/services/exporter.py` unless acceptance explicitly asks for a shared endpoint. That file currently contains older Phase 2-style output behavior that includes IFC/schedules/details, which conflicts with the deferred-roadmap boundaries for this track.

## Execution Model

- API layer enqueues export work through Celery and returns a job id.
- Worker runs 2D export stages off-request:
  - build/validate drawing contract
  - generate DXF sheets
  - convert DXF to DWG through ODA CLI
  - generate bundled PDF
  - run gates
  - persist outputs only if gates pass
- Local demo command can run synchronously as a developer fixture generator, but product-facing execution stays async-first.
- Feature flag: `ENABLE_PROFESSIONAL_DELIVERABLES=false` by default until integration is accepted.

## Sheet Strategy

Planned canonical files for the golden fixture:

- `A-100-site.dxf/.dwg`: site boundary, footprint, setbacks/context, north arrow.
- `A-101-floorplan.dxf/.dwg`: floor plan sheet. Pending PM clarification, this will either contain F1/F2 on one sheet to satisfy the four-sheet DoD, or split into `A-101-F1` and `A-101-F2` if the per-floor rule overrides the four-sheet count.
- `A-201-elevations.dxf/.dwg`: north, south, east, west elevations.
- `A-301-sections.dxf/.dwg`: one transverse and one longitudinal section.
- `bundle.pdf`: same sheet set with Vietnamese title block labels.

## Test Plan Per CI Gate

| Gate | Automated test |
|---|---|
| DWG opens cleanly | Generate DXF, convert to DWG using ODA CLI with audit enabled, then run an ODA round-trip DWG to DXF. If LibreCAD is available in CI, open under `xvfb-run` and fail on non-zero exit or recovery/error logs. |
| AIA layer exactness | Unit-test `aia_layers.py` against PRD Appendix A exact names, colors, and lineweights. Integration-test each generated DXF and ODA round-trip DXF: no production entities on layer `0`, required layers exist, layer color/lineweight match exactly. |
| PDF Vietnamese diacritics | Generate `bundle.pdf`, extract text with PyMuPDF, assert `ô`, `ư`, `đ`, `ấ` are present, and assert no `?`, replacement character, or tofu-style fallback markers appear in required labels. Inspect embedded font names for Be Vietnam Pro. |
| PDF scale | Draw a normal 1:100 graphic scale/dimension on plan sheets. Use PyMuPDF vector extraction to assert 1 m in drawing units maps to 10 mm / 1 cm on the PDF page, within a tight tolerance. |
| Golden fixture | `make sprint1-demo` regenerates the full bundle into `storage/professional-deliverables/golden-townhouse/`; test validates all expected files exist and gates pass. |

## CI and PR Reporting

- Add a GitHub Actions workflow in `ai-architect-api/.github/workflows/sprint1-deliverables.yml`.
- Run pytest gates and golden demo in the backend Docker image.
- Install or mount ODA converter via CI environment variable `ODA_FILE_CONVERTER_BIN`.
- Emit a Markdown gate summary artifact suitable for PR comments.
- Sprint report will be written to `docs/phase-2/sprint-reports/sprint-1.md` with one row per gate and the reproducible demo command.

## Clarifications Raised

Formal files created for PO relay:

- `docs/phase-2/questions-from-dev/sprint-1-oda-ci-runner.md`
- `docs/phase-2/questions-from-dev/sprint-1-sheet-count.md`

These do not block starting low-risk implementation after plan acceptance, but they must be resolved before claiming Sprint 1 DoD complete.

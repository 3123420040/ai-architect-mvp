---
title: Sprint 1 Report — 2D Pipeline Foundation
phase: 2
status: ACCEPTED
date: 2026-04-26
accepted: 2026-04-27
owner: Dev/Test Agent
reviewer: PM/Architect Agent
pr: https://github.com/blackbirdzzzz365-gif/ai-architect-api/pull/1
---

# Sign-off (PM/Architect Agent — 2026-04-27)

**Sprint 1 ACCEPTED.** All Definition of Done items satisfied:

- [x] All required DWG sheets generated per per-floor strategy (5 sheets for golden fixture).
- [x] PDF generator with VN title block; Be Vietnam Pro embedded; diacritic check passes.
- [x] All Sprint 1 CI gates green in PR #1 — including the conditional `DWG clean-open` gate (`ODA audit round-tripped 5 DWG files`).
- [x] Sprint report submitted with reproducible demo command.
- [x] No breaking changes to Phase 1 baseline; new path lives under `app/services/professional_deliverables/`.

**Additional fixes landed in PR #1 (not regressions, real CI environment hardening):**
- Qt/xcb runtime dependencies installed for ODA File Converter on `ubuntu-latest`.
- Workflow `permissions: pull-requests: write` added so the sticky gate-summary comment can post.

Sprint 2 is now formally unblocked. See `docs/phase-2/sprint-plans/sprint-2.md` (to be created by Dev/Test Agent).

---


# Sprint 1 Report — 2D Pipeline Foundation

## What Was Built

Implemented in `ai-architect-api/`:

| Path | Purpose |
|---|---|
| `app/services/professional_deliverables/aia_layers.py` | Exact PRD-05 Appendix A AIA layer dictionary: 25 layers, color, lineweight, no-plot flag. |
| `app/services/professional_deliverables/drawing_contract.py` | Typed drawing contract and failure validation for incomplete geometry. |
| `app/services/professional_deliverables/golden_fixture.py` | Golden townhouse fixture: 5 m x 15 m, 2 storeys, Tropical VN. |
| `app/services/professional_deliverables/sheet_assembler.py` | Per-floor sheet strategy: `A-100`, `A-101-F1`, `A-101-F2`, `A-201`, `A-301`. |
| `app/services/professional_deliverables/dxf_exporter.py` | DXF generation with editable text/entities and AIA layers. |
| `app/services/professional_deliverables/dwg_converter.py` | ODA File Converter wrapper using `ODA_FILE_CONVERTER_BIN` and `xvfb-run` in CI. |
| `app/services/professional_deliverables/pdf_generator.py` | Bundled PDF sheet set with VN title block, Be Vietnam Pro font, north arrow, dimensions, 1:100 scale. |
| `app/services/professional_deliverables/validators.py` | Gates for AIA layers, PDF diacritics, embedded font, 1:100 scale, PDF size, DWG audit. |
| `app/services/professional_deliverables/demo.py` | Golden bundle generator CLI. |
| `app/tasks/professional_deliverables.py` | Celery task entrypoint for async execution. |
| `tests/professional_deliverables/` | Focused Sprint 1 tests. |
| `.github/workflows/sprint1-deliverables.yml` | GitHub Actions workflow for ODA install, golden demo, pytest, PR comment. |
| `Makefile` | `make sprint1-demo`, `make sprint1-demo-local`, `make sprint1-ci`. |

## Golden Output

Local golden output path:

`ai-architect-api/storage/professional-deliverables/project-golden-townhouse/2d/`

Generated locally:

- `A-100-site.dxf`
- `A-101-F1-floorplan.dxf`
- `A-101-F2-floorplan.dxf`
- `A-201-elevations.dxf`
- `A-301-sections.dxf`
- `bundle.pdf`
- `sprint1_gate_summary.json`
- `sprint1_gate_summary.md`

DWG files are produced only when `ODA_FILE_CONVERTER_BIN` is installed/configured. The accepted CI contract installs ODA on `ubuntu-latest` and runs the hard DWG gate there.

## CI Gate Results

| Gate | Status | Evidence |
|---|---|---|
| DWG opens cleanly | Pending CI | Local Mac has no `ODAFileConverter`; workflow `.github/workflows/sprint1-deliverables.yml` installs ODA `.deb`, runs `make sprint1-ci`, and posts `sprint1_gate_summary.md` to PR. Local gate summary marks this as skipped. |
| Layer name + color + lineweight exactness | Pass | `pytest tests/professional_deliverables -q` passed; local `sprint1_gate_summary.md` says `5 DXF sheets match Appendix A exactly`. |
| PDF Vietnamese diacritics | Pass | Local gate extracted `ô`, `ư`, `đ`, `ấ` with no replacement markers. |
| PDF font embedding | Pass | Local gate found Be Vietnam Pro embedded/subset in `bundle.pdf`. |
| PDF 1:100 scale | Pass | Local gate measured a 1 m calibration segment as `28.35 pt = 1 cm at 1:100`. |
| PDF opens / size sanity | Pass | `bundle.pdf` generated as valid PDF, 5 pages, 41,947 bytes. |

## Verification Commands Run

```bash
cd /Users/nguyenquocthong/project/ai-architect/ai-architect-api
.venv/bin/python -m pytest tests/professional_deliverables -q
.venv/bin/python -m pytest -q
make sprint1-demo-local
```

Results:

- Focused Sprint 1 tests: `7 passed`
- Full backend suite: `28 passed`
- Local demo: generated golden `/2d/` bundle; DWG gate skipped because ODA is absent locally.

## Reproducible Demo Command

Full Sprint 1 DoD demo with DWG conversion/audit:

```bash
cd /Users/nguyenquocthong/project/ai-architect/ai-architect-api
export ODA_FILE_CONVERTER_BIN=/usr/bin/ODAFileConverter
make sprint1-demo
```

Local DXF/PDF-only developer demo:

```bash
cd /Users/nguyenquocthong/project/ai-architect/ai-architect-api
make sprint1-demo-local
```

## Known Issues / Follow-up

- DWG clean-open cannot be completed on this macOS workspace because ODA is not installed. This is expected per the answered question file: the hard gate runs on GitHub-hosted `ubuntu-latest` with ODA `.deb` and `xvfb-run`.
- GitHub variable `ODA_DEB_URL` must be configured before the CI workflow can install ODA.
- Sprint 1 intentionally does not implement IFC, schedule tables, hatching, EN labels, 3D/video deliverables, or full `manifest.json`; those are out of scope or later sprint work per PRD/ADR/deferred roadmap.


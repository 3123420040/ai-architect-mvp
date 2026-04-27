---
title: Sprint 3 Local Linux Parity Handoff — System Analysis
phase: 2
status: ready-for-opencode-after-pm-approval
date: 2026-04-27
owner: Codex Coordinator
---

# System Analysis

## Current Behavior

The Sprint 3 demo target exists:

```bash
make sprint3-ci
```

It calls:

```bash
PYTHONPATH=. $(PYTHON) -m app.services.professional_deliverables.sprint3_demo --require-external-tools
PYTHONPATH=. $(PYTHON) -m pytest tests/professional_deliverables
```

Current local macOS smoke verification can run unit tests, but required gates are skipped or blocked when external tools and Sprint 2 artifacts are missing.

## Relevant Modules

API repo: `/Users/nguyenquocthong/project/ai-architect/ai-architect-api`

- `Makefile`
- `requirements.txt`
- `tools/sprint2/package.json`
- `tools/sprint2/package-lock.json`
- `tools/sprint3/README.md`
- `app/services/professional_deliverables/sprint2_demo.py`
- `app/services/professional_deliverables/sprint3_demo.py`
- `app/services/professional_deliverables/ktx2_encoder.py`
- `app/services/professional_deliverables/blender_runner.py`
- `app/services/professional_deliverables/fbx_exporter.py`
- `app/services/professional_deliverables/usdz_converter.py`
- `app/services/professional_deliverables/video_renderer.py`
- `app/services/professional_deliverables/model_validators.py`
- `app/services/professional_deliverables/usdz_validators.py`
- `app/services/professional_deliverables/video_validators.py`

Docs repo:

- `docs/phase-2/07-local-git-verification-protocol.md`
- `docs/phase-2/sprint-reports/sprint-3.md`
- this handoff folder

## Existing Tool Install Recipe

Historical GitHub workflow files already define the required Linux toolchain:

- `.github/workflows/sprint2-deliverables.yml`
- `.github/workflows/sprint3-deliverables.yml`

Important pins:

- Python 3.12
- Node 22
- Blender 4.5.1 Linux x64 tarball from `download.blender.org`
- KTX-Software 4.4.2 Linux x86_64 `.deb`
- FFmpeg from Ubuntu apt packages
- Sprint 2 Node tools via `npm ci --prefix tools/sprint2`

## Data Flow

Expected local parity flow:

1. Build or enter the Linux parity environment.
2. Install Python dependencies from `requirements.txt`.
3. Install Sprint 2 Node tooling.
4. Install Blender/KTX/FFmpeg.
5. Run `make sprint2-ci`.
6. Confirm generated Sprint 2 artifacts exist under:
   - `storage/professional-deliverables/project-golden-townhouse/3d/`
   - `storage/professional-deliverables/project-golden-townhouse/textures/`
7. Run `make sprint3-ci`.
8. Confirm generated Sprint 3 artifacts exist:
   - `3d/model.usdz`
   - `3d/model_lite.usdz`
   - `video/master_4k.mp4`
   - `video/camera_path.json`
9. Update Sprint 3 report.

## Risks

- On Apple Silicon hosts, Docker `linux/amd64` may run through emulation and be slow, especially for the dual-render determinism gate.
- Network downloads are required for Blender and KTX-Software unless cached.
- The current macOS virtualenv has a broken `.venv/bin/pip` shebang; commands should prefer `.venv/bin/python -m pip`.
- If the local Docker run exceeds practical time limits, the correct outcome is `BLOCKED` with elapsed time and a recommendation for an x86_64 Linux machine or self-hosted free runner.

## Assumptions

- Docker is available locally.
- Local-first verification remains the accepted operating model.
- Remote GitHub Actions and PR comments are not required.


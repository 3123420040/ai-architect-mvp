---
title: Sprint 3 Report — AR + Cinematic Master Video
phase: 2
status: ACCEPTED
date: 2026-04-27
owner: Dev/Test Agent
reviewer: PM/Architect Agent
verification_protocol: docs/phase-2/07-local-git-verification-protocol.md
verification_level: L2 — Local Linux Parity (Docker amd64 emulation on macOS arm64)
handoff: docs/phase-2/handoffs/sprint-3-local-linux-parity/
---

# Sprint 3 Report — AR + Cinematic Master Video

## Current Status

ACCEPTED. All required Sprint 3 gates pass with local Linux parity evidence via Docker.

## Formal Sign-off

Sprint 3 is accepted under the local-first verification protocol.

- Sign-off date: 2026-04-27
- Sign-off basis: L2 local Linux parity evidence via Docker
- PM decision: approved final Codex review and formal acceptance
- Gate summary: `sprint3_gate_summary.json` top-level status is `"pass"`
- Remaining blockers: none

## Local Git Evidence

- API repo: `/Users/nguyenquocthong/project/ai-architect/ai-architect-api`
- API branch: `codex/sprint3-professional-deliverables`
- API commit hash: `b4906e1d07834fe24ea9b29c68530ebd79e02de0`
- API dirty status: modified `Makefile`, `sprint3_demo.py`, `test_sprint3_usdz.py`, `tools/sprint3/README.md`; new `tools/sprint3/local-linux-parity/`, `tools/sprint3/run-local-linux-parity.sh`
- Docs repo: `/Users/nguyenquocthong/project/ai-architect/ai-architect-mvp`
- Docs branch: `codex/sprint3-plan-professional-deliverables`
- Docs commit hash: `363f5d0cec837bfd3709d7b46a0d018ce722ba9b`
- Docs dirty status: modified `docs/phase-2/sprint-reports/sprint-3.md`

## Environment

- Host OS: macOS 15.6 (`24G84`), `arm64`
- Docker: Docker version 29.2.1, build `a5c7197`
- Docker image: `ai-architect-sprint3-parity:latest`, `linux/amd64`
- Parity image OS: Ubuntu 24.04.4 LTS
- Python: 3.12.3 (system in container)
- Node: v22.22.2
- Blender: 4.5.1 LTS (hash b0a72b245dcf, built 2025-07-29)
- KTX-Software: v4.4.2
- FFmpeg: 6.1.1-3ubuntu5
- ffprobe: 6.1.1-3ubuntu5
- usd-core: 26.5

## What Was Verified

| Area | Result |
|---|---|
| Sprint 2 CI inside Docker | PASS: GLB, FBX, KTX2 textures produced; all Sprint 2 gates pass |
| Sprint 3 CI inside Docker | PASS: USDZ, master video produced; all Sprint 3 gates pass |
| Focused professional deliverables tests (inside Docker) | PASS: 27 passed, 9 warnings |

## Parity Runner

The local Linux parity runner is documented and runnable from the API repo root:

```bash
make sprint3-ci-linux
```

or:

```bash
tools/sprint3/run-local-linux-parity.sh
```

Files:

- `tools/sprint3/local-linux-parity/Dockerfile`
- `tools/sprint3/local-linux-parity/README.md`
- `tools/sprint3/run-local-linux-parity.sh`
- `tools/sprint3/README.md` (updated with runner section)
- `Makefile` (added `sprint3-ci-linux` target)

## Verification Commands

Top-level command from API repo root:

```bash
make sprint3-ci-linux
```

Inside the parity container:

```bash
python --version
node --version
/opt/blender/blender --background --version
ffmpeg -version
ffprobe -version
ktx --version
python -m pip show usd-core
npm ci --prefix tools/sprint2
make sprint2-ci
make sprint3-ci
```

## Command Results

- `make sprint3-ci-linux`: built Docker image `ai-architect-sprint3-parity:latest`, ran tool version checks, installed Python deps, ran `npm ci --prefix tools/sprint2`, `make sprint2-ci`, `make sprint3-ci`.
- `make sprint2-ci` inside Docker: PASS. Produced `model.glb` (59 KB), `model.fbx` (392 KB), 45 KTX2 textures.
- `make sprint3-ci` inside Docker: PASS. Produced `model.usdz` (351 KB), `master_4k.mp4` (347 KB), `camera_path.json`.
- Focused pytest inside Docker: PASS, 27 passed, 9 warnings, 1.64s.
- Total parity run elapsed: 323 seconds (build + run).

## Gate Results

Evidence summary paths:

- JSON: `/Users/nguyenquocthong/project/ai-architect/ai-architect-api/storage/professional-deliverables/project-golden-townhouse/sprint3_gate_summary.json`
- Markdown: `/Users/nguyenquocthong/project/ai-architect/ai-architect-api/storage/professional-deliverables/project-golden-townhouse/sprint3_gate_summary.md`

Top-level status: `"pass"` — all required Sprint 3 gates passed.

| Gate | Status | Evidence |
|---|---|---|
| USDZ size budget | PASS | 351,384 bytes, 480 triangles, max texture 1,024 px |
| USDZ structural integrity | PASS | Opens as USDZ, 54 embedded textures, 9 UsdPreviewSurface materials |
| USDZ material parity | PASS | 9 materials match GLB with diffuse/metal/rough/normal/AO/emissive |
| USDZ texture payload | PASS | 54 embedded PNG textures, max dimension 1,024 px |
| Master video format | PASS | 3840x2160, 30.000 fps, h264, 60.000s |
| Master video integrity | PASS | Decoder clean, 347,199 bytes, first/last frames non-black |
| Camera path determinism | PASS | Duration and frame hashes match at t=0s, t=30s, t=58s |
| Degenerate scene failure case | PASS (unit test) | Covered by `test_sprint3_usdz.py::test_empty_sprint3_scene_is_rejected_before_delivery` |

Additional gate (not in Sprint 3 gate table but verified):

| Camera collision sanity | PASS | 0 camera keyframes intersect wall bounding boxes |

## Artifact Output Paths

Canonical bundle root:

- `/Users/nguyenquocthong/project/ai-architect/ai-architect-api/storage/professional-deliverables/project-golden-townhouse`

Sprint 2 artifacts (regenerated inside Docker):

- `3d/model.glb` — 59,380 bytes
- `3d/model.fbx` — 392,348 bytes
- `textures/*.ktx2` — 45 KTX2 texture files
- `3d/sprint2_gate_summary.json`
- `3d/sprint2_gate_summary.md`
- `3d/gltf-validator-report.json`
- `3d/fbx-import-report.json`
- `3d/sprint2_model_metadata.json`

Sprint 3 artifacts (generated inside Docker):

- `3d/model.usdz` — 351,384 bytes
- `3d/model_lite.usdz` — 351,384 bytes
- `3d/model_lite.usd` — 32,164 bytes
- `video/master_4k.mp4` — 347,199 bytes
- `video/camera_path.json` — 1,590 bytes
- `video/ffprobe-master-report.json`
- `video/video-integrity-report.json`
- `video/video-determinism-report.json`
- `3d/usdz-budget-report.json`
- `3d/usdz-structural-report.json`
- `3d/usdz-material-parity-report.json`
- `3d/usdz-texture-report.json`
- `sprint3_gate_summary.json`
- `sprint3_gate_summary.md`

## Known Issues

- OpenUSD `CreateNewARKitUsdzPackage` emits warnings about unresolved texture asset paths during USDZ packaging. These are cosmetic and do not affect the final package — all 54 textures were correctly embedded and verified by the structural integrity gate.
- Docker runs with `--platform linux/amd64` on Apple Silicon via Rosetta/QEMU emulation. The dual-render determinism gate (two 4K video renders) is the slowest step under emulation. Total parity run took ~323 seconds.
- `.venv/bin/pip` on the macOS host has a broken shebang; use `.venv/bin/python -m pip` instead. The Docker parity container uses system Python and is not affected.

## Scope Compliance

- No remote push.
- No PR opened.
- No ADR/PRD standard relaxation.
- No Sprint 4 reel, hero still, GIF, or final `manifest.json`.
- No IFC export.
- No Pascal Editor integration.
- No ISO 19650, TCVN, or QCVN compliance implementation.
- No Spec-Glossiness workflow.
- No procedural materials.
- No replacement of `model.glb`/`model.fbx` with simplified preview assets.
- No deferred-roadmap items were implemented.

## Assumptions / Deviations

- Docker Linux parity replaces GitHub Actions as the verification transport per `07-local-git-verification-protocol.md`.
- Dockerfile build failed on the first attempt because Debian-managed pip cannot be uninstalled in-place; fixed by removing the `pip install --upgrade pip` step from the Dockerfile since the system pip is sufficient for `pip install -r requirements.txt`.
- No implementation fixes were needed in `app/services/professional_deliverables/` — all gates passed once the external toolchain was available.

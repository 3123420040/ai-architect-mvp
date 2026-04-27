---
title: Sprint 3 Local Linux Parity Handoff — Context
phase: 2
status: ready-for-pm-decision
date: 2026-04-27
owner: Codex Coordinator
---

# Context

Sprint 3 implementation exists in the API repo, but final Sprint 3 acceptance is blocked by local verification environment gaps.

## Current State

- API repo: `/Users/nguyenquocthong/project/ai-architect/ai-architect-api`
- Expected API branch: `codex/sprint3-professional-deliverables`
- Docs repo: `/Users/nguyenquocthong/project/ai-architect/ai-architect-mvp`
- Local-first protocol: `docs/phase-2/07-local-git-verification-protocol.md`
- Current sprint report: `docs/phase-2/sprint-reports/sprint-3.md`

The latest opencode follow-up fixed the report semantics issue:

- `usd-core==26.5` is installed when checked through `.venv/bin/python -m pip show usd-core`.
- `sprint3_gate_summary.json` now reports top-level `partial`, not `pass`, when required Sprint 3 gates are skipped.
- Focused professional deliverables tests pass locally: `27 passed`.

## Remaining Blockers

Final Sprint 3 gates still cannot run because the available host environment lacks:

- Blender 4.5.1
- KTX-Software 4.4.2 CLI (`ktx` preferred; `toktx` fallback only if compatible)
- FFmpeg and ffprobe
- Canonical Sprint 2 generated outputs in the bundle:
  - `3d/model.glb`
  - `3d/model.fbx`
  - `/textures/*.ktx2`

## Recommended Next Step

Create a project-owned local Linux parity runner that replaces the old GitHub Actions transport:

- Docker-based Ubuntu parity environment.
- Installs the same toolchain previously installed by `.github/workflows/sprint2-deliverables.yml` and `.github/workflows/sprint3-deliverables.yml`.
- Runs `make sprint2-ci` first to regenerate the missing Sprint 2 GLB/FBX/KTX2 artifacts.
- Runs `make sprint3-ci` second to produce and validate USDZ + master video.
- Updates `docs/phase-2/sprint-reports/sprint-3.md` with real local L2 evidence.

## PM Decision Needed

Approve the next implementation workstream as **Docker Linux parity local verification**.

This is the recommended path because it preserves the locked ADR/PRD acceptance criteria without requiring paid GitHub Actions.


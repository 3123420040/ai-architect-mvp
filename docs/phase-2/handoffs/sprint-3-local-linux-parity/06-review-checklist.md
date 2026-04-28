---
title: Sprint 3 Local Linux Parity Handoff — Review Checklist
phase: 2
status: ready-for-codex-review
date: 2026-04-27
owner: Codex Coordinator
---

# Review Checklist

Codex must review the opencode report in this order.

## Scope

- [ ] No remote push.
- [ ] No PR creation/update.
- [ ] No ADR-001 changes.
- [ ] No PRD-05 acceptance relaxation.
- [ ] No Sprint 4 outputs implemented.
- [ ] No deferred-roadmap items implemented.

## Runner

- [ ] Local Linux parity command exists and is documented.
- [ ] Runner uses or documents Python 3.12.
- [ ] Runner uses or documents Node 22.
- [ ] Runner uses or documents Blender 4.5.1.
- [ ] Runner uses or documents KTX-Software 4.4.2.
- [ ] Runner uses or documents FFmpeg/ffprobe.
- [ ] Runner confirms `usd-core==26.5`.
- [ ] Generated artifacts are written to the host API repo, not lost inside a container layer.

## Sprint 2 Regeneration

- [ ] `make sprint2-ci` passed.
- [ ] `3d/model.glb` exists.
- [ ] `3d/model.fbx` exists.
- [ ] `/textures/*.ktx2` exists.
- [ ] `3d/sprint2_gate_summary.json` top-level status is `pass`.

## Sprint 3 Acceptance

- [ ] `make sprint3-ci` passed, or BLOCKED is justified with exact evidence.
- [ ] `3d/model.usdz` exists.
- [ ] `3d/model_lite.usdz` exists.
- [ ] `video/master_4k.mp4` exists.
- [ ] `video/camera_path.json` exists.
- [ ] `sprint3_gate_summary.json` top-level status is `pass` only if all required gates pass.
- [ ] Gate table includes every Sprint 3 required gate.

## Decision

Return one:

- `ACCEPTED`: all required gates pass and report is complete.
- `NEEDS_FIX`: scoped implementation/report issue remains.
- `NEEDS_MORE_TESTS`: code changed but verification is insufficient.
- `BLOCKED`: external environment/tool/runtime issue remains and is documented.
- `NEEDS_CLARIFICATION`: PM decision is required before continuing.


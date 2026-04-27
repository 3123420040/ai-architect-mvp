---
title: Sprint 3 Local Linux Parity Handoff — Requirements
phase: 2
status: ready-for-opencode-after-pm-approval
date: 2026-04-27
owner: Codex Coordinator
---

# Requirements

## Objective

Provide a reproducible local Linux-equivalent verification path for AI Architect Phase 2 Sprint 3, without GitHub Actions, remote PRs, or paid CI.

## Goals

- Add a project-owned local parity runner for Sprint 2 + Sprint 3 professional deliverables verification.
- Regenerate the golden fixture's Sprint 2 3D outputs locally:
  - `3d/model.glb`
  - `3d/model.fbx`
  - `/textures/*.ktx2`
- Run Sprint 3 acceptance gates locally:
  - USDZ size budget
  - USDZ structural integrity
  - USDZ material parity
  - USDZ texture payload
  - master video format
  - master video integrity
  - camera path determinism
  - degenerate scene failure case
- Update Sprint 3 report with real L2 local Linux parity evidence.

## Non-Goals

- Do not push to remote.
- Do not open or update PRs.
- Do not implement Sprint 4 outputs: reel, hero still, GIF, final `manifest.json`.
- Do not implement IFC, Pascal Editor integration, ISO 19650 process compliance, TCVN/QCVN compliance, Spec-Glossiness, or procedural materials.
- Do not relax ADR-001 or PRD-05 acceptance criteria.
- Do not replace Sprint 2 GLB/FBX outputs with simplified preview artifacts.

## Success Criteria

- The parity runner can be invoked from the local machine with a documented command.
- The runner logs exact versions for Python, Node, Blender, KTX-Software, FFmpeg/ffprobe, and usd-core.
- `make sprint2-ci` runs inside the parity environment and produces required Sprint 2 artifacts.
- `make sprint3-ci` runs inside the parity environment and produces required Sprint 3 artifacts.
- Required Sprint 3 gates are `pass`, or the report remains `BLOCKED` with precise evidence for the remaining external blocker.
- `sprint3_gate_summary.json` must not show top-level `pass` when required gates are skipped or blocked.

## PM Acceptance Decision

If the Product Owner copies the opencode prompt from this handoff, that is treated as approval for the Docker Linux parity path.


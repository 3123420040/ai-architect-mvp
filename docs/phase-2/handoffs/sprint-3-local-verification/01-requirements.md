---
title: Sprint 3 Local Verification Handoff — Requirements
phase: 2
status: ready-for-opencode
date: 2026-04-27
---

# Requirements

## Goal

Produce local verification evidence for Sprint 3 and prepare `docs/phase-2/sprint-reports/sprint-3.md`.

## Success Criteria

- Local git branch and commit hash are recorded.
- `make sprint3-ci` runs in a local Linux-equivalent environment, or a blocker is reported with exact missing tool/runtime.
- Sprint 3 required gates pass:
  - USDZ size budget
  - USDZ structural integrity
  - USDZ material parity
  - USDZ texture payload
  - Master video format
  - Master video integrity
  - Camera path determinism
  - Degenerate scene failure case
- Gate summaries and reports are saved and referenced from the sprint report.
- No Sprint 4 deliverables are implemented.

## Non-Goals

- No remote GitHub Actions requirement.
- No remote push.
- No PR creation.
- No reel, hero still, GIF, final manifest, IFC, Pascal Editor, procedural materials, Spec-Glossiness, or video audio.

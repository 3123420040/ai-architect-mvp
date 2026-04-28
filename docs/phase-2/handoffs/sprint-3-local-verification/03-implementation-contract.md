---
title: Sprint 3 Local Verification Handoff — Implementation Contract
phase: 2
status: ready-for-opencode
date: 2026-04-27
---

# Implementation Contract

## Allowed Changes

- API Sprint 3 verification fixes only, if a required gate fails.
- Sprint 3 report at `docs/phase-2/sprint-reports/sprint-3.md`.
- Local verification notes under this handoff folder if needed.

## Forbidden Changes

- Do not push to remote.
- Do not open or update remote PRs.
- Do not change ADR-001 standards.
- Do not relax PRD-05 acceptance criteria.
- Do not implement Sprint 4 outputs: reel, hero still, GIF, final `manifest.json`.
- Do not implement IFC, Pascal Editor, ISO 19650 process compliance, TCVN/QCVN compliance, Spec-Glossiness, or procedural materials.
- Do not replace Sprint 2 GLB/FBX deliverables with simplified preview artifacts.

## Verification Requirements

Run from `/Users/nguyenquocthong/project/ai-architect/ai-architect-api`:

```bash
git status --short
git branch --show-current
git rev-parse HEAD
PYTHONPATH=. .venv/bin/python -m pytest
make sprint3-ci
```

If using Linux parity via Docker/VM, record:

- image/OS version
- Python version
- Node version
- Blender version
- KTX-Software version
- FFmpeg/ffprobe version
- exact command used to enter/run the environment

## Completion Rule

Sprint 3 is ready for PM/Architect review only when the report shows all required Sprint 3 gates as `pass`, or a blocker is documented with exact missing external requirement.

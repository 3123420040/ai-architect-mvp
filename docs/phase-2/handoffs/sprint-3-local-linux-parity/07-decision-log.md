---
title: Sprint 3 Local Linux Parity Handoff — Decision Log
phase: 2
status: ready-for-pm-decision
date: 2026-04-27
owner: Codex Coordinator
---

# Decision Log

## D-001 — Recommended Verification Transport

Decision: use local Docker Linux parity as the next Sprint 3 verification transport.

Status: pending PM action. If the PM copies the opencode prompt, this is treated as approval.

Rationale:

- The Product Owner does not want paid GitHub Actions.
- Sprint 3 gates still require Linux-compatible external tools.
- Docker parity is the closest local replacement for `ubuntu-latest`.
- This keeps ADR-001 and PRD-05 intact.

## D-002 — Do Not Lower Sprint 3 Gates

Decision: skipped or blocked required gates must not be treated as acceptance.

Status: active.

Rationale:

- Sprint 3 deliverables are not complete without USDZ and master video artifacts.
- Local smoke runs may be useful but are not acceptance evidence.

## D-003 — Sprint 2 Artifacts Must Be Regenerated

Decision: run `make sprint2-ci` before `make sprint3-ci` in the parity environment.

Status: active.

Rationale:

- Sprint 3 derives USDZ and video from Sprint 2 `model.glb` and KTX2 textures.
- The current local storage folder does not contain those source artifacts.


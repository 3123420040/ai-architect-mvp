---
title: Local Git Verification Protocol
phase: 2
status: active
date: 2026-04-27
owner: Product Owner
applies_to:
  - AI Architect Phase 2 Professional Deliverables
supersedes_operationally:
  - GitHub Actions as mandatory verification transport
  - PR comment as mandatory gate-result transport
related:
  - docs/phase-2/03-adr-001-standards-combo.md
  - docs/phase-2/05-prd-deliverables.md
  - docs/phase-2/06-sprint-brief-handoff.md
---

# Local Git Verification Protocol

## 1. Decision

Phase 2 Professional Deliverables now uses a **local-first git and verification workflow**.

GitHub Actions, remote PRs, and sticky PR comments are **optional transport mechanisms**, not mandatory acceptance requirements. Agents must not require paid GitHub CI to continue work.

This document does **not** relax ADR-001 standards or PRD-05 acceptance criteria. It only changes how implementation work is coordinated and how gate evidence is collected.

## 2. Reason

The Product Owner does not want to pay for GitHub-hosted CI. The project still needs reproducible verification evidence, but that evidence can be generated through local git commits, local commands, and local Linux-equivalent runners.

## 3. Source of Truth Priority

When instructions conflict, use this order:

1. ADR-001 standards in `03-adr-001-standards-combo.md`
2. PRD-05 functional requirements and acceptance criteria in `05-prd-deliverables.md`
3. This local verification protocol
4. Sprint plans and sprint reports
5. Chat messages

Older references to "GitHub Actions", "PR comment", or "ubuntu-latest" remain historical unless a newer sprint contract explicitly opts back into remote CI.

## 4. Git Workflow

Default workflow:

- Work on local git branches.
- Commit locally with clear messages.
- Do not push to remote unless the Product Owner explicitly asks.
- Do not open remote PRs unless the Product Owner explicitly asks.
- Use `git status`, `git diff --stat`, and local commit hash as report evidence.

Required report evidence:

- Repo path
- Branch name
- Local commit hash
- Dirty worktree status
- Files changed summary
- Exact commands run
- Gate summary file paths

## 5. Verification Levels

Use the strongest feasible verification level for the gate.

| Level | Name | Use When | Evidence |
|---|---|---|---|
| L0 | Unit/local tests | Pure Python/Node logic, schema checks, static validation | Test command + pass/fail output |
| L1 | Local external-tool run | Tool exists on the current machine | Tool version + command + gate summary |
| L2 | Local Linux parity | Gate previously depended on `ubuntu-latest` or Linux-only tooling | Docker/VM/WSL/Ubuntu runner command + tool versions + gate summary |
| L3 | Remote CI | Free/available remote CI is explicitly requested | CI run URL + artifact/gate summary |

For Sprint DoD, L2 is the preferred replacement for GitHub-hosted `ubuntu-latest` gates when Linux parity matters.

## 6. Gate Rules

Required gates keep the same pass/fail semantics:

- A bundle is **not deliverable** if any required gate fails.
- A skipped gate is acceptable only for local developer smoke runs, not for final sprint acceptance.
- If a required gate cannot run because a tool is unavailable, report `blocked`, not `pass`.
- If a gate is intentionally out of scope for the sprint, report `skipped` with the sprint/scope reason.
- Gate summaries must be written as machine-readable JSON and human-readable Markdown when the pipeline supports it.

Expected summary locations:

- Sprint 1: `/2d/sprint1_gate_summary.{json,md}`
- Sprint 2: `/3d/sprint2_gate_summary.{json,md}`
- Sprint 3+: bundle root or sprint-specific output path, as defined by the sprint plan/report

## 7. Required Sprint Report Format

Each sprint report must include:

- Status: `DRAFT`, `READY_FOR_REVIEW`, `ACCEPTED`, `REJECTED`, or `BLOCKED`
- Local git evidence: branch, commit hash, dirty status
- Environment: OS, CPU/GPU if relevant, Docker/VM image if used
- Tool versions: Blender, KTX, ODA, FFmpeg, Node, Python, validator tools as relevant
- Commands run: exact commands, from repo root
- Gate result table: one row per required gate with pass/fail/skipped/blocked and evidence path
- Artifact output paths
- Known issues
- Reproducible demo command
- Explicit statement that no deferred-roadmap items were implemented

Remote CI URLs may be included when available, but they are no longer required.

## 8. Agent Handoff Requirements

Codex, opencode, and any future implementation agent must reference this protocol in handoff prompts for Phase 2 work.

Implementation prompts must include:

- Scope
- Non-goals
- Allowed file areas
- Forbidden changes
- Acceptance criteria
- Local verification commands
- Required report template
- Instruction to stop and report if a required external tool or contract is missing

Agents must not silently broaden scope to compensate for missing CI.

## 9. Historical Remote-CI Runs

Existing Sprint 1 and Sprint 2 GitHub Actions evidence remains valid historical evidence. Future work does not need to reproduce that evidence in GitHub unless explicitly requested.

Sprint 3 remote PR evidence is currently blocked by GitHub billing/spending limits. The correct next verification path is local L2 Linux parity or an explicitly approved free remote runner.

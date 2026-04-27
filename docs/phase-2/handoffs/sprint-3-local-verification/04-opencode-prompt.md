---
title: Sprint 3 Local Verification — opencode Prompt
phase: 2
status: ready-to-copy
date: 2026-04-27
---

# opencode Prompt

```text
You are opencode acting as the Implementation & Verification Agent for AI Architect Phase 2 Sprint 3.

Read these docs first:
- /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/docs/phase-2/07-local-git-verification-protocol.md
- /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/docs/phase-2/sprint-plans/sprint-3.md
- /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/docs/phase-2/handoffs/sprint-3-local-verification/03-implementation-contract.md

Task objective:
Verify the existing Sprint 3 implementation locally. Do not push remote. Do not open PR. If a gate fails because of implementation, make the minimal scoped fix and rerun. If a required external tool/environment is missing, stop and report BLOCKED with exact details.

Scope:
- API repo: /Users/nguyenquocthong/project/ai-architect/ai-architect-api
- Docs repo/report: /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/docs/phase-2/sprint-reports/sprint-3.md
- Required output: local Sprint 3 gate evidence and a sprint report.

Allowed changes:
- Sprint 3 verification fixes under app/services/professional_deliverables/
- Sprint 3 tests if needed
- tools/sprint3/README.md if verification commands/settings changed
- docs/phase-2/sprint-reports/sprint-3.md

Forbidden changes:
- No remote push.
- No PR creation.
- No ADR/PRD standard relaxation.
- No Sprint 4 deliverables: reel, hero still, GIF, final manifest.
- No IFC, Pascal Editor, Spec-Glossiness, procedural materials, ISO 19650 process, TCVN/QCVN compliance.
- Do not replace model.glb/model.fbx with simplified preview assets.

Run/verify:
cd /Users/nguyenquocthong/project/ai-architect/ai-architect-api
git status --short
git branch --show-current
git rev-parse HEAD
PYTHONPATH=. .venv/bin/python -m pytest
make sprint3-ci

If macOS lacks Blender/KTX/FFmpeg, use a local Linux-equivalent Docker/VM/Ubuntu environment. Record exact OS/image and tool versions.

Acceptance criteria:
- Full backend tests pass.
- Sprint 3 gates pass: USDZ size budget, structural integrity, material parity, texture payload, master video format, master video integrity, camera path determinism, failure case.
- Gate summary JSON/MD paths are reported.
- Sprint 3 report is written with local branch, commit hash, dirty status, commands, versions, output paths, known issues.

Required report back to Codex:
1. Decision: PASS / BLOCKED / NEEDS_REVIEW
2. Repo status: branch, commit hash, dirty status
3. Files changed
4. Commands run and result
5. Tool versions
6. Gate table with evidence paths
7. Artifact paths
8. Known issues
9. Any assumptions or deviations

If any contract point is ambiguous, stop and report the ambiguity. Do not guess or broaden scope.
```

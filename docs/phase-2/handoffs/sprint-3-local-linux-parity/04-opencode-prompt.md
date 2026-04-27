---
title: Sprint 3 Local Linux Parity Handoff — opencode Prompt
phase: 2
status: ready-to-copy-after-pm-approval
date: 2026-04-27
owner: Codex Coordinator
---

# opencode Prompt

```text
You are opencode acting as the Implementation & Verification Agent for AI Architect Phase 2 Sprint 3.

Your job is to implement and run a local Linux parity verification path. Do not push remote. Do not open PRs. Do not broaden scope.

Read these docs first:
- /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/docs/phase-2/07-local-git-verification-protocol.md
- /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/docs/phase-2/sprint-plans/sprint-3.md
- /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/docs/phase-2/sprint-reports/sprint-3.md
- /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/docs/phase-2/handoffs/sprint-3-local-linux-parity/00-context.md
- /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/docs/phase-2/handoffs/sprint-3-local-linux-parity/01-requirements.md
- /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/docs/phase-2/handoffs/sprint-3-local-linux-parity/02-system-analysis.md
- /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/docs/phase-2/handoffs/sprint-3-local-linux-parity/03-implementation-contract.md
- /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/docs/phase-2/handoffs/sprint-3-local-linux-parity/05-opencode-report-template.md

Task objective:
Create a project-owned local Linux parity runner that replaces the old GitHub Actions transport for Sprint 3 verification. It must regenerate Sprint 2 golden 3D artifacts and then run Sprint 3 gates locally.

Repos:
- API repo: /Users/nguyenquocthong/project/ai-architect/ai-architect-api
- Docs repo: /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp

Current blockers to resolve:
- Host lacks Blender, KTX, FFmpeg/ffprobe.
- Sprint 2 generated artifacts are missing from storage: model.glb, model.fbx, textures/*.ktx2.
- GitHub Actions is not available/required.

Allowed changes in API repo:
- tools/sprint3/
- Makefile
- optional runner scripts under scripts/ or tools/sprint3/
- focused tests if needed
- minimal app/services/professional_deliverables/ fixes only if real gates expose implementation bugs after the parity toolchain is available

Allowed changes in docs repo:
- docs/phase-2/sprint-reports/sprint-3.md
- docs/phase-2/handoffs/sprint-3-local-linux-parity/ only for local notes if needed

Forbidden changes:
- No remote push.
- No PR creation or update.
- No ADR-001 changes.
- No PRD-05 acceptance relaxation.
- No Sprint 4 deliverables: reel, hero still, GIF, final manifest.json.
- No IFC, Pascal Editor, ISO 19650, TCVN/QCVN, Spec-Glossiness, or procedural materials.
- Do not replace model.glb/model.fbx with simplified preview assets.
- Do not mark required skipped/blocked gates as top-level pass.

Implementation requirements:
1. Add a documented local Linux parity runner.
   Recommended structure:
   - tools/sprint3/local-linux-parity/Dockerfile
   - tools/sprint3/local-linux-parity/README.md
   - tools/sprint3/run-local-linux-parity.sh
   You may use a different clean structure if documented.

2. The parity environment must install or provide:
   - Python 3.12
   - Node 22
   - Blender 4.5.1 Linux x64 at /opt/blender/blender or set BLENDER_BIN accordingly
   - KTX-Software 4.4.2, with KTX_BIN pointing to ktx if available
   - FFmpeg and ffprobe
   - usd-core==26.5
   - Sprint 2 Node dependencies via npm ci --prefix tools/sprint2

3. The parity run must execute:
   cd /work or mounted API repo equivalent
   python --version
   node --version
   /opt/blender/blender --background --version || $BLENDER_BIN --background --version
   ffmpeg -version
   ffprobe -version
   ktx --version || toktx --version
   python -m pip show usd-core
   npm ci --prefix tools/sprint2
   make sprint2-ci
   make sprint3-ci

4. Generated artifacts must stay in the host API repo under:
   /Users/nguyenquocthong/project/ai-architect/ai-architect-api/storage/professional-deliverables/project-golden-townhouse/

Acceptance criteria:
- Local parity command is documented and runnable from the API repo.
- Sprint 2 CI passes inside parity environment and produces model.glb, model.fbx, and textures/*.ktx2.
- Sprint 3 CI passes inside parity environment and produces model.usdz, model_lite.usdz, master_4k.mp4, camera_path.json, sprint3_gate_summary.json, sprint3_gate_summary.md.
- sprint3_gate_summary.json top-level status is pass only if all required Sprint 3 gates pass.
- Sprint 3 report is updated with environment, commands, tool versions, gate table, artifact paths, known issues, and final status.

If the Docker/Linux parity run is blocked by network, architecture emulation, build time, missing package, or tool incompatibility, stop and report BLOCKED with exact command, error, elapsed time, and proposed next option. Do not invent a lower standard.

Required report back to Codex:
1. Decision: PASS / BLOCKED / NEEDS_REVIEW
2. PM decision assumed: Docker Linux parity local verification
3. Files changed
4. Exact commands run and results
5. Tool versions from inside parity environment
6. Gate table with evidence paths
7. Artifact paths produced
8. Remaining blockers, if any
9. Any implementation fixes made after gates exposed bugs
10. Dirty git status for API repo and docs repo
```


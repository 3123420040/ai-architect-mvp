---
title: Sprint 3 Local Linux Parity Handoff — Implementation Contract
phase: 2
status: ready-for-opencode-after-pm-approval
date: 2026-04-27
owner: Codex Coordinator
---

# Implementation Contract

## Scope

Implement a local Docker Linux parity verification path and use it to run Sprint 2 and Sprint 3 acceptance commands.

## Allowed Changes

In `/Users/nguyenquocthong/project/ai-architect/ai-architect-api`:

- `tools/sprint3/`
- `Makefile`
- optional local runner scripts under `scripts/` or `tools/sprint3/`
- focused tests only if needed for runner/report semantics
- minimal fixes under `app/services/professional_deliverables/` only if a required gate exposes an implementation bug after the parity toolchain is available

In `/Users/nguyenquocthong/project/ai-architect/ai-architect-mvp`:

- `docs/phase-2/sprint-reports/sprint-3.md`
- this handoff folder, only if opencode needs to add local notes

## Forbidden Changes

- No remote push.
- No PR creation or update.
- No ADR-001 changes.
- No PRD-05 acceptance relaxation.
- No Sprint 4 deliverables: reel, hero still, GIF, final `manifest.json`.
- No IFC export.
- No Pascal Editor integration.
- No ISO 19650 process compliance.
- No TCVN/QCVN compliance implementation.
- No Spec-Glossiness workflow.
- No procedural materials.
- Do not replace `model.glb` or `model.fbx` with simplified preview assets.
- Do not mark required skipped gates as top-level `pass`.

## Required Runner Behavior

Create a documented command that:

- runs on the local machine;
- builds or uses a Linux parity environment;
- installs/pins the required toolchain;
- mounts the API repo so generated artifacts remain available on the host;
- runs `make sprint2-ci`;
- runs `make sprint3-ci`;
- leaves gate summaries and artifacts in the canonical `storage/professional-deliverables/project-golden-townhouse/` layout.

Recommended file structure:

```text
tools/sprint3/local-linux-parity/
  Dockerfile
  README.md
tools/sprint3/run-local-linux-parity.sh
```

Alternative file structure is allowed if simpler, but it must be documented in `tools/sprint3/README.md`.

## Required Tool Versions

Use the historical CI contract unless a newer local blocker makes it impossible:

- Ubuntu Linux parity environment, preferably matching current `ubuntu-latest` behavior.
- Python 3.12.
- Node 22.
- Blender 4.5.1 Linux x64.
- KTX-Software 4.4.2.
- FFmpeg/ffprobe from Ubuntu apt packages.
- `usd-core==26.5`.
- Sprint 2 Node dependencies from `npm ci --prefix tools/sprint2`.

## Required Verification Commands

Inside the parity environment, run:

```bash
python --version
node --version
/opt/blender/blender --background --version
ffmpeg -version
ffprobe -version
ktx --version || toktx --version
python -m pip show usd-core
npm ci --prefix tools/sprint2
make sprint2-ci
make sprint3-ci
```

If using host invocation, provide one top-level command such as:

```bash
tools/sprint3/run-local-linux-parity.sh
```

or:

```bash
make sprint3-ci-linux
```

## Completion Rule

Return `PASS` only if all required Sprint 3 gates pass and required artifacts exist.

Return `BLOCKED` if:

- Docker cannot build the parity image;
- downloads are unavailable;
- Apple Silicon emulation makes the run practically infeasible;
- required external tools cannot be installed;
- Sprint 2 or Sprint 3 artifacts still cannot be produced.

Do not guess or broaden scope to bypass a blocker.


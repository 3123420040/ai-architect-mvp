---
title: UI E2E Professional Deliverables Handoff - opencode Report Template
phase: 2
status: approved-for-opencode-handoff
date: 2026-04-27
owner: Codex Coordinator
---

# Required opencode Report Template

```text
Decision: PASS | BLOCKED | NEEDS_REVIEW

Repos:
- API repo:
- API branch:
- API commit, if any:
- API dirty status:
- Web repo:
- Web branch:
- Web commit, if any:
- Web dirty status:
- Docs repo:
- Docs branch:
- Docs commit, if any:
- Docs dirty status:

Scope summary:
- What was implemented:
- What was deliberately not implemented:

Files changed:
- API:
- Web:
- Docs/compose:

API contract implemented:
- POST /versions/{version_id}/professional-deliverables/jobs:
- GET /versions/{version_id}/professional-deliverables:
- GET /professional-deliverables/jobs/{job_id}:
- POST /professional-deliverables/jobs/{job_id}/retry:

Data model/migration:
- New tables/columns:
- Alembic migration file:
- Migration verification result:

Geometry adapter:
- Supported schema:
- Mapping summary:
- Validation behavior:
- Failure behavior:

Worker/Docker:
- professional-worker service added: yes/no
- Dockerfile/toolchain path:
- Blender version:
- KTX version:
- FFmpeg/ffprobe version:
- Node version:
- Python version:
- usd-core version:

UI behavior:
- Review page trigger:
- Progress bar:
- Delivery page artifact panel:
- Polling behavior:

Commands run:
1.
2.
3.

Test results:
- API focused:
- API foundation/flows:
- Golden parity:
- Web lint:
- Web build:
- Docker Compose E2E:

Artifact evidence:
- Bundle root:
- PDF:
- DXF:
- DWG or skip reason:
- GLB:
- FBX:
- USDZ:
- MP4:
- Gate summary JSON:
- Gate summary MD:

Manual UI E2E evidence:
- Project id:
- Version id:
- Job id:
- Final bundle id:
- Final status:
- Progress stages observed:
- Delivery page links verified:

Known issues:
- 

Scope compliance:
- No remote push:
- No PR:
- No Sprint 4 outputs:
- No deferred roadmap items:
- No main API heavy toolchain:
- No synchronous render request:

Questions for Codex/PM:
-
```


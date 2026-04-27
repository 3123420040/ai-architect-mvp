---
title: Sprint 4 Final Bundle Handoff - opencode Report Template
phase: 2
status: ready-for-opencode-handoff
date: 2026-04-27
owner: Codex Coordinator
---

# opencode Report Template

Use this exact structure when reporting back.

```text
Decision: PASS | BLOCKED | NEEDS_CLARIFICATION

Repos:
- API repo:
- API branch:
- API commit:
- API dirty status:
- Web repo:
- Web branch:
- Web commit:
- Web dirty status:
- Docs/compose repo:
- Docs branch:
- Docs commit:
- Docs dirty status:

Files changed:
- API:
- Web:
- Docs/compose:

Implementation summary:
- Reel:
- Hero still:
- GIF:
- Manifest:
- Gate summaries:
- UI:
- Optional archive:

Artifact paths:
- Bundle root:
- Reel:
- Hero still:
- GIF:
- Manifest:
- Sprint 4 gate JSON:
- Sprint 4 gate MD:
- Optional zip:

E2E IDs if product flow was run:
- Project:
- Version:
- Bundle:
- Job:
- Final bundle status:
- Final quality_status:
- Degraded reasons:

Gate table:
| Gate | Result | Evidence |
|---|---|---|
| Reel format | pass/fail/blocked/skipped | |
| Reel integrity | pass/fail/blocked/skipped | |
| Hero still | pass/fail/blocked/skipped | |
| GIF preview | pass/fail/blocked/skipped | |
| Manifest schema | pass/fail/blocked/skipped | |
| Manifest inventory/checksum | pass/fail/blocked/skipped | |
| LOD summary | pass/fail/blocked/skipped | |
| Bundle self-contained | pass/fail/blocked/skipped | |
| Failure case | pass/fail/blocked/skipped | |

Commands run:
1.
2.
3.

Tool versions:
- Python:
- Node:
- FFmpeg:
- ffprobe:
- Blender:
- KTX:
- Docker image/OS if used:

Verification result:
- tests/professional_deliverables:
- tests/test_foundation.py tests/test_flows.py:
- make sprint3-ci-linux:
- make sprint4-ci-linux:
- pnpm lint:
- pnpm build:
- Docker Compose product E2E:

Scope compliance:
- No remote push:
- No PR:
- No ADR/PRD relaxation:
- No external upload/import:
- No deferred-roadmap item:
- No Sprint 4 non-goal implemented:
- Known unrelated dirty files left untouched:

Remaining blockers:
- None, or list exact blocker with command/error/elapsed time/smallest proposed fix.
```


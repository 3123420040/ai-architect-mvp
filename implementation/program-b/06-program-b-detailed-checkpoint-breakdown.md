# Program B Detailed Checkpoint Breakdown

## 1. Purpose

This document breaks Program B Release 1 into execution checkpoints detailed enough for the development team to implement and validate without reopening the architecture.

It assumes the team will implement only:

**Program B Release 1: Coordination-ready architectural handoff**

## 2. Source Documents

This breakdown is derived from:

- [implementation/program-b/01-program-b-scope-lock.md](/Users/nguyenquocthong/project/ai-architect-mvp/implementation/program-b/01-program-b-scope-lock.md:1)
- [implementation/program-b/02-program-b-requirements-detailed.md](/Users/nguyenquocthong/project/ai-architect-mvp/implementation/program-b/02-program-b-requirements-detailed.md:1)
- [implementation/program-b/03-program-b-technical-design-detailed.md](/Users/nguyenquocthong/project/ai-architect-mvp/implementation/program-b/03-program-b-technical-design-detailed.md:1)
- [implementation/program-b/04-program-b-implementation-detailed.md](/Users/nguyenquocthong/project/ai-architect-mvp/implementation/program-b/04-program-b-implementation-detailed.md:1)
- [implementation/program-b/05-program-b-checkpoint-execution-plan.md](/Users/nguyenquocthong/project/ai-architect-mvp/implementation/program-b/05-program-b-checkpoint-execution-plan.md:1)

## 3. Execution Principles

Every Program B checkpoint must obey these rules:

1. do not drift into native BIM authoring
2. keep launch scope architectural-only
3. keep launch typologies limited to `townhouse` and `villa`
4. keep release language honest about coordination vs authoring
5. optimize for visible handoff value, not only backend exports

## 4. Team Lane Model

The checkpoints below assume four engineering lanes.

### Lane A — Backend Persistence and API

Owns:

- DB migration
- ORM models
- API schemas
- resource endpoints

### Lane B — Semantic Model and Orchestration

Owns:

- eligibility validation
- semantic model generation
- schedule extraction orchestration
- job tracking

### Lane C — Export and Bundle Packaging

Owns:

- IFC export
- validation metadata
- manifest
- readiness summary
- storage registration

### Lane D — Frontend and Delivery UX

Owns:

- delivery workspace
- schedule preview
- issue summary
- status and release UX

## 5. Checkpoint Overview

| Order | Code | Checkpoint | Main target |
|---|---|---|---|
| 0 | `cp0-program-b-scope-lock-and-semantic-baseline` | Scope Lock and Semantic Baseline | Freeze launch truth and validation thresholds |
| 1 | `cp1-program-b-semantic-model-and-persistence` | Semantic Model and Persistence | Add Program B persistence and semantic core |
| 2 | `cp2-program-b-quantity-and-issue-contracts` | Quantity and Issue Contracts | Generate schedules and issue registry resources |
| 3 | `cp3-program-b-coordination-ifc-export` | Coordination IFC Export | Produce architectural coordination IFC |
| 4 | `cp4-program-b-handoff-package-and-manifest` | Handoff Package and Manifest | Bundle outputs into releaseable artifact set |
| 5 | `cp5-program-b-delivery-workspace-and-status` | Delivery Workspace and Status | Surface Program B value in product UI |
| 6 | `cp6-program-b-downstream-validation-pilot` | Downstream Validation Pilot | Validate real continuation value on benchmark cases |
| 7 | `cp7-program-b-release-readiness-and-launch-gate` | Release Readiness and Launch Gate | Close launch blockers and freeze readiness evidence |

## 6. Detailed Checkpoints

## CP0 — Scope Lock and Semantic Baseline

### Goal

Freeze all launch decisions that affect semantic quality, typology support, and user messaging.

### Dependencies

- final critique accepted

### Required closure items

- confirm Program B Release 1 scope
- confirm launch typologies
- confirm minimum entity set
- confirm schedule set
- confirm release language
- confirm pilot success thresholds

### Test focus

- document review only

### DoD

- no launch-blocking ambiguity remains

## CP1 — Semantic Model and Persistence

### Goal

Introduce first-class Program B persistence and semantic model generation.

### Dependencies

- CP0 pass

### Lane tasks

Lane A:

- add Program B tables and enums
- add API schemas and base endpoints

Lane B:

- implement semantic model builder
- implement stable semantic id strategy

Lane D:

- add typed fetch layer for Program B resources

### Test focus

- migration apply
- deterministic semantic ids on benchmark fixtures
- unsupported typology blocking

### DoD

- semantic model exists as a durable resource

## CP2 — Quantity and Issue Contracts

### Goal

Generate required schedules and first-class issue records.

### Dependencies

- CP1 pass

### Lane tasks

Lane B:

- implement quantity extraction
- persist schedule rows and confidence states

Lane A:

- implement issue persistence and APIs

Lane D:

- wire schedule and issue data fetch contracts

### Test focus

- schedule completeness
- issue linkage to room and element ids
- confidence status visibility

### DoD

- required schedules exist and issues are first-class

## CP3 — Coordination IFC Export

### Goal

Generate architectural coordination IFC with selected property sets.

### Dependencies

- CP2 pass

### Lane tasks

Lane C:

- implement IfcOpenShell mapping
- add validation metadata

Lane B:

- supply export-ready semantic model input

### Test focus

- IFC artifact generation
- entity continuity
- validation metadata persistence

### DoD

- coordination IFC is generated and registered

## CP4 — Handoff Package and Manifest

### Goal

Package Program B artifacts into a releaseable handoff bundle.

### Dependencies

- CP3 pass

### Lane tasks

Lane C:

- implement manifest builder
- implement readiness summary builder
- register object storage assets

Lane A:

- add bundle release metadata endpoints

### Test focus

- bundle completeness
- manifest references
- readiness summary correctness

### DoD

- bundle can be reviewed as a coherent release object

## CP5 — Delivery Workspace and Status

### Goal

Expose Program B value in the delivery workspace.

### Dependencies

- CP4 pass

### Lane tasks

Lane D:

- add readiness summary panel
- add schedule preview tab
- add issue summary card
- add release status copy

Lane A:

- expose release and detail APIs needed by UI

### Test focus

- UI states
- plain-language copy
- role-based controls

### DoD

- Program B no longer appears as raw file export only

## CP6 — Downstream Validation Pilot

### Goal

Validate whether Program B actually improves continuation quality.

### Dependencies

- CP5 pass

### Lane tasks

Lane A/B/C:

- generate benchmark townhouse and villa bundles
- capture pilot evidence and blocking defects

Lane D:

- expose evidence screens if needed for internal review

### Test focus

- benchmark bundle quality
- semantic stability
- downstream continuation feedback

### DoD

- launch decision is based on evidence, not only architecture confidence

## CP7 — Release Readiness and Launch Gate

### Goal

Close blockers, validate launch claims, and freeze Program B Release 1 readiness.

### Dependencies

- CP6 pass

### Lane tasks

All lanes:

- close launch-blocking gaps
- record release evidence
- confirm no scope bleed into authoring or connectors

### Test focus

- launch threshold pass
- artifact completeness
- message honesty

### DoD

- Program B Release 1 can move into implementation or launch with explicit evidence.

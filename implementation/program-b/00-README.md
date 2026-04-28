# Program B: Coordination-Ready Architectural Handoff

## Context

This document set defines the **final narrowed execution scope** for Program B after the critique and assumption review.

Program B is no longer treated as:

- "future BIM, broadly defined"
- or "native BIM authoring later"

for the purpose of the next execution wave.

Instead, Program B is locked to:

**Coordination-ready architectural handoff**

This means the first executable version of Program B should focus on:

- stronger semantic architectural truth,
- coordination-grade IFC export,
- trustworthy schedule snapshots,
- issue tracking for coordination,
- handoff manifest and readiness summary,
- and a delivery workspace that exposes this value clearly.

## Core Decision

The final executable scope for Program B is:

**Program B Release 1: Coordination-ready architectural handoff for residential projects**

It is explicitly **not**:

- native BIM authoring,
- a browser BIM editor,
- multi-discipline BIM coordination across structure and MEP,
- full construction documentation automation,
- or Revit-first platform integration.

## Target Outputs

Every successful Program B release bundle must contain:

- `coordination_model.json`
- `architectural_coordination.ifc`
- required schedule set
- `issue_register.json`
- `coordination_manifest.json`
- `readiness_summary.json`

## Launch Boundary

Launch scope is intentionally narrow.

Supported launch typologies:

- `townhouse`
- `villa`

Roadmap-only typologies:

- `apartment_reno`
- `shophouse`
- `home_office`

Program B Release 1 is optimized for:

- design firms,
- project architects,
- downstream BIM or documentation teams,
- and secondarily homeowners who need confidence and transparency rather than raw BIM interaction.

## Read Order

1. `implementation/program-b/00-README.md`
2. `implementation/program-b/01-program-b-scope-lock.md`
3. `implementation/program-b/02-program-b-requirements-detailed.md`
4. `implementation/program-b/03-program-b-technical-design-detailed.md`
5. `implementation/program-b/04-program-b-implementation-detailed.md`
6. `implementation/program-b/05-program-b-checkpoint-execution-plan.md`
7. `implementation/program-b/06-program-b-detailed-checkpoint-breakdown.md`
8. `docs/phases/program-b/checkpoints/README.md`

Supporting analysis:

- `implementation/phase-6/program-b-bim-and-construction-research-report.md`
- `implementation/phase-6/04-independent-research-requirements-for-bim-and-premium-cgi.md`

## What “Ready for Dev” Means for Program B

Program B is ready for dev only when the team can build without reopening:

- what Program B Release 1 actually is,
- which personas it is optimizing for,
- what typologies are supported at launch,
- what semantic model minimum is required,
- what IFC level is targeted,
- what schedules and issues are required,
- what must be visible in the delivery workspace,
- and what is explicitly outside launch scope.

This doc set freezes those answers.

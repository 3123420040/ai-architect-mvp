# Program B Scope Lock

*Status: Locked*
*Decision date: 2026-04-14*
*Authority: Scope narrowed after critique and assumption review*

## 1. Purpose

This document freezes the first executable scope of Program B so engineering can build a useful professional handoff lane without drifting into native BIM authoring or full construction automation.

## 2. Executive Decision Summary

| Area | Locked decision |
|---|---|
| Program in scope | `Program B Release 1: Coordination-ready architectural handoff` |
| Primary value | Better downstream continuation, less ambiguity, stronger professional trust |
| Primary operators | Design firms, project architects, downstream BIM or documentation teams |
| Secondary beneficiary | Homeowner sees readiness and issue transparency, not raw BIM tooling |
| Launch typologies | `townhouse`, `villa` |
| Source truth | locked brief + approved canonical version + issued DD package |
| Core outputs | `coordination_model.json`, `architectural_coordination.ifc`, schedule set, `issue_register.json`, `coordination_manifest.json`, `readiness_summary.json` |
| Delivery policy | internal preview allowed before release; release blocked until handoff QA and architect review pass |
| Export policy | coordination-grade IFC only; not authoring-grade round-trip IFC |
| UI policy | expose readiness, schedules, issues, and release state in delivery workspace |
| Explicit non-goals | native BIM editing, multi-discipline BIM authoring, full construction docs, Revit connector as launch dependency |

## 3. Final Scope Definition

Program B Release 1 exists to:

1. convert approved architectural design truth into a stronger semantic coordination model,
2. generate consultant-usable architectural handoff artifacts,
3. expose quantities, issue state, and release intent clearly,
4. and reduce downstream ambiguity before external authoring continues.

Program B Release 1 does **not** exist to:

1. replace Revit or another BIM authoring environment,
2. promise construction-authoring completeness,
3. or create a generic "BIM platform" marketing layer.

## 4. In Scope

- semantic strengthening of architectural source truth
- stable semantic ids for launch-supported typologies
- coordination-grade architectural IFC export
- room, opening, area, and selected finish or wall-related schedules
- issue registry for architectural coordination
- handoff manifest with verification and release metadata
- readiness summary for non-BIM stakeholders
- delivery workspace updates to surface schedules, issues, and release state
- release gating for coordination handoff bundles
- benchmark and pilot validation on `townhouse` and `villa`

## 5. Out of Scope

- native BIM editor UX
- authoring-grade IFC round-trip guarantees
- structural modeling
- MEP modeling
- fabrication modeling
- automated clash detection across disciplines
- permit set automation
- full construction detail library generation
- Revit, APS, or MCP-based authoring connector as launch-blocking dependency
- Speckle as required system of record
- homeowner-facing raw IFC inspection workflow

## 6. Persona and Value Policy

Program B must optimize first for:

- the professional user who needs to continue the design reliably,
- not for the client who wants a richer visual presentation,
- and not for a future in-browser BIM editor persona.

User-visible value must be stated in plain language as:

- clearer continuation,
- fewer downstream surprises,
- stronger consultant handoff,
- more explicit issue visibility,
- and clearer release readiness.

Avoid launch messaging that centers on:

- "BIM platform"
- "construction authoring"
- "editable BIM"

unless those claims are technically and operationally proven.

## 7. Launch Typology Policy

Launch-blocking typologies:

- `townhouse`
- `villa`

Roadmap-only typologies:

- `apartment_reno`
- `shophouse`
- `home_office`

If a requirement cannot be validated on `townhouse` and `villa`, it is not launch-ready.

## 8. Source-of-Truth Policy

Program B Release 1 must read from:

- locked brief
- approved canonical version
- issued design-development package metadata
- semantic architectural references derived from canonical truth

It must not generate final coordination outputs directly from:

- raw intake transcript
- prompt-only design text
- a single image
- unresolved draft geometry

## 9. Required Final Outputs

Every released Program B bundle must contain:

- `coordination_model.json`
- `architectural_coordination.ifc`
- `room_schedule.csv`
- `door_window_schedule.csv`
- `area_schedule.csv`
- `issue_register.json`
- `coordination_manifest.json`
- `readiness_summary.json`

Optional preview artifacts may exist before release, but they must remain blocked if verification or QA rules fail.

## 10. Delivery State Policy

Program B introduces separate states for:

- semantic model status
- bundle job status
- handoff QA status
- issue status
- delivery status

Required behavior:

- bundle assets may exist before release
- internal review is allowed before release
- official consultant handoff is blocked until QA and architect review pass

## 11. Non-Negotiable Acceptance Bar

Program B Release 1 is not accepted if any of these remain true:

- semantic element identity is not stable enough for issue and schedule linkage
- IFC export is still effectively "minimal placeholder interoperability"
- schedules have no verification or confidence markers
- issues are not tied to version, room, or element references
- delivery workspace hides readiness and issue state behind raw file links only
- release language implies construction-authoring certainty without proof

## 12. Relationship to Future Work

Future Program B expansion may later include:

- authoring seed workflows,
- external tool connectors,
- richer assemblies,
- broader typology coverage,
- and selective continuation into external BIM environments.

Those belong to later Program B releases, not Release 1.

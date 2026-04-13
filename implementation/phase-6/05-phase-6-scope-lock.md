# Phase 6 Scope Lock

*Status: Locked*  
*Decision date: 2026-04-13*  
*Authority: Sponsor direction captured in Codex implementation session*

## 1. Purpose

This document freezes the Phase 6 scope so product, engineering, QA, and DevOps can execute without mixing in BIM authoring or premium CGI requirements.

Phase 6 exists to turn the current placeholder 3D derivation lane into a real presentation-grade 3D delivery workflow.

## 2. Executive Decision Summary

| Area | Locked decision |
|---|---|
| Program in scope | `Program A: Presentation-grade 3D` only |
| Entry condition | locked brief + approved canonical 2D version + issued package metadata |
| Core outputs | `scene.glb`, curated still renders, `walkthrough.mp4`, `presentation_manifest.json` |
| Delivery policy | preview allowed before approval, client release blocked until QA + architect approval pass |
| Viewer policy | replace debug viewer with client-ready presentation viewer |
| Runtime split | app orchestration on app host, render execution on dedicated GPU runtime |
| Storage policy | final 3D artifacts move to object storage, not local Docker volume only |
| Quality policy | placeholder glTF/SVG output is not acceptable as final Phase 6 behavior |
| Explicit non-goals | BIM authoring, construction model, BLEND/USD/FBX premium CGI pipeline |

## 3. Phase Objective

Phase 6 must:

1. convert approved design truth into a deterministic scene specification,
2. generate a consistent 3D presentation bundle from that scene truth,
3. validate the bundle against quality and completeness rules,
4. require architect approval before client delivery,
5. and expose a client-ready presentation workflow in the product.

## 4. In Scope

- `presentation_scene_spec` generation from approved canonical 2D design state
- async 3D job orchestration
- dedicated GLB export lane
- curated still-render pack
- walkthrough MP4 generation
- presentation manifest generation
- 3D QA validator
- degraded preview mode
- architect approval gate
- client delivery-ready 3D viewer and delivery surface
- object-storage-backed artifact handling
- production deployment path for render-capable runtime

## 5. Out of Scope

- full BIM semantic authoring model
- native BIM edit file generation
- construction detailing and issued construction sheets beyond existing 2D package baseline
- premium CGI scene handoff in `BLEND`, `USD`, or `FBX`
- artist-facing DCC workflow
- panorama/VR/AR as mandatory outputs
- structural, MEP, consultant, or fabrication modeling
- automatic conversion of presentation GLB into editable BIM truth

## 6. Source-of-Truth Policy

Phase 6 3D generation must read from:

- locked brief
- approved canonical version
- issued package metadata
- style/material mapping
- presentation directives

Phase 6 must not generate final 3D output directly from:

- raw intake transcript
- prompt-only style text
- a single floor plan image
- unresolved draft geometry

## 7. Required Final Outputs

Every approved Phase 6 package must contain:

- `scene.glb`
- one hero exterior still
- required interior still set for target rooms
- one `walkthrough.mp4`
- `presentation_manifest.json`
- QA report
- approval metadata

Preview-only packages may exist before approval, but they must remain blocked from client issue if degraded or incomplete.

## 8. Delivery State Policy

Phase 6 introduces separate states for:

- render job state
- 3D bundle QA state
- approval state
- delivery state

Required behavior:

- assets may exist before approval
- `preview` is allowed internally
- `client delivery` is blocked until all required gates pass

## 9. Degraded Policy

If the system can generate only partial or low-confidence assets:

- keep the bundle visible internally as preview
- attach visible `DEGRADED` labeling
- record failure reason in QA and manifest
- block final client issue

`DEGRADED` is allowed for internal review. It is not allowed as official client delivery.

## 10. Non-Negotiable Acceptance Bar

Phase 6 is not accepted if any of these remain true:

- the API still returns only sync `model_url + render_urls` as the main contract
- the GPU lane still produces placeholder SVGs as the accepted end state
- the viewer remains a raw debug page
- there is no manifest
- there is no architect approval gate
- artifacts still depend only on local Docker volume paths for final delivery

## 11. Relationship to Future Programs

Program B and Program C are real future programs, but they must not be smuggled into this phase.

If a requirement depends on:

- BIM authoring semantics,
- native editable BIM files,
- construction-authoring workflows,
- premium CGI scene handoff,
- or cinematic artist pipelines,

then that requirement belongs to the independent research brief and not to Phase 6 execution.

Reference:

- `implementation/phase-6/04-independent-research-requirements-for-bim-and-premium-cgi.md`

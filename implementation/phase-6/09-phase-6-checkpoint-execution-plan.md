# Phase 6 Checkpoint Execution Plan

## CP-6.0 Scope Lock and Contract Freeze

Goal:

- freeze Phase 6 to Program A only,
- confirm source-of-truth inputs,
- and lock docs, contracts, and out-of-scope lines.

DoD:

- scope lock approved,
- doc set complete,
- backend/frontend/GPU lanes agree on the same contract.

## CP-6.1 Persistence and Bundle Backbone

Goal:

- add the core entities for bundle, job, asset, QA report, and approval
- and expose the initial bundle-oriented API shape.

DoD:

- persistence exists,
- bundle endpoints respond,
- legacy-only `model_url + render_urls` is no longer the target contract.

## CP-6.2 Scene Spec Builder

Goal:

- transform approved canonical version data into persisted `presentation_scene_spec`
- and validate required inputs.

DoD:

- scene spec is generated deterministically,
- missing upstream inputs are blocked,
- fixture tests cover key typology cases.

## CP-6.3 Async Job Orchestration

Goal:

- replace sync derive flow with queued job orchestration,
- emit progress stages,
- and persist job outcomes.

DoD:

- API enqueues jobs,
- frontend can observe progress,
- retries and failure states are captured.

## CP-6.4 GPU Runtime and Artifact Generation

Goal:

- deploy render-capable runtime,
- generate real GLB, still renders, and walkthrough video,
- and push artifacts into object storage.

DoD:

- GLB exists,
- required still pack exists,
- walkthrough MP4 exists,
- storage keys and signed URLs are registered.

## CP-6.5 QA Validator and Degraded Policy

Goal:

- validate generated bundles,
- record warnings and blocking failures,
- and enforce degraded preview rules.

DoD:

- QA report is produced for every bundle,
- degraded bundles are visible internally,
- degraded bundles cannot be released.

## CP-6.6 Approval Gate and Delivery Integration

Goal:

- add architect approval controls,
- generate release manifest,
- and wire 3D bundle state into delivery workspace.

DoD:

- approval and rejection actions work,
- manifest is generated,
- release state is visible in delivery UI.

## CP-6.7 Presentation Viewer UX

Goal:

- replace debug viewer behavior,
- build a real presentation workspace for stills, video, and GLB,
- and clean up user-facing copy and state communication.

DoD:

- hero image, gallery, video, and model actions exist,
- status chips are clear,
- no raw JSON is shown as primary content.

## CP-6.8 Production Deployment and Validation

Goal:

- deploy the full Phase 6 candidate,
- validate a real end-to-end production run,
- and close the final quality gaps before phase closure.

DoD:

- production deploy succeeds,
- one real project completes the full 3D path,
- approval gate and release state are validated,
- final acceptance evidence is recorded.

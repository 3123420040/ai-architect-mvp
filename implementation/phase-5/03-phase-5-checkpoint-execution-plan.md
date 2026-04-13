# Phase 5 Checkpoint Execution Plan

## CP-5.0 Scope Lock and Production Truth

Goal:

- freeze the Phase 5 problem statement from production evidence,
- capture the exact as-is/to-be contract,
- and lock the artifacts, success criteria, and sequencing rules.

DoD:

- phase docs created,
- checkpoint set locked,
- production evidence references recorded.

## CP-5.1 Intake Chat-Only Workspace

Goal:

- remove suggestion clutter outside the intake chat,
- keep only compact supporting status surfaces,
- and make the conversation the center of the experience.

DoD:

- intake no longer shows large suggestion blocks outside chat,
- build passes,
- UX matches the chat-first direction.

## CP-5.2 Brief Lock Contract

Goal:

- separate readiness from brief lock state,
- expose locked state consistently,
- and make the UI clearly show when the brief is truly complete and confirmed.

DoD:

- backend returns explicit brief contract state,
- frontend shows `Draft`, `Ready to lock`, `Brief locked`,
- tests cover the locked path and reopened path.

## CP-5.3 Conversation Quality Hardening

Goal:

- improve the assistant response contract,
- reduce repetitive or mechanical prompting,
- and make each turn clearer, more tactful, and easier to scan.

DoD:

- assistant payload better prioritizes one or two follow-up asks,
- chat formatting is clean,
- transcript fixtures for tricky cases pass review.

## CP-5.4 Designs Sequence and State Correction

Goal:

- correct project and version sequencing from generation to review,
- remove eager generation stream behavior,
- make the audit trail reflect the true workflow,
- and harden the generation contract so generated options are treated as a distinct lane before review.

DoD:

- generation no longer implies review,
- project state reflects `options generated` before selection,
- audit logs and tests confirm the corrected sequence,
- option-generation deep-dive requirements for generation state and metadata have been applied,
- option strategy and decision metadata slice is wired into the generation contract.

## CP-5.5 Designs Decision Workspace

Goal:

- redesign the `Designs` page into a decision workspace,
- improve option card quality,
- support compare/select actions with professional Vietnamese copy,
- and surface stronger option rationale from the generation lane.

DoD:

- designs page is decision-oriented,
- compare flow exists,
- option cards show useful rationale and metrics,
- option titles/descriptions stop looking like raw technical placeholders,
- strategy profile and decision metadata are visibly consumed by the page,
- screenshot review confirms better UX.

## CP-5.6 Production Validation and Polish

Goal:

- deploy the full Phase 5 candidate,
- test the real production flow,
- patch final UX or sequence regressions before closure,
- and validate that the generated options feel materially more professional to an end user.

DoD:

- production deploy succeeds,
- real-case validation is completed,
- follow-up fixes are redeployed,
- final screenshots and audit notes are saved,
- generation-quality notes are captured against the deep-dive target,
- production notes explicitly assess strategy profile and decision metadata quality.

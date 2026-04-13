# Phase 5 Checkpoints

Phase 5 is locked to:

- `implementation/phase-5/01-phase-5-analysis-brief.md`
- `implementation/phase-5/02-phase-5-implementation-detailed.md`
- `implementation/phase-5/03-phase-5-checkpoint-execution-plan.md`
- `implementation/phase-5/04-phase-5-option-generation-deep-dive.md`
- `implementation/phase-5/05-phase-5-option-strategy-decision-metadata-slice.md`
- `implementation/phase-5/06-phase-5-option-strategy-technical-task-breakdown.md`

## Sequence

| Order | Code | Checkpoint | Depends On | Target |
|---|---|---|---|---|
| 0 | `cp0-phase5-scope-truth` | Scope Lock and Production Truth | — | Freeze the exact product problem, production evidence, and acceptance contract |
| 1 | `cp1-intake-chat-only-workspace` | Intake Chat-Only Workspace | `cp0-phase5-scope-truth` | Remove suggestion clutter and make the conversation the primary workspace |
| 2 | `cp2-brief-lock-contract` | Brief Lock Contract | `cp1-intake-chat-only-workspace` | Add explicit brief lock states and consistent FE/BE contract |
| 3 | `cp3-conversation-quality` | Conversation Quality Hardening | `cp2-brief-lock-contract` | Improve assistant turns, prompt prioritization, and chat formatting |
| 4 | `cp4-designs-sequence-state` | Designs Sequence and State Correction | `cp3-conversation-quality` | Fix project/version sequencing from generation into review |
| 5 | `cp5-designs-decision-workspace` | Designs Decision Workspace | `cp4-designs-sequence-state` | Redesign `Designs` into a compare-and-choose workspace |
| 6 | `cp6-production-validation-polish` | Production Validation and Polish | `cp5-designs-decision-workspace` | Deploy, validate on production truth, and close final UX gaps |

## Notes

- Phase 5 intentionally narrows scope around the two highest-friction user moments: clarification and option decision.
- Phase 5 must preserve compatibility with the Phase 3 package/export baseline.
- CP4, CP5, and CP6 must additionally follow the option-generation contract in `implementation/phase-5/04-phase-5-option-generation-deep-dive.md`.
- CP4, CP5, and CP6 must also follow the lane-specific contract in `implementation/phase-5/05-phase-5-option-strategy-decision-metadata-slice.md`.
- Production truth remains the final acceptance gate.

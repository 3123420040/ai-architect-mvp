# CP0 — Phase 2 Readiness Gate

**Code:** cp0-phase2-readiness  
**Order:** 0  
**Depends On:** —  
**Estimated Effort:** 0.5 day

## Mục tiêu

Lock lại prerequisite cho Phase 2 trước khi code: Layer 1.5 baseline, data contract, export contract, repo/runtime/deploy assumptions, và trạng thái production hiện tại.

## Artifacts dự kiến

| File/Path | Action | Mô tả |
|-----------|--------|-------|
| `.phase.json` | updated | Chuyển phase hiện tại sang `phase-2` |
| `docs/phases/phase-2/checkpoints/README.md` | created | Index checkpoint cho Phase 2 |
| `docs/phases/phase-2/checkpoints/cp0-phase2-readiness/*` | created | Readiness checkpoint package |

## Checklist Validator

| ID | Mô tả | Blocker |
|----|-------|---------|
| CHECK-01 | `.phase.json` co `current=phase-2` va phase metadata hop le | ✓ |
| CHECK-02 | Phase 2 checkpoint index map dung 7 CP theo tai lieu | ✓ |
| CHECK-03 | Docker-based production path duoc xac nhan tu compose va deploy scripts | ✓ |


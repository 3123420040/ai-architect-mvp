# CP9 — Conversation Style Inference

**Mục tiêu:** Infer design intent and style from natural conversation while minimizing homeowner burden.
**Requires:** CP8 PASS.

## Steps

1. Add `CustomerUnderstanding` with facts, inferred needs, style signals, image signals, missing blockers, and assumptions.
2. Add a deterministic first-pass Vietnamese signal extractor for site, family, rooms, lifestyle, style words, likes, and dislikes.
3. Add `StyleInferenceResult` with ranked candidates, evidence, confidence, and `needs_confirmation`.
4. Support image descriptors as structured input; full image model integration can be deferred.
5. Add tests for sparse Vietnamese prompts and uploaded-reference descriptors.

## Verification

```bash
cd /Users/nguyenquocthong/project/ai-architect/ai-architect-api
PYTHONPATH=. .venv/bin/python -m pytest tests/test_design_intelligence_style_inference.py
PYTHONPATH=. .venv/bin/python -m pytest tests/test_briefing.py
```

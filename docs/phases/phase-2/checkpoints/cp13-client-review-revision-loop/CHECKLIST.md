# CP13 Validation Checklist — Client Review Revision Loop

## CHECK-01: Feedback Parsing

```bash
cd /Users/nguyenquocthong/project/ai-architect/ai-architect-api
PYTHONPATH=. .venv/bin/python -m pytest tests/test_concept_revision_loop.py -q
```

**Expected:** Natural feedback becomes structured operations.

## CHECK-02: Version Safety

**Expected:** Revisions produce a child version with changelog and preserve parent evidence.
**Fail if:** Revision mutates the old package silently.

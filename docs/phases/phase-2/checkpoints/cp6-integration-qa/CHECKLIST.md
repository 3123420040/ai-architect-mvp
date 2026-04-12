# CP6 Validation Checklist — Integration + QA

**Dành cho:** Validator Agent  
**Mục tiêu:** Verify Phase 2 da duoc ship va validate tren production lane.

## Danh sách kiểm tra

### CHECK-01: API tests pass

```bash
cd /Users/nguyenquocthong/project/ai-architect-api && pytest -q
```

**Expected:** test suite pass  
**Fail if:** co regression o flow generation/review/export/handoff

### CHECK-02: Web production build passes

```bash
cd /Users/nguyenquocthong/project/ai-architect-web && pnpm build
```

**Expected:** build pass  
**Fail if:** compile/type/runtime build fail

### CHECK-03: Production loop artifact exists

```bash
test -f /Users/nguyenquocthong/project/ai-architect-mvp/artifacts/production-checks/latest-report.json && echo ok
```

**Expected:** in `ok`  
**Fail if:** khong co artifact production check


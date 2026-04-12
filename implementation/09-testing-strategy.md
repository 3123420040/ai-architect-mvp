# 09 - Testing Strategy

*Version: 1.0 FINAL*
*Ngay chot: Apr 11, 2026*

---

## 1. Testing Pyramid

```
         /\
        /  \         E2E Tests (Playwright)
       / 10 \        Full user flows, critical paths
      /______\
     /        \      Integration Tests
    /    30    \     API endpoints, DB queries, service calls
   /____________\
  /              \   Unit Tests
 /      60       \   Domain logic, state machine, utils
/________________\
```

- **60% Unit** - Nhanh, chay moi commit
- **30% Integration** - API + DB, chay moi PR
- **10% E2E** - Full browser, chay truoc merge vao main

---

## 2. Backend Testing (ai-architect-api)

### 2.1 Stack

| Tool | Dung cho |
|------|----------|
| pytest | Test runner |
| pytest-asyncio | Async test support |
| pytest-cov | Coverage reporting |
| httpx | Async HTTP client for API tests |
| factory-boy | Test data factories |
| testcontainers | Docker-based PostgreSQL for integration |

### 2.2 Unit Tests - MUST HAVE

| Module | What to test | Priority |
|--------|-------------|----------|
| **Version State Machine** | All valid transitions, all invalid transitions rejected | P0 |
| **Permission Classifier** | Role checks, ownership checks, state-based checks | P0 |
| **Handoff Readiness** | All conditions: locked + approved + exports exist | P0 |
| **Brief Validation** | Valid brief JSON, missing fields, invalid values | P0 |
| **Audit Trail** | Log created for every state change | P0 |
| **Recovery Levels** | Level 1-5 escalation logic | P0 |
| **Tool Orchestrator** | READ concurrent, WRITE exclusive partitioning | P0 |
| **Context Management** | Truncation, microcompact triggers | P1 |

**State Machine Test Example:**
```python
# tests/unit/test_state_machine.py

class TestVersionStateMachine:
    def test_draft_to_generated(self):
        version = VersionFactory(status="draft")
        transition_version(version, "generated", actor=user)
        assert version.status == "generated"
    
    def test_draft_to_approved_invalid(self):
        version = VersionFactory(status="draft")
        with pytest.raises(InvalidTransition):
            transition_version(version, "approved", actor=user)
    
    def test_locked_is_immutable(self):
        version = VersionFactory(status="locked")
        with pytest.raises(InvalidTransition):
            transition_version(version, "draft", actor=user)
    
    def test_reject_does_not_transition_creates_new(self):
        version = VersionFactory(status="under_review")
        transition_version(version, "rejected", actor=kts)
        assert version.status == "rejected"
        # New version should be created by revision flow, not state machine
    
    @pytest.mark.parametrize("from_status,to_status", [
        ("draft", "generated"),
        ("generated", "under_review"),
        ("under_review", "approved"),
        ("approved", "locked"),
        ("locked", "handoff_ready"),
        ("handoff_ready", "delivered"),
    ])
    def test_happy_path_transitions(self, from_status, to_status):
        version = VersionFactory(status=from_status)
        transition_version(version, to_status, actor=kts)
        assert version.status == to_status
```

**Permission Test Example:**
```python
# tests/unit/test_permissions.py

class TestPermissions:
    def test_user_cannot_approve(self):
        user = UserFactory(role="user")
        version = VersionFactory(status="under_review")
        with pytest.raises(Forbidden):
            check_permission(user, "approve", version)
    
    def test_architect_can_approve_own_org(self):
        kts = UserFactory(role="architect", org_id="org1")
        version = VersionFactory(status="under_review", org_id="org1")
        check_permission(kts, "approve", version)  # No exception
    
    def test_architect_cannot_approve_other_org(self):
        kts = UserFactory(role="architect", org_id="org1")
        version = VersionFactory(status="under_review", org_id="org2")
        with pytest.raises(Forbidden):
            check_permission(kts, "approve", version)
    
    def test_export_requires_approved_status(self):
        kts = UserFactory(role="architect")
        version = VersionFactory(status="draft")
        with pytest.raises(Forbidden):
            check_permission(kts, "export", version)
```

### 2.3 Integration Tests - MUST HAVE

| Endpoint | What to test | Priority |
|----------|-------------|----------|
| POST /auth/register | Create user + org, JWT returned | P0 |
| POST /auth/login | Valid creds -> token, invalid -> 401 | P0 |
| POST /projects | Create project, saved to DB | P0 |
| GET /projects | List with filter, pagination | P0 |
| PUT /projects/{id}/brief | Save brief JSON, validated | P0 |
| POST /projects/{id}/generate | Job created, queued | P0 |
| POST /reviews/{id}/approve | State transition, audit log | P0 |
| POST /reviews/{id}/reject | Requires reason, state change | P0 |
| POST /versions/{id}/annotations | Pin saved with coordinates | P0 |
| POST /exports/{id} | Job created, file generated | P0 |
| GET /share/{token} | Valid token returns data, expired returns 404 | P0 |

**Integration Test Example:**
```python
# tests/integration/test_review_flow.py

class TestReviewFlow:
    async def test_full_review_approve_flow(self, client, db):
        # Setup
        user = await create_user(db, role="architect")
        project = await create_project(db, kts_user_id=user.id)
        version = await create_version(db, project_id=project.id, status="under_review")
        
        # Add annotation
        resp = await client.post(
            f"/api/v1/versions/{version.id}/annotations",
            json={"x": 0.5, "y": 0.3, "comment": "OK"},
            headers=auth_headers(user)
        )
        assert resp.status_code == 201
        
        # Approve
        resp = await client.post(
            f"/api/v1/reviews/{version.id}/approve",
            json={"comment": "LGTM"},
            headers=auth_headers(user)
        )
        assert resp.status_code == 200
        
        # Verify state
        version = await db.get(DesignVersion, version.id)
        assert version.status == "locked"
        assert version.locked_at is not None
        
        # Verify audit log
        logs = await db.query(AuditLog).filter_by(version_id=version.id).all()
        assert any(log.action == "approve" for log in logs)
```

### 2.4 Coverage Targets

| Area | Minimum Coverage |
|------|-----------------|
| State machine | 100% |
| Permissions | 100% |
| API endpoints | 80% |
| Services | 70% |
| Overall | 75% |

---

## 3. Frontend Testing (ai-architect-web)

### 3.1 Stack

| Tool | Dung cho |
|------|----------|
| Vitest | Unit test runner |
| React Testing Library | Component tests |
| Playwright | E2E browser tests |
| MSW (Mock Service Worker) | API mocking for component tests |

### 3.2 Component Tests - MUST HAVE

| Component | What to test | Priority |
|-----------|-------------|----------|
| StatusBadge | All 8 statuses render correct color + text | P0 |
| OptionCard | Image loads, select button works, selected state | P0 |
| ReviewActions | Approve/reject buttons, reject requires reason | P0 |
| ChatInterface | Send message, receive response, auto-scroll | P0 |
| IntakeForm | Step navigation, validation, submit | P0 |
| GenerationProgress | Progress bar updates, stage text changes | P0 |
| AnnotationLayer | Click adds pin, pin shows comment | P0 |
| BriefEditor | Display brief, edit fields, save | P0 |

**Component Test Example:**
```typescript
// components/common/__tests__/status-badge.test.tsx

describe('StatusBadge', () => {
  const statuses = [
    { status: 'draft', text: 'Draft', color: 'status-draft' },
    { status: 'generating', text: 'Generating', color: 'status-generating' },
    { status: 'approved', text: 'Approved', color: 'status-approved' },
    { status: 'rejected', text: 'Rejected', color: 'status-rejected' },
    { status: 'locked', text: 'Locked', color: 'status-locked' },
  ]

  statuses.forEach(({ status, text }) => {
    it(`renders ${status} correctly`, () => {
      render(<StatusBadge status={status} />)
      expect(screen.getByText(text)).toBeInTheDocument()
    })
  })
})
```

### 3.3 E2E Tests - MUST HAVE

| Flow | Steps | Priority |
|------|-------|----------|
| Auth flow | Register -> Login -> See dashboard | P0 |
| Intake flow | Create project -> Chat -> Brief confirmed | P0 |
| Generation flow | Brief confirmed -> Generate -> See 3 options -> Select | P0 |
| Review flow | KTS opens review -> Annotate -> Approve | P0 |
| Export flow | Locked version -> Export PDF -> Download | P0 |
| Share flow | Create share link -> Open -> Submit feedback | P0 |
| Revision flow | Feedback -> AI revise -> New version created | P0 |

**E2E Test Example:**
```typescript
// e2e/review-flow.spec.ts

test('KTS can review and approve a design', async ({ page }) => {
  // Login as KTS
  await page.goto('/login')
  await page.fill('[name="email"]', 'kts@test.com')
  await page.fill('[name="password"]', 'password')
  await page.click('button[type="submit"]')
  
  // Navigate to review
  await page.goto('/projects/test-project/review')
  
  // Add annotation
  await page.click('.floor-plan-viewer', { position: { x: 300, y: 200 } })
  await page.fill('[name="annotation-comment"]', 'Cua so ok')
  await page.click('button:has-text("Save")')
  
  // Approve
  await page.click('button:has-text("Approve")')
  
  // Verify
  await expect(page.locator('.status-badge')).toHaveText('Locked')
})
```

---

## 4. GPU Service Testing (ai-architect-gpu)

### 4.1 Unit Tests
- Workflow JSON validation
- Post-processing functions (label overlay, resize)
- API schema validation

### 4.2 Integration Tests (requires GPU)
- ComfyUI workflow execution
- Diffusers pipeline fallback
- S3 upload after generation
- Webhook callback

### 4.3 Quality Tests (manual + automated)
- Floor plan visual quality checklist
- Render consistency (same seed = similar output)
- Resolution check (>= 2048px)

---

## 5. Quality Gates

### 5.1 PR Merge Gate

```
[ ] CI passes (lint + type check + unit tests + integration tests)
[ ] Coverage >= threshold
[ ] No new Sentry errors
[ ] 1 approval from team member
[ ] API contract changes reviewed by cross-team
```

### 5.2 Checkpoint Merge Gate (develop -> main)

```
[ ] All PR gates passed
[ ] E2E tests pass on staging
[ ] Demo to PM completed
[ ] No P0 bugs open
[ ] Performance metrics within NFR targets
```

### 5.3 Production Deploy Gate

```
[ ] All checkpoint gates passed
[ ] Security audit completed
[ ] Load test passed (50 concurrent users)
[ ] Rollback tested
[ ] Monitoring + alerting active
```

---

## 6. Test Data Strategy

### 6.1 Factories (Backend)

```python
# tests/factories.py
class UserFactory(factory.Factory):
    class Meta:
        model = User
    
    email = factory.Sequence(lambda n: f"user{n}@test.com")
    full_name = factory.Faker("name", locale="vi_VN")
    role = "architect"
    organization = factory.SubFactory(OrganizationFactory)

class ProjectFactory(factory.Factory):
    class Meta:
        model = Project
    
    name = factory.Faker("sentence", nb_words=3)
    client_name = factory.Faker("name", locale="vi_VN")
    organization = factory.SubFactory(OrganizationFactory)

class VersionFactory(factory.Factory):
    class Meta:
        model = DesignVersion
    
    status = "draft"
    version_number = factory.Sequence(lambda n: n + 1)
    project = factory.SubFactory(ProjectFactory)
    brief_json = {
        "lot": {"width_m": 5, "depth_m": 20, "orientation": "south", "area_m2": 100},
        "floors": 4,
        "rooms": [{"type": "living", "floor": 1, "min_area_m2": 20}],
        "style": "modern_minimalist"
    }
```

### 6.2 Seed Data (Development)

```python
# scripts/seed_dev_data.py
# Tao du lieu mau de dev test UI

def seed():
    org = create_organization("Studio Demo")
    kts = create_user("kts@demo.com", role="architect", org=org)
    user = create_user("user@demo.com", role="user", org=org)
    
    project = create_project("Nha pho Tan Binh", kts=kts, org=org)
    
    # Version 1: rejected
    v1 = create_version(project, status="rejected", version_number=1)
    
    # Version 2: locked (approved)
    v2 = create_version(project, status="locked", version_number=2, parent=v1)
    add_sample_floor_plans(v2)
    add_sample_renders(v2)
    
    # Version 3: under_review
    v3 = create_version(project, status="under_review", version_number=3, parent=v2)
    add_sample_floor_plans(v3)
    add_annotations(v3, kts)
```

---

## 7. Test Automation Schedule

| When | What runs | Where |
|------|-----------|-------|
| Every commit (local) | Pre-commit: lint + format | Developer machine |
| Every PR | CI: lint + type check + unit + integration | GitHub Actions |
| Merge to develop | CI + E2E on staging | GitHub Actions + Playwright |
| Merge to main | Full suite + load test | GitHub Actions |
| Daily (cron) | E2E regression on staging | GitHub Actions scheduled |
| Pre-release | Security scan + penetration test | Manual + automated |

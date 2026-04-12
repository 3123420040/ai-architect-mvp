# CP0 Validation Checklist — Phase 2 Readiness Gate

**Dành cho:** Validator Agent  
**Mục tiêu:** Verify Phase 2 da duoc mo dung cach va checkpoint chain hop le.

## Danh sách kiểm tra

### CHECK-01: Phase state updated

```bash
python3 - <<'PY'
import json
from pathlib import Path
payload = json.loads(Path('/Users/nguyenquocthong/project/ai-architect-mvp/.phase.json').read_text())
assert payload['current'] == 'phase-2'
assert 'phase-2' in payload['phases']
print('ok')
PY
```

**Expected:** lenh in `ok`  
**Fail if:** khong co `phase-2` hoac `current` khac `phase-2`

### CHECK-02: Checkpoint index exists

```bash
test -f /Users/nguyenquocthong/project/ai-architect-mvp/docs/phases/phase-2/checkpoints/README.md && echo ok
```

**Expected:** in `ok`  
**Fail if:** khong co phase-2 checkpoint index

### CHECK-03: Production deploy path stays Docker-first

```bash
rg -n "docker compose|cloudflared|caddy|../ai-architect-api|../ai-architect-web|../ai-architect-gpu" /Users/nguyenquocthong/project/ai-architect-mvp/docker-compose.production.yml /Users/nguyenquocthong/project/ai-architect-mvp/scripts/deploy_public_production.sh
```

**Expected:** co match cho compose production path  
**Fail if:** deploy path khong con Docker-based


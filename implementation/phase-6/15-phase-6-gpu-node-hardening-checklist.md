# Phase 6 GPU Node Hardening Checklist

## 1. Purpose

This document explains, in simple and implementation-facing language, what the team must do to move the current Phase 6 GPU service from:

- `service is alive but running without real GPU acceleration`

to:

- `production-ready GPU node with real hardware-backed rendering`

This is a hardening checklist for infra and runtime.

It is not a product-scope document.

## 2. Current Reality

Today, the Phase 6 render service is working as an application service, but not as a true GPU node.

What is true right now:

- the `gpu` container is up
- `/health` returns `200`
- `/presentation/render` can return artifacts
- the Phase 6 pipeline can complete end-to-end

What is **not** true right now:

- the host does not expose NVIDIA GPU hardware
- `nvidia-smi` is not available on the host
- the container is running with `runc`, not an NVIDIA runtime
- Docker does not pass any GPU devices into the container
- the current image is a lightweight Python image, not a CUDA/Blender render runtime
- health reports `gpu_available: false`

## 3. Target Outcome

The target state is:

- host has a real NVIDIA GPU
- host driver is healthy
- Docker can see the GPU
- the `gpu` container can see the GPU
- the render runtime can use the GPU intentionally
- `/health` reports `gpu_available: true`
- Phase 6 jobs can produce the same artifact set, but on a real GPU-backed node

Minimum target artifact set remains:

- `scene.glb`
- curated still renders
- `walkthrough.mp4`
- `presentation_manifest.json`
- `qa_report.json`

## 4. Important Decision

The recommended direction is:

**Do not try to force real GPU hosting onto the current app node if that node does not already have NVIDIA support.**

Preferred deployment shape:

- app node: `web + api + worker + postgres + redis`
- GPU node: `gpu runtime only`

Reason:

- easier driver management
- lower blast radius
- better render isolation
- easier scale-up later

## 5. Hard Gates

Do **not** call the system a "real GPU node" until all of these are true:

1. `nvidia-smi` works on the host
2. `docker run --gpus all ... nvidia-smi` works
3. GPU container health reports `gpu_available: true`
4. a live `/presentation/render` probe succeeds on the GPU node
5. a real Phase 6 bundle succeeds using that node
6. logs and metadata clearly show that the render used GPU, not CPU fallback

## 6. Checklist

### A. Host Readiness

- [ ] Provision a Linux host with a real NVIDIA GPU
- [ ] Confirm the host is intended for production rendering, not general web/API traffic
- [ ] Confirm enough VRAM for the target render workload
- [ ] Confirm enough SSD/NVMe disk for scratch frames, temporary scenes, and video assembly
- [ ] Confirm enough RAM and CPU headroom for Blender/encoding support tasks

Validation:

```bash
uname -a
lspci | grep -i nvidia
nvidia-smi
df -h
free -h
```

Exit condition:

- host sees the NVIDIA device
- `nvidia-smi` returns clean output

### B. NVIDIA Driver and Runtime

- [ ] Install a stable NVIDIA driver on the host
- [ ] Install `nvidia-container-toolkit`
- [ ] Restart Docker after toolkit setup
- [ ] Confirm Docker can expose GPU devices to containers

Validation:

```bash
nvidia-smi
docker run --rm --gpus all nvidia/cuda:12.4.1-base-ubuntu22.04 nvidia-smi
```

Exit condition:

- both host and container-level `nvidia-smi` work

### C. Compose and Container Binding

- [ ] Add explicit GPU binding for the `gpu` service
- [ ] Ensure only the render service gets GPU access unless another service truly needs it
- [ ] Keep the API and worker pointing to the GPU node using a stable `GPU_SERVICE_URL`
- [ ] If GPU is on a separate host, confirm network reachability and firewall rules

Example direction:

```yaml
gpu:
  build:
    context: ../ai-architect-gpu
  gpus: all
  environment:
    APP_NAME: KTC KTS GPU
    APP_ENV: production
    APP_PORT: 8001
    NVIDIA_VISIBLE_DEVICES: all
    NVIDIA_DRIVER_CAPABILITIES: compute,utility,video
```

Exit condition:

- `docker inspect` shows GPU device requests
- the running container can execute `nvidia-smi`

### D. GPU Runtime Image

- [ ] Replace the lightweight CPU image with a CUDA-compatible runtime image
- [ ] Install all runtime dependencies needed for real rendering
- [ ] Install Blender headless or the actual chosen render engine
- [ ] Keep `ffmpeg` for video encoding
- [ ] Add startup checks so the container fails fast when GPU prerequisites are missing

What is missing in the current image:

- CUDA runtime
- Blender/headless render engine
- explicit GPU render backend

Exit condition:

- image boot logs confirm the expected render engine is available
- the render runtime can intentionally select GPU mode

### E. Application Health Contract

- [ ] Extend `/health` beyond just `gpu_available`
- [ ] Return enough data for ops and deploy validation

Recommended fields:

- `gpu_available`
- `gpu_name`
- `driver_version`
- `cuda_version`
- `renderer_backend`
- `render_device`
- `blender_available`
- `ffmpeg_available`

Exit condition:

- the health payload can prove whether the node is actually GPU-backed

### F. Scratch Storage and Artifact Safety

- [ ] Separate durable output storage from scratch render storage
- [ ] Keep final artifacts durable
- [ ] Keep scratch files disposable
- [ ] Add cleanup rules for abandoned temp files and frame sequences
- [ ] Confirm scratch storage does not fill the root disk

Recommended separation:

- `/app/storage` for final released artifacts
- `/app/scratch` for render temp files, frame caches, transient scenes

Exit condition:

- long video renders do not fill the main app disk unexpectedly

### G. Observability and Logs

- [ ] Add logs that say whether each job used GPU or CPU fallback
- [ ] Capture render duration
- [ ] Capture queue wait time
- [ ] Capture error stage
- [ ] Capture GPU identity in runtime metadata

Minimum runtime metadata to persist:

- `renderer_backend`
- `render_device`
- `gpu_name`
- `driver_version`
- `render_started_at`
- `render_finished_at`

Exit condition:

- after any failed or slow job, ops can tell whether the problem is infra, queue, or renderer

### H. Security and Isolation

- [ ] Avoid putting database or public web traffic on the GPU node if not required
- [ ] Restrict inbound access to the GPU service
- [ ] Expose the GPU service only to trusted internal callers
- [ ] Keep secrets off the GPU image itself
- [ ] Use the minimum open ports needed

Exit condition:

- GPU node is not acting as a general public application server

### I. Production Cutover

- [ ] Point `GPU_SERVICE_URL` to the new GPU node
- [ ] Keep one rollback path ready
- [ ] Run a smoke render before switching normal traffic
- [ ] Run one full Phase 6 bundle after cutover
- [ ] Only then mark the node production-ready

Exit condition:

- one real Phase 6 bundle succeeds against the new GPU node without manual intervention

## 7. Acceptance Test Checklist

The team must pass these in order.

### Test 1. Host GPU check

- [ ] `nvidia-smi` on host returns clean output

### Test 2. Docker GPU check

- [ ] `docker run --gpus all ... nvidia-smi` passes

### Test 3. Service health check

- [ ] `/health` returns `gpu_available: true`
- [ ] `/health` includes real GPU metadata

### Test 4. Runtime probe

- [ ] `/presentation/render` probe succeeds
- [ ] output metadata shows GPU device usage

### Test 5. Full Phase 6 bundle

- [ ] create one approved source version
- [ ] issue package
- [ ] create presentation job
- [ ] wait for completion
- [ ] verify:
  - `scene.glb`
  - still renders
  - `walkthrough.mp4`
  - `presentation_manifest.json`
  - `qa_report.json`
- [ ] architect approval gate still works

### Test 6. Failure fallback test

- [ ] temporarily simulate GPU unavailable condition
- [ ] verify the service reports the condition clearly
- [ ] verify the system does not silently claim GPU usage when running CPU fallback

## 8. What Should Be Changed in Code

This checklist is mainly infra-facing, but several code changes should accompany it.

- [ ] update GPU Dockerfile to a real render runtime
- [ ] update `docker-compose.production.yml` or the GPU-host compose to bind GPU devices
- [ ] upgrade the GPU `/health` response
- [ ] add runtime metadata persistence for GPU/CPU mode
- [ ] add explicit degraded-mode behavior when GPU is unavailable

## 9. Recommended Rollout Sequence

Use this order.

1. Prepare a separate Linux GPU node
2. Install driver and NVIDIA container runtime
3. Pass host and Docker GPU smoke tests
4. Upgrade the GPU image/runtime
5. Upgrade the health contract
6. Run direct render probe
7. Point `GPU_SERVICE_URL` to the GPU node
8. Run one full Phase 6 production smoke
9. Only then call the GPU lane production-ready

## 10. Simple Go / No-Go Rule

### Go

You may say the GPU node is ready when:

- health says `gpu_available: true`
- runtime probe passes
- full Phase 6 bundle passes
- logs show real GPU execution

### No-Go

You must **not** call it ready if any of these are still true:

- host has no `nvidia-smi`
- Docker has no GPU binding
- health still says `gpu_available: false`
- the renderer only works through CPU fallback
- the team cannot prove that production bundles were rendered on GPU

## 11. Final Verdict for Current Environment

Current environment status:

- application service health: **PASS**
- Phase 6 render service reachability: **PASS**
- real GPU node readiness: **FAIL**

Meaning:

The service is operational, but the infrastructure is not yet a true GPU production node.

The blocker is infrastructure/runtime enablement, not the Phase 6 API contract itself.

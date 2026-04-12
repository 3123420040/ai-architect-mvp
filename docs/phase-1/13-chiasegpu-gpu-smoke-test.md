# 13 - ChiaseGPU A5000 Smoke Test

*Updated: Apr 11, 2026*

## Target

- Provider: `ChiaseGPU`
- Host: `e1.chiasegpu.vn`
- SSH: `root@e1.chiasegpu.vn -p 43205`
- Public GPU API port: `http://e1.chiasegpu.vn:63468`
- Public secondary port: `http://e1.chiasegpu.vn:24478`
- GPU: `1 x NVIDIA RTX A5000`

## What Was Verified

### SSH and runtime access

- SSH login succeeded.
- Container hostname during test: `bc85ebe0614e`
- OS: `Ubuntu 20.04.6 LTS`

### GPU visibility

- `nvidia-smi` succeeded.
- Driver version: `570.133.07`
- CUDA version reported by driver: `12.8`
- GPU memory: `24564 MiB`

### Container resources observed

- Container CPU allocation: `6 cores`
- Container RAM allocation: about `12 GiB`
- Container storage allocation: `50 GiB`
- Host overlay free disk during session: about `130 GiB`

### Public port mapping

- `8001` was reachable through public address and returned health successfully.
- `8188` was reachable through public address and served HTTP successfully.

### Python GPU runtime test

- System Python available: `Python 3.8.10`
- `python3-pip`, `python3-venv`, `git`, `curl`, `lsof` were installed successfully.
- Virtualenv created at `/workspace/kts-gpu-test/.venv`
- `torch==2.4.1+cu121` installed successfully.
- `torch.cuda.is_available()` returned `True`.
- CUDA smoke compute passed with matrix multiplication on `cuda:0`.

## Temporary Services Started

### Port 8001

- Temporary FastAPI GPU smoke service started.
- Endpoints verified:
  - `GET /health`
  - `POST /generate/floor-plan`
  - `POST /derive/model`

### Port 8188

- Temporary static HTTP server started as placeholder for future ComfyUI exposure.

## Key Findings

### Good news

- ChiaseGPU container works for real GPU Python execution, not just placeholder networking.
- The chosen `RTX A5000` is valid for early CP3 smoke and pipeline bring-up.
- Public port exposure from ChiaseGPU works and can be integrated from API/backend.

### Constraints still blocking full CP3 production-quality setup

- Current base runtime is too old: `Python 3.8`.
- Current container memory is low for the intended stack: about `12 GiB`.
- Current disk is low for models/workflows/cache: `50 GiB`.
- Current image is not actually a ready-to-use PyTorch workspace despite the panel label; bootstrap was needed manually.

## Verdict

### Enough to continue

Current container is enough for:

- remote GPU smoke tests
- API integration tests
- placeholder GPU boundary deployment
- initial PyTorch CUDA validation

### Not enough yet for full CP3 real pipeline

Current container is not a good final base for:

- `ComfyUI + SDXL + ControlNet` full setup
- larger model cache
- durable iteration on workflow graphs
- CP5 `Blender` or heavier render tasks

## Recommended Next Step

Either:

1. Recreate or resize to at least:
   - `8 CPU`
   - `32 GB RAM`
   - `120 GB disk`
   - preferably `Ubuntu 22.04` or runtime with `Python 3.10+`

Or:

2. Keep this container only for short smoke/integration work, then provision a stronger one for real generation.

## Commands Verified During Test

```bash
nvidia-smi
python -c "import torch; print(torch.cuda.is_available())"
curl http://127.0.0.1:8001/health
curl http://e1.chiasegpu.vn:63468/health
curl -X POST http://e1.chiasegpu.vn:63468/generate/floor-plan
```

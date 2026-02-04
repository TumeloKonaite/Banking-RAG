# Changelog

All notable changes to this project will be documented in this file.

## [1.0.0] - 2026-02-04

### Added
- FastAPI + Gradio demo app for banking-document RAG.
- Artifact build pipeline with manifest checks.
- `/health` and `/ready` endpoints for liveness/readiness.
- Demo-mode API key auth (`X-API-Key`) and request validation limits.
- AWS CDK deployment to ECS Fargate behind an ALB.
- Operations runbook at `docs/ops.md` for monitoring and redeploy.

### Improved
- CI workflow covering lint, byte-compile, tests, and Docker build.
- README setup/deploy guidance and troubleshooting notes.

### Known limitations
- Demo-focused setup (not a production banking platform).
- Single-service MVP deployment profile.
- Artifact/config mismatch requires rebuild and redeploy.

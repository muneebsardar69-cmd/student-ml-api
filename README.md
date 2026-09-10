# Student ML API - MLOps Assignment

Professional ML prediction API with complete MLOps workflow.

## Quick Start

### Run Locally
```bash
pip3 install -r requirements.txt
python3 app.py
curl http://localhost:5000/health
```

### Run with Docker
```bash
docker run -d -p 5000:5000 ghcr.io/muneebsardar69-cmd/student-ml-api:1.1.0
curl http://localhost:5000/health
```

## API Endpoints

### GET /health
```bash
curl http://localhost:5000/health
# Returns: {"status":"healthy","application":"student-ml-api","application_version":"1.1.0","model_version":"model-1"}
```

### POST /predict
```bash
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{"value": 10}'
# Returns: {"input":10,"prediction":20}
```

## Versions Released

- **v1.0.0** - Initial release
- **v1.1.0** - Added model metadata

## GitHub Links

- Repository: https://github.com/muneebsardar69-cmd/student-ml-api
- Releases: https://github.com/muneebsardar69-cmd/student-ml-api/releases
- Actions: https://github.com/muneebsardar69-cmd/student-ml-api/actions

## Technologies

- Python 3.10 with Flask 3.1.3
- Docker containerization
- GitHub Actions CI/CD
- GitHub Container Registry (GHCR)

## Key Features

✓ Automated testing (4 tests)
✓ CI/CD pipeline (GitHub Actions)
✓ Docker best practices
✓ Semantic versioning
✓ Instant rollback
✓ Complete traceability

## Evidence

All screenshots and proofs are in the `evidence/` folder showing:
- CI/CD pipelines passing
- Docker builds and layer caching
- API endpoint testing
- Failure analysis and fixes
- Version rollback demonstration

## Failure Analysis

See FAILURE_ANALYSIS.md for detailed documentation of:
- Broken test failure (caught by CI)
- Empty Dockerfile error (caught by CI)
- GHCR permission denied (caught and fixed)

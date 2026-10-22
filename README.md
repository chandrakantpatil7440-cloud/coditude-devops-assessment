# Coditude DevOps Assessment

Next.js frontend, FastAPI backend, and PostgreSQL with Docker, AWS CloudFormation, and GitHub Actions.

## Technology Stack
- Frontend: Next.js, React, TypeScript
- Backend: Python, FastAPI, Uvicorn
- Database: PostgreSQL
- Containers: Docker and Docker Compose
- Infrastructure as Code: AWS CloudFormation
- CI/CD: GitHub Actions

## Repository Structure
- app/frontend - Next.js frontend
- app/backend - FastAPI backend
- infra/cloudformation - network, security, database, ECR, and ECS templates
- .github/workflows/ci.yml - application build and health checks
- .github/workflows/infra-validate.yml - CloudFormation template linting
- docs/architecture.md - architecture details
- docs/architecture-diagram.md - intended architecture diagram
- docs/ci-cd.md - pipeline design and deployment recommendations
- docs/deployment.md - deployment guide

## Run Locally
Prerequisites: Docker Desktop and Docker Compose.

```powershell
docker compose up --build -d
docker compose ps
```

Endpoints:
- Frontend: http://localhost:3000
- Backend health: http://localhost:8000/health
- Database health: http://localhost:8000/health/db

Stop the application:
```powershell
docker compose down
```

## CI/CD
Application CI builds the frontend, builds the backend Docker image, and checks the backend health endpoint.
Infrastructure validation runs cfn-lint against CloudFormation templates. It does not deploy AWS resources.
See docs/ci-cd.md.

## Security
- Do not commit credentials or .env files.
- Keep PostgreSQL private and restrict access with security groups.
- Use Secrets Manager and least-privilege IAM roles.
- Add HTTPS, monitoring, backups, and production approvals before production use.

## Deployment Status
- Local Docker Compose and health checks were previously tested successfully.
- GitHub Actions workflows are configured; check the Actions tab for current results.
- AWS deployment is pending because an AWS Organizations service control policy denies CloudFormation operations.
- The architecture diagram describes the intended design, not a deployed environment.
- Production readiness requires successful AWS deployment and end-to-end security and operational testing.

# CI/CD Design

## Application CI
Workflow: `.github/workflows/ci.yml`

- Builds the Next.js frontend using Node.js.
- Builds the FastAPI backend Docker image.
- Runs the backend container and checks its `/health` endpoint.
- Runs on pushes and pull requests targeting `main`, or manual execution.

## Infrastructure Validation
Workflow: `.github/workflows/infra-validate.yml`

- Installs `cfn-lint`.
- Validates CloudFormation templates.
- Runs when infrastructure files change, on relevant pull requests, or manually.
- Does not deploy AWS resources.

## Recommended Deployment Pipeline
1. Build and test frontend and backend.
2. Scan container images for vulnerabilities.
3. Authenticate using GitHub OIDC and a least-privilege IAM role.
4. Push versioned images to Amazon ECR.
5. Deploy to ECS Fargate and run smoke tests.
6. Roll back to a previous known-good image if health checks fail.

## Infrastructure Release
1. Run formatting and template validation.
2. Create and review a CloudFormation change set.
3. Require approval for production changes.
4. Execute only when authorized.
5. Verify resource health after deployment.

## Security
- Never commit AWS credentials, tokens, or `.env` files.
- Prefer GitHub OIDC and temporary AWS credentials.
- Keep production and non-production environments separate.
- Store application secrets in AWS Secrets Manager.

## Current Limitations
Current workflows build and validate code and templates; they do not prove AWS deployment. CloudFormation operations are blocked by an AWS Organizations service control policy. Deployment remains pending until the required permission is granted.

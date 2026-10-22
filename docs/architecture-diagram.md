# AWS Architecture Diagram

```mermaid
flowchart TD
    U[User] --> ALB[Application Load Balancer]
    ALB --> FE[Next.js Frontend on ECS Fargate]
    FE --> BE[FastAPI Backend on ECS Fargate]
    BE --> DB[(Amazon RDS PostgreSQL)]
    GH[GitHub Actions] --> CI[Build and Validation]
    CI --> ECR[Amazon ECR]
    BE --> SM[AWS Secrets Manager]
    FE --> CW[CloudWatch]
    BE --> CW
```

## Deployment status

This diagram represents the intended architecture. Actual AWS deployment remains pending because CloudFormation operations are blocked by an AWS Organizations service control policy.

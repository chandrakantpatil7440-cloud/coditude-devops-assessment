\# Deployment Guide



\## 1. Prerequisites



\- Git

\- Docker Desktop and Docker Compose

\- AWS CLI

\- Access to an AWS account

\- GitHub repository access



\## 2. Local Deployment



Create a `.env` file in the repository root:



```dotenv

POSTGRES\_PASSWORD=replace\_with\_a\_strong\_local\_password

```



Do not commit `.env` or production credentials.



Start the application:



```powershell

docker compose up --build -d

```



Check containers:



```powershell

docker compose ps

```



Test application endpoints:



\- Frontend: `http://localhost:3000`

\- Backend: `http://localhost:8000/health`

\- Frontend backend proxy: `http://localhost:3000/api/health`

\- Database health: `http://localhost:3000/api/health/db`



Stop the application:



```powershell

docker compose down

```



To remove local database data as well, use `docker compose down -v` only when that data is no longer required.



\## 3. Continuous Integration



The GitHub Actions workflow in `.github/workflows/ci.yml` runs for pushes and pull requests targeting `main`.



It performs these steps:



1\. Checks out the repository.

2\. Sets up Node.js and installs frontend dependencies.

3\. Builds the Next.js frontend.

4\. Builds the backend Docker image.

5\. Runs the backend container and checks its health endpoint.



\## 4. AWS Infrastructure Templates



The current CloudFormation templates are:



\- `infra/cloudformation/network.yaml`

\- `infra/cloudformation/security.yaml`

\- `infra/cloudformation/database.yaml`



Before deployment, validate parameters, dependencies, IAM permissions, subnet routing, image access, and security group references.



The templates are separate building blocks. They do not yet provision the entire application stack or a working CI/CD deployment pipeline.



\## 5. Production Deployment — Planned



The following work is required before production deployment:



1\. Complete the application compute layer and load balancer configuration.

2\. Configure private connectivity to Amazon ECR and other required AWS services, or implement an appropriately secured NAT design.

3\. Configure HTTPS using ACM and a suitable domain.

4\. Configure IAM roles and least-privilege permissions.

5\. Configure application environment variables and secure database-secret retrieval.

6\. Add monitoring, logging, alarms, health checks, and rollback procedures.

7\. Deploy to a development environment and validate end-to-end behavior before staging or production.



\## 6. Cost and Cleanup



AWS resources may incur charges even when the application receives no traffic. Review the current AWS pricing for each selected service before deployment.



After testing, delete disposable CloudFormation stacks and verify that associated resources have been removed. RDS snapshots and other retained resources may continue to incur charges.



\## 7. Current Status



\- Local Docker Compose: tested.

\- GitHub Actions CI: passed.

\- Network, security group, and database CloudFormation templates: created and syntax-validated.

\- Complete AWS application deployment: not performed.

\- Automated AWS CD pipeline: pending.




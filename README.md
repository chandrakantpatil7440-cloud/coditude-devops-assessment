\# Coditude DevOps Assessment



\## Project Overview



Production-oriented deployment design for a Next.js frontend, FastAPI backend, and PostgreSQL database using Docker, AWS CloudFormation, and GitHub Actions.



\## Application Stack



\- \*\*Frontend:\*\* Next.js, React, TypeScript

\- \*\*Backend:\*\* Python, FastAPI, Uvicorn

\- \*\*Database:\*\* PostgreSQL

\- \*\*Local development:\*\* Docker Compose

\- \*\*Infrastructure as Code:\*\* AWS CloudFormation

\- \*\*CI:\*\* GitHub Actions



\## Repository Structure



```text

.

├── app/

│   ├── frontend/

│   └── backend/

├── infra/

│   └── cloudformation/

│       ├── network.yaml

│       ├── security.yaml

│       └── database.yaml

├── .github/

│   └── workflows/

│       └── ci.yml

├── docker-compose.yml

└── README.md

```



\## Run Locally



Prerequisites: Docker Desktop, Git, and PowerShell.



1\. Create a local `.env` file containing a strong `POSTGRES\_PASSWORD` value.

2\. Start the application:



&#x20;  ```powershell

&#x20;  docker compose up --build -d

&#x20;  ```



3\. Check service status:



&#x20;  ```powershell

&#x20;  docker compose ps

&#x20;  ```



4\. Test endpoints:



&#x20;  - Frontend: `http://localhost:3000`

&#x20;  - Backend health: `http://localhost:8000/health`

&#x20;  - Frontend-to-backend health: `http://localhost:3000/api/health`

&#x20;  - Database health: `http://localhost:3000/api/health/db`



5\. Stop services:



&#x20;  ```powershell

&#x20;  docker compose down

&#x20;  ```



\## AWS Architecture Design



CloudFormation templates define:



\- A VPC with two public and two private subnets across two Availability Zones.

\- An Internet Gateway and public routing.

\- Security groups for the load balancer, frontend, backend, and database.

\- A private PostgreSQL RDS instance with encryption and managed master credentials.

\- Production-specific database settings for Multi-AZ, backups, and deletion protection.



The current templates are infrastructure building blocks and are not yet a complete, deployed application architecture. Container hosting, load balancer resources, image publishing, private-subnet connectivity, and deployment orchestration still need to be implemented and validated.



\## Continuous Integration



The GitHub Actions workflow runs on pushes and pull requests targeting `main`. It builds the frontend and builds the backend Docker image, then checks the backend health endpoint.



\## Security Considerations



\- Keep `.env` and credentials out of source control.

\- Keep PostgreSQL private; do not expose port 5432 publicly.

\- Restrict application access through security groups.

\- Use managed database credentials and encrypted storage.

\- Store CI/CD cloud credentials in an appropriately configured identity/secret mechanism.



\## Deployment Status



\- Local Docker Compose application: tested.

\- GitHub Actions CI: passed.

\- CloudFormation templates: created and syntax-validated.

\- AWS deployment: not performed.

\- Production readiness: further integration, deployment testing, monitoring, and operational validation required.




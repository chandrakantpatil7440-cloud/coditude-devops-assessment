\# AWS Architecture and Design



\## 1. Objective



Design a secure, scalable, and highly available architecture for a Next.js frontend, FastAPI backend, and PostgreSQL database.



\## 2. Proposed Architecture



```text

&#x20;                        Internet Users

&#x20;                              |

&#x20;                        Internet Gateway

&#x20;                              |

&#x20;                   Public Application Load

&#x20;                        Balancer (HTTP/HTTPS)

&#x20;                        /              \\

&#x20;                Frontend Service   Frontend Service

&#x20;                   AZ-A                 AZ-B

&#x20;                        \\              /

&#x20;                     Private Application Tier

&#x20;                              |

&#x20;                        FastAPI Backend

&#x20;                              |

&#x20;                    Private Database Subnets

&#x20;                              |

&#x20;                       Amazon RDS PostgreSQL

```



This is a proposed logical architecture. The application load balancer, compute services, and database have not been deployed as a complete stack.



\## 3. Network Design



\- VPC CIDR: `10.0.0.0/16`

\- Public subnet A: `10.0.1.0/24`

\- Public subnet B: `10.0.2.0/24`

\- Private subnet A: `10.0.11.0/24`

\- Private subnet B: `10.0.12.0/24`

\- Public subnets use an Internet Gateway route.

\- Private subnets currently have no NAT Gateway or VPC endpoints configured.



\## 4. Security Design



\- Load balancer accepts HTTP traffic on port 80.

\- Frontend accepts traffic on port 3000 from the load balancer security group.

\- Backend accepts traffic on port 8000 from the frontend security group.

\- PostgreSQL accepts traffic on port 5432 from the backend security group.

\- RDS storage encryption is enabled.

\- RDS master credentials are managed by AWS Secrets Manager through RDS.

\- Production database configuration enables Multi-AZ, seven-day backup retention, and deletion protection.



HTTPS, ACM certificates, WAF, and complete secrets access policies still need to be implemented and validated.



\## 5. Availability and Scalability



The network is designed across two Availability Zones. Production RDS is configured for Multi-AZ. Application compute scaling, load balancer target groups, health checks, and deployment orchestration remain to be implemented.



\## 6. Monitoring and Operations



Recommended additions include CloudWatch application and infrastructure metrics, centralized logs, alarms, health checks, and operational dashboards. These have not yet been deployed.



\## 7. Key Remaining Work



1\. Implement and validate the application compute layer.

2\. Create the load balancer, listeners, target groups, and health checks.

3\. Provide secure private connectivity to required container images and AWS services.

4\. Implement a deployment pipeline with least-privilege access.

5\. Add HTTPS, monitoring, alarms, and rollback procedures.

6\. Validate the full architecture in AWS before describing it as production-ready.

@'

## 8. Architecture Diagram

The following diagram represents the proposed target architecture, not a deployed AWS environment.

```mermaid
flowchart TB
    U[Internet Users] --> IGW[Internet Gateway]
    IGW --> ALB[Application Load Balancer]

    subgraph VPC["VPC 10.0.0.0/16"]
        subgraph PUB["Public Subnets - AZ A and AZ B"]
            ALB
        end

        subgraph APP["Private Application Tier - Planned"]
            FE1[Next.js Frontend - AZ A]
            FE2[Next.js Frontend - AZ B]
            BE[FastAPI Backend]
        end

        subgraph DB["Private Database Subnets"]
            RDS[(Amazon RDS PostgreSQL)]
        end

        ALB --> FE1
        ALB --> FE2
        FE1 --> BE
        FE2 --> BE
        BE --> RDS
    end

    SEC[AWS Secrets Manager] -. Database credentials .-> RDS
    CW[Amazon CloudWatch] -. Monitoring - planned .-> APP


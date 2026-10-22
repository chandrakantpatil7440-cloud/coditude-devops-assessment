
import os
from urllib.parse import quote

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from psycopg import connect

app = FastAPI(
    title="Coditude Assessment API",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=False,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["Content-Type", "Authorization"],
)


def get_database_url():
    # Keep compatibility with local Docker Compose configuration.
    database_url = os.getenv("DATABASE_URL")
    if database_url:
        return database_url

    # ECS will receive these values from its task configuration
    # and AWS Secrets Manager.
    host = os.getenv("DATABASE_HOST")
    name = os.getenv("DATABASE_NAME")
    username = os.getenv("DATABASE_USERNAME")
    password = os.getenv("DATABASE_PASSWORD")
    port = os.getenv("DATABASE_PORT", "5432")

    if not all([host, name, username, password]):
        return None

    encoded_username = quote(username, safe="")
    encoded_password = quote(password, safe="")
    encoded_name = quote(name, safe="")

    return (
        f"postgresql://{encoded_username}:{encoded_password}"
        f"@{host}:{port}/{encoded_name}"
    )


@app.get("/")
def root():
    return {"message": "Coditude Assessment API is running"}


@app.get("/health")
def health():
    return {"status": "healthy", "service": "backend"}


@app.get("/health/db")
def database_health():
    database_url = get_database_url()

    if not database_url:
        return {
            "status": "not_configured",
            "database": "PostgreSQL",
        }

    try:
        with connect(database_url, connect_timeout=3) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT 1")
                cur.fetchone()

        return {"status": "healthy", "database": "PostgreSQL"}

    except Exception:
        raise HTTPException(
            status_code=503,
            detail="Database connection failed",
        )

import os

from fastapi import FastAPI
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


@app.get("/")
def root():
    return {"message": "Coditude Assessment API is running"}


@app.get("/health")
def health():
    return {"status": "healthy", "service": "backend"}


@app.get("/health/db")
def database_health():
    database_url = os.getenv("DATABASE_URL")

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
        from fastapi import HTTPException
        raise HTTPException(
            status_code=503,
            detail="Database connection failed",
        )

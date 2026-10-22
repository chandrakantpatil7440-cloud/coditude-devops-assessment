"use client";

import { useEffect, useState } from "react";

type Health = {
  status: string;
  service?: string;
  database?: string;
};

export default function Home() {
  const [backend, setBackend] = useState("Checking...");
  const [database, setDatabase] = useState("Checking...");

  useEffect(() => {
    fetch("/api/health")
      .then((res) => {
        if (!res.ok) throw new Error("Backend unavailable");
        return res.json();
      })
      .then((data: Health) => setBackend(data.status))
      .catch(() => setBackend("Unavailable"));

    fetch("/api/health/db")
      .then((res) => {
        if (!res.ok) throw new Error("Database unavailable");
        return res.json();
      })
      .then((data: Health) => setDatabase(data.status))
      .catch(() => setDatabase("Unavailable"));
  }, []);

  const statusStyle = (status: string) =>
    status === "healthy"
      ? "text-green-700 bg-green-100"
      : status === "Checking..."
        ? "text-amber-700 bg-amber-100"
        : "text-red-700 bg-red-100";

  return (
    <main className="min-h-screen bg-slate-950 px-6 py-16 text-white">
      <div className="mx-auto max-w-4xl">
        <p className="text-sm font-semibold uppercase tracking-[0.25em] text-cyan-400">
          DevOps Assessment
        </p>
        <h1 className="mt-4 text-4xl font-bold sm:text-5xl">
          Application Health Dashboard
        </h1>
        <p className="mt-4 text-slate-300">
          Monitoring the application services and database connectivity.
        </p>

        <div className="mt-10 grid gap-5 sm:grid-cols-2">
          <section className="rounded-2xl border border-slate-700 bg-slate-900 p-6">
            <h2 className="text-xl font-semibold">FastAPI Backend</h2>
            <p className="mt-2 text-sm text-slate-400">
              API service health
            </p>
            <span className={`mt-5 inline-block rounded-full px-4 py-2 text-sm font-bold ${statusStyle(backend)}`}>
              {backend.toUpperCase()}
            </span>
          </section>

          <section className="rounded-2xl border border-slate-700 bg-slate-900 p-6">
            <h2 className="text-xl font-semibold">PostgreSQL</h2>
            <p className="mt-2 text-sm text-slate-400">
              Database connection health
            </p>
            <span className={`mt-5 inline-block rounded-full px-4 py-2 text-sm font-bold ${statusStyle(database)}`}>
              {database.toUpperCase()}
            </span>
          </section>
        </div>

        <p className="mt-8 text-sm text-slate-400">
          Local development environment · Docker Compose
        </p>
      </div>
    </main>
  );
}


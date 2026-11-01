# AI-Powered Business Operations Agent

A multi-agent system that automates daily business operations: customer support (RAG), sales lead scoring, email triage, data analysis and browser automation, with human approval for sensitive actions.

## Stack
n8n, Python (FastAPI), PostgreSQL + pgvector, Redis, Docker, Playwright.

## Structure
```
n8n/workflows/       n8n workflow exports
backend/             FastAPI app (agents, api, services, utils)
database/migrations/ SQL schema
docker/              docker-compose.yml
docs/                architecture.md
```

## Quick start
```powershell
copy .env.example .env      # then edit the values
cd docker
docker compose up -d --build
```
- n8n: http://localhost:5678
- API docs: http://localhost:8000/docs
- Health: http://localhost:8000/health

## Browser agent
Uses the separate Playwright HTTP bridge (runs on the host, port 3000), reached through `host.docker.internal`.

## Roadmap
- [x] Infrastructure (Docker, Postgres, Redis, n8n)
- [x] Database schema
- [x] Backend skeleton + orchestrator
- [ ] Email agent + Telegram
- [ ] Human approval flow
- [ ] Support agent + RAG
- [ ] Sales + Analytics agents
- [ ] Logging and error handling improvements

## Security
Never commit `.env`. Use strong API keys. Do not expose services to the internet.

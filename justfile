backend:
  cd backend && uv run fastapi dev main.py

frontend:
  cd frontend && pnpm run dev

ingest:
  cd backend && uv run ingest.py

db-build:
  cd backend && uv run db.py

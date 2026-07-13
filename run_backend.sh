#!/usr/bin/env bash
# run_backend.sh — Starts the JobHub FastAPI backend.
#
# Used by Replit (see .replit) and can be run manually:
#   bash run_backend.sh
#
# Environment variables (set in Replit Secrets or a local .env):
#   PORT            — Port to bind (Replit sets this automatically; defaults to 8000)
#   DATABASE_URL    — PostgreSQL connection string
#   SECRET_KEY      — App secret (change for production)
#   JWT_SECRET      — JWT signing key (change for production)
#   ALLOWED_HOSTS   — Comma-separated trusted hostnames
#   CORS_ORIGINS    — Comma-separated allowed CORS origins
#
# Optional (app boots without them):
#   REDIS_URL, SMTP_*, TWILIO_*, CRYTONET_*, SUPABASE_*, SENTRY_DSN

set -e

# Move to backend directory so relative imports resolve correctly.
cd "$(dirname "$0")/backend"

# Install/upgrade dependencies if pip is available (idempotent on Replit).
if command -v pip &>/dev/null; then
  echo "📦 Installing dependencies..."
  pip install -q -r requirements.txt
fi

# Resolve the port: honour $PORT (Replit) or default to 8000.
PORT="${PORT:-8000}"

echo "🚀 Starting JobHub API on port $PORT ..."
exec uvicorn app.main:app --host 0.0.0.0 --port "$PORT"

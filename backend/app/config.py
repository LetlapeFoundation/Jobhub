"""Application configuration and environment variables."""

import json
import os
from typing import List

from pydantic_settings import BaseSettings

# -----------------------------------------------------------------------
# Pre-process list-typed environment variables so they work whether the
# operator sets them as comma-separated strings (Replit Secrets) or as
# JSON arrays.  pydantic-settings expects JSON arrays for List[str] fields,
# so we normalise them here before the Settings class is instantiated.
# -----------------------------------------------------------------------
def _normalise_list_env(var_name: str) -> None:
    raw = os.environ.get(var_name, "")
    if raw and not raw.startswith("["):
        os.environ[var_name] = json.dumps(
            [item.strip() for item in raw.split(",") if item.strip()]
        )


_normalise_list_env("ALLOWED_HOSTS")
_normalise_list_env("CORS_ORIGINS")


class Settings(BaseSettings):
    """Application settings from environment variables."""

    # General
    ENVIRONMENT: str = "development"
    DEBUG: bool = True
    SECRET_KEY: str = "dev-secret-key-change-in-production"
    # Accepted as a JSON list OR a comma-separated string via env var.
    # Default includes wildcard so the app boots on Replit without extra host config;
    # override with a stricter value in production.
    ALLOWED_HOSTS: List[str] = ["localhost", "127.0.0.1", "0.0.0.0", "*"]
    # Accepted as a JSON list OR a comma-separated string via env var.
    CORS_ORIGINS: List[str] = ["http://localhost:3000", "http://localhost:8000"]

    # Runtime port — Replit injects $PORT; falls back to 8000
    PORT: int = 8000

    # Database
    DATABASE_URL: str = (
        "postgresql://jobhub:jobhub_password@localhost:5432/jobhub_dev"
    )
    DATABASE_ECHO: bool = False

    # Redis
    REDIS_URL: str = "redis://localhost:6379/0"
    REDIS_CACHE_DB: int = 1
    REDIS_SESSION_DB: int = 2

    # JWT
    JWT_SECRET: str = "dev-jwt-secret"
    JWT_ALGORITHM: str = "HS256"
    JWT_EXPIRATION_HOURS: int = 24
    JWT_REFRESH_EXPIRATION_DAYS: int = 7

    # Email — defaults match Mailhog for local dev; set real SMTP values for hosted
    SMTP_HOST: str = "localhost"
    SMTP_PORT: int = 1025  # Mailhog default; use 587 for SendGrid/Mailgun
    SMTP_USER: str = ""
    SMTP_PASSWORD: str = ""
    SMTP_FROM_EMAIL: str = "noreply@jobhub.co.za"
    SMTP_FROM_NAME: str = "JobHub"

    # SMS (Twilio)
    TWILIO_ACCOUNT_SID: str = ""
    TWILIO_AUTH_TOKEN: str = ""
    TWILIO_PHONE_NUMBER: str = ""

    # CRYTONET
    CRYTONET_API_KEY: str = ""
    CRYTONET_API_URL: str = "https://api.crytonet.io/v1"
    CRYTONET_WEBHOOK_SECRET: str = ""

    # File Storage (Supabase)
    SUPABASE_URL: str = ""
    SUPABASE_ANON_KEY: str = ""
    SUPABASE_SERVICE_ROLE_KEY: str = ""
    SUPABASE_STORAGE_BUCKET: str = "jobhub-uploads"

    # Celery
    CELERY_BROKER_URL: str = "redis://localhost:6379/3"
    CELERY_RESULT_BACKEND: str = "redis://localhost:6379/4"

    # Sentry
    SENTRY_DSN: str = ""
    LOG_LEVEL: str = "INFO"

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()

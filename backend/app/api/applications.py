"""Job application endpoints."""

from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session

from app.database import get_db

router = APIRouter()


@router.post("/", status_code=status.HTTP_201_CREATED)
def apply_for_job(
    job_id: str,
    db: Session = Depends(get_db),
) -> dict:
    """Submit job application."""
    # TODO: Calculate matching score, create application, send notifications
    raise HTTPException(status_code=501, detail="Feature in development")


@router.get("/", response_model=list[dict])
def list_applications(
    job_id: str = None,
    db: Session = Depends(get_db),
) -> list[dict]:
    """List applications."""
    # TODO: Filter by job_id or user, pagination
    raise HTTPException(status_code=501, detail="Feature in development")

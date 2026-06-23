"""Employer management endpoints."""

from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session

from app.database import get_db

router = APIRouter()


@router.post("/verify", status_code=status.HTTP_202_ACCEPTED)
def verify_employer_cipc(
    cipc_number: str,
    db: Session = Depends(get_db),
) -> dict:
    """Verify employer via CIPC registration (CRYTONET Layer 1)."""
    # TODO: Call CRYTONET API for CIPC verification
    raise HTTPException(status_code=501, detail="Feature in development")

"""Job posting endpoints."""

from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.job import JobCreate, JobResponse

router = APIRouter()


@router.post("/", response_model=JobResponse, status_code=status.HTTP_201_CREATED)
def create_job(
    job: JobCreate,
    db: Session = Depends(get_db),
) -> JobResponse:
    """Create a new job posting."""
    # TODO: Validate employer is VERIFIED
    # TODO: CRYTONET scan for scam indicators
    # TODO: Create job in database
    raise HTTPException(status_code=501, detail="Feature in development")


@router.get("/{job_id}", response_model=JobResponse)
def get_job(job_id: str, db: Session = Depends(get_db)) -> JobResponse:
    """Get job posting details."""
    # TODO: Fetch from database
    raise HTTPException(status_code=501, detail="Feature in development")


@router.get("/", response_model=list[JobResponse])
def list_jobs(
    skip: int = 0,
    limit: int = 20,
    db: Session = Depends(get_db),
) -> list[JobResponse]:
    """List active job postings."""
    # TODO: Fetch from database with pagination, smart matching
    raise HTTPException(status_code=501, detail="Feature in development")

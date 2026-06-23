"""Job request/response schemas."""

from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional, List
from uuid import UUID

from app.models.job import JobType, WorkLocation, JobStatus


class JobCreate(BaseModel):
    """Create job posting request."""
    title: str = Field(..., min_length=5, max_length=200)
    description: str = Field(..., min_length=50)
    job_type: JobType
    work_location: WorkLocation
    work_location_city: Optional[str] = None
    salary_min: int = Field(..., gt=0)
    salary_max: int = Field(..., gt=0)
    experience_level: Optional[str] = None
    required_skills: Optional[List[str]] = None
    education_required: Optional[str] = None
    years_experience_required: int = 0
    languages_required: Optional[List[str]] = None
    eea_target_designated_groups: Optional[List[str]] = None
    application_deadline: datetime


class JobUpdate(BaseModel):
    """Update job posting request."""
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[JobStatus] = None
    salary_min: Optional[int] = None
    salary_max: Optional[int] = None
    # ... other fields


class JobResponse(BaseModel):
    """Job response schema."""
    id: UUID
    employer_id: UUID
    title: str
    description: str
    job_type: JobType
    work_location: WorkLocation
    salary_min: int
    salary_max: int
    status: JobStatus
    total_applications: int
    application_deadline: datetime
    published_at: Optional[datetime]
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

"""Job application model."""

from datetime import datetime
from enum import Enum

from sqlalchemy import (
    Column,
    String,
    DateTime,
    ForeignKey,
    Enum as SQLEnum,
    Text,
    Float,
)
from sqlalchemy.dialects.postgresql import UUID
import uuid

from app.database import Base


class ApplicationStatus(str, Enum):
    """Application status in the hiring pipeline."""
    SUBMITTED = "submitted"
    VIEWED = "viewed"
    SHORTLISTED = "shortlisted"
    INTERVIEW_SCHEDULED = "interview_scheduled"
    INTERVIEW_COMPLETED = "interview_completed"
    OFFERED = "offered"
    HIRED = "hired"
    REJECTED = "rejected"
    WITHDRAWN = "withdrawn"


class Application(Base):
    """Job application record."""
    __tablename__ = "applications"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    job_id = Column(UUID(as_uuid=True), ForeignKey("jobs.id"), nullable=False)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)  # Job seeker
    employer_id = Column(UUID(as_uuid=True), ForeignKey("employers.id"), nullable=False)
    
    # Application Content
    cover_letter = Column(Text, nullable=True)
    cv_url = Column(String(255), nullable=True)  # Supabase URL at time of application
    
    # Status & Pipeline
    status = Column(
        SQLEnum(ApplicationStatus),
        default=ApplicationStatus.SUBMITTED,
        nullable=False,
        index=True,
    )
    
    # Matching Score (v1: Rules-based)
    matching_score = Column(Float, nullable=True)  # 0.0 - 1.0
    skills_match = Column(Float, nullable=True)  # 40% weight
    location_match = Column(Float, nullable=True)  # 20% weight
    experience_match = Column(Float, nullable=True)  # 20% weight
    salary_match = Column(Float, nullable=True)  # 15% weight
    availability_match = Column(Float, nullable=True)  # 5% weight
    
    # Timeline
    applied_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    viewed_at = Column(DateTime, nullable=True)
    shortlisted_at = Column(DateTime, nullable=True)
    interview_scheduled_at = Column(DateTime, nullable=True)
    interview_completed_at = Column(DateTime, nullable=True)
    offer_sent_at = Column(DateTime, nullable=True)
    hired_at = Column(DateTime, nullable=True)
    rejected_at = Column(DateTime, nullable=True)
    withdrawn_at = Column(DateTime, nullable=True)
    
    # Interview Details
    interview_notes = Column(Text, nullable=True)
    interview_rating = Column(Float, nullable=True)  # 0.0 - 5.0
    
    # Rejection Reason
    rejection_reason = Column(String(255), nullable=True)
    
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __repr__(self) -> str:
        return f"<Application(id={self.id}, job_id={self.job_id}, user_id={self.user_id}, status={self.status})>"

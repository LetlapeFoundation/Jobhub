"""Job posting model."""

from datetime import datetime
from enum import Enum

from sqlalchemy import (
    Column,
    String,
    Integer,
    DateTime,
    ForeignKey,
    Enum as SQLEnum,
    Text,
    ARRAY,
    Boolean,
)
from sqlalchemy.dialects.postgresql import UUID
import uuid

from app.database import Base


class JobStatus(str, Enum):
    """Job posting status."""
    DRAFT = "draft"
    ACTIVE = "active"
    CLOSED = "closed"
    EXPIRED = "expired"
    ARCHIVED = "archived"


class JobType(str, Enum):
    """Employment type."""
    FULL_TIME = "full_time"
    PART_TIME = "part_time"
    CONTRACT = "contract"
    TEMPORARY = "temporary"
    INTERNSHIP = "internship"
    FREELANCE = "freelance"


class WorkLocation(str, Enum):
    """Work location type."""
    ONSITE = "onsite"
    REMOTE = "remote"
    HYBRID = "hybrid"


class Job(Base):
    """Job posting/vacancy."""
    __tablename__ = "jobs"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    employer_id = Column(UUID(as_uuid=True), ForeignKey("employers.id"), nullable=False)
    
    # Basic Info
    title = Column(String(200), nullable=False, index=True)
    description = Column(Text, nullable=False)
    
    # Job Details
    job_type = Column(SQLEnum(JobType), nullable=False)
    work_location = Column(SQLEnum(WorkLocation), nullable=False)
    work_location_city = Column(String(100), nullable=True)  # e.g., "Johannesburg"
    
    # Compensation
    salary_min = Column(Integer, nullable=False)  # In ZAR, mandatory per Constitution
    salary_max = Column(Integer, nullable=False)
    currency = Column(String(3), default="ZAR")
    
    # Requirements
    experience_level = Column(String(50), nullable=True)  # e.g., "entry", "mid", "senior"
    required_skills = Column(ARRAY(String), nullable=True)  # e.g., ["Python", "PostgreSQL"]
    education_required = Column(String(100), nullable=True)
    years_experience_required = Column(Integer, default=0)
    languages_required = Column(ARRAY(String), nullable=True)  # e.g., ["English", "Zulu"]
    
    # EEA (Employment Equity Act)
    eea_target_designated_groups = Column(ARRAY(String), nullable=True)  # e.g., ["Black", "Women"]
    
    # Application Settings
    application_deadline = Column(DateTime, nullable=False)
    max_applications = Column(Integer, nullable=True)  # e.g., limit to 100 applications
    
    # Status & Tracking
    status = Column(SQLEnum(JobStatus), default=JobStatus.DRAFT, index=True)
    published_at = Column(DateTime, nullable=True)
    closed_at = Column(DateTime, nullable=True)
    
    # Metrics
    total_applications = Column(Integer, default=0)
    total_interviews = Column(Integer, default=0)
    total_placements = Column(Integer, default=0)
    
    # CRYTONET: Fraud Detection
    crytonet_flagged = Column(Boolean, default=False)
    crytonet_flag_reason = Column(Text, nullable=True)
    
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __repr__(self) -> str:
        return f"<Job(id={self.id}, title={self.title}, employer_id={self.employer_id})>"

"""Job Seeker profile model."""

from datetime import datetime
from enum import Enum

from sqlalchemy import (
    Column,
    String,
    Integer,
    Float,
    DateTime,
    ForeignKey,
    Enum as SQLEnum,
    ARRAY,
    Text,
    Boolean,
)
from sqlalchemy.dialects.postgresql import UUID, JSONB
import uuid

from app.database import Base


class ExperienceLevel(str, Enum):
    """Experience level enumeration."""
    ENTRY = "entry"
    MID = "mid"
    SENIOR = "senior"
    LEAD = "lead"
    EXECUTIVE = "executive"


class EducationLevel(str, Enum):
    """Education level enumeration."""
    NO_FORMAL = "no_formal"
    HIGH_SCHOOL = "high_school"
    DIPLOMA = "diploma"
    BACHELOR = "bachelor"
    MASTER = "master"
    PHD = "phd"


class JobSeekerProfile(Base):
    """Job Seeker profile with KYC details."""
    __tablename__ = "job_seeker_profiles"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False, unique=True)
    
    # Personal Info
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    id_number = Column(String(13), nullable=True, unique=True)  # South African ID
    date_of_birth = Column(DateTime, nullable=True)
    
    # Location
    suburb = Column(String(100), nullable=True)
    province = Column(String(50), nullable=True)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    
    # Education & Skills
    education_level = Column(SQLEnum(EducationLevel), nullable=True)
    experience_level = Column(SQLEnum(ExperienceLevel), nullable=True)
    skills = Column(ARRAY(String), nullable=True, default=[])  # e.g., ["Python", "FastAPI"]
    certifications = Column(ARRAY(String), nullable=True, default=[])  # e.g., AWS, GCP
    languages = Column(ARRAY(String), nullable=True, default=[])  # e.g., ["English", "Zulu"]
    
    # Employment Preferences
    desired_salary_min = Column(Integer, nullable=True)  # In ZAR
    desired_salary_max = Column(Integer, nullable=True)
    availability_status = Column(String(50), nullable=True)  # e.g., "immediately", "2 weeks"
    
    # Optional Fields
    portfolio_url = Column(String(255), nullable=True)
    cv_url = Column(String(255), nullable=True)  # Supabase storage URL
    profile_photo_url = Column(String(255), nullable=True)
    disability_status = Column(Boolean, nullable=True)  # EEA reporting
    criminal_record = Column(Boolean, nullable=True)  # Candidate-declared
    
    # Metadata
    profile_completion = Column(Integer, default=0)  # 0-100%
    bio = Column(Text, nullable=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __repr__(self) -> str:
        return f"<JobSeekerProfile(user_id={self.user_id}, name={self.first_name} {self.last_name})>"

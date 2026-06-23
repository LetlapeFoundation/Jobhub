"""Employer profile model."""

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
    Boolean,
)
from sqlalchemy.dialects.postgresql import UUID
import uuid

from app.database import Base


class BBBEELevel(str, Enum):
    """B-BBEE level enumeration (South African BEE classification)."""
    LEVEL_1 = "level_1"
    LEVEL_2 = "level_2"
    LEVEL_3 = "level_3"
    LEVEL_4 = "level_4"
    LEVEL_5 = "level_5"
    LEVEL_6 = "level_6"
    LEVEL_7 = "level_7"
    LEVEL_8 = "level_8"
    NON_COMPLIANT = "non_compliant"
    EXEMPT = "exempt"


class CompanySize(str, Enum):
    """Company size enumeration."""
    MICRO = "micro"  # 1-10
    SMALL = "small"  # 11-50
    MEDIUM = "medium"  # 51-250
    LARGE = "large"  # 251+


class Employer(Base):
    """Employer/Company profile."""
    __tablename__ = "employers"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False, unique=True)
    
    # Company Info
    company_name = Column(String(255), nullable=False)
    cipc_registration_number = Column(String(50), nullable=False, unique=True)  # Verified via CRYTONET
    vat_number = Column(String(50), nullable=True, unique=True)
    company_website = Column(String(255), nullable=True)
    
    # Address
    physical_address = Column(String(255), nullable=False)
    latitude = Column(String(50), nullable=True)
    longitude = Column(String(50), nullable=True)
    
    # Contact
    contact_person_name = Column(String(100), nullable=False)
    contact_email = Column(String(100), nullable=False)
    contact_phone = Column(String(20), nullable=False)
    
    # Company Details
    industry = Column(String(100), nullable=True)
    company_size = Column(SQLEnum(CompanySize), nullable=True)
    year_established = Column(Integer, nullable=True)
    bbee_level = Column(SQLEnum(BBBEELevel), nullable=True)
    
    # Verification (CRYTONET)
    cipc_verified = Column(Boolean, default=False)
    cipc_verified_at = Column(DateTime, nullable=True)
    contact_email_verified = Column(Boolean, default=False)
    contact_email_verified_at = Column(DateTime, nullable=True)
    
    # Profile
    company_description = Column(Text, nullable=True)
    logo_url = Column(String(255), nullable=True)  # Supabase storage
    
    # Metadata
    total_jobs_posted = Column(Integer, default=0)
    active_jobs = Column(Integer, default=0)
    total_placements = Column(Integer, default=0)
    nps_score = Column(Integer, nullable=True)  # Net Promoter Score
    
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __repr__(self) -> str:
        return f"<Employer(id={self.id}, company={self.company_name})>"

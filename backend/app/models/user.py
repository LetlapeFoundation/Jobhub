"""User model - base for all user types."""

from datetime import datetime
from enum import Enum

from sqlalchemy import Column, Integer, String, DateTime, Enum as SQLEnum, Boolean
from sqlalchemy.dialects.postgresql import UUID
import uuid

from app.database import Base


class UserType(str, Enum):
    """User type enumeration."""
    JOB_SEEKER = "job_seeker"
    EMPLOYER = "employer"
    RECRUITER = "recruiter"
    ENTREPRENEUR = "entrepreneur"
    INVESTOR = "investor"


class VerificationStatus(str, Enum):
    """Verification status enumeration."""
    UNVERIFIED = "unverified"
    PENDING = "pending"
    VERIFIED = "verified"
    REJECTED = "rejected"


class User(Base):
    """Base user model."""
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = Column(String(255), unique=True, nullable=False, index=True)
    phone = Column(String(20), nullable=True, unique=True)
    password_hash = Column(String(255), nullable=False)
    
    user_type = Column(SQLEnum(UserType), nullable=False, index=True)
    verification_status = Column(
        SQLEnum(VerificationStatus),
        nullable=False,
        default=VerificationStatus.UNVERIFIED,
    )
    
    is_active = Column(Boolean, default=True)
    is_deleted = Column(Boolean, default=False)
    
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Metadata for tracking
    last_login_at = Column(DateTime, nullable=True)
    ip_address = Column(String(45), nullable=True)  # IPv4 or IPv6
    user_agent = Column(String(255), nullable=True)
    
    def __repr__(self) -> str:
        return f"<User(id={self.id}, email={self.email}, type={self.user_type})>"

"""In-app messaging model for employer-candidate communication."""

from datetime import datetime
from enum import Enum

from sqlalchemy import (
    Column,
    String,
    DateTime,
    ForeignKey,
    Enum as SQLEnum,
    Text,
    Boolean,
)
from sqlalchemy.dialects.postgresql import UUID
import uuid

from app.database import Base


class MessageFlag(str, Enum):
    """CRYTONET fraud flags for messages."""
    CLEAN = "clean"
    PAYMENT_REQUEST = "payment_request"
    BANKING_DETAILS = "banking_details"
    SUSPICIOUS = "suspicious"
    OFF_PLATFORM_PRESSURE = "off_platform_pressure"
    MANUAL_REVIEW = "manual_review"


class Message(Base):
    """Direct message between employer and job seeker."""
    __tablename__ = "messages"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    sender_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    receiver_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    
    # Context (optional - can be job or application related)
    job_id = Column(UUID(as_uuid=True), ForeignKey("jobs.id"), nullable=True)
    application_id = Column(UUID(as_uuid=True), ForeignKey("applications.id"), nullable=True)
    
    # Message Content
    content = Column(Text, nullable=False)
    
    # CRYTONET Fraud Detection
    crytonet_flag = Column(
        SQLEnum(MessageFlag),
        default=MessageFlag.CLEAN,
        nullable=False,
        index=True,
    )
    crytonet_flag_details = Column(Text, nullable=True)  # Details for manual review
    flagged_at = Column(DateTime, nullable=True)
    
    # Message Status
    is_read = Column(Boolean, default=False)
    read_at = Column(DateTime, nullable=True)
    
    sent_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    
    def __repr__(self) -> str:
        return f"<Message(id={self.id}, from={self.sender_id}, to={self.receiver_id})>"

"""User request/response schemas."""

from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from typing import Optional
from uuid import UUID

from app.models.user import UserType, VerificationStatus


class UserBase(BaseModel):
    """Base user schema."""
    email: EmailStr
    user_type: UserType


class UserRegister(UserBase):
    """User registration request."""
    password: str = Field(..., min_length=8)
    phone: Optional[str] = None


class UserLogin(BaseModel):
    """User login request."""
    email: EmailStr
    password: str


class UserResponse(UserBase):
    """User response schema."""
    id: UUID
    verification_status: VerificationStatus
    is_active: bool
    created_at: datetime
    last_login_at: Optional[datetime] = None

    class Config:
        from_attributes = True


class TokenResponse(BaseModel):
    """JWT token response."""
    access_token: str
    refresh_token: Optional[str] = None
    token_type: str = "bearer"
    expires_in: int  # Seconds

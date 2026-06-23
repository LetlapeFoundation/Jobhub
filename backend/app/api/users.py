"""User management endpoints."""

from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.user import UserRegister, UserLogin, UserResponse, TokenResponse
from app.models.user import User

router = APIRouter()


@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def register(user: UserRegister, db: Session = Depends(get_db)) -> UserResponse:
    """Register a new user."""
    # Check if user already exists
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email already registered",
        )
    
    # TODO: Hash password, integrate CRYTONET for KYC
    # new_user = User(...)
    # db.add(new_user)
    # db.commit()
    # return new_user
    raise HTTPException(status_code=501, detail="Feature in development")


@router.post("/login", response_model=TokenResponse)
def login(credentials: UserLogin, db: Session = Depends(get_db)) -> TokenResponse:
    """User login."""
    # TODO: Verify password, generate JWT
    raise HTTPException(status_code=501, detail="Feature in development")


@router.get("/me", response_model=UserResponse)
def get_current_user(db: Session = Depends(get_db)) -> UserResponse:
    """Get current logged-in user."""
    # TODO: Extract JWT, return user
    raise HTTPException(status_code=501, detail="Feature in development")

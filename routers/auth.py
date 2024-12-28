from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from auth.handlers import (
    authenticate_user,
    create_access_token,
    get_password_hash,
)
from app.models import UserTable
from database import get_db
from sqlalchemy.orm import Session
from app.schemas import User, Token

router = APIRouter()

@router.post("/register_user/")
async def register_user(user: User, db: Session = Depends(get_db)):
    new_user = UserTable(
        username=user.username,
        email=user.email,
        hashed_password=get_password_hash(user.password),
        is_active=True,
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.post("/token")
async def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)
) -> Token:
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={"sub": user.username})
    return Token(access_token=access_token, token_type="bearer")

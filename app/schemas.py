from typing import Optional
from pydantic import BaseModel
from datetime import datetime


# object schema to post
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None


class User(BaseModel):
    username: str
    email: str
    password: str
    is_active: Optional[bool] = None

    class Config:
        from_attributes  = True  # Allow Pydantic to serialize SQLAlchemy models


class Product(BaseModel):
    name: str
    ecoscore: Optional[float] = None
    natural_resources_score: Optional[float] = None
    health_score: Optional[float] = None
    pollution_score: Optional[float] = None
    ecosystem_score: Optional[float] = None
    analyzed_at: Optional[datetime] = None

    class Config:
        from_attributes  = True  # Allow Pydantic to serialize SQLAlchemy models



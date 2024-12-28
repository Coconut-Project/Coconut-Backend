from sqlalchemy import Boolean, Column, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from base import Base


class ProductTable(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    name = Column(String, nullable=False)
    ecoscore = Column(Float, nullable=False)
    natural_resources_score = Column(Float, nullable=False)
    health_score = Column(Float, nullable=False)
    pollution_score = Column(Float, nullable=False)
    ecosystem_score = Column(Float, nullable=False)
    analyzed_at = Column(DateTime, default=None)

    user = relationship("UserTable", back_populates="products")


class UserTable(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    products = relationship("ProductTable", back_populates="user")

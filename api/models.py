from sqlalchemy import Column, Integer, String
from base import Base


class EcoProductsTable(Base):
    __tablename__ = "ecoproducts"
    id = Column(Integer, primary_key=True, index=True)
    code = Column(String, nullable=False, index=True)
    name = Column(String, nullable=False, index=True)


class EcoMaterialsTable(Base):
    __tablename__ = "ecomaterials"
    id = Column(Integer, primary_key=True, index=True)
    code = Column(String, nullable=False, index=True)  # id
    name = Column(String, nullable=False, index=True)


class EcoCountriesTable(Base):
    __tablename__ = "ecocountries"
    id = Column(Integer, primary_key=True, index=True)
    code = Column(String, nullable=False, index=True)  # id
    name = Column(String, nullable=False, index=True)

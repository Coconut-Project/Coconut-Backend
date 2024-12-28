from pydantic import BaseModel, Field

class EcoProducts(BaseModel):
    code: str = Field(..., alias="id")
    name: str


class EcoMaterials(BaseModel):
    code: str = Field(..., alias="id")
    name: str

class EcoCountries(BaseModel):
    code: str
    name: str


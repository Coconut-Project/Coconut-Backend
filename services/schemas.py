from pydantic import BaseModel, Field

class Image(BaseModel):
    image_name: str = Field(alias="imageName")
    image_data: str = Field(alias="imageData")
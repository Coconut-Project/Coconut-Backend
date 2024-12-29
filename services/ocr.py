from fastapi import APIRouter
from services.handlers import base64_to_image
from services.schemas import Image

router = APIRouter()

@router.post("/process-image/")
async def process_image(images: list[Image]):
    for image in images:
        print(f"{image.image_name} = {len(image.image_data)} bytes")
        base64_to_image(image)

    return {"Image processing complete"}
import base64
import os
import binascii
from services.schemas import Image

def base64_to_image(image: Image):
    try:
        if not os.path.exists("images"):
            os.makedirs("images")

        decoded_image_data = base64.b64decode(image.image_data, validate=True)
        file_to_save = f"images/{image.image_name}"

        with open(file_to_save, "wb") as file:
            file.write(decoded_image_data)
            print(f"Image saved as {file_to_save}")

    except binascii.Error as e:
        print(f"Error in decoding base64: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

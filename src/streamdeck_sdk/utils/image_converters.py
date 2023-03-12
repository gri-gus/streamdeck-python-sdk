import base64
import mimetypes
from pathlib import Path


def image_file_to_base64(file_path: Path) -> str:
    image_mime = mimetypes.guess_type(file_path, strict=True)[0]
    prefix = f"data:{image_mime};base64,"
    with open(file_path, "rb") as image_file:
        image_base64: bytes = base64.b64encode(image_file.read())
    result = prefix + image_base64.decode("UTF-8")
    return result


def image_bytes_to_base64(obj: bytes, image_mime: str) -> str:
    prefix = f"data:{image_mime};base64,"
    image_base64: bytes = base64.b64encode(obj)
    result = prefix + image_base64.decode("UTF-8")
    return result

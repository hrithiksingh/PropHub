import os
import tempfile
import uuid
import shutil
from fastapi import UploadFile
from src.models.prop_images import TagResponse
from .tagging import OpenAIClient, TagGenerator

def process_image_upload(file: UploadFile) -> dict:
    # 1) Write upload to a temp file
    suffix   = os.path.splitext(file.filename)[1]
    tmp_path = os.path.join(tempfile.gettempdir(), f"{uuid.uuid4()}{suffix}")
    with open(tmp_path, "wb") as buf:
        shutil.copyfileobj(file.file, buf)

    client = OpenAIClient()
    gen = TagGenerator(client)
    result = gen.generate(tmp_path)

    print("sending:...",result)
    return result
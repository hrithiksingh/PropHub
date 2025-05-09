# src/services/tagging.py
import json
import os
import base64
import mimetypes
from dotenv import load_dotenv
from openai import OpenAI
from src.models.prop_images import TagResponse

load_dotenv()

MANDATORY_CATEGORIES = {
    "size":     ["small", "medium", "large", "extra-large"],
    "shape":    ["square", "rectangle", "circle", "oval", "triangle", "hexagon"],
    "color":    ["red", "blue", "green", "yellow", "black", "white", "brown", "gray"],
    "material": ["wood", "glass", "metal", "plastic", "fabric"],
    "hardness": ["soft", "semi-hard", "hard"],
}

UNIVERSAL_TAGS = ["vintage", "modern", "rustic", "elegant", "minimalist"]

def build_prompt() -> str:
    return "\n".join([
        "You are an expert image‑tagging assistant.",
        "Given an image, do the following:",
        "1) Provide a concise, descriptive **name** for this object.",
        "2) Choose exactly one option from each category:",
        *[
            f"   • {cat}: [{', '.join(opts)}]"
            for cat, opts in MANDATORY_CATEGORIES.items()
        ],
        "3) Suggest at least **10** additional descriptive tags.",
        f"   You may include any universal tags: [{', '.join(UNIVERSAL_TAGS)}]",
        "4) Return **only** a single JSON object (no markdown or code fences) with keys:",
        '   "mandatory": { "name": "<string>", "size": "<choice>", ..., "hardness": "<choice>" },',
        '   "extras":    ["<tag1>", "<tag2>", ...]'
    ])

class OpenAIClient:
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.model  = os.getenv("IMAGE_MODEL", "gpt-4o-mini")

    def ask(self, image_path: str, prompt: str) -> str:
        mime, _ = mimetypes.guess_type(image_path)
        mime = mime or "application/octet-stream"
        with open(image_path, "rb") as f:
            b64 = base64.b64encode(f.read()).decode("utf-8")
        data_uri = f"data:{mime};base64,{b64}"

        resp = self.client.responses.create(
            model=self.model,
            input=[{
                "role": "user",
                "content": [
                    {"type": "input_text",  "text": prompt},
                    {"type": "input_image", "image_url": data_uri},
                ],
            }],
        )
        # returns raw JSON string
        return resp.output[0].content[0].text

class TagGenerator:
    """
    Returns a plain dict with 'mandatory' and 'extras' keys.
    """
    def __init__(self, client: OpenAIClient):
        self.client = client

    def generate(self, image_path: str) -> dict:
        prompt   = build_prompt()
        raw_json = self.client.ask(image_path, prompt)
        # parse into Python dict
        return json.loads(raw_json)

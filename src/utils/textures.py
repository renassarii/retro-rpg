"""Texture loading helpers."""

from io import BytesIO

import arcade
import requests
from PIL import Image


def load_texture_from_url(url):
    """Download an image and wrap it in an arcade.Texture."""
    response = requests.get(url)
    image_data = BytesIO(response.content)
    img = Image.open(image_data).convert("RGBA")
    return arcade.Texture(name=url, image=img)


def load_image_from_url(url):
    """Download an image and return it as a PIL Image (RGB)."""
    response = requests.get(url)
    return Image.open(BytesIO(response.content)).convert("RGB")

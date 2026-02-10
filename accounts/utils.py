from PIL import Image, ImageDraw, ImageFont
import os
from django.conf import settings
import random


def generate_random_color():
    """Génère une couleur aléatoire qui n'est pas blanche."""
    while True:
        color = (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255),
        )
        if color != (255, 255, 255):
            return color


def generate_profile_image(initials, output_path):
    background_color = generate_random_color()

    img = Image.new("RGB", (100, 100), color=background_color)
    d = ImageDraw.Draw(img)

    font_path = os.path.join(
        settings.BASE_DIR,
        "assets",
        "fonts",
        "Roboto-Bold.ttf"
    )

    try:
        font = ImageFont.truetype(font_path, 50)
    except OSError:
        font = ImageFont.load_default()

    # Calcul taille du texte (Pillow récent)
    bbox = d.textbbox((0, 0), initials, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    position = (
        (100 - text_width) / 2,
        (100 - text_height) / 2
    )

    d.text(position, initials, fill=(255, 255, 255), font=font)

    # Assure que le dossier de sortie existe
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    img.save(output_path)

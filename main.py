import os
import pandas as pd

from PIL import Image, ImageDraw, ImageFont

# Paths
TEMPLATE = "templates/certificate.png"
DATA = "data/participants.csv"
OUTPUT = "output"

os.makedirs(OUTPUT, exist_ok=True)


def generate_certificate(name, certificate_id):

    # Open certificate template
    img = Image.open(TEMPLATE).convert("RGB")

    draw = ImageDraw.Draw(img)

    width, height = img.size

    # Load font
    try:
        font = ImageFont.truetype(
            "C:/Windows/Fonts/georgiab.ttf", 65
        )
    except OSError:
        font = ImageFont.truetype(
            "C:/Windows/Fonts/times.ttf", 65
        )

    # Calculate name position
    bbox = draw.textbbox((0, 0), name, font=font)
    text_width = bbox[2] - bbox[0]

    x = (width - text_width) / 2
    y = int(height * 0.47)

    # Insert participant name
    draw.text(
        (x, y),
        name,
        fill="#393536",
        font=font
    )

    # Save as PDF
    output_path = f"{OUTPUT}/{certificate_id}.pdf"

    img.save(output_path, "PDF", resolution=150)

    print(f"Generated: {output_path}")


def main():

    df = pd.read_csv(DATA)

    for _, row in df.iterrows():

        generate_certificate(
            str(row["name"]),
            str(row["certificate_id"])
        )


if __name__ == "__main__":
    main()
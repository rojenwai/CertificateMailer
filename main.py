import pandas as pd
import os

from reportlab.lib.pagesizes import landscape, A4
from reportlab.pdfgen import canvas

DATA_FILE = "data/participants.csv"
OUTPUT_DIR = "output"

os.makedirs(OUTPUT_DIR, exist_ok=True)


def generate_certificate(name, certificate_id):

    filename = f"{OUTPUT_DIR}/{certificate_id}.pdf"

    c = canvas.Canvas(
        filename,
        pagesize=landscape(A4)
    )

    width, height = landscape(A4)

    c.setFont("Helvetica-Bold", 32)
    c.drawCentredString(
        width / 2,
        height - 130,
        "CERTIFICATE OF PARTICIPATION"
    )

    c.setFont("Helvetica", 18)
    c.drawCentredString(
        width / 2,
        height - 220,
        "This certificate is proudly presented to"
    )

    c.setFont("Helvetica-Bold", 28)
    c.drawCentredString(
        width / 2,
        height - 280,
        name
    )

    c.setFont("Helvetica", 15)
    c.drawCentredString(
        width / 2,
        height - 350,
        "For participating in our event."
    )

    c.setFont("Helvetica", 12)
    c.drawCentredString(
        width / 2,
        70,
        f"Certificate ID: {certificate_id}"
    )

    c.save()

    return filename


def main():

    df = pd.read_csv(DATA_FILE)

    for _, row in df.iterrows():

        path = generate_certificate(
            row["name"],
            row["certificate_id"]
        )

        print(f"Generated: {path}")


if __name__ == "__main__":
    main()
# main.py
import subprocess
import json
from PIL import Image, ImageDraw

IMAGE_PATH = "inputs/sample01.png"
OUTPUT_PATH = "outputs/result.png"

def run():
    proc = subprocess.run(
        ["python", "infer.py", IMAGE_PATH],
        capture_output=True,
        text=True,
        check=True,
    )

    detections = json.loads(proc.stdout)

    image = Image.open(IMAGE_PATH).convert("RGB")
    draw = ImageDraw.Draw(image)

    for d in detections:
        draw.rectangle(
            [(d["x1"], d["y1"]), (d["x2"], d["y2"])],
            outline="red",
            width=3,
        )
        draw.text((d["x1"], d["y1"] - 10), d["type"], fill="red")

    image.save(OUTPUT_PATH)
    print(f"Saved: {OUTPUT_PATH}")

if __name__ == "__main__":
    run()

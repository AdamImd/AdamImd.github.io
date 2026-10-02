"""Extract static project-card thumbnails from the existing animated WebPs.

Requires Python 3 and Pillow. Run from any directory; originals remain unchanged.
"""
import hashlib
import json
from pathlib import Path

from PIL import Image, __version__ as pillow_version

ROOT = Path(__file__).resolve().parents[1]
SOURCES = {
    "Tactile_Skin": "assets/img/Tactile/tactile.webp",
    "Spark_Remote": "assets/img/SPARK/spark.webp",
    "SpotNLP": "assets/img/Spot/demo.webp",
    "Gen_AI": "assets/img/GenAI/WAN.webp",
}


def main():
    folder = ROOT / "assets/img/projects/thumbnails"
    folder.mkdir(parents=True, exist_ok=True)
    rows = {}
    for name, source in SOURCES.items():
        path = ROOT / source
        with Image.open(path) as animation:
            animation.seek(0)
            frame = animation.convert("RGB")
            frame.thumbnail((960, 960), Image.Resampling.LANCZOS)
            output = folder / (name + ".jpg")
            frame.save(output, quality=88, optimize=True)
            rows[name] = {
                "source": source,
                "source_sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
                "frame_index": 0,
                "width": frame.width,
                "height": frame.height,
                "output": str(output.relative_to(ROOT)),
                "output_bytes": output.stat().st_size,
                "output_sha256": hashlib.sha256(output.read_bytes()).hexdigest(),
                "pillow_version": pillow_version,
            }
    (folder / "provenance.json").write_text(json.dumps(rows, indent=2) + "\n")
    print("Extracted", len(rows), "still thumbnails")


if __name__ == "__main__":
    main()

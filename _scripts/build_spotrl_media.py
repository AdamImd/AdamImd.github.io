"""Derive approved Spot portfolio clips from the preserved simulation recordings.

Requires FFmpeg/ffprobe with libx264. CPU only, two threads. Inputs are not
bundled in the public repository; see docs/spot-whole-body-media.md.
"""

import argparse
import hashlib
import json
from pathlib import Path
import subprocess


def digest(path):
    with path.open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()


def run(command):
    subprocess.run(command, check=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-dir", required=True, type=Path)
    parser.add_argument("--output-root", required=True, type=Path)
    parser.add_argument("--recipe", type=Path, default=Path(__file__).with_name("spotrl-media-sources.json"))
    args = parser.parse_args()
    recipe = json.loads(args.recipe.read_text())
    video_dir = args.output_root / "assets/video/projects/spot-whole-body"
    image_dir = args.output_root / "assets/img/projects/spot-whole-body"
    video_dir.mkdir(parents=True, exist_ok=True)
    image_dir.mkdir(parents=True, exist_ok=True)
    for source in recipe["sources"]:
        source_path = args.source_dir / source["file"]
        if digest(source_path) != source["sha256"]:
            raise ValueError(f"Source identity mismatch: {source['file']}")
    clips = []
    for clip in recipe["clips"]:
        source = next(item for item in recipe["sources"] if item["id"] == clip["source"])
        source_path = args.source_dir / source["file"]
        output = video_dir / (clip["id"] + ".mp4")
        filters = []
        if "crop" in clip:
            filters.append("crop=" + ":".join(str(value) for value in clip["crop"]))
        if clip.get("speed", 1) != 1:
            filters.append(f"setpts=PTS/{clip['speed']}")
        filters.extend(["setsar=1", "format=yuv420p"])
        run(["ffmpeg", "-hide_banner", "-nostdin", "-y", "-hwaccel", "none",
             "-threads", "2", "-ss", str(clip["start"]), "-i", str(source_path),
             "-t", str(clip["duration"] / clip.get("speed", 1)), "-an",
             "-vf", ",".join(filters), "-c:v", "libx264", "-threads", "2",
             "-preset", "slow", "-crf", "18", "-movflags", "+faststart", str(output)])
        poster = image_dir / (clip["id"] + ".jpg")
        run(["ffmpeg", "-hide_banner", "-nostdin", "-y", "-hwaccel", "none",
             "-threads", "2", "-ss", str(clip["poster_time"]), "-i", str(output),
             "-frames:v", "1", "-q:v", "2", "-threads", "2", str(poster)])
        run(["ffmpeg", "-hide_banner", "-nostdin", "-hwaccel", "none", "-threads", "2",
             "-v", "error", "-i", str(output), "-f", "null", "-"])
        metadata = json.loads(subprocess.check_output([
            "ffprobe", "-v", "error", "-show_streams", "-show_format", "-of", "json", str(output)
        ]))
        stream = next(item for item in metadata["streams"] if item["codec_type"] == "video")
        clips.append({**clip, "file": output.name, "poster": poster.name,
                      "width": stream["width"], "height": stream["height"],
                      "output_duration": float(metadata["format"]["duration"]),
                      "video_sha256": digest(output), "poster_sha256": digest(poster)})
    card = image_dir / "spot-card.jpg"
    card_source = image_dir / (recipe["card_from"] + ".jpg")
    card.write_bytes(card_source.read_bytes())
    for source in recipe["sources"]:
        if digest(args.source_dir / source["file"]) != source["sha256"]:
            raise ValueError(f"Source changed during derivation: {source['file']}")
    manifest = {"schema_version": 1, "scope": recipe["scope"], "sources": recipe["sources"],
                "derivation": {"script": "_scripts/build_spotrl_media.py",
                               "video": "libx264 CRF 18, slow, yuv420p, faststart, CPU threads 2",
                               "ffmpeg_version": subprocess.check_output(["ffmpeg", "-version"], text=True).splitlines()[0]},
                "clips": clips, "card": {"file": card.name, "from": recipe["card_from"], "sha256": digest(card)}}
    (video_dir / "provenance.json").write_text(json.dumps(manifest, indent=2) + "\n")
    for path in [*video_dir.iterdir(), *image_dir.iterdir()]:
        path.chmod(0o644)
    print(json.dumps({"status": "complete", "clips": len(clips), "manifest": str(video_dir / "provenance.json")}))


if __name__ == "__main__":
    main()

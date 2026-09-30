"""Build short GIF/WebP previews using Python 3 and FFmpeg (no Python packages).

Example: python3 _scripts/build_gif_showcase.py --ffmpeg /path/to/ffmpeg --cache /path/to/cache
Use --only ID ID for a bounded pilot. Completed, unchanged entries are reused.
"""
import argparse
import hashlib
import json
import re
import subprocess
import urllib.request
from pathlib import Path


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--ffmpeg", default="ffmpeg")
    parser.add_argument("--cache", required=True, type=Path)
    parser.add_argument("--only", nargs="+")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    config = json.loads((root / "_scripts/gif-showcase-sources.json").read_text())
    output = root / "assets/img/gifs"
    output.mkdir(parents=True, exist_ok=True)
    args.cache.mkdir(parents=True, exist_ok=True)
    manifest_path = root / "_data/gif_showcase.json"
    manifest = json.loads(manifest_path.read_text()) if manifest_path.exists() else {}

    def run(command):
        result = subprocess.run([args.ffmpeg, "-nostdin", "-hide_banner", *command], capture_output=True, text=True)
        if result.returncode:
            raise RuntimeError(result.stderr[-2500:])
        return result

    for item in config["items"]:
        key = item["id"]
        if args.only and key not in args.only:
            continue
        source = item["source"]
        if source.startswith("https://"):
            path = args.cache / (key + Path(source).suffix)
            if not path.exists():
                temp = path.with_suffix(path.suffix + ".part")
                with urllib.request.urlopen(source, timeout=60) as response, temp.open("wb") as stream:
                    while chunk := response.read(1024 * 1024):
                        stream.write(chunk)
                temp.replace(path)
        else:
            path = root / source.lstrip("/")
        source_hash = digest(path)
        recipe_hash = hashlib.sha256(json.dumps(item, sort_keys=True).encode() + Path(__file__).read_bytes()).hexdigest()
        old = manifest.get(key, {})
        if old.get("source_sha256") == source_hash and old.get("recipe_sha256") == recipe_hash:
            if all((root / old[k].lstrip("/")).is_file() and digest(root / old[k].lstrip("/")) == old[k + "_sha256"] for k in ("gif", "webp", "poster")):
                print("reused", key, flush=True)
                continue
        probe = subprocess.run([args.ffmpeg, "-nostdin", "-hide_banner", "-i", str(path)], stdin=subprocess.DEVNULL, capture_output=True, text=True).stderr
        duration_match = re.search(r"Duration: (\d+):(\d+):([\d.]+)", probe)
        video_line = next(line for line in probe.splitlines() if "Video:" in line)
        size = re.search(r"\b(\d{2,5})x(\d{2,5})\b", video_line)
        if not duration_match or not size:
            raise RuntimeError("Could not inspect " + key)
        hours, minutes, seconds = map(float, duration_match.groups())
        source_duration = hours * 3600 + minutes * 60 + seconds
        sw, sh = map(int, size.groups())
        tw, th = (720, 1280) if item["portrait"] else (1280, 720)
        factor = min(1, tw / sw, th / sh)
        width, height = max(2, int(sw * factor) // 2 * 2), max(2, int(sh * factor) // 2 * 2)
        duration = min(item["duration_seconds"], source_duration)
        start = round(min(source_duration * item["start_fraction"], source_duration - duration), 3)
        common = ["-v", "error", "-threads", "2", "-filter_threads", "2", "-filter_complex_threads", "2", "-ss", str(start), "-i", str(path), "-t", str(duration), "-an"]
        vf = f"fps={item['fps']},scale={width}:{height}:flags=lanczos,setsar=1"
        gif, webp, poster = [output / (key + suffix) for suffix in (".gif", ".webp", ".jpg")]
        run([*common, "-filter_complex", vf + ",split[a][b];[a]palettegen=max_colors=192:stats_mode=diff[p];[b][p]paletteuse=dither=bayer:bayer_scale=3", "-loop", "0", "-y", str(gif)])
        run([*common, "-vf", vf, "-c:v", "libwebp_anim", "-quality", "78", "-compression_level", "4", "-loop", "0", "-threads", "2", "-y", str(webp)])
        run([*common, "-vf", f"scale={width}:{height}:flags=lanczos", "-frames:v", "1", "-q:v", "3", "-y", str(poster)])
        if gif.stat().st_size > config["max_gif_bytes"] or webp.stat().st_size > config["max_webp_bytes"]:
            raise RuntimeError(f"Size gate failed for {key}: GIF {gif.stat().st_size}, WebP {webp.stat().st_size}")
        row = {"source": source, "source_sha256": source_hash, "source_bytes": path.stat().st_size, "recipe_sha256": recipe_hash,
               "source_width": sw, "source_height": sh, "width": width, "height": height, "start_seconds": start,
               "duration_seconds": duration, "fps": item["fps"], "source_duration_seconds": source_duration}
        for kind, file in (("gif", gif), ("webp", webp), ("poster", poster)):
            row[kind] = "/" + str(file.relative_to(root))
            row[kind + "_bytes"] = file.stat().st_size
            row[kind + "_sha256"] = digest(file)
        manifest[key] = row
        temp = manifest_path.with_suffix(".tmp")
        temp.write_text(json.dumps(manifest, indent=2) + "\n")
        temp.replace(manifest_path)
        print(f"complete {key}: {width}x{height}, {duration}s, GIF {row['gif_bytes']}, WebP {row['webp_bytes']}", flush=True)


if __name__ == "__main__":
    main()

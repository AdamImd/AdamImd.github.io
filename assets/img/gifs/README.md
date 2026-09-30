# GIF showcase derivatives

These three-second, silent loops are excerpts of the public recordings listed in
`_scripts/gif-showcase-sources.json`. The originals remain unchanged. The SpotNLP
preview instead uses the project's existing rotation-gesture GIF; its caption
identifies that source rather than implying it is the navigation recording.

Each item has a real `.gif` download, an animated `.webp` for smaller browser
transfers, and a `.jpg` still. The GIF page initially loads stills and requests
animations only for visible cards. Pausing or scrolling away restores the still;
reduced-motion settings start paused. Browsers supporting WebP use that file and
others fall back to GIF. No video player, iframe, or audio is loaded on this page.

## Derivation

- Preserve the complete frame and aspect ratio, including both panels of the
  tactile recordings. No crop, frame interpolation, or speed-up.
- Bound landscape frames to 1280 × 720 and portrait frames to 720 × 1280. Do not
  upscale lower-resolution sources; the page displays each actual resolution.
- Sample at 12 frames/second, starting 40% into each source (clamped to fit).
  GIF timing is quantized to the format's centisecond resolution.
- GIF: 192-color palette, Bayer dithering. WebP: quality 78, compression level 4.
- Generation gates: animated WebP at most 1.8 MB, downloadable GIF at most 16 MB.
  The separate limits reflect the larger size of HD GIF encoding.

`_data/gif_showcase.json` records source locations, source and output SHA-256
hashes, dimensions, excerpt times, frame rates, byte sizes, and a recipe hash
covering both the item settings and generator source. Full recordings are linked
from every card. Existing evidence captions distinguish hardware footage,
sensor visualizations, simulations, and renderings.

## Rebuild

Requires Python 3 and FFmpeg with `libwebp_anim`, `palettegen`, and `paletteuse`:

```bash
python3 _scripts/build_gif_showcase.py --ffmpeg /path/to/ffmpeg --cache /durable/path/to/source-cache
```

Run from any directory. Use `--only tactile-fabric-touch alem-coalitions
g1-walking` for a representative subset. External recordings are cached once;
keep this cache for reproducibility. Each successful item updates the manifest
atomically, and subsequent runs reuse entries whose recipe/source/output hashes
match. A failed size gate leaves generated files for diagnosis but does not
update that item's manifest. Review any source changes before rebuilding.

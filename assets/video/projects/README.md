# Project recordings

General project-media sources are documented in `assets/img/projects/README.md` and the corresponding project pages.

## Tailorable sensing skins — IROS lightning talk V6

Adam supplied `Tailorable_IROS_Lightning_Talk_V6.pptx` and requested using its videos, including the sensor visualizations. Six embedded 1080 × 1920 H.264/AAC recordings are used on `/videos/` and `/projects/Tactile_Skin/`.

Each source video already combines physical footage above and the taxel visualization below. Preserve both panels and their original timing. These are recorded demonstrations, not live sensor feeds on the website. The gripper recording shows grasping while the arm skin is installed; it does not depict a gripper touching the arm skin.

The published files are stream-copy remuxes for progressive web playback (`moov` before `mdat`):

```sh
ffmpeg -i SOURCE.mp4 -map 0 -c copy -movflags +faststart DESTINATION.mp4
```

No cropping, trimming, re-encoding, or retiming was applied. Encoded video-stream SHA-256 hashes match the embedded sources. `tactile-talk-v6-provenance.json` records source-presentation hash, embedded members, slide mappings, published file hashes, dimensions, durations, and preview provenance. The presentation itself is not distributed here.

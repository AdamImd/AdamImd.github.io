# Spot whole-body policy gallery

The public page is `/projects/spot-whole-body-rl/`, authored in
`_projects/Spot_Whole_Body_RL.md`. Captions and visual descriptions live in
`_data/spotrl_showcase.yml`; `_includes/spotrl-video.liquid` renders the native
players, English description tracks, posters, and MP4 downloads. Styling is
scoped in `_sass/_spotrl.scss`. Videos load on demand and do not autoplay.

## Evidence and selection

These are saved Isaac Lab simulation rollouts from two separate studies:

- **Box tipping:** the partial iteration-7600 policy, rendered with source commit
  `d6e2437f04d66bddc5b435292977cc9b2387c65e`. The original 15-second collage has
  four environments chosen before their outcomes. Its first episodes include
  two valid tips, a support failure, and a timeout without a stable tip. The
  website deliberately selects successful env0 tips and the unsuccessful env3
  episode. This selection is for presentation and is not a success-rate estimate.
- **Crouching:** the frozen seed42 policy from source commit
  `4073885940e3b2a3f5afd7624ebe86627a76951d`. The visible final batch descends
  toward a 24 cm body-height target with the arm stowed. The lower 17 cm successes
  in the episode records are not filmed and are not claimed by the page. Both
  independent assessments failed the study's requirement of at least 80 percent
  whole-episode success in every populated motion/depth cell. A selected motion
  excerpt does not change that outcome.

The page adds no training, evaluation, tactile-sensing benefit, or physical
deployment claim. Cropping removes the original telemetry bars and other panels;
the short captions and optional context explain the examples. All clips retain
real-time speed, with no frame interpolation or generated motion. Episode resets
within the tipping excerpt remain visible. The crouch clip is a partial episode.

## Ownership and preserved originals

The private research sources on RPM (`cs-u-rpm-dt-03`) remain authoritative:

- `/home/adam/repos/research/research-spot-whole-body-tactile/experiments/box-visual-20261001/runs/collage-01/`
  owns `box-tipping-collage.mp4`, `render.json`, `primary-review.json`, and
  `validation-clarification.json`.
- `/home/adam/repos/research/research-spot-crouch-rpy-20261005/experiments/crouch-rpy-20261005/runs/final-seed42-terminal-01/`
  owns `rollout-readable-03.mp4`, its original `rollout.mp4`, telemetry, frozen
  evaluation, and scientific review. The campaign's `final-report/` records its
  full outcomes.

Collection, source rechecks, FFprobe metadata, and timestamped contact sheets are
preserved under the first repository's
`reports/portfolio-media-20261015/inventory-01/`. X1 review and publication evidence
are under `/mnt/c/Users/adami/Documents/Codex/2026-09-24/cl/work/spot-whole-body/`.
The accepted CPU presentation record is `reports/portfolio-media-20261015/presentation-02/` on RPM. Revision 01 is preserved; revision 02 tightens the hero and crouch crops to exclude neighboring robots at the right edge. Only approved presentation exports and their edit record enter this public repo.

## Rebuild the presentation exports

Use Python 3.11+ and FFmpeg/ffprobe with libx264. Place the two hash-matched source
videos in a directory using the filenames in `_scripts/spotrl-media-sources.json`:

```bash
python3 _scripts/build_spotrl_media.py \
  --source-dir /path/to/preserved/source-media \
  --output-root /path/to/site-or-export-root
```

The script checks source hashes before and after derivation, uses CPU FFmpeg with
two threads, writes H.264/yuv420p MP4s with fast-start metadata, fully decodes each
output, extracts posters, and creates
`assets/video/projects/spot-whole-body/provenance.json`. The recipe records exact
source timestamps, crop rectangles, speed, and poster timestamps. The manifest
records output dimensions, durations, hashes, and the FFmpeg version. The English
description tracks are separately authored `.vtt` files next to the videos.

Review the resulting frames before publication. Verify the production Jekyll
build, local links, live media decoding, keyboard/native playback, and mobile
layouts. Jekyll minifies JSON: compare the served provenance as a parsed JSON
object and compare binary video/image assets by their exact hashes.

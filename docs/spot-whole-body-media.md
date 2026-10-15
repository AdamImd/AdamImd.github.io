# Spot whole-body policy gallery

The public page is `/projects/spot-whole-body-rl/`, authored in
`_projects/Spot_Whole_Body_RL.md`. Captions and visual descriptions live in
`_data/spotrl_showcase.yml`; `_includes/spotrl-video.liquid` renders the native
players, English description tracks, posters, and MP4 downloads. Styling is
scoped in `_sass/_spotrl.scss`. Videos load on demand and do not autoplay.

## Native HD presentation

All three current clips are rendered by an Isaac Lab camera at **1920×1080,
25 fps**. These are studio replays of simulator root, joint, and object states
captured while running frozen policies. Every second 50 Hz state is displayed
at 25 fps and real-time speed, with no motion interpolation. Camera orbit, floor
appearance, studio lights, reflections, global illumination, and DLAA change
presentation. Rendering is kinematic and generates no new contact evidence.

The private rendering tools are `tools/export_portfolio_states.py` and
`tools/render_portfolio_hd.py`, documented in `docs/PORTFOLIO_HD.md` in the owning
research worktree. Native camera shape is asserted before H.264 encoding.
`assets/video/projects/spot-whole-body/provenance.json` binds the public exports
to the renderer, trace hashes, source checkpoints, and native camera dimensions.

## Evidence and selection

These are selected simulation behaviors from two separate studies:

- **Box tipping:** partial iteration-7600 policy from source commit
  `d6e2437f04d66bddc5b435292977cc9b2387c65e`, four environments, seed 3042,
  stage 5. Foreground env0 and env3 are selected before the new visualization
  rollout. The page shows successful tips with resets and an unsuccessful
  episode. It does not report a success-rate estimate.
- **Crouching:** frozen seed42 policy from source commit
  `4073885940e3b2a3f5afd7624ebe86627a76951d`. Capture uses the original final
  cohort beginning at command index 128, 32 environments and scenario seed 88146. Visible env0 descends toward a 24 cm body-height target with its arm
  stowed. The lower 17 cm successes in historical records are not filmed and
  are not claimed by the page. Both independent historical assessments failed
  the study's requirement of at least 80 percent whole-episode success in every
  populated motion/depth cell. A selected excerpt does not change that result.

The new visualization run is separate from the old assessment videos. No bitwise
trajectory equivalence is claimed. Policy/learner state and checkpoint hashes are
checked before and after capture. Full trace outcomes remain preserved. The
page adds no training, qualification, tactile-benefit, or physical deployment
claim. The crouch video is a partial episode.

## Ownership and preserved originals

The private research sources on RPM (`cs-u-rpm-dt-03`) remain authoritative:

- `/home/adam/repos/research/research-spot-whole-body-tactile/experiments/box-visual-20261001/runs/collage-01/`
  owns the original box collage, render metadata, primary review, and outcome
  clarification. Its source snapshot and partial checkpoint are preserved.
- `/home/adam/repos/research/research-spot-crouch-rpy-20261005/experiments/crouch-rpy-20261005/`
  owns the crouch checkpoint, geometry bank, original final assessment videos,
  telemetry, evaluation, and scientific review. `final-report/` records the full
  campaign outcomes.
- `/home/adam/repos/research/research-spot-portfolio-hd-20261015/`
  owns the new capture/render tools, protocol, immutable source, and durable
  records under `experiments/portfolio-hd-20261015/`. Only available RPM GPU0
  is used; GPU1 remains reserved for separate research evaluation.

The original source collection and CPU crop revisions are preserved under the
first repository's `reports/portfolio-media-20261015/`. They precede Adam's
explicit native-HD requirement and are superseded on the public page.

X1 review and publication evidence are under
`/mnt/c/Users/adami/Documents/Codex/2026-09-24/cl/work/spot-whole-body/`.
Only approved presentation exports and their edit record enter this public repo.

## Package approved HD exports

Use Python 3.11+ and ffprobe. The recipe
`_scripts/spotrl-media-sources.json` pins the accepted native render metadata,
video hashes, and poster frames. With its corresponding render output directory:

```bash
python3 _scripts/build_spotrl_media.py \
  --source-dir /path/to/accepted/native-render-output \
  --output-root /path/to/site-or-export-root
```

The script verifies native dimensions, H.264 encoding, durations, hashes, and
poster identity, then copies the approved pixels without resizing or re-encoding.
It writes the public provenance manifest and project card. English description
tracks are separately authored `.vtt` files next to the videos.

Before publication, require full video decode, primary visual review, production
Jekyll build, generated local links, live playback/seeking/captions, and mobile
layouts in light and dark themes. Jekyll minifies JSON: compare the served
provenance as a parsed JSON object and binary media by exact hashes.

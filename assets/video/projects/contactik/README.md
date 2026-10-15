# Contact IK explanatory videos

Three silent, annotated 1920×1080 H.264/yuv420p clips at 30 fps. Each clip is
16 seconds, with fast-start metadata for browser playback. English WebVTT
description tracks and page transcripts explain the visuals.

The source is a deterministic offline export from the existing ContactIK
research code. Both pose-only and contact-aware conditions apply the same joint
projection. This is an explicit visualization variant of the original objective.
The clips replay retimed optimizer iterates in Isaac Lab; they are separate from
closed-loop task evaluation and physical robot validation.

The original recorded contact point is fixed in world coordinates. The halo
illustrates an 8 cm penalty radius. The contact cost uses a synthetic geometric
atlas and is not a force or pressure measurement. The comparison changes only
the contact weight, retaining the same hand goal and joint bounds.

Public frame and video identities, source revision, and rendering settings are
recorded in the media provenance manifest. Full run records and editable rendering
source remain in the owning private ContactIK repository on RPM. The website page
is `/projects/Contact_Manipulation/`; media metadata is `_data/contactik_showcase.yml`.

The Franka Panda asset is provided by NVIDIA Isaac Sim, rendered using NVIDIA
Isaac Lab. Raw robot assets are not redistributed here.

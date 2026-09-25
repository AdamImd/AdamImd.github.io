---
layout: page
title: Astra / GPT-6 Zero-Shot UR5 Manipulation
description: An exploratory blue-marker pickup on the physical Thunder UR5e using wrist-camera observations.
img: assets/img/projects/ur5-thunder-marker.png
icon: fa-solid fa-robot
importance: 4
category: Systems
---

## Blue-marker pickup on Thunder

On September 6, 2026, I asked a GPT-6-based Astra controller to pick up a blue marker with the Thunder UR5e. The controller used observations from the wrist camera. In this recorded run, it completed the pickup in about 15 minutes. The frame below is from the robot's wrist camera during the run.

This is **one exploratory physical-robot demonstration**, not a benchmark of zero-shot reliability or a claim that the system can safely handle arbitrary objects or scenes.

{% include figure.liquid path="assets/img/projects/ur5-thunder-marker.png" alt="Thunder UR5e wrist-camera frame during the blue-marker pickup" class="img-fluid rounded z-depth-1" caption="Wrist-camera observation from the recorded blue-marker run. The gripper is holding the marker; this frame alone is not the complete outcome evidence." %}

{% include video.liquid path="assets/video/projects/ur5-thunder-zero-shot-marker.mp4" poster="assets/img/projects/ur5-thunder-marker.png" class="img-fluid rounded z-depth-1" controls=true caption="Annotated, accelerated video of the September 6 Thunder run. The source recording and hash-verified export are archived with the RPM dual-arm toolkit." %}

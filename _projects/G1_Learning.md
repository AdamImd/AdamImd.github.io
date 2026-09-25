---
layout: page
title: G1 Locomotion and Whole-Body Learning
description: Simulation studies of humanoid walking, supported pickup, and large-object enclosure.
img: assets/img/projects/g1-scene.png
icon: fa-solid fa-person-walking
importance: 6
category: Research
---

## From locomotion to contact-rich tasks

In Isaac Lab, I have studied Unitree G1 locomotion and manipulation tasks that need the body as well as the hands. A walking policy passed a frozen simulation evaluation. The pickup and large-object enclosure studies exposed harder control and validation problems: assisted pickup and relaxed enclosure were observed, while unassisted pickup and sustained strict enclosure remain open.

These results are **simulation-only**. They do not establish transfer to a physical G1 or safe autonomous behavior. The current work uses them to define better experiments for learning contact-aware whole-body skills.

## Simulation replays

{% include figure.liquid path="assets/img/projects/g1-scene.png" alt="Simulated Unitree G1 walking scene" class="img-fluid rounded z-depth-1" caption="Isaac Lab walking evaluation scene. The walking policy passed its frozen simulation evaluation." %}

{% include video.liquid path="assets/video/projects/g1-walking.mp4" class="img-fluid rounded z-depth-1" controls=true caption="Walking rollout in Isaac Lab (seed 2042); no physical transfer is implied." %}

{% include video.liquid path="assets/video/projects/g1-pickup.mp4" class="img-fluid rounded z-depth-1" controls=true caption="Supported-reach pickup development trace (seed 5146). Assistance is present; unassisted pickup remains unvalidated." %}

{% include figure.liquid path="assets/img/projects/g1-hug.png" alt="G1 strict-enclosure simulation diagnostic" class="img-fluid rounded z-depth-1" caption="Large-object enclosure diagnostic in simulation." %}

{% include video.liquid path="assets/video/projects/g1-hug.mp4" class="img-fluid rounded z-depth-1" controls=true caption="Near-miss enclosure replay (seed 9479). Sustained strict-enclosure success remains open." %}

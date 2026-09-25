---
layout: page
title: Remote Stroke Intervention Robotics
description: Telerobotic guidewires, vascular path planning, and learning data from a University of Minnesota–Medtronic collaboration.
img: assets/img/projects/stroke-guidewire-actuator.png
icon: fa-solid fa-heart-pulse
importance: 4
category: Research
---

## From remote control to navigation support

I co-authored three papers from the University of Minnesota's collaboration with Medtronic on tools for remote stroke treatment. They address different pieces of the same problem: a small telerobotic system for guidewire control, a way to turn patient-specific vascular geometry into a route-planning graph, and a 2D dataset for studying learning-based navigation. The [Minnesota Robotics Institute overview](https://cse.umn.edu/mnri/news/mnri-partners-medtronic-remote-stroke-treatment-research) describes the broader collaboration.

These are research and feasibility results. They do not demonstrate autonomous treatment or a clinically deployed system.

## Telerobotic guidewire prototype

<div class="row">
  <div class="col-md-6">
    {% include figure.liquid path="assets/img/projects/stroke-guidewire-actuator.png" alt="Compact two-degree-of-freedom guidewire actuator prototype with a coin for scale" class="img-fluid rounded z-depth-1" caption="Photograph of the compact bedside guidewire actuator from Figure 2 of the DMD 2026 paper. This is a benchtop prototype, not a clinical device." %}
  </div>
  <div class="col-md-6">
    {% include figure.liquid path="assets/img/projects/stroke-benchtop-navigation.png" alt="Benchtop guidewire navigation setup with a backlit planar vascular phantom" class="img-fluid rounded z-depth-1" caption="Figure 4 benchtop setup, advancing a guidewire through a planar vascular model. Local joystick control is shown; this is not an in-patient procedure." %}
  </div>
</div>

{% include figure.liquid path="assets/img/projects/stroke-network-latency.png" alt="Histograms of control-message round-trip time over local Wi-Fi, cellular hotspot, and residential Wi-Fi" class="img-fluid rounded z-depth-1" max-width="760px" caption="Figure 7 round-trip control-message latency across three network settings. These measurements do not establish complete procedural latency or clinical readiness." %}

## 2026 Design of Medical Devices papers

- [**Towards Remote Thrombectomy with Telerobotically-Driven Guidewires**](https://doi.org/10.1115/DMD2026-1079) reports a two-degree-of-freedom benchtop telerobotic platform and latency measurements across local, residential, and cellular connections.
- [**Vasculature Discretization and Search Space Simplification for Automating Catheter Navigation**](https://doi.org/10.1115/DMD2026-1054) converts 3D vascular models into reduced graph roadmaps for path planning. Its reported timing is a computational result, not a clinical navigation trial.
- [**StrokeNav2D: A Skeleton Based Dataset for Cerebrovascular Imitation Learning**](https://doi.org/10.1115/DMD2026-1063) presents 2D navigation samples derived from CT angiography for imitation-learning research. Its simplified geometry is a testbed, not a validated autonomous intervention policy.

My role was as a co-author on these team papers. The author lists and full methods are available at the linked ASME records.

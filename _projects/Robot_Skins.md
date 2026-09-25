---
layout: page
title: Robot-Wide Tactile Skin Design
description: Procedural CAD for layered sensing shells over UR5e, Spot, and G1 link geometry.
img: assets/img/projects/spot_assembled.png
icon: fa-solid fa-robot
importance: 5
category: Research
---

## Designing coverage beyond the gripper

Whole-body tactile sensing requires a practical way to fit sensing layers around curved robot housings, joints, and moving links. I am developing a configurable CAD pipeline that builds inner and outer shell layers from robot geometry while leaving clearances and installation openings.

The current geometry studies cover a UR5e arm, Boston Dynamics Spot with arm, and Unitree G1. The generated meshes have passed checks in recorded design poses. **Physical fabrication, fit, sensing behavior, and clearance through motion remain to be validated.** The designs are research prototypes, not production-ready skins.

This work connects sensor design with the longer-term goal of letting robots perceive and deliberately use contact across their bodies.

## Lite6 full-surface A2 prototype

A separate Lite6 design adapts the same approach to two curved arm links. It lays out one 5 × 6 [wireless tactile matrix]({% link _projects/Wireless_Tactile_PCB.md %}) per link, with printed inner and outer shells, continuous electrode bands, and removable electronics mounts. The selected CAD package includes checked printable parts and aligned assembly exports. Layout coverage of the usable surfaces was 94.31% on link 2 and 93.83% on link 4.

The motion screen still found poses with potential interference. Physical fit, laminate installation, electrical calibration, and safe movement with the skins attached remain open; the percentages describe a CAD layout, not sensed coverage on an operating robot.

## UR5e CAD walkthrough

This 34-second film shows the proposed layered shells on a UR5e. It is a visualization of the design geometry, not footage of fabricated or operating sensors. The Spot and G1 designs appear in the still previews below.

{% include video.liquid path="assets/video/projects/ur5e-tactile-skins-cad.mp4" poster="/assets/img/projects/ur5e-skin-assembled.png" class="img-fluid rounded z-depth-1" controls=true caption="UR5e tactile-skin CAD walkthrough. Fit through motion, fabrication, and sensing performance remain to be tested." %}

## Geometry previews

{% include figure.liquid path="assets/img/projects/ur5e-skin-assembled.png" alt="CAD render of tactile shell layers assembled on a UR5e arm" class="img-fluid rounded z-depth-1" caption="UR5e shell assembly rendered from generated geometry. This shows a checked design pose, not fabrication or sensor operation." %}

{% include figure.liquid path="assets/img/projects/spot_assembled.png" alt="CAD render of tactile shell parts around Spot" class="img-fluid rounded z-depth-1" caption="Spot with arm: assembled CAD preview of proposed tactile shell coverage." %}

{% include figure.liquid path="assets/img/projects/g1_assembled.png" alt="CAD render of tactile shell parts around a Unitree G1" class="img-fluid rounded z-depth-1" caption="G1: assembled CAD preview. Physical fit and moving-link clearance still need validation." %}

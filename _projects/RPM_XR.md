---
layout: page
title: Robot Sensing in Extended Reality
description: Quest and desktop tools for viewing robot sensors, replaying demonstrations, and studying tactile interfaces.
img: assets/img/projects/xr-contact-scope.png
icon: fa-solid fa-vr-cardboard
importance: 3
category: Systems
---

## Making robot state visible

I am building an extended-reality research suite around Meta Quest, Godot/OpenXR, and robot simulation. Its applications explore tactile heatmaps, contact forces, demonstration review, sensor placement, and comparisons between possible future actions.

The suite includes simulation and offline replay workflows for Spot, G1, and dual-arm systems. A separate read-only G1 sensor pipeline records and displays selected live observations. **Live telepresence and physical robot control remain separate commissioning work**; the current Quest applications should be understood as research interfaces and prototypes.

These tools help researchers see what a robot sensed and inspect why a manipulation attempt succeeded or failed.

## G1 in VR: Human World mode

A separate Quest/G1 teleoperation prototype places the headset in a room-scale **human viewpoint** independent of the simulated robot's body motion. Both hands command world-space palm targets, while the robot follows through bounded inverse kinematics and a posture controller. This makes it possible to study walking and two-handed reach without attaching the viewer's camera to the robot's head.

The Human World implementation passed 39 targeted CPU tests. In Isaac simulation, five standing validation episodes passed with no recorded falls or joint-limit violations; the reachable palm-target 95th-percentile error was at most 1.67 cm. A walking diagnostic stayed upright but missed its tracking target, so walking remains experimental. The Quest app was installed, but a GPU conflict blocked the live Human World session. **On-device Human World acceptance and physical-G1 operation have not been demonstrated.**

These are [G1 simulation and VR-control studies]({% link _projects/G1_Learning.md %}); the locomotion and pickup videos on that page show separate Isaac Lab policies, not this Human World Quest controller.

## Interface previews

{% include figure.liquid path="assets/img/projects/xr-contact-scope.png" alt="Contact Scope interface for inspecting simulated contact signals" class="img-fluid rounded z-depth-1" avoid_scaling=true caption="Contact Scope screenshot from an offline simulation and replay UX audit. It is a research interface preview, not a live robot view." %}

{% include figure.liquid path="assets/img/projects/xr-demo-forge.png" alt="Demo Forge research interface screenshot" class="img-fluid rounded z-depth-1" avoid_scaling=true caption="Demo Forge screenshot from the same offline audit, used to inspect recorded demonstration data." %}

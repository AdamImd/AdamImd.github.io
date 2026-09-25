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

## Interface previews

{% include figure.liquid path="assets/img/projects/xr-contact-scope.png" alt="Contact Scope interface for inspecting simulated contact signals" class="img-fluid rounded z-depth-1" avoid_scaling=true caption="Contact Scope screenshot from an offline simulation and replay UX audit. It is a research interface preview, not a live robot view." %}

{% include figure.liquid path="assets/img/projects/xr-demo-forge.png" alt="Demo Forge research interface screenshot" class="img-fluid rounded z-depth-1" avoid_scaling=true caption="Demo Forge screenshot from the same offline audit, used to inspect recorded demonstration data." %}

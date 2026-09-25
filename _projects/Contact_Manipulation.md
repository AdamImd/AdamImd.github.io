---
layout: page
title: Contact-Aware Manipulation
description: Exploring inverse kinematics and whole-body strategies that respond to contact along a robot's body.
img: assets/img/projects/planar-scene.png
icon: fa-solid fa-hand
importance: 4
category: Research
---

## Learning to use body contact

Most manipulation systems plan around the gripper and treat other contact as a collision. My current research asks when contact at the arm, torso, or base can improve a task, and how a robot can sense and control it.

I have studied contact-aware inverse kinematics, sensing-aware placement of tactile skins, and simulated whole-body pushing, bracing, and pivoting. These are **analytic and simulation studies**. They establish software baselines and expose limitations; they do not demonstrate a general contact-rich policy on physical hardware.

The next research step is to connect distributed sensing to control and learning on a real robot, starting with bounded, supervised experiments.

## What the current studies show

{% include figure.liquid path="assets/img/projects/contactik-avoidance.svg" alt="Twelve-case fixed-point contact avoidance comparison" class="img-fluid rounded z-depth-1" caption="Original fixed-weight contact-aware IK study: the avoidance objective reduced violation in all 12 numerical cases, with a nonzero residual in 11. This is an analytic result, not robot hardware validation or a result from the later ContactIK-MPC work." %}

{% include figure.liquid path="assets/img/projects/planar-scene.png" alt="Planar simulated robot and contact funnel" class="img-fluid rounded z-depth-1" avoid_scaling=true caption="Planar whole-body contact simulation used to diagnose the pushing and bracing task setup. It does not establish a learned manipulation policy." %}

---
layout: page
title: AugInsert
description: Data augmentation for robust visual-force policies in contact-rich assembly (IROS 2025).
img: assets/img/publication_preview/auginsert.jpg
importance: 3
category: Research
---

## Robustness in object assembly

AugInsert studies how a dual-arm robot can finish a peg-in-hole insertion after contact begins. The policy combines visual observations, force/torque readings, and proprioception. Online augmentation expands a limited set of human demonstrations with changes in grasp pose, object geometry, appearance, camera pose, and sensor noise.

The paper evaluates these factors **in simulation** and finds that grasp variation is particularly challenging. It also studies the contribution of force/torque sensing to robustness. I co-authored this work with Ryan Diaz, Vivek Veeriah, and Karthik Desingh; it appeared at IROS 2025.

[Read the paper](https://arxiv.org/abs/2410.14968).

## Paper video and figures

{% include video.liquid path="https://www.youtube.com/embed/UTA7sefgs2o" class="w-100 rounded z-depth-1" width="100%" height="420" title="AugInsert project video" caption="The authors' public project video shows the assembly setup and evaluation." %}

The [AugInsert project page](https://rpm-lab-umn.github.io/auginsert/) has the model diagram, augmentation examples, and evaluation videos. The results shown there are part of the published study; the page distinguishes simulation evaluations from its real-world augmentation study.

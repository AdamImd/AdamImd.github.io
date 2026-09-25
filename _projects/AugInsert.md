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

<figure><video class="img-fluid rounded z-depth-1" width="100%" controls preload="metadata" aria-label="AugInsert real-world assembly study animation"><source src="https://rpm-lab-umn.github.io/auginsert/media/video/real_world_exp_animation.mp4" type="video/mp4">Your browser does not support this video.</video><figcaption class="caption">Real-world augmentation study animation from the public AugInsert project page. See the paper for the evaluation protocol.</figcaption></figure>

The [AugInsert project page](https://rpm-lab-umn.github.io/auginsert/) has the model diagram, augmentation examples, and evaluation videos. The results shown there are part of the published study; the page distinguishes simulation evaluations from its real-world augmentation study.

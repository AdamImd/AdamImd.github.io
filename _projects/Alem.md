---
layout: page
title: Alem Multi-Agent Coordination
description: Experiments on communication, specialization, and leadership in a shared multi-agent world.
img: assets/img/projects/alem64.png
icon: fa-solid fa-people-group
importance: 5
category: Systems
---

## Coordination at scale

I use Alem, a multi-agent survival benchmark, to study how teams coordinate over long tasks. The [AlemDICE research fork](https://github.com/AdamImd/AlemDICE) reproduces a small LLM-agent baseline and provides a starting point for experiments on leadership, role coherence, and failures in communication.

My broader studies compare sparse communication, hierarchical organization, and contract-market ideas. These are **simulation experiments**. An initial held-out market study did not support its proposed positive efficiency claim, so the portfolio treats that result as a finding about the current method rather than a solved coordination problem.

The goal is to understand which coordination structures remain useful as teams and tasks grow.

## Recorded simulations

{% include figure.liquid path="assets/img/projects/alem64.png" alt="Map of 64 simulated Alem agents and their task locations" class="img-fluid rounded z-depth-1" caption="A recorded 64-agent Alem replay. The map illustrates the test environment and agent distribution, not a performance comparison." %}

{% include video.liquid path="assets/video/projects/alem-coalitions.mp4" class="img-fluid rounded z-depth-1" controls=true caption="Coalition behavior in one deterministic simulation replay (seed 10008)." %}

{% include video.liquid path="assets/video/projects/alem-comparison.mp4" class="img-fluid rounded z-depth-1" controls=true caption="Side-by-side coordination methods in the same simulated setting. This clip is illustrative; the held-out study did not establish an efficiency advantage." %}

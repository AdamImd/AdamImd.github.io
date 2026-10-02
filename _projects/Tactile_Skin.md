---
layout: page
title: Tailorable Force-Sensing Skins
description: Textile and additive-manufactured sensing layers for whole-arm contact; accepted at IROS 2026.
img: assets/img/projects/thumbnails/Tactile_Skin.jpg
importance: 1
category: Research
stage: IROS 2026
---

## The question

How can a robot sense contact along its arm without relying only on force/torque sensors at the wrist? With Heidi Woelfle, Brad Holschuh, and Karthik Desingh, I developed a tailorable force-sensing skin that combines textile sensing materials with additive-manufactured structures.

The work studies fabrication, sensor response, and integration on manipulator surfaces. It is **accepted for the IROS 2026 conference proceedings**. A related submission was accepted as a poster at the IROS 2026 Scalable Tactile Sensing for Dexterous Manipulation workshop.

## Why it matters

Contact can happen anywhere along a robot's body. A distributed skin could help detect and localize those interactions, supporting safer and more capable contact-aware manipulation. The project is part of my broader work on learning to use body contact.

## Project materials

- [Public project page, figures, and video](https://rpm-lab-umn.github.io/TactileSkin/)
- [Workshop submission](https://openreview.net/forum?id=TyIYPuqcfc)

The published project page reports sensor experiments. Extensions toward full-body coverage and contact-aware control are ongoing research, not claims of completed robot-wide validation.

## See the sensors in use

{% include figure.liquid path="https://rpm-lab-umn.github.io/TactileSkin/static/images/figures/sensor_overall_both_v4.png" url="https://rpm-lab-umn.github.io/TactileSkin/static/images/figures/sensor_overall_both_v4.png" alt="Tailorable textile and printed tactile sensing layers" class="img-fluid rounded z-depth-1" avoid_scaling=true caption="Sensor constructions from the public TactileSkin project page." %}

### Physical interaction and sensor readouts

These six recordings come from my IROS lightning talk. Each preserves the physical view above and the sensor visualization below, with the original timing. The colored taxels show the recorded sensor response; consult the paper for calibration and quantitative evaluation.

{% assign skin_section = site.data.video_showcase | where: "id", "sensing-skins" | first %}
<div class="video-showcase-grid video-showcase-grid--portrait">
{% for video in skin_section.videos %}
  {% include showcase-video.liquid video=video hide_project_link=true %}
{% endfor %}
</div>

[Browse the full video showcase]({% link _pages/videos.md %}).

---
layout: page
title: Spot Whole-Body Reinforcement Learning
description: Learned box tipping, crouching, and body reorientation.
permalink: /projects/spot-whole-body-rl/
img: assets/img/projects/spot-whole-body/spot-card.jpg
icon: fa-solid fa-dog
importance: 4
category: Research
stage: Simulation research
---

<div class="spotrl-page">

<div class="spotrl-intro"><span class="spotrl-badge">Selected policy rollouts</span><span>Isaac Lab simulation</span><nav aria-label="Rollout chapters"><a href="#spot-box">Box tipping</a><a href="#spot-crouch">Body control</a><a href="#spot-outtake">Outtake <span aria-hidden="true">↘</span></a></nav></div>

<section id="spot-box" class="spotrl-chapter" aria-labelledby="spot-box-title">
<div class="spotrl-heading"><span class="spotrl-number" aria-hidden="true">01</span><div><p class="spotrl-eyebrow">Manipulation</p><h2 id="spot-box-title">Tip the box.</h2></div></div>
{% include spotrl-video.liquid media=site.data.spotrl_showcase.box %}
</section>

<section id="spot-crouch" class="spotrl-chapter" aria-labelledby="spot-crouch-title">
<div class="spotrl-heading"><span class="spotrl-number" aria-hidden="true">02</span><div><p class="spotrl-eyebrow">Whole-body control</p><h2 id="spot-crouch-title">Get low. Stay balanced.</h2></div></div>
{% include spotrl-video.liquid media=site.data.spotrl_showcase.crouch %}
</section>

<section id="spot-outtake" class="spotrl-chapter" aria-labelledby="spot-outtake-title">
<div class="spotrl-heading"><span class="spotrl-number" aria-hidden="true">03</span><div><p class="spotrl-eyebrow">The outtake</p><h2 id="spot-outtake-title">Almost had it.</h2></div><span class="spotrl-outtake-tag">Failed attempt</span></div>
{% include spotrl-video.liquid media=site.data.spotrl_showcase.outtake %}
</section>

<details class="spotrl-context"><summary>About these rollouts</summary><p>Selected examples from separate reinforcement-learning studies in simulation. Box-tipping footage comes from a partial policy checkpoint. The crouch policy learns leg-joint control with the arm stowed; its full assessment did not meet the study's criterion in every tested condition. Selected behaviors do not estimate overall success or demonstrate physical-robot performance.</p><p><a href="{{ 'assets/video/projects/spot-whole-body/provenance.json' | relative_url }}">Media sources &amp; edit record</a> · Related: <a href="{% link _projects/Contact_Manipulation.md %}">Contact IK</a> · <a href="{% link _projects/SpotNLP.md %}">SpotNLP</a></p></details>

</div>

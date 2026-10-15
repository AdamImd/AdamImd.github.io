---
layout: page
title: Contact IK
description: Inverse kinematics that lets the whole arm respond to touch.
img: assets/img/projects/contactik/contactik-card.jpg
icon: fa-solid fa-hand
importance: 4
category: Research
stage: Research in progress
---

<div class="contactik-page" markdown="1">

<div class="contactik-intro">
  <p class="contactik-eyebrow">Differentiable IK <span>·</span> Whole-arm contact <span>·</span> Isaac Lab</p>
  <h2>Reach with the hand.<br>Respond with the whole arm.</h2>
  <p class="contactik-lead">A touch on the arm changes the problem. Contact IK puts that information inside the inverse-kinematics objective, so the robot can adjust its posture while pursuing a hand goal.</p>
  <nav class="contactik-jump" aria-label="On this page"><a href="#watch-contactik">Watch the demos <span aria-hidden="true">↓</span></a><a href="#how-contactik-works">How it works</a><a href="#contactik-evidence">Results &amp; context</a></nav>
</div>

<section id="watch-contactik" class="contactik-section" aria-labelledby="contactik-watch-title" markdown="1">

<div class="contactik-section-heading"><div><p class="contactik-eyebrow">Watch it happen</p><h2 id="contactik-watch-title">Same goal. A different solve.</h2></div><span class="contactik-evidence-tag">Offline IK visualizations</span></div>

{% include contactik-video.liquid media=site.data.contactik_showcase.hero %}

<div class="contactik-legend" aria-label="Video legend"><span><i class="contactik-dot contactik-dot-goal" aria-hidden="true"></i>Cyan: hand goal</span><span><i class="contactik-dot contactik-dot-contact" aria-hidden="true"></i>Amber: contact input</span><span>Readouts: remaining task error &amp; contact cost</span></div>

</section>

<section id="how-contactik-works" class="contactik-section" aria-labelledby="contactik-how-title" markdown="1">

<p class="contactik-eyebrow">The idea</p>
<h2 id="contactik-how-title">Give contact a place in the objective.</h2>

<div class="contactik-steps">
  <article><span class="contactik-step-number">01</span><h3>Locate the touch</h3><p>Express an observed contact point in the robot's world frame. Link geometry tells the solver how sampled surface points move with each joint.</p></article>
  <article><span class="contactik-step-number">02</span><h3>Combine the objectives</h3><p>Keep the hand-pose goal, add a penalty for sampled points near the contact input, and include joint-limit terms.</p></article>
  <article><span class="contactik-step-number">03</span><h3>Update the posture</h3><p>Differentiate through forward kinematics and update the joints. The contact term can change the solution across the arm.</p></article>
</div>

<div class="contactik-equation" aria-label="Minimize the sum of task error, weighted contact cost, and joint-limit cost"><span class="contactik-equation-label">Find a joint configuration</span><div><span class="contactik-term-goal">task error</span><b>+</b><span class="contactik-term-contact">λ · contact cost</span><b>+</b><span>joint-limit cost</span></div><p>The comparison changes only the contact weight: λ = 0 on the left, λ = 1 on the right.</p></div>

<details class="contactik-method"><summary>A closer look at the contact term</summary><p>The illustrated formulation sums squared penalties for sampled points within an 8 cm radius of a fixed observed contact point. The samples form a synthetic geometric atlas. The cost is an optimization signal; it is not a pressure measurement or a guarantee of collision-free motion.</p><p>Both rendered conditions project each optimizer update to the same joint bounds. This explicit visualization modification keeps the displayed configurations bounded. The original study below used the unprojected formulation with a final command-boundary projection.</p></details>

</section>

<section class="contactik-section" aria-labelledby="contactik-detail-title" markdown="1">

<p class="contactik-eyebrow">Explore the geometry</p>
<h2 id="contactik-detail-title">Look closer.</h2>

<div class="contactik-demo-grid">
{% for demo in site.data.contactik_showcase.demos %}
<article class="contactik-demo"><h3>{{ demo.title }}</h3>{% include contactik-video.liquid media=demo %}</article>
{% endfor %}
</div>

<p class="contactik-render-note">Rendered in NVIDIA Isaac Lab with the Franka Panda asset from Isaac Sim. The clips replay and retime offline optimizer iterates from recorded exploratory states. They show a joint-bounded variant of the original Contact IK objective; closed-loop force control and hardware performance require separate evaluation.</p>

</section>

<section id="contactik-evidence" class="contactik-section contactik-findings" aria-labelledby="contactik-evidence-title" markdown="1">

<p class="contactik-eyebrow">Results &amp; context</p>
<h2 id="contactik-evidence-title">What the original study showed</h2>

The original formulation study evaluated 28 recorded Franka states, including 12 with contact. The contact term reduced the avoidance residual in every contact-positive case. Pose accuracy, solve speed, and reliable convergence remained limiting.

<div class="contactik-findings-grid"><div><strong>12 / 12</strong><span>Contact cases with a lower avoidance residual</span></div><div><strong>0 / 12</strong><span>Contact cases meeting the full pose-success criterion</span></div><div><strong>28 states</strong><span>Kinematic evaluation; physical validation pending</span></div></div>

{% include figure.liquid path="assets/img/projects/contactik-avoidance.svg" alt="Original ContactIK avoidance residual before and after optimization for twelve contact-positive cases" class="img-fluid" caption="Original fixed-weight formulation: lower avoidance residual in all 12 contact-positive cases, with a nonzero residual in 11. These historical numbers belong to the original evaluation, rather than the joint-bounded render variant." %}

### Where the research goes next

My broader work connects contact sensing to manipulation along the arm and body. The first hardware direction is the Spot arm with the existing [force-sensing skins]({% link _projects/Tactile_Skin.md %}), using bounded, supervised experiments. Related simulation studies explore pushing, bracing, and pivoting.

**ContactIK-MPC is a separate research extension.** It adds learned objectives and short-horizon contact prediction. The videos on this page demonstrate the original geometric idea and its joint-bounded visualization variant.

<details class="contactik-method"><summary>Related whole-body simulation</summary><p>A planar pushing and bracing setup helped diagnose whole-body contact tasks. It is a separate simulation study, with learned-policy and hardware validation still open.</p>{% include figure.liquid path="assets/img/projects/planar-scene.png" alt="Planar robot and funnel used in a separate contact-manipulation simulation" class="img-fluid rounded" avoid_scaling=true %}</details>

<p class="contactik-credits">Rendering tools: <a href="https://github.com/isaac-sim/IsaacLab">NVIDIA Isaac Lab</a> · <a href="https://docs.isaacsim.omniverse.nvidia.com/5.1.0/assets/usd_assets_robots.html">Isaac Sim robot assets</a> · <a href="{{ 'assets/video/projects/contactik/provenance.json' | relative_url }}">Media provenance</a>. Clips are silent and include optional English descriptions and MP4 downloads.</p>

</section>

</div>

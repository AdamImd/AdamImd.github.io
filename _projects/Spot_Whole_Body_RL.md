---
layout: page
title: Spatial Touch for Support Transfer in Whole-Body Package Handling
description: A Spot quadruped uses its arm and back to load, carry, and release a bulky carton.
permalink: /projects/spot-whole-body-rl/
img: assets/img/projects/spot-whole-body/warehouse-delivery-continuous.jpg
icon: fa-solid fa-dog
importance: 4
category: Research
stage: Simulation research
---

<div class="spotrl-page">

<div class="spotrl-lead">
<p>A carton can be light enough to carry and too wide to grasp. Spot can brace it against a rear deck, but has to know when the deck has taken its weight. The same problem arises at delivery. One corner can touch the floor while most of the load still rests on the robot.</p>
<a class="spotrl-paper-link" href="{{ 'assets/pdf/spatial-touch.pdf' | relative_url }}">Read the working manuscript <span aria-hidden="true">↗</span></a>
</div>

<section id="warehouse-delivery" class="spotrl-chapter" aria-labelledby="delivery-title">
<div class="spotrl-heading"><h2 id="delivery-title">One continuous warehouse delivery</h2></div>
{% include spotrl-video.liquid media=site.data.spotrl_showcase.delivery %}
<p class="spotrl-result">In this simulated trial, Spot carried the 0.93 kg carton 11.38 m around the marked fire lane. The carton finished fully inside bay B. Over the final second, the floor supported 9.12 N and the arm and deck carried zero measured carton load. <a href="{{ 'assets/video/projects/spot-whole-body/warehouse-delivery-continuous.json' | relative_url }}">Trial measurements</a></p>
</section>

<section id="spatial-touch" class="spotrl-chapter" aria-labelledby="touch-title">
<div class="spotrl-heading"><h2 id="touch-title">Feeling where the weight goes</h2></div>
<p>A single force reading can tell Spot that it touched the box. A pressure map also shows which part of the deck supports it and where the gripper is pressing. We study whether that information helps Spot decide when to stand and when to withdraw its arm.</p>
<figure class="spotrl-teaser"><a href="{{ 'assets/img/projects/spot-whole-body/task-and-tactile-teaser.png' | relative_url }}" aria-label="Open the task sequence and tactile maps at full resolution"><img src="{{ 'assets/img/projects/spot-whole-body/task-and-tactile-teaser.png' | relative_url }}" loading="lazy" alt="The upper row follows the carton from the floor to the receiving bay. Below, a loaded pose is paired with normal forces from the deck grid and gripper patches at that instant."></a><figcaption>One simulation from righting to walk-away. At 92.00 s, the 54 deck cells measured 22.94 N in total, and the six gripper patches measured 6.05 N. <a href="{{ 'assets/img/projects/spot-whole-body/task-and-tactile-teaser.png' | relative_url }}">Enlarge figure</a></figcaption></figure>
<p>The task planner (S3) chooses a skill from the available actions using onboard camera observations. The package controller (S2) uses sensor history to adjust the brace and manage the transfer. The locomotion controller (S1) tracks body posture and walking commands. In this trial, S3 used ideal base localization and the righting controller used simulated carton orientation to finish the tip.</p>
</section>

<section id="transfer-results" class="spotrl-chapter" aria-labelledby="transfer-results-title">
<div class="spotrl-heading"><h2 id="transfer-results-title">How much does spatial touch help?</h2></div>
<p>Four controllers each attempted the same 32 held-out simulated transfers. Each trial began seated and required Spot to load the carton, hold it, lower it, and release it.</p>
<table class="spotrl-results"><caption>Completed load–hold–unload cycles</caption><thead><tr><th scope="col">Sensor input</th><th scope="col">Completed</th></tr></thead><tbody>
<tr><th scope="row">Vision and robot history</th><td>20 / 32</td></tr>
<tr><th scope="row">Add force totals on each surface</th><td>10 / 32</td></tr>
<tr><th scope="row">Add contact centroids and footprints</th><td>9 / 32</td></tr>
<tr class="spotrl-full-field"><th scope="row">Add the full spatial pressure field</th><td>23 / 32</td></tr>
</tbody></table>
<p>Full spatial touch completed three more transfers than vision and robot history alone. The paired difference was 9.4 percentage points, with a 95% bootstrap interval from −6.25 to +25.0 points. Initial alignment mattered. With full touch, all eight nominal starts succeeded, compared with one of eight misaligned starts.</p>
<p>A separate standing-start evaluation exposed a mechanical limit. All 48 attempts reached a gripper joint limit before lift. The warehouse film shows a revised pickup controller completing one development layout.</p>
<p>The planned 224-episode hardware study will measure support independently and test how gently Spot handles the contents. Synchronized inertial sensors on each carton wall and on each test item inside will record shocks and rotation through loading, walking, and placement. Physical carton-transfer results are pending.</p>
</section>

<section aria-labelledby="earlier-policies">
<div class="spotrl-heading"><h2 id="earlier-policies">Earlier policies</h2></div>
<div class="spotrl-intro"><span class="spotrl-badge">Selected policy rollouts</span><span>Isaac Lab · Native 1080p</span><nav aria-label="Rollout chapters"><a href="#spot-box">Box tipping</a><a href="#spot-crouch">Body control</a><a href="#spot-outtake">Outtake <span aria-hidden="true">↘</span></a></nav></div>

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

<details class="spotrl-context"><summary>About these rollouts</summary><p>Native HD studio replays of recorded simulator states from separate reinforcement-learning studies. The saved policies are frozen during state capture; the studio replays their motion kinematically. Box-tipping footage comes from a partial policy checkpoint. The crouch policy learns leg-joint control with the arm stowed; its full assessment did not meet the study's criterion in every tested condition. Selected behaviors do not estimate overall success or demonstrate physical-robot performance.</p><p>Simulation and rendering: <a href="https://github.com/isaac-sim/IsaacLab">NVIDIA Isaac Lab</a>. Spot model and configuration: <a href="https://github.com/rai-opensource/relic">ReLIC</a>.</p><p><a href="{{ 'assets/video/projects/spot-whole-body/provenance.json' | relative_url }}">Media sources &amp; edit record</a> · Related: <a href="{% link _projects/Contact_Manipulation.md %}">Contact IK</a> · <a href="{% link _projects/SpotNLP.md %}">SpotNLP</a></p></details>

</section>

</div>

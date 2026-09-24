---
layout: page
title: Visual Futures for Manipulation
description: Exploring whether generated future video can guide robot actions, and where visual plans fall short.
img: assets/img/GenAI/WAN.webp
importance: 8
category: Research
---

# Overview

This exploratory project asks whether a pretrained video model can suggest useful future observations for a manipulation policy. The visuals below illustrate the proposed pipeline; they are not evidence of reliable zero-shot robot performance.

<div class="row justify-content-center">
    <div class="col-sm-10 mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/GenAI/WAN.webp" title="Generated video example for a manipulation prompt" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    Example generated sequence for the prompt "Untie the knot"; an illustration of the proposed approach, not a robot-success result.
</div>

The pipeline generates candidate future frames from a current observation and text goal, then uses them as context for action prediction. Subsequent visual-plan experiments did not pass their registered benefit gate, so this remains a research question rather than a validated zero-shot manipulation system.

<div class="row justify-content-center">
    <div class="col-sm-10 mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/GenAI/arch.png" title="System Architecture" class="img-fluid rounded z-depth-1" %}
    </div>
</div>

The proposed policy uses the current observation and a feature derived from predicted frames. Cross-attention provides one way to combine the present observation with imagined futures. The next step is to test when those predictions add useful information beyond a policy trained on observed data.
## Project proposal

The original [course project proposal](/assets/pdf/VE.pdf) records the motivation and planned architecture. It predates the later evaluation and should be read as a proposal.

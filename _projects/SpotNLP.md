---
layout: page
title: SpotNLP
description: A Natural Language Interface for Boston Dynamics Spot
img:
importance: 3
category: work
---


This project involves developing a natural language interface for the Boston Dynamics Spot robot, enabling users to command the robot using everyday language. By integrating large language models (LLMs) with Spot's control systems, we aim to facilitate intuitive interactions and enhance the robot's usability in various environments.


# SpotNLP: Overview. 
<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include video.liquid path="https://drive.google.com/file/d/1gJQImMGEnGH4fOe8TpPvDU1NuAJ4rH7D/preview" class="img-fluid rounded z-depth-1" controls=true autoplay=true %}
    </div>
</div>

<div class="caption">
    SpotNLP in action: Spot Following natural language commands for a Demo for DoD representatives. Spot is instructed to follow the controller, save semantic keypoints, and navigate given contextual information about the environment.
</div>



<!-- https://docs.google.com/presentation/d/1ZNhnRRa5fr2BqYxXX8ax2uWAo9YG3EmxY5pKJuxG-Ic/edit?usp=sharing -->
# Human Following / Gesture Recognition
<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include video.liquid path="https://drive.google.com/file/d/1gJQImMGEnGH4fOe8TpPvDU1NuAJ4rH7D/preview" class="img-fluid rounded z-depth-1" controls=true autoplay=true %}
    </div>
</div>
<div class="caption">
    Spot follows humans using segmentation models. XMem is used to propigate the original segmentation mask throughout time, leading Spot to be robust to distractions in crowded environments and occlusions. Spot also recognizes simple gestures to start and stop following.
</div>
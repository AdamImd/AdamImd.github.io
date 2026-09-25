---
layout: page
title: SpotNLP
description: A natural-language and gesture interface for Boston Dynamics Spot, with human following and semantic navigation demos.
img: assets/img/Spot/demo.webp
importance: 4
category: Systems
---

## GitHub Repository
<div class="repositories d-flex flex-wrap flex-md-row flex-column justify-content-between align-items-center">
  {% include repository/repo.liquid repository='RPM-lab-UMN/SpotNLP' %}
</div>

# Overview
This project involves developing a natural language interface for the Boston Dynamics Spot robot, enabling users to command the robot using everyday language. By integrating large language models (LLMs) and gesture detection with Spot's control systems, we aim to facilitate intuitive interactions and enhance the robot's usability in various environments.

<!-- Insert figure assets/img/SpotNLP_Diagram.png -->
<div class="row justify-content-center">
    <div class="col-sm-10 mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/SpotNLP_Diagram.png" title="SpotNLP System Diagram" class="img-fluid rounded z-depth-1" %}
    </div>
</div>

<div>
    {% include figure.liquid path="assets/img/Spot/demo.webp" title="SpotNLP in Action" class="img-fluid rounded z-depth-1" %}
</div>

## Human Following / Gesture Recognition
<div class="row justify-content-center" style="width: 80%; margin: 0 auto;">
    <div class="col-sm-6 mt-3 mt-md-0" >
        {% include video.liquid path="https://drive.google.com/file/d/1gJQImMGEnGH4fOe8TpPvDU1NuAJ4rH7D/preview?embedded=true" class="img-fluid rounded z-depth-1" height="400" controls=true autoplay=true %}
    </div>
</div>

<div class="caption">
    Recorded SpotNLP demonstration: Spot follows the controller, saves semantic keypoints, and navigates using contextual information about the environment.
</div>

<div class="caption">
    Spot follows a selected person using segmentation models. XMem propagates the initial mask across frames to help maintain the track through distractions and occlusions in the recorded demonstrations. Spot also recognizes gestures to start and stop following.
</div>

<div class="row justify-content-center" style="width: 80%; margin: 0 auto;">
    <div class="col-sm-6 mt-3 mt-md-0">
        {% include video.liquid path="https://drive.google.com/file/d/1DzkEhDpsXLYuy0WCevADSRJa6uH253XG/preview?embedded=true" class="img-fluid rounded z-depth-1" controls=true autoplay=false %}
    </div>
</div>


<div class="caption">
    MediaPipe initializes a segmentation mask when a person makes a T pose. XMem propagates the mask over time to help maintain the track when other people enter the scene or the controller is temporarily occluded.
</div>

<div class="row justify-content-center" style="width: 80%; margin: 0 auto;">
        {% include video.liquid path="https://drive.google.com/file/d/1av83pP9L-Fncdzo6P8c_H_YUpHi7n1Aj/preview?embedded=true" class="img-fluid rounded z-depth-1" controls=true autoplay=false %}
        {% include video.liquid path="https://drive.google.com/file/d/1N_Sea-M7rhEHcjo70N8pOEmj9biPUR0d/preview?embedded=true" class="img-fluid rounded z-depth-1" controls=true autoplay=false %}
</div>


<div class="caption">
    SpotNLP can recognize gestures to start and stop following. The controller can make a T pose to start following or use a stop gesture to pause. Three further gestures adjust the following distance: close, medium, and far. MediaPipe pose estimates are combined into a history vector and passed to an MLP gesture classifier.
</div>




<!-- https://docs.google.com/presentation/d/1ZNhnRRa5fr2BqYxXX8ax2uWAo9YG3EmxY5pKJuxG-Ic/edit?usp=sharing -->


## Natural Language Interface

<!-- https://www.youtube.com/watch?v=90_ityN9vLs -->
<div class="row justify-content-center" style="width: 80%; margin: 0 auto;">
    <div class="col-sm-6 mt-3 mt-md-0">
        {% include video.liquid path="https://www.youtube.com/embed/90_ityN9vLs" class="img-fluid rounded z-depth-1" controls=true %}
    </div>
</div>

<div class="caption">
    SpotNLP enables natural-language commands for longer task sequences. In this demo, the user asks Spot to follow them, save semantic keypoints with contextual information, and navigate back to those keypoints. The user can also ask about the environment and refer to previous locations using the semantic map.

    Future work includes pointing gestures for more precise references to keypoints and manipulation with Spot's arm.
</div>

<div class="row justify-content-center" style="width: 80%; margin: 0 auto;">
    <div class="col mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/Spot/no.gif" title="SpotNLP System Diagram" class="img-fluid rounded z-depth-1" avoid_scaling=true %}
    </div>
    <div class="col mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/Spot/question.gif" title="SpotNLP System Diagram" class="img-fluid rounded z-depth-1" avoid_scaling=true %}
    </div>
    <div class="col mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/Spot/rotate.gif" title="SpotNLP System Diagram" class="img-fluid rounded z-depth-1" avoid_scaling=true %}
    </div>
    <div class="col mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/Spot/up.gif" title="SpotNLP System Diagram" class="img-fluid rounded z-depth-1" avoid_scaling=true %}
    </div>
</div>

The videos above are recorded demonstrations of the SpotNLP system. They show specific behaviors in their recorded settings, not a general reliability or safety evaluation.

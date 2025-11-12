---
layout: page
title: SpotNLP
description: A Natural Language Interface for Boston Dynamics Spot
img: assets/img/Spot/demo.webp
importance: 3
category: work
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
    SpotNLP in action: Spot Following natural language commands for a Demo for DoD representatives. Spot is instructed to follow the controller, save semantic keypoints, and navigate given contextual information about the environment.
</div>

<div class="caption">
    Spot follows humans using segmentation models. XMem is used to propigate the original segmentation mask throughout time, leading Spot to be robust to distractions in crowded environments and occlusions. Spot also recognizes simple gestures to start and stop following.
</div>

<div class="row justify-content-center" style="width: 80%; margin: 0 auto;">
    <div class="col-sm-6 mt-3 mt-md-0">
        {% include video.liquid path="https://drive.google.com/file/d/1DzkEhDpsXLYuy0WCevADSRJa6uH253XG/preview?embedded=true" class="img-fluid rounded z-depth-1" controls=true autoplay=false %}
    </div>
</div>


<div class="caption">
    MediaPipe creates a segmentation mask of the first human to make a T pose. XMem is used to propagate the original segmentation mask throughout time, leading Spot to be robust to distractions in crowded environments and occlusions. Even with multiple humans in the scene, Spot can follow the controller, even after they are completely occluded.
</div>

<div class="row justify-content-center" style="width: 80%; margin: 0 auto;">
        {% include video.liquid path="https://drive.google.com/file/d/1av83pP9L-Fncdzo6P8c_H_YUpHi7n1Aj/preview?embedded=true" class="img-fluid rounded z-depth-1" controls=true autoplay=false %}
        {% include video.liquid path="https://drive.google.com/file/d/1N_Sea-M7rhEHcjo70N8pOEmj9biPUR0d/preview?embedded=true" class="img-fluid rounded z-depth-1" controls=true autoplay=false %}
</div>


<div class="caption">
    SpotNLP can also recognize simple gestures to start and stop following. The controller can make a T pose to start following, and use a "stop" gesture to start or stop following. The robot also allows the user to change the following distance by using one of three gestures: "close", "medium", and "far". SpotNLP uses MediaPipe to detect the poses, that are combined into a history vecotr, passed to a MLP model trained to detect actions. By using MediaPipe, no additional training is required to pair with new users, so the robot can be used by anyone without additional setup.
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
    SpotNLP enables natural language commands for long-horizon tasks. In this demo, the user conversatonally instructs Spot to follow them, save semantic keypoints with contextual information about the environment, and navigate to those keypoints later. The user can also ask Spot questions about the environment, and implicitly reference previous keypoints using context from the semantic map. 

    Future work includes detection of pointing gestures to enable more precise referencing of keypoints, and integration of manipulation capabilities using Spot's arm. The more capabilites we can give Spot, the more useful the natrual language interface becomes.
</div>

<div class="row justify-content-center" style="width: 80%; margin: 0 auto;">
    <div class="col mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/Spot/no.gif" title="SpotNLP System Diagram" class="img-fluid rounded z-depth-1" %}
    </div>
    <div class="col mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/Spot/question.gif" title="SpotNLP System Diagram" class="img-fluid rounded z-depth-1" %}
    </div>
    <div class="col mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/Spot/rotate.gif" title="SpotNLP System Diagram" class="img-fluid rounded z-depth-1" %}
    </div>
    <div class="col mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/Spot/up.gif" title="SpotNLP System Diagram" class="img-fluid rounded z-depth-1" %}
    </div>
</div>

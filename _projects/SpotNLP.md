---
layout: page
title: SpotNLP
description: A Natural Language Interface for Boston Dynamics Spot
img:
importance: 3
category: work
---

## GitHub Repository
<div class="repositories d-flex flex-wrap flex-md-row flex-column justify-content-between align-items-center">
  {% include repository/repo.liquid repository='RPM-lab-UMN/SpotNLP' %}
</div>

# Overview
This project involves developing a natural language interface for the Boston Dynamics Spot robot, enabling users to command the robot using everyday language. By integrating large language models (LLMs) and gesture detection with Spot's control systems, we aim to facilitate intuitive interactions and enhance the robot's usability in various environments.


## Human Following / Gesture Recognition
<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include video.liquid path="https://drive.google.com/file/d/1gJQImMGEnGH4fOe8TpPvDU1NuAJ4rH7D/preview" class="img-fluid rounded z-depth-1" controls=true autoplay=true %}
    </div>
</div>

<div class="caption">
    SpotNLP in action: Spot Following natural language commands for a Demo for DoD representatives. Spot is instructed to follow the controller, save semantic keypoints, and navigate given contextual information about the environment.
</div>

<div class="caption">
    Spot follows humans using segmentation models. XMem is used to propigate the original segmentation mask throughout time, leading Spot to be robust to distractions in crowded environments and occlusions. Spot also recognizes simple gestures to start and stop following.
</div>

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include video.liquid path="https://drive.google.com/file/d/1av83pP9L-Fncdzo6P8c_H_YUpHi7n1Aj/preview" class="img-fluid rounded z-depth-1" controls=true autoplay=true %}
    </div>
</div>

<div class="caption">
    MediaPipe creates a segmentation mask of the first human to make a T pose. XMem is used to propagate the original segmentation mask throughout time, leading Spot to be robust to distractions in crowded environments and occlusions. Even with multiple humans in the scene, Spot can follow the controller, even after they are completely occluded.

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include video.liquid path="https://drive.google.com/file/d/1N_Sea-M7rhEHcjo70N8pOEmj9biPUR0d/preview" class="img-fluid rounded z-depth-1" controls=true autoplay=true %}
    </div>
</div>

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include video.liquid path="https://drive.google.com/file/d/1DzkEhDpsXLYuy0WCevADSRJa6uH253XG/preview" class="img-fluid rounded z-depth-1" controls=true autoplay=true %}
    </div>
</div>

<div class="caption">
    SpotNLP can also recognize simple gestures to start and stop following. The controller can make a T pose to start following, and use a "stop" gesture to start or stop following. The robot also allows the user to change the following distance by using one of three gestures: "close", "medium", and "far". SpotNLP uses MediaPipe to detect the poses, that are combined into a history vecotr, passed to a MLP model trained to detect actions. By using MediaPipe, no additional training is required to pair with new users, so the robot can be used by anyone without additional setup.
</div>




<!-- https://docs.google.com/presentation/d/1ZNhnRRa5fr2BqYxXX8ax2uWAo9YG3EmxY5pKJuxG-Ic/edit?usp=sharing -->

## Natrual Language Interface
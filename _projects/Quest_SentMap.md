---
layout: page
title: Quest 3 SentMap / World Mapper
description: A mixed-reality room mapper with measured geometry and progressive object reconstruction from Quest observations.
img: assets/img/projects/quest-sentmap-objects.png
icon: fa-solid fa-vr-cardboard
importance: 4
category: Systems
---

## Mapping as you move

SentMap is a Quest 3 mixed-reality prototype that builds a measured room mesh from headset observations and adds object reconstructions as processing finishes. The Unity/OpenXR client renders passthrough, the measured mesh, object outlines, and reconstructed models. Capture, mapping, segmentation, reconstruction, and rendering run asynchronously so a slow object model does not stop the room view.

A recorded Quest session automatically produced three distinct object models—a monitor, keyboard, and papers—in 47.7 seconds. The later offline pipeline also supports reviewed semantic labels and an editable desktop viewer. The installed headset build has been checked with recorded-data replay and controller interaction.

The **five-minute live walkthrough, map alignment and latency checks remain open**. The preview below is from recorded headset captures processed offline; it is not proof of a complete live room scan.

{% include figure.liquid path="assets/img/projects/quest-sentmap-objects.png" alt="Three object reconstructions from recorded Quest headset observations" class="img-fluid rounded z-depth-1" caption="Offline preview of three reconstructed objects from a recorded Quest session. Measured-fit acceptance is shown per object; live walkthrough acceptance is pending." %}

The project connects spatial mapping with my interest in interfaces that let researchers inspect what a robot or headset measured, where the reconstruction is uncertain, and which objects still need review.

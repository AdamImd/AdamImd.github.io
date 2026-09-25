---
layout: page
title: MagPie Tactile Skin
description: A modular magnetic and piezoresistive skin, developed with Breck School students and accepted for an IROS 2026 workshop oral presentation.
img: assets/img/projects/magpie-taxel-prototype.jpg
icon: fa-solid fa-wave-square
importance: 2
category: Research
---

## Two sensing signals in one module

MagPie combines piezoresistive and Hall-effect sensing in a compliant triangular taxel. Its modular housing is designed to let multiple taxels form a larger tactile surface. The workshop paper reports the electronic architecture, force-response measurements, and an eight-taxel latency study.

I developed this project with **Jackson Goodrich and Eytan Krebs**, high school students at Breck School, and **Karthik Desingh**. Jackson and Eytan contributed equally to the paper. It was accepted for an oral presentation at the [IROS 2026 Scalable Tactile Sensing for Dexterous Manipulation workshop](https://tactile-dexterity-iros.github.io/).

[Read the accepted workshop submission](https://openreview.net/forum?id=dnU9RnbNk0).

This is a sensor research prototype. The workshop result does not establish full-body robot deployment or general-purpose tactile manipulation.

## Prototype and measurements

{% include figure.liquid path="assets/img/projects/magpie-taxel-prototype.jpg" alt="Photograph of an assembled triangular MagPie tactile taxel with its four-wire bus" class="img-fluid rounded z-depth-1" caption="Assembled MagPie taxel from the IROS 2026 workshop poster. This is a sensor prototype, not a robot-wide deployed skin." %}

{% include figure.liquid path="assets/img/projects/magpie-force-response.png" alt="Measured raw ADC counts versus applied force for the piezoresistive and Hall-effect channels" class="img-fluid rounded z-depth-1" caption="One taxel under two load–unload cycles. The piezoresistive channel approaches its ADC ceiling earlier; the Hall-effect channel responds over a wider tested force range. These are raw counts, not a calibrated force estimate." %}

{% include figure.liquid path="assets/img/projects/magpie-bus-latency.png" alt="Measured response latencies across eight MagPie taxels" class="img-fluid rounded z-depth-1" caption="Poster latency measurements from ten trials on each of eight taxels. The tested bus showed roughly 5–12 ms command-to-response latency without a clear position-dependent increase; this does not establish larger-network performance." %}

## Sensor design views

{% include figure.liquid path="assets/img/projects/magpie-robot.jpg" alt="CAD rendering of modular MagPie skin on a robot arm" class="img-fluid rounded z-depth-1" caption="Manuscript CAD illustration of modular MagPie taxels on a robot arm; it is a design visualization, not a deployed skin." %}

{% include figure.liquid path="assets/img/projects/magpie-taxel.jpg" alt="Exploded CAD view of a triangular MagPie taxel" class="img-fluid rounded z-depth-1" caption="Exploded CAD view of the 44 mm triangular taxel, showing the layered piezoresistive and magnetic-sensing design." %}

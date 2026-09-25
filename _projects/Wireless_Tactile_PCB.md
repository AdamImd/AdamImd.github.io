---
layout: page
title: Wireless Tactile Matrix Electronics
description: A compact ESP32-S3 sensing board and raw-count readout for modular robot skins.
img: assets/img/projects/wireless-tactile-matrix.svg
icon: fa-solid fa-microchip
importance: 8
category: Research
---

## A compact readout for sensing skins

The Revision F electronics combine a XIAO ESP32-S3 Plus carrier with a 5 × 6 tactile matrix interface, designed for a modular skin on robot links. The board design includes scanning electronics, USB power, and a Bluetooth Low Energy data path. The interface is laid out so a larger 10 × 10 configuration can be studied later; that expansion is not a validated sensor.

I also studied how shared row resistance can distort a scanned matrix. An additional row-impedance measurement gives an inverse correction under a **static, calibrated circuit model**; the current evidence is analytic and synthetic. Raw ADC values should not be read as calibrated force, pressure, or capacitance maps.

An assembly guide and electrical checks are prepared for the Revision F boards. The related [Lite6 full-surface A2 skin design](https://app.notion.com/p/3e4c5a4440b781268afff78bf283701e) places one 5 × 6 matrix on each of two robot links. Its CAD, coverage, and printable-part checks are complete, while physical fit, motion clearance, and sensor response still require testing.

This board is a step toward distributed tactile readout, with hardware characterization and calibration still to be done.

{% include figure.liquid path="assets/img/projects/wireless-tactile-matrix.svg" alt="Explanatory schematic of five row electrodes, six column electrodes, and an ESP32-S3 readout" class="img-fluid rounded z-depth-1" caption="Explanatory matrix topology. This is not the manufactured PCB layout or a measured tactile map." %}

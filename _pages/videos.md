---
layout: page
title: Videos
permalink: /videos/
description: Tactile sensing, manipulation, and robot learning in motion.
nav: true
nav_order: 3.5
---

Selected demonstrations from my research and collaborations. Each recording links to a project page with methods, publications, and evaluation details.

[Browse quick GIF previews]({% link _pages/gifs.md %}).

<nav class="video-showcase-nav" aria-label="Video categories">
{% for section in site.data.video_showcase %}
  <a href="#{{ section.id }}">{{ section.title }}</a>
{% endfor %}
</nav>

{% for section in site.data.video_showcase %}
<section class="video-showcase-section" id="{{ section.id }}" aria-labelledby="{{ section.id }}-heading">
  <h2 id="{{ section.id }}-heading">{{ section.title }}</h2>
  <p>{{ section.description }}</p>
  <div class="video-showcase-grid{% if section.portrait %} video-showcase-grid--portrait{% endif %}">
  {% for video in section.videos %}
    {% include showcase-video.liquid video=video %}
  {% endfor %}
  </div>
</section>
{% endfor %}

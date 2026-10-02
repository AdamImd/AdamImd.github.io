---
layout: page
title: GIFs
permalink: /projects/gifs/
description: Short loops of tactile sensing, manipulation, and robot learning.
nav: false
gif_showcase: true
nav_section: Projects
project_view: gifs
---

{% include project-nav.liquid %}


Quick previews of my research and collaborations. The sensing-skin loops keep the physical footage and sensor readouts together. Each preview links to its project and full recording.

<div class="gif-showcase-toolbar">
  <button type="button" id="gif-motion-toggle" class="gif-showcase-button" aria-pressed="false" hidden>Play animations</button>
  <span>Short loops · HD where the source supports it · GIF downloads</span>
</div>

<nav class="video-showcase-nav" aria-label="GIF categories">
{% for section in site.data.video_showcase %}
  <a href="#{{ section.id }}">{{ section.title }}</a>
{% endfor %}
</nav>

{% for section in site.data.video_showcase %}
<section class="video-showcase-section" id="{{ section.id }}" aria-labelledby="{{ section.id }}-heading">
  <h2 id="{{ section.id }}-heading">{{ section.title }}</h2>
  <div class="video-showcase-grid{% if section.portrait %} video-showcase-grid--portrait{% endif %}">
  {% for video in section.videos %}
    {% assign gif = site.data.gif_showcase[video.id] %}
    {% if gif %}
      {% include showcase-gif.liquid video=video gif=gif %}
    {% endif %}
  {% endfor %}
  </div>
</section>
{% endfor %}

The page uses smaller animated images where supported, with real GIF files available for every preview. Animations load as you reach them; reduced-motion preferences start the page paused. Full-length recordings remain on the [Videos page]({% link _pages/videos.md %}).

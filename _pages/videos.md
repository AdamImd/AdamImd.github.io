---
layout: page
title: Videos
permalink: /videos/
description: Tactile sensing, manipulation, and robot learning in motion.
nav: true
nav_order: 3.5
_styles: |
  .video-showcase-nav { display: flex; flex-wrap: wrap; gap: .65rem; margin: 1.5rem 0 2.5rem; }
  .video-showcase-nav a { padding: .5rem .9rem; border: 1px solid var(--global-divider-color); border-radius: 2rem; color: var(--global-text-color); }
  .video-showcase-nav a:hover { border-color: var(--global-theme-color); color: var(--global-theme-color); }
  .video-showcase-section { margin-bottom: 3rem; scroll-margin-top: 6rem; }
  .video-showcase-section > p { max-width: 46rem; margin-bottom: 1.4rem; }
  .video-showcase-grid { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 1.5rem; }
  .video-showcase-card { display: flex; flex-direction: column; min-width: 0; overflow: hidden; border: 1px solid var(--global-divider-color); border-radius: .75rem; background: var(--global-card-bg-color); scroll-margin-top: 6rem; }
  .video-showcase-player { aspect-ratio: 16 / 9; background: #111; }
  .video-showcase-player video, .video-showcase-player iframe { display: block; width: 100%; height: 100%; object-fit: contain; border: 0; }
  .video-showcase-body { display: flex; flex: 1; flex-direction: column; padding: 1.15rem; }
  .video-showcase-kind { align-self: flex-start; margin-bottom: .7rem; padding: .2rem .55rem; border: 1px solid var(--global-divider-color); border-radius: .35rem; font-size: .75rem; font-weight: 600; }
  .video-showcase-body h3 { margin: 0 0 .7rem; font-size: 1.2rem; line-height: 1.35; }
  .video-showcase-body p { font-size: .95rem; line-height: 1.6; }
  .video-showcase-links { display: flex; flex-wrap: wrap; gap: .6rem 1rem; margin-top: auto; padding-top: .4rem; font-size: .9rem; }
  .video-showcase-nav a:focus-visible, .video-showcase-links a:focus-visible { outline: 2px solid var(--global-theme-color); outline-offset: 4px; }
  @media (max-width: 640px) { .video-showcase-grid { grid-template-columns: 1fr; } }
---

Selected demonstrations from my research and collaborations. Each recording links to a project page with methods, publications, and evaluation details.

<nav class="video-showcase-nav" aria-label="Video categories">
{% for section in site.data.video_showcase %}
  <a href="#{{ section.id }}">{{ section.title }}</a>
{% endfor %}
</nav>

{% for section in site.data.video_showcase %}
<section class="video-showcase-section" id="{{ section.id }}" aria-labelledby="{{ section.id }}-heading">
  <h2 id="{{ section.id }}-heading">{{ section.title }}</h2>
  <p>{{ section.description }}</p>
  <div class="video-showcase-grid">
  {% for video in section.videos %}
    {% include showcase-video.liquid video=video %}
  {% endfor %}
  </div>
</section>
{% endfor %}

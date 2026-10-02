---
layout: page
title: Projects
permalink: /projects/
description: Tactile sensing, robot learning, and tools for working with robots.
nav: true
nav_order: 3
project_view: overview
project_filter: true
display_categories: [Research, Systems]
---

{% include project-nav.liquid %}

I build sensors and systems that help robots understand contact and use it during manipulation. Browse the research below, watch a demonstration, or explore the public code. Project pages describe the methods, results, and current stage of each effort.

<div class="project-filter" hidden>
  <label for="project-search">Find a project</label>
  <div class="project-filter-row">
    <input id="project-search" type="search" placeholder="Try tactile, learning, or Spot" autocomplete="off" aria-describedby="project-results">
    <button type="button" id="project-search-clear" hidden>Clear</button>
    <span id="project-results" role="status" aria-live="polite">{{ site.projects.size }} projects</span>
  </div>
</div>
<p id="project-empty" hidden>No matching projects. Try another phrase.</p>

<div class="projects">
{% for category in page.display_categories %}
  {% assign categorized_projects = site.projects | where: "category", category | sort: "importance" %}
  <section class="project-group" data-project-group aria-labelledby="{{ category | downcase }}-heading">
    <div class="project-group-heading">
      <h2 id="{{ category | downcase }}-heading">{% if category == 'Systems' %}Systems & interfaces{% else %}{{ category }}{% endif %}</h2>
      <span>{% if category == 'Research' %}Sensors, contact, and learning{% else %}Teleoperation, spatial computing, and coordination{% endif %}</span>
    </div>
    <div class="project-grid">
    {% for project in categorized_projects %}
      {% include projects.liquid %}
    {% endfor %}
    </div>
  </section>
{% endfor %}
</div>

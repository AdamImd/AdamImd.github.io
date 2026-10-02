---
layout: page
permalink: /projects/code/
title: Code
description: Public repositories for research and robot interfaces.
nav: false
nav_section: Projects
project_view: code
---

{% include project-nav.liquid %}

Source code, simulation environments, and project materials from my work and collaborations. Each repository documents its own setup and scope. More of my public work is on [GitHub](https://github.com/AdamImd).

<div class="code-grid">
{% for repo in site.data.public_code %}
  <article class="code-card">
    <h2><a href="https://github.com/{{ repo.repository }}">{{ repo.title }} <span aria-hidden="true">↗</span></a></h2>
    <p>{{ repo.description }}</p>
    <small>{{ repo.repository }}</small>
  </article>
{% endfor %}
</div>

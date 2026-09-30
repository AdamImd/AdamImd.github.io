/* Animate only visible image previews; restore stills for pause/reduced motion. */
(() => {
  const toggle = document.getElementById("gif-motion-toggle");
  if (!toggle) return;
  const preference = window.matchMedia("(prefers-reduced-motion: reduce)");
  let enabled = !preference.matches;
  const cards = Array.from(document.querySelectorAll(".gif-showcase-card"), (element) => ({
    element,
    image: element.querySelector("img[data-gif]"),
    source: element.querySelector("source[data-srcset]"),
    button: element.querySelector(".gif-card-toggle"),
    visible: false,
    paused: false,
    playing: false,
  }));
  const update = (card) => {
    const playing = enabled && card.visible && !card.paused && !document.hidden;
    if (playing !== card.playing) {
      if (playing) {
        card.source.srcset = card.source.dataset.srcset;
        card.image.src = card.image.dataset.gif;
      } else {
        card.source.removeAttribute("srcset");
        card.image.src = card.image.dataset.poster;
      }
      card.playing = playing;
    }
    card.button.textContent = playing ? "Pause preview" : "Play preview";
    card.button.setAttribute("aria-pressed", String(playing));
  };
  const updateAll = () => {
    toggle.textContent = enabled ? "Pause animations" : "Play animations";
    toggle.setAttribute("aria-pressed", String(enabled));
    cards.forEach(update);
  };
  toggle.hidden = false;
  toggle.addEventListener("click", () => {
    enabled = !enabled;
    if (enabled) cards.forEach((card) => { card.paused = false; });
    updateAll();
  });
  cards.forEach((card) => {
    card.button.hidden = false;
    card.button.addEventListener("click", () => {
      if (!enabled) {
        enabled = true;
        cards.forEach((other) => { other.paused = other !== card; });
        card.paused = false;
      } else {
        card.paused = !card.paused;
      }
      updateAll();
    });
  });
  if ("IntersectionObserver" in window) {
    const byElement = new Map(cards.map((card) => [card.element, card]));
    const observer = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        const card = byElement.get(entry.target);
        card.visible = entry.isIntersecting;
        update(card);
      });
    }, { rootMargin: "0px", threshold: 0.05 });
    cards.forEach((card) => observer.observe(card.element));
  } else {
    // Older browsers stay still until the visitor explicitly plays a preview.
    enabled = false;
    cards.forEach((card) => { card.visible = true; });
  }
  preference.addEventListener("change", () => {
    enabled = !preference.matches;
    updateAll();
  });
  document.addEventListener("visibilitychange", updateAll);
  updateAll();
})();

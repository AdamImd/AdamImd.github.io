/* Keep the full project collection available when JavaScript is disabled. */
(() => {
  const input = document.getElementById("project-search");
  if (!input) return;
  const cards = Array.from(document.querySelectorAll("[data-project-card]"), (element) => ({
    element,
    text: element.textContent.toLocaleLowerCase(),
  }));
  const groups = Array.from(document.querySelectorAll("[data-project-group]"));
  const results = document.getElementById("project-results");
  const clear = document.getElementById("project-search-clear");
  const empty = document.getElementById("project-empty");
  const update = () => {
    const words = input.value.trim().toLocaleLowerCase().split(/\s+/).filter(Boolean);
    let count = 0;
    cards.forEach(({ element, text }) => {
      element.hidden = !words.every((word) => text.includes(word));
      if (!element.hidden) count++;
    });
    groups.forEach((group) => { group.hidden = !Array.from(group.querySelectorAll("[data-project-card]")).some((card) => !card.hidden); });
    results.textContent = `${count} ${count === 1 ? "project" : "projects"}`;
    empty.hidden = count > 0;
    clear.hidden = words.length === 0;
  };
  input.closest(".project-filter").hidden = false;
  input.addEventListener("input", update);
  input.addEventListener("keydown", (event) => {
    if (event.key === "Escape") { input.value = ""; update(); }
  });
  clear.addEventListener("click", () => { input.value = ""; update(); input.focus(); });
  update();
})();

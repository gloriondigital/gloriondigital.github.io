(function () {
  // Capture the Turkish defaults straight from the page so TR text lives only in index.html.
  const TR = {};
  document.querySelectorAll("[data-i18n]").forEach(el => { TR[el.dataset.i18n] = el.textContent; });
  document.querySelectorAll("[data-i18n-html]").forEach(el => { TR[el.dataset.i18nHtml] = el.innerHTML; });
  const dict = { tr: TR, en: EN };

  function setLang(lang) {
    if (!dict[lang]) lang = "tr";
    const d = dict[lang];
    document.querySelectorAll("[data-i18n]").forEach(el => {
      const v = d[el.dataset.i18n]; if (v != null) el.textContent = v;
    });
    document.querySelectorAll("[data-i18n-html]").forEach(el => {
      const v = d[el.dataset.i18nHtml]; if (v != null) el.innerHTML = v;
    });
    document.documentElement.lang = lang;
    document.title = META[lang].title;
    const md = document.querySelector('meta[name="description"]');
    if (md) md.setAttribute("content", META[lang].desc);
    document.querySelectorAll("[data-lang]").forEach(b =>
      b.setAttribute("aria-pressed", String(b.dataset.lang === lang)));
    try { localStorage.setItem("gd-lang", lang); } catch (e) {}
    const url = new URL(location.href);
    if (lang === "en") url.searchParams.set("lang", "en"); else url.searchParams.delete("lang");
    history.replaceState(null, "", url);
  }

  document.querySelectorAll("[data-lang]").forEach(b =>
    b.addEventListener("click", () => setLang(b.dataset.lang)));

  // Priority: ?lang= in URL → visitor's saved choice → Turkish
  let initial = new URLSearchParams(location.search).get("lang");
  if (!initial) { try { initial = localStorage.getItem("gd-lang"); } catch (e) {} }
  if (!initial) initial = "tr";
  setLang(initial);

  // Mobile menu
  const burger = document.getElementById("burger");
  const menu = document.getElementById("menu");
  burger.addEventListener("click", () => {
    const open = menu.classList.toggle("open");
    burger.setAttribute("aria-expanded", String(open));
  });
  menu.querySelectorAll("a").forEach(a => a.addEventListener("click", () => {
    menu.classList.remove("open"); burger.setAttribute("aria-expanded", "false");
  }));

  document.getElementById("year").textContent = new Date().getFullYear();
})();

(function () {
  const WA_NUMBER = (typeof WHATSAPP_NUMBER !== "undefined" && WHATSAPP_NUMBER) || "905434945528";
  const ENDPOINT = (typeof FORM_ENDPOINT !== "undefined" && FORM_ENDPOINT) || "";
  const esc = s => String(s).replace(/[&<>"']/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));

  // ---------- Blog cards on the homepage (both languages rendered; CSS shows the active one) ----------
  const both = (tr, en) => `<span class="lang-tr">${esc(tr)}</span><span class="lang-en">${esc(en)}</span>`;
  if (typeof POSTS !== "undefined") {
    document.querySelectorAll(".post-grid[data-posts]").forEach(grid => {
      const limit = Number(grid.dataset.posts) || POSTS.length;
      grid.innerHTML = POSTS.slice(0, limit).map(p => ["tr", "en"].map(l => `
        <a class="post-card lang-${l}" href="${p[l].url}">
          <span class="post-tag">${esc(p[l].tag)}</span>
          <h3>${esc(p[l].title)}</h3>
          <p>${esc(p[l].excerpt)}</p>
          <span class="post-foot">${esc(p[l].date)} · ${p.minutes} ${l === "tr" ? "dk okuma" : "min read"}</span>
        </a>`).join("")).join("");
    });
  }

  // ---------- Language ----------
  const TR = {};
  document.querySelectorAll("[data-i18n]").forEach(el => { if (!(el.dataset.i18n in TR)) TR[el.dataset.i18n] = el.textContent; });
  document.querySelectorAll("[data-i18n-html]").forEach(el => { TR[el.dataset.i18nHtml] = el.innerHTML; });
  Object.assign(TR, {
    "form.sending": "Gönderiliyor…",
    "form.ok": "Teşekkürler! Başvurunuz alındı, en kısa sürede size dönüyoruz.",
    "form.wa": "Başvurunuzu göndermeniz için WhatsApp açılıyor…",
    "form.err": "Lütfen ad soyad, telefon ve onay kutusunu doldurun.",
    "form.fail": "Bir sorun oluştu. Lütfen WhatsApp'tan bize yazın."
  });
  const dict = { tr: TR, en: (typeof EN !== "undefined" ? EN : {}) };
  let current = "tr";
  const t = key => (dict[current] && dict[current][key]) || TR[key] || key;

  const STATIC = document.documentElement.dataset.static === "1";

  function setLang(lang) {
    if (!dict[lang]) lang = "tr";
    current = lang;
    const d = dict[lang];
    document.querySelectorAll("[data-i18n]").forEach(el => {
      const v = d[el.dataset.i18n]; if (v != null) el.textContent = v;
    });
    document.querySelectorAll("[data-i18n-html]").forEach(el => {
      const v = d[el.dataset.i18nHtml]; if (v != null) el.innerHTML = v;
    });
    document.documentElement.lang = lang;
    document.querySelectorAll("[data-href-" + lang + "]").forEach(a => { a.href = a.getAttribute("data-href-" + lang); });
    if (typeof META !== "undefined") {
      document.title = META[lang].title;
      const md = document.querySelector('meta[name="description"]');
      if (md) md.setAttribute("content", META[lang].desc);
    }
    document.querySelectorAll("[data-lang]").forEach(b =>
      b.setAttribute("aria-pressed", String(b.dataset.lang === lang)));
    try { localStorage.setItem("gd-lang", lang); } catch (e) {}
    const url = new URL(location.href);
    if (lang === "en") url.searchParams.set("lang", "en"); else url.searchParams.delete("lang");
    history.replaceState(null, "", url);
  }

  document.querySelectorAll("[data-lang]").forEach(b =>
    b.addEventListener("click", () => setLang(b.dataset.lang)));

  if (STATIC) {
    // Blog pages have a fixed language per URL; the TR/EN links go to the other version.
    current = document.documentElement.lang || "tr";
    document.querySelectorAll("[data-lang-link]").forEach(a => a.addEventListener("click", () => {
      try { localStorage.setItem("gd-lang", a.dataset.langLink); } catch (e) {}
    }));
  } else {
    // Priority: ?lang= in URL → visitor's saved choice → Turkish
    let initial = new URLSearchParams(location.search).get("lang");
    if (!initial) { try { initial = localStorage.getItem("gd-lang"); } catch (e) {} }
    setLang(initial || "tr");
  }

  // ---------- Mobile menu ----------
  const burger = document.getElementById("burger");
  const menu = document.getElementById("menu");
  if (burger && menu) {
    burger.addEventListener("click", () => {
      const open = menu.classList.toggle("open");
      burger.setAttribute("aria-expanded", String(open));
    });
    menu.querySelectorAll("a").forEach(a => a.addEventListener("click", () => {
      menu.classList.remove("open"); burger.setAttribute("aria-expanded", "false");
    }));
  }

  const year = document.getElementById("year");
  if (year) year.textContent = new Date().getFullYear();

  // ---------- Scroll effects ----------
  const reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  const nav = document.querySelector(".nav");
  const onScroll = () => nav && nav.classList.toggle("scrolled", window.scrollY > 10);
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  if (!reduce && "IntersectionObserver" in window) {
    const targets = document.querySelectorAll(
      ".section h2, .section .eyebrow, .card, .steps li, .chip, .compare .col, details, .post-card, .lead-form, .contact-item, .post-cta, .training > div:first-child"
    );
    targets.forEach((el, i) => {
      el.classList.add("reveal");
      el.style.setProperty("--d", `${(i % 4) * 70}ms`);
    });
    const io = new IntersectionObserver(entries => {
      entries.forEach(e => { if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); } });
    }, { threshold: 0.12, rootMargin: "0px 0px -40px 0px" });
    targets.forEach(el => io.observe(el));

    // Count-up stats
    const counters = document.querySelectorAll("[data-count]");
    const cio = new IntersectionObserver(entries => {
      entries.forEach(e => {
        if (!e.isIntersecting) return;
        const el = e.target, end = Number(el.dataset.count), suf = el.dataset.suffix || "";
        const start = performance.now(), dur = 1200;
        const step = now => {
          const p = Math.min(1, (now - start) / dur);
          el.textContent = Math.round(end * (1 - Math.pow(1 - p, 3))) + suf;
          if (p < 1) requestAnimationFrame(step);
        };
        requestAnimationFrame(step);
        cio.unobserve(el);
      });
    }, { threshold: 0.6 });
    counters.forEach(el => cio.observe(el));
  }

  // Buttons that pre-select a service in the form
  document.querySelectorAll("[data-pick-service]").forEach(a => a.addEventListener("click", () => {
    const sel = document.querySelector('#leadForm select[name="service"]');
    if (sel) sel.value = a.dataset.pickService;
  }));

  // ---------- Lead form → Google Sheets (or WhatsApp fallback) ----------
  const form = document.getElementById("leadForm");
  if (form) {
    const status = document.getElementById("formStatus");
    const btn = form.querySelector('button[type="submit"]');
    const show = (msg, kind) => { status.textContent = msg; status.dataset.kind = kind || ""; };

    form.addEventListener("submit", async ev => {
      ev.preventDefault();
      const fd = new FormData(form);
      if (fd.get("website")) return; // spam trap
      const name = (fd.get("name") || "").trim();
      const phone = (fd.get("phone") || "").trim();
      if (!name || phone.replace(/\D/g, "").length < 10 || !form.consent.checked) {
        show(t("form.err"), "err"); return;
      }
      const data = {
        name, phone,
        business: (fd.get("business") || "").trim(),
        sector: fd.get("sector") || "",
        service: fd.get("service") || "",
        message: (fd.get("message") || "").trim(),
        language: current,
        page: location.pathname
      };

      if (!ENDPOINT) {
        const text = [
          "Merhaba, web sitenizden başvuru:",
          `Ad Soyad: ${data.name}`, `Telefon: ${data.phone}`,
          data.business && `İşletme: ${data.business}`,
          `Sektör: ${data.sector}`, `Hizmet: ${data.service}`,
          data.message && `Mesaj: ${data.message}`
        ].filter(Boolean).join("\n");
        show(t("form.wa"), "ok");
        window.open(`https://wa.me/${WA_NUMBER}?text=${encodeURIComponent(text)}`, "_blank", "noopener");
        return;
      }

      btn.disabled = true; show(t("form.sending"), "");
      try {
        // Apps Script web apps don't return CORS headers; no-cors still delivers the request.
        await fetch(ENDPOINT, { method: "POST", mode: "no-cors", body: new URLSearchParams(data) });
        form.reset();
        show(t("form.ok"), "ok");
      } catch (e) {
        show(t("form.fail"), "err");
      } finally {
        btn.disabled = false;
      }
    });
  }
})();

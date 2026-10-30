(function () {
  const WA_NUMBER = (typeof WHATSAPP_NUMBER !== "undefined" && WHATSAPP_NUMBER) || "905434945528";
  const ENDPOINT = (typeof FORM_ENDPOINT !== "undefined" && FORM_ENDPOINT) || "";
  // Analytics/pixel events via GTM dataLayer (no personal data is sent)
  const track = (event, params) => { window.dataLayer = window.dataLayer || []; window.dataLayer.push(Object.assign({ event }, params || {})); };
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
        const el = e.target, end = Number(el.dataset.count), suf = "";
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
    counters.forEach(el => { el.textContent = "0"; cio.observe(el); });
  }

  // ---------- WhatsApp button follows the scroll (spring) ----------
  const wa = document.querySelector(".wa-float");
  if (wa && !reduce) {
    let lastY = window.scrollY, offset = 0, vel = 0, raf = null, idle = null;
    const tick = () => {
      // spring back toward 0
      vel += -offset * 0.12;
      vel *= 0.78;
      offset += vel;
      wa.style.setProperty("--wy", offset.toFixed(2) + "px");
      wa.style.setProperty("--wr", (offset * -0.6).toFixed(2) + "deg");
      if (Math.abs(offset) > 0.1 || Math.abs(vel) > 0.1) raf = requestAnimationFrame(tick);
      else { wa.style.setProperty("--wy", "0px"); wa.style.setProperty("--wr", "0deg"); raf = null; }
    };
    window.addEventListener("scroll", () => {
      const y = window.scrollY, d = y - lastY; lastY = y;
      // scrolling down pushes the button up a little, scrolling up pulls it down
      offset = Math.max(-26, Math.min(26, offset - d * 0.35));
      wa.classList.remove("wa-nudge");
      if (!raf) raf = requestAnimationFrame(tick);
      clearTimeout(idle);
      idle = setTimeout(() => { void wa.offsetWidth; wa.classList.add("wa-nudge"); }, 220);
    }, { passive: true });
  }

  // ---------- Sample PDF behind a short form ----------
  const PDF_URL = "assets/canli-meta-reklam-egitimi-ornek.pdf";
  const PDF_NAME = "Glorion-Digital-Meta-Reklam-Egitimi-Ornek.pdf";
  const modal = document.getElementById("pdfModal");
  const downloadPdf = () => {
    const a = document.createElement("a");
    a.href = PDF_URL; a.download = PDF_NAME; document.body.appendChild(a); a.click(); a.remove();
  };
  if (modal) {
    const pf = document.getElementById("pdfForm");
    const st = pf.querySelector(".form-status");
    const msg = {
      tr: { err: "Lütfen ad soyad, telefon, geçerli bir e-posta ve onay kutusunu doldurun.", sending: "Gönderiliyor…",
            ok: "Teşekkürler! PDF iniyor.", wa: "Teşekkürler! PDF iniyor; bilgilerinizi iletmek için WhatsApp açılıyor." },
      en: { err: "Please fill in your name, phone, a valid email and the consent box.", sending: "Sending…",
            ok: "Thank you! Your PDF is downloading.", wa: "Thank you! Your PDF is downloading; WhatsApp is opening to send your details." }
    };
    const m = k => (msg[current] || msg.tr)[k];
    let unlocked = false;
    try { unlocked = localStorage.getItem("gd-pdf") === "1"; } catch (e) {}

    document.querySelectorAll("[data-pdf-gate]").forEach(btn => btn.addEventListener("click", ev => {
      ev.preventDefault();
      if (unlocked) { downloadPdf(); return; }   // already filled the form before
      st.textContent = ""; st.dataset.kind = "";
      if (typeof modal.showModal === "function") modal.showModal(); else modal.setAttribute("open", "");
      setTimeout(() => pf.name.focus(), 50);
    }));
    modal.querySelectorAll("[data-close]").forEach(b => b.addEventListener("click", () => modal.close()));
    modal.addEventListener("click", e => { if (e.target === modal) modal.close(); });

    pf.addEventListener("submit", async ev => {
      ev.preventDefault();
      const fd = new FormData(pf);
      if (fd.get("website")) return;
      const name = (fd.get("name") || "").trim(), phone = (fd.get("phone") || "").trim();
      const email = (fd.get("email") || "").trim();
      if (!name || phone.replace(/\D/g, "").length < 10 || !/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(email) || !pf.consent.checked) {
        st.textContent = m("err"); st.dataset.kind = "err"; return;
      }
      const data = { name, phone, email, business: (fd.get("business") || "").trim(), sector: "",
                     service: "Örnek PDF indirme", message: "Örnek eğitim PDF'ini indirdi", language: current, page: location.pathname };
      const btn = pf.querySelector('button[type="submit"]');
      btn.disabled = true; st.textContent = m("sending"); st.dataset.kind = "";
      if (ENDPOINT) {
        try { await fetch(ENDPOINT, { method: "POST", mode: "no-cors", body: new URLSearchParams(data) }); } catch (e) {}
        st.textContent = m("ok");
      } else {
        const text = ["Merhaba, web sitenizden örnek eğitim PDF'ini indirdim.", `Ad Soyad: ${name}`, `Telefon: ${phone}`, `E-posta: ${email}`,
                      data.business && `İşletme/Okul: ${data.business}`].filter(Boolean).join("\n");
        window.open(`https://wa.me/${WA_NUMBER}?text=${encodeURIComponent(text)}`, "_blank", "noopener");
        st.textContent = m("wa");
      }
      st.dataset.kind = "ok";
      track("lead_form_submit", { form_name: "ornek_pdf", service: "Örnek PDF indirme", sector: "" });
      unlocked = true;
      try { localStorage.setItem("gd-pdf", "1"); } catch (e) {}
      downloadPdf();
      btn.disabled = false;
      setTimeout(() => { modal.close(); pf.reset(); }, 2200);
    });
  }

  // ---------- Pointer effects (desktop, fine pointer, motion allowed) ----------
  const finePointer = window.matchMedia("(hover: hover) and (pointer: fine)").matches;

  // Reading progress bar (all devices)
  const bar = document.querySelector(".scroll-progress");
  if (bar) {
    const setBar = () => {
      const h = document.documentElement.scrollHeight - innerHeight;
      bar.style.transform = `scaleX(${h > 0 ? Math.min(1, scrollY / h) : 0})`;
    };
    addEventListener("scroll", setBar, { passive: true }); addEventListener("resize", setBar); setBar();
  }

  // Training seats fill one by one
  const seats = document.querySelector(".tc-seats");
  if (seats) {
    if (reduce || !("IntersectionObserver" in window)) seats.classList.add("filled");
    else new IntersectionObserver((en, o) => { if (en[0].isIntersecting) { seats.classList.add("filled"); o.disconnect(); } }, { threshold: .6 }).observe(seats);
  }

  if (finePointer && !reduce) {
    // Hero spotlight + parallax dots
    const hero = document.querySelector(".hero");
    const fx = hero && hero.querySelector(".hero-fx");
    if (fx) {
      let tx = .7, ty = .3, cx = tx, cy = ty, run = false;
      const loop = () => {
        cx += (tx - cx) * .08; cy += (ty - cy) * .08;
        fx.style.setProperty("--mx", (cx * 100).toFixed(2) + "%");
        fx.style.setProperty("--my", (cy * 100).toFixed(2) + "%");
        fx.style.setProperty("--px", ((cx - .5) * -24).toFixed(2) + "px");
        fx.style.setProperty("--py", ((cy - .5) * -24).toFixed(2) + "px");
        if (Math.abs(tx - cx) > .001 || Math.abs(ty - cy) > .001) requestAnimationFrame(loop); else run = false;
      };
      hero.addEventListener("pointermove", e => {
        const r = hero.getBoundingClientRect();
        tx = (e.clientX - r.left) / r.width; ty = (e.clientY - r.top) / r.height;
        if (!run) { run = true; requestAnimationFrame(loop); }
      });
      hero.addEventListener("pointerenter", () => fx.classList.add("on"));
      hero.addEventListener("pointerleave", () => fx.classList.remove("on"));
    }

    // 3D tilt + glare on cards
    document.querySelectorAll(".train-card, .card, .level, .post-card, .contact-item, .compare .col").forEach(el => {
      el.classList.add("tilt");
      let raf = null;
      el.addEventListener("pointermove", e => {
        const r = el.getBoundingClientRect();
        const x = (e.clientX - r.left) / r.width, y = (e.clientY - r.top) / r.height;
        const max = el.classList.contains("train-card") ? 6 : 8;
        cancelAnimationFrame(raf);
        raf = requestAnimationFrame(() => {
          el.style.setProperty("--rx", ((.5 - y) * max).toFixed(2) + "deg");
          el.style.setProperty("--ry", ((x - .5) * max).toFixed(2) + "deg");
          el.style.setProperty("--gx", (x * 100).toFixed(1) + "%");
          el.style.setProperty("--gy", (y * 100).toFixed(1) + "%");
        });
      });
      el.addEventListener("pointerenter", () => el.classList.add("tilting"));
      el.addEventListener("pointerleave", () => {
        el.classList.remove("tilting");
        el.style.setProperty("--rx", "0deg"); el.style.setProperty("--ry", "0deg");
      });
    });

    // Magnetic primary buttons
    document.querySelectorAll(".btn-gold:not(.btn-block), .btn-ghost:not(.btn-sm)").forEach(btn => {
      btn.classList.add("magnetic");
      btn.addEventListener("pointermove", e => {
        const r = btn.getBoundingClientRect();
        btn.style.setProperty("--bx", ((e.clientX - r.left - r.width / 2) * .25).toFixed(1) + "px");
        btn.style.setProperty("--by", ((e.clientY - r.top - r.height / 2) * .35).toFixed(1) + "px");
      });
      btn.addEventListener("pointerleave", () => { btn.style.setProperty("--bx", "0px"); btn.style.setProperty("--by", "0px"); });
    });
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
        track("lead_form_submit", { form_name: "on_gorusme", service: data.service, sector: data.sector });
        window.open(`https://wa.me/${WA_NUMBER}?text=${encodeURIComponent(text)}`, "_blank", "noopener");
        return;
      }

      btn.disabled = true; show(t("form.sending"), "");
      try {
        // Apps Script web apps don't return CORS headers; no-cors still delivers the request.
        await fetch(ENDPOINT, { method: "POST", mode: "no-cors", body: new URLSearchParams(data) });
        form.reset();
        show(t("form.ok"), "ok");
        track("lead_form_submit", { form_name: "on_gorusme", service: data.service, sector: data.sector });
      } catch (e) {
        show(t("form.fail"), "err");
      } finally {
        btn.disabled = false;
      }
    });
  }
})();

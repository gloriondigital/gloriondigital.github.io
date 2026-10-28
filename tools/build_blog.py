# -*- coding: utf-8 -*-
"""Builds the blog (TR + EN), blog/posts.js, sitemap.xml, robots.txt and llms.txt.

Run from anywhere:  python3 tools/build_blog.py
Content lives in tools/posts_data.py.
"""
import html, json, pathlib, re, shutil, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
from posts_data import POSTS  # noqa: E402

SITE = "https://gloriondigital.github.io"   # change here when the custom domain is connected
BRAND = "Glorion Digital"
WA = "https://wa.me/905434945528"
PHONE = "+905434945528"
EMAIL = "info.gloriondigital@gmail.com"
IG = "https://www.instagram.com/gloriondigital/"
LINKEDIN = "https://www.linkedin.com/in/yusuf-aslan-134075b1/"

POSTS.sort(key=lambda p: p["date"], reverse=True)
BY_KEY = {p["key"]: p for p in POSTS}

T = {
  "tr": dict(home="Ana sayfa", blog="Blog", services="Hizmetler", training="Canlı Eğitim", faq="SSS",
             cta="Ücretsiz Görüşme", read="dk okuma", short="Kısa cevap", faqh="Sık sorulan sorular",
             more="Bunları da okuyun", readmore="Yazıyı oku →", by="Yazan", team="Glorion Digital ekibi",
             updated="Güncellendi", ctaT="Reklam hesabınıza birlikte bakalım mı?",
             ctaP="İlk görüşme ücretsiz. WhatsApp'tan yazın, hesabınızı birlikte inceleyelim.",
             ctaB="WhatsApp'tan Yazın", trainT="Canlı Meta Reklam Eğitimi",
             trainP="10 kişilik sınıflarda, eğitmenle canlı ve kendi reklam hesabınız üzerinde.",
             trainB="Eğitimi İncele", listT="Meta reklamları üzerine pratik notlar",
             listP="Her gün gerçek reklam hesaplarında gördüklerimiz: reklamlar neden mesaj getirmez, bütçe nasıl doğru harcanır, önce neyi düzeltmek gerekir.",
             all="← Tüm yazılar", menu="Menü",
             months=["Ocak","Şubat","Mart","Nisan","Mayıs","Haziran","Temmuz","Ağustos","Eylül","Ekim","Kasım","Aralık"]),
  "en": dict(home="Home", blog="Blog", services="Services", training="Live Training", faq="FAQ",
             cta="Free Consultation", read="min read", short="Short answer", faqh="Frequently asked questions",
             more="Keep reading", readmore="Read post →", by="By", team="the Glorion Digital team",
             updated="Updated", ctaT="Want us to look at your ad account?",
             ctaP="The first consultation is free. Message us on WhatsApp and we'll review your account together.",
             ctaB="Message on WhatsApp", trainT="Live Meta Ads Training",
             trainP="Classes of 10, live with an instructor, on your own ad account.",
             trainB="See the training", listT="Practical notes on Meta ads",
             listP="What we see in real ad accounts every day: why ads don't bring messages, how to spend budget right, and what to fix first.",
             all="← All posts", menu="Menu",
             months=["January","February","March","April","May","June","July","August","September","October","November","December"]),
}

def home_url(lang):  return "/" if lang == "tr" else "/?lang=en"
def blog_url(lang):  return "/blog/" if lang == "tr" else "/en/blog/"
def post_url(p, lang): return f"{blog_url(lang)}{p[lang]['slug']}/"
def anchor(lang, sec): return ("/" if lang == "tr" else "/?lang=en") + "#" + sec
def fmt_date(iso, lang):
    y, m, d = map(int, iso.split("-")); mo = T[lang]["months"][m - 1]
    return f"{d} {mo} {y}" if lang == "tr" else f"{mo} {d}, {y}"
E = html.escape

def resolve_links(body, lang):
    def rep(m):
        target, text = m.group(1), m.group(2)
        if target == "services": href = anchor(lang, "hizmetler")
        elif target == "training": href = anchor(lang, "egitim")
        elif target == "contact": href = anchor(lang, "iletisim")
        elif target.startswith("post:"): href = post_url(BY_KEY[target[5:]], lang)
        else: raise ValueError(target)
        return f'<a class="kw" href="{href}">{text}</a>'
    return re.sub(r"\[\[([^|\]]+)\|([^\]]+)\]\]", rep, body)

ORG = {
  "@type": "ProfessionalService", "@id": f"{SITE}/#org", "name": BRAND,
  "url": f"{SITE}/", "logo": f"{SITE}/assets/icon-512.png", "image": f"{SITE}/assets/og-image.jpg",
  "telephone": PHONE, "email": EMAIL, "areaServed": "TR", "sameAs": [IG],
}

def head(lang, title, desc, canonical, alt_tr, alt_en, ld, og_type="website"):
    return f'''<!doctype html>
<html lang="{lang}" data-static="1">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{E(title)}</title>
<meta name="description" content="{E(desc)}">
<link rel="canonical" href="{SITE}{canonical}">
<link rel="alternate" hreflang="tr" href="{SITE}{alt_tr}">
<link rel="alternate" hreflang="en" href="{SITE}{alt_en}">
<link rel="alternate" hreflang="x-default" href="{SITE}{alt_tr}">
<meta name="robots" content="index,follow,max-image-preview:large">
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="{BRAND}">
<meta property="og:locale" content="{'tr_TR' if lang == 'tr' else 'en_US'}">
<meta property="og:title" content="{E(title)}">
<meta property="og:description" content="{E(desc)}">
<meta property="og:url" content="{SITE}{canonical}">
<meta property="og:image" content="{SITE}/assets/og-image.jpg">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" type="image/png" sizes="64x64" href="/assets/favicon-64.png">
<link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,700&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/styles.css">
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
</head>
<body>
'''

def header(lang, alt_tr, alt_en):
    t = T[lang]
    return f'''<header class="nav">
  <div class="wrap nav-inner">
    <a href="{home_url(lang)}" class="logo" aria-label="{BRAND}">
      <img class="logo-img" src="/assets/logo-mark.webp" alt="" width="40" height="61">
      <span class="logo-text">GLORION <small>DIGITAL</small></span>
    </a>
    <nav class="menu" id="menu" aria-label="{t['menu']}">
      <a href="{anchor(lang, 'egitim')}" class="menu-hot">{t['training']}</a>
      <a href="{anchor(lang, 'hizmetler')}">{t['services']}</a>
      <a href="{anchor(lang, 'sss')}">{t['faq']}</a>
      <a href="{blog_url(lang)}" aria-current="page">{t['blog']}</a>
    </nav>
    <div class="nav-actions">
      <div class="lang" role="group" aria-label="Dil / Language">
        <a href="{alt_tr}" data-lang-link="tr" aria-pressed="{str(lang == 'tr').lower()}" hreflang="tr">TR</a>
        <a href="{alt_en}" data-lang-link="en" aria-pressed="{str(lang == 'en').lower()}" hreflang="en">EN</a>
      </div>
      <a href="{anchor(lang, 'iletisim')}" class="btn btn-gold btn-sm">{t['cta']}</a>
      <button class="burger" id="burger" aria-label="{t['menu']}" aria-expanded="false"><span></span><span></span></button>
    </div>
  </div>
</header>'''

def footer(lang):
    return f'''<a class="wa-float" href="{WA}" target="_blank" rel="noopener" aria-label="WhatsApp">
  <svg viewBox="0 0 24 24" width="28" height="28" aria-hidden="true"><path fill="currentColor" d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2Zm0 18.2c-1.5 0-3-.4-4.3-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2Zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8-.2-.1-.4-.1-.6.1l-.8 1c-.1.2-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.3-.4.2-.4.7-1.3.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.7 11.9 11.9 0 0 0 4.6 4c1.7.7 2.4.8 3.2.7.5-.1 1.5-.6 1.7-1.2.2-.6.2-1.1.2-1.2-.1-.1-.3-.2-.5-.3Z"/></svg>
</a>
<footer class="footer">
  <div class="wrap footer-inner">
    <span>© <span id="year"></span> {BRAND}</span>
    <span class="footer-links">
      <a href="tel:{PHONE}">0 543 494 55 28</a>
      <a href="mailto:{EMAIL}">{EMAIL}</a>
      <a href="{IG}" target="_blank" rel="noopener">Instagram</a>
    </span>
  </div>
</footer>
<script src="/main.js"></script>
</body>
</html>
'''

def card(p, lang):
    d = p[lang]
    return f'''<a class="post-card" href="{post_url(p, lang)}">
  <span class="post-tag">{E(p['cat'][0 if lang == 'tr' else 1])}</span>
  <h3>{E(d['title'])}</h3>
  <p>{E(d['desc'])}</p>
  <span class="post-foot">{fmt_date(p['date'], lang)} · {p['minutes']} {T[lang]['read']}</span>
</a>'''

def write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")

# ---- clean old output ----
for d in [ROOT / "en"]:
    if d.exists(): shutil.rmtree(d)
for f in (ROOT / "blog").glob("*"):
    if f.name != "posts.js":
        shutil.rmtree(f) if f.is_dir() else f.unlink()

urls = [("/", "/?lang=en")]

for lang in ("tr", "en"):
    t = T[lang]
    other = "en" if lang == "tr" else "tr"

    # ---- posts ----
    for p in POSTS:
        d = p[lang]
        url = post_url(p, lang)
        alt = {lang: url, other: post_url(p, other)}
        body = resolve_links(d["body"], lang)
        faq_html = "".join(f'<details><summary>{E(q)}</summary><p>{E(a)}</p></details>' for q, a in d["faq"])
        related = [BY_KEY[k] for k in p.get("related", []) if k in BY_KEY]
        rel_html = "".join(f'''<a class="post-card" href="{post_url(r, lang)}"><span class="post-tag">{E(r['cat'][0 if lang=='tr' else 1])}</span><h3>{E(r[lang]['title'])}</h3><span class="post-foot">{t['readmore']}</span></a>''' for r in related)
        ld = {"@context": "https://schema.org", "@graph": [
            {"@type": "BlogPosting", "headline": d["title"], "description": d["desc"],
             "abstract": d["answer"], "inLanguage": lang, "datePublished": p["date"], "dateModified": p["date"],
             "mainEntityOfPage": f"{SITE}{url}", "image": f"{SITE}/assets/og-image.jpg",
             "articleSection": p["cat"][0 if lang == "tr" else 1],
             "author": {"@type": "Organization", "@id": f"{SITE}/#org", "name": BRAND, "url": f"{SITE}/"},
             "publisher": {"@id": f"{SITE}/#org"}},
            {"@type": "BreadcrumbList", "itemListElement": [
              {"@type": "ListItem", "position": 1, "name": t["home"], "item": f"{SITE}{home_url(lang)}"},
              {"@type": "ListItem", "position": 2, "name": t["blog"], "item": f"{SITE}{blog_url(lang)}"},
              {"@type": "ListItem", "position": 3, "name": d["title"], "item": f"{SITE}{url}"}]},
            {"@type": "FAQPage", "mainEntity": [
              {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in d["faq"]]},
            ORG]}
        page = head(lang, f"{d['title']} | {BRAND}", d["desc"], url, alt["tr"], alt["en"], ld, "article") \
            + header(lang, alt["tr"], alt["en"]) + f'''
<main>
  <article class="post">
    <div class="wrap narrow">
      <nav class="crumbs" aria-label="breadcrumb"><a href="{home_url(lang)}">{t['home']}</a><span>/</span><a href="{blog_url(lang)}">{t['blog']}</a><span>/</span><span>{E(p['cat'][0 if lang=='tr' else 1])}</span></nav>
      <p class="post-meta"><span class="post-tag">{E(p['cat'][0 if lang=='tr' else 1])}</span>
        <span>{t['by']} <a href="{home_url(lang)}">{t['team']}</a></span>
        <span>· <time datetime="{p['date']}">{fmt_date(p['date'], lang)}</time></span>
        <span>· {p['minutes']} {t['read']}</span></p>
      <h1 class="post-title">{E(d['title'])}</h1>
      <div class="answer-box"><strong>{t['short']}:</strong> {E(d['answer'])}</div>
      <div class="prose">{body}</div>
      <section class="post-faq"><h2>{t['faqh']}</h2>{faq_html}</section>
      <aside class="post-cta">
        <h3>{t['ctaT']}</h3>
        <p>{t['ctaP']}</p>
        <a href="{WA}" target="_blank" rel="noopener" class="btn btn-gold">{t['ctaB']}</a>
      </aside>
      <aside class="post-train">
        <span class="train-pill">✦ {t['trainT']}</span>
        <p>{t['trainP']}</p>
        <a href="{anchor(lang, 'egitim')}" class="link">{t['trainB']} →</a>
      </aside>
    </div>
  </article>
  <section class="section section-tight">
    <div class="wrap"><h2 class="more-title">{t['more']}</h2><div class="post-grid">{rel_html}</div></div>
  </section>
</main>
''' + footer(lang)
        write(ROOT / url.strip("/") / "index.html", page)
        if lang == "tr": urls.append((url, post_url(p, "en")))

    # ---- blog index ----
    url = blog_url(lang)
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "Blog", "name": f"{BRAND} Blog", "url": f"{SITE}{url}", "inLanguage": lang,
         "publisher": {"@id": f"{SITE}/#org"},
         "blogPost": [{"@type": "BlogPosting", "headline": p[lang]["title"], "url": f"{SITE}{post_url(p, lang)}",
                       "datePublished": p["date"]} for p in POSTS]}, ORG]}
    page = head(lang, f"{t['blog']} — {t['listT']} | {BRAND}", t["listP"], url, "/blog/", "/en/blog/", ld) \
        + header(lang, "/blog/", "/en/blog/") + f'''
<main>
  <section class="page-hero">
    <div class="wrap">
      <p class="eyebrow">{t['blog']}</p>
      <h1 class="page-title">{t['listT']}</h1>
      <p class="lead">{t['listP']}</p>
    </div>
  </section>
  <section class="section section-tight">
    <div class="wrap"><div class="post-grid">{''.join(card(p, lang) for p in POSTS)}</div></div>
  </section>
</main>
''' + footer(lang)
    write(ROOT / url.strip("/") / "index.html", page)
urls.insert(1, ("/blog/", "/en/blog/"))

# ---- posts.js for homepage cards ----
data = [{"tr": {"url": post_url(p, "tr"), "title": p["tr"]["title"], "excerpt": p["tr"]["desc"],
                "tag": p["cat"][0], "date": fmt_date(p["date"], "tr")},
         "en": {"url": post_url(p, "en"), "title": p["en"]["title"], "excerpt": p["en"]["desc"],
                "tag": p["cat"][1], "date": fmt_date(p["date"], "en")},
         "minutes": p["minutes"]} for p in POSTS]
write(ROOT / "blog" / "posts.js", "// Generated by tools/build_blog.py — do not edit by hand.\nconst POSTS = "
      + json.dumps(data, ensure_ascii=False, indent=1) + ";\n")

# ---- sitemap / robots / llms ----
last = POSTS[0]["date"]
def sm_url(tr, en, lm):
    return (f'<url><loc>{SITE}{tr}</loc><lastmod>{lm}</lastmod>'
            f'<xhtml:link rel="alternate" hreflang="tr" href="{SITE}{tr}"/>'
            f'<xhtml:link rel="alternate" hreflang="en" href="{SITE}{en}"/></url>\n')
sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
sm += sm_url("/", "/?lang=en", last) + sm_url("/blog/", "/en/blog/", last)
sm += sm_url("/en/blog/", "/en/blog/", last).replace(f'hreflang="tr" href="{SITE}/en/blog/"', f'hreflang="tr" href="{SITE}/blog/"')
for p in POSTS:
    sm += sm_url(post_url(p, "tr"), post_url(p, "en"), p["date"])
    sm += sm_url(post_url(p, "en"), post_url(p, "en"), p["date"]).replace(
        f'hreflang="tr" href="{SITE}{post_url(p, "en")}"', f'hreflang="tr" href="{SITE}{post_url(p, "tr")}"')
sm += "</urlset>\n"
write(ROOT / "sitemap.xml", sm)
write(ROOT / "robots.txt", f"User-agent: *\nAllow: /\nDisallow: /tools/\n\nSitemap: {SITE}/sitemap.xml\n")

llms = f"""# {BRAND}

> Türkiye merkezli Meta reklam ajansı. Instagram ve Facebook reklamlarıyla mesaj, form, kayıt ve satış getiren sistemler kurar; ayrıca 10 kişilik sınıflarda canlı Meta reklam eğitimi verir.
> Meta (Facebook & Instagram) ads agency based in Turkey. Builds ad systems for messages, leads and sales, and runs live Meta ads training in classes of 10.

## Hizmetler / Services
- Canlı Meta Reklam Eğitimi — eğitmenle canlı, kendi reklam hesabında, 10 kişilik sınıflar: {SITE}/#egitim
- Meta Reklam Yönetimi — strateji, kreatif yönlendirme, kurulum, optimizasyon, raporlama: {SITE}/#hizmetler
- E-Ticaret Büyüme — katalog reklamları, piksel/CAPI, yeniden hedefleme, ROAS odaklı ölçekleme: {SITE}/#hizmetler
- Sektörler: anaokulları, e-ticaret, gayrimenkul, güzellik & wellness, perakende

## İletişim / Contact
- WhatsApp & telefon: +90 543 494 55 28
- E-posta: {EMAIL}
- Instagram: {IG}

## Blog
""" + "".join(f"- [{p['tr']['title']}]({SITE}{post_url(p, 'tr')}): {p['tr']['answer']}\n" for p in POSTS) \
    + "\n## Blog (English)\n" + "".join(f"- [{p['en']['title']}]({SITE}{post_url(p, 'en')}): {p['en']['answer']}\n" for p in POSTS)
write(ROOT / "llms.txt", llms)
(ROOT / ".nojekyll").touch()

print(f"Built {len(POSTS)} posts x 2 languages; sitemap {sm.count('<url>')} urls")

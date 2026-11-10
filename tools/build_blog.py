# -*- coding: utf-8 -*-
"""Builds the blog (TR + EN), blog/posts.js, sitemap.xml, robots.txt and llms.txt.

Run from anywhere:  python3 tools/build_blog.py
Content lives in tools/posts_data.py.
"""
import html, json, pathlib, re, shutil, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
from posts_data import POSTS  # noqa: E402

SITE = "https://gloriondigital.com"   # change here when the custom domain is connected
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
        elif target == "contact": href = anchor(lang, "basvuru")
        elif target.startswith("post:"): href = post_url(BY_KEY[target[5:]], lang)
        else: raise ValueError(target)
        return f'<a class="kw" href="{href}">{text}</a>'
    return re.sub(r"\[\[([^|\]]+)\|([^\]]+)\]\]", rep, body)

ORG = {
  "@type": "ProfessionalService", "@id": f"{SITE}/#org", "name": BRAND,
  "url": f"{SITE}/", "logo": f"{SITE}/assets/icon-512.png", "image": f"{SITE}/assets/og-image.jpg",
  "telephone": PHONE, "email": EMAIL, "areaServed": "TR", "sameAs": [IG],
}

GTM_CONSENT = "<!-- Consent Mode v2 (KVKK): analytics & ads off until the visitor accepts -->\n<script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}\ngtag('consent','default',{ad_storage:'denied',ad_user_data:'denied',ad_personalization:'denied',analytics_storage:'denied',functionality_storage:'granted',security_storage:'granted',wait_for_update:500});\ntry{if(localStorage.getItem('gd-consent')==='granted'){gtag('consent','update',{ad_storage:'granted',ad_user_data:'granted',ad_personalization:'granted',analytics_storage:'granted'});}}catch(e){}</script>\n"
GTM_HEAD = "<!-- Google Tag Manager -->\n<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':\nnew Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],\nj=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=\n'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);\n})(window,document,'script','dataLayer','GTM-MHCS35X3');</script>\n<!-- End Google Tag Manager -->"
GTM_BODY = '<!-- Google Tag Manager (noscript) -->\n<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-MHCS35X3"\nheight="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>\n<!-- End Google Tag Manager (noscript) -->'

def head(lang, title, desc, canonical, alt_tr, alt_en, ld, og_type="website"):
    return f'''<!doctype html>
<html lang="{lang}" data-static="1">
<head>
{GTM_CONSENT}{GTM_HEAD}
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
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/styles.css?v=20261110a">
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
</head>
<body>
{GTM_BODY}
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
      <a href="{anchor(lang, 'hizmetler')}">{t['services']}</a>
      <a href="{anchor(lang, 'egitim')}">{t['training']}</a>
      <a href="{anchor(lang, 'sss')}">{t['faq']}</a>
      <a href="{blog_url(lang)}" aria-current="page">{t['blog']}</a>
    </nav>
    <div class="nav-actions">
      <div class="lang" role="group" aria-label="Dil / Language">
        <a href="{alt_tr}" data-lang-link="tr" aria-pressed="{str(lang == 'tr').lower()}" hreflang="tr">TR</a>
        <a href="{alt_en}" data-lang-link="en" aria-pressed="{str(lang == 'en').lower()}" hreflang="en">EN</a>
      </div>
      <a href="{anchor(lang, 'basvuru')}" class="btn btn-gold btn-sm">{t['cta']}</a>
      <button class="burger" id="burger" aria-label="{t['menu']}" aria-expanded="false"><span></span><span></span></button>
    </div>
  </div>
</header>'''

def footer(lang):
    return f'''<a class="wa-float" href="{WA}" target="_blank" rel="noopener" aria-label="WhatsApp">
  <svg viewBox="0 0 24 24" width="28" height="28" aria-hidden="true"><path fill="currentColor" d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2Zm0 18.2c-1.5 0-3-.4-4.3-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2Zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8-.2-.1-.4-.1-.6.1l-.8 1c-.1.2-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.3-.4.2-.4.7-1.3.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.7 11.9 11.9 0 0 0 4.6 4c1.7.7 2.4.8 3.2.7.5-.1 1.5-.6 1.7-1.2.2-.6.2-1.1.2-1.2-.1-.1-.3-.2-.5-.3Z"/></svg>
</a>
<a class="ig-float" href="{IG}" target="_blank" rel="noopener" aria-label="Instagram">
  <svg viewBox="0 0 24 24" width="26" height="26" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r=".9" fill="currentColor" stroke="none"/></svg>
</a>
<footer class="footer">
  <div class="wrap footer-inner">
    <span>© <span id="year"></span> {BRAND}</span>
    <span class="footer-links">
      <a href="tel:{PHONE}">0 543 494 55 28</a>
      <a href="mailto:{EMAIL}">{EMAIL}</a>
      <a href="{IG}" target="_blank" rel="noopener">Instagram</a>
      <a href="{'/kvkk/' if lang == 'tr' else '/en/privacy/'}">{'KVKK' if lang == 'tr' else 'Privacy'}</a>
    </span>
  </div>
</footer>
<script src="/nudge.js?v=20261101e" defer></script>
<script src="/main.js?v=20261110a"></script>
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
    # Turkish pages: "İnstagram" with a dotted capital; English pages and URLs stay as they are.
    if path.suffix == ".html" and "/en/" not in str(path).replace("\\", "/"):
        text = text.replace("Instagram", "İnstagram")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")

# ---- clean old output ----
for d in [ROOT / "en", ROOT / "kvkk"]:
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
data = [{"tr": {"url": post_url(p, "tr"), "title": p["tr"]["title"].replace("Instagram", "İnstagram"), "excerpt": p["tr"]["desc"].replace("Instagram", "İnstagram"),
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

# ---------------------------------------------------------------------------
# KVKK / Privacy pages
# ---------------------------------------------------------------------------
LEGAL_UPDATED = "2026-11-01"
KVKK = {
 "tr": dict(url="/kvkk/", title="KVKK Aydınlatma Metni",
  desc="Glorion Digital web sitesi üzerinden toplanan kişisel verilerin işlenmesine ilişkin 6698 sayılı KVKK kapsamında aydınlatma metni.",
  body=f"""
<p>Bu metin, 6698 sayılı Kişisel Verilerin Korunması Kanunu (“KVKK”) uyarınca, <strong>Gülsüm KABA (Glorion Digital)</strong> (“biz”) tarafından bu web sitesi üzerinden toplanan kişisel verilerin hangi amaçla ve nasıl işlendiği konusunda sizi bilgilendirmek için hazırlanmıştır.</p>
<h2>1. Veri sorumlusu</h2>
<p>Veri sorumlusu, <strong>Gülsüm KABA (Glorion Digital)</strong>'dır.<br>Adres: Ortaköy Mahallesi, Diğerküme Evleri, 360 Sokak No:1A, Arslan Villaları, Menteşe/Muğla.<br>Bize <a href="mailto:info.gloriondigital@gmail.com">info.gloriondigital@gmail.com</a> adresinden ve <a href="tel:+905434945528">0 543 494 55 28</a> numarasından ulaşabilirsiniz.</p>
<h2>2. İşlenen kişisel veriler</h2>
<ul>
<li><strong>Kimlik ve iletişim:</strong> ad soyad, telefon numarası, e-posta adresi.</li>
<li><strong>Talep bilgileri:</strong> işletme veya okul adı, sektör, ilgilendiğiniz hizmet ve mesajınız.</li>
<li><strong>İşlem bilgisi:</strong> formun gönderildiği tarih, sayfa ve dil tercihi.</li>
</ul>
<p>Formlarda sizden özel nitelikli kişisel veri (sağlık, din, biyometrik veri vb.) istemiyoruz; lütfen mesaj alanına bu tür bilgiler yazmayın.</p>
<h2>3. İşleme amaçları</h2>
<ul>
<li>Ücretsiz ön görüşme, hizmet ve eğitim taleplerinize dönüş yapmak,</li>
<li>Talep ettiğiniz örnek eğitim dokümanını size sunmak,</li>
<li>Eğitim dönemleri ve hizmetlerimiz hakkında, talebinizle ilgili bilgi vermek,</li>
<li>Hukuki yükümlülüklerimizi yerine getirmek ve olası uyuşmazlıklarda haklarımızı korumak.</li>
</ul>
<h2>4. Hukuki sebepler ve toplama yöntemi</h2>
<p>Verileriniz, web sitemizdeki formlar ve WhatsApp üzerinden, elektronik ortamda toplanır. KVKK'nın 5. maddesinde yer alan; bir sözleşmenin kurulması veya ifasıyla doğrudan ilgili olması, veri sorumlusunun meşru menfaati ve hukuki yükümlülüklerin yerine getirilmesi sebeplerine; yurt dışına aktarım gerektiren işlemler için ise KVKK'nın 9. maddesi kapsamında açık rızanıza dayanılarak işlenir.</p>
<h2>5. Aktarım</h2>
<p>Formda paylaştığınız iletişim bilgileriniz satılmaz ve reklam amacıyla üçüncü kişilerle paylaşılmaz. Hizmetin sunulabilmesi için aşağıdaki hizmet sağlayıcılar kullanılır; bu sağlayıcıların sunucuları yurt dışında bulunabilir:</p>
<ul>
<li><strong>Google (Google E-Tablolar / Apps Script):</strong> form kayıtlarının saklanması,</li>
<li><strong>WhatsApp (Meta):</strong> WhatsApp üzerinden iletişime geçmeyi seçmeniz halinde mesajlaşma,</li>
<li><strong>GitHub Pages:</strong> web sitesinin barındırılması (teknik erişim kayıtları),</li>
<li><strong>Google Fonts:</strong> sitedeki yazı tiplerinin yüklenmesi (IP adresi gibi teknik veriler),</li>
<li><strong>Google Analytics ve Google Etiket Yöneticisi:</strong> yalnızca çerezlere onay vermeniz halinde, site ziyaretlerinin istatistiksel olarak ölçülmesi,</li>
<li><strong>Meta Pikseli (Meta Platforms):</strong> yalnızca çerezlere onay vermeniz halinde, reklamlarımızın ölçülmesi ve ilgili kitlelere gösterilmesi (ziyaret edilen sayfa, form gönderimi veya iletişim butonuna tıklama gibi olaylar; ad ve telefon gibi form bilgileriniz Meta'ya gönderilmez).</li>
</ul>
<p>Ayrıca kanunen yetkili kamu kurum ve kuruluşlarına, talep halinde ve mevzuatın izin verdiği ölçüde aktarım yapılabilir.</p>
<h2>6. Çerezler ve yerel depolama</h2>
<p>Sitemizde, yalnızca açık rızanızla çalışan analiz (Google Analytics) ve reklam (Meta Pikseli) çerezleri kullanılır. Siteye ilk girişinizde çıkan bildirimden bu çerezleri kabul edebilir veya reddedebilirsiniz; reddetmeniz halinde bu çerezler yerleştirilmez. Tercihinizi istediğiniz zaman sayfanın altındaki "Çerez Ayarları" bağlantısından değiştirebilirsiniz.</p>
<p>Dil tercihiniz, çerez tercihiniz, örnek PDF formunu doldurduğunuz bilgisi ve sitedeki bilgilendirme kutularını kapatıp kapatmadığınız, tekrar sormamak için yalnızca tarayıcınızın yerel depolama alanında tutulur. Tarayıcı ayarlarınızdan bu kayıtları istediğiniz zaman silebilirsiniz.</p>
<h2>7. Saklama süresi</h2>
<p>Verileriniz, işleme amacının gerektirdiği süre boyunca ve her halükarda ilgili mevzuatta öngörülen süreler kadar saklanır; süre sonunda silinir, yok edilir veya anonim hale getirilir.</p>
<h2>8. Haklarınız</h2>
<p>KVKK'nın 11. maddesi uyarınca; kişisel verilerinizin işlenip işlenmediğini öğrenme, işlenmişse bilgi talep etme, işlenme amacını ve amacına uygun kullanılıp kullanılmadığını öğrenme, aktarıldığı üçüncü kişileri bilme, eksik veya yanlış işlenmişse düzeltilmesini, şartları oluştuğunda silinmesini veya yok edilmesini isteme, bu işlemlerin aktarılan üçüncü kişilere bildirilmesini isteme, münhasıran otomatik sistemlerle analiz edilmesi sonucu aleyhinize bir sonuç çıkmasına itiraz etme ve kanuna aykırı işleme nedeniyle zarara uğramanız halinde zararın giderilmesini talep etme haklarına sahipsiniz.</p>
<h2>9. Başvuru</h2>
<p>Haklarınıza ilişkin taleplerinizi, kimliğinizi doğrulayacak bilgilerle birlikte <a href="mailto:info.gloriondigital@gmail.com">info.gloriondigital@gmail.com</a> adresine iletebilirsiniz. Başvurunuz en geç 30 gün içinde ücretsiz olarak sonuçlandırılır.</p>
"""),
 "en": dict(url="/en/privacy/", title="Privacy Notice (KVKK)",
  desc="Privacy notice under Turkish Personal Data Protection Law No. 6698 (KVKK) for personal data collected through the Glorion Digital website.",
  body=f"""
<p>This notice explains, under Turkish Personal Data Protection Law No. 6698 (“KVKK”), how <strong>Gülsüm KABA (Glorion Digital)</strong> (“we”) processes personal data collected through this website and for what purposes. The Turkish version is the binding text.</p>
<h2>1. Data controller</h2>
<p>The data controller is <strong>Gülsüm KABA (Glorion Digital)</strong>.<br>Address: Ortaköy Mahallesi, Diğerküme Evleri, 360 Sokak No:1A, Arslan Villaları, Menteşe/Muğla, Türkiye.<br>You can reach us at <a href="mailto:info.gloriondigital@gmail.com">info.gloriondigital@gmail.com</a> or <a href="tel:+905434945528">+90 543 494 55 28</a>.</p>
<h2>2. Personal data we process</h2>
<ul>
<li><strong>Identity and contact:</strong> full name, phone number, email address.</li>
<li><strong>Request details:</strong> business or school name, industry, the service you're interested in and your message.</li>
<li><strong>Transaction data:</strong> date, page and language of the submission.</li>
</ul>
<p>We do not ask for special categories of personal data (health, religion, biometrics, etc.); please do not include such information in the message field.</p>
<h2>3. Purposes</h2>
<ul>
<li>Responding to your consultation, service and training requests,</li>
<li>Providing the sample training document you requested,</li>
<li>Informing you about classes and services related to your request,</li>
<li>Meeting legal obligations and protecting our rights in potential disputes.</li>
</ul>
<h2>4. Legal grounds and collection method</h2>
<p>Data is collected electronically through our website forms and WhatsApp. It is processed under Article 5 of KVKK (necessity for entering into or performing a contract, legitimate interest, legal obligations), and, for transfers abroad, on the basis of your explicit consent under Article 9.</p>
<h2>5. Transfers</h2>
<p>The contact details you share in our forms are never sold or shared with third parties for advertising. The following providers are used to run the service, and their servers may be located outside Turkey:</p>
<ul>
<li><strong>Google (Google Sheets / Apps Script):</strong> storing form submissions,</li>
<li><strong>WhatsApp (Meta):</strong> messaging, if you choose to contact us on WhatsApp,</li>
<li><strong>GitHub Pages:</strong> website hosting (technical access logs),</li>
<li><strong>Google Fonts:</strong> loading fonts (technical data such as IP address),</li>
<li><strong>Google Analytics and Google Tag Manager:</strong> only if you accept cookies, statistical measurement of site visits,</li>
<li><strong>Meta Pixel (Meta Platforms):</strong> only if you accept cookies, measuring our ads and showing them to relevant audiences (events such as pages viewed, form submissions or clicks on contact buttons; your name and phone number from forms are not sent to Meta).</li>
</ul>
<p>Data may also be shared with authorized public authorities upon request, as permitted by law.</p>
<h2>6. Cookies and local storage</h2>
<p>We use analytics (Google Analytics) and advertising (Meta Pixel) cookies only with your explicit consent. You can accept or reject them in the notice shown on your first visit; if you reject, these cookies are not set. You can change your choice at any time via the "Cookie settings" link at the bottom of the page.</p>
<p>Your language preference, your cookie choice, whether you've filled in the sample PDF form and whether you've closed the information boxes on the site are stored only in your browser's local storage so we don't ask again. You can clear them in your browser settings at any time.</p>
<h2>7. Retention</h2>
<p>Data is kept for as long as the purpose requires and in any case for the periods set by applicable law, after which it is deleted, destroyed or anonymized.</p>
<h2>8. Your rights</h2>
<p>Under Article 11 of KVKK you have the right to learn whether your data is processed, request information about it, learn the purpose and whether it is used accordingly, know the third parties it is transferred to, request correction of incomplete or inaccurate data, request deletion or destruction where conditions are met, request that such actions be notified to third parties, object to outcomes against you arising solely from automated analysis, and claim compensation for damages caused by unlawful processing.</p>
<h2>9. How to apply</h2>
<p>Send your request, with information that verifies your identity, to <a href="mailto:info.gloriondigital@gmail.com">info.gloriondigital@gmail.com</a>. Requests are answered free of charge within 30 days at the latest.</p>
"""),
}

for lang in ("tr", "en"):
    k = KVKK[lang]; t = T[lang]
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "WebPage", "name": k["title"], "url": f"{SITE}{k['url']}", "inLanguage": lang,
         "dateModified": LEGAL_UPDATED, "publisher": {"@id": f"{SITE}/#org"}}, ORG]}
    page = head(lang, f"{k['title']} | {BRAND}", k["desc"], k["url"], KVKK["tr"]["url"], KVKK["en"]["url"], ld) \
        + header(lang, KVKK["tr"]["url"], KVKK["en"]["url"]) + f'''
<main>
  <article class="post">
    <div class="wrap narrow">
      <nav class="crumbs" aria-label="breadcrumb"><a href="{home_url(lang)}">{t['home']}</a><span>/</span><span>{k['title']}</span></nav>
      <h1 class="post-title">{k['title']}</h1>
      <p class="post-meta"><span>{t['updated']}: <time datetime="{LEGAL_UPDATED}">{fmt_date(LEGAL_UPDATED, lang)}</time></span></p>
      <div class="prose legal">{k['body']}</div>
    </div>
  </article>
</main>
''' + footer(lang)
    write(ROOT / k["url"].strip("/") / "index.html", page)

# add legal pages to sitemap
sm_path = ROOT / "sitemap.xml"
smx = sm_path.read_text(encoding="utf-8").replace("</urlset>\n",
    sm_url(KVKK["tr"]["url"], KVKK["en"]["url"], LEGAL_UPDATED)
    + sm_url(KVKK["en"]["url"], KVKK["en"]["url"], LEGAL_UPDATED).replace(
        f'hreflang="tr" href="{SITE}{KVKK["en"]["url"]}"', f'hreflang="tr" href="{SITE}{KVKK["tr"]["url"]}"')
    + "</urlset>\n")
sm_path.write_text(smx, encoding="utf-8")
print("Built KVKK pages")

# ---------------------------------------------------------------------------
# Hizmet detay sayfalari (tools/services_data.py)
# ---------------------------------------------------------------------------
from services_data import SERVICES
SVC_UPDATED = "2026-11-01"
SVC_DIR = {"tr": "/hizmetler/", "en": "/en/services/"}
if (ROOT / "hizmetler").exists():
    shutil.rmtree(ROOT / "hizmetler")

def svc_url(s, lang): return f"{SVC_DIR[lang]}{s[lang]['slug']}/"

SVC_T = {
  "tr": dict(svc="Hizmetler", cta="Ücretsiz ön görüşme al", wa="WhatsApp'tan yazın", stats_t="Rakamlarla",
             pay_t="Kredi kartıyla güvenli ödeme", pay_p="Teklif onayından sonra size özel, güvenli bir ödeme linki gönderiyoruz; ödemeyi kredi kartınızla tamamlıyorsunuz. Ödeme linkini yalnızca 0 543 494 55 28 numaralı WhatsApp hattımızdan veya info.gloriondigital@gmail.com adresinden gönderiyoruz.",
             pay_more="Ödeme nasıl yapılır?", other="Diğer hizmetlerimiz", detail="Detayları incele →",
             form_t="Ücretsiz ön görüşme başvurusu", form_sub="Formu doldurun, en kısa sürede size dönelim.",
             name="Ad Soyad", phone="Telefon", business="İşletme adı", sector="Sektör", service="İlgilendiğiniz hizmet",
             message="Mesajınız (isteğe bağlı)", submit="Başvuruyu Gönder",
             consent='<a href="/kvkk/" target="_blank" rel="noopener">KVKK Aydınlatma Metni</a>\'ni okudum; bilgilerimin benimle iletişime geçilmesi amacıyla işlenmesini kabul ediyorum.',
             sectors=[("Anaokulu","Anaokulları"),("E-ticaret","E-ticaret"),("Gayrimenkul","Gayrimenkul"),("Güzellik & Wellness","Güzellik &amp; Wellness"),("Perakende","Perakende"),("Diğer","Diğer")],
             stats=[("50+","yönetilen e-ticaret mağazası"),("50+","hizmet verilen eğitim kurumu"),("60+","eğitim verilen kişi"),("%100","şeffaf raporlama")]),
  "en": dict(svc="Services", cta="Get a free consultation", wa="Message on WhatsApp", stats_t="In numbers",
             pay_t="Secure credit card payment", pay_p="After you approve the quote, we send you a personal, secure payment link and you complete the payment by credit card. We only send payment links from our WhatsApp line 0 543 494 55 28 or from info.gloriondigital@gmail.com.",
             pay_more="How payment works", other="Our other services", detail="See details →",
             form_t="Free consultation request", form_sub="Fill in the form and we'll get back to you shortly.",
             name="Full name", phone="Phone", business="Business name", sector="Industry", service="Service you're interested in",
             message="Your message (optional)", submit="Send request",
             consent='I have read the <a href="/en/privacy/" target="_blank" rel="noopener">Privacy Notice</a> and agree that my details are processed to contact me.',
             sectors=[("Anaokulu","Preschools"),("E-ticaret","E-commerce"),("Gayrimenkul","Real Estate"),("Güzellik & Wellness","Beauty &amp; Wellness"),("Perakende","Retail"),("Diğer","Other")],
             stats=[("50+","e-commerce stores managed"),("50+","education institutions served"),("60+","people trained"),("100%","transparent reporting")]),
}
CARD_SVG = '<svg class="pay-ic" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="2.5" y="5" width="19" height="14" rx="2.5"/><path d="M2.5 10h19M6.5 15h4"/></svg>'

def svc_form(s, lang):
    st = SVC_T[lang]
    opts = "".join(f'<option value="{E(x["form_value"])}"{" selected" if x is s else ""}>{E(x[lang]["title"])}</option>' for x in SERVICES)
    secs = "".join(f'<option value="{E(v)}"{" selected" if (s["key"] == "eticaret" and v == "E-ticaret") else ""}>{lab}</option>' for v, lab in st["sectors"])
    return f'''<form class="lead-form" id="leadForm" novalidate>
        <h3>{st['form_t']}</h3>
        <p class="form-sub">{st['form_sub']}</p>
        <div class="form-grid">
          <label><span>{st['name']}</span><input name="name" type="text" autocomplete="name" required></label>
          <label><span>{st['phone']}</span><input name="phone" type="tel" autocomplete="tel" inputmode="tel" required placeholder="05xx xxx xx xx"></label>
          <label><span>{st['business']}</span><input name="business" type="text" autocomplete="organization"></label>
          <label><span>{st['sector']}</span><select name="sector">{secs}</select></label>
          <label class="full"><span>{st['service']}</span><select name="service">{opts}</select></label>
          <label class="full"><span>{st['message']}</span><textarea name="message" rows="3"></textarea></label>
          <input type="text" name="website" class="hp" tabindex="-1" autocomplete="off" aria-hidden="true">
          <label class="check full"><input type="checkbox" name="consent" required><span>{st['consent']}</span></label>
        </div>
        <button type="submit" class="btn btn-gold btn-block">{st['submit']}</button>
        <p class="form-status" id="formStatus" role="status" aria-live="polite"></p>
      </form>'''

def svc_page(s, lang):
    d = s[lang]; t = T[lang]; st = SVC_T[lang]
    url = svc_url(s, lang); alt_tr = svc_url(s, "tr"); alt_en = svc_url(s, "en")
    service_ld = {"@type": "Course" if s["key"] == "egitim" else "Service", "name": d["title"], "description": d["desc"],
                  "url": f"{SITE}{url}", "inLanguage": lang, "provider": {"@id": f"{SITE}/#org"}}
    if s["key"] != "egitim":
        service_ld.update({"serviceType": d["title"], "areaServed": "TR"})
    ld = {"@context": "https://schema.org", "@graph": [
        service_ld,
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": t["home"], "item": f"{SITE}{home_url(lang)}"},
            {"@type": "ListItem", "position": 2, "name": st["svc"], "item": f"{SITE}{anchor(lang, 'hizmetler')}"},
            {"@type": "ListItem", "position": 3, "name": d["title"], "item": f"{SITE}{url}"}]},
        {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in d["faq"]]},
        ORG]}
    wa_text = "EĞİTİM - Canlı Meta Reklam Eğitimi hakkında bilgi almak istiyorum." if s["key"] == "egitim" else f"Merhaba, {s['tr']['title']} hizmeti hakkında bilgi almak istiyorum."
    wa = f"{WA}?text={urllib.parse.quote(wa_text)}"
    fors = "".join(f"<li>{E(x)}</li>" for x in d["for"])
    incs = "".join(f'<article class="card"><h3>{E(h)}</h3><p>{E(p)}</p></article>' for h, p in d["inc"])
    steps = "".join(f"<li><span>{i+1:02d}</span><h3>{E(h)}</h3><p>{E(p)}</p></li>" for i, (h, p) in enumerate(d["steps"]))
    gets = "".join(f"<li>{E(x)}</li>" for x in d["get"])
    faqs = "".join(f"<details><summary>{E(q)}</summary><p>{E(a)}</p></details>" for q, a in d["faq"])
    stats = "".join(f'<div><b>{n}</b><span>{E(l)}</span></div>' for n, l in st["stats"])
    levels = ""
    if d.get("levels"):
        lv = "".join(f"<li><span>{'+' if i == 3 else f'{i+1:02d}'}</span><h3>{E(h)}</h3><p>{E(p)}</p></li>" for i, (h, p) in enumerate(d["levels"]))
        levels = f'''
  <section id="egitim" class="section section-alt">
    <div class="wrap">
      <p class="eyebrow">{E(d['title'])}</p>
      <h2>{E(d['levels_title'])}</h2>
      <ol class="steps">{lv}</ol>
    </div>
  </section>'''
    others = "".join(f'<a class="card svc-other" href="{svc_url(x, lang)}"><span class="icon">{x["icon"]}</span><h3>{E(x[lang]["title"])}</h3><p>{E(x[lang]["desc"])}</p><span class="link">{st["detail"]}</span></a>' for x in SERVICES if x is not s)
    pay_anchor = anchor(lang, "odeme")
    page = head(lang, f"{d['seo_title']} | {BRAND}", d["desc"], url, alt_tr, alt_en, ld) \
        + header(lang, alt_tr, alt_en).replace(' aria-current="page"', '').replace(f'href="{anchor(lang, "basvuru")}" class="btn btn-gold btn-sm"', 'href="#basvuru" class="btn btn-gold btn-sm"') + f'''
<main data-service="{s['key']}">
  <section class="section svc-hero">
    <div class="wrap">
      <nav class="crumbs" aria-label="breadcrumb"><a href="{home_url(lang)}">{t['home']}</a><span>/</span><a href="{anchor(lang, 'hizmetler')}">{st['svc']}</a><span>/</span><span>{E(d['title'])}</span></nav>
      <div class="svc-hero-grid">
        <div>
          <span class="icon svc-icon" aria-hidden="true">{s['icon']}</span>
          <h1 class="svc-title">{E(d['title'])}</h1>
          <p class="lead">{E(d['lead'])}</p>
          <div class="hero-cta">
            <a href="#basvuru" class="btn btn-gold">{st['cta']}</a>
            <a href="{wa}" target="_blank" rel="noopener" class="btn btn-ghost">{st['wa']}</a>
          </div>
          <p class="note pay-inline">{CARD_SVG}<span>{st['pay_t']}</span> <a href="#odeme-bilgi" class="link">{st['pay_more']}</a></p>
        </div>
        <aside class="svc-for">
          <h2>{E(d['for_title'])}</h2>
          <ul>{fors}</ul>
        </aside>
      </div>
    </div>
  </section>

  <section class="section section-alt">
    <div class="wrap">
      <p class="eyebrow">{E(d['title'])}</p>
      <h2>{E(d['inc_title'])}</h2>
      <div class="cards svc-inc">{incs}</div>
    </div>
  </section>
{levels}
  <section class="section">
    <div class="wrap">
      <h2>{E(d['steps_title'])}</h2>
      <ol class="steps">{steps}</ol>
    </div>
  </section>

  <section class="section section-alt">
    <div class="wrap svc-get-grid">
      <div>
        <h2>{E(d['get_title'])}</h2>
        <ul class="svc-get">{gets}</ul>
      </div>
      <div class="svc-stats" aria-label="{st['stats_t']}">{stats}</div>
    </div>
  </section>

  <section class="section" id="odeme-bilgi">
    <div class="wrap narrow">
      <p class="pay-note svc-pay">{CARD_SVG}<span><strong>{st['pay_t']}.</strong> {st['pay_p']} <a href="{pay_anchor}" class="link">{st['pay_more']} →</a></span></p>
      <h2 class="svc-faq-h">{t['faqh']}</h2>
      {faqs}
    </div>
  </section>

  <section class="section contact" id="iletisim">
    <div class="wrap contact-inner">
      <h2>{E(d['cta_title'])}</h2>
      <p class="lead">{E(d['cta_lead'])}</p>
      <div id="basvuru" aria-hidden="true"></div>
      {svc_form(s, lang)}
    </div>
  </section>

  <section class="section section-alt">
    <div class="wrap">
      <h2>{st['other']}</h2>
      <div class="cards svc-others">{others}</div>
    </div>
  </section>
</main>
''' + footer(lang).replace('<script src="/nudge.js', '<script src="/config.js?v=20261101a"></script>\n<script src="/i18n.js?v=20261102b"></script>\n<script src="/nudge.js')
    write(ROOT / url.strip("/") / "index.html", page)

import urllib.parse
for s in SERVICES:
    for lang in ("tr", "en"):
        svc_page(s, lang)

smx = sm_path.read_text(encoding="utf-8").replace("</urlset>\n", "".join(
    sm_url(svc_url(s, "tr"), svc_url(s, "en"), SVC_UPDATED)
    + sm_url(svc_url(s, "en"), svc_url(s, "en"), SVC_UPDATED).replace(
        f'hreflang="tr" href="{SITE}{svc_url(s, "en")}"', f'hreflang="tr" href="{SITE}{svc_url(s, "tr")}"')
    for s in SERVICES) + "</urlset>\n")
sm_path.write_text(smx, encoding="utf-8")

llms_path = ROOT / "llms.txt"
lt = llms_path.read_text(encoding="utf-8")
for s in SERVICES:
    lt = lt.replace(f"{SITE}/#egitim" if s["key"] == "egitim" else "@@none@@", f"{SITE}{svc_url(s, 'tr')}")
lt = lt.replace(f"raporlama: {SITE}/#hizmetler", f"raporlama: {SITE}{svc_url(SERVICES[0], 'tr')}")
lt = lt.replace(f"ölçekleme: {SITE}/#hizmetler", f"ölçekleme: {SITE}{svc_url(SERVICES[1], 'tr')}")
llms_path.write_text(lt, encoding="utf-8")
print("Built service pages:", ", ".join(svc_url(s, l) for s in SERVICES for l in ("tr", "en")))

# ---------------------------------------------------------------------------
# Musteri degerlendirme sayfasi (/yorum/) — menude yok, arama motorlarina kapali.
# Yanitlar "Glorion Digital — Musteri Degerlendirmesi" Google Formu'na gider.
# ---------------------------------------------------------------------------
REVIEW_FORM = "https://docs.google.com/forms/d/e/1FAIpQLSdx5Kc4kTAC7FFWFKiWXXjTW6eFh_DEaoV8JNTc_CD_7_of1w/formResponse"
RV_CONSENT = "Bu görüşün Glorion Digital'in web sitesi ve sosyal medya hesaplarında, seçtiğim şekilde yayınlanmasına izin veriyorum. Telefon numaram yayınlanmaz."
RV_SERVICES = ["Meta Reklam Yönetimi", "E-Ticaret Büyüme", "Canlı Meta Reklam Eğitimi"]
RV_DISPLAY = ["Ad soyadım ve işletmemle", "Adım ve soyadımın baş harfiyle (ör. Ayşe K.)", "İsimsiz, sadece sektörümle (ör. Anaokulu sahibi)"]

def rv_radio(name, opts):
    return "".join(f'<label class="rv-opt"><input type="radio" name="{name}" value="{E(o)}" required><span>{E(o)}</span></label>' for o in opts)

rv_ld = {"@context": "https://schema.org", "@graph": [{"@type": "WebPage", "name": "Müşteri Değerlendirmesi", "url": f"{SITE}/yorum/", "inLanguage": "tr"}, ORG]}
rv_page = head("tr", f"Müşteri Değerlendirmesi | {BRAND}", "Glorion Digital ile çalışma deneyiminizi paylaşın.", "/yorum/", "/yorum/", "/yorum/", rv_ld) \
    .replace('<meta name="robots" content="index,follow,max-image-preview:large">', '<meta name="robots" content="noindex,nofollow">') \
    + header("tr", "/yorum/", "/yorum/").replace(' aria-current="page"', '') + f'''
<main>
  <section class="section contact rv">
    <div class="wrap contact-inner">
      <p class="eyebrow">Müşteri değerlendirmesi</p>
      <h1 class="svc-title">Bizimle çalışmak nasıldı?</h1>
      <p class="lead">Görüşünüz bizim için çok değerli. İzin verirseniz web sitemizde ve sosyal medya hesaplarımızda, seçtiğiniz şekilde paylaşacağız. Form 1 dakika sürer.</p>
      <form class="lead-form rv-form" id="reviewForm" novalidate>
        <fieldset class="rv-group"><legend>Hangi hizmetimizi aldınız? <span class="rv-req">*</span></legend>{rv_radio("entry.1451213733", RV_SERVICES)}</fieldset>
        <label class="rv-field"><span>Görüşünüz nedir? Bizimle çalışmak size neler kazandırdı? <span class="rv-req">*</span></span>
          <textarea name="entry.989898274" rows="5" required></textarea></label>
        <div class="form-grid">
          <label><span>Ad Soyad <small>(isteğe bağlı)</small></span><input name="entry.24661653" type="text" autocomplete="name"></label>
          <label><span>İşletmeniz veya sektörünüz <small>(isteğe bağlı)</small></span><input name="entry.151524149" type="text" autocomplete="organization" placeholder="ör. Anaokulu, E-ticaret"></label>
        </div>
        <fieldset class="rv-group"><legend>Görüşünüz sitede nasıl görünsün? <span class="rv-req">*</span></legend>{rv_radio("entry.258122235", RV_DISPLAY)}</fieldset>
        <label class="rv-field"><span>Telefon numaranız <span class="rv-req">*</span> <small>(yayınlanmaz, yalnızca doğrulama ve izin kaydı için)</small></span>
          <input name="entry.609434414" type="tel" autocomplete="tel" inputmode="tel" required placeholder="05xx xxx xx xx"></label>
        <label class="check rv-consent"><input type="checkbox" name="entry.1792725728" value="{E(RV_CONSENT)}" required><span>{E(RV_CONSENT)} <span class="rv-req">*</span></span></label>
        <p class="rv-kvkk">Bilgileriniz <a href="/kvkk/" target="_blank" rel="noopener">KVKK Aydınlatma Metni</a> kapsamında işlenir.</p>
        <button type="submit" class="btn btn-gold btn-block">Değerlendirmeyi Gönder</button>
        <p class="form-status" id="rvStatus" role="status" aria-live="polite"></p>
      </form>
      <div class="lead-form rv-thanks" id="rvThanks" hidden>
        <h3>Teşekkür ederiz!</h3>
        <p class="form-sub">Değerlendirmeniz bize ulaştı. Desteğiniz için çok teşekkürler.</p>
      </div>
    </div>
  </section>
</main>
<script>
(function () {{
  var f = document.getElementById('reviewForm'), st = document.getElementById('rvStatus');
  f.addEventListener('submit', function (e) {{
    e.preventDefault();
    var fd = new FormData(f), msg = '';
    if (!fd.get('entry.1451213733')) msg = 'Lütfen aldığınız hizmeti seçin.';
    else if (!String(fd.get('entry.989898274') || '').trim()) msg = 'Lütfen görüşünüzü yazın.';
    else if (!fd.get('entry.258122235')) msg = 'Lütfen görüşünüzün sitede nasıl görüneceğini seçin.';
    else if (fd.get('entry.258122235') !== {json.dumps(RV_DISPLAY[2], ensure_ascii=False)} && !String(fd.get('entry.24661653') || '').trim()) msg = 'Bu görünüm seçeneği için ad soyadınızı yazın ya da "İsimsiz" seçeneğini işaretleyin.';
    else if (String(fd.get('entry.609434414') || '').replace(/\\D/g, '').length < 10) msg = 'Lütfen geçerli bir telefon numarası yazın.';
    else if (!fd.get('entry.1792725728')) msg = 'Paylaşabilmemiz için yayın iznini işaretleyin.';
    if (msg) {{ st.textContent = msg; st.dataset.kind = 'err'; return; }}
    var body = new URLSearchParams();
    fd.forEach(function (v, k) {{ if (String(v).trim()) body.append(k, v); }});
    var btn = f.querySelector('button'); btn.disabled = true; st.textContent = 'Gönderiliyor…'; st.dataset.kind = '';
    fetch({json.dumps(REVIEW_FORM)}, {{ method: 'POST', mode: 'no-cors', body: body }})
      .then(function () {{ f.hidden = true; document.getElementById('rvThanks').hidden = false; window.scrollTo({{ top: 0, behavior: 'smooth' }}); }})
      .catch(function () {{ btn.disabled = false; st.textContent = 'Bir sorun oluştu, lütfen tekrar deneyin.'; st.dataset.kind = 'err'; }});
  }});
}})();
</script>
''' + footer("tr").replace('<script src="/nudge.js?v=20261101e" defer></script>\n', '')
write(ROOT / "yorum" / "index.html", rv_page)
print("Built /yorum/")

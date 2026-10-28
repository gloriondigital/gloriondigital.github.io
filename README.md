# Glorion Digital — Web Sitesi

Yayın adresi: https://gloriondigital.com (yedek: https://gloriondigital.github.io)

Statik site (HTML/CSS/JS). Türkçe varsayılan, İngilizce desteği var. CRM'den bağımsızdır.

## Yapı
- `index.html` — ana sayfa (TR metinler), `i18n.js` — ana sayfanın İngilizce çevirileri
- `styles.css`, `main.js` — tasarım, dil geçişi, efektler, form
- `config.js` — form bağlantısı (`FORM_ENDPOINT`) ve WhatsApp numarası
- `blog/` (TR) ve `en/blog/` (EN) — **oluşturulan** blog sayfaları, elle düzenlemeyin
- `tools/posts_data.py` — blog içerikleri; `tools/build_blog.py` — blog, sitemap, robots.txt, llms.txt oluşturucu
- `google-sheets-form.gs` — formu Google Sheet'e bağlayan Apps Script kodu
- `assets/` — logo, favicon, paylaşım görseli

## Yeni blog yazısı eklemek
1. `tools/posts_data.py` içine yeni bir kayıt ekleyin (TR + EN; başlık, açıklama, kısa cevap, metin, SSS, ilgili yazılar).
   Metin içi linkler: `[[services|metin]]`, `[[training|metin]]`, `[[contact|metin]]`, `[[post:<key>|metin]]`.
2. `python3 tools/build_blog.py` çalıştırın.
3. Commit + push. GitHub Pages birkaç dakikada yayına alır.

## SEO / GEO
Her yazıda: canonical + hreflang (TR/EN), Open Graph, BlogPosting + BreadcrumbList + FAQPage şeması,
"Kısa cevap" kutusu, soru biçiminde başlıklar, metin içi linkler ve ilgili yazılar.
Sitede ayrıca: `sitemap.xml`, `robots.txt`, `llms.txt`, ana sayfada ProfessionalService + Course + FAQPage şeması.

## Form → Google Sheet
1. Meta formunun bağlı olduğu Sheet'te Uzantılar → Apps Script, `google-sheets-form.gs` içeriğini yapıştırın.
2. Dağıt → Yeni dağıtım → Web uygulaması (Yürütme: Ben, Erişim: Herkes).
3. Verilen `/exec` adresini `config.js` içindeki `FORM_ENDPOINT` değerine yazın.
Boş bırakılırsa form, bilgileri WhatsApp'a aktarır.

## Alan adı
Kendi alan adını bağlarken: Settings → Pages → Custom domain, ardından `tools/build_blog.py` içindeki `SITE` ve
`index.html` içindeki canonical/og adreslerini güncelleyip `python3 tools/build_blog.py` çalıştırın.

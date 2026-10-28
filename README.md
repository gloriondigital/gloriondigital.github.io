# Glorion Digital — Web Sitesi

Glorion Digital için tek sayfalık, statik tanıtım sitesi. Türkçe varsayılan, İngilizce dil desteği var (sağ üstteki TR/EN düğmesi veya `?lang=en`).

CRM'den bağımsızdır: form, takip kodu veya harici veri bağlantısı yoktur. İletişim butonları doğrudan Instagram DM'e (`ig.me/m/gloriondigital`) gider.

## Dosyalar
- `index.html` — sayfa ve Türkçe metinler
- `i18n.js` — İngilizce çeviriler
- `styles.css` — tasarım (siyah + altın)
- `main.js` — dil değiştirme ve mobil menü

## Metin düzenleme
Türkçe metni `index.html` içinde, İngilizcesini `i18n.js` içinde aynı anahtarla (`data-i18n="..."`) değiştirin.

## Yayınlama
Derleme gerekmez. GitHub Pages: Settings → Pages → Branch: `main` / root. Alan adı için `CNAME` dosyası eklenebilir.

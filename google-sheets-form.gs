/**
 * Glorion Digital — web sitesi formunu Google Sheet'e bağlar.
 *
 * KURULUM (bir kez):
 * 1. Meta formunun bağlı olduğu Google Sheet'i açın.
 * 2. Uzantılar → Apps Script. Açılan editördeki kodu silip bu dosyanın tamamını yapıştırın, kaydedin.
 * 3. Dağıt → Yeni dağıtım → Web uygulaması (Yürütme: Ben, Erişim: Herkes) → Dağıt, izinleri onaylayın.
 * 4. "…/exec" ile biten URL'yi config.js içindeki FORM_ENDPOINT değerine yazın.
 * Kod güncellenince: Dağıt → Dağıtımları yönet → kalem → Sürüm: Yeni sürüm → Dağıt (URL değişmez).
 *
 * Kayıtlar ayrı bir "Web Sitesi" sekmesine yazılır; Meta'nın sekmelerine dokunulmaz.
 *
 * Korumalar:
 * - Gizli tuzak alanı (website) doluysa kayıt yazılmaz (bot).
 * - Ad 2–80 karakter, telefon 10–13 hane, e-posta (varsa) geçerli biçimde olmalı.
 * - Aynı telefon 10 dakika içinde tekrar gelirse yazılmaz (çift kayıt / tekrar gönderim).
 * - Bir saatte en fazla 30 kayıt yazılır (toplu sahte gönderime karşı).
 */
const SHEET_NAME = "Web Sitesi";
const HEADERS = ["Tarih", "Ad Soyad", "Telefon", "E-posta", "İşletme", "Sektör", "Hizmet", "Mesaj", "Dil", "Sayfa"];
const DUPLICATE_WINDOW_SEC = 600;   // aynı telefon için 10 dakika
const MAX_PER_HOUR = 30;            // saatlik üst sınır

function doPost(e) {
  const p = (e && e.parameter) || {};
  if (p.website) return ok_();                       // tuzak alanı dolu → bot

  const name = String(p.name || "").trim();
  const phoneDigits = String(p.phone || "").replace(/\D/g, "");
  const email = String(p.email || "").trim();
  if (name.length < 2 || name.length > 80) return ok_();
  if (phoneDigits.length < 10 || phoneDigits.length > 13) return ok_();
  if (email && !/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(email)) return ok_();

  const lock = LockService.getScriptLock();
  if (!lock.tryLock(10000)) return ok_();
  try {
    const cache = CacheService.getScriptCache();

    const dupKey = "tel_" + phoneDigits.slice(-10) + "_" + String(p.service || "").slice(0, 40);
    if (cache.get(dupKey)) return ok_();             // 10 dk içinde aynı kişi, aynı form

    const hourKey = "saat_" + Utilities.formatDate(new Date(), "Europe/Istanbul", "yyyyMMddHH");
    const count = Number(cache.get(hourKey) || 0);
    if (count >= MAX_PER_HOUR) return ok_();          // saatlik sınır aşıldı

    const ss = SpreadsheetApp.getActiveSpreadsheet();
    let sheet = ss.getSheetByName(SHEET_NAME);
    if (!sheet) {
      sheet = ss.insertSheet(SHEET_NAME);
      sheet.appendRow(HEADERS);
      sheet.setFrozenRows(1);
    }
    const clean = v => String(v || "").slice(0, 1000).replace(/^[=+\-@]/, "'$&");
    sheet.appendRow([
      Utilities.formatDate(new Date(), "Europe/Istanbul", "dd.MM.yyyy HH:mm"),
      clean(name), "'" + String(p.phone || "").trim().slice(0, 30), clean(email), clean(p.business), clean(p.sector),
      clean(p.service), clean(p.message), clean(p.language), clean(p.page)
    ]);

    cache.put(dupKey, "1", DUPLICATE_WINDOW_SEC);
    cache.put(hourKey, String(count + 1), 3600);
    return ok_();
  } finally {
    lock.releaseLock();
  }
}

function doGet() {
  return ContentService.createTextOutput("Glorion Digital form endpoint çalışıyor.");
}

function ok_() {
  return ContentService.createTextOutput(JSON.stringify({ ok: true }))
    .setMimeType(ContentService.MimeType.JSON);
}

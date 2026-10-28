/**
 * Glorion Digital — web sitesi formunu Google Sheet'e bağlar.
 *
 * KURULUM (bir kez):
 * 1. Meta formunun bağlı olduğu Google Sheet'i açın.
 * 2. Uzantılar → Apps Script. Açılan editördeki kodu silip bu dosyanın tamamını yapıştırın, kaydedin.
 * 3. Sağ üstte Dağıt (Deploy) → Yeni dağıtım → tür: Web uygulaması.
 *      Yürütme yetkisi: Ben (kendi hesabınız)
 *      Erişimi olanlar: Herkes
 *    Dağıt'a basın, Google izin isterse onaylayın.
 * 4. Verilen "Web uygulaması URL'si"ni (…/exec ile biter) kopyalayıp gönderin;
 *    sitedeki config.js dosyasında FORM_ENDPOINT değerine yazılacak.
 *
 * Kayıtlar ayrı bir "Web Sitesi" sekmesine yazılır; Meta'nın kendi sekmesine dokunulmaz,
 * böylece Meta entegrasyonu bozulmaz.
 */
const SHEET_NAME = "Web Sitesi";
const HEADERS = ["Tarih", "Ad Soyad", "Telefon", "İşletme", "Sektör", "Hizmet", "Mesaj", "Dil", "Sayfa"];

function doPost(e) {
  const lock = LockService.getScriptLock();
  lock.tryLock(10000);
  try {
    const p = (e && e.parameter) || {};
    if (p.website) return ok_(); // spam trap
    const ss = SpreadsheetApp.getActiveSpreadsheet();
    let sheet = ss.getSheetByName(SHEET_NAME);
    if (!sheet) {
      sheet = ss.insertSheet(SHEET_NAME);
      sheet.appendRow(HEADERS);
      sheet.setFrozenRows(1);
    }
    const clean = v => String(v || "").slice(0, 1000).replace(/^[=+\-@]/, "'$&");
    sheet.appendRow([
      new Date(),
      clean(p.name), clean(p.phone), clean(p.business), clean(p.sector),
      clean(p.service), clean(p.message), clean(p.language), clean(p.page)
    ]);
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

// Site settings.
// FORM_ENDPOINT: Google Apps Script web app URL (see google-sheets-form.gs).
// While empty, the form opens WhatsApp with the filled-in details instead.
const FORM_ENDPOINT = "https://script.google.com/macros/s/AKfycbzhm7PZWrwPoj6eRLsaReF38nsnD5x689AChu7I4f7Aj3G9_mJ-QRBSYKtsG8w0EQTi/exec";
const WHATSAPP_NUMBER = "905434945528";

// Canlı eğitim pop-up'ı için kontenjan bilgisi.
// Boş bırakılırsa pop-up genel "kontenjan sınırlı" mesajını gösterir; sayı yazılırsa "son X kişilik yer" der.
// Lütfen yalnızca gerçek ve güncel sayıyı yazın (yanıltıcı aciliyet reklam mevzuatına aykırıdır).
const EGITIM_KALAN_KONTENJAN = null;   // örnek: 3
const EGITIM_DONEM_BASLANGIC = "";     // örnek: "17 Kasım"

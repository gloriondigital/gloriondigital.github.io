# -*- coding: utf-8 -*-
"""Blog content for gloriondigital.github.io.

To add a post: append a dict to POSTS (newest first is not required — the list is
sorted by date), then run:  python3 tools/build_blog.py

Inline link placeholders (resolved per language):
  [[services|anchor text]]   → homepage services section
  [[training|anchor text]]   → live training section
  [[contact|anchor text]]    → contact / form section
  [[post:<key>|anchor text]] → another post (by key)
"""

POSTS = [
{
  "key": "anaokulu-rehber",
  "date": "2026-11-27",
  "minutes": 6,
  "cat": ("Anaokulları", "Preschools"),
  "related": ["anaokulu", "mesaj-gelmiyor", "one-cikar"],
  "tr": {
    "slug": "anaokulu-reklami-nasil-yapilir",
    "title": "Anaokulu reklamı nasıl yapılır? Adım adım Meta rehberi",
    "desc": "Anaokulu reklamı nasıl yapılır? Meta Reklam Yöneticisi'nde hedef seçimi, okul çevresi lokasyonu, veli kitlesi, kreatif, mesaj akışı ve ölçüm adım adım.",
    "answer": "Anaokulu reklamı yapmak için Meta Reklam Yöneticisi'nde önce sonucu seçin (mesaj veya form), lokasyonu okulun çevresiyle sınırlayın, yaşa ve bölgeye dayalı yetişkin bir veli kitlesi kurun ve gerçek okul görselleriyle iki üç kreatif hazırlayın. Yayından önce gelen mesajlara hızlı dönecek bir akış kurun, ilk haftalarda sonuçları ölçüp bütçeyi işe yarayan reklama kaydırın.",
    "body": """
<p>“Anaokulumuz için reklam vermek istiyoruz ama nereden başlayacağımızı bilmiyoruz.” Bu cümleyi her kayıt döneminde duyuyoruz. Bu yazıda bir anaokulu reklamını Meta Reklam Yöneticisi'nde sıfırdan nasıl kurduğumuzu adım adım anlatıyoruz. Stratejinin genel çerçevesini merak ediyorsanız önce [[post:anaokulu|anaokulu reklamlarında doğru veliye ulaşmanın 4 kuralı]] yazımıza göz atabilirsiniz; burada işin uygulama tarafına odaklanıyoruz.</p>
<h2>Reklama başlamadan önce neler hazır olmalı?</h2>
<p>Kurulumdan önce üç konuyu netleştirmek, sonradan bütçe kaybını önler:</p>
<ul>
<li><strong>Hesaplar:</strong> Okulun Facebook sayfası ve İnstagram hesabı aynı Meta işletme hesabına bağlı olmalı, reklam hesabında ödeme yöntemi tanımlı olmalı. Mesajları WhatsApp'tan almak istiyorsanız WhatsApp Business numaranızı da sayfanıza bağlayın.</li>
<li><strong>Teklif:</strong> “Kayıtlarımız başladı” tek başına zayıf bir mesajdır. Tanışma ziyareti, deneme günü ya da açık kapı etkinliği gibi velinin bugün atabileceği somut bir adım belirleyin.</li>
<li><strong>Cevap planı:</strong> Gelen mesajlara kim, hangi saatlerde dönecek? Reklamı bu soru cevaplanmadan açmayın.</li>
</ul>
<h2>Anaokulu reklamı adım adım nasıl kurulur?</h2>
<ol>
<li><strong>Kampanya hedefini seçin.</strong> Velilerin WhatsApp, Messenger ya da İnstagram'dan yazmasını istiyorsanız Etkileşim hedefinde mesaj seçeneğini, bilgi formu toplamak istiyorsanız Potansiyel Müşteri hedefini seçin. Mesaj reklamları, tıklayan kişiyi doğrudan işletmenizle bir sohbete götürür (<a href="https://developers.facebook.com/documentation/ads-commerce/marketing-api/ad-creative/messaging-ads/click-to-messenger" target="_blank" rel="noopener">Meta for Developers</a>); form reklamları ise kişinin bilgi almak için hızlıca kayıt bırakmasını sağlar (<a href="https://www.facebook.com/business/help/761812391313386" target="_blank" rel="noopener">Meta İşletme Yardım Merkezi</a>).</li>
<li><strong>Lokasyonu okulun çevresiyle sınırlayın.</strong> Konumu şehir olarak değil, okul adresine iğne bırakarak seçin. Meta, bir noktanın çevresinde 1 ile 80 kilometre arasında yarıçap tanımlamaya izin verir (<a href="https://developers.facebook.com/docs/marketing-api/audiences/reference/basic-targeting" target="_blank" rel="noopener">Meta for Developers</a>). Çoğu anaokulu için velinin her gün rahatça ulaşabileceği birkaç kilometre yeterlidir; servis güzergâhınız varsa onu da hesaba katın.</li>
<li><strong>Veli kitlesini yaşa ve bölgeye göre kurun.</strong> Okul öncesi çağda çocuğu olan velilerin yaş aralığını kendi kayıt verinize bakarak belirleyin. Ayrıntılı hedeflemedeki “ebeveyn” türü seçeneklere tek başına güvenmeyin: Meta bu listeyi zaman zaman daraltıyor; örneğin hassas konularla ilgili seçenekleri 19 Ocak 2022'den itibaren kaldırdı (<a href="https://developers.facebook.com/blog/post/2021/12/08/updating-metas-detailed-targeting-options/" target="_blank" rel="noopener">Meta for Developers</a>). Advantage+ kitle açıkken Meta, performansı artıracağını öngördüğünde yaş ve cinsiyet önerilerinizin dışına da çıkabilir (<a href="https://www.facebook.com/business/help/273363992030035" target="_blank" rel="noopener">Meta İşletme Yardım Merkezi</a>); bu yüzden asıl sınırı lokasyonla çizin.</li>
<li><strong>Bütçeyi az sayıda reklam setinde toplayın.</strong> Küçük bir bütçeyi beş altı reklam setine bölmek, her birinde yeterli veri birikmesini zorlaştırır. Başlangıçta tek kampanya, tek reklam seti ve birkaç reklamla ilerlemek daha sağlıklıdır.</li>
<li><strong>İki üç kreatif hazırlayın.</strong> Gerçek sınıf fotoğrafları, öğretmenin kendini tanıttığı kısa bir video ve izin alınmış bir veli yorumu stok görsellerden çok daha güven verir. Çocukların yüzünün göründüğü içeriklerde mutlaka velilerden yazılı izin alın.</li>
<li><strong>Metni ve butonu tek bir adıma bağlayın.</strong> İlk satırda okulun yeri ve farkı, ardından teklif, sonra “Mesaj gönderin” ya da “Ziyaret planlayın” gibi tek bir çağrı olsun. Görsel, metin ve buton aynı şeyi söylemeli.</li>
<li><strong>Mesaj akışını hazırlayın.</strong> Otomatik karşılama mesajı, sık sorulan sorulara hazır cevaplar ve “Fiyatınız nedir?” sorusuna ziyaret davetiyle dönen bir şablon hazırlayın. Akış kurulmadan açılan reklamlar sık sık [[post:mesaj-gelmiyor|gösterim alıp mesaj getirmeyen reklamlar]] listesine girer.</li>
<li><strong>Yayına alın ve ilk haftayı izleyin.</strong> İlk günlerde sonuçlar dalgalı olabilir. Bir haftanın sonunda mesaj ya da form başına maliyeti, gelen mesajların kalitesini ve kaç ziyarete dönüştüğünü birlikte değerlendirin.</li>
</ol>
<h2>Mesaj reklamı mı, form reklamı mı?</h2>
<p>İkisi de işe yarar; seçim, okulunuzun veliyle nasıl konuşmak istediğine bağlıdır:</p>
<table>
<thead><tr><th></th><th>Mesaj reklamı</th><th>Form reklamı</th></tr></thead>
<tbody>
<tr><td>Veli ne yapar?</td><td>WhatsApp, Messenger veya İnstagram'dan yazar</td><td>Adını ve telefonunu bırakır</td></tr>
<tr><td>Güçlü yanı</td><td>Anında sohbet, soruları hemen cevaplama</td><td>Kayıtları düzenli bir listede toplama</td></tr>
<tr><td>Dikkat edilecek nokta</td><td>Mesajlara hızlı dönülmeli</td><td>Formu bırakanı kısa sürede aramak gerekir</td></tr>
<tr><td>Kime uygun?</td><td>Mesajlara gün içinde dönebilen okullar</td><td>Telefonla geri dönüş yapan okullar</td></tr>
</tbody>
</table>
<h2>Reklamın işe yarayıp yaramadığını nasıl anlarsınız?</h2>
<p>Gösterim ve beğeni sayısı tek başına bir şey söylemez. Biz anaokulu hesaplarında şu sırayla bakıyoruz: mesaj ya da form başına maliyet, gelen mesajların kaçının gerçek veli olduğu, kaçının ziyarete geldiği ve sonunda kaçının kayıt olduğu. İki görsel veya iki metin arasında kararsızsanız Meta'nın <a href="https://www.facebook.com/business/help/1738164643098669" target="_blank" rel="noopener">A/B testi</a> aracıyla aynı bütçeyi ikiye bölüp hangisinin daha iyi sonuç verdiğini görebilirsiniz.</p>
<h2>“Öne Çıkar” butonu yeterli olur mu?</h2>
<p>Tek bir gönderiyi çevrenizde daha çok kişiye göstermek için yeterli olabilir; ama hedef seçimi, test ve ölçüm seçenekleri sınırlıdır. Kayıt dönemi boyunca düzenli veli mesajı istiyorsanız kurulumu Reklam Yöneticisi'nde yapmanızı öneririz. Farkı [[post:one-cikar|Öne Çıkar ile Reklam Yöneticisi karşılaştırmamızda]] anlattık.</p>
<h2>Google Ads de kullanmalı mıyım?</h2>
<p>Meta reklamları, henüz okul aramaya başlamamış velilere sizi tanıtır. Google Arama reklamları ise “yakınımdaki anaokulu” gibi aramaları yapan veliyi yakalar; orada da hedef bölgeyi konum ayarıyla sınırlayabilirsiniz (<a href="https://support.google.com/google-ads/answer/1722043?hl=tr" target="_blank" rel="noopener">Google Ads Yardım</a>). Bütçeniz sınırlıysa önce bir kanalı doğru kurup ölçmek, iki kanala yarım yamalak başlamaktan daha verimlidir.</p>
<h2>Bu kurulumu kim yapmalı?</h2>
<p>Okulunuzda reklamlara düzenli zaman ayırabilecek biri varsa bu adımları kendiniz uygulayabilirsiniz; [[training|canlı Meta reklam eğitimimizde]] kurulumu kendi hesabınızda, eğitmenle birlikte yapıyoruz. Bu işi tamamen devretmek isterseniz [[services|anaokulları için Meta reklam yönetimi]] hizmetimizle hesabınızı birlikte değerlendirebiliriz.</p>
""",
    "faq": [
      ("Anaokulu reklamı için hangi kampanya hedefi seçilmeli?", "Velilerin yazmasını istiyorsanız Etkileşim hedefinde mesaj seçeneğini, bilgi formu toplamak istiyorsanız Potansiyel Müşteri hedefini seçin. Bilinirlik hedefi mesaj veya form için optimize etmez."),
      ("Anaokulu reklamında lokasyon yarıçapı ne kadar olmalı?", "Meta 1 ile 80 kilometre arasında yarıçap tanımlamaya izin verir. Çoğu anaokulu için velinin her gün ulaşabileceği birkaç kilometre yeterlidir; servis güzergâhı varsa ona göre genişletilebilir."),
      ("Anaokulu reklamında çocuk fotoğrafı kullanılabilir mi?", "Çocukların yüzünün göründüğü her içerik için velilerden yazılı izin alınmalıdır. İzin yoksa sınıf ortamı, öğretmen tanıtımı ve etkinlik detayları gibi yüz göstermeyen içerikler tercih edilmelidir."),
      ("Anaokulu reklamına ne zaman başlamalı?", "Kayıt döneminden birkaç hafta önce tanıtım içerikleriyle başlayıp kayıt döneminde mesaj ve form kampanyalarına ağırlık vermek, bütçeyi son haftaya sıkıştırmaktan daha verimlidir."),
    ],
  },
  "en": {
    "slug": "how-to-advertise-to-parents",
    "title": "How to advertise to parents: a preschool Meta ads guide",
    "desc": "How to advertise to parents with Meta ads: choose the right objective, target the area around your school, build a parent audience and track enrollments.",
    "answer": "To advertise to parents, set up a Meta Ads Manager campaign optimized for messages or leads, limit the location to a radius around your school, build an adult audience by age and area rather than relying on “parent” interests, and run two or three ads with real school photos and video. Make sure someone answers messages quickly, then shift budget to the ad that brings visits.",
    "body": """
<p>“We want to run ads for our preschool, but we don't know where to start.” We hear this every enrollment season. This guide walks through how we set up school advertising to parents in Meta Ads Manager, step by step. If you want the bigger picture first, read our [[post:anaokulu|4 rules for reaching the right parents with preschool ads]]; here we focus on the hands-on setup.</p>
<h2>What should be ready before you advertise to parents?</h2>
<p>Sorting out three things before launch saves budget later:</p>
<ul>
<li><strong>Accounts:</strong> your school's Facebook Page and Instagram account connected to the same Meta business account, with a payment method on the ad account. If you want messages on WhatsApp, connect your WhatsApp Business number to the Page too.</li>
<li><strong>Offer:</strong> “Enrollment is open” is a weak message on its own. Give parents a concrete next step: a school tour, a trial day or an open house.</li>
<li><strong>Reply plan:</strong> who answers messages, and when? Don't launch until you know.</li>
</ul>
<h2>How do you set up ads for parents, step by step?</h2>
<ol>
<li><strong>Choose the objective.</strong> If you want parents to write to you on WhatsApp, Messenger or Instagram, use the Engagement objective with messages; to collect inquiry forms, use Leads. Messaging ads take the person who clicks straight into a conversation with your business (<a href="https://developers.facebook.com/documentation/ads-commerce/marketing-api/ad-creative/messaging-ads/click-to-messenger" target="_blank" rel="noopener">Meta for Developers</a>), while lead ads let people sign up for information in a few taps (<a href="https://www.facebook.com/business/help/761812391313386" target="_blank" rel="noopener">Meta Business Help Center</a>).</li>
<li><strong>Limit the location to your school's area.</strong> Drop a pin on your school's address instead of choosing a whole city. Meta lets you set a radius of 1 to 80 kilometers (0.63 to 50 miles) around a point (<a href="https://developers.facebook.com/docs/marketing-api/audiences/reference/basic-targeting" target="_blank" rel="noopener">Meta for Developers</a>). For most preschools, the few kilometers parents can travel daily is enough; widen it only if you run a bus route.</li>
<li><strong>Target parents by age and area, not fragile interests.</strong> Use your own enrollment data to choose the age range of parents with preschool-age children. Don't rely on “parent” detailed targeting options alone: Meta trims that list from time to time, for example removing options tied to sensitive topics from January 19, 2022 (<a href="https://developers.facebook.com/blog/post/2021/12/08/updating-metas-detailed-targeting-options/" target="_blank" rel="noopener">Meta for Developers</a>). With Advantage+ audience on, Meta may also go beyond your age and gender suggestions when it expects better performance (<a href="https://www.facebook.com/business/help/273363992030035" target="_blank" rel="noopener">Meta Business Help Center</a>), so let location do the real limiting.</li>
<li><strong>Keep the budget in few ad sets.</strong> Splitting a small budget across five or six ad sets makes it hard for any of them to gather enough data. Start with one campaign, one ad set and a few ads.</li>
<li><strong>Prepare two or three creatives.</strong> Real classroom photos, a short video of a teacher introducing herself and a parent review (shared with permission) build far more trust than stock images. Get written consent from parents for any content showing children's faces.</li>
<li><strong>Tie copy and button to one action.</strong> Lead with where the school is and what makes it different, then the offer, then a single call to action such as “Send message” or “Book a visit”.</li>
<li><strong>Set up your message flow.</strong> Prepare a greeting, saved replies for common questions and a reply to “What's your price?” that invites parents to visit. Without this, campaigns often end up among [[post:mesaj-gelmiyor|ads that get impressions but no messages]].</li>
<li><strong>Launch and watch the first week.</strong> Early results can swing. After a week, look at cost per message or lead, the quality of conversations and how many turn into visits.</li>
</ol>
<h2>Messaging ads or lead ads?</h2>
<p>Both work; the choice depends on how your school prefers to talk to parents:</p>
<table>
<thead><tr><th></th><th>Messaging ads</th><th>Lead ads</th></tr></thead>
<tbody>
<tr><td>What the parent does</td><td>Writes on WhatsApp, Messenger or Instagram</td><td>Leaves a name and phone number</td></tr>
<tr><td>Strength</td><td>Instant conversation, quick answers</td><td>Inquiries collected in one tidy list</td></tr>
<tr><td>Watch out for</td><td>Replies must be fast</td><td>Call people back promptly</td></tr>
<tr><td>Best for</td><td>Schools that can reply during the day</td><td>Schools that follow up by phone</td></tr>
</tbody>
</table>
<h2>How do you know if your parent advertising works?</h2>
<p>Impressions and likes alone say little. In preschool accounts we look, in order, at cost per message or lead, how many conversations are real parents, how many book a visit and how many enroll. Torn between two images or two headlines? Meta's <a href="https://www.facebook.com/business/help/1738164643098669" target="_blank" rel="noopener">A/B testing</a> splits the same budget so you can see which performs better.</p>
<h2>Is the Boost button enough?</h2>
<p>It can be enough to show one post to more people nearby, but its objective, testing and measurement options are limited. For steady messages from parents across enrollment season, we recommend setting up in Ads Manager. We explain the difference in [[post:one-cikar|Boost post vs Ads Manager]].</p>
<h2>Should preschools use Google Ads too?</h2>
<p>Meta ads introduce your school to parents who haven't started searching yet. Google Ads for preschools catch parents who are already searching for things like “preschool near me”, and you can restrict them to your area with location targeting as well (<a href="https://support.google.com/google-ads/answer/1722043?hl=en" target="_blank" rel="noopener">Google Ads Help</a>). On a tight budget, setting up and measuring one channel properly beats starting two halfway.</p>
<h2>Who should run the setup?</h2>
<p>If someone at your school can give ads regular attention, you can follow these steps yourself; in our [[training|live Meta ads training]] we build the campaign on your own account with an instructor. If you'd rather hand it off, our [[services|Meta ads management for preschools]] starts with a review of your account.</p>
""",
    "faq": [
      ("What's the best Meta ad objective for advertising to parents?", "Use Engagement with messages if you want parents to write to you, or Leads to collect inquiry forms. The Awareness objective does not optimize for messages or forms."),
      ("What radius should a preschool use when targeting parents with ads?", "Meta allows a radius of 1 to 80 km (0.63 to 50 miles). For most preschools, the few kilometers parents can travel daily is enough; widen it only if you offer transport."),
      ("Can I use photos of children in preschool ads?", "Only with written consent from parents for any content showing children's faces. Without it, use classroom spaces, teacher introductions and activity details that don't show faces."),
      ("When should a preschool start advertising to parents?", "Start a few weeks before enrollment season with introductory content, then shift to message and lead campaigns during enrollment rather than squeezing the budget into the final week."),
    ],
  },
},
{
  "key": "mesaj-gelmiyor",
  "date": "2026-10-28",
  "minutes": 4,
  "cat": ("Meta Reklamları", "Meta Ads"),
  "related": ["one-cikar", "anaokulu"],
  "tr": {
    "slug": "reklam-gosterim-aliyor-mesaj-gelmiyor",
    "title": "Reklamınız gösterim alıyor ama mesaj gelmiyor mu? 5 olası sebep",
    "desc": "Meta reklamlarında yüksek gösterime rağmen mesaj gelmemesinin en yaygın 5 sebebi: yanlış kampanya hedefi, geniş kitle, net olmayan teklif, kreatif kopukluğu ve geç dönüş.",
    "answer": "Meta reklamınız çok gösterim alıp mesaj getirmiyorsa sorun çoğu zaman bütçe değil kurgudur. En sık 5 sebep: kampanya hedefinin “Mesajlar” yerine bilinirlik ya da etkileşim seçilmesi, gereksiz geniş kitle, net olmayan teklif, görselle metnin farklı şeyler anlatması ve gelen mesajlara geç dönülmesi.",
    "body": """
<p>Reklam panelinde binlerce gösterim görüyorsunuz ama telefon çalmıyor, DM kutusu sessiz. Bu tabloyu neredeyse her yeni hesapta görüyoruz. İyi haber şu: sorun genellikle bütçede değil, [[services|Meta reklam]] kurgusunun bir halkasında.</p>
<h2>1. Kampanya hedefi doğru mu?</h2>
<p>“Bilinirlik” ya da “Etkileşim” hedefiyle açılan bir reklam, Meta'ya “beni çok kişiye göster” der. Mesaj istiyorsanız hedefi <strong>Etkileşim → Mesajlar</strong> veya <strong>Potansiyel Müşteri</strong> olarak seçmelisiniz. Meta, seçtiğiniz eylemi yapma ihtimali yüksek kişileri arar. Bu fark, [[post:one-cikar|Öne Çıkar ile Reklam Yöneticisi]] arasındaki farkın da temelidir.</p>
<h2>2. Kitle çok mu geniş?</h2>
<p>Yerel bir işletmeyseniz tüm şehre değil, gerçekten hizmet verdiğiniz bölgeye reklam vermelisiniz. Gereksiz geniş bir lokasyon ucuz ama ilgisiz gösterim demektir. Bu kuralın en net görüldüğü alan [[post:anaokulu|anaokulu reklamları]]dır.</p>
<h2>3. Teklifiniz net mi?</h2>
<p>“Kaliteli hizmet” bir teklif değildir. Kullanıcı reklama baktığında üç saniyede şunu anlamalı: Ne kazanacağım ve neden şimdi yazmalıyım? [[contact|Ücretsiz ön görüşme]], sınırlı kontenjan ya da net bir fiyat aralığı bu soruya cevap verir.</p>
<h2>4. Görsel ve metin aynı şeyi mi anlatıyor?</h2>
<p>Görsel bir şey vaat edip metin başka bir şey anlatıyorsa kullanıcı kaydırıp geçer. Görsel, başlık ve metin tek bir fikri anlatmalı.</p>
<h2>5. Gelen mesajlara ne kadar hızlı dönüyorsunuz?</h2>
<p>Reklam işini yaptıysa top artık sizdedir. Saatler sonra dönülen bir mesaj çoğu zaman kaybedilmiş bir müşteridir. Otomatik karşılama mesajı ve hazır cevaplar bu açığı kapatır.</p>
<h2>Önce neyi kontrol etmeli?</h2>
<p>Sırasıyla hedefi, kitleyi ve teklifi kontrol edin. Hangisinin aksadığından emin değilseniz hesabınıza birlikte bakabiliriz; kendi hesabınızda öğrenmek isterseniz [[training|canlı Meta reklam eğitimimiz]] tam bu sorular üzerine kurulu.</p>
""",
    "faq": [
      ("Meta reklamında mesaj almak için hangi kampanya hedefi seçilmeli?", "Mesaj almak için Etkileşim hedefi altında Mesajlar seçeneği, form toplamak için Potansiyel Müşteri hedefi seçilmelidir. Bilinirlik hedefi mesaj için optimize etmez."),
      ("Reklam çok gösterim alıyor ama tıklama yoksa ne yapmalıyım?", "Önce kitlenin hizmet verdiğiniz bölge ve profille uyumlu olduğunu, ardından teklifin ve görselin ilk üç saniyede anlaşılır olduğunu kontrol edin."),
    ],
  },
  "en": {
    "slug": "ad-gets-impressions-but-no-messages",
    "title": "Meta ad gets impressions but no messages? 5 fixes",
    "desc": "Facebook or Instagram ad getting impressions but no messages or clicks? Check these 5 causes in order: objective, audience, offer, creative and reply speed.",
    "answer": "If your Meta ad gets lots of impressions but no messages, the problem is usually the setup, not the budget. The 5 most common causes: choosing awareness or engagement instead of the Messages objective, an oversized audience, an unclear offer, visuals and copy saying different things, and replying to messages too slowly.",
    "body": """
<p>You see thousands of impressions in Ads Manager, yet the phone stays quiet and your DMs are empty. We see this in almost every new account. The good news: the problem is usually not the budget, but one link in your [[services|Meta ads]] setup.</p>
<h2>1. Is the campaign objective right?</h2>
<p>An ad running on “Awareness” or “Engagement” tells Meta “show me to lots of people”. If you want messages, choose <strong>Engagement → Messages</strong> or <strong>Leads</strong>. Meta then looks for people likely to take that action. This is also the core of the difference between [[post:one-cikar|Boost and Ads Manager]].</p>
<h2>2. Is the audience too broad?</h2>
<p>If you're a local business, advertise to the area you actually serve, not the whole city. An oversized location means cheap but irrelevant impressions. Nowhere is this clearer than in [[post:anaokulu|preschool ads]].</p>
<h2>3. Is your offer clear?</h2>
<p>“Quality service” is not an offer. Within three seconds people should know what they get and why they should message now. A [[contact|free consultation]], limited spots or a clear price range answers that.</p>
<h2>4. Do the visual and the copy say the same thing?</h2>
<p>If the visual promises one thing and the text says another, people scroll past. Image, headline and copy should tell one single idea.</p>
<h2>5. How fast do you reply?</h2>
<p>Once the ad has done its job, the ball is in your court. A message answered hours later is often a lost customer. An automatic greeting and saved replies close that gap.</p>
<h2>What should you check first?</h2>
<p>Check the objective, then the audience, then the offer. Not sure which one is off? We can look at your account together — or learn it on your own account in our [[training|live Meta ads training]], built around exactly these questions.</p>
""",
    "faq": [
      ("Which campaign objective should I use to get messages from Meta ads?", "Use Engagement with the Messages option to get messages, or the Leads objective to collect forms. The Awareness objective does not optimize for messages."),
      ("My ad gets impressions but no clicks — what should I do?", "First check that the audience matches the area and profile you serve, then make sure the offer and visual are clear within the first three seconds."),
    ],
  },
},
{
  "key": "one-cikar",
  "date": "2026-10-21",
  "minutes": 3,
  "cat": ("Başlangıç", "Basics"),
  "related": ["mesaj-gelmiyor", "anaokulu"],
  "tr": {
    "slug": "one-cikar-mi-reklam-yoneticisi-mi",
    "title": "“Öne Çıkar” mı, Reklam Yöneticisi mi? Farkı ve doğru seçim",
    "desc": "Instagram'daki Öne Çıkar butonu ile Meta Reklam Yöneticisi arasındaki fark: hedefleme, test, ölçüm ve hangisinin ne zaman kullanılacağı.",
    "answer": "Öne Çıkar, mevcut bir gönderiyi birkaç dokunuşla reklama çeviren hızlı ama sınırlı bir araçtır. Meta Reklam Yöneticisi ise kampanya hedefi, kitle, test ve dönüşüm ölçümü üzerinde tam kontrol verir. Tek bir gönderiyi hızlıca yaymak için Öne Çıkar yeterli olabilir; düzenli mesaj, kayıt veya satış hedefliyorsanız doğru kurulmuş Reklam Yöneticisi her zaman daha verimlidir.",
    "body": """
<p>“Öne Çıkar yaptığımda mesaj geliyordu, şimdi reklam veriyoruz ama kimse yazmıyor.” Bu cümleyi işletme sahiplerinden çok sık duyuyoruz. Asıl mesele butonun kendisi değil, arkasındaki [[services|reklam kurgusu]].</p>
<h2>Öne Çıkar nedir?</h2>
<p>Mevcut bir gönderiyi birkaç dokunuşla reklama çeviren hızlı bir araçtır. Kolaydır ama hedefleme, yerleşim ve ölçüm seçenekleri sınırlıdır.</p>
<h2>Reklam Yöneticisi neyi farklı yapar?</h2>
<ul>
<li><strong>Doğru hedef:</strong> Mesaj, form veya satış gibi net bir sonuç için optimize edersiniz.</li>
<li><strong>Kitle kontrolü:</strong> Lokasyon, ilgi alanı, benzer kitle ve yeniden hedefleme kullanırsınız.</li>
<li><strong>Test:</strong> Farklı görsel ve metinleri aynı anda deneyip kazananı bulursunuz.</li>
<li><strong>Ölçüm:</strong> Piksel ve dönüşüm takibiyle reklamın gerçekten ne getirdiğini görürsünüz.</li>
</ul>
<h2>Reklam Yöneticisi'ne geçince sonuçlar neden düşer?</h2>
<p>Reklam Yöneticisi güçlüdür ama yanlış kurulursa Öne Çıkar'dan bile kötü sonuç verebilir. Yanlış hedef, gereksiz geniş kitle ya da çok küçük parçalara bölünmüş bütçe en yaygın sebeplerdir. Ayrıntıları [[post:mesaj-gelmiyor|mesaj gelmeyen reklamların 5 sebebi]] yazısında anlattık.</p>
<h2>Hangisini seçmeli?</h2>
<p>Tek bir gönderiyi hızlıca daha çok kişiye göstermek istiyorsanız Öne Çıkar yeterli olabilir. Düzenli mesaj, kayıt ya da satış hedefliyorsanız Reklam Yöneticisi'ni doğru kurgulamak uzun vadede her zaman daha verimlidir. Kurulumu kendiniz yapmak isterseniz [[training|canlı eğitimde]] kendi hesabınız üzerinde birlikte kuruyoruz.</p>
""",
    "faq": [
      ("Öne Çıkar ile reklam vermek aynı şey mi?", "Hayır. Öne Çıkar da bir reklamdır ama hedefleme, test ve ölçüm seçenekleri Reklam Yöneticisi'ne göre çok sınırlıdır."),
      ("Küçük bir işletme Reklam Yöneticisi kullanmalı mı?", "Düzenli müşteri hedefliyorsa evet. Küçük bütçede bile doğru hedef ve dar bir kitleyle Reklam Yöneticisi daha verimli sonuç verir."),
    ],
  },
  "en": {
    "slug": "boost-or-ads-manager",
    "title": "Boost post vs Ads Manager: which gets better results?",
    "desc": "Boost post or Meta Ads Manager? Compare objectives, targeting, testing and tracking, and see when boosting a Facebook or Instagram post is enough.",
    "answer": "Boost turns an existing post into an ad in a few taps — fast but limited. Meta Ads Manager gives full control over the campaign objective, audience, testing and conversion tracking. Boost can be enough to quickly spread one post; if you want steady messages, sign-ups or sales, a well-built Ads Manager setup is always more efficient.",
    "body": """
<p>“We got messages when we boosted posts, but now that we run ads nobody writes.” We hear this from business owners all the time. The issue isn't the button itself, it's the [[services|ad setup]] behind it.</p>
<h2>What is Boost?</h2>
<p>A quick tool that turns an existing post into an ad in a few taps. It's easy, but its targeting, placement and measurement options are limited.</p>
<h2>What does Ads Manager do differently?</h2>
<ul>
<li><strong>The right objective:</strong> optimize for a clear result like messages, leads or sales.</li>
<li><strong>Audience control:</strong> use location, interests, lookalikes and retargeting.</li>
<li><strong>Testing:</strong> try different images and copy at once and find the winner.</li>
<li><strong>Measurement:</strong> with the pixel and conversion tracking you see what the ad really brings in.</li>
</ul>
<h2>Why do results drop after switching to Ads Manager?</h2>
<p>Ads Manager is powerful, but set up wrong it can perform worse than Boost. A wrong objective, an oversized audience or budgets split too thin are the usual causes. We cover them in [[post:mesaj-gelmiyor|5 reasons your ad gets no messages]].</p>
<h2>Which one should you choose?</h2>
<p>To quickly show one post to more people, Boost may be enough. If you want steady messages, sign-ups or sales, a well-built Ads Manager setup is always more efficient in the long run. Want to set it up yourself? In our [[training|live training]] we build it together on your own account.</p>
""",
    "faq": [
      ("Is boosting a post the same as running an ad?", "No. Boost is an ad too, but its targeting, testing and measurement options are far more limited than Ads Manager."),
      ("Should a small business use Ads Manager?", "Yes, if it wants steady customers. Even on a small budget, the right objective and a focused audience make Ads Manager more efficient."),
    ],
  },
},
{
  "key": "anaokulu",
  "date": "2026-10-14",
  "minutes": 4,
  "cat": ("Anaokulları", "Preschools"),
  "related": ["anaokulu-rehber", "mesaj-gelmiyor", "one-cikar"],
  "tr": {
    "slug": "anaokulu-reklamlari-dogru-veliye-ulasmak",
    "title": "Anaokulu reklamlarında doğru veliye ulaşmanın 4 kuralı",
    "desc": "Anaokulu Meta reklamlarında görüntülenmeyi kayda çevirmek için 4 kural: dar lokasyon, güven veren içerik, fiyat sorusuna doğru cevap ve doğru zamanlanmış bütçe.",
    "answer": "Anaokulu reklamlarında kayıt getirmenin 4 kuralı: okulun çevresinde dar bir lokasyon seçmek, gerçek sınıf ve öğretmen içerikleriyle güven vermek, “fiyatınız nedir?” sorusuna sadece rakamla değil okulun farkı ve ziyaret davetiyle cevap vermek, bütçeyi kayıt döneminden önce ve kayıt döneminde doğru dağıtmak.",
    "body": """
<p>Anaokulu reklamlarında yüksek görüntülenme her zaman yüksek kayıt anlamına gelmez. Bir veli, çocuğunu emanet edeceği okulu seçerken yalnızca etkinliklere veya fiyata bakmaz; önce güven arar. Anaokulları için yürüttüğümüz [[services|Meta reklam yönetiminde]] en çok şu dört kurala dikkat ediyoruz.</p>
<h2>1. Lokasyonu neden daraltmalısınız?</h2>
<p>Veliler çoğunlukla evlerine ya da iş yerlerine yakın okul tercih eder. Okulunuzun çevresinde makul bir yarıçap seçin; şehrin öbür ucundaki gösterimler bütçenizi boşa harcar. Bu, [[post:mesaj-gelmiyor|mesaj gelmeyen reklamların]] en yaygın sebeplerinden biridir.</p>
<h2>2. Güveni nasıl öne çıkarırsınız?</h2>
<p>Gerçek sınıf fotoğrafları, öğretmen tanıtımları, güvenlik önlemleri ve veli yorumları stok görsellerden çok daha fazla mesaj getirir. Veli, okulun içini görmek ister.</p>
<h2>3. “Fiyatınız nedir?” sorusuna nasıl cevap vermeli?</h2>
<p>Fiyat soran veli bir daha yazmıyorsa sorun her zaman fiyatın yüksekliği değildir. Cevabınızda okulunuzun farkını, bir ziyaret davetini ve net bir sonraki adımı verin. Sadece rakam yazmak konuşmayı bitirir.</p>
<h2>4. Bütçeyi ne zaman harcamalı?</h2>
<p>Kayıt döneminden önce bilinirliği artırın, kayıt döneminde mesaj ve form kampanyalarına ağırlık verin. Tüm bütçeyi son haftaya bırakmak hem pahalıdır hem de güven oluşturmaya zaman bırakmaz. Bunun için “Öne Çıkar” yerine [[post:one-cikar|Reklam Yöneticisi]] kullanmak gerekir.</p>
<h2>Sonuç</h2>
<p>Doğru lokasyon, güven veren içerik ve iyi yönetilen mesaj akışı bir araya geldiğinde reklam bütçeniz görüntülenme değil kayıt getirmeye başlar. Kurulumu adım adım görmek isterseniz [[post:anaokulu-rehber|anaokulu reklamı nasıl yapılır rehberimize]] bakabilir, okulunuz için [[contact|ücretsiz ön görüşme]] talep edebilirsiniz.</p>
""",
    "faq": [
      ("Anaokulu reklamı için lokasyon yarıçapı ne kadar olmalı?", "Okulun bulunduğu semte ve ulaşıma göre değişir; genelde velilerin günlük olarak ulaşabileceği birkaç kilometrelik bir alan yeterlidir."),
      ("Anaokulu reklamlarında hangi içerik daha çok mesaj getirir?", "Gerçek sınıf fotoğrafları, öğretmen tanıtımları, güvenlik önlemleri ve veli yorumları stok görsellerden daha fazla güven ve mesaj getirir."),
    ],
  },
  "en": {
    "slug": "preschool-ads-reaching-the-right-parents",
    "title": "4 rules for reaching the right parents with preschool ads",
    "desc": "4 rules to turn preschool Meta ad views into enrollments: a narrow location, trust-building content, the right answer to price questions and well-timed budget.",
    "answer": "The 4 rules for preschool ads that bring enrollments: choose a narrow radius around the school, build trust with real classroom and teacher content, answer “what's your price?” with your difference and a visit invitation rather than just a number, and spread the budget before and during enrollment season.",
    "body": """
<p>In preschool advertising, high views don't always mean high enrollment. When choosing a school for their child, parents don't just look at activities or price; first they look for trust. In our [[services|Meta ads management]] for preschools, these are the four rules we focus on most.</p>
<h2>1. Why narrow the location?</h2>
<p>Parents mostly prefer schools close to home or work. Pick a sensible radius around your school; impressions on the other side of the city waste your budget. It's one of the most common reasons [[post:mesaj-gelmiyor|ads get no messages]].</p>
<h2>2. How do you put trust first?</h2>
<p>Real classroom photos, teacher introductions, safety measures and parent reviews bring far more messages than stock images. Parents want to see inside the school.</p>
<h2>3. How should you answer “What's your price?”</h2>
<p>If a parent who asked about price never writes back, the price isn't always too high. In your reply, give your school's difference, an invitation to visit and a clear next step. Just sending a number ends the conversation.</p>
<h2>4. When should you spend the budget?</h2>
<p>Build awareness before enrollment season, then focus on message and lead campaigns during it. Leaving the whole budget for the last week is expensive and leaves no time to build trust. This requires [[post:one-cikar|Ads Manager]] rather than Boost.</p>
<h2>The result</h2>
<p>When the right location, trust-building content and a well-managed message flow come together, your budget starts bringing enrollments instead of just views. For the hands-on setup, see our step-by-step guide on [[post:anaokulu-rehber|how to advertise to parents]], or request a [[contact|free consultation]] for your school.</p>
""",
    "faq": [
      ("What location radius should a preschool ad use?", "It depends on the neighborhood and transport, but generally a few kilometers that parents can reach daily is enough."),
      ("What content brings the most messages in preschool ads?", "Real classroom photos, teacher introductions, safety measures and parent reviews build more trust and bring more messages than stock images."),
    ],
  },
},
]

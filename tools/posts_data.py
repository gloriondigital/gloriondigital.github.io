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
    "title": "Your ad gets impressions but no messages? 5 likely reasons",
    "desc": "The 5 most common reasons Meta ads get impressions but no messages: wrong campaign objective, broad audience, unclear offer, mismatched creative and slow replies.",
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
    "title": "“Boost” or Ads Manager? The difference and the right choice",
    "desc": "The difference between Instagram's Boost button and Meta Ads Manager: targeting, testing, measurement and when to use which.",
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
  "related": ["mesaj-gelmiyor", "one-cikar"],
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
<p>Doğru lokasyon, güven veren içerik ve iyi yönetilen mesaj akışı bir araya geldiğinde reklam bütçeniz görüntülenme değil kayıt getirmeye başlar. Okulunuz için [[contact|ücretsiz ön görüşme]] talep edebilirsiniz.</p>
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
<p>When the right location, trust-building content and a well-managed message flow come together, your budget starts bringing enrollments instead of just views. You can request a [[contact|free consultation]] for your school.</p>
""",
    "faq": [
      ("What location radius should a preschool ad use?", "It depends on the neighborhood and transport, but generally a few kilometers that parents can reach daily is enough."),
      ("What content brings the most messages in preschool ads?", "Real classroom photos, teacher introductions, safety measures and parent reviews build more trust and bring more messages than stock images."),
    ],
  },
},
]

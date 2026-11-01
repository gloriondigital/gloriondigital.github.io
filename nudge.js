/* Glorion Digital — site ici mesajlar (her sayfada iki tur):
   1) Kayan kutu: sayfanin yarisina (blogda yazinin %60'ina) inince, tum cihazlarda.
   2) Cikis mesaji: bilgisayarda fare tarayicinin ustune cikinca, mobilde hizli yukari kaydirinca
      (sayfada en az 10 sn sonra).
   Her tur oturum basina bir kez; kapatilan tur 7 gun gosterilmez; kutudan tiklayana cikis mesaji
   gosterilmez; form gonderene hicbiri gosterilmez. Cerez cubugu acikken mesaj beklenir. */
(function () {
  var path = location.pathname;
  if (/^\/(kvkk|en\/privacy|yorum)\//.test(path)) return;

  function get(k) { try { return localStorage.getItem(k); } catch (e) { return null; } }
  function set(k, v) { try { localStorage.setItem(k, v); } catch (e) {} }
  function sget(k) { try { return sessionStorage.getItem(k); } catch (e) { return null; } }
  function sset(k, v) { try { sessionStorage.setItem(k, v); } catch (e) {} }

  var params; try { params = new URLSearchParams(location.search); } catch (e) { params = null; }

  // Mesajdan gelindiyse ana sayfadaki formda hizmet / sektoru onceden sec
  var SERVICE = { yonetim: 'Meta Reklam Yönetimi', eticaret: 'E-Ticaret Büyüme', egitim: 'Canlı Meta Reklam Eğitimi' };
  var SECTOR = { anaokulu: 'Anaokulu', eticaret: 'E-ticaret' };
  var lead = document.getElementById('leadForm');
  if (lead && params) {
    var sv = SERVICE[params.get('hizmet')], sc = SECTOR[params.get('sektor')];
    if (sv && lead.service) lead.service.value = sv;
    if (sc && lead.sector) lead.sector.value = sc;
  }
  // Form gonderenlere bir daha mesaj gosterme
  ['leadForm', 'pdfForm'].forEach(function (id) {
    var f = document.getElementById(id);
    if (f) f.addEventListener('submit', function () { if (!f.checkValidity || f.checkValidity()) set('gd_basvurdu', '1'); });
  });

  if (get('gd_basvurdu') === '1') return;

  var WEEK = 7 * 24 * 3600 * 1000;
  function allowed(kind) {
    var closedAt = parseInt(get('gd_nudge_kapandi_' + kind) || '0', 10);
    if (closedAt && Date.now() - closedAt < WEEK) return false;
    if (sget('gd_nudge_goruldu_' + kind) === '1') return false;
    if (kind === 'cikis' && sget('gd_nudge_tiklandi') === '1') return false;
    if (kind === 'kutu' && sget('gd_nudge_goruldu_egitim') === '1') return false;
    if (kind === 'egitim' && sget('gd_nudge_goruldu_kutu') === '1') return false;
    return true;
  }
  function cookieBarOpen() { return !!document.querySelector('.cookie-bar'); }

  var isPost = !!document.querySelector('.prose') && /\/blog\/[^\/]+\/$/.test(path);
  var preschool = /anaokulu|preschool/.test(path);
  var onHome = !!lead;
  var svcEl = document.querySelector('main[data-service]');
  var svc = svcEl ? svcEl.getAttribute('data-service') : '';

  // Metinler (TR + EN; ana sayfada dil gecisiyle birlikte degisir)
  var T = {
    home: {
      k: ['Ücretsiz ön görüşme', 'Free consultation'],
      h: ['Reklamlarınız neden satış getirmiyor?', 'Why aren’t your ads bringing sales?'],
      p: ['Reklam hesabınızı birlikte inceleyip sorunun kaynağını gösterelim. Ön görüşme ücretsiz.', 'Let’s review your ad account together and show you where the problem is. The first consultation is free.'],
      c: ['Ücretsiz görüşme al', 'Get a free consultation'],
      q: 'hizmet=yonetim'
    },
    post: {
      k: ['Ücretsiz ön görüşme', 'Free consultation'],
      h: ['Reklam hesabınıza birlikte bakalım.', 'Let’s look at your ad account together.'],
      p: ['Hangi reklamın para yaktığını, neyin düzeltilmesi gerektiğini ön görüşmede net olarak gösterelim.', 'In a free consultation we show you which ads waste money and what needs fixing.'],
      c: ['Ücretsiz görüşme al', 'Get a free consultation'],
      q: 'hizmet=yonetim'
    },
    preschool: {
      k: ['Anaokulları için', 'For preschools'],
      h: ['Kayıt getiren reklamları birlikte kuralım.', 'Let’s build ads that bring enrollments.'],
      p: ['Doğru lokasyondaki velilere ulaşan kampanya için ücretsiz ön görüşme alın.', 'Get a free consultation for campaigns that reach the right parents nearby.'],
      c: ['Ücretsiz görüşme al', 'Get a free consultation'],
      q: 'hizmet=yonetim&sektor=anaokulu'
    },
    exit: {
      k: ['Gitmeden önce', 'Before you go'],
      h: ['Canlı Meta Reklam Eğitimi’nde kontenjan sınırlı.', 'Spots in the Live Meta Ads Training are limited.'],
      p: ['10 kişilik sınıflarda, kendi reklam hesabınızda öğrenin. Yerinizi sormak için başvurun.', 'Learn on your own ad account in classes of 10. Apply to ask about a spot.'],
      c: ['Kontenjan sor', 'Ask about a spot'],
      q: 'hizmet=egitim'
    }
  };
  var seats = (typeof EGITIM_KALAN_KONTENJAN === 'number' && EGITIM_KALAN_KONTENJAN > 0) ? EGITIM_KALAN_KONTENJAN : 0;
  var start = (typeof EGITIM_DONEM_BASLANGIC === 'string') ? EGITIM_DONEM_BASLANGIC.trim() : '';
  T.egitim = {
    k: ['Canlı Meta Reklam Eğitimi', 'Live Meta Ads Training'],
    h: seats
      ? ['Bu dönem için son ' + seats + ' kişilik yer.', 'Only ' + seats + (seats === 1 ? ' spot' : ' spots') + ' left this term.']
      : ['Kontenjan sınırlı, yerini kaçırma.', 'Spots are limited — don’t miss yours.'],
    p: [
      'Sınıflar 10 kişiyle sınırlı; eğitmenle canlı, kendi reklam hesabında öğrenirsin.' + (start ? ' Yeni dönem ' + start + '’ta başlıyor.' : ' Yeni dönem başlamadan yerini ayırt.'),
      'Classes are limited to 10; learn live with an instructor on your own ad account.' + (start ? ' The new term starts on ' + start + '.' : ' Save your spot before the new term starts.')
    ],
    c: ['Hemen kayıt ol', 'Enroll now'],
    w: ['WhatsApp’tan yaz', 'Message on WhatsApp'],
    q: 'hizmet=egitim'
  };
  // Egitim pop-up'i gosterildiyse cikis mesaji egitimi tekrarlamasin, on gorusme teklif etsin
  function exitT() { return (sget('gd_nudge_goruldu_egitim') === '1' || (svc && svc !== 'egitim')) ? {
    k: T.exit.k, h: ['Reklamlarınıza ücretsiz bakalım.', 'Let’s review your ads for free.'], p: T.home.p, c: T.home.c, q: T.home.q } : T.exit; }
  T.eticaret = {
    k: ['Ücretsiz mağaza analizi', 'Free store review'],
    h: ['Reklam bütçeniz satışa dönüşüyor mu?', 'Is your ad budget turning into sales?'],
    p: ['Mağazanızın reklam hesabını ve ölçüm altyapısını ücretsiz inceleyelim, kazandıran kampanyayı birlikte bulalım.', 'Let’s review your store’s ad account and tracking for free and find the campaign that makes money.'],
    c: ['Ücretsiz analiz al', 'Get a free review'],
    q: 'hizmet=eticaret&sektor=eticaret'
  };
  var boxT = isPost ? (preschool ? T.preschool : T.post)
    : svc === 'eticaret' ? T.eticaret
    : svc === 'egitim' ? { k: T.egitim.k, h: T.egitim.h, p: T.egitim.p, c: T.egitim.c, w: T.egitim.w, q: T.egitim.q }
    : T.home;

  function lang() { return (document.documentElement.lang || 'tr').indexOf('en') === 0 ? 'en' : 'tr'; }
  function both(pair) { return '<span class="lang-tr">' + pair[0] + '</span><span class="lang-en">' + pair[1] + '</span>'; }

  window.dataLayer = window.dataLayer || [];
  function track(ev, kind) {
    window.dataLayer.push({ event: ev, nudge_type: kind === 'kutu' ? (isPost ? 'blog-kutu' : 'sayfa-kutu') : kind === 'egitim' ? 'egitim-kontenjan' : 'cikis', nudge_category: svc ? 'hizmet-' + svc : isPost ? (preschool ? 'anaokulu' : 'blog') : 'genel' });
  }

  var open = null;
  function closeBox(kind, byUser) {
    if (!open || open.kind !== kind) return;
    var el = open.el; open = null;
    el.classList.remove('is-open');
    if (byUser) { set('gd_nudge_kapandi_' + kind, String(Date.now())); track('nudge_close', kind); }
    setTimeout(function () { if (el.parentNode) el.parentNode.removeChild(el); }, 400);
  }
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && open) closeBox(open.kind, true); });

  function show(kind) {
    if (!allowed(kind) || cookieBarOpen()) return false;
    if (open) closeBox(open.kind, false);
    sset('gd_nudge_goruldu_' + kind, '1');
    var t = kind === 'kutu' ? boxT : kind === 'egitim' ? T.egitim : exitT();
    var src = kind === 'kutu' ? (isPost ? 'blog-kutu' : 'sayfa-kutu') : kind === 'egitim' ? 'egitim-kontenjan' : 'cikis-mesaji';
    var el = document.createElement('aside');
    el.className = 'gd-nudge' + (kind === 'cikis' ? ' is-center' : '') + (kind === 'egitim' ? ' is-urgent' : '');
    el.setAttribute('role', 'dialog');
    el.setAttribute('aria-live', 'polite');
    el.setAttribute('aria-label', t.k[lang() === 'en' ? 1 : 0]);
    el.innerHTML =
      '<button type="button" class="gd-nudge-x" aria-label="Kapat / Close">&times;</button>' +
      '<span class="gd-nudge-k">' + both(t.k) + '</span>' +
      '<p class="gd-nudge-h">' + both(t.h) + '</p>' +
      '<p class="gd-nudge-p">' + both(t.p) + '</p>' +
      '<a class="btn btn-gold btn-block gd-nudge-cta" href="/?' + t.q + '&kaynak=' + src + '#basvuru">' + both(t.c) + '&nbsp;→</a>' +
      (t.w ? '<a class="gd-nudge-wa" target="_blank" rel="noopener" href="https://wa.me/905434945528?text=' + encodeURIComponent('EĞİTİM - Canlı Meta Reklam Eğitimi için kayıt olmak istiyorum.') + '">' + both(t.w) + '</a>' : '');
    document.body.appendChild(el);
    open = { el: el, kind: kind };
    el.querySelector('.gd-nudge-x').addEventListener('click', function () { closeBox(kind, true); });
    var cta = el.querySelector('.gd-nudge-cta');
    cta.addEventListener('click', function (e) {
      sset('gd_nudge_tiklandi', '1');
      track('nudge_click', kind);
      // Ana sayfadaysak sayfa yenilemeden forma kaydir ve secimi yap
      if (onHome) {
        e.preventDefault();
        var q = new URLSearchParams(t.q);
        if (SERVICE[q.get('hizmet')]) lead.service.value = SERVICE[q.get('hizmet')];
        if (SECTOR[q.get('sektor')]) lead.sector.value = SECTOR[q.get('sektor')];
        closeBox(kind, false);
        var target = document.getElementById('basvuru') || lead;
        target.scrollIntoView({ behavior: 'smooth', block: 'start' });
        setTimeout(function () { var n = lead.querySelector('input[name="name"]'); if (n) n.focus({ preventScroll: true }); }, 700);
      }
    });
    requestAnimationFrame(function () { requestAnimationFrame(function () { el.classList.add('is-open'); }); });
    track('nudge_view', kind);
    return true;
  }

  // 0) Egitim kontenjan pop-up'i: ana sayfada egitim bolumu en az 3 sn ekranda kalinca
  var egitimSec = document.getElementById('egitim');
  if (lead && egitimSec && allowed('egitim') && 'IntersectionObserver' in window) {
    var timer = null;
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (x) {
        if (x.isIntersecting) {
          if (!timer) timer = setTimeout(function () { if (show('egitim')) io.disconnect(); timer = null; }, 3000);
        } else if (timer) { clearTimeout(timer); timer = null; }
      });
    }, { threshold: 0.4 });
    io.observe(egitimSec);
  }

  // 1) Kayan kutu
  if (allowed('kutu')) {
    var prose = document.querySelector('.prose');
    var onScroll = function () {
      var reached;
      if (isPost && prose) {
        var r = prose.getBoundingClientRect();
        reached = (window.innerHeight - r.top) / Math.max(1, r.height) >= 0.6;
      } else {
        var d = document.documentElement;
        reached = (window.scrollY + window.innerHeight) / Math.max(1, d.scrollHeight) >= (svc ? 0.35 : 0.5);
      }
      if (reached && show('kutu')) window.removeEventListener('scroll', onScroll);
    };
    window.addEventListener('scroll', onScroll, { passive: true });
  }

  // 2) Cikis mesaji
  if (allowed('cikis')) {
    var fine = window.matchMedia && window.matchMedia('(hover: hover) and (pointer: fine)').matches;
    var ready = false;
    setTimeout(function () { ready = true; }, 10000);
    if (fine) {
      document.addEventListener('mouseout', function (e) {
        if (!ready || (open && open.kind === 'cikis')) return;
        if (!e.relatedTarget && e.clientY <= 0) show('cikis');
      });
    } else {
      var lastY = window.scrollY, lastT = Date.now(), maxY = 0;
      window.addEventListener('scroll', function () {
        var y = window.scrollY, now = Date.now();
        if (y > maxY) maxY = y;
        var dy = lastY - y, dt = Math.max(1, now - lastT);
        if (ready && maxY > window.innerHeight * 1.5 && dy > 0 && dy / dt > 2.5 && !(open && open.kind === 'cikis')) show('cikis');
        lastY = y; lastT = now;
      }, { passive: true });
    }
  }
})();

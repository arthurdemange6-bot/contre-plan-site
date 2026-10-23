/* Éléments interactifs Contre-Plan (fonctionnent avec ou sans animations) */
(function () {
  var COMEUP = 'https://comeup.com/fr/@contreplan';
  var reduce = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
  function each(l, f) { Array.prototype.forEach.call(l, f); }
  function gc(path) { try { if (window.goatcounter && goatcounter.count) goatcounter.count({ path: path, title: path, event: true }); } catch (e) {} }

  /* ---------- Mini-test ---------- */
  function test() {
    var box = document.getElementById('cp-test'); if (!box) return;
    var qs = box.querySelectorAll('.cp-q'), bar = box.querySelector('.cp-test-bar i'), res = box.querySelector('.cp-res'), done = false;
    function update() {
      var answered = 0, issues = [];
      each(qs, function (q) {
        var on = q.querySelector('button[aria-pressed="true"]');
        if (on) { answered++; if (on.getAttribute('data-v') !== 'oui') issues.push(q.getAttribute('data-tip')); }
      });
      bar.style.width = (answered / qs.length * 100) + '%';
      if (answered < qs.length) { res.classList.remove('on'); return; }
      var n = issues.length, h, p;
      if (n === 0) { h = 'Votre devis coche les bases.'; p = 'Bonne nouvelle pour la forme. Reste ce qu\'un test ne peut pas voir : les prix poste par poste, les oublis techniques et l\'enchaînement des travaux.'; }
      else if (n <= 2) { h = n + ' point' + (n > 1 ? 's' : '') + ' à clarifier avant de signer.'; p = 'Rien d\'alarmant en soi, mais à faire préciser par écrit par l\'artisan :'; }
      else { h = n + ' points à vérifier : ne signez pas en l\'état.'; p = 'Ce sont autant de sources de suppléments ou de litiges. À faire préciser par écrit avant de vous engager :'; }
      res.innerHTML = '<h3>' + h + '</h3><p>' + p + '</p>' + (n ? '<ul>' + issues.map(function (t) { return '<li>' + t + '</li>'; }).join('') + '</ul>' : '') +
        '<p>Je peux relire votre devis ligne par ligne et vous dire précisément quoi demander.</p>' +
        '<a class="cp-cta" href="' + COMEUP + '" data-goatcounter-click="clic-comeup-test">Faire analyser mon devis</a>';
      res.classList.add('on');
      if (!done) { done = true; gc('test-devis-termine'); setTimeout(function () { res.scrollIntoView({ behavior: reduce ? 'auto' : 'smooth', block: 'start' }); }, 120); }
    }
    each(qs, function (q) {
      each(q.querySelectorAll('button'), function (b) {
        b.addEventListener('click', function () {
          each(q.querySelectorAll('button'), function (o) { o.setAttribute('aria-pressed', o === b ? 'true' : 'false'); });
          update();
        });
      });
    });
  }

  /* ---------- Avant / après ---------- */
  function slider() {
    var ba = document.getElementById('cp-ba'); if (!ba) return;
    var input = ba.querySelector('input');
    function set(v) { ba.style.setProperty('--x', v + '%'); }
    input.addEventListener('input', function () { set(input.value); });
    set(input.value);
    if (reduce || !('IntersectionObserver' in window)) return;
    var io = new IntersectionObserver(function (en) {
      if (!en[0].isIntersecting) return; io.disconnect();
      var t0 = null, from = 92, to = 50;
      function step(t) { if (!t0) t0 = t; var k = Math.min(1, (t - t0) / 1400), e = 1 - Math.pow(1 - k, 3), v = from + (to - from) * e; set(v); input.value = v; if (k < 1) requestAnimationFrame(step); }
      setTimeout(function () { requestAnimationFrame(step); }, 300);
    }, { threshold: 0.5 });
    set(92); input.value = 92; io.observe(ba);
  }

  /* ---------- Calcul ---------- */
  function calc() {
    var c = document.getElementById('cp-calc'); if (!c) return;
    var input = c.querySelector('input'), out = c.querySelector('.out'), price = parseFloat(c.getAttribute('data-prix'));
    function fmt(v, d) { return v.toLocaleString('fr-FR', { minimumFractionDigits: d, maximumFractionDigits: d }); }
    function upd() {
      var m = parseFloat(String(input.value).replace(/\s/g, '').replace(',', '.'));
      if (!m || m < 100) { out.innerHTML = 'Saisissez le montant TTC de votre devis.'; return; }
      var pct = price / m * 100, ex = m * 0.05;
      out.innerHTML = 'L\'analyse à ' + fmt(price, 2) + '\u00a0€ représente <b>' + fmt(pct, pct < 0.1 ? 2 : 1) + '\u00a0%</b> de votre devis de ' + fmt(m, 0) + '\u00a0€.<br>À titre d\'exemple, un écart de prix de 5\u00a0% sur ce devis représente ' + fmt(ex, 0) + '\u00a0€.';
    }
    input.addEventListener('input', upd); upd();
  }

  /* ---------- Barre mobile ---------- */
  function bar() {
    if (!('IntersectionObserver' in window)) return;
    var b = document.createElement('div'); b.id = 'cp-bar';
    b.innerHTML = '<span><b>Votre devis relu par un ingénieur</b>dès 16,50 €, rapport sous 48 h</span><a href="' + COMEUP + '" data-goatcounter-click="clic-comeup-barre">Faire analyser</a>';
    document.body.appendChild(b);
    var top = document.getElementById('top') || document.querySelector('header');
    var past = false, hide = 0;
    function show() { var on = past && hide === 0; b.classList.toggle('on', on); document.body.classList.toggle('cp-bar-on', on); }
    if (top) new IntersectionObserver(function (en) { past = !en[0].isIntersecting && en[0].boundingClientRect.top < 0; show(); }).observe(top);
    var ends = document.querySelectorAll('footer, section:last-of-type');
    var vis = new Set();
    var io = new IntersectionObserver(function (en) { en.forEach(function (e) { if (e.isIntersecting) vis.add(e.target); else vis.delete(e.target); }); hide = vis.size; show(); });
    each(ends, function (e) { io.observe(e); });
  }

  function start() { test(); slider(); calc(); bar(); }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', start); else start();
})();

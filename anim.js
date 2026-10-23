/* Animations Contre-Plan : apparition au défilement, en-tête animé. Sans JavaScript, tout reste visible. */
(function () {
  if (!('IntersectionObserver' in window)) return;
  if (window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  document.documentElement.classList.add('anim');
  function each(list, fn) { Array.prototype.forEach.call(list, fn); }
  function init() {
    // Fonds « plan » qui glissent lentement
    each(document.querySelectorAll('[style*="linear-gradient(#2d3d62"]'), function (el) { el.classList.add('cp-grid'); });
    // En-tête de l'accueil
    var top = document.getElementById('top');
    if (top) {
      var left = top.children[0], card = top.children[1];
      if (left) each(left.children, function (el, i) { el.classList.add('cp-hero'); el.style.animationDelay = (0.05 + i * 0.12) + 's'; });
      var accent = top.querySelector('h1 span');
      if (accent) accent.classList.add('cp-pen');
      if (card) {
        card.classList.add('cp-card');
        var rows = card.children, n = 0;
        each(rows, function (r, i) { if (i === 0) return; r.classList.add('cp-row'); r.style.animationDelay = (0.75 + i * 0.2) + 's'; n = i; });
        each(card.querySelectorAll('span'), function (s) {
          if (s.textContent.trim() === 'NÉGOCIABLE') { s.classList.add('cp-stamp'); s.style.animationDelay = (0.95 + n * 0.2) + 's'; }
        });
      }
    }
    // Apparition au défilement
    var sel = 'main h1, main h2, main h3, main p, main ul, main ol, main details, main .note, main > div > a, ' +
              'section h2, section h3, section p, section ul, section ol, section details, section table, ' +
              'section a[style*="border-radius"], section div[style*="border-radius: 6px"], section div[style*="border-radius:6px"]';
    var cand = [];
    each(document.querySelectorAll(sel), function (el) {
      if (top && top.contains(el)) return;
      if (el.closest('header')) return;
      for (var i = 0; i < cand.length; i++) if (cand[i].contains(el)) return;
      cand = cand.filter(function (c) { return !el.contains(c); });
      cand.push(el);
    });
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (!e.isIntersecting) return;
        var el = e.target, sib = 0, p = el.previousElementSibling;
        while (p && sib < 5) { if (p.classList.contains('cp-rv') && !p.classList.contains('cp-in')) sib++; p = p.previousElementSibling; }
        el.style.animationDelay = (sib * 0.08) + 's';
        el.classList.add('cp-in');
        io.unobserve(el);
      });
    }, { rootMargin: '0px 0px -6% 0px', threshold: 0.08 });
    cand.forEach(function (el) { el.classList.add('cp-rv'); io.observe(el); });
  }

  function extras() {
    var top = document.getElementById('top');
    // Barre de progression façon règle de chantier
    var bar = document.createElement('div'); bar.id = 'cp-progress'; document.body.appendChild(bar);
    var ticking = false;
    function prog() { var h = document.documentElement.scrollHeight - innerHeight; bar.style.transform = 'scaleX(' + (h > 0 ? Math.min(1, scrollY / h) : 0) + ')'; ticking = false; }
    addEventListener('scroll', function () { if (!ticking) { ticking = true; requestAnimationFrame(prog); } }, { passive: true }); prog();
    // Coches qui se dessinent une à une
    each(document.querySelectorAll('section li > svg'), function (svg) {
      svg.classList.add('cp-check');
      var li = svg.parentNode, i = Array.prototype.indexOf.call(li.parentNode.children, li);
      each(svg.querySelectorAll('path'), function (pth) { pth.style.animationDelay = (0.25 + i * 0.18) + 's'; });
    });
    // Numéros d'étapes
    each(document.querySelectorAll('#etapes ol > li > span:first-child'), function (sp, i) {
      sp.classList.add('cp-num'); sp.style.animationDelay = (0.2 + i * 0.3) + 's, ' + (0.7 + i * 0.3) + 's';
    });
    // Soulignement des mots en couleur dans les titres
    each(document.querySelectorAll('section h2 span, main h2 span'), function (sp) { if (!(top && top.contains(sp))) sp.classList.add('cp-pen2'); });
    // Tarifs : prix qui défilent, ancien prix barré, badge tamponné
    var prices = [];
    each(document.querySelectorAll('#tarifs span'), function (sp) {
      var fs = sp.style.fontSize;
      if (fs === '44px') prices.push(sp);
      if (sp.style.textDecoration === 'line-through') sp.classList.add('cp-strike');
      if (/^Lancement/.test(sp.textContent.trim())) sp.classList.add('cp-badge');
    });
    function countUp(sp) {
      var tn = sp.firstChild; if (!tn || tn.nodeType !== 3) return;
      var m = tn.nodeValue.match(/(\d+)(?:,(\d+))?/); if (!m) return;
      var orig = tn.nodeValue, target = parseFloat(m[1] + '.' + (m[2] || '0')), dec = m[2] ? m[2].length : 0, t0 = null;
      function step(t) {
        if (!t0) t0 = t; var k = Math.min(1, (t - t0) / 900), e = 1 - Math.pow(1 - k, 3);
        var v = (target * e).toFixed(dec).replace('.', ',');
        tn.nodeValue = orig.replace(m[0], v);
        if (k < 1) requestAnimationFrame(step); else tn.nodeValue = orig;
      }
      requestAnimationFrame(step);
    }
    var once = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (!e.isIntersecting) return; once.unobserve(e.target);
        if (e.target.classList.contains('cp-scanbox')) e.target.classList.add('cp-go'); else countUp(e.target);
      });
    }, { threshold: 0.4 });
    prices.forEach(function (sp) { once.observe(sp); });
    // Balayage sur l'exemple de rapport
    var img = document.querySelector('img[src*="exemple-rapport"]');
    if (img && img.parentNode) { img.parentNode.classList.add('cp-scanbox'); once.observe(img.parentNode); }
    // Bouton du chat : trois pulsations après 6 s
    setTimeout(function () { var b = document.getElementById('cp-chat-btn'); if (b) b.classList.add('cp-ring'); }, 6000);
    // Carte de l'accueil qui s'incline légèrement sous la souris
    if (top && top.children[1] && matchMedia('(hover: hover) and (pointer: fine)').matches) {
      var card = top.children[1];
      card.addEventListener('animationend', function onEnd(ev) { if (ev.target !== card) return; card.removeEventListener('animationend', onEnd); card.classList.remove('cp-card'); card.classList.add('cp-tilt'); });
      top.addEventListener('mousemove', function (ev) {
        if (!card.classList.contains('cp-tilt')) return;
        var r = card.getBoundingClientRect(), x = (ev.clientX - r.left) / r.width - 0.5, y = (ev.clientY - r.top) / r.height - 0.5;
        card.style.transform = 'perspective(900px) rotateY(' + (x * 6) + 'deg) rotateX(' + (-y * 6) + 'deg)';
      });
      top.addEventListener('mouseleave', function () { card.style.transform = ''; });
    }
  }
  function start() { init(); extras(); }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', start); else start();
})();

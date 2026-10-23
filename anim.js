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
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init); else init();
})();

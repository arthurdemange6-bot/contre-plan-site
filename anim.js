/* Animations Contre-Plan : apparition au défilement, en-tête animé. Sans JavaScript, tout reste visible. */
(function () {
  if (!('IntersectionObserver' in window)) return;
  if (window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  document.documentElement.classList.add('anim');
  function each(list, fn) { Array.prototype.forEach.call(list, fn); }
  function init() {
    // Fonds « plan » qui glissent lentement
    each(document.querySelectorAll('[style*="linear-gradient(#2a4a75"]'), function (el) { el.classList.add('cp-grid'); });
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
              'section a[style*="border-radius"], section div[style*="border-radius: 2px"], section div[style*="border-radius:2px"]';
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

  function devis() {
    var top = document.getElementById('top');
    if (!top) return;
    var wrap = document.body.firstElementChild;
    if (!wrap || wrap.tagName !== 'DIV') return;
    var rows = [
      ['Protection des sols, évacuation du mobilier', '1 ft', '180,00', '180,00'],
      ['Dépose carrelage mural et sol', '25 m²', '58,00', '1 450,00', 'ring', 'élevé ?'],
      ['Dépose baignoire et sanitaires', '1 u', '250,00', '250,00'],
      ['Receveur extra-plat 90×120', '1 u', '690,00', '690,00', '', 'OK ✓'],
      ['Étanchéité sous carrelage', '—', '—', '—', '', 'non chiffrée !'],
      ['Faïence murale 30×60, fourniture et pose', '14 m²', '95,00', '1 330,00'],
      ['Carrelage sol antidérapant', '6 m²', '89,00', '534,00'],
      ['Plomberie : alimentations, évacuations', '1 ft', '1 150,00', '1 150,00', '', 'à détailler'],
      ['Meuble vasque 80 cm et mitigeur', '1 u', '640,00', '640,00'],
      ['Électricité : 2 spots, raccordement VMC', '1 ft', '480,00', '480,00']
    ];
    function el(tag, cls, html) { var e = document.createElement(tag); if (cls) e.className = cls; if (html != null) e.innerHTML = html; return e; }
    var layer = el('div'); layer.id = 'cp-devis'; layer.setAttribute('aria-hidden', 'true');
    var sheet = el('div', 'cp-sheet'); layer.appendChild(sheet);
    var steps = [];  // [élément, début, fin, type]
    var h = el('div', 'h cp-w', '<b>DEVIS</b><span>Exemple fictif · Salle de bain 6 m²</span>'); sheet.appendChild(h); steps.push([h, 0, 0.05, 'w']);
    var hd = el('div', 'r hd cp-w', '<span>Désignation</span><span>Qté</span><span>P.U. HT</span><span>Total HT</span>'); sheet.appendChild(hd); steps.push([hd, 0.03, 0.07, 'w']);
    var notes = [];
    rows.forEach(function (r, i) {
      var row = el('div', 'r cp-w');
      row.innerHTML = '<span>' + r[0] + '</span><span>' + r[1] + '</span><span>' + r[2] + '</span><span class="cp-amt">' + r[3] + '</span>';
      sheet.appendChild(row);
      var a = 0.07 + i * 0.05; steps.push([row, a, a + 0.045, 'w']);
      if (r[4] === 'ring') { var ring = el('i', 'cp-ring2'); row.lastChild.appendChild(ring); notes.push(ring); }
      if (r[5]) { var n = el('span', 'cp-n', r[5]); row.appendChild(n); notes.push(n); }
    });
    var gr = el('div', 'r cp-w', '<span></span><span></span><span></span><span></span>'); gr.appendChild(el('span', 'cp-n', '+ évacuation des gravats ?')); gr.lastChild.style.right = 'auto'; gr.lastChild.style.left = '0'; gr.lastChild.style.top = '.2em';
    sheet.appendChild(gr); steps.push([gr, 0.57, 0.575, 'w']); notes.splice(4, 0, gr.lastChild);
    var t1 = el('div', 't cp-w', '<span>Total HT</span><span>6 704,00 €</span>');
    var t2 = el('div', 't cp-w', '<span>TVA 10 %</span><span>670,40 €</span>');
    var t3 = el('div', 't cp-w', '<span>Total TTC</span><span>7 374,40 €</span>');
    var t4 = el('div', 't cp-w', '<span>Acompte à la commande : 50 %</span><span class="cp-amt">3 687,20 €</span>');
    [t1, t2, t3, t4].forEach(function (t, i) { sheet.appendChild(t); steps.push([t, 0.58 + i * 0.03, 0.61 + i * 0.03, 'w']); });
    var ring4 = el('i', 'cp-ring2'); t4.lastChild.appendChild(ring4); var n4 = el('span', 'cp-n', '→ 30 % suffit'); t4.appendChild(n4); notes.push(ring4, n4);
    var sig = el('div', 'sig cp-w', '<span>Bon pour accord, le …</span><span>Signature :</span>'); sheet.appendChild(sig); steps.push([sig, 0.7, 0.74, 'w']);
    var tampon = el('div', 'cp-tampon', 'RELU'); sig.style.position = 'relative'; sig.appendChild(tampon);
    notes.forEach(function (n, i) { var a = 0.75 + i * 0.022; steps.push([n, a, a, 'on']); });
    steps.push([tampon, 0.95, 0.95, 'on']);
    document.body.insertBefore(layer, wrap);
    wrap.style.background = 'transparent'; wrap.classList.add('cp-front');
    var busy = false;
    function upd() {
      busy = false;
      var H = document.documentElement.scrollHeight - innerHeight, p = H > 0 ? scrollY / H : 1;
      steps.forEach(function (s) {
        if (s[3] === 'w') { var k = Math.max(0, Math.min(1, (p - s[1]) / (s[2] - s[1]))); s[0].style.clipPath = k >= 1 ? 'none' : 'inset(0 ' + (100 - k * 100) + '% 0 0)'; }
        else s[0].classList.toggle('on', p >= s[1]);
      });
    }
    addEventListener('scroll', function () { if (!busy) { busy = true; requestAnimationFrame(upd); } }, { passive: true });
    addEventListener('resize', upd); upd();
  }

  function finitions() {
    var top = document.getElementById('top');
    if (top && top.children[1]) {
      var card = top.children[1]; card.classList.add('cp-coted');
      var h = document.createElement('div'); h.className = 'cp-cote h'; h.setAttribute('aria-hidden', 'true'); h.innerHTML = '<span>Relu ligne par ligne</span>';
      var v = document.createElement('div'); v.className = 'cp-cote v'; v.setAttribute('aria-hidden', 'true'); v.innerHTML = '<span>Sous 48 h</span>';
      card.appendChild(h); card.appendChild(v);
      var cta = top.querySelector('a[style*="background: #bf4a17"]'); if (cta) cta.classList.add('cp-shine');
    }
    each(document.querySelectorAll('section div[style*="border-radius: 2px"]'), function (c) {
      var f = c.firstElementChild; if (f && /^0\d$/.test(f.textContent.trim())) c.classList.add('cp-topline');
    });
    each(document.querySelectorAll('section p'), function (p) {
      var key = 'mon seul intérêt est que vous signiez un devis juste';
      each(p.childNodes, function (n) {
        if (n.nodeType !== 3) return; var i = n.nodeValue.indexOf(key); if (i < 0) return;
        var after = n.splitText(i); after.splitText(key.length);
        var m = document.createElement('span'); m.className = 'cp-mark'; m.textContent = key; after.parentNode.replaceChild(m, after);
      });
    });
  }
  function start() { finitions(); init(); extras(); devis(); }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', start); else start();
})();

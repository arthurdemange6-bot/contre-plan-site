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
      if (/^−50/.test(sp.textContent.trim())) sp.classList.add('cp-badge');
    });
    // Prix qui montent au fil du défilement (et redescendent si l'on remonte)
    var pr = prices.map(function (sp) {
      var tn = sp.firstChild; if (!tn || tn.nodeType !== 3) return null;
      var m = tn.nodeValue.match(/(\d+)(?:,(\d+))?/); if (!m) return null;
      return { sp: sp, tn: tn, orig: tn.nodeValue, m: m, target: parseFloat(m[1] + '.' + (m[2] || '0')), dec: m[2] ? m[2].length : 0, last: '' };
    }).filter(Boolean);
    var tarifs = document.getElementById('tarifs'), pbusy = false;
    function pupd() {
      pbusy = false; if (!tarifs) return;
      var r = tarifs.getBoundingClientRect(), vh = innerHeight;
      var k = Math.max(0, Math.min(1, (vh - r.top) / (vh * 0.7)));
      pr.forEach(function (o, i) {
        var ki = Math.max(0, Math.min(1, k * 1.12 - i * 0.06));
        var v = ki >= 1 ? o.orig : o.orig.replace(o.m[0], (o.target * ki).toFixed(o.dec).replace('.', ','));
        if (v !== o.last) { o.tn.nodeValue = v; o.last = v; }
      });
      if (k > 0.2) each(document.querySelectorAll('#tarifs .cp-strike, #tarifs .cp-badge'), function (x) { x.closest('div').classList.add('cp-in'); });
    }
    addEventListener('scroll', function () { if (!pbusy) { pbusy = true; requestAnimationFrame(pupd); } }, { passive: true });
    addEventListener('resize', pupd); pupd();
    // Chiffres clés qui montent au fil du défilement
    var stats = Array.prototype.map.call(document.querySelectorAll('[data-count]'), function (b) {
      return { b: b, to: +b.getAttribute('data-count'), pre: b.getAttribute('data-prefix') || '', suf: b.getAttribute('data-suffix') || '', orig: b.textContent };
    });
    function sfmt(v) { return String(Math.round(v)).replace(/\B(?=(\d{3})+(?!\d))/g, ' '); }
    function supd() {
      stats.forEach(function (o, i) {
        var r = o.b.getBoundingClientRect(), k = Math.max(0, Math.min(1, (innerHeight - r.top) / (innerHeight * 0.55) * 1.1 - i * 0.05));
        var t = k >= 1 ? o.orig : o.pre + sfmt(o.to * (1 - Math.pow(1 - k, 2))) + o.suf;
        if (o.b.textContent !== t) o.b.textContent = t;
      });
    }
    if (stats.length) { addEventListener('scroll', function () { requestAnimationFrame(supd); }, { passive: true }); supd(); }
    var once = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (!e.isIntersecting) return; once.unobserve(e.target);
        if (e.target.classList.contains('cp-scanbox')) e.target.classList.add('cp-go');
      });
    }, { threshold: 0.4 });
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
    var wrap = document.body.firstElementChild;
    if (!wrap || wrap.tagName !== 'DIV') return;
    var home = !!document.getElementById('top');
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
    var pen = el('div', 'cp-pentip', '<svg viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M3 21l3.5-1 11-11-2.5-2.5-11 11L3 21z"/><path d="M14.5 5.5l2.5-2.5 4 4-2.5 2.5"/></svg>');
    sheet.appendChild(pen);
    var typed = [];   // [span, texte, début, fin]
    var marks = [];   // [élément, seuil]
    var lines = [];   // [ligne, seuil]
    function line(cls, cells, a, b) {
      var r = el('div', cls); sheet.appendChild(r);
      var tot = cells.reduce(function (s, c) { return s + Math.max(1, c.length); }, 0), pos = a;
      cells.forEach(function (c) {
        var s = el('span'); r.appendChild(s);
        var d = (b - a) * Math.max(1, c.length) / tot; typed.push([s, c, pos, pos + d]); pos += d;
      });
      lines.push([r, a]);
      return r;
    }
    var hd0 = el('div', 'h'); sheet.insertBefore(hd0, pen);
    var tb = el('b'); var ts = el('span'); hd0.appendChild(tb); hd0.appendChild(ts);
    typed.push([tb, 'DEVIS', 0, 0.025]); typed.push([ts, 'Exemple fictif · Salle de bain 6 m²', 0.025, 0.06]); lines.push([hd0, 0]);
    line('r hd', ['Désignation', 'Qté', 'P.U. HT', 'Total HT'], 0.06, 0.08);
    var span = 0.46 / rows.length;
    rows.forEach(function (r, i) {
      var a = 0.08 + i * span, row = line('r', r.slice(0, 4), a, a + span * 0.92);
      row.lastChild.className = 'cp-amt';
      if (r[4] === 'ring') { var ring = el('i', 'cp-ring2'); row.lastChild.appendChild(ring); marks.push([ring, a + span]); }
      if (r[5]) { var n = el('span', 'cp-n', r[5]); row.appendChild(n); marks.push([n, a + span * 1.05]); }
    });
    var gr = el('div', 'r'); sheet.appendChild(gr); var gn = el('span', 'cp-n', '+ évacuation des gravats ?'); gn.style.right = 'auto'; gn.style.left = '0'; gn.style.top = '.2em'; gr.appendChild(gn); marks.push([gn, 0.56]); lines.push([gr, 0.555]);
    var tt = [['Total HT', '6 704,00 €'], ['TVA 10 %', '670,40 €'], ['Total TTC', '7 374,40 €'], ['Acompte à la commande : 50 %', '3 687,20 €']], t4;
    tt.forEach(function (t, i) { var a = 0.57 + i * 0.035; t4 = line('t', t, a, a + 0.032); });
    t4.lastChild.className = 'cp-amt';
    var ring4 = el('i', 'cp-ring2'); t4.lastChild.appendChild(ring4); var n4 = el('span', 'cp-n', '→ 30 % suffit'); t4.appendChild(n4); marks.push([ring4, 0.72], [n4, 0.73]);
    var sig = line('sig', ['Bon pour accord, le …', 'Signature :'], 0.74, 0.79); sig.style.position = 'relative';
    var tampon = el('div', 'cp-tampon', 'RELU'); sig.appendChild(tampon); marks.push([tampon, 0.93]);
    sheet.appendChild(pen);
    document.body.insertBefore(layer, wrap);
    wrap.style.background = 'transparent'; wrap.classList.add('cp-front');
    if (!home) layer.classList.add('cp-soft');
    // Sections blanches légèrement translucides : le devis apparaît derrière
    each(wrap.children, function (c) {
      var bg = c.getAttribute('style') || '';
      if (/background:\s*#ffffff/i.test(bg)) c.style.background = 'rgba(255,255,255,.72)';
    });
    function fmt(v) { var s = v.toFixed(2).split('.'), i = s[0].replace(/\B(?=(\d{3})+(?!\d))/g, ' '); return i + ',' + s[1]; }
    // Les montants comptent plus longtemps : leur cellule s'étire jusqu'à la fin de la ligne suivante
    typed.forEach(function (t) { if (/^[\d ]+,\d\d( €)?$/.test(t[1])) t[3] = t[3] + (t[3] - t[2]) * 2.5; });
    var busy = false, idle;
    function upd() {
      busy = false;
      var H = document.documentElement.scrollHeight - innerHeight, p = H > 40 ? scrollY / H : 1;
      p = Math.min(1, p * (home ? 1.05 : 1.25));
      var cur = null;
      typed.forEach(function (t) {
        var k = Math.max(0, Math.min(1, (p - t[2]) / (t[3] - t[2]))), n = Math.round(k * t[1].length);
        var txt = t[1].slice(0, n), mm = t[1].match(/^([\d ]+),(\d\d)( €)?$/);
        if (mm && k > 0 && k < 1) { var tv = parseFloat(mm[1].replace(/ /g, '') + '.' + mm[2]) * (1 - Math.pow(1 - k, 2)); txt = fmt(tv) + (mm[3] || ''); }
        else if (mm && k === 0) txt = '';
        if (t[0].firstChild && t[0].firstChild.nodeType === 3) { if (t[0].firstChild.nodeValue !== txt) t[0].firstChild.nodeValue = txt; }
        else t[0].insertBefore(document.createTextNode(txt), t[0].firstChild);
        if (k > 0 && k < 1) cur = t[0];
      });
      var last = null;
      lines.forEach(function (l) { var on = p >= l[1]; l[0].classList.toggle('on', on); if (on) last = l[0]; });
      if (last) { var f = 0.42 - 0.2 * Math.max(0, Math.min(1, (p - 0.75) / 0.2)), want = last.offsetTop + last.offsetHeight - innerHeight * f; sheet.style.marginTop = (-Math.max(0, want)) + 'px'; }
      marks.forEach(function (m) { m[0].classList.toggle('on', p >= m[1]); });
      if (cur) {
        var sr = sheet.getBoundingClientRect(), r = cur.getBoundingClientRect();
        pen.style.transform = 'translate(' + (r.right - sr.left) + 'px,' + (r.top - sr.top - 18) + 'px)';
        pen.classList.add('on'); clearTimeout(idle); idle = setTimeout(function () { pen.classList.remove('on'); }, 500);
      }
    }
    addEventListener('scroll', function () { if (!busy) { busy = true; requestAnimationFrame(upd); } }, { passive: true });
    addEventListener('resize', upd); upd();
  }

  // Bandeaux qui se déroulent, cartes qui se soulèvent, reflets sur les boutons
  function plus() {
    var bands = [];
    each(document.querySelectorAll('.cp-kicker, .cp-kick, span[style*="text-transform: uppercase"][style*="background:"]'), function (b) { b.classList.add('cp-band'); bands.push(b); });
    var io = new IntersectionObserver(function (en) { en.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('cp-go'); io.unobserve(e.target); } }); }, { threshold: 0.6 });
    bands.forEach(function (b) { io.observe(b); });
    each(document.querySelectorAll('#travaux a, #tarifs div[style*="padding: 32px"], .cp-rcard, .cp-tpl, .cp-term, section a[style*="border: 1px solid"]'), function (c) { c.classList.add('cp-lift'); });
    each(document.querySelectorAll('a[style*="background: #bf4a17"], .cp-side a[style*="background"], .cp-form button'), function (a) { a.classList.add('cp-shine'); });
    var h2 = new IntersectionObserver(function (en) { en.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('cp-drawn'); h2.unobserve(e.target); } }); }, { threshold: 0.5 });
    each(document.querySelectorAll('.art h2, main h2'), function (h) { h2.observe(h); });
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
  function start() { finitions(); init(); extras(); devis(); plus(); }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', start); else start();
})();

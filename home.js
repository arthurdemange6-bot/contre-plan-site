/* Accueil Contre-Plan : en-tête collant, révélations, devis décortiqué, compteurs, parallaxe, cartes inclinées.
   Sans JavaScript ou en mouvement réduit, tout reste visible. */
(function () {
  var reduce = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
  var fine = window.matchMedia && matchMedia('(hover: hover) and (pointer: fine)').matches;
  function each(l, f) { Array.prototype.forEach.call(l, f); }
  function gc(path) { try { if (window.goatcounter && goatcounter.count) goatcounter.count({ path: path, title: path, event: true }); } catch (e) {} }

  function start() {
    /* En-tête qui se compacte */
    var bar = document.querySelector('.top-bar');
    function onScroll() { if (bar) bar.classList.toggle('scrolled', scrollY > 40); }
    addEventListener('scroll', onScroll, { passive: true }); onScroll();

    var hasIO = 'IntersectionObserver' in window;

    /* Révélations */
    var rv = document.querySelectorAll('.rv, .rv-l, .rv-s, .steps2');
    if (!hasIO || reduce) each(rv, function (e) { e.classList.add('in'); });
    else {
      var io = new IntersectionObserver(function (en) {
        en.forEach(function (e) {
          if (!e.isIntersecting) return;
          var el = e.target, d = el.getAttribute('data-d');
          if (d) el.style.transitionDelay = d + 's';
          el.classList.add('in'); io.unobserve(el);
        });
      }, { rootMargin: '0px 0px -8% 0px', threshold: 0.12 });
      each(rv, function (e) { io.observe(e); });
    }

    /* Compteurs */
    var nums = document.querySelectorAll('[data-to]');
    function fmt(v) { return String(Math.round(v)).replace(/\B(?=(\d{3})+(?!\d))/g, ' '); }
    function run(el) {
      var to = +el.getAttribute('data-to'), pre = el.getAttribute('data-pre') || '', suf = el.getAttribute('data-suf') || '';
      if (reduce) { el.innerHTML = pre + fmt(to) + suf; return; }
      var t0 = null, dur = 1600;
      function step(t) { if (!t0) t0 = t; var k = Math.min(1, (t - t0) / dur), e = 1 - Math.pow(1 - k, 4); el.innerHTML = pre + fmt(to * e) + suf; if (k < 1) requestAnimationFrame(step); }
      requestAnimationFrame(step);
    }
    if (hasIO) {
      var cio = new IntersectionObserver(function (en) { en.forEach(function (e) { if (e.isIntersecting) { run(e.target); cio.unobserve(e.target); } }); }, { threshold: 0.6 });
      each(nums, function (n) { cio.observe(n); });
    }

    /* Le devis décortiqué au fil du défilement */
    var steps = document.querySelectorAll('.st'), doc = document.querySelector('.story-doc');
    if (doc && steps.length) {
      var lines = doc.querySelectorAll('.l[data-k]'), dots = doc.querySelectorAll('.dots i'), cnt = doc.querySelector('.meter b'), seen = false;
      function setStep(k) {
        each(steps, function (s) { s.classList.toggle('on', +s.getAttribute('data-k') === k); });
        each(lines, function (l) { l.classList.toggle('on', +l.getAttribute('data-k') <= k); });
        each(dots, function (d, i) { d.classList.toggle('on', i < k); });
        if (cnt) cnt.textContent = k + '/' + steps.length;
        if (k === steps.length && !seen) { seen = true; gc('demo-devis-vue'); }
      }
      if (!hasIO || reduce) setStep(steps.length);
      else {
        var sio = new IntersectionObserver(function (en) {
          en.forEach(function (e) { if (e.isIntersecting) setStep(+e.target.getAttribute('data-k')); });
        }, { rootMargin: '-45% 0px -45% 0px', threshold: 0 });
        each(steps, function (s) { sio.observe(s); });
        setStep(0);
      }
    }

    /* Parallaxe du plan en fond */
    var plan = document.querySelector('.hero2 .plan');
    if (plan && !reduce) {
      var busy = false;
      addEventListener('scroll', function () {
        if (busy) return; busy = true;
        requestAnimationFrame(function () { var y = Math.min(scrollY, 900); plan.style.transform = 'translateY(' + (y * 0.25) + 'px) rotate(' + (-8 + y * 0.006) + 'deg)'; busy = false; });
      }, { passive: true });
    }

    /* Cartes qui s'inclinent sous la souris */
    if (fine && !reduce) each(document.querySelectorAll('.job'), function (c) {
      c.addEventListener('mousemove', function (ev) {
        var r = c.getBoundingClientRect(), x = (ev.clientX - r.left) / r.width - 0.5, y = (ev.clientY - r.top) / r.height - 0.5;
        c.style.transform = 'perspective(700px) rotateX(' + (-y * 6) + 'deg) rotateY(' + (x * 8) + 'deg) translateY(-4px)';
      });
      c.addEventListener('mouseleave', function () { c.style.transform = ''; });
    });
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', start); else start();
})();

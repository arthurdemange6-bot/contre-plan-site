/* Contre-Plan : une seule séquence d'animation, à l'arrivée sur l'accueil.
   L'exemple de devis se remplit ligne par ligne, les cotes se tracent, puis le tampon est apposé.
   Rien ne bouge si le visiteur a demandé moins d'animations ; sans JavaScript, tout reste affiché. */
(function () {
  if (window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  var top = document.getElementById('top');
  if (!top || !top.children[1]) return;
  document.documentElement.classList.add('anim');
  function each(l, f) { Array.prototype.forEach.call(l, f); }
  function start() {
    var card = top.children[1];
    card.classList.add('cp-coted', 'cp-card');
    var h = document.createElement('div'); h.className = 'cp-cote h'; h.setAttribute('aria-hidden', 'true'); h.innerHTML = '<span>Relu ligne par ligne</span>';
    var v = document.createElement('div'); v.className = 'cp-cote v'; v.setAttribute('aria-hidden', 'true'); v.innerHTML = '<span>Sous 48 h</span>';
    card.appendChild(h); card.appendChild(v);
    var n = 0;
    each(card.children, function (r, i) {
      if (i === 0 || r.classList.contains('cp-cote')) return;
      r.classList.add('cp-row'); r.style.animationDelay = (0.45 + i * 0.16) + 's'; n = i;
    });
    each(card.querySelectorAll('span'), function (s) {
      if (s.textContent.trim() === 'NÉGOCIABLE') { s.classList.add('cp-stamp'); s.style.animationDelay = (0.65 + n * 0.16) + 's'; }
    });
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', start); else start();
})();

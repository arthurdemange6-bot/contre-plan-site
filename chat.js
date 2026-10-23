/* Contre-Plan – assistant FAQ (100 % local, aucune donnée envoyée) */
(function () {
  var COMEUP = "https://comeup.com/fr/@contreplan";
  var KB = [
    { q: "Combien ça coûte ?", k: ["prix", "tarif", "coût", "cout", "combien", "€", "euro", "cher"],
      a: "L'analyse d'un devis coûte 16,50 € sur ComeUp (prix de lancement −50 %, au lieu de 33 €). Options : 2e devis + 11 €, comparatif de plusieurs devis + 16,50 €, livraison express en 24 h + 5,50 €. Pas de TVA." },
    { q: "Quel est le délai ?", k: ["délai", "délai ", "delai", "quand", "recevoir", "sous combien", "combien de temps", "rapide", "express", "24", "48", "jours"],
      a: "Vous recevez votre rapport PDF sous 48 h après l'envoi du devis, ou 24 h avec l'option express." },
    { q: "Comment ça marche ?", k: ["comment", "marche", "fonctionne", "étapes", "etapes", "commander", "procédure"],
      a: "1. Vous commandez sur ComeUp. 2. Vous envoyez votre devis en PDF ou en photo. 3. Vous recevez un rapport avec un verdict, les prix poste par poste, les oublis et les questions à poser à l'artisan." },
    { q: "Que contient le rapport ?", k: ["rapport", "contient", "reçois", "recois", "livrable", "pdf", "exemple"],
      a: "Un verdict global (cohérent, négociable ou signaux d'alerte), le contrôle des prix poste par poste, les postes oubliés, les incohérences d'enchaînement des travaux, les questions à poser avant de signer, et un échange de suivi inclus.", l: ["/exemple-rapport-contre-plan.pdf", "Voir un exemple de rapport complet (PDF)"] },
    { q: "Quels travaux analysez-vous ?", k: ["travaux", "type", "salle de bain", "cuisine", "isolation", "toiture", "pompe", "pac", "électricité", "electricite", "plomberie", "maçonnerie", "extension", "fenêtre", "menuiserie"],
      a: "Rénovation et construction : salle de bain, cuisine, isolation, toiture, pompe à chaleur, électricité, plomberie, maçonnerie, menuiseries, extension…", l: ["/#travaux", "Ce que je vérifie selon vos travaux"] },
    { q: "Mes données sont-elles protégées ?", k: ["données", "donnees", "confidentiel", "nom", "adresse", "personnel", "sécurité", "partag"],
      a: "Vous pouvez masquer votre nom et votre adresse sur le devis : seuls les postes, quantités et prix sont utiles. Votre devis n'est jamais partagé.", l: ["/engagements.html", "Mes engagements de confidentialité"] },
    { q: "Vous déplacez-vous ?", k: ["déplace", "deplace", "visite", "chantier", "venir", "sur place", "expertise", "litige", "avocat"],
      a: "Non, le service est 100 % à distance. Ce n'est ni une expertise judiciaire ni une maîtrise d'œuvre, et je n'interviens pas dans un litige déjà en cours." },
    { q: "Peut-on en parler par téléphone ?", k: ["appel", "téléphone", "telephone", "parler", "visio", "rendez-vous", "rdv", "joindre"],
      a: "Oui : vous pouvez réserver un appel gratuit de 15 min en visio pour présenter votre projet : https://calendar.app.google/6LCc6yKVHnbvA3WN7" },
    { q: "Quel acompte verser ?", k: ["acompte", "arrhes", "verser", "signature", "payer", "paiement", "échéancier", "echeancier", "solde", "avance"],
      a: "L'usage est d'environ 30 % à la signature, puis des paiements liés à l'avancement et le solde à la réception. Un acompte de 50 % ou plus mérite d'être négocié.", l: ["/guide-acompte-paiement-devis-travaux.html", "Le guide acompte et paiement"] },
    { q: "Quel taux de TVA ?", k: ["tva", "taux", "5,5", "10 %", "20 %", "taxe"],
      a: "5,5 % pour la rénovation énergétique, 10 % pour l'amélioration d'un logement de plus de 2 ans, 20 % dans les autres cas (neuf, agrandissement, certains équipements). Le taux doit correspondre à vos travaux.", l: ["/guide-tva-travaux-renovation.html", "Le guide TVA"] },
    { q: "Que veut dire ce mot ?", k: ["mot", "terme", "signifie", "veut dire", "définition", "definition", "lexique", "ragréage", "forfait", "ml"],
      a: "Les termes courants d'un devis (forfait, ml, P.U., ragréage, SPEC, RGE, réception…) sont expliqués simplement dans le lexique.", l: ["/lexique-devis-travaux.html", "Ouvrir le lexique"] },
    { q: "Qui analyse mon devis ?", k: ["qui", "ingénieur", "ingenieur", "expérience", "experience", "compétent", "fiable", "commission", "indépendant"],
      a: "Un ingénieur BTP qui pilote des chantiers depuis 2020. Indépendant : aucune commission d'artisan, aucune entreprise à vous revendre.", l: ["/methode.html", "Voir ma méthode"] }
  ];
  var FALLBACK = "Je n'ai pas la réponse à cette question. Écrivez à contact@contre-plan.com, ou réservez un appel gratuit de 15 min : https://calendar.app.google/6LCc6yKVHnbvA3WN7";

  var css = "#cp-chat-btn{position:fixed;right:20px;bottom:20px;z-index:9999;display:flex;align-items:center;gap:10px;background:#c44c19;color:#fff;border:0;border-radius:999px;padding:14px 20px;font:700 16px 'Source Sans 3',Arial,sans-serif;box-shadow:0 8px 24px rgba(0,0,0,.3);cursor:pointer}" +
    "#cp-chat-btn:hover{background:#b8461a}" +
    "#cp-chat{position:fixed;right:20px;bottom:86px;z-index:9999;width:min(380px,calc(100vw - 40px));max-height:min(560px,calc(100vh - 120px));display:none;flex-direction:column;background:#fbfaf6;color:#14284b;border-radius:10px;box-shadow:0 16px 48px rgba(0,0,0,.35);overflow:hidden;font-family:'Source Sans 3',Arial,sans-serif}" +
    "#cp-chat.open{display:flex}" +
    "#cp-chat header{background:#08111f;color:#fff;padding:14px 16px;display:flex;align-items:center;justify-content:space-between;gap:10px}" +
    "#cp-chat header b{font-family:Archivo,Arial,sans-serif;letter-spacing:1px}" +
    "#cp-chat header small{display:block;color:#c9d3ea;font-size:13px;font-weight:400;letter-spacing:0}" +
    "#cp-close{background:none;border:0;color:#fff;font-size:26px;line-height:1;cursor:pointer;width:44px;height:44px}" +
    "#cp-log{flex:1;overflow-y:auto;padding:14px;display:flex;flex-direction:column;gap:10px}" +
    ".cp-m{max-width:85%;padding:10px 13px;border-radius:12px;font-size:15px;line-height:1.45}" +
    ".cp-bot{background:#fff;border:1px solid #ddd8ca;align-self:flex-start}" +
    ".cp-user{background:#14284b;color:#fff;align-self:flex-end}" +
    ".cp-chips{display:flex;flex-wrap:wrap;gap:6px}" +
    ".cp-chip{background:#fff;border:1px solid #c44c19;color:#b8461a;border-radius:999px;padding:8px 12px;font:600 14px 'Source Sans 3',Arial,sans-serif;cursor:pointer;min-height:36px}" +
    ".cp-chip:hover{background:#fdf1ea}" +
    ".cp-cta{display:inline-block;margin-top:6px;background:#c44c19;color:#fff!important;text-decoration:none;font-weight:700;padding:9px 14px;border-radius:4px}" +
    "#cp-form{display:flex;gap:8px;padding:10px;border-top:1px solid #e3e0d6;background:#fff}" +
    "#cp-in{flex:1;border:1px solid #c9c3b3;border-radius:6px;padding:10px;font:15px 'Source Sans 3',Arial,sans-serif;min-width:0}" +
    "#cp-send{background:#14284b;color:#fff;border:0;border-radius:6px;padding:0 14px;font-weight:700;cursor:pointer;min-height:44px}";
  var st = document.createElement("style"); st.textContent = css; document.head.appendChild(st);

  var btn = document.createElement("button");
  btn.id = "cp-chat-btn"; btn.type = "button"; btn.setAttribute("aria-expanded", "false"); btn.setAttribute("aria-controls", "cp-chat");
  btn.innerHTML = '<svg aria-hidden="true" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path></svg>Une question ?';

  var box = document.createElement("section");
  box.id = "cp-chat"; box.setAttribute("aria-label", "Assistant Contre-Plan");
  box.innerHTML = '<header><div><b>CONTRE-PLAN</b><small>Réponses aux questions fréquentes</small></div><button id="cp-close" type="button" aria-label="Fermer">×</button></header>' +
    '<div id="cp-log" aria-live="polite"></div>' +
    '<form id="cp-form"><label for="cp-in" style="position:absolute;left:-9999px">Votre question</label><input id="cp-in" type="text" placeholder="Posez votre question…" autocomplete="off"><button id="cp-send" type="submit">Envoyer</button></form>';
  document.body.appendChild(btn); document.body.appendChild(box);

  var log = box.querySelector("#cp-log"), input = box.querySelector("#cp-in"), started = false;

  function add(text, who, html) {
    var d = document.createElement("div"); d.className = "cp-m " + (who === "user" ? "cp-user" : "cp-bot");
    if (html) d.innerHTML = text; else d.textContent = text;
    log.appendChild(d); log.scrollTop = log.scrollHeight; return d;
  }
  function chips() {
    var w = document.createElement("div"); w.className = "cp-chips";
    KB.forEach(function (e) {
      var c = document.createElement("button"); c.type = "button"; c.className = "cp-chip"; c.textContent = e.q;
      c.onclick = function () { ask(e.q, e); }; w.appendChild(c);
    });
    log.appendChild(w); log.scrollTop = log.scrollHeight;
  }
  function norm(s) { return s.toLowerCase(); }
  function find(t) {
    var n = norm(t), best = null, score = 0;
    KB.forEach(function (e) { var s = 0; e.k.forEach(function (k) { if (n.indexOf(k) !== -1) s += k.length; }); if (s > score) { score = s; best = e; } });
    return best;
  }
  function ask(text, entry) {
    add(text, "user");
    var e = entry || find(text);
    setTimeout(function () {
      var m = add(e ? e.a : FALLBACK, "bot");
      var a = document.createElement("a"); a.href = COMEUP; a.className = "cp-cta"; a.target = "_blank"; a.rel = "noopener"; a.textContent = "Faire analyser mon devis";
      a.onclick = function () { try { window.goatcounter && window.goatcounter.count({ path: "clic-comeup-chat", event: true }); } catch (x) {} };
      if (e && e.l) { var l = document.createElement("a"); l.href = e.l[0]; l.textContent = e.l[1] + " →"; l.style.cssText = "display:block;margin-top:8px;color:#b8461a;font-weight:700"; m.appendChild(l); }
      m.appendChild(document.createElement("br")); m.appendChild(a);
    }, 250);
  }
  function open(v) {
    box.classList.toggle("open", v); btn.setAttribute("aria-expanded", v ? "true" : "false");
    if (v && !started) { started = true; add("Bonjour ! Je réponds aux questions fréquentes sur l'analyse de devis. Choisissez une question ou écrivez la vôtre.", "bot"); chips(); }
    if (v) input.focus();
  }
  btn.onclick = function () { open(!box.classList.contains("open")); };
  box.querySelector("#cp-close").onclick = function () { open(false); btn.focus(); };
  box.querySelector("#cp-form").onsubmit = function (ev) { ev.preventDefault(); var t = input.value.trim(); if (!t) return; input.value = ""; ask(t); };
})();

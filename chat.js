/* Contre-Plan – assistant : orientation en 3 questions + FAQ (100 % local ; seuls des compteurs anonymes GoatCounter sont envoyés, aucune réponse saisie) */
(function () {
  var COMEUP = "https://comeup.com/fr/service/549064/verifier-votre-devis-de-travaux-avant-signature-et-reperer-les-prix-abusifs-et-les-oublis";
  var KB = [
    { q: "Combien ça coûte ?", k: ["prix", "tarif", "coût", "cout", "combien", "€", "euro", "cher"],
      a: "L'analyse d'un devis coûte 16,50 € sur ComeUp (prix de lancement). Options : 2e devis + 11 €, comparatif de plusieurs devis + 16,50 €, livraison express en 24 h + 5,50 €. Pas de TVA." },
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
      a: "L'usage est d'environ 30 % à la signature, puis des paiements liés à l'avancement et le solde à la réception. Au-delà de 40 à 50 %, demandez pourquoi et proposez un échéancier.", l: ["/guide-acompte-paiement-devis-travaux.html", "Le guide acompte et paiement"] },
    { q: "Quel taux de TVA ?", k: ["tva", "taux", "5,5", "10 %", "20 %", "taxe"],
      a: "5,5 % pour la rénovation énergétique, 10 % pour l'amélioration d'un logement de plus de 2 ans, 20 % dans les autres cas (neuf, agrandissement, certains équipements). Le taux doit correspondre à vos travaux.", l: ["/guide-tva-travaux-renovation.html", "Le guide TVA"] },
    { q: "Que veut dire ce mot ?", k: ["mot", "terme", "signifie", "veut dire", "définition", "definition", "lexique", "ragréage", "forfait", "ml"],
      a: "Les termes courants d'un devis (forfait, ml, P.U., ragréage, SPEC, RGE, réception…) sont expliqués simplement dans le lexique.", l: ["/lexique-devis-travaux.html", "Ouvrir le lexique"] },
    { q: "Comment comparer mes devis ?", k: ["comparer", "comparatif", "plusieurs devis", "deux devis", "trois devis", "tableau"],
      a: "Comparez poste par poste, en HT, en mettant les prestations comparables sur la même ligne : un devis moins cher avec des postes absents peut finir plus cher. Un tableau gratuit est disponible, et l'option « Comparatif multi devis » vous le livre rempli et commenté.", l: ["/comparer-ses-devis.html", "Le tableau comparatif gratuit"] },
    { q: "Qui analyse mon devis ?", k: ["qui", "ingénieur", "ingenieur", "expérience", "experience", "compétent", "fiable", "commission", "indépendant"],
      a: "Un ingénieur BTP avec 10 ans d'expérience sur les chantiers et environ 1 000 devis lus et négociés. Indépendant : aucune commission d'artisan, aucune entreprise à vous revendre.", l: ["/methode.html", "Voir ma méthode"] },
    { q: "Est-ce fiable ?", k: ["arnaque", "fiable", "confiance", "sérieux", "serieux", "escroquerie", "légal", "legal", "vrai", "siret", "garantie", "rassur"],
      a: "Contre-Plan est une entreprise immatriculée (SIRET 132 070 426 00011), rattachée au médiateur de la consommation CM2C. Vous payez sur ComeUp, une plateforme de paiement sécurisé, et vous pouvez masquer votre nom et votre adresse sur le devis. Pas sûr que l'analyse vous serve ? Le pré-diagnostic gratuit vous le dit avant toute commande.", l: ["/mentions-legales.html", "Voir les mentions légales"] },
    { q: "Mon devis me paraît trop cher", k: ["trop cher", "devis cher", "est cher", "paraît cher", "parait cher", "arnaqué", "arnaque moi", "surfactur", "abus", "gonflé", "gonfle", "normal ce prix", "prix normal", "est-ce normal"],
      a: "C'est exactement ce que vérifie l'analyse : le prix de chaque poste comparé aux prix constatés, les postes oubliés ou comptés deux fois, et les points à négocier. Pour savoir d'abord si l'analyse vaut le coup sur votre devis, demandez le pré-diagnostic gratuit (réponse sous 24 h).", l: ["/contact.html?sujet=prediagnostic", "Demander le pré-diagnostic gratuit"] },
    { q: "Comment vous contacter ?", k: ["contact", "contacter", "joindre", "écrire", "ecrire", "mail", "email", "message", "formulaire"],
      a: "Par le formulaire de contact : je réponds sous 24 h. Pour faire analyser un devis, commandez directement sur ComeUp.", l: ["/contact.html", "Formulaire de contact"] }
  ];
  var FALLBACK = "Je n'ai pas de réponse toute prête à cette question, mais je vous réponds personnellement sous 24 h via le formulaire de contact. Vous pouvez aussi demander le pré-diagnostic gratuit de votre devis, ou réserver un appel gratuit de 15 min : https://calendar.app.google/6LCc6yKVHnbvA3WN7";

  var css = "#cp-chat-btn{position:fixed;right:20px;bottom:20px;z-index:9999;display:flex;align-items:center;gap:10px;background:#bf4a17;color:#fff;border:0;border-radius:2px;padding:14px 20px;font:700 16px 'Source Sans 3',Arial,sans-serif;box-shadow:0 8px 24px rgba(0,0,0,.3);cursor:pointer}" +
    "#cp-chat-btn:hover{background:#b8461a}" +
    "@media (max-width:600px){#cp-chat-btn{right:12px;bottom:12px;padding:12px;border-radius:50%}#cp-chat-btn span{position:absolute;left:-9999px}body{padding-bottom:72px}}" +
    "#cp-chat{position:fixed;right:20px;bottom:86px;z-index:9999;width:min(380px,calc(100vw - 40px));max-height:min(560px,calc(100vh - 120px));display:none;flex-direction:column;background:#ffffff;color:#14284b;border-radius:10px;box-shadow:0 16px 48px rgba(0,0,0,.35);overflow:hidden;font-family:'Source Sans 3',Arial,sans-serif}" +
    "#cp-chat.open{display:flex}" +
    "#cp-chat header{background:#0f2747;color:#fff;padding:14px 16px;display:flex;align-items:center;justify-content:space-between;gap:10px}" +
    "#cp-chat header b{font-family:Archivo,Arial,sans-serif;}" +
    "#cp-chat header small{display:block;color:#c9d3ea;font-size:13px;font-weight:400;letter-spacing:0}" +
    "#cp-close{background:none;border:0;color:#fff;font-size:26px;line-height:1;cursor:pointer;width:44px;height:44px}" +
    "#cp-log{flex:1;overflow-y:auto;padding:14px;display:flex;flex-direction:column;gap:10px}" +
    ".cp-m{max-width:85%;padding:10px 13px;border-radius:12px;font-size:15px;line-height:1.45}" +
    ".cp-bot{background:#fff;border:1px solid #d8dee6;align-self:flex-start}" +
    ".cp-user{background:#14284b;color:#fff;align-self:flex-end}" +
    ".cp-chips{display:flex;flex-wrap:wrap;gap:6px}" +
    ".cp-chip{background:#fff;border:1px solid #bf4a17;color:#b8461a;border-radius:2px;padding:8px 12px;font:600 14px 'Source Sans 3',Arial,sans-serif;cursor:pointer;min-height:36px}" +
    ".cp-chip:hover{background:#fdf1ea}" +
    ".cp-cta{display:inline-block;margin-top:6px;background:#bf4a17;color:#fff!important;text-decoration:none;font-weight:700;padding:9px 14px;border-radius:2px}" +
    "#cp-form{display:flex;gap:8px;padding:10px;border-top:1px solid #e6e9ee;background:#fff}" +
    "#cp-in{flex:1;border:1px solid #c5ccd6;border-radius:2px;padding:10px;font:15px 'Source Sans 3',Arial,sans-serif;min-width:0}" +
    "#cp-send{background:#14284b;color:#fff;border:0;border-radius:2px;padding:0 14px;font-weight:700;cursor:pointer;min-height:44px}";
  var st = document.createElement("style"); st.textContent = css; document.head.appendChild(st);

  var btn = document.createElement("button");
  btn.id = "cp-chat-btn"; btn.type = "button"; btn.setAttribute("aria-expanded", "false"); btn.setAttribute("aria-controls", "cp-chat");
  btn.innerHTML = '<svg aria-hidden="true" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path></svg><span>Une question ?</span>';

  var box = document.createElement("section");
  box.id = "cp-chat"; box.setAttribute("aria-label", "Assistant Contre-Plan");
  box.innerHTML = '<header><div><b>CONTRE-PLAN</b><small>Orientation et questions fréquentes</small></div><button id="cp-close" type="button" aria-label="Fermer">×</button></header>' +
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
      if (!e) { var lc = document.createElement("a"); lc.href = "/contact.html"; lc.textContent = "Formulaire de contact"; lc.style.cssText = "display:block;margin-top:8px;color:#b8461a;font-weight:700"; m.appendChild(lc); }
      if (e && e.l) { var l = document.createElement("a"); l.href = e.l[0]; l.textContent = e.l[1] + ""; l.style.cssText = "display:block;margin-top:8px;color:#b8461a;font-weight:700"; m.appendChild(l); }
      m.appendChild(document.createElement("br")); m.appendChild(a);
    }, 250);
  }
  var BOOK = "https://calendar.app.google/6LCc6yKVHnbvA3WN7";
  function gc(path) { try { window.goatcounter && window.goatcounter.count({ path: "chat/" + path, title: "Assistant : " + path, event: true }); } catch (x) {} }
  function link(href, text, primary, ev) {
    var a = document.createElement("a"); a.href = href; a.textContent = text;
    if (/^https?:/.test(href)) { a.target = "_blank"; a.rel = "noopener"; }
    a.style.cssText = primary ? "" : "display:block;margin-top:8px;color:#b8461a;font-weight:700";
    if (primary) a.className = "cp-cta";
    if (ev) a.onclick = function () { gc(ev); };
    return a;
  }
  function choose(question, options, cb) {
    add(question, "bot");
    var w = document.createElement("div"); w.className = "cp-chips";
    options.forEach(function (o) {
      var c = document.createElement("button"); c.type = "button"; c.className = "cp-chip"; c.textContent = o[0];
      c.onclick = function () { w.remove(); add(o[0], "user"); setTimeout(function () { cb(o); }, 250); };
      w.appendChild(c);
    });
    log.appendChild(w); log.scrollTop = log.scrollHeight;
  }
  var PAGES = { sdb: ["/analyse-devis-salle-de-bain.html", "Ce que je vérifie sur un devis de salle de bain"],
    iso: ["/analyse-devis-isolation.html", "Ce que je vérifie sur un devis d'isolation"],
    toit: ["/analyse-devis-toiture.html", "Ce que je vérifie sur un devis de toiture"],
    pac: ["/analyse-devis-pompe-a-chaleur.html", "Ce que je vérifie sur un devis de pompe à chaleur"] };
  function qualify() {
    gc("orientation-debut");
    var r = {};
    choose("C'est pour quels travaux ?", [["Salle de bain", "sdb"], ["Isolation", "iso"], ["Toiture", "toit"], ["Pompe à chaleur", "pac"], ["Cuisine", "cuisine"], ["Autre", "autre"]], function (t) {
      r.t = t[1]; gc("travaux-" + t[1]);
      choose("Le devis fait combien, à peu près ?", [["Moins de 5 000 €", "moins-5k"], ["De 5 000 à 20 000 €", "5-20k"], ["Plus de 20 000 €", "plus-20k"], ["Je n'ai pas encore de devis", "pas-de-devis"]], function (m) {
        r.m = m[1]; gc("montant-" + m[1]);
        if (r.m === "pas-de-devis") return result(r);
        choose("Vous devez signer quand ?", [["Cette semaine", "semaine"], ["Ce mois-ci", "mois"], ["Pas de date pour l'instant", "sans-date"]], function (d) {
          r.d = d[1]; gc("signature-" + d[1]); result(r);
        });
      });
    });
  }
  function result(r) {
    var m, page = PAGES[r.t];
    if (r.m === "pas-de-devis") {
      gc("resultat-preparer");
      m = add("Vous êtes au bon moment : c'est avant de demander les devis qu'on évite le plus de pièges. Commencez par décrire votre projet de la même façon à chaque artisan, pour recevoir des offres comparables.", "bot");
      m.appendChild(link("/guide-bien-demander-ses-devis.html", "Comment bien demander ses devis", false, "lien-guide-demander"));
      m.appendChild(link("/checklist-devis-travaux.pdf", "La check-list à imprimer (PDF)", false, "lien-checklist"));
      m.appendChild(link("https://docs.google.com/forms/d/e/1FAIpQLScS7zVctXEahK71wNv8hUGD-MjfyqH4h_l8EpJyYPLVM-ToAA/viewform", "Recevoir le conseil devis du mois", false, "lien-conseil-du-mois"));
    } else if (r.d === "semaine") {
      gc("resultat-urgent");
      m = add("Vous signez bientôt : faites relire le devis avant. Choisissez l'option express : vous recevez le rapport sous 24 h, avec les points à négocier et les questions à envoyer à l'artisan.", "bot");
      m.appendChild(document.createElement("br")); m.appendChild(link(COMEUP, "Faire analyser mon devis en express", true, "clic-comeup-orientation-urgent"));
    } else if (r.m === "plus-20k") {
      gc("resultat-gros-devis");
      m = add("Sur un devis de plus de 20 000 €, chaque ligne compte. Vous pouvez commander l'analyse directement, ou en parler d'abord lors d'un appel gratuit de 15 minutes.", "bot");
      m.appendChild(document.createElement("br")); m.appendChild(link(COMEUP, "Faire analyser mon devis", true, "clic-comeup-orientation-gros"));
      m.appendChild(link(BOOK, "Réserver l'appel gratuit de 15 min", false, "clic-appel-orientation"));
    } else {
      gc("resultat-standard");
      m = add("Le bon moment pour faire relire votre devis, c'est avant de le signer. Vous recevez sous 48 h un rapport avec le verdict, les prix poste par poste, les oublis et les questions à poser à l'artisan.", "bot");
      m.appendChild(document.createElement("br")); m.appendChild(link(COMEUP, "Faire analyser mon devis", true, "clic-comeup-orientation"));
      m.appendChild(link("/exemple-rapport-contre-plan.pdf", "Voir un exemple de rapport", false, "lien-exemple-rapport"));
    }
    if (page) m.appendChild(link(page[0], page[1], false, "lien-page-" + r.t));
    var w = document.createElement("div"); w.className = "cp-chips";
    var c = document.createElement("button"); c.type = "button"; c.className = "cp-chip"; c.textContent = "J'ai une autre question";
    c.onclick = function () { w.remove(); add("Choisissez une question ou écrivez la vôtre.", "bot"); chips(); };
    w.appendChild(c); log.appendChild(w); log.scrollTop = log.scrollHeight;
  }
  function welcome() {
    add("Bonjour ! Je vous oriente en 3 questions, ou je réponds à vos questions sur l'analyse de devis.", "bot");
    var w = document.createElement("div"); w.className = "cp-chips";
    [["J'ai un devis à faire vérifier", function () { qualify(); }], ["J'ai une question", function () { gc("faq-debut"); add("Choisissez une question ou écrivez la vôtre.", "bot"); chips(); }]].forEach(function (o) {
      var c = document.createElement("button"); c.type = "button"; c.className = "cp-chip"; c.textContent = o[0];
      c.onclick = function () { w.remove(); add(o[0], "user"); setTimeout(o[1], 250); }; w.appendChild(c);
    });
    log.appendChild(w); log.scrollTop = log.scrollHeight;
  }
  function open(v) {
    box.classList.toggle("open", v); btn.setAttribute("aria-expanded", v ? "true" : "false");
    if (v && !started) { started = true; gc("ouverture"); welcome(); }
    if (v) input.focus();
  }
  btn.onclick = function () { open(!box.classList.contains("open")); };
  box.querySelector("#cp-close").onclick = function () { open(false); btn.focus(); };
  box.querySelector("#cp-form").onsubmit = function (ev) { ev.preventDefault(); var t = input.value.trim(); if (!t) return; input.value = ""; ask(t); };
})();

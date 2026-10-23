import json, html, os
OUT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # racine du site
GC = '<script data-goatcounter="https://contreplan.goatcounter.com/count" async src="//gc.zgo.at/count.js"></script>'
COMEUP = "https://comeup.com/fr/@contreplan"
BOOK = "https://calendar.app.google/6LCc6yKVHnbvA3WN7"
DATE = "2026-10-23"  # date de publication par défaut des guides existants
MOIS = ["janvier","février","mars","avril","mai","juin","juillet","août","septembre","octobre","novembre","décembre"]
def date_fr(d):
    y, m, j = d.split("-")
    return f"{int(j)} {MOIS[int(m)-1]} {y}"
LASTMOD = {}

def head(title, desc, url, extra="", root=""):
    return f'''<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<link rel="icon" href="{root}favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="{root}favicon-32.png">
<link rel="apple-touch-icon" href="{root}apple-touch-icon.png">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="article">
<meta property="og:url" content="{url}">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:image" content="https://contre-plan.com/og-image.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Contre-Plan : votre devis de travaux relu ligne par ligne avant que vous signiez">
<meta name="twitter:card" content="summary_large_image">
<link rel="preload" href="{root}fonts/source-sans-3-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="{root}fonts/source-sans-3-latin-700-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="{root}fonts/archivo-latin-800-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{root}fonts.css">
<style>
body{{margin:0;background:#08111f}}
a{{color:#b8461a}}a:hover{{color:#8f3612}}
h1{{font-size:clamp(32px,5.5vw,48px)!important}}
.art h2{{font-family:Archivo,Arial,sans-serif;font-weight:800;font-size:clamp(22px,3.5vw,28px);line-height:1.2;color:#14284b;margin:40px 0 8px}}
.art h3{{font-size:20px;color:#14284b;margin:24px 0 4px}}
.art p,.art li{{font-size:18px;line-height:1.65;color:#33415f}}
.art p{{margin:0 0 14px}}
.art ul,.art ol{{margin:0 0 14px;padding-left:24px}}
.art li{{margin-bottom:8px}}
.art strong{{color:#14284b}}
.note{{background:#fff;border:1px solid #ddd8ca;border-left:4px solid #c44c19;border-radius:6px;padding:16px 20px;margin:20px 0}}
.note p{{margin:0}}
</style>
{extra}
<link rel="stylesheet" href="{root}anim.css">
<script src="{root}anim.js" defer></script>
<link rel="stylesheet" href="{root}site.css">
<script src="{root}site.js" defer></script>
{GC}
</head>
<body>
<div style="font-family: 'Source Sans 3', Arial, sans-serif; color: #14284b; background: #f3f0e8; width: 100%;">
<header style="background: #08111f;">
<div style="max-width: 1160px; margin: 0 auto; padding: 24px; display: flex; flex-wrap: wrap; gap: 16px; align-items: center; justify-content: space-between;">
<a href="{root or './'}" style="color: #ffffff; text-decoration: none; font-family: Archivo, Arial, sans-serif; font-weight: 800; font-size: 22px; letter-spacing: 2px;">CONTRE-PLAN</a>
<nav style="display: flex; flex-wrap: wrap; gap: 20px; align-items: center; font-size: 17px;">
<a href="{root}methode.html" style="color: #c9d3ea; text-decoration: none;">Méthode</a>
<a href="{root}guides.html" style="color: #c9d3ea; text-decoration: none;">Guides</a>
<a href="{COMEUP}" data-goatcounter-click="clic-comeup" style="background: #c44c19; color: #ffffff; text-decoration: none; font-weight: 700; padding: 12px 20px; border-radius: 4px;">Faire analyser mon devis</a>
</nav>
</div>
</header>
'''

def footer(root=""):
    return f'''<footer style="background: #08111f; color: #a9b6d3; border-top: 1px solid #1c2943;">
<div style="max-width: 1160px; margin: 0 auto; padding: 40px 24px; display: flex; flex-wrap: wrap; gap: 24px; justify-content: space-between; font-size: 15px; line-height: 1.6;">
<div><div style="color: #ffffff; font-family: Archivo, Arial, sans-serif; font-weight: 800; letter-spacing: 2px; font-size: 18px;">CONTRE-PLAN</div><div>Analyse de devis travaux · 100 % à distance</div></div>
<div style="display: flex; flex-wrap: wrap; gap: 20px; align-items: center; font-size: 13px;"><a href="{root}methode.html" style="color: #a9b6d3;">Méthode</a><a href="{root}engagements.html" style="color: #a9b6d3;">Engagements</a><a href="{root}guides.html" style="color: #a9b6d3;">Guides</a><a href="{root}mentions-legales.html" style="color: #a9b6d3; font-size: 11px;">Mentions légales</a><span>© 2026 Contre-Plan</span></div>
</div>
</footer>
</div>
<script src="{root}chat.js" defer></script>
</body>
</html>
'''

CTA = f'''<aside style="margin-top: 48px; background-color: #08111f; background-image: linear-gradient(#2d3d62 1px, transparent 1px), linear-gradient(90deg, #2d3d62 1px, transparent 1px); background-size: 80px 80px; color: #fff; border-radius: 8px; padding: 32px; display: flex; flex-direction: column; gap: 16px;">
<p style="margin: 0; font-family: Archivo, Arial, sans-serif; font-weight: 800; font-size: 26px; line-height: 1.2; color: #fff;">Un devis à signer ? Faites-le relire par un ingénieur BTP.</p>
<p style="margin: 0; font-size: 18px; line-height: 1.5; color: #c9d3ea;">Prix poste par poste, oublis, TVA, conditions de paiement : rapport PDF sous 48 h, 16,50 € au tarif de lancement.</p>
<div style="display: flex; flex-wrap: wrap; gap: 12px;"><a href="{COMEUP}" data-goatcounter-click="clic-comeup" style="background: #c44c19; color: #fff; text-decoration: none; font-weight: 700; font-size: 18px; padding: 16px 24px; border-radius: 4px;">Faire analyser mon devis</a><a href="{BOOK}" data-goatcounter-click="clic-appel" target="_blank" rel="noopener" style="color: #fff; font-weight: 700; font-size: 17px; padding: 14px 22px; border: 2px solid #fff; border-radius: 4px; text-decoration: none;">Appel gratuit de 15 min</a></div>
</aside>'''

ARTICLES = []
def article(slug, title, h1, desc, lead, body, readtime, date=DATE):
    url = f"https://contre-plan.com/{slug}.html"
    ld = {"@context":"https://schema.org","@type":"Article","headline":h1,"description":desc,
          "datePublished":date,"dateModified":date,"inLanguage":"fr-FR",
          "author":{"@type":"Organization","name":"Contre-Plan","url":"https://contre-plan.com/"},
          "publisher":{"@type":"Organization","name":"Contre-Plan","logo":{"@type":"ImageObject","url":"https://contre-plan.com/logo-512.png"}},
          "mainEntityOfPage":url}
    extra = '<script type="application/ld+json">' + json.dumps(ld, ensure_ascii=False) + '</script>'
    page = head(title, desc, url, extra) + f'''<main class="art" style="max-width: 760px; margin: 0 auto; padding: 56px 24px 96px;">
<p style="font-size: 15px; margin: 0 0 16px;"><a href="guides.html">Guides</a> <span style="color:#5b6784">›</span> <span style="color:#5b6784">{html.escape(h1)}</span></p>
<h1 style="margin: 0 0 16px; font-family: Archivo, Arial, sans-serif; font-weight: 800; line-height: 1.1; color: #14284b;">{html.escape(h1)}</h1>
<p style="font-size: 15px; color: #5b6784; margin: 0 0 28px;">Par un ingénieur BTP · mis à jour le {date_fr(date)} · lecture {readtime} min</p>
<p style="font-size: 20px !important; color: #14284b !important;">{lead}</p>
{body}
{CTA}
</main>
''' + footer()
    open(os.path.join(OUT, slug + ".html"), "w").write(page)
    ARTICLES.append((slug, h1, desc))
    LASTMOD[slug + ".html"] = date

# ---------- Article 1
article("guide-mentions-obligatoires-devis",
 "Mentions obligatoires d'un devis de travaux : la liste à vérifier | Contre-Plan",
 "Devis de travaux : les mentions obligatoires à vérifier avant de signer",
 "Assurance décennale, détail des postes, déchets, TVA, délais : la liste des mentions qu'un devis de travaux doit contenir, et ce que leur absence doit vous faire demander.",
 "Un devis signé vaut contrat. S'il est incomplet, c'est vous qui en supporterez les conséquences en cas de désaccord. Voici ce qu'un devis de travaux doit contenir, regroupé dans l'ordre où je le vérifie.",
 '''<h2>1. L'entreprise et son assurance</h2>
<ul>
<li><strong>Nom, forme juridique, adresse, numéro SIRET</strong> et <strong>immatriculation</strong> de l'entreprise (RCS et ville du greffe pour une société commerciale, Registre national des entreprises pour un artisan). Vérifiez le SIRET sur l'annuaire des entreprises de l'État : une entreprise radiée ou créée la veille est un signal à prendre au sérieux.</li>
<li><strong>L'assurance professionnelle</strong> : nom et coordonnées de l'assureur et zone géographique couverte. Pour les travaux qui touchent au bâti (gros œuvre, étanchéité, toiture, menuiseries, plomberie encastrée…), demandez l'<strong>attestation d'assurance décennale</strong> valable à la date d'ouverture du chantier, et vérifiez qu'elle couvre bien l'activité concernée.</li>
</ul>
<h2>2. Vous et le chantier</h2>
<ul>
<li>Votre nom et <strong>l'adresse exacte du chantier</strong>.</li>
<li>La <strong>date du devis</strong> et sa <strong>durée de validité</strong>.</li>
<li>La <strong>date de début</strong> et la <strong>date de fin ou le délai d'exécution</strong> auquel l'entreprise s'engage (par exemple « 3 semaines à compter du démarrage »). Une simple « durée indicative » ne l'engage à rien : demandez un délai ferme, c'est lui qui vous permettra d'agir si le chantier traîne.</li>
</ul>
<h2>3. Le détail des travaux</h2>
<p>C'est la partie la plus importante, et celle où je trouve le plus de problèmes.</p>
<ul>
<li>Chaque prestation doit être détaillée avec sa <strong>quantité</strong> (m², ml, unités) et son <strong>prix unitaire</strong>. Un « forfait salle de bain » ne permet ni de comparer ni de contester.</li>
<li>Les <strong>matériaux et équipements</strong> doivent être désignés précisément : marque, gamme, référence, dimensions. Sinon, rien ne vous garantit la qualité posée.</li>
<li>La <strong>main-d'œuvre</strong> et les éventuels <strong>frais de déplacement</strong> apparaissent clairement.</li>
<li>Les totaux <strong>HT et TTC</strong>, avec le ou les <strong>taux de TVA</strong> appliqués (voir notre <a href="guide-tva-travaux-renovation.html">guide sur la TVA des travaux</a>).</li>
</ul>
<h2>4. Les déchets de chantier</h2>
<p>Depuis le 1<sup>er</sup> juillet 2021, un devis de travaux doit indiquer l'<strong>estimation de la quantité de déchets</strong>, les <strong>modalités d'enlèvement et de tri</strong>, les <strong>points de collecte</strong> prévus et le <strong>coût estimé</strong> de cette gestion. C'est aussi un excellent révélateur : si l'évacuation n'est pas chiffrée, elle risque de revenir en supplément.</p>
<h2>5. Travaux de rénovation énergétique et aides</h2>
<p>Si vous visez MaPrimeRénov', les CEE ou un éco-PTZ, le devis doit aussi mentionner la <strong>qualification RGE</strong> de l'entreprise (organisme et numéro), les <strong>caractéristiques de performance</strong> des équipements et matériaux (résistance thermique de l'isolant, coefficient de performance d'une pompe à chaleur…) et les <strong>surfaces traitées</strong>. Un oubli peut faire perdre l'aide.</p>
<h2>6. Paiement et garanties</h2>
<ul>
<li>Les <strong>conditions de paiement</strong> : montant de l'acompte et échéancier. La loi ne fixe pas de plafond général, mais un acompte au-delà de 30 % avant le démarrage mérite d'être discuté.</li>
<li>Si le devis a été signé chez vous à la suite d'un démarchage, vous disposez en principe d'un <strong>délai de rétractation de 14 jours</strong>, et l'artisan ne peut en principe pas encaisser de paiement avant 7 jours (des exceptions existent, notamment pour les dépannages urgents que vous avez demandés).</li>
<li>Les <strong>garanties</strong> : garanties légales de conformité et des vices cachés, et pour le bâtiment la garantie de parfait achèvement (1 an), la garantie de bon fonctionnement des équipements (2 ans) et la garantie décennale.</li>
<li>Les <strong>conditions générales</strong>, au dos ou en annexe : lisez-les, notamment les clauses de <strong>révision de prix</strong> (hausse des matériaux) et de pénalités.</li>
<li>Les coordonnées du <strong>médiateur de la consommation</strong> dont relève l'entreprise : elle doit vous les communiquer, souvent sur le devis ou dans ses conditions générales. C'est votre recours amiable gratuit en cas de litige.</li>
<li>Si l'entreprise recueille votre numéro de téléphone, elle doit vous informer de votre droit de vous inscrire sur <strong>Bloctel</strong>, la liste d'opposition au démarchage téléphonique.</li>
</ul>
<div class="note"><p><strong>Le réflexe à avoir :</strong> une mention manque ? Demandez simplement un devis corrigé par écrit avant de signer. Un artisan sérieux le fait sans difficulté. À la signature, datez, signez et ajoutez « Bon pour accord » : vous gardez ainsi une trace claire de ce que vous avez accepté et quand.</p></div>
<h2>Ce que les mentions ne disent pas</h2>
<p>Un devis peut contenir toutes les mentions obligatoires et rester mauvais : un prix gonflé, un poste indispensable oublié, un enchaînement de travaux incohérent. C'est ce que je vérifie en plus, ligne par ligne, dans chaque analyse.</p>
<p style="font-size: 15px !important; color: #5b6784 !important;">Article d'information générale, qui ne remplace pas un conseil juridique. Sources : Code de la consommation, Code des assurances, décret n° 2020-1817 sur les déchets de chantier.</p>''', 6)

# ---------- Article 2
article("guide-tva-travaux-renovation",
 "TVA travaux 5,5 %, 10 % ou 20 % : quel taux sur votre devis ? | Contre-Plan",
 "TVA sur un devis de travaux : 5,5 %, 10 % ou 20 %, quel taux est le bon ?",
 "Rénovation énergétique, amélioration, neuf ou agrandissement : quel taux de TVA doit figurer sur votre devis de travaux, et la mention qui remplace l'attestation depuis 2025.",
 "Sur un devis de 15 000 € HT, passer de 10 % à 20 % de TVA, c'est 1 500 € de plus. Pourtant, je vois régulièrement des taux mal appliqués, dans les deux sens. Voici comment vérifier le vôtre.",
 '''<h2>La condition de base : un logement achevé depuis plus de 2 ans</h2>
<p>Les taux réduits ne s'appliquent qu'aux travaux dans des <strong>locaux d'habitation achevés depuis plus de deux ans</strong>. Ils sont exclus si les travaux, sur deux ans, aboutissent à un <strong>immeuble neuf</strong> ou <strong>augmentent la surface de plancher de plus de 10 %</strong>.</p>
<div class="note"><p><strong>Le piège de la rénovation lourde :</strong> même sans gagner un mètre carré, des travaux sont fiscalement considérés comme produisant un immeuble neuf s'ils remettent à neuf la majorité des fondations ou des éléments porteurs (murs, planchers, charpente), ou plus des deux tiers de <em>chacun</em> des éléments de second œuvre : planchers non porteurs, menuiseries extérieures, cloisons intérieures, plomberie et sanitaires, électricité et, en métropole, chauffage. Dans ce cas, tout passe à 20 %.</p></div>
<h2>5,5 % : la rénovation énergétique</h2>
<p>Le taux réduit concerne les travaux qui améliorent la performance énergétique et respectent des critères techniques précis : <strong>isolation</strong> (murs, toiture, planchers, fenêtres, portes d'entrée, volets isolants), certains <strong>équipements de chauffage et d'eau chaude utilisant les énergies renouvelables</strong>, certaines <strong>VMC</strong>, la régulation du chauffage, ainsi que les travaux indissociablement liés.</p>
<p>Attention : chaque équipement doit atteindre les performances minimales fixées par la réglementation. Le devis doit donc les préciser.</p>
<h2>10 % : amélioration, transformation, entretien</h2>
<p>C'est le taux de la plupart des rénovations : <strong>salle de bain, électricité, plomberie, peinture, carrelage, revêtements</strong>… Il s'applique à la main-d'œuvre et aux fournitures posées par l'entreprise.</p>
<p>Attention aux <strong>cuisines et meubles de salle de bain</strong> : la pose est à 10 %, mais la fourniture des meubles ne l'est que s'ils sont intégrés au bâti (sur mesure, encastrés). Des meubles standard simplement posés et l'<strong>électroménager</strong> restent à 20 % pour la fourniture.</p>
<h2>20 % : ce qui reste au taux normal</h2>
<ul>
<li>Les travaux dans un logement de <strong>moins de 2 ans</strong>, la <strong>construction neuve</strong> et les <strong>agrandissements</strong> au-delà du seuil de 10 %.</li>
<li>La fourniture et la pose d'une <strong>chaudière fonctionnant aux énergies fossiles</strong> (gaz, fioul).</li>
<li>La <strong>climatisation</strong>, y compris les pompes à chaleur air/air, pour la part équipement.</li>
<li>Le nettoyage et les espaces verts.</li>
<li>Les <strong>équipements que vous achetez vous-même</strong> : l'artisan ne peut appliquer le taux réduit qu'à la pose.</li>
</ul>
<h2>Fini l'attestation : une mention sur le devis</h2>
<p>Depuis la loi de finances pour 2025, l'attestation simplifiée (formulaire 1301-SD) n'est plus nécessaire. Elle est remplacée par une <strong>mention sur le devis ou la facture</strong>, que vous signez, par laquelle vous certifiez que les conditions du taux réduit sont remplies (logement de plus de 2 ans, pas d'immeuble neuf, pas d'agrandissement de plus de 10 %).</p>
<div class="note"><p><strong>Important :</strong> sans cette mention, ou si elle est incomplète, le taux normal de 20 % s'applique. Et si vos déclarations sont inexactes, vous pouvez être tenu de payer la différence de TVA. Conservez votre exemplaire signé jusqu'à la fin de la 5<sup>e</sup> année suivant les travaux.</p></div>
<h2>Un devis peut mélanger plusieurs taux</h2>
<p>C'est normal et fréquent : isolation à 5,5 %, reprise des cloisons à 10 %, climatiseur à 20 %. Ce qui ne l'est pas : un taux unique de 20 % sur une rénovation de logement ancien sans explication, ou au contraire un 5,5 % sur des travaux qui n'y ont pas droit. Dans le second cas, si l'erreur vient de ce que vous avez certifié (un logement de moins de 2 ans déclaré ancien, par exemple), vous pouvez être tenu de payer le complément de TVA avec l'entreprise.</p>
<p style="font-size: 15px !important; color: #5b6784 !important;">Article d'information générale, à jour au 24 octobre 2026. Les règles fiscales évoluent : vérifiez sur impots.gouv.fr. Sources : articles 278-0 bis A et 279-0 bis du Code général des impôts, loi n° 2025-127 du 14 février 2025.</p>''', 5)

# ---------- Article 3
article("guide-oublis-devis-salle-de-bain",
 "Devis salle de bain : les 7 oublis qui font exploser la facture | Contre-Plan",
 "Devis de salle de bain : les 7 oublis qui font grimper la facture",
 "Dépose, étanchéité, évacuation, électricité, ventilation : les postes souvent absents d'un devis de salle de bain, qui reviennent en supplément une fois le chantier lancé.",
 "Le devis le moins cher n'est pas toujours le moins cher à l'arrivée. Sur une salle de bain, les mauvaises surprises viennent presque toujours de ce qui n'est pas écrit. Voici les sept postes que je vérifie en premier.",
 '''<h2>1. La dépose et l'évacuation des gravats</h2>
<p>Retirer l'ancienne baignoire, la faïence et le carrelage prend du temps et génère des déchets. Si la dépose n'est pas chiffrée, ou si l'évacuation n'apparaît pas, attendez-vous à un supplément. Rappel : le devis doit d'ailleurs mentionner la gestion des déchets (voir <a href="guide-mentions-obligatoires-devis.html">les mentions obligatoires</a>).</p>
<div class="note"><p><strong>Logement dont le permis de construire date d'avant le 1<sup>er</sup> juillet 1997 :</strong> colles, carrelages, enduits ou faux plafonds peuvent contenir de l'amiante. Un repérage amiante avant travaux est en principe requis avant de les démolir. Parlez-en avec l'artisan avant de signer : qui le commande, et à quel prix.</p></div>
<h2>2. L'étanchéité sous carrelage</h2>
<p>C'est l'oubli le plus coûteux, parce qu'on ne le voit qu'une fois les dégâts faits. En zone de douche, et surtout pour une douche de plain-pied, un <strong>système d'étanchéité sous carrelage</strong> au sol et sur les murs exposés est indispensable. Un simple carrelage avec des joints ne suffit pas. Exigez que le système soit nommé sur le devis : en général un <strong>SPEC</strong> (système de protection à l'eau sous carrelage) sur les murs et le sol de la douche, ou un <strong>SEL</strong> (système d'étanchéité liquide) ou une natte d'étanchéité sous avis technique selon le support.</p>
<h2>3. La préparation des supports</h2>
<p>Après la dépose, les murs et le sol sont rarement prêts à recevoir un nouveau revêtement : ragréage, reprise de plâtre, plaques hydrofuges à poser. Un devis qui passe directement de « dépose » à « pose carrelage » cache souvent ce poste.</p>
<p>Attention à une idée reçue : une plaque de plâtre hydrofuge (la plaque verte) résiste à l'humidité, mais <strong>elle n'est pas étanche</strong>. Dans la douche, elle doit être recouverte par l'étanchéité du point 2.</p>
<h2>4. La plomberie et l'évacuation de la douche</h2>
<p>Une douche à l'italienne demande une pente vers le siphon ou le caniveau, et parfois de décaisser la dalle ou de rehausser le sol. Vérifiez que le type d'évacuation, sa position et la création de la pente sont prévus.</p>
<p>Côté alimentation, le devis doit préciser si les tuyaux sont refaits et en quel matériau (multicouche, PER, cuivre), et prévoir des <strong>robinets d'arrêt accessibles</strong> pour chaque appareil. Une fois la faïence posée, ce qui n'a pas été prévu derrière ne se rattrape plus.</p>
<h2>5. L'électricité de la pièce</h2>
<p>La salle de bain est découpée en <strong>volumes de sécurité</strong> autour de la douche et de la baignoire, avec des règles strictes sur ce qu'on peut y installer (norme NF C 15-100). Déplacer un point lumineux, ajouter un sèche-serviettes ou une prise pour le lavabo, c'est de l'électricité : si ce n'est pas sur le devis, ce sera un avenant.</p>
<h2>6. La ventilation</h2>
<p>Sans extraction d'air, l'humidité abîme les joints, la peinture et favorise les moisissures. Si la pièce n'a pas de bouche de VMC ou d'aérateur, ou si l'existant est déplacé, le poste doit apparaître.</p>
<h2>7. Les finitions</h2>
<p>Joints silicone, profilés d'angle, raccords de peinture, habillage de baignoire, plinthes, pose des accessoires : chaque poste est petit, mais leur absence cumulée peut représenter plusieurs centaines d'euros, ou une salle de bain « terminée » qui ne l'est pas.</p>
<div class="note"><p><strong>Et les conditions de paiement ?</strong> Un acompte d'environ 30 % à la signature est l'usage. Ensuite, privilégiez des paiements liés à l'avancement réel du chantier, et gardez un solde à régler à la réception, une fois les réserves levées.</p></div>
<h2>Comment l'utiliser</h2>
<p>Reprenez votre devis avec cette liste et cochez chaque point. Pour chaque absence, posez la question à l'artisan <strong>par écrit</strong> : soit le poste est inclus et il le précise, soit il le chiffre. Dans les deux cas, vous signez en sachant ce que vous payez.</p>
<p style="font-size: 15px !important; color: #5b6784 !important;">Article d'information générale. Chaque chantier est différent : en cas de doute sur un point technique, faites vérifier votre devis.</p>''', 5)


PAGES = []
def page(slug, title, h1, desc, lead, body, kicker):
    url = f"https://contre-plan.com/{slug}.html"
    ld = {"@context":"https://schema.org","@type":"WebPage","name":h1,"description":desc,"url":url,"inLanguage":"fr-FR",
          "publisher":{"@type":"Organization","name":"Contre-Plan","url":"https://contre-plan.com/"}}
    extra = '<script type="application/ld+json">' + json.dumps(ld, ensure_ascii=False) + '</script>'
    out = head(title, desc, url, extra).replace('<meta property="og:type" content="article">','<meta property="og:type" content="website">') + f'''<main class="art" style="max-width: 760px; margin: 0 auto; padding: 56px 24px 96px;">
<span style="display:inline-block;background:#14284b;color:#fff;font-weight:700;font-size:15px;letter-spacing:1.5px;text-transform:uppercase;padding:8px 14px;margin-bottom:18px;">{kicker}</span>
<h1 style="margin: 0 0 20px; font-family: Archivo, Arial, sans-serif; font-weight: 800; line-height: 1.1; color: #14284b;">{html.escape(h1)}</h1>
<p style="font-size: 20px !important; color: #14284b !important;">{lead}</p>
{body}
{CTA}
</main>
''' + footer()
    open(os.path.join(OUT, slug + ".html"), "w").write(out)
    PAGES.append(slug)

# ---------- Pages Méthode et Engagements
page("methode",
 "Ma méthode : ce que je vérifie sur un devis | Contre-Plan",
 "Ma méthode : ce que je vérifie sur chaque devis",
 "Recalcul, mentions obligatoires, TVA, oublis techniques, prix : la grille de contrôle appliquée à chaque devis de travaux analysé par Contre-Plan.",
 "Chaque devis passe par la même grille de contrôle, en cinq temps. Voici ce que je regarde, et pourquoi.",
 """<h2>1. Je relis et je recalcule tout</h2>
<p>Je reprends chaque ligne du devis dans un tableau : désignation, unité, quantité, prix unitaire, total. Je refais tous les calculs, des lignes jusqu'au total TTC.</p>
<ul><li>Erreurs de multiplication ou d'addition, TVA mal calculée.</li><li>Quantités incohérentes entre elles ou avec la surface annoncée (par exemple plus de faïence que de murs).</li><li>Postes en double, ou main-d'œuvre facturée deux fois.</li></ul>
<h2>2. Je vérifie la forme et les mentions obligatoires</h2>
<p>Un devis incomplet n'est pas forcément mauvais, mais il vous laisse sans recours en cas de problème. Je contrôle notamment :</p>
<ul><li>La date, la durée de validité, la date de début et un délai d'exécution ferme.</li><li>L'identité de l'entreprise : raison sociale, adresse, SIRET, immatriculation.</li><li>L'assurance décennale : assureur et zone géographique couverte, et je vous dis quelle attestation demander.</li><li>La gestion des déchets, le détail fourniture et main-d'œuvre, les marques et références.</li><li>Les conditions de paiement et l'acompte, les garanties, le médiateur de la consommation.</li><li>Le droit de rétractation si le devis a été signé chez vous.</li></ul>
<p>Le détail est expliqué dans le guide <a href="guide-mentions-obligatoires-devis.html">des mentions obligatoires d'un devis</a>.</p>
<h2>3. Je contrôle la TVA et les aides</h2>
<p>Je vérifie que le taux appliqué (5,5 %, 10 % ou 20 %) correspond à vos travaux et à votre logement, et que la mention à signer est prévue. Si vous visez des aides, je vérifie la qualification RGE de l'entreprise pour les travaux concernés. Voir aussi <a href="guide-tva-travaux-renovation.html">le guide TVA</a>.</p>
<h2>4. Je cherche ce qui manque et ce qui est flou</h2>
<p>C'est le cœur de mon travail d'ingénieur : repérer ce qui n'est pas écrit et qui coûtera cher plus tard.</p>
<ul><li>Les forfaits sans détail (« plomberie », « divers », « finitions ») et les unités inadaptées.</li><li>Les oublis classiques : préparation des supports, dépose et évacuation, protection du chantier, raccordements, mises en conformité, accès en hauteur, nettoyage.</li><li>Les points propres à chaque type de travaux : étanchéité et volumes électriques en salle de bain, liaisons frigorifiques et évacuation des condensats pour une pompe à chaleur, repérage amiante pour un logement ancien.</li><li>Les enchaînements de travaux incohérents entre les lots.</li></ul>
<h2>5. Je compare les prix</h2>
<p>Je compare les principaux prix unitaires à des ordres de grandeur récents, en tenant compte de votre région quand je la connais. Chaque poste est classé cohérent, bas ou élevé. Je regarde aussi la répartition entre fourniture et main-d'œuvre, et le niveau de l'acompte : l'usage est d'environ 30 % à la signature.</p>
<div class="note"><p>Les prix cités sont toujours des fourchettes indicatives : ils varient selon la région, l'accès au chantier et les matériaux. Je ne vous dirai jamais qu'un prix est « le bon » au centime près.</p></div>
<h2>Ce que vous recevez</h2>
<p>Un rapport PDF avec une synthèse, un verdict, les points prioritaires chiffrés, l'analyse poste par poste, les questions à poser à l'artisan et un récapitulatif des corrections. <a href="exemple-rapport-contre-plan.pdf" target="_blank" rel="noopener" data-goatcounter-click="telechargement-exemple-rapport">Voir un exemple de rapport complet (PDF)</a>.</p>
<p>Ce que couvre l'analyse, et ce qu'elle ne couvre pas, est détaillé dans <a href="engagements.html">mes engagements</a>.</p>""",
 "Méthode")

page("engagements",
 "Mes engagements : indépendance et confidentialité | Contre-Plan",
 "Mes engagements",
 "Indépendance vis-à-vis des artisans, confidentialité de vos devis, délais et portée de l'analyse : ce sur quoi Contre-Plan s'engage.",
 "Vous me confiez un document qui engage plusieurs milliers d'euros. Voici comment je le traite.",
 """<h2>Indépendance</h2>
<ul><li>Je ne touche aucune commission, d'aucune entreprise.</li><li>Je ne vous recommande ni ne vous revends aucun artisan.</li><li>Mon seul intérêt est que vous signiez un devis juste, quel que soit l'artisan que vous choisissez.</li></ul>
<h2>Confidentialité de vos devis</h2>
<ul><li>Vous pouvez masquer votre nom, votre adresse et vos coordonnées avant de m'envoyer le devis : ils ne sont pas nécessaires à l'analyse.</li><li>Votre devis sert uniquement à réaliser votre analyse. Il n'est jamais transmis à un artisan ni à un tiers à des fins commerciales.</li><li>Les documents sont conservés dans un espace professionnel sécurisé. Vous pouvez demander leur suppression à tout moment en écrivant à contact@contre-plan.com.</li><li>Pour certaines vérifications (recalculs, recherche de prix et de textes de référence), je m'aide d'outils logiciels. Chaque rapport est relu, corrigé et validé par moi avant de vous être envoyé.</li></ul>
<h2>Délais</h2>
<ul><li>Rapport sous 48 h, ou 24 h avec l'option express, à compter de la réception de votre devis complet.</li><li>Un échange de suivi est inclus : vous pouvez me poser une question après lecture du rapport.</li><li>Si un document manque ou est illisible, je vous le signale dès réception.</li></ul>
<h2>Commande et paiement</h2>
<p>Les commandes et le paiement passent par la plateforme ComeUp, selon ses conditions générales. Vous n'avez rien à régler en dehors de la plateforme.</p>
<h2>Portée de cette analyse</h2>
<p>Cette analyse est un avis technique établi à distance, uniquement à partir des documents et informations que vous avez transmis. Elle ne comprend pas de visite du chantier : les éléments non visibles ou non communiqués (état réel des supports et des réseaux, présence d'amiante, contraintes de copropriété ou d'urbanisme…) ne peuvent pas être évalués.</p>
<p>Les prix de référence cités sont des fourchettes indicatives. Ils varient selon la région, l'accès au chantier et les matériaux choisis.</p>
<p>Cet avis n'est ni une expertise judiciaire ou d'assurance, ni une mission de maîtrise d'œuvre, ni un conseil juridique. Il ne remplace pas le devoir de conseil de l'entreprise qui réalisera les travaux.</p>
<p>La décision de signer, de négocier ou de refuser le devis vous appartient. En cas de litige déjà engagé ou de travaux touchant la structure du bâtiment, faites appel à un expert ou à un professionnel qui pourra se rendre sur place.</p>
<p>Pour savoir précisément ce que je contrôle, voir <a href="methode.html">ma méthode</a>.</p>""",
 "Engagements")

# ---------- Guides index
cards = "".join(f'''<a href="{s}.html" style="display:flex;flex-direction:column;gap:10px;background:#fff;border:1px solid #ddd8ca;border-radius:6px;padding:28px;text-decoration:none;color:#14284b;">
<span style="font-family:Archivo,Arial,sans-serif;font-weight:800;font-size:22px;line-height:1.25;">{html.escape(h)}</span>
<span style="font-size:17px;line-height:1.5;color:#4a5b7e;">{html.escape(d)}</span>
<span style="margin-top:auto;font-weight:700;color:#b8461a;">Lire le guide →</span></a>''' for s,h,d in ARTICLES)
idx = head("Guides : bien lire un devis de travaux | Contre-Plan",
  "Guides pratiques d'un ingénieur BTP pour vérifier un devis de travaux avant de signer : mentions obligatoires, TVA, oublis fréquents.",
  "https://contre-plan.com/guides.html") + f'''<main style="max-width: 1160px; margin: 0 auto; padding: 56px 24px 96px; display:flex; flex-direction:column; gap:32px;">
<div style="display:flex;flex-direction:column;gap:12px;max-width:760px;">
<h1 style="margin:0;font-family:Archivo,Arial,sans-serif;font-weight:800;line-height:1.1;">Guides : bien lire un devis de travaux</h1>
<p style="margin:0;font-size:20px;line-height:1.5;color:#4a5b7e;">Ce que je vérifie sur chaque devis, expliqué simplement pour que vous puissiez le faire vous-même.</p>
</div>
<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:20px;">{cards}</div>
<a href="checklist-devis-travaux.pdf" download data-goatcounter-click="telechargement-checklist" style="display:flex;flex-wrap:wrap;gap:16px;align-items:center;justify-content:space-between;background:#14284b;color:#fff;border-radius:6px;padding:28px;text-decoration:none;"><span style="display:flex;flex-direction:column;gap:6px;"><span style="font-family:Archivo,Arial,sans-serif;font-weight:800;font-size:22px;">La check-list à imprimer : 20 points avant de signer</span><span style="font-size:17px;color:#c9d3ea;">Une page PDF gratuite, sans inscription. Cochez au fur et à mesure.</span></span><span style="background:#c44c19;font-weight:700;padding:14px 22px;border-radius:4px;">Télécharger le PDF</span></a>
</main>
''' + footer()
open(os.path.join(OUT, "guides.html"), "w").write(idx)

# ---------- 404 (absolute paths: served at any URL)
p404 = head("Page introuvable | Contre-Plan", "Cette page n'existe pas ou a été déplacée.", "https://contre-plan.com/404.html", root="/").replace('<meta property="og:type" content="article">','<meta name="robots" content="noindex">') + f'''<main style="background-color: #08111f; background-image: linear-gradient(#2d3d62 1px, transparent 1px), linear-gradient(90deg, #2d3d62 1px, transparent 1px); background-size: 160px 160px; color:#fff; min-height: 60vh;">
<div style="max-width: 760px; margin: 0 auto; padding: 120px 24px; display:flex; flex-direction:column; gap:24px;">
<span style="align-self:flex-start;background:#c44c19;color:#fff;font-weight:700;font-size:15px;letter-spacing:1.5px;text-transform:uppercase;padding:8px 14px;">Erreur 404</span>
<h1 style="margin:0;font-family:Archivo,Arial,sans-serif;font-weight:800;line-height:1.1;">Ce poste ne figure pas <span style="color:#e8733c;">sur le plan.</span></h1>
<p style="margin:0;font-size:20px;line-height:1.5;color:#c9d3ea;">La page que vous cherchez n'existe pas ou a été déplacée.</p>
<div style="display:flex;flex-wrap:wrap;gap:14px;"><a href="/" style="background:#c44c19;color:#fff;text-decoration:none;font-weight:700;font-size:18px;padding:16px 24px;border-radius:4px;">Retour à l'accueil</a><a href="/guides.html" style="color:#fff;font-weight:700;font-size:17px;padding:14px 22px;border:2px solid #fff;border-radius:4px;text-decoration:none;">Lire les guides</a></div>
</div>
</main>
''' + footer(root="/")
open(os.path.join(OUT, "404.html"), "w").write(p404)

# ---------- sitemap
urls = [("", "1.0"), ("guides.html","0.8")] + [(s+".html","0.7") for s,_,_ in ARTICLES] + [(s+".html","0.7") for s in PAGES] + [("checklist-devis-travaux.pdf","0.6"),("exemple-rapport-contre-plan.pdf","0.6")]
sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(f'  <url><loc>https://contre-plan.com/{u}</loc><lastmod>{LASTMOD.get(u, max([DATE] + list(LASTMOD.values())))}</lastmod><priority>{p}</priority></url>\n' for u,p in urls) + '</urlset>\n'
open(os.path.join(OUT, "sitemap.xml"), "w").write(sm)
print("ok", [a[0] for a in ARTICLES])

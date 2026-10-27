import json, html, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import nouveaux_guides as NG  # guides et pages ajoutés en octobre 2026
OUT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # racine du site
GC = '<script data-goatcounter="https://contreplan.goatcounter.com/count" async src="//gc.zgo.at/count.js"></script>'
COMEUP = "https://comeup.com/fr/@contreplan"
BOOK = "https://calendar.app.google/6LCc6yKVHnbvA3WN7"
NEWS = "https://docs.google.com/forms/d/e/1FAIpQLScS7zVctXEahK71wNv8hUGD-MjfyqH4h_l8EpJyYPLVM-ToAA/viewform"  # formulaire « Le conseil devis du mois »
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
<link rel="icon" type="image/png" sizes="192x192" href="{root}favicon-192.png">
<link rel="icon" href="{root}favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="{root}favicon-32.png">
<link rel="apple-touch-icon" href="{root}apple-touch-icon.png">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="theme-color" content="#0a1d3a">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="article">
<meta property="og:locale" content="fr_FR">
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
body{{margin:0;background:#0a1d3a}}
h1{{font-size:clamp(32px,5.5vw,48px)!important}}
.art h2{{font-family:Archivo,Arial,sans-serif;font-weight:800;font-size:clamp(22px,3.5vw,28px);line-height:1.2;color:#14284b;margin:40px 0 8px}}
.art h3{{font-size:20px;color:#14284b;margin:24px 0 4px}}
.art p,.art li{{font-size:18px;line-height:1.65;color:#33415f}}
.art p{{margin:0 0 14px}}
.art ul,.art ol{{margin:0 0 14px;padding-left:24px}}
.art li{{margin-bottom:8px}}
.art strong{{color:#14284b}}
.note{{margin:20px 0}}
.note p{{margin:0}}
</style>
{extra}
<link rel="stylesheet" href="{root}site.css">
<link rel="stylesheet" href="{root}brand.css">
<script src="{root}site.js" defer></script>
{GC}
</head>
<body>
<a class="cp-skip" href="#contenu">Aller au contenu</a>
<div class="cp-page">
<header class="cp-hd">
<div class="cp-hd-in">
<a class="logo" href="{root or './'}"><i aria-hidden="true"></i>CONTRE-PLAN</a>
<nav class="cp-topnav" aria-label="Navigation principale">
<a href="{root}methode.html">Méthode</a>
<a href="{root}index.html#travaux">Travaux</a>
<a href="{root}comparer-ses-devis.html">Outils</a>
<a href="{root}guides.html">Guides</a>
<a class="btn" href="{COMEUP}" data-goatcounter-click="clic-comeup">Faire analyser<span class="lg"> mon devis</span></a>
</nav>
</div>
</header>
'''

def FOOTER(root=""):
    def L(h, t, ev=""):
        e = f' data-goatcounter-click="{ev}"' if ev else ""
        return f'<a href="{root}{h}"{e}>{t}</a>'
    soc = "".join(f'<a href="{u}" target="_blank" rel="noopener me" data-goatcounter-click="{ev}" class="cp-soc">{t}</a>' for u, t, ev in [
        ("https://www.tiktok.com/@contreplan_", "TikTok", "clic-tiktok"), ("https://www.instagram.com/contreplan_/", "Instagram", "clic-instagram"),
        ("https://www.pinterest.fr/contreplan/", "Pinterest", "clic-pinterest")])
    return f"""<footer class="cp-foot"><div class="cp-foot-in">
<div class="cp-foot-brand"><div class="cp-foot-logo">CONTRE-PLAN</div><p>Votre devis de travaux relu par un ingénieur BTP avant que vous signiez. 100 % à distance, indépendant de tout artisan.</p><div class="cp-socs">{soc}</div></div>
<div class="cp-foot-col"><p>Le service</p>{L("methode.html","Ma méthode")}{L("engagements.html","Mes engagements")}{L("exemple-rapport-contre-plan.pdf","Exemple de rapport","telechargement-exemple-rapport")}{L("index.html#tarifs","Tarifs")}{L("contact.html","Contact")}<a href="{COMEUP}" data-goatcounter-click="clic-comeup">Commander sur ComeUp</a></div>
<div class="cp-foot-col"><p>Par travaux</p>{L("analyse-devis-salle-de-bain.html","Salle de bain")}{L("analyse-devis-pompe-a-chaleur.html","Pompe à chaleur")}{L("analyse-devis-isolation.html","Isolation")}{L("analyse-devis-toiture.html","Toiture")}{''.join(L(j['slug'] + '.html', j['kicker']) for j in NG.JOB_PAGES)}{L("cas-fictifs.html","Cas fictifs")}</div>
<div class="cp-foot-col"><p>Ressources</p>{L("guides.html","Guides")}{L("comparer-ses-devis.html","Tableau comparatif")}{L("modeles-messages-artisan.html","Modèles de messages")}{L("lexique-devis-travaux.html","Lexique")}{L("checklist-devis-travaux.pdf","Check-list PDF","telechargement-checklist")}<a href="{NEWS}" target="_blank" rel="noopener" data-goatcounter-click="clic-conseil-du-mois">Le conseil du mois par email</a></div>
</div><div class="cp-foot-bottom"><span>© 2026 Contre-Plan</span><a href="{root}mentions-legales.html" class="cp-ml">Mentions légales</a><a href="{root}cgv.html" class="cp-ml">CGV</a><a href="{root}confidentialite.html" class="cp-ml">Confidentialité</a></div></footer>"""

def footer(root=""):
    return FOOTER(root) + f"""
</div>
<script src="{root}chat.js" defer></script>
</body>
</html>
"""

CTA = f'''<aside class="cp-cta-box bp">
<span class="tag">Avant de signer</span>
<p class="t">Un devis à signer ? Faites-le relire par un ingénieur BTP.</p>
<p>Prix poste par poste, oublis, TVA, conditions de paiement : rapport PDF sous 48 h, 16,50 € au tarif de lancement.</p>
<div class="row"><a class="btn" href="{COMEUP}" data-goatcounter-click="clic-comeup">Faire analyser mon devis</a><a class="btn line" href="{BOOK}" data-goatcounter-click="clic-appel" target="_blank" rel="noopener">Appel gratuit de 15 min</a></div>
<small>Paiement sécurisé sur ComeUp. Rapport PDF sous 48 h. Aucun engagement envers l'artisan.</small>
</aside>'''

SIDE = f"""<div class="cp-sidecard"><p class="t">Votre devis relu par un ingénieur BTP</p><p>Rapport PDF sous 48 h, prix poste par poste, oublis et questions à poser. Dès 16,50 €.</p><a class="cp-btn" href="{COMEUP}" data-goatcounter-click="clic-comeup-side">Faire analyser mon devis</a><a class="cp-sublink" href="exemple-rapport-contre-plan.pdf" target="_blank" rel="noopener" data-goatcounter-click="telechargement-exemple-rapport">Voir un exemple de rapport</a></div>
<div class="cp-sidelinks"><p>Outils gratuits</p><a href="index.html#test">Test : votre devis est-il complet ?</a><a href="comparer-ses-devis.html">Tableau comparatif de devis</a><a href="modeles-messages-artisan.html">Modèles de messages</a><a href="checklist-devis-travaux.pdf" download data-goatcounter-click="telechargement-checklist">Check-list à imprimer</a><a href="{NEWS}" target="_blank" rel="noopener" data-goatcounter-click="clic-conseil-du-mois">Le conseil du mois par email</a></div>"""

def slug_id(t):
    t = t.lower()
    for a_, b_ in (("é","e"),("è","e"),("ê","e"),("ë","e"),("à","a"),("â","a"),("ç","c"),("î","i"),("ï","i"),("ô","o"),("ù","u"),("û","u"),("œ","oe"),("’","-"),("'","-")):
        t = t.replace(a_, b_)
    return re.sub(r"[^a-z0-9]+", "-", t).strip("-")[:60]

def pagehero(kicker, h1, lead, meta, crumbs):
    cr = ' <span aria-hidden="true">›</span> '.join(f'<a href="{h}">{html.escape(t)}</a>' if h else f'<span aria-current="page">{html.escape(t)}</span>' for t, h in crumbs)
    m = f'<p class="cp-meta">{meta}</p>' if meta else ''
    return f'<section class="cp-ph"><div class="cp-ph-in"><nav class="cp-crumbs" aria-label="Fil d\'Ariane">{cr}</nav><span class="cp-kick">{kicker}</span><h1>{html.escape(h1)}</h1><p class="cp-lead">{lead}</p>{m}</div></section>'

def crumbs_ld(crumbs, url):
    items = [{"@type":"ListItem","position":i+1,"name":t,"item":("https://contre-plan.com/" + (h if h != "index.html" else "")) if h else url} for i,(t,h) in enumerate(crumbs)]
    return '<script type="application/ld+json">' + json.dumps({"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":items}, ensure_ascii=False) + '</script>'

def layout(body, toc_on=True):
    toc = []
    def rep(m):
        txt = html.unescape(re.sub(r"<[^>]+>", "", m.group(1))); i = slug_id(txt); toc.append((i, re.sub(r"^\d+\.\s*", "", txt))); return f'<h2 id="{i}">{m.group(1)}</h2>'
    body = re.sub(r"<h2>(.*?)</h2>", rep, body)
    show = toc_on and len(toc) >= 3
    tl = "".join(f'<li><a href="#{i}">{html.escape(t)}</a></li>' for i, t in toc)
    side_toc = f'<nav class="cp-toc" aria-label="Sommaire"><p>Sommaire</p><ol>{tl}</ol></nav>' if show else ''
    mob_toc = f'<details class="cp-toc-m"><summary>Sommaire</summary><ol>{tl}</ol></details>' if show else ''
    return f'<div class="cp-wrap" id="contenu"><main class="art">{mob_toc}{body}{CTA}</main><aside class="cp-side">{side_toc}{SIDE}</aside></div>'

# FAQ des guides (section visible + données structurées FAQPage) et date de mise à jour
FAQS = {
    'guide-acompte-paiement-devis-travaux': [
        ("Quel acompte verser à la signature d'un devis de travaux ?",
         "Aucun texte ne fixe de plafond général chez un particulier. L'usage est d'environ 30 % à la signature, parfois un peu plus pour des matériaux sur mesure. Au-delà de 40 à 50 %, demandez pourquoi et proposez un échéancier."),
        ('Quelle différence entre acompte et arrhes ?',
         "Avec des arrhes, chacun peut renoncer : vous en perdant les arrhes, l'entreprise en vous rendant le double. Avec un acompte, le contrat est ferme des deux côtés. Sauf mention contraire, les sommes versées d'avance sont considérées comme des arrhes."),
        ('Peut-on payer un artisan juste après avoir signé chez soi ?',
         "En principe non : après une signature à domicile, l'entreprise ne peut rien encaisser pendant 7 jours, sauf exceptions, et vous disposez de 14 jours pour vous rétracter. Ne remettez ni chèque ni autorisation de prélèvement pendant ce délai."),
    ],
    'guide-bien-demander-ses-devis': [
        ('Combien de devis demander pour des travaux ?',
         'Trois devis suffisent en général pour situer les prix. Au-delà, la comparaison devient difficile et les artisans les plus demandés risquent de ne pas répondre.'),
        ('Comment comparer des devis de travaux entre eux ?',
         "Donnez la même description écrite à chaque artisan, demandez les quantités et prix unitaires de chaque prestation, puis comparez poste par poste. Demandez aussi que la dépose, l'évacuation des déchets, la protection du chantier et le nettoyage soient chiffrés."),
        ("Que vérifier sur l'entreprise avant de signer ?",
         "Son immatriculation sur annuaire-entreprises.data.gouv.fr, sa qualification RGE sur france-renov.gouv.fr si vous visez des aides, et son attestation d'assurance décennale."),
    ],
    'guide-mentions-obligatoires-devis': [
        ("Quelles informations sur l'entreprise doivent figurer sur un devis ?",
         "Son nom, sa forme juridique, son adresse, son numéro SIRET et son immatriculation, ainsi que son assurance professionnelle avec le nom de l'assureur et la zone couverte. Pour les travaux qui touchent au bâti, demandez aussi l'attestation décennale valable à l'ouverture du chantier."),
        ('Le devis doit-il parler des déchets de chantier ?',
         "Oui. Depuis le 1er juillet 2021, il doit indiquer l'estimation de la quantité de déchets, les modalités d'enlèvement et de tri, les points de collecte et le coût estimé de cette gestion."),
        ('Que faire si une mention manque sur mon devis ?',
         'Demandez un devis corrigé par écrit avant de signer. Un artisan sérieux le fait sans difficulté.'),
    ],
    'guide-oublis-devis-salle-de-bain': [
        ("Quel est l'oubli le plus coûteux sur un devis de salle de bain ?",
         "L'étanchéité sous carrelage, parce qu'on ne la voit qu'une fois les dégâts faits. En zone de douche, un système d'étanchéité au sol et sur les murs exposés est indispensable, et il doit être nommé sur le devis."),
        ('Une plaque de plâtre hydrofuge suffit-elle dans une douche ?',
         "Non. La plaque hydrofuge résiste à l'humidité mais elle n'est pas étanche : dans la douche, elle doit être recouverte par un système d'étanchéité."),
        ('Faut-il un repérage amiante avant de rénover une salle de bain ?',
         "Si le permis de construire date d'avant le 1er juillet 1997, colles, carrelages, enduits ou faux plafonds peuvent contenir de l'amiante, et un repérage avant travaux est en principe requis avant de les démolir. Voyez avec l'artisan qui le commande et à quel prix."),
    ],
    'guide-reception-travaux-reserves': [
        ('Que se passe-t-il si je ne note pas un défaut à la réception ?',
         'Un défaut visible le jour de la réception et non noté en réserve est considéré comme accepté. Vous ne pourrez en principe plus le réclamer au titre des garanties.'),
        ('Puis-je garder une partie du solde tant que les réserves ne sont pas levées ?',
         "Une retenue de garantie d'au plus 5 % est possible si le devis signé la prévoit. Elle doit être consignée auprès d'un tiers, un notaire par exemple, et non gardée chez vous. Elle est libérée un an après la réception, sauf opposition motivée notifiée avant."),
        ("Que faire si l'entreprise refuse de signer le procès-verbal avec réserves ?",
         "Ne signez pas un procès-verbal sans réserves. Rédigez-le vous-même avec vos réserves, indiquez le refus de l'entreprise présente ou dûment convoquée, joignez les photos et envoyez-le en recommandé avec accusé de réception."),
    ],
    'guide-tva-travaux-renovation': [
        ('Quel taux de TVA pour une rénovation de salle de bain ?',
         "En général 10 %, sur la main-d'œuvre et les fournitures posées par l'entreprise, si le logement est achevé depuis plus de deux ans. La fourniture des meubles standard simplement posés et de l'électroménager reste à 20 %."),
        ("L'attestation de TVA 1301-SD est-elle encore nécessaire ?",
         "Non. Depuis la loi de finances pour 2025, elle est remplacée par une mention sur le devis ou la facture, que vous signez pour certifier que les conditions du taux réduit sont remplies. Sans cette mention, le taux de 20 % s'applique."),
        ('Un même devis peut-il avoir plusieurs taux de TVA ?',
         "Oui, c'est normal et fréquent : par exemple isolation à 5,5 %, reprise des cloisons à 10 % et climatiseur à 20 %. Un taux unique de 20 % sur la rénovation d'un logement ancien, sans explication, mérite en revanche une question."),
    ],
}
UPDATED = {'guide-acompte-paiement-devis-travaux': "2026-10-26", 'guide-bien-demander-ses-devis': "2026-10-26", 'guide-mentions-obligatoires-devis': "2026-10-26", 'guide-oublis-devis-salle-de-bain': "2026-10-26", 'guide-reception-travaux-reserves': "2026-10-26", 'guide-tva-travaux-renovation': "2026-10-26"}
for _s in ['guide-tva-travaux-renovation','guide-mentions-obligatoires-devis','guide-reception-travaux-reserves','guide-verifier-assurance-decennale','guide-negocier-devis-travaux','guide-depassement-devis-travaux-supplementaires','guide-annuler-devis-signe-retractation']:
    UPDATED[_s] = "2026-10-27"  # relecture et corrections du 27/10/2026
AUTEUR = "Rédigé par l'<a href=\"methode.html\">ingénieur BTP de Contre-Plan</a> (10 ans d'expérience, environ 1 000 devis lus)"

# Liens vers les sources officielles (bloc « Pour aller plus loin », vérifiés le 27/10/2026)
SP = "https://www.service-public.gouv.fr/particuliers/vosdroits/"
LINKS = {
    'guide-verifier-assurance-decennale': [(SP + "F2034", "Garantie décennale des constructeurs"), (SP + "F2032", "Assurance dommages-ouvrage")],
    'guide-negocier-devis-travaux': [(SP + "F2533", "Devis et contrat avant des travaux")],
    'guide-depassement-devis-travaux-supplementaires': [(SP + "F2533", "Devis et contrat avant des travaux"), (SP + "R24080", "Modèle de lettre : contester une facture qui dépasse le devis")],
    'guide-annuler-devis-signe-retractation': [(SP + "F23224", "Démarchage à domicile : règles à respecter"), (SP + "F2434", "Crédit affecté")],
    'guide-reception-travaux-reserves': [(SP + "F2958", "Garanties après la réception des travaux")],
    'guide-mentions-obligatoires-devis': [(SP + "F2533", "Devis et contrat avant des travaux"), ("https://entreprendre.service-public.gouv.fr/vosdroits/F23568", "TVA des travaux dans les logements")],
    'guide-acompte-paiement-devis-travaux': [(SP + "F31187", "Acompte, arrhes, avance : quelles différences ?"), ("https://www.economie.gouv.fr/dgccrf/les-fiches-pratiques/vente-hors-etablissement-soyez-vigilant", "Vente hors établissement (DGCCRF)")],
    'guide-oublis-devis-salle-de-bain': [(SP + "F288", "Habitat contenant de l'amiante"), ("https://entreprendre.service-public.gouv.fr/vosdroits/F23568", "TVA des travaux dans les logements")],
    'guide-bien-demander-ses-devis': [(SP + "F2533", "Devis et contrat avant des travaux"), ("https://entreprendre.service-public.gouv.fr/vosdroits/F32251", "Mention RGE : comment la vérifier"), ("https://annuaire-entreprises.data.gouv.fr/", "Annuaire des entreprises de l'État")],
    'guide-tva-travaux-renovation': [("https://entreprendre.service-public.gouv.fr/vosdroits/F23568", "TVA des travaux dans les logements"), (SP.replace("vosdroits/", "actualites/") + "A19002", "TVA à 5,5 % pour les pompes à chaleur air/air")],
    'analyse-devis-cuisine': [("https://bofip.impots.gouv.fr/bofip/1666-PGP.html/identifiant=BOI-TVA-LIQ-30-20-90-20-20260909", "TVA des cuisines (BOFiP, impots.gouv.fr)"), (SP + "F2533", "Devis, contrat et rétractation")],
    'analyse-devis-electricite': [("https://www.consuel.com/questions-frequentes/", "Questions fréquentes du Consuel"), ("https://entreprendre.service-public.gouv.fr/vosdroits/F23568", "TVA des travaux dans les logements")],
    'analyse-devis-extension': [(SP + "F36777", "Autorisation pour un agrandissement"), (SP + "F2032", "Assurance dommages-ouvrage")],
    'analyse-devis-fenetres': [(SP + "F35083", "MaPrimeRénov'"), (SP + "F36762", "Autorisation pour changer des fenêtres")],
    'analyse-devis-ravalement-facade': [(SP + "F36779", "Autorisation pour un ravalement"), (SP + "F33682", "Obligation d'isoler lors d'un ravalement ou d'une réfection de toiture")],
    'analyse-devis-salle-de-bain': [("https://entreprendre.service-public.gouv.fr/vosdroits/F23568", "TVA des travaux dans les logements"), (SP + "F288", "Habitat contenant de l'amiante")],
    'analyse-devis-pompe-a-chaleur': [(SP.replace("vosdroits/", "actualites/") + "A19002", "TVA à 5,5 % pour les pompes à chaleur air/air"), (SP + "F35083", "MaPrimeRénov'")],
    'analyse-devis-isolation': [(SP + "F33682", "Obligation d'isoler"), (SP + "F35083", "MaPrimeRénov'")],
    'analyse-devis-toiture': [(SP + "F36767", "Autorisation pour des travaux de toiture"), (SP + "F33682", "Obligation d'isoler lors d'une réfection de toiture")],
}

def links_html(slug):
    L = LINKS.get(slug)
    if not L:
        return ""
    items = " · ".join(f'<a href="{u}" target="_blank" rel="noopener">{html.escape(t)}</a>' for u, t in L)
    return f'<p class="cp-src"><strong>Sources officielles pour aller plus loin :</strong> {items}</p>'

# Liens internes ajoutés en fin de page « analyse de devis » (maillage vers les guides récents)
SEE_ALSO = {
    "guide-verifier-assurance-decennale": "vérifier l'assurance décennale de l'artisan",
    "guide-annuler-devis-signe-retractation": "annuler un devis signé ou se rétracter",
    "guide-negocier-devis-travaux": "négocier un devis sans se fâcher avec l'artisan",
}
SEE_ALSO_PAGES = {
    "analyse-devis-cuisine": ["guide-verifier-assurance-decennale", "guide-negocier-devis-travaux"],
    "analyse-devis-electricite": ["guide-verifier-assurance-decennale", "guide-negocier-devis-travaux"],
    "analyse-devis-extension": ["guide-negocier-devis-travaux"],
    "analyse-devis-fenetres": ["guide-verifier-assurance-decennale", "guide-annuler-devis-signe-retractation"],
    "analyse-devis-ravalement-facade": ["guide-verifier-assurance-decennale", "guide-negocier-devis-travaux"],
    "analyse-devis-salle-de-bain": ["guide-verifier-assurance-decennale", "guide-negocier-devis-travaux"],
    "analyse-devis-pompe-a-chaleur": ["guide-verifier-assurance-decennale", "guide-annuler-devis-signe-retractation"],
    "analyse-devis-isolation": ["guide-verifier-assurance-decennale", "guide-annuler-devis-signe-retractation"],
    "analyse-devis-toiture": ["guide-verifier-assurance-decennale", "guide-negocier-devis-travaux"],
}

def see_also_html(slug, body):
    items = [g for g in SEE_ALSO_PAGES.get(slug, []) if g + ".html" not in body]
    if not items:
        return ""
    return "<p>À lire aussi : " + ", ".join(f'<a href="{g}.html">{SEE_ALSO[g]}</a>' for g in items) + ".</p>"

    block = see_also_html(slug, body) + ("\n" if slug in SEE_ALSO_PAGES else "") + links_html(slug)
    block = block.strip()
def with_links(body, slug, before='<p style="font-size: 15px'):
    block = (see_also_html(slug, body) + "\n" + links_html(slug)).strip()
    if not block:
        return body
    i = body.rfind(before)
    if i == -1:
        return body.rstrip("\n") + "\n" + block
    return body[:i].rstrip("\n") + "\n" + block + "\n" + body[i:]

def faq_html(qa):
    return "<h2>Questions fréquentes</h2>\n" + "\n".join(f"<h3>{q}</h3>\n<p>{a}</p>" for q, a in qa)

def faq_ld(qa):
    return '<script type="application/ld+json">' + json.dumps({"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
        {"@type":"Question","name":html.unescape(re.sub(r"<[^>]+>", "", q)),"acceptedAnswer":{"@type":"Answer","text":html.unescape(re.sub(r"<[^>]+>", "", a))}} for q, a in qa]}, ensure_ascii=False) + '</script>'

def with_faq(body, qa, before='<p style="font-size: 15px'):
    """Insère la FAQ avant le marqueur `before` (par défaut la note de sources en petit) s'il existe, sinon en fin de corps."""
    block = faq_html(qa)
    i = body.find(before)
    if i == -1:
        return body.rstrip("\n") + "\n" + block
    return body[:i].rstrip("\n") + "\n" + block + "\n" + body[i:]

ARTICLES = []
def article(slug, title, h1, desc, lead, body, readtime, date=DATE):
    url = f"https://contre-plan.com/{slug}.html"
    mod = UPDATED.get(slug, date)
    qa = FAQS.get(slug)
    ld = {"@context":"https://schema.org","@type":"Article","headline":h1,"description":desc,
          "datePublished":date,"dateModified":mod,"inLanguage":"fr-FR",
          "author":{"@type":"Organization","name":"Contre-Plan","url":"https://contre-plan.com/",
                    "description":"Analyse de devis de travaux par un ingénieur BTP (10 ans d'expérience, environ 1 000 devis lus)"},
          "publisher":{"@type":"Organization","name":"Contre-Plan","logo":{"@type":"ImageObject","url":"https://contre-plan.com/logo-512.png"}},
          "mainEntityOfPage":url,"image":"https://contre-plan.com/og-image.jpg"}
    extra = '<script type="application/ld+json">' + json.dumps(ld, ensure_ascii=False) + '</script>'
    crumbs = [("Accueil", "index.html"), ("Guides", "guides.html"), (h1, None)]
    extra += crumbs_ld(crumbs, url) + ("\n" + faq_ld(qa) if qa else "")
    if qa:
        body = with_faq(body, qa)
    body = with_links(body, slug)
    page = head(title, desc, url, extra) + pagehero("Guide", h1, lead, f"Mis à jour le {date_fr(mod)}, lecture {readtime} min · {AUTEUR}", crumbs) + layout(body) + footer()
    open(os.path.join(OUT, slug + ".html"), "w").write(page)
    ARTICLES.append((slug, h1, desc, readtime))
    LASTMOD[slug + ".html"] = mod

# ---------- Article 1
article("guide-mentions-obligatoires-devis",
 "Mentions obligatoires d'un devis de travaux : la check-list",
 "Devis de travaux : les mentions obligatoires à vérifier avant de signer",
 "Assurance décennale, détail des postes, déchets, TVA, délais : les mentions qu'un devis de travaux doit contenir, et quoi demander si elles manquent.",
 "Un devis signé vaut contrat. S'il est incomplet, c'est vous qui en supporterez les conséquences en cas de désaccord. Voici ce qu'un devis de travaux doit contenir, regroupé dans l'ordre où je le vérifie.",
 '''<h2>1. L'entreprise et son assurance</h2>
<ul>
<li><strong>Nom, forme juridique, adresse, numéro SIRET</strong> et <strong>immatriculation</strong> de l'entreprise (RCS et ville du greffe pour une société commerciale, Registre national des entreprises pour un artisan). Vérifiez le SIRET sur l'annuaire des entreprises de l'État : une entreprise radiée ou créée la veille est un signal à prendre au sérieux.</li>
<li><strong>L'assurance professionnelle</strong> : nom et coordonnées de l'assureur et zone géographique couverte. Pour les travaux qui touchent au bâti (gros œuvre, étanchéité, toiture, menuiseries, plomberie encastrée…), demandez l'<strong>attestation d'assurance décennale</strong> valable à la date d'ouverture du chantier, et vérifiez qu'elle couvre bien l'activité concernée (<a href="guide-verifier-assurance-decennale.html">comment lire l'attestation décennale</a>).</li>
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
<li>Les <strong>conditions de paiement</strong> : montant de l'acompte et échéancier. La loi ne fixe pas de plafond général, mais l'usage est d'environ 30 % à la signature : au-delà de 40 à 50 %, demandez pourquoi.</li>
<li>Si le devis a été signé chez vous à la suite d'un démarchage, vous disposez en principe d'un <strong>délai de rétractation de 14 jours</strong>, et l'artisan ne peut en principe pas encaisser de paiement avant 7 jours (des exceptions existent, notamment pour les dépannages urgents que vous avez demandés). Le détail est dans <a href="guide-annuler-devis-signe-retractation.html">le guide pour annuler un devis signé</a>.</li>
<li>Les <strong>garanties</strong> : garanties légales de conformité et des vices cachés, et pour le bâtiment la garantie de parfait achèvement (1 an), la garantie de bon fonctionnement des équipements (2 ans) et la garantie décennale. Elles démarrent toutes à la <a href="guide-reception-travaux-reserves.html">réception des travaux</a>.</li>
<li>Les <strong>conditions générales</strong>, au dos ou en annexe : lisez-les, notamment les clauses de <strong>révision de prix</strong> (hausse des matériaux) et de pénalités. Un supplément en cours de chantier doit passer par un avenant écrit : voir <a href="guide-depassement-devis-travaux-supplementaires.html">dépassement de devis et travaux supplémentaires</a>.</li>
<li>Les coordonnées du <strong>médiateur de la consommation</strong> dont relève l'entreprise : elle doit vous les communiquer, souvent sur le devis ou dans ses conditions générales. C'est votre recours amiable gratuit en cas de litige.</li>
<li>Si l'entreprise recueille votre numéro de téléphone, elle doit vous informer de votre droit de vous inscrire sur <strong>Bloctel</strong>, la liste d'opposition au démarchage téléphonique.</li>
</ul>
<div class="note"><p><strong>Le réflexe à avoir :</strong> une mention manque ? Demandez simplement un devis corrigé par écrit avant de signer. Un artisan sérieux le fait sans difficulté. À la signature, datez, signez et ajoutez « Bon pour accord » : vous gardez ainsi une trace claire de ce que vous avez accepté et quand.</p></div>
<h2>Ce que les mentions ne disent pas</h2>
<p>Un devis peut contenir toutes les mentions obligatoires et rester mauvais : un prix gonflé, un poste indispensable oublié, un enchaînement de travaux incohérent. C'est ce que je vérifie en plus, ligne par ligne, dans chaque analyse.</p>
<p style="font-size: 15px !important; color: #5b6784 !important;">Article d'information générale, qui ne remplace pas un conseil juridique. Sources : Code de la consommation, Code des assurances, décret n° 2020-1817 sur les déchets de chantier.</p>''', 6)

# ---------- Article 2
article("guide-tva-travaux-renovation",
 "TVA travaux 5,5 %, 10 % ou 20 % : quel taux sur votre devis ?",
 "TVA sur un devis de travaux : 5,5 %, 10 % ou 20 %, quel taux est le bon ?",
 "Rénovation énergétique, amélioration, neuf, agrandissement : quel taux de TVA sur votre devis, et la mention qui remplace l'attestation depuis 2025.",
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
<li>La <strong>climatisation</strong> seule, pour la part équipement. Attention : depuis le 18 juillet 2026, les <strong>pompes à chaleur air/air réversibles</strong> fixes peuvent passer à 5,5 % si elles respectent des critères précis (classe énergétique, fluide frigorigène, pilotage à distance). Le devis doit alors les indiquer.</li>
<li>Le nettoyage et les espaces verts.</li>
<li>Les <strong>équipements que vous achetez vous-même</strong> : l'artisan ne peut appliquer le taux réduit qu'à la pose.</li>
</ul>
<h2>Fini l'attestation : une mention sur le devis</h2>
<p>Depuis la loi de finances pour 2025, l'attestation simplifiée (formulaire 1301-SD) n'est plus nécessaire. Elle est remplacée par une <strong>mention sur le devis ou la facture</strong>, que vous signez, par laquelle vous certifiez que les conditions du taux réduit sont remplies (logement de plus de 2 ans, pas d'immeuble neuf, pas d'agrandissement de plus de 10 %).</p>
<div class="note"><p><strong>Important :</strong> sans cette mention, ou si elle est incomplète, le taux normal de 20 % s'applique. Et si vos déclarations sont inexactes, vous pouvez être tenu de payer la différence de TVA. Conservez votre exemplaire signé jusqu'à la fin de la 5<sup>e</sup> année suivant les travaux.</p></div>
<h2>Un devis peut mélanger plusieurs taux</h2>
<p>C'est normal et fréquent : isolation à 5,5 %, reprise des cloisons à 10 %, climatiseur à 20 %. Ce qui ne l'est pas : un taux unique de 20 % sur une rénovation de logement ancien sans explication, ou au contraire un 5,5 % sur des travaux qui n'y ont pas droit. Dans le second cas, si l'erreur vient de ce que vous avez certifié (un logement de moins de 2 ans déclaré ancien, par exemple), vous pouvez être tenu de payer le complément de TVA avec l'entreprise.</p>
<p style="font-size: 15px !important; color: #5b6784 !important;">Article d'information générale, à jour au 27 octobre 2026. Les règles fiscales évoluent : vérifiez sur impots.gouv.fr. Sources : articles 278-0 bis A et 279-0 bis du Code général des impôts, loi n° 2025-127 du 14 février 2025, arrêté du 13 juillet 2026 (pompes à chaleur air/air).</p>''', 5)

# ---------- Article 3
article("guide-oublis-devis-salle-de-bain",
 "Devis salle de bain : 7 oublis qui font exploser la facture",
 "Devis de salle de bain : les 7 oublis qui font grimper la facture",
 "Dépose, étanchéité, évacuation, électricité, ventilation : les postes souvent absents d'un devis de salle de bain, qui reviennent en supplément.",
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
<p>Reprenez votre devis avec cette liste et cochez chaque point. Pour chaque absence, posez la question à l'artisan <strong>par écrit</strong> : soit le poste est inclus et il le précise, soit il le chiffre. Dans les deux cas, vous signez en sachant ce que vous payez. Si le total vous paraît élevé, voyez <a href="guide-negocier-devis-travaux.html">comment négocier un devis</a> sans braquer l'artisan.</p>
<p style="font-size: 15px !important; color: #5b6784 !important;">Article d'information générale. Chaque chantier est différent : en cas de doute sur un point technique, faites vérifier votre devis.</p>''', 5)


PRIX = "16.50"  # prix de base de l'analyse (schéma Service des pages par type de travaux)

# Pages « Analyse de devis <travaux> » : nom du service (schéma Service) et FAQ visible + FAQPage
JOBS = {
    "analyse-devis-salle-de-bain": ("Analyse de devis de salle de bain", [
        ("Une plaque hydrofuge suffit-elle sous le carrelage de la douche ?",
         "Non. Une plaque hydrofuge résiste à l'humidité mais n'est pas étanche. En zone de douche, le devis doit prévoir un système d'étanchéité sous carrelage (liquide ou natte, selon le support), avec des bandes d'angle et autour de l'évacuation."),
        ("Pourquoi un forfait plomberie pose-t-il problème ?",
         "Parce qu'il ne dit pas ce qui est fait. Demandez le détail : alimentations et évacuations refaites ou conservées, matériaux, raccordements, robinets d'arrêt accessibles. Sans ce détail, impossible de comparer deux devis ni de contester un oubli."),
        ("Comment faire relire mon devis de salle de bain ?",
         "Commandez l'analyse sur ComeUp et envoyez votre devis en PDF ou en photo. Vous recevez sous 48 h un rapport qui reprend chaque poste : prix, quantités, oublis, TVA et questions à poser à l'artisan avant de signer."),
    ]),
    "analyse-devis-pompe-a-chaleur": ("Analyse de devis de pompe à chaleur", [
        ("Comment savoir si la puissance de la pompe à chaleur est adaptée ?",
         "Demandez sur quelle base elle a été choisie. Un dimensionnement sérieux part des déperditions du logement (isolation, volume, zone climatique, température de départ des émetteurs), pas seulement de la surface habitable."),
        ("L'entreprise doit-elle être RGE ?",
         "Oui si vous comptez sur MaPrimeRénov' ou sur une prime CEE : la qualification RGE est obligatoire pour ces travaux. Vérifiez-la sur france-renov.gouv.fr, et vérifiez aussi que l'entreprise détient l'attestation de capacité pour manipuler les fluides frigorigènes."),
        ("Comment faire relire mon devis de pompe à chaleur ?",
         "Commandez l'analyse sur ComeUp et envoyez votre devis en PDF ou en photo. Le rapport, livré sous 48 h, vérifie le dimensionnement annoncé, les postes techniques oubliés, la TVA et les aides déduites."),
    ]),
    "analyse-devis-isolation": ("Analyse de devis d'isolation", [
        ("Quelle résistance thermique doit figurer sur un devis d'isolation des combles ?",
         "La résistance thermique (R, en m².K/W) de l'isolant posé doit être écrite noir sur blanc, avec la marque, la référence et l'épaisseur. Pour les aides, il faut au moins R = 7 en combles perdus et R = 6 en rampants."),
        ("Le prix au m² suffit-il pour comparer deux devis d'isolation ?",
         "Non. Sans résistance thermique, épaisseur après tassement et préparation prévue (retrait de l'ancien isolant, traitement des spots et des conduits), deux prix au m² ne parlent pas de la même chose."),
        ("Comment faire relire mon devis d'isolation ?",
         "Commandez l'analyse sur ComeUp et envoyez votre devis en PDF ou en photo. Le rapport, livré sous 48 h, vérifie les surfaces, la performance de l'isolant, l'éligibilité aux aides et la TVA."),
    ]),
    "analyse-devis-toiture": ("Analyse de devis de toiture", [
        ("Que signifie « selon état » sur un devis de toiture ?",
         "Que le prix final n'est pas connu. Demandez un prix unitaire (au mètre de chevron, de liteau, au m² de volige) et un plafond au-delà duquel l'entreprise doit vous prévenir avant d'engager des travaux supplémentaires."),
        ("Faut-il une autorisation pour refaire sa toiture ?",
         "Une réfection à l'identique n'en demande en général pas. Si l'aspect extérieur change (matériau, couleur, ajout de fenêtres de toit), une déclaration préalable en mairie est en principe nécessaire, et le PLU peut imposer des règles."),
        ("Comment faire relire mon devis de toiture ?",
         "Commandez l'analyse sur ComeUp et envoyez votre devis en PDF ou en photo. Le rapport, livré sous 48 h, vérifie les surfaces, l'échafaudage, la zinguerie, les lignes « selon état » et les questions à poser au couvreur."),
    ]),
}

PAGES = []
# Date de dernière mise à jour réelle des pages (date visible, dateModified et lastmod du sitemap)
PAGE_UPDATED = {s: "2026-10-27" for s in ["analyse-devis-salle-de-bain", "analyse-devis-pompe-a-chaleur", "analyse-devis-isolation", "analyse-devis-toiture", "analyse-devis-cuisine", "analyse-devis-electricite", "analyse-devis-extension", "analyse-devis-fenetres", "analyse-devis-ravalement-facade"]}

def page(slug, title, h1, desc, lead, body, kicker, toc=True):
    url = f"https://contre-plan.com/{slug}.html"
    mod = PAGE_UPDATED.get(slug)
    ld = {"@context":"https://schema.org","@type":"WebPage","name":h1,"description":desc,"url":url,"inLanguage":"fr-FR",
          "publisher":{"@type":"Organization","name":"Contre-Plan","url":"https://contre-plan.com/"}}
    if mod:
        ld["dateModified"] = mod
        LASTMOD[slug + ".html"] = mod
    crumbs = [("Accueil", "index.html"), (kicker, None)]
    extra = '<script type="application/ld+json">' + json.dumps(ld, ensure_ascii=False) + '</script>' + crumbs_ld(crumbs, url)
    if slug in JOBS:
        service, qa = JOBS[slug]
        svc = {"@context":"https://schema.org","@type":"Service","name":service,"serviceType":"Analyse de devis de travaux","description":desc,"url":url,
               "areaServed":{"@type":"Country","name":"France"},
               "provider":{"@type":"ProfessionalService","name":"Contre-Plan","url":"https://contre-plan.com/"},
               "offers":{"@type":"Offer","price":PRIX,"priceCurrency":"EUR","url":COMEUP}}
        extra += '\n<script type="application/ld+json">' + json.dumps(svc, ensure_ascii=False) + '</script>\n' + faq_ld(qa)
        body = with_faq(body, qa, before='<div class="note"><p><b>Vous avez un devis')
    body = with_links(body, slug, before='<div class="note"><p><b>Vous avez un devis')
    out = head(title, desc, url, extra).replace('<meta property="og:type" content="article">','<meta property="og:type" content="website">') + pagehero(kicker, h1, lead, (f"Mis à jour le {date_fr(mod)} · {AUTEUR}" if mod and slug in JOBS else None), crumbs) + layout(body, toc) + footer()
    open(os.path.join(OUT, slug + ".html"), "w").write(out)
    PAGES.append(slug)

article("guide-acompte-paiement-devis-travaux",
 "Acompte sur un devis de travaux : combien, quand, comment",
 "Acompte, échéancier, solde : comment payer un devis de travaux",
 "Montant de l'acompte, arrhes ou acompte, démarchage, paiements à l'avancement, solde et réserves : les règles pour payer vos travaux sans risque.",
 "Un acompte trop élevé, c'est vous qui financez le chantier à la place de l'entreprise, et c'est votre seul levier qui disparaît en cas de problème. Voici comment caler les paiements.",
 '''<h2>Combien verser à la signature ?</h2>
<p>Aucun texte ne fixe un plafond général d'acompte pour des travaux chez un particulier. L'usage est d'environ <strong>30 % à la signature</strong>, parfois un peu plus si l'entreprise doit commander des matériaux sur mesure (menuiseries, cuisine). Au-delà de 40 à 50 %, demandez pourquoi et proposez un échéancier.</p>
<div class="note"><p><strong>À éviter :</strong> payer l'intégralité avant le début des travaux. Si le chantier dérape ou si l'entreprise disparaît, vous n'avez plus aucun moyen de pression.</p></div>
<h2>Acompte ou arrhes : ce n'est pas la même chose</h2>
<p>Avec des <strong>arrhes</strong>, chacun peut renoncer : vous en perdant les arrhes, l'entreprise en vous rendant le double. Avec un <strong>acompte</strong>, le contrat est ferme des deux côtés. Sauf mention contraire, les sommes versées d'avance sont considérées comme des arrhes. Vérifiez le mot employé sur le devis.</p>
<h2>Devis signé chez vous : attention au démarchage</h2>
<p>Si le devis a été signé à votre domicile, vous disposez en principe d'un <strong>délai de rétractation de 14 jours</strong>, et l'entreprise ne peut rien encaisser pendant les <strong>7 jours</strong> qui suivent la signature, sauf exceptions. Le devis doit comporter un formulaire de rétractation. Ne remettez ni chèque, même daté plus tard, ni autorisation de prélèvement pendant ce délai. Pour revenir sur votre signature, voir <a href="guide-annuler-devis-signe-retractation.html">comment annuler un devis signé</a>.</p>
<h2>Un échéancier lié à l'avancement</h2>
<p>Le plus sain est de payer au rythme du chantier. Par exemple, pour une salle de bain :</p>
<ul><li>30 % à la signature ;</li><li>30 % à la fin de la dépose et des réseaux (plomberie, électricité) ;</li><li>30 % à la fin de la pose des revêtements ;</li><li>le solde à la réception.</li></ul>
<p>Chaque étape doit être décrite pour être vérifiable : « fin de la plomberie », plutôt qu'une date fixe sans rapport avec l'avancement.</p>
<h2>Le solde et la réception</h2>
<p>La <strong>réception</strong> (<a href="guide-reception-travaux-reserves.html">mode d'emploi ici</a>) est le moment où vous acceptez les travaux, avec ou sans réserves. Notez par écrit chaque défaut constaté : ce sont les réserves, que l'entreprise doit corriger. La réception fait aussi démarrer les garanties (parfait achèvement, biennale, décennale). Si le contrat le prévoit, une <strong>retenue de garantie</strong> limitée à 5 % du prix peut être conservée jusqu'à la levée des réserves, dans la limite d'un an.</p>
<h2>Les travaux supplémentaires</h2>
<p>Tout ajout en cours de chantier doit faire l'objet d'un <strong>avenant écrit et chiffré</strong>, signé avant d'être réalisé. Un supplément annoncé oralement puis découvert sur la facture est la première source de litige. Voir <a href="guide-depassement-devis-travaux-supplementaires.html">que faire face à un dépassement de devis</a>.</p>
<h2>Ce que je vérifie sur votre devis</h2>
<p>Le montant et la nature de l'acompte, l'échéancier, la cohérence avec l'avancement réel du chantier et les conditions de paiement en cas de démarchage. Voir aussi <a href="guide-mentions-obligatoires-devis.html">les mentions obligatoires d'un devis</a>, <a href="guide-negocier-devis-travaux.html">comment négocier un devis</a> et <a href="lexique-devis-travaux.html">le lexique du devis</a>.</p>''',
 6, date="2026-10-23")

article("guide-bien-demander-ses-devis",
 "Comment bien demander ses devis de travaux | Contre-Plan",
 "Avant de demander vos devis : comment obtenir des offres comparables",
 "Décrire son projet, donner les mêmes bases à chaque artisan, poser les bonnes questions : la méthode pour recevoir des devis vraiment comparables.",
 "La plupart des devis impossibles à comparer le sont dès la demande : chaque artisan a compris un projet différent. Dix minutes de préparation évitent ce piège.",
 '''<h2>1. Décrivez votre projet par écrit</h2>
<p>Rédigez une description courte, la même pour tous les artisans : ce que vous voulez faire, les surfaces, l'état actuel, ce que vous gardez, ce que vous remplacez. Joignez quelques photos et, si vous en avez, un plan ou des mesures.</p>
<ul><li>Pour une salle de bain : surface, remplacement de la baignoire par une douche ou non, hauteur de faïence souhaitée, équipements conservés.</li>
<li>Pour une pompe à chaleur : surface chauffée, année de construction, isolation existante, système actuel, radiateurs ou plancher chauffant.</li>
<li>Pour une isolation : surface des combles, accès, isolant existant, présence de spots ou de conduits.</li></ul>
<h2>2. Fixez les mêmes bases à chaque artisan</h2>
<p>Demandez à chacun de chiffrer les mêmes prestations, et de détailler les quantités et les prix unitaires. Si vous avez une gamme de matériaux en tête (une marque de receveur, un type de carrelage), donnez-la à tous. Sinon, demandez les marques et références prévues pour pouvoir comparer.</p>
<div class="note"><p><strong>L'astuce :</strong> demandez explicitement que la dépose, l'évacuation des déchets, la protection du chantier et le nettoyage soient chiffrés, même s'ils semblent évidents. Ce sont les postes qui disparaissent le plus souvent.</p></div>
<h2>3. Demandez trois devis, pas dix</h2>
<p>Trois devis suffisent en général pour situer les prix. Au-delà, la comparaison devient difficile et les artisans les plus demandés risquent de ne pas répondre. Privilégiez des entreprises qui ont visité le chantier : un devis fait sans visite oublie souvent des contraintes.</p>
<h2>4. Vérifiez l'entreprise avant de recevoir le devis</h2>
<ul><li>Son immatriculation, sur annuaire-entreprises.data.gouv.fr.</li>
<li>Sa qualification RGE si vous visez des aides, sur france-renov.gouv.fr.</li>
<li>Son attestation d'assurance décennale, à demander avec le devis.</li></ul>
<h2>5. Ne signez rien le jour de la visite</h2>
<p>Un devis se relit au calme. Méfiez-vous des remises valables « seulement aujourd'hui ». Si vous signez chez vous, vous disposez en principe d'un délai de rétractation de 14 jours, et aucun paiement ne peut être exigé pendant 7 jours, sauf exceptions.</p>
<h2>6. Comparez poste par poste</h2>
<p>Une fois les devis reçus, mettez-les côte à côte avec <a href="comparer-ses-devis.html">le tableau comparatif gratuit</a>. Pour les points à faire préciser, utilisez <a href="modeles-messages-artisan.html">les modèles de messages</a>, et vérifiez les mentions obligatoires avec <a href="guide-mentions-obligatoires-devis.html">ce guide</a>. Ensuite seulement, <a href="guide-negocier-devis-travaux.html">négociez</a> sur des bases claires.</p>''',
 6, date="2026-10-23")

article("guide-reception-travaux-reserves",
 "Réception des travaux : PV, réserves et solde, mode d'emploi",
 "Réception des travaux et réserves : comment ne rien laisser passer",
 "Procès-verbal, réserves, retenue de garantie de 5 %, solde, garantie de parfait achèvement : comment réceptionner vos travaux sans perdre vos recours.",
 "L'artisan annonce que le chantier est fini et vous tend un papier à signer avec la facture du solde. Ce que vous écrivez, ou n'écrivez pas, ce jour-là décide de ce que vous pourrez encore lui réclamer.",
 '''<h2>La réception, c'est quoi exactement ?</h2>
<p>La réception est l'acte par lequel vous, le maître de l'ouvrage, déclarez <strong>accepter les travaux, avec ou sans réserves</strong> (article 1792-6 du Code civil). Elle a lieu à la demande de la partie la plus diligente, vous ou l'entreprise, à l'amiable ou, à défaut, par décision du juge. Elle est toujours <strong>contradictoire</strong> : les deux parties sont présentes ou dûment convoquées.</p>
<p>En pratique, elle se fait lors d'une visite du chantier terminé et se formalise par un <strong>procès-verbal de réception</strong> écrit, daté et signé, normalement par les deux parties. Un simple « bon de fin de travaux » glissé avec la facture ne remplace pas cette visite : je vois souvent des particuliers le signer sans avoir fait le tour des pièces.</p>
<h2>Pourquoi cette signature compte autant</h2>
<p>La date de réception fait basculer plusieurs choses à la fois :</p>
<ul>
<li>elle fait démarrer les <strong>garanties légales</strong> : parfait achèvement (1 an), bon fonctionnement des équipements dissociables (2 ans minimum), décennale (10 ans) ;</li>
<li>la <strong>garde de l'ouvrage et ses risques</strong> vous sont transférés ;</li>
<li>le <strong>solde</strong> devient en principe payable, selon l'échéancier prévu au contrat ;</li>
<li>le délai d'un an de la <strong>retenue de garantie</strong>, si elle est prévue, commence à courir.</li>
</ul>
<div class="note"><p><strong>Le point qui coûte cher :</strong> un défaut visible le jour de la réception et que vous ne notez pas est considéré comme accepté. Vous ne pourrez en principe plus le réclamer à l'entreprise au titre des garanties. Les défauts invisibles ce jour-là restent, eux, couverts selon leur nature.</p></div>
<h2>Préparer la visite</h2>
<p>Ne faites pas la réception en dix minutes entre deux rendez-vous. Prévoyez une heure, en plein jour, et apportez :</p>
<ul>
<li>le <strong>devis signé</strong> et les éventuels avenants, pour vérifier que tout ce qui est payé est bien posé, avec les bonnes références ;</li>
<li>un téléphone pour <strong>photographier</strong> chaque défaut, avec un élément qui permet de le situer ;</li>
<li>un mètre, un niveau à bulle si vous en avez un, et une lampe ;</li>
<li>un modèle de procès-verbal si l'entreprise n'en propose pas : une feuille datée qui identifie le chantier, les parties, la liste des réserves et les signatures suffit.</li>
</ul>
<p>Si vos travaux ont été suivis par un architecte ou un maître d'œuvre et que sa mission comprend l'assistance à la réception (c'est courant, vérifiez son contrat), il doit vous assister et vous conseiller à ce moment-là.</p>
<h2>Ce que je regarde pendant la visite</h2>
<p>Je fais le tour pièce par pièce, du sol au plafond, puis je teste tout ce qui fonctionne. Concrètement :</p>
<ul>
<li><strong>les finitions</strong> : éclats de carrelage, joints manquants ou fissurés, traces de peinture, plinthes mal fixées, raccords visibles ;</li>
<li><strong>les menuiseries</strong> : chaque porte, fenêtre et volet doit s'ouvrir, se fermer et se verrouiller sans forcer ;</li>
<li><strong>l'eau</strong> : ouvrir chaque robinet, remplir et vider le bac de douche ou la baignoire, chercher une fuite sous les siphons, vérifier que l'eau s'écoule bien vers la bonde ;</li>
<li><strong>l'électricité</strong> : actionner chaque interrupteur, tester les prises avec un petit appareil, regarder le tableau électrique ;</li>
<li><strong>les équipements</strong> : faire démarrer le chauffage, la ventilation, le chauffe-eau, et demander qu'on vous montre les réglages ;</li>
<li><strong>la conformité au devis</strong> : quantités, matériaux, marques et coloris annoncés ;</li>
<li><strong>le chantier rendu</strong> : gravats évacués, abords et parties communes propres, dégâts éventuels sur l'existant.</li>
</ul>
<h2>Rédiger des réserves utiles</h2>
<p>Une réserve doit être <strong>précise</strong>. « Finitions à reprendre » ne sert à rien en cas de désaccord. Écrivez plutôt :</p>
<ul>
<li>où : « salle de bain, mur de la douche, à gauche du mitigeur » ;</li>
<li>quoi : « deux carreaux fêlés, joint silicone décollé sur 40 cm » ;</li>
<li>ce qui est attendu : « remplacement des deux carreaux, reprise du joint ».</li>
</ul>
<p>Numérotez les réserves, renvoyez aux photos et prévoyez sur le procès-verbal un <strong>délai de levée</strong> fixé d'un commun accord. Gardez un exemplaire signé. Si l'entreprise refuse de signer avec des réserves, ne signez pas un procès-verbal sans réserves pour autant. Rédigez et signez vous-même le procès-verbal avec vos réserves, en indiquant que l'entreprise, présente ou dûment convoquée, a refusé de signer, joignez les photos et envoyez-le-lui en recommandé avec accusé de réception. En cas de blocage, la réception peut être demandée au juge.</p>
<div class="note"><p><strong>Bon à savoir :</strong> des réserves ne vous empêchent pas d'occuper votre logement. En revanche, emménager sans procès-verbal et payer la totalité des travaux peut être considéré comme une réception tacite, éventuellement sans réserves. Faites la réception écrite avant d'occuper les lieux ou de solder.</p></div>
<h2>Le solde et la retenue de garantie</h2>
<p>Beaucoup de particuliers pensent pouvoir garder librement une partie du solde tant que tout n'est pas repris. La règle est plus encadrée.</p>
<ul>
<li>La loi du 16 juillet 1971 permet une <strong>retenue de garantie d'au plus 5 %</strong> du montant des travaux, pour couvrir les réserves faites à la réception. Elle n'est possible que si le <strong>contrat la prévoit</strong>, donc le devis signé.</li>
<li>Cette somme n'est pas gardée chez vous : elle doit être <strong>consignée</strong> auprès d'un consignataire accepté par les deux parties (un notaire, par exemple) ou, à défaut, désigné par le juge. Si vous la gardez simplement de votre côté, vous risquez de devoir la reverser à l'entreprise même si les réserves ne sont pas levées. L'entreprise peut la remplacer par une <strong>caution bancaire</strong>.</li>
<li>Elle est libérée dès la levée des réserves, et au plus tard un an après la réception, même sans levée formelle, sauf si vous avez notifié avant cette date, par <strong>lettre recommandée</strong> au consignataire ou à la caution, une opposition motivée par l'inexécution des obligations de l'entreprise.</li>
</ul>
<p>Pour le reste, le montant du solde payable à la réception, et ce que vous pouvez raisonnablement garder en proportion des réserves, se négocie avant la signature du devis. C'est l'objet de l'échéancier, détaillé dans <a href="guide-acompte-paiement-devis-travaux.html">le guide sur l'acompte et le paiement</a>.</p>
<h2>Après la réception : faire lever les réserves</h2>
<p>La garantie de parfait achèvement oblige l'entreprise à réparer, pendant un an, les désordres notés en réserve et ceux qui apparaissent dans l'année, hors usure normale ou mauvais usage.</p>
<ul>
<li>Si une réserve n'est pas reprise dans le délai convenu, écrivez à l'entreprise par <strong>lettre recommandée avec accusé de réception</strong>, en rappelant la réserve et en fixant un nouveau délai.</li>
<li>Un défaut apparu après la réception se signale de la même façon, <strong>avant la fin de l'année</strong> qui suit la réception.</li>
<li>Sans réponse, envoyez une <strong>mise en demeure</strong> et sollicitez le <strong>médiateur de la consommation</strong> dont relève l'entreprise. Si la mise en demeure reste sans effet, la loi permet en principe de faire réaliser les réparations par une autre entreprise, aux frais et risques de l'entreprise défaillante.</li>
</ul>
<p>Attention au calendrier : une lettre, une mise en demeure ou une médiation ne prolongent pas de façon sûre le délai d'un an de la garantie de parfait achèvement. En principe, seule une action en justice engagée avant la fin de l'année préserve vos droits. Si la date approche sans solution, prenez conseil rapidement auprès d'un juriste, d'une association de consommateurs ou de votre assurance protection juridique.</p>
<h2>Ce que je vérifie sur votre devis, en pensant à la réception</h2>
<p>La réception se prépare dès le devis. Quand je relis un devis, je regarde notamment :</p>
<ul>
<li>si l'échéancier garde un <strong>solde suffisant à la réception</strong>, et si une retenue de garantie est prévue ;</li>
<li>si les ouvrages sont décrits assez précisément (marques, références, quantités) pour pouvoir vérifier, le jour venu, que ce qui est posé correspond à ce qui a été payé ;</li>
<li>si le nettoyage, l'évacuation des gravats et la remise en état des abords sont bien inclus ;</li>
<li>si un délai d'exécution ferme est indiqué, pour savoir à partir de quand vous pouvez demander la réception.</li>
</ul>
<p>Voir aussi <a href="guide-mentions-obligatoires-devis.html">les mentions obligatoires d'un devis</a>, <a href="guide-depassement-devis-travaux-supplementaires.html">que faire en cas de travaux supplémentaires</a>, <a href="guide-verifier-assurance-decennale.html">comment vérifier l'attestation décennale</a> et <a href="modeles-messages-artisan.html">les modèles de messages à l'artisan</a>.</p>
<p style="font-size: 15px !important; color: #5b6784 !important;">Article d'information générale, à jour au 27 octobre 2026, qui ne remplace pas un conseil juridique. Sources : article 1792-6 du Code civil, loi n° 71-584 du 16 juillet 1971 (retenue de garantie), service-public.gouv.fr (garanties après la réception des travaux), DGCCRF (Malfaçon : mettez en œuvre les garanties), ANIL (jurisprudence sur la consignation de la retenue de garantie).</p>''',
 7, date="2026-10-25")

# ---------- Pages Méthode et Engagements
# ---------- Nouveaux guides (tools/nouveaux_guides.py)
FAQS.update(NG.GUIDE_FAQS)
for g in NG.GUIDES:
    article(g["slug"], g["title"], g["h1"], g["desc"], g["lead"], g["body"], g["readtime"], date="2026-10-26")

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
 "Engagements de Contre-Plan : indépendance et confidentialité",
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

# ---------- Pages par type de travaux
def cta_type(t):
    return f"""<div class="note"><p><b>Vous avez un devis {t} sous les yeux ?</b> Faites d'abord <a href="index.html#test">le test en 1 minute</a>, puis envoyez-le moi : je le relis ligne par ligne et vous dites quoi demander à l'artisan. <a href="exemple-rapport-contre-plan.pdf" target="_blank" rel="noopener">Voir un exemple de rapport</a>.</p></div>"""

page("analyse-devis-salle-de-bain",
 "Analyse de devis salle de bain par un ingénieur BTP",
 "Analyse de devis salle de bain",
 "Étanchéité, dépose, plomberie au forfait, électricité, TVA : les points qu'un ingénieur BTP vérifie sur un devis de rénovation de salle de bain.",
 "Une salle de bain concentre plusieurs corps de métier dans quelques mètres carrés : c'est le devis où les oublis coûtent le plus cher.",
 """<h2>Les pièges les plus fréquents</h2>
<ul><li><b>L'étanchéité sous carrelage absente ou floue.</b> En zone de douche, un système d'étanchéité (liquide ou natte, selon le support) est indispensable. Une plaque hydrofuge seule n'est pas étanche.</li>
<li><b>La dépose et l'évacuation des gravats oubliées.</b> Retirer faïence, carrelage et baignoire prend du temps et génère des déchets : s'ils ne sont pas chiffrés, ils reviendront en supplément.</li>
<li><b>La plomberie au forfait.</b> Un forfait sans détail empêche de savoir si les alimentations, les évacuations et les robinets d'arrêt sont refaits.</li>
<li><b>L'électricité.</b> Les volumes de sécurité autour de la douche et de la baignoire (norme NF C 15-100) imposent des règles précises pour les prises, les spots et le chauffage.</li>
<li><b>La ventilation.</b> Une salle de bain refaite sans ventilation adaptée vieillit mal.</li>
<li><b>La pente et l'évacuation de la douche</b>, surtout pour une douche à l'italienne.</li></ul>
<h2>Exemple de ligne à faire préciser</h2>
<p>« Plomberie : 1 forfait, 1 150 € HT. » Rien ne permet de vérifier ce qui est prévu. À demander : la liste des travaux (alimentations, évacuations, raccordements), les matériaux et la présence de robinets d'arrêt accessibles.</p>
<h2>La TVA sur une salle de bain</h2>
<p>Dans un logement achevé depuis plus de 2 ans, les travaux d'amélioration relèvent en principe du taux de 10 %. Les meubles non intégrés au bâti et l'électroménager restent à 20 %. Détails dans <a href="guide-tva-travaux-renovation.html">le guide TVA</a>.</p>
<h2>Logement ancien : pensez à l'amiante</h2>
<p>Si le permis de construire date d'avant le 1er juillet 1997, un repérage amiante avant travaux est en principe requis pour la démolition. Demandez qui le prend en charge.</p>
<h2>Ce que je vérifie en plus</h2>
<p>Les quantités (surfaces de faïence et de sol cohérentes avec la pièce), les prix unitaires comparés à des ordres de grandeur récents, les références des équipements, l'enchaînement des travaux et les conditions de paiement. Voir aussi <a href="guide-oublis-devis-salle-de-bain.html">les 7 oublis qui font grimper la facture</a> et <a href="methode.html">ma méthode</a>.</p>
""" + cta_type("de salle de bain"),
 "Salle de bain")

page("analyse-devis-pompe-a-chaleur",
 "Analyse de devis pompe à chaleur par un ingénieur BTP",
 "Analyse de devis pompe à chaleur",
 "Dimensionnement, fluides frigorigènes, liaisons, condensats, RGE, TVA : ce qu'un ingénieur BTP vérifie sur un devis de pompe à chaleur.",
 "Une pompe à chaleur mal dimensionnée ou mal posée consomme plus et dure moins. Le devis doit le montrer avant la signature.",
 """<h2>Le dimensionnement</h2>
<p>La puissance de la pompe à chaleur doit correspondre aux besoins du logement. Un devis sérieux s'appuie sur une estimation des déperditions, pas seulement sur la surface. Trop puissante, elle fonctionne par à-coups ; pas assez, l'appoint électrique prend le relais. Demandez sur quelle base la puissance a été choisie.</p>
<h2>Les points techniques à retrouver sur le devis</h2>
<ul><li><b>L'attestation de capacité</b> de l'entreprise pour la manipulation des fluides frigorigènes.</li>
<li><b>Les liaisons frigorifiques</b> : longueur prévue et prix du mètre supplémentaire.</li>
<li><b>L'évacuation des condensats</b> : gravitaire ou par pompe de relevage.</li>
<li><b>Les supports du groupe extérieur</b> et les plots anti-vibratiles, pour limiter le bruit.</li>
<li><b>L'alimentation électrique dédiée</b> et sa protection au tableau.</li>
<li><b>La mise en service</b> : tirage au vide, contrôle d'étanchéité, réglages.</li>
<li>Pour une pompe à chaleur air-eau : le raccordement au circuit existant, le désembouage éventuel et la régulation.</li></ul>
<h2>Les aides et la qualification RGE</h2>
<p>Pour bénéficier des aides à la rénovation énergétique (MaPrimeRénov', primes CEE), l'entreprise doit être qualifiée RGE pour ces travaux : vérifiez-le sur france-renov.gouv.fr. Si une prime est déduite sur le devis, son montant et son origine doivent être indiqués clairement.</p>
<h2>La TVA</h2>
<p>Dans un logement achevé depuis plus de 2 ans, les pompes à chaleur éligibles à la rénovation énergétique relèvent du taux de 5,5 %. Depuis le 18 juillet 2026, c'est aussi possible pour une pompe à chaleur air/air réversible fixe qui atteint les performances exigées (classe énergétique, fluide frigorigène, pilotage à distance). La climatisation seule n'en bénéficie pas, et les chaudières fonctionnant au gaz ou au fioul sont au taux de 20 % depuis le 1er mars 2025. Vérifiez que le taux appliqué correspond bien à l'équipement.</p>
<h2>Exemple de ligne à faire préciser</h2>
<p>« Liaisons frigorifiques : forfait. » Sans longueur indiquée, impossible de savoir si un supplément sera facturé le jour de la pose. À demander : la longueur incluse et le prix au mètre au-delà.</p>
""" + cta_type("de pompe à chaleur"),
 "Pompe à chaleur")

page("analyse-devis-isolation",
 "Analyse de devis isolation par un ingénieur BTP",
 "Analyse de devis isolation",
 "Résistance thermique, épaisseur, surface, pare-vapeur, points singuliers, RGE et TVA : ce qu'un ingénieur BTP vérifie sur un devis d'isolation.",
 "Sur un devis d'isolation, un chiffre compte plus que tous les autres : la résistance thermique. S'il manque, vous ne savez pas ce que vous achetez.",
 """<h2>La résistance thermique (R)</h2>
<p>Le devis doit indiquer la résistance thermique de l'isolant posé, en m².K/W, avec la marque, la référence et l'épaisseur. Pour les aides, des minimums s'appliquent, par exemple R ≥ 7 en combles perdus et R ≥ 6 en rampants de toiture pour la prime CEE d'isolation des combles. Un isolant soufflé se tasse : l'épaisseur posée doit tenir compte du tassement.</p>
<h2>Les points à retrouver sur le devis</h2>
<ul><li><b>La surface isolée en m²</b>, cohérente avec la maison, et le prix au m².</li>
<li><b>Le pare-vapeur ou la membrane d'étanchéité à l'air</b> quand la technique l'exige.</li>
<li><b>Les points singuliers</b> : trappe d'accès, spots encastrés, conduits de cheminée (distances de sécurité), boîtiers électriques.</li>
<li><b>La préparation</b> : retrait de l'ancien isolant si nécessaire, protection, repérage des gaines.</li>
<li><b>Le certificat de l'isolant</b> (certification ACERMI ou équivalent) pour justifier les performances annoncées.</li></ul>
<h2>Les aides, le RGE et la TVA</h2>
<p>Les aides à la rénovation énergétique exigent une entreprise qualifiée RGE pour ces travaux. Dans un logement achevé depuis plus de 2 ans, l'isolation relève du taux de TVA de 5,5 %. Si une prime est déduite du devis, son montant doit apparaître clairement.</p>
<h2>Exemple de ligne à faire préciser</h2>
<p>« Isolation des combles, laine soufflée : 80 m², 22 € le m². » Sans résistance thermique ni épaisseur, impossible de comparer deux devis ni de savoir si vous êtes éligible aux aides. À demander : le produit exact, la résistance thermique, l'épaisseur après tassement.</p>
""" + cta_type("d'isolation"),
 "Isolation")

page("analyse-devis-toiture",
 "Analyse de devis toiture par un ingénieur BTP",
 "Analyse de devis toiture",
 "Surface, échafaudage, dépose, écran sous-toiture, zinguerie, charpente, amiante : ce qu'un ingénieur BTP vérifie sur un devis de toiture.",
 "Une toiture se refait rarement deux fois dans une vie. Le devis doit dire précisément ce qui est remplacé, et ce qui ne l'est pas.",
 """<h2>Les points à retrouver sur le devis</h2>
<ul><li><b>La surface de toiture</b> en m², mesurée en rampant et non au sol, et le prix au m² pour chaque poste.</li>
<li><b>L'échafaudage et la sécurité</b> : souvent un poste important, parfois oublié.</li>
<li><b>La dépose et l'évacuation</b> de l'ancienne couverture.</li>
<li><b>L'écran sous-toiture, les liteaux et contre-liteaux</b> : remplacés ou conservés ?</li>
<li><b>La zinguerie</b> : gouttières, descentes, noues, faîtage, solins autour des cheminées et fenêtres de toit.</li>
<li><b>La charpente</b> : traitement, remplacement de pièces abîmées, avec un prix au mètre ou à la pièce plutôt qu'un forfait « selon état ».</li></ul>
<h2>L'amiante dans les anciennes couvertures</h2>
<p>Les plaques de fibres-ciment posées avant 1997 peuvent contenir de l'amiante. Leur retrait obéit à des règles strictes et doit être confié à une entreprise habilitée. Le repérage et la filière d'élimination doivent apparaître sur le devis.</p>
<h2>Les démarches et la TVA</h2>
<p>Une réfection qui change l'aspect extérieur (matériau, couleur, fenêtres de toit) peut nécessiter une déclaration préalable en mairie. Dans un logement achevé depuis plus de 2 ans, la réfection relève en principe du taux de 10 %, et l'isolation de la toiture de 5,5 % si les conditions sont réunies. Vérifiez aussi l'attestation d'assurance décennale : c'est elle qui vous couvre en cas d'infiltration.</p>
<h2>Exemple de ligne à faire préciser</h2>
<p>« Remplacement des bois abîmés : selon état. » Cette ligne ouvre la porte à n'importe quel supplément. À demander : un prix unitaire par mètre de chevron ou de liteau, et un plafond au-delà duquel l'entreprise doit vous prévenir avant d'agir.</p>
""" + cta_type("de toiture"),
 "Toiture")

# ---------- Nouvelles pages par type de travaux (tools/nouveaux_guides.py)
for j in NG.JOB_PAGES:
    JOBS[j["slug"]] = (j["service"], j["faq"])
    page(j["slug"], j["title"], j["h1"], j["desc"], j["lead"], j["body"] + cta_type(j["cta"]), j["kicker"])

# ---------- Lexique
LEX = [
 ("Acompte", "Somme versée à la signature. Elle engage les deux parties : vous ne pouvez pas renoncer en la perdant, comme avec des arrhes."),
 ("Arrhes", "Somme versée d'avance qui permet de renoncer en la perdant (ou, pour l'entreprise, en la remboursant au double). Sauf mention contraire, les sommes versées d'avance sont des arrhes."),
 ("Avenant", "Modification du devis signé (travaux en plus ou en moins). Il doit être écrit et accepté avant d'être réalisé."),
 ("Décennale (assurance)", "Assurance obligatoire de l'entreprise qui couvre pendant 10 ans les dommages graves touchant la solidité de l'ouvrage ou le rendant impropre à son usage."),
 ("Dépose", "Retrait de l'existant (carrelage, sanitaires, couverture…) avant les nouveaux travaux."),
 ("Échéancier", "Calendrier des paiements : acompte, paiements à l'avancement, solde à la réception."),
 ("Écran sous-toiture", "Membrane posée sous les tuiles ou ardoises qui protège la charpente des infiltrations et de la poussière."),
 ("Fourniture et pose (F+P)", "Le prix comprend le matériau et la main-d'œuvre pour l'installer."),
 ("Forfait (ft)", "Prix global pour un ensemble de travaux, sans détail des quantités. Pratique, mais impossible à vérifier sans précisions."),
 ("HT / TTC", "Hors taxes / toutes taxes comprises. Le TTC est le montant que vous payez réellement."),
 ("Liaisons frigorifiques", "Tuyaux qui relient l'unité extérieure et l'unité intérieure d'une pompe à chaleur ou d'une climatisation."),
 ("ml (mètre linéaire)", "Unité de longueur utilisée pour les plinthes, les gouttières, les tuyaux ou les joints."),
 ("Mise en service", "Réglages et contrôles réalisés au démarrage d'un équipement (chauffage, pompe à chaleur, VMC)."),
 ("NF C 15-100", "Norme française des installations électriques des logements, avec des règles précises dans les salles de bain."),
 ("Parfait achèvement (garantie de)", "Garantie d'un an après la réception : l'entreprise doit réparer les défauts signalés."),
 ("Pare-vapeur", "Membrane qui empêche l'humidité intérieure de pénétrer dans l'isolant."),
 ("Plus-value / moins-value", "Supplément ou réduction de prix par rapport au devis initial, généralement formalisé par un avenant."),
 ("P.U. (prix unitaire)", "Prix d'une unité (un m², un mètre, une pièce). Multiplié par la quantité, il donne le total de la ligne."),
 ("Ragréage", "Couche de mortier fluide qui rend un sol plan et lisse avant la pose d'un revêtement."),
 ("Réception", "Moment où vous acceptez les travaux, avec ou sans réserves. Elle fait démarrer les garanties."),
 ("Réserves", "Défauts constatés à la réception et notés par écrit, que l'entreprise doit corriger."),
 ("Résistance thermique (R)", "Capacité d'un isolant à freiner la chaleur, en m².K/W. Plus R est élevé, plus l'isolation est performante."),
 ("RGE", "Reconnu garant de l'environnement : qualification obligatoire de l'entreprise pour que vous ayez droit aux aides à la rénovation énergétique."),
 ("SPEC / SEL", "Systèmes d'étanchéité liquide appliqués sous le carrelage, au mur (SPEC) ou au sol (SEL), dans les zones exposées à l'eau."),
 ("Solde", "Dernier paiement, versé à la réception des travaux."),
 ("u (unité)", "Prix à la pièce : un receveur, un radiateur, une fenêtre."),
 ("Zinguerie", "Éléments en métal d'une toiture : gouttières, descentes, noues, solins, faîtage."),
]
def _first(t):
    c = t[0].upper()
    return {"É":"E","È":"E","Ê":"E","À":"A","Ç":"C"}.get(c, c)
_groups = {}
for t, d in sorted(LEX, key=lambda x: slug_id(x[0])):
    _groups.setdefault(_first(t), []).append((t, d))
lex_html = '<nav class="cp-letters" aria-label="Lettres">' + "".join(f'<a href="#lettre-{k.lower()}">{k}</a>' for k in sorted(_groups)) + '</nav>'
for k in sorted(_groups):
    lex_html += f'<section class="cp-gl" id="lettre-{k.lower()}"><div class="cp-gl-letter">{k}</div><dl>' + "".join(
        f'<div class="cp-term" id="{slug_id(t)}"><dt>{html.escape(t)}</dt><dd>{html.escape(d)}</dd></div>' for t, d in _groups[k]) + '</dl></section>'

page("lexique-devis-travaux",
 "Lexique du devis de travaux : les termes expliqués",
 "Lexique du devis de travaux",
 "Acompte, arrhes, forfait, ml, P.U., ragréage, SPEC, RGE, résistance thermique : les mots d'un devis de travaux expliqués simplement.",
 "Les termes qu'on croise sur un devis de travaux, expliqués en une ou deux phrases.",
 lex_html + '<p style="margin-top:28px">Un terme vous manque ? Posez-moi la question via le chat du site.</p>',
 "Lexique", toc=False)

# ---------- Cas fictifs
page("cas-fictifs",
 "Cas fictifs : trois devis de travaux analysés | Contre-Plan",
 "Trois devis analysés : cas fictifs",
 "Salle de bain, pompe à chaleur, isolation des combles : trois exemples fictifs de devis analysés pour montrer ce qu'une relecture peut révéler.",
 "Ces trois cas sont inventés pour illustrer le travail d'analyse. Les devis, les entreprises et les chiffres sont fictifs, mais les points relevés sont ceux que l'on rencontre réellement.",
 """<div class="note"><p><b>Cas fictifs.</b> Aucun de ces exemples ne correspond à un client ou à une entreprise réels.</p></div>
<h2>Cas 1 : une salle de bain de 6 m² à 7 374 € TTC</h2>
<p><b>Le devis :</b> rénovation complète avec dépose, receveur extra-plat, faïence, plomberie au forfait et électricité.</p>
<p><b>Ce que la relecture relève :</b> étanchéité sous carrelage non chiffrée, évacuation des gravats absente, dépose jugée élevée, plomberie au forfait sans détail, acompte de 50 %.</p>
<p><b>Ce qu'il faut demander :</b> l'ajout de l'étanchéité et des gravats, le détail de la plomberie, une révision de la dépose et un acompte ramené à 30 %.</p>
<p><a href="exemple-rapport-contre-plan.pdf" target="_blank" rel="noopener" data-goatcounter-click="telechargement-exemple-rapport">Lire le rapport complet de ce cas (PDF, 4 pages)</a></p>
<h2>Cas 2 : une pompe à chaleur air-eau à 14 900 € TTC</h2>
<p><b>Le devis :</b> remplacement d'une chaudière fioul par une pompe à chaleur air-eau de 11 kW, prime déduite, pose comprise.</p>
<p><b>Ce que la relecture relève :</b> aucune estimation des besoins de chauffage pour justifier les 11 kW, liaisons au forfait sans longueur, dépose de l'ancienne chaudière et de la cuve non mentionnées, prime déduite sans indication de son origine ni de la qualification RGE.</p>
<p><b>Ce qu'il faut demander :</b> la base du dimensionnement, la longueur de liaisons incluse et le prix au mètre au-delà, le chiffrage de la dépose et de la neutralisation de la cuve, le certificat RGE et le détail de la prime.</p>
<h2>Cas 3 : l'isolation de 90 m² de combles perdus à 2 300 € TTC</h2>
<p><b>Le devis :</b> laine soufflée en combles perdus, « isolation performante », TVA à 5,5 %.</p>
<p><b>Ce que la relecture relève :</b> ni résistance thermique ni épaisseur indiquées, aucune mention de la protection des spots et du conduit de cheminée, surface plus grande que l'emprise de la maison au sol.</p>
<p><b>Ce qu'il faut demander :</b> la marque et la référence de l'isolant, la résistance thermique et l'épaisseur après tassement, le traitement des points singuliers, la justification de la surface.</p>
<h2>Ce que montrent ces trois cas</h2>
<p>Aucun de ces devis n'était malhonnête. Ils étaient incomplets, comme beaucoup de devis : ce qui n'est pas écrit est justement ce qui finit en supplément ou en litige. Une relecture avant signature permet de le faire préciser pendant qu'il est encore temps.</p>
<p>Pour voir ce que je contrôle à chaque fois : <a href="methode.html">ma méthode</a>.</p>""",
 "Cas fictifs")

# ---------- Outils gratuits
page("comparer-ses-devis",
 "Tableau comparatif de devis gratuit (Excel et PDF)",
 "Comparer ses devis : le tableau gratuit",
 "Tableau gratuit pour comparer 2 ou 3 devis de travaux poste par poste : totaux, TVA, acompte, postes non chiffrés, garanties. Excel et PDF à imprimer.",
 "Deux devis ne se comparent pas sur le total : ils ne contiennent presque jamais les mêmes prestations. Ce tableau vous aide à les remettre à plat, poste par poste.",
 """<div style="display:flex;flex-wrap:wrap;gap:12px;margin:8px 0 24px;">
<a href="tableau-comparatif-devis.xlsx" download data-goatcounter-click="telechargement-comparatif-xlsx" class="btn">Télécharger le tableau (Excel)</a>
<a href="tableau-comparatif-devis.pdf" download data-goatcounter-click="telechargement-comparatif-pdf" class="btn dark">Version à imprimer (PDF)</a>
</div>
<p>Le fichier Excel s'ouvre aussi dans Google Sheets (Fichier, Importer) et dans Numbers. Une feuille d'exemple fictif montre un tableau rempli.</p>
<h2>Ce que le tableau fait pour vous</h2>
<ul><li>Il additionne les postes, calcule la TVA, le total TTC et l'acompte en euros pour chaque artisan.</li>
<li>Il affiche l'écart de chaque devis avec le moins cher.</li>
<li>Il colore en orange les postes chiffrés chez un artisan mais absents chez un autre : ce sont ceux à faire chiffrer avant de comparer.</li>
<li>Il signale en rouge chaque « Non » : attestation décennale non reçue, pas de délai ferme, déchets non chiffrés.</li>
<li>Il met en évidence un acompte supérieur à 30 %.</li></ul>
<h2>Comment bien l'utiliser</h2>
<ul><li><b>Une ligne par prestation comparable.</b> Si un artisan regroupe la dépose et l'évacuation et un autre les sépare, additionnez pour comparer la même chose.</li>
<li><b>Les montants hors taxes.</b> La TVA peut différer d'un devis à l'autre si l'un des taux est mal appliqué : comparez d'abord en HT.</li>
<li><b>Les quantités.</b> Si deux devis n'annoncent pas la même surface pour le même travail, demandez pourquoi avant de comparer les prix.</li>
<li><b>Le moins cher n'est pas forcément le meilleur.</b> Un devis bas avec deux postes absents peut finir plus cher qu'un devis complet.</li></ul>
<p>Une fois les écarts repérés, voyez <a href="guide-negocier-devis-travaux.html">comment négocier un devis de travaux</a> sur les postes qui coincent.</p>
<div class="note"><p><b>Vous préférez un regard d'ingénieur ?</b> L'option « Comparatif multi devis » vous livre ce tableau rempli et commenté poste par poste, avec ce qui différencie vraiment les offres. Voir <a href="index.html#tarifs">les tarifs</a>.</p></div>
<p>Pour demander des devis comparables dès le départ : <a href="guide-bien-demander-ses-devis.html">comment bien demander ses devis</a>. Pour écrire aux artisans : <a href="modeles-messages-artisan.html">les modèles de messages</a>.</p>""",
 "Outil gratuit")

TPL = [
 ("Demander l'attestation d'assurance décennale",
  "Bonjour,\n\nMerci pour votre devis du [date]. Avant de m'engager, pourriez-vous me transmettre votre attestation d'assurance décennale en cours de validité, couvrant les travaux prévus ([type de travaux]) ?\n\nJe vous remercie par avance.\n\nCordialement,\n[Votre nom]"),
 ("Négocier l'acompte et l'échéancier",
  "Bonjour,\n\nVotre devis me convient sur le fond. Concernant le paiement, serait-il possible de prévoir un acompte de 30 % à la signature, puis des paiements liés à l'avancement des travaux et le solde à la réception ?\n\nPar exemple : 30 % à la signature, 30 % à [étape], 30 % à [étape], le solde à la réception.\n\nMerci de me dire si cela vous convient.\n\nCordialement,\n[Votre nom]"),
 ("Faire détailler un forfait",
  "Bonjour,\n\nSur votre devis, la ligne « [intitulé du forfait] » est indiquée au forfait pour [montant] € HT. Pour pouvoir comparer, pourriez-vous me détailler ce qu'elle comprend (travaux, quantités, matériaux) ?\n\nMerci beaucoup.\n\nCordialement,\n[Votre nom]"),
 ("Faire ajouter un poste oublié",
  "Bonjour,\n\nEn relisant votre devis, je ne vois pas de ligne pour [poste : par exemple l'étanchéité sous carrelage de la douche / l'évacuation des gravats]. Pourriez-vous l'ajouter, ou me confirmer par écrit qu'il est inclus dans un autre poste ?\n\nJe préfère que tout soit chiffré avant de signer pour éviter les suppléments en cours de chantier.\n\nCordialement,\n[Votre nom]"),
 ("Obtenir une date de début et un délai ferme",
  "Bonjour,\n\nVotre devis indique une durée indicative de [durée]. Pourriez-vous préciser une date de début des travaux et un délai d'exécution sur lequel vous vous engagez ?\n\nMerci par avance.\n\nCordialement,\n[Votre nom]"),
 ("Demander les marques et références",
  "Bonjour,\n\nPour bien comparer les offres, pourriez-vous m'indiquer les marques et références des matériaux et équipements prévus, notamment [équipement : receveur, mitigeur, pompe à chaleur, isolant…] ?\n\nMerci beaucoup.\n\nCordialement,\n[Votre nom]"),
 ("Refuser poliment un devis",
  "Bonjour,\n\nMerci pour le temps passé et pour votre devis du [date]. Après réflexion, j'ai choisi une autre proposition pour ce projet.\n\nJe garde vos coordonnées pour de futurs travaux.\n\nBien cordialement,\n[Votre nom]"),
]
tpl_html = "".join(f'<div class="cp-tpl"><h2>{html.escape(t)}</h2><pre id="tpl{i}">{html.escape(x)}</pre><button type="button" class="cp-copy" data-copy="tpl{i}">Copier le message</button></div>' for i,(t,x) in enumerate(TPL,1))
page("modeles-messages-artisan",
 "Modèles de messages à envoyer à un artisan | Contre-Plan",
 "Modèles de messages à envoyer à l'artisan",
 "Messages prêts à copier pour demander l'attestation décennale, négocier l'acompte, faire détailler un forfait ou ajouter un poste oublié.",
 "Poser les bonnes questions par écrit, c'est la meilleure protection avant de signer. Voici des messages prêts à copier : remplacez simplement les passages entre crochets.",
 '<p>Gardez un ton cordial : l\'artisan n\'est pas un adversaire, et un devis précisé par écrit protège aussi l\'entreprise. Envoyez vos questions par e-mail ou par message, pour en garder une trace.</p>' + tpl_html +
 '<p style="margin-top:24px">Vous ne savez pas quelles questions poser sur votre devis ? <a href="index.html#test">Faites le test en 1 minute</a>, ou confiez-le moi : chaque rapport se termine par les questions à envoyer à l\'artisan.</p>',
 "Outil gratuit")

# ---------- Guides index (centre de ressources)
def rcard(href, tag, title, desc, cta, extra=""):
    return f'<a class="cp-rcard" href="{href}"{extra}><span class="cp-rtag">{tag}</span><span class="cp-rtitle">{html.escape(title)}</span><span class="cp-rdesc">{html.escape(desc)}</span><span class="cp-rcta">{cta} </span></a>'
g_cards = "".join(rcard(f"{s_}.html", f"Guide, {rt} min", h_, d_, "Lire le guide") for s_, h_, d_, rt in ARTICLES)
t_cards = "".join(rcard(h_, "Par travaux", t_, d_, "Ce que je vérifie") for h_, t_, d_ in [
 ("analyse-devis-salle-de-bain.html", "Salle de bain", "Étanchéité, dépose, plomberie au forfait, volumes électriques."),
 ("analyse-devis-pompe-a-chaleur.html", "Pompe à chaleur", "Dimensionnement, liaisons, condensats, RGE et TVA."),
 ("analyse-devis-isolation.html", "Isolation", "Résistance thermique, surface, pare-vapeur, points singuliers."),
 ("analyse-devis-toiture.html", "Toiture", "Surface, échafaudage, zinguerie, charpente, amiante.")] + [
 (j["slug"] + ".html", j["kicker"], j["card"]) for j in NG.JOB_PAGES])
o_cards = "".join([
 rcard("index.html#test", "Outil gratuit", "Test : votre devis est-il complet ?", "Six questions pour repérer en une minute ce qu'il faut faire préciser.", "Faire le test"),
 rcard("comparer-ses-devis.html", "Outil gratuit", "Tableau comparatif de devis", "Excel et PDF : totaux, TVA, acompte et postes manquants calculés pour vous.", "Télécharger"),
 rcard("modeles-messages-artisan.html", "Outil gratuit", "Modèles de messages à l'artisan", "Sept messages prêts à copier pour demander, négocier ou refuser poliment.", "Voir les modèles"),
 rcard("checklist-devis-travaux.pdf", "Outil gratuit", "Check-list à imprimer", "Vingt points à cocher en relisant n'importe quel devis de travaux.", "Télécharger", ' download data-goatcounter-click="telechargement-checklist"')])
c_cards = "".join([
 rcard("methode.html", "Comprendre", "Ma méthode", "La grille de contrôle appliquée à chaque devis, en cinq temps.", "Découvrir"),
 rcard("cas-fictifs.html", "Comprendre", "Trois devis analysés", "Salle de bain, pompe à chaleur, combles : ce qu'une relecture révèle (cas fictifs).", "Lire les cas"),
 rcard("lexique-devis-travaux.html", "Comprendre", "Lexique du devis", "Les termes d'un devis expliqués en une ou deux phrases.", "Ouvrir le lexique"),
 rcard("exemple-rapport-contre-plan.pdf", "Comprendre", "Exemple de rapport", "Un rapport complet de 4 pages, sur un devis fictif de salle de bain.", "Voir le PDF", ' target="_blank" rel="noopener" data-goatcounter-click="telechargement-exemple-rapport"')])
def rsec(title, sub, cards):
    return f'<section class="cp-rsec"><div class="cp-rhead"><h2>{title}</h2><p>{sub}</p></div><div class="cp-rgrid">{cards}</div></section>'
crumbs = [("Accueil", "index.html"), ("Guides et outils", None)]
idx = head("Guides et outils pour lire un devis de travaux | Contre-Plan",
  "Guides, outils gratuits et pages par type de travaux pour vérifier un devis avant de signer : mentions, TVA, acompte, comparatif, modèles de messages.",
  "https://contre-plan.com/guides.html", crumbs_ld(crumbs, "https://contre-plan.com/guides.html")) + pagehero("Ressources", "Guides et outils pour lire un devis", "Tout ce que je vérifie sur un devis, expliqué simplement, et des outils gratuits pour le faire vous-même avant de signer.", None, crumbs) + \
  '<main class="cp-res-wrap" id="contenu">' + rsec("Guides", "Les règles et les pièges, sujet par sujet.", g_cards) + rsec("Par type de travaux", "Chaque chantier a ses oublis classiques.", t_cards) + \
  rsec("Outils gratuits", "À utiliser avec votre devis sous les yeux.", o_cards) + rsec("Pour aller plus loin", "Ce que contient une analyse, et comment je la mène.", c_cards) + \
  f'<div class="cp-res-cta">{CTA}</div></main>' + footer()
open(os.path.join(OUT, "guides.html"), "w").write(idx)


# ---------- contact
FORM_ACTION = "https://docs.google.com/forms/d/e/1FAIpQLScKwDm4HbZRdSL-ztX3gq3D7E7z_C8HTu44G3CKTzHwInyvyQ/formResponse"
contact_body = f"""<p>Une question sur le service, sur un devis ou sur un guide ? Écrivez-moi ici, je réponds sous 24 h à l'adresse que vous indiquez.</p>
<p><b>Pas sûr que votre devis vaille une analyse ?</b> Choisissez « Pré-diagnostic gratuit » et décrivez-le en 3 lignes (type de travaux, montant, ce qui vous inquiète) : je vous dis gratuitement si une analyse vaut le coup.</p>
<p class="cp-form-note">Pour faire analyser un devis, passez directement par <a href="{COMEUP}" data-goatcounter-click="clic-comeup-contact">ComeUp</a> : c'est là que vous l'envoyez et que vous recevez le rapport. N'envoyez pas votre devis par ce formulaire.</p>
<div class="cp-form-ok" id="cp-form-ok" role="status" aria-live="polite" tabindex="-1" hidden></div>
<form class="cp-form" action="{FORM_ACTION}" method="POST" accept-charset="UTF-8">
<input type="text" id="cp-hp" class="cp-hp" tabindex="-1" autocomplete="off" aria-hidden="true">
<div class="cp-f2">
<label>Prénom ou pseudo<input type="text" name="entry.110816487" required maxlength="80" autocomplete="given-name"></label>
<label>Adresse e-mail<input type="email" name="entry.721010462" required maxlength="120" autocomplete="email"></label>
</div>
<label>Sujet<select name="entry.1520641388" required>
<option value="">Choisissez un sujet</option>
<option>Pré-diagnostic gratuit</option>
<option>Question sur le service</option>
<option>Question sur un devis</option>
<option>Question sur un guide ou un outil</option>
<option>Partenariat ou presse</option>
<option>Autre</option>
</select></label>
<label>Comment avez-vous connu Contre-Plan ? <span style="font-weight:400">(facultatif)</span><select id="cp-source">
<option value="">Choisissez</option>
<option>Recherche Google</option>
<option>TikTok</option>
<option>Instagram</option>
<option>Pinterest</option>
<option>Forum (ForumConstruire ou autre)</option>
<option>ComeUp</option>
<option>Bouche-à-oreille</option>
<option>Assistant IA (ChatGPT, Gemini…)</option>
<option>Autre</option>
</select></label>
<label>Votre message<textarea name="entry.881289893" required minlength="10" maxlength="4000" rows="7"></textarea></label>
<button type="submit" data-goatcounter-click="envoi-formulaire-contact">Envoyer le message</button>
<p class="cp-form-rgpd">Vos nom, e-mail et message servent uniquement à vous répondre. Ils sont enregistrés via Google Forms (Google) et conservés au plus 12 mois. Vous pouvez demander leur suppression à tout moment : voir les <a href="mentions-legales.html">mentions légales</a>.</p>
</form>
<p>Vous préférez en parler de vive voix ? <a href="https://calendar.app.google/6LCc6yKVHnbvA3WN7" target="_blank" rel="noopener" data-goatcounter-click="clic-rdv-contact">Réservez un appel gratuit de 15 min</a>.</p>"""
page("contact", "Contact | Contre-Plan", "Me contacter",
 "Une question sur l'analyse de devis de travaux ? Écrivez à Contre-Plan via le formulaire de contact, réponse sous 24 h.",
 "Une question avant de commander, ou après avoir lu un guide ? Je vous réponds personnellement.", contact_body, "Contact", toc=False)

merci = head("Message envoyé | Contre-Plan", "Votre message a bien été envoyé.", "https://contre-plan.com/merci.html").replace('<meta property="og:type" content="article">','<meta name="robots" content="noindex">') + pagehero("Contact", "Message envoyé", "Merci, votre message est bien parti. Je vous réponds sous 24 h à l'adresse indiquée.", None, [("Accueil", "index.html"), ("Contact", "contact.html"), ("Message envoyé", None)]) + layout(f"""<p>En attendant, vous pouvez déjà vérifier votre devis avec les <a href="guides.html">guides et outils gratuits</a>, ou le <a href="lexique-devis-travaux.html">lexique du devis</a>.</p>""", False) + footer()
open(os.path.join(OUT, "merci.html"), "w").write(merci)

# ---------- 404 (absolute paths: served at any URL)
p404 = head("Page introuvable | Contre-Plan", "Cette page n'existe pas ou a été déplacée.", "https://contre-plan.com/404.html", root="/").replace('<meta property="og:type" content="article">','<meta name="robots" content="noindex">') + f'''<main id="contenu" class="bp" style="min-height:60vh">
<div style="max-width: 760px; margin: 0 auto; padding: 120px 24px; display:flex; flex-direction:column; gap:24px; align-items:flex-start;">
<span class="tag">Erreur 404</span>
<h1 style="margin:0;font-family:Archivo,Arial,sans-serif;font-weight:800;line-height:1.05;color:#fff">Ce poste ne figure pas <span style="color:var(--or)">sur le plan.</span></h1>
<p style="margin:0;font-size:20px;line-height:1.5;color:#d3ddf0;">La page que vous cherchez n'existe pas ou a été déplacée.</p>
<div style="display:flex;flex-wrap:wrap;gap:14px;"><a class="btn" href="/">Retour à l'accueil</a><a class="btn line" href="/guides.html">Lire les guides</a></div>
</div>
<div class="ruler" aria-hidden="true"></div>
</main>
''' + footer(root="/")
open(os.path.join(OUT, "404.html"), "w").write(p404)

# ---------- pages légales (CGV, confidentialité) : noindex, hors sitemap
import pages_legales as PL
for _slug, _title, _h1, _desc, _lead, _body in [
    ("cgv", "Conditions générales de vente | Contre-Plan", "Conditions générales de vente", "Conditions générales de vente des analyses de devis de travaux Contre-Plan : prestation, prix, délais, rétractation, responsabilité, médiation.", "Ce que comprend l'analyse de votre devis, ce qu'elle ne comprend pas, et vos droits.", PL.CGV_BODY),
    ("confidentialite", "Politique de confidentialité | Contre-Plan", "Politique de confidentialité", "Quelles données Contre-Plan collecte, pourquoi, combien de temps elles sont conservées et comment exercer vos droits.", "Vos devis et vos coordonnées servent uniquement à vous répondre et à réaliser l'analyse.", PL.CONF_BODY)]:
    _url = f"https://contre-plan.com/{_slug}.html"
    _out = head(_title, _desc, _url).replace('<meta property="og:type" content="article">','<meta name="robots" content="noindex">') + pagehero("Informations légales", _h1, _lead, None, [("Accueil", "index.html"), (_h1, None)]) + layout(_body, False) + footer()
    open(os.path.join(OUT, _slug + ".html"), "w").write(_out)

# ---------- sitemap
urls = [("", "1.0"), ("guides.html","0.8")] + [(s+".html","0.7") for s,_,_,_ in ARTICLES] + [(s+".html","0.7") for s in PAGES] + [("checklist-devis-travaux.pdf","0.6"),("exemple-rapport-contre-plan.pdf","0.6"),("tableau-comparatif-devis.pdf","0.5")]
sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(f'  <url><loc>https://contre-plan.com/{u}</loc><lastmod>{LASTMOD.get(u, max([DATE] + list(LASTMOD.values())))}</lastmod><priority>{p}</priority></url>\n' for u,p in urls) + '</urlset>\n'
open(os.path.join(OUT, "sitemap.xml"), "w").write(sm)
import subprocess, sys as _s
subprocess.run([_s.executable, os.path.join(os.path.dirname(os.path.abspath(__file__)), "typo.py"), OUT], check=True)
print("ok", [a[0] for a in ARTICLES])

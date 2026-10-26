# Nouveaux guides et pages par type de travaux (octobre 2026).
# Importé par build.py : chaque entrée est passée à article() ou page().

SRC = '<p style="font-size: 15px !important; color: #5b6784 !important;">'

# ---------------------------------------------------------------- Guides
GUIDES = []
GUIDE_FAQS = {}

# ---------- Décennale
GUIDES.append(dict(
 slug="guide-verifier-assurance-decennale",
 title="Assurance décennale : comment vérifier l'attestation d'un artisan",
 h1="Assurance décennale : comment vérifier l'attestation de votre artisan",
 desc="Activités couvertes, période de validité, assureur, couverture géographique : les 5 points à contrôler sur l'attestation décennale avant de signer un devis.",
 lead="Une attestation décennale jointe au devis ne prouve pas grand-chose si elle couvre une autre activité, une autre période ou une autre entreprise. Voici comment la lire en deux minutes.",
 readtime=6,
 body='''<h2>À quoi sert la garantie décennale</h2>
<p>Pendant <strong>10 ans après la réception</strong> des travaux, l'entreprise est responsable des dommages qui compromettent la solidité de l'ouvrage ou le rendent impropre à son usage : infiltrations par la toiture, fissures structurelles, étanchéité de douche défaillante qui ruine un plancher. Son assurance décennale paie les réparations, même si l'entreprise a disparu entre-temps.</p>
<p>Elle s'ajoute à deux autres garanties qui démarrent aussi à la réception : la <strong>garantie de parfait achèvement</strong> (1 an, tous les défauts signalés) et la <strong>garantie de bon fonctionnement</strong> (2 ans minimum, pour les équipements dissociables comme un radiateur ou une porte intérieure).</p>
<h2>L'attestation doit être jointe au devis</h2>
<p>Depuis le 1er juillet 2016, une entreprise soumise à l'assurance décennale doit <strong>joindre son attestation</strong> à ses devis et factures, selon un modèle fixé par arrêté. Le devis lui-même doit mentionner l'assurance souscrite, les coordonnées de l'assureur et la couverture géographique.</p>
<div class="note"><p><strong>Pas d'attestation, pas de signature.</strong> Une entreprise qui ne la fournit pas, ou qui promet de l'envoyer « après », ne respecte pas une obligation légale. C'est un signal d'alerte, quel que soit le prix.</p></div>
<h2>Les 5 points à vérifier</h2>
<ol><li><strong>Le nom de l'assuré</strong> : c'est exactement l'entreprise qui signe le devis (même raison sociale, même numéro SIREN). Une attestation au nom d'un confrère ou d'une ancienne société ne vous couvre pas.</li>
<li><strong>Les activités couvertes</strong> : l'attestation liste des activités précises. Une attestation « plomberie » ne couvre pas la pose de carrelage ou la reprise d'une charpente. Chaque poste important du devis doit correspondre à une activité listée.</li>
<li><strong>La période de validité</strong> : c'est l'assurance en vigueur <strong>à l'ouverture du chantier</strong> qui compte. Si l'attestation expire avant le démarrage prévu, demandez la nouvelle.</li>
<li><strong>La couverture géographique</strong> : la plupart des contrats couvrent la France métropolitaine. Vérifiez-le si vos travaux sont ailleurs.</li>
<li><strong>L'assureur</strong> : son nom et ses coordonnées doivent figurer. Méfiez-vous des assureurs étrangers inconnus : plusieurs ont fait faillite ces dernières années, laissant les clients sans couverture. En cas de doute, appelez l'assureur avec le numéro de contrat.</li></ol>
<h2>Les travaux qui ne sont pas concernés</h2>
<p>Tous les travaux ne relèvent pas de la décennale. La peinture purement décorative ou le simple entretien, par exemple, n'en dépendent pas forcément. En revanche, dès que les travaux touchent au clos et couvert, à la structure, à l'étanchéité ou à des équipements indissociables du bâti (plomberie encastrée, chape, carrelage collé), l'attestation est attendue.</p>
<h2>Et l'assurance dommages-ouvrage ?</h2>
<p>C'est l'assurance du <strong>maître d'ouvrage</strong>, donc la vôtre. Elle préfinance les réparations relevant de la décennale sans attendre de savoir qui est responsable. Elle est obligatoire avant des travaux de construction, y compris pour un particulier, mais le particulier qui fait construire pour lui-même n'encourt pas de sanction pénale s'il ne la souscrit pas. En pratique, elle concerne surtout les extensions et les rénovations lourdes, et son coût est élevé : posez la question pour ces chantiers-là.</p>
<h2>Ce que je vérifie sur votre devis</h2>
<p>La présence de l'attestation, la concordance entre l'entreprise, les activités couvertes et les postes du devis, et les dates de validité. Voir aussi <a href="guide-mentions-obligatoires-devis.html">les mentions obligatoires d'un devis</a> et <a href="modeles-messages-artisan.html">le message type pour demander l'attestation</a>.</p>
''' + SRC + '''Article d'information générale, à jour au 26 octobre 2026. Sources : articles 1792 à 1792-6 du Code civil, articles L241-1, L242-1 et L243-2 du Code des assurances, article 22-2 de la loi n° 96-603 du 5 juillet 1996, arrêté du 5 janvier 2016 (modèle d'attestation), INC (inc-conso.fr).</p>''',
))
GUIDE_FAQS["guide-verifier-assurance-decennale"] = [
 ("L'attestation décennale est-elle obligatoire sur un devis ?",
  "Oui, pour les travaux soumis à l'assurance décennale : depuis le 1er juillet 2016, l'attestation doit être jointe aux devis et aux factures, et le devis doit mentionner l'assureur et la couverture géographique."),
 ("Quelle date de validité compte sur l'attestation ?",
  "Celle de l'ouverture du chantier. L'assurance en vigueur au démarrage des travaux couvre l'ouvrage pendant 10 ans après la réception, même si l'entreprise change d'assureur ou cesse son activité ensuite."),
 ("Que faire si l'artisan refuse de fournir son attestation ?",
  "Ne signez pas. La fournir est une obligation, pas une faveur. Un refus ou un « je vous l'envoie plus tard » doit vous faire choisir une autre entreprise."),
]

# ---------- Négocier
GUIDES.append(dict(
 slug="guide-negocier-devis-travaux",
 title="Devis de travaux trop cher : comment négocier sans se faire avoir",
 h1="Devis de travaux trop cher : comment le négocier intelligemment",
 desc="Faire détailler les forfaits, comparer poste par poste, vérifier TVA et aides, revoir l'échéancier : les leviers pour faire baisser un devis sans sacrifier la qualité.",
 lead="Demander « un geste » sur le total marche rarement, et quand ça marche, la différence se retrouve souvent ailleurs. On négocie mieux un devis quand on sait ligne par ligne ce qu'on paie.",
 readtime=6,
 body='''<h2>D'abord, savoir ce que vous payez</h2>
<p>On ne négocie pas un forfait. Pour les travaux de dépannage, de réparation et d'entretien, la réglementation impose un devis détaillé : prestations, quantités, prix unitaires, taux de TVA. Pour les autres travaux, rien ne vous empêche d'exiger le même niveau de détail avant de signer. Une ligne « Rénovation salle de bain : 9 800 € » doit devenir une dizaine de postes chiffrés.</p>
<div class="note"><p><strong>Le bon réflexe :</strong> demandez le détail <em>avant</em> de parler prix. C'est en voyant les quantités que l'on repère une surface surestimée ou un poste compté deux fois.</p></div>
<h2>Comparer poste par poste, pas les totaux</h2>
<p>Deux devis à 12 000 € et 14 000 € ne décrivent souvent pas les mêmes travaux. Mettez-les côte à côte avec <a href="comparer-ses-devis.html">le tableau comparatif gratuit</a> : vous verrez qu'un des deux oublie la dépose, l'autre compte une étanchéité complète. Le moins cher n'est pas forcément le plus avantageux une fois les oublis réintégrés.</p>
<p>Un écart de prix sur un même poste, à prestation égale, est en revanche un vrai argument : « L'autre entreprise chiffre la même faïence, même surface, 20 % moins cher. Pouvez-vous vous aligner sur ce poste ? »</p>
<h2>Vérifier la TVA et les aides avant de négocier</h2>
<p>Un taux de TVA mal appliqué peut peser plus lourd qu'une remise. Dans un logement achevé depuis plus de 2 ans, la plupart des travaux relèvent du taux de 10 %, et la rénovation énergétique de 5,5 %, sous réserve d'une mention que vous certifiez sur le devis. Détails dans <a href="guide-tva-travaux-renovation.html">le guide TVA</a>.</p>
<p>Pour les travaux d'économie d'énergie, vérifiez aussi les aides (MaPrimeRénov', primes CEE) et la qualification RGE de l'entreprise, qui conditionne ces aides. Leurs règles ont beaucoup changé en 2026 : faites le point avec un conseiller France Rénov', gratuit, avant de signer.</p>
<h2>Les leviers qui fonctionnent</h2>
<ul><li><strong>Ajuster le périmètre</strong> : faire vous-même la dépose ou la peinture finale, conserver un équipement en bon état, choisir une gamme de faïence plus courante.</li>
<li><strong>Grouper les travaux</strong> : un chantier plus gros, ou deux lots confiés à la même entreprise, réduit ses frais fixes (déplacements, installation).</li>
<li><strong>Être souple sur la date</strong> : une entreprise qui a un trou dans son planning acceptera plus facilement un effort.</li>
<li><strong>Négocier les conditions plutôt que le prix</strong> : un acompte plus faible (l'usage est de 20 à 30 %), un échéancier calé sur l'avancement, une retenue de garantie de 5 % jusqu'à la levée des réserves. Voir <a href="guide-acompte-paiement-devis-travaux.html">le guide sur l'acompte</a>.</li></ul>
<h2>Ce qu'il ne faut pas négocier</h2>
<p>L'étanchéité, la ventilation, la protection électrique, l'épaisseur d'isolant : ce sont les postes qui coûtent cher à reprendre et que l'entreprise sera tentée de rogner si vous serrez trop le prix global. Une remise obtenue en supprimant un poste indispensable n'est pas une économie.</p>
<h2>Et si l'entreprise refuse ?</h2>
<p>Un refus argumenté n'est pas mauvais signe : il montre souvent que le prix a été calculé, pas gonflé pour laisser de la marge à la négociation. Si l'écart reste important avec d'autres devis à prestation égale, demandez simplement ce qui le justifie, avec <a href="modeles-messages-artisan.html">les modèles de messages</a>.</p>
<h2>Ce que je vérifie sur votre devis</h2>
<p>Les quantités, les prix unitaires comparés à des ordres de grandeur récents, la TVA, les oublis et les postes à faire préciser. Le rapport se termine par les questions à poser à l'artisan, que vous pouvez utiliser telles quelles pour négocier.</p>
''' + SRC + '''Article d'information générale, à jour au 26 octobre 2026. Sources : arrêté du 24 janvier 2017 relatif à la publicité des prix des prestations de dépannage, de réparation et d'entretien dans le secteur du bâtiment, article L111-1 du Code de la consommation, articles 278-0 bis A et 279-0 bis du Code général des impôts, ecologie.gouv.fr (MaPrimeRénov' 2026).</p>''',
))
GUIDE_FAQS["guide-negocier-devis-travaux"] = [
 ("Peut-on négocier un devis de travaux ?",
  "Oui, tant qu'il n'est pas signé. Le plus efficace est de faire détailler les forfaits, de comparer poste par poste avec d'autres devis et d'ajuster le périmètre, plutôt que de demander une remise sur le total."),
 ("Un artisan peut-il faire payer son devis ?",
  "Oui, à condition de vous en informer avant de l'établir. Son montant est souvent déduit si vous signez. Pour un dépannage, le devis doit indiquer s'il est gratuit ou payant, et son prix."),
 ("Quel acompte verser à la signature ?",
  "Aucun plafond légal ne s'applique aux travaux chez un particulier. L'usage est de 20 à 30 %. Au-delà, demandez pourquoi et proposez un échéancier lié à l'avancement du chantier."),
]

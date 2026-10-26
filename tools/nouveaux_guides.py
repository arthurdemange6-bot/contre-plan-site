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

# ---------- Dépassement du devis
GUIDES.append(dict(
 slug="guide-depassement-devis-travaux-supplementaires",
 title="Facture plus chère que le devis : que dit la loi sur les suppléments ?",
 h1="L'artisan dépasse le devis : que faire face aux travaux supplémentaires",
 desc="Devis signé, marché à forfait, imprévu de chantier, avenant écrit : quand un supplément est dû, quand il ne l'est pas, et les recours si la facture dépasse le devis.",
 lead="Le devis disait 8 000 €, la facture en annonce 9 400 €. Avant de payer ou de refuser, il faut savoir une chose : qu'avez-vous accepté, et par écrit ?",
 readtime=7,
 body='''<h2>Un devis signé engage l'artisan</h2>
<p>Une fois signé, le devis est un <strong>contrat</strong>. L'entreprise ne peut pas modifier seule ni le prix ni le contenu des travaux. Si elle facture plus, c'est à elle de prouver que vous avez accepté ce supplément. Pour un particulier, au-delà de 1 500 €, cette preuve doit en principe être écrite.</p>
<h2>Le marché à forfait : la protection la plus forte</h2>
<p>Quand le devis fixe un <strong>prix global et forfaitaire</strong> pour des travaux décrits précisément, la loi est très claire : l'entrepreneur ne peut demander aucune augmentation, ni pour la hausse de la main-d'œuvre ou des matériaux, ni pour des changements ou ajouts, <strong>sauf si ces changements ont été autorisés par écrit et leur prix convenu avec vous</strong> (article 1793 du Code civil).</p>
<div class="note"><p><strong>En pratique :</strong> un supplément annoncé à l'oral sur le chantier, puis découvert sur la facture, n'est pas dû dans un marché à forfait. Votre silence ne vaut pas accord.</p></div>
<h2>Devis au métré ou « selon état » : plus de marge pour l'artisan</h2>
<p>Si le devis fixe des <strong>prix unitaires</strong> (au m², au mètre linéaire, à la pièce) plutôt qu'un prix global, la facture suit les quantités réellement exécutées. Elle peut donc dépasser le devis si les quantités augmentent, à condition qu'elles soient justifiées. Les lignes « selon état » ou « hors imprévus » ne sont pas un chèque en blanc, mais elles affaiblissent votre position : c'est pour cela qu'il faut les faire chiffrer avant de signer.</p>
<h2>L'imprévu de chantier</h2>
<p>Une poutre pourrie derrière un doublage, une canalisation en plomb sous un carrelage : les vraies surprises existent. Mais aucun texte ne permet à l'artisan de les facturer de son propre chef. La bonne pratique, et votre protection, c'est :</p>
<ol><li>l'entreprise vous prévient <strong>avant</strong> d'engager les travaux supplémentaires, photos à l'appui ;</li>
<li>elle vous remet un <strong>avenant ou un devis complémentaire chiffré</strong> ;</li>
<li>vous le signez, ou vous le refusez et discutez d'une autre solution.</li></ol>
<p>Une erreur de métré ou de chiffrage de l'entreprise n'est pas un imprévu : c'est à elle de l'assumer.</p>
<h2>Révision de prix : seulement si le devis la prévoit</h2>
<p>Le prix d'un devis ne s'indexe pas automatiquement sur la hausse des matériaux. Une révision n'est possible que si le contrat la prévoit expressément, avec une formule et un indice de référence en lien avec les travaux (les index BT du bâtiment, par exemple). Une telle clause joue aussi à la baisse.</p>
<h2>La facture dépasse le devis : les étapes</h2>
<ol><li><strong>Demandez par écrit le détail</strong> du supplément et le document par lequel vous l'auriez accepté.</li>
<li><strong>Payez ce qui est dû selon le devis</strong> et contestez le reste par écrit, en expliquant pourquoi. Ne bloquez pas l'intégralité sans raison : ce serait vous mettre en tort.</li>
<li><strong>Envoyez une mise en demeure</strong> par lettre recommandée avec accusé de réception si le désaccord persiste.</li>
<li><strong>Saisissez le médiateur de la consommation</strong> de l'entreprise : tout professionnel doit en désigner un et indiquer ses coordonnées sur ses devis. Il faut d'abord avoir fait une réclamation écrite, et le saisir dans l'année qui suit.</li>
<li><strong>Le conciliateur de justice</strong>, gratuit, est une autre voie. Pour un litige de 5 000 € ou moins, une tentative de règlement amiable est en principe obligatoire avant de saisir le tribunal.</li></ol>
<p>Vous pouvez aussi faire un signalement sur SignalConso : il ne règle pas votre litige, mais il aide la DGCCRF à cibler ses contrôles.</p>
<h2>Ce que je vérifie sur votre devis</h2>
<p>Le type de prix (forfait ou unitaire), les lignes « selon état », « hors imprévus » ou « à définir », et les postes oubliés qui deviendront des suppléments. Chaque rapport les liste avec la question à poser pour les faire chiffrer avant de signer. Voir aussi <a href="modeles-messages-artisan.html">les modèles de messages à l'artisan</a>.</p>
''' + SRC + '''Article d'information générale, à jour au 26 octobre 2026, qui ne remplace pas un conseil juridique sur votre situation. Sources : articles 1103, 1359 et 1793 du Code civil, articles L612-1 et L612-2 du Code de la consommation (médiation), article 750-1 du Code de procédure civile, economie.gouv.fr, inc-conso.fr.</p>''',
))
GUIDE_FAQS["guide-depassement-devis-travaux-supplementaires"] = [
 ("Un artisan peut-il facturer plus cher que le devis signé ?",
  "Pas de lui-même. Dans un marché à forfait, un supplément n'est dû que si vous l'avez autorisé par écrit et que son prix a été convenu avec vous. Avec des prix unitaires, la facture peut suivre les quantités réellement exécutées, à condition qu'elles soient justifiées."),
 ("Un accord oral suffit-il pour des travaux supplémentaires ?",
  "Dans un marché à forfait, non : la loi exige une autorisation écrite. Dans les autres cas, c'est à l'artisan de prouver votre accord, en principe par écrit au-delà de 1 500 €. Exigez toujours un avenant chiffré avant les travaux."),
 ("Que faire si la facture dépasse le devis ?",
  "Payez ce qui correspond au devis, contestez le supplément par écrit, puis envoyez une mise en demeure si le désaccord persiste. Ensuite, saisissez le médiateur de la consommation de l'entreprise ou un conciliateur de justice."),
]

# ---------- Annuler un devis signé
GUIDES.append(dict(
 slug="guide-annuler-devis-signe-retractation",
 title="Annuler un devis signé : délai de rétractation et cas sans retour",
 h1="Devis signé : peut-on encore annuler ou se rétracter ?",
 desc="Signature à domicile, en magasin, sur un salon ou en ligne, crédit travaux, arrhes ou acompte : quand vous pouvez annuler un devis signé, et ce que ça coûte.",
 lead="Vous avez signé, et vous le regrettez. Tout dépend d'un détail que l'on oublie souvent : l'endroit où vous avez signé.",
 readtime=7,
 body='''<h2>Signé chez vous : 14 jours pour changer d'avis</h2>
<p>Un devis signé à votre domicile (ou ailleurs que dans les locaux de l'entreprise, à la suite d'une visite) est un contrat <strong>hors établissement</strong>. Vous disposez de <strong>14 jours</strong> pour vous rétracter, sans motif et sans frais. Pour des travaux, le délai court à partir du lendemain de la signature.</p>
<ul><li>L'entreprise doit vous remettre un <strong>formulaire de rétractation</strong>. Vous pouvez l'utiliser, ou envoyer un courrier recommandé avec accusé de réception.</li>
<li>Pendant les <strong>7 premiers jours</strong>, elle ne peut encaisser <strong>aucun paiement</strong> : ni acompte, ni chèque, même daté plus tard, ni autorisation de prélèvement.</li>
<li>Si vous vous rétractez, elle doit vous rembourser sous 14 jours.</li></ul>
<div class="note"><p><strong>Le formulaire manque ?</strong> Si l'entreprise ne vous a pas informé de votre droit de rétractation, le délai est prolongé de 12 mois. Et selon la Cour de justice de l'Union européenne (2023), si vous vous rétractez dans ce cas, vous ne devez rien pour les travaux déjà réalisés.</p></div>
<h2>Les travaux ont commencé pendant le délai</h2>
<p>Si vous avez demandé expressément que les travaux démarrent avant la fin des 14 jours, vous pouvez toujours vous rétracter, mais vous payez la part déjà réalisée. Plus de rétractation possible, en revanche, pour une prestation entièrement exécutée avec votre accord, pour des travaux d'entretien ou de réparation <strong>urgents</strong> que vous avez demandés, ou pour un bien fabriqué sur mesure.</p>
<h2>Signé en magasin, en agence ou chez l'artisan : pas de rétractation</h2>
<p>Si vous vous êtes déplacé pour signer, la loi ne prévoit <strong>aucun délai de rétractation</strong>. Le devis vous engage dès la signature, sauf si l'entreprise vous a accordé contractuellement un délai : vérifiez les conditions générales.</p>
<h2>Signé sur une foire ou un salon : pas de rétractation non plus</h2>
<p>C'est le piège classique des salons de l'habitat. Aucun délai de rétractation, et le vendeur doit l'afficher clairement sur son stand et l'écrire en tête du contrat. Seule exception : si les travaux sont financés par un <strong>crédit affecté</strong> souscrit sur place.</p>
<h2>Signé à distance (internet, téléphone) : 14 jours</h2>
<p>Un devis accepté en ligne ou par téléphone, sans rencontre physique, ouvre droit au même délai de 14 jours.</p>
<h2>Les travaux sont financés par un crédit</h2>
<p>Vous pouvez renoncer au crédit affecté dans les <strong>14 jours</strong> suivant l'acceptation de l'offre. Cette rétractation <strong>annule automatiquement le contrat de travaux</strong>, sans indemnité. Attention, si vous avez demandé une exécution immédiate des travaux, ce délai peut être réduit à 3 jours.</p>
<h2>Hors de ces cas : annuler a un coût</h2>
<p>Tout dépend de ce que vous avez versé, et du mot employé sur le devis :</p>
<ul><li><strong>Des arrhes</strong> : vous pouvez renoncer en les perdant (l'entreprise, elle, rembourserait le double). Si le devis ne précise rien, les sommes versées d'avance sont considérées comme des arrhes.</li>
<li><strong>Un acompte</strong> : le contrat est ferme. Annuler vous expose à indemniser l'entreprise.</li></ul>
<p>Pour un <strong>marché à forfait</strong>, la loi vous permet de résilier à tout moment, même travaux commencés, mais vous devez alors dédommager l'entreprise : ses dépenses, les travaux déjà faits et le bénéfice qu'elle aurait tiré du chantier (article 1794 du Code civil). Si l'entreprise a commis une faute, la situation est différente : faites-vous conseiller.</p>
<h2>Démarchage pour la rénovation énergétique</h2>
<p>Le démarchage téléphonique pour des travaux de rénovation énergétique est interdit, et depuis juillet 2025 l'interdiction s'étend aux SMS, courriels et réseaux sociaux : un contrat conclu dans ces conditions est nul. Depuis le 11 août 2026, tout démarchage téléphonique suppose en outre votre accord préalable.</p>
<h2>Le meilleur moment pour annuler, c'est avant de signer</h2>
<p>Un devis relu à tête reposée, c'est un regret en moins. Je vérifie la présence du formulaire de rétractation quand il est obligatoire, la nature des sommes demandées (arrhes ou acompte), l'échéancier et les conditions de résiliation. Voir aussi <a href="guide-acompte-paiement-devis-travaux.html">le guide sur l'acompte</a>.</p>
''' + SRC + '''Article d'information générale, à jour au 26 octobre 2026, qui ne remplace pas un conseil juridique sur votre situation. Sources : articles L221-10, L221-18, L221-20, L221-25, L221-28, L224-59, L312-19 et L214-1 du Code de la consommation, articles 1590 et 1794 du Code civil, loi n° 2025-594 du 30 juin 2025, CJUE 17 mai 2023 (C-97/22), service-public.gouv.fr (fiche F23224), anil.org.</p>''',
))
GUIDE_FAQS["guide-annuler-devis-signe-retractation"] = [
 ("Peut-on se rétracter après avoir signé un devis ?",
  "Oui si le devis a été signé à domicile ou à distance : vous avez 14 jours. Non s'il a été signé en magasin, chez l'artisan ou sur une foire ou un salon, sauf clause contraire ou crédit affecté."),
 ("L'artisan peut-il encaisser un acompte juste après la signature à domicile ?",
  "Non. Pendant les 7 jours qui suivent la signature hors établissement, il ne peut recevoir aucun paiement, sous aucune forme, sauf pour des travaux urgents de réparation demandés par le client."),
 ("Que se passe-t-il si j'annule un devis signé en magasin ?",
  "Vous n'avez pas de droit de rétractation. Si vous avez versé des arrhes, vous les perdez. Avec un acompte, le contrat est ferme et l'entreprise peut demander une indemnisation."),
]

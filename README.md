# contre-plan-site

Site vitrine Contre-Plan (GitHub Pages) : index.html, guides (guides.html, guide-*.html), 404.html, mentions-legales.html.
Mesure d'audience : GoatCounter (code contreplan).

## Ajouter ou modifier un guide

Les guides, la page Guides, la page 404 et le sitemap sont générés par `tools/build.py`.

1. Ajouter un appel `article(...)` dans `tools/build.py` (même format que les guides existants), avec `date="AAAA-MM-JJ"` = date de publication.
2. Lancer `python3 tools/build.py` depuis n'importe où : il réécrit les fichiers à la racine du site.
3. Ne jamais modifier à la main les fichiers générés (guide-*.html, guides.html, 404.html, sitemap.xml) : ils seraient écrasés au prochain build.

`index.html` et `mentions-legales.html` ne sont pas générés : on les modifie directement.

## Si les prix changent

Mettre à jour partout en même temps : `index.html` (cartes Tarifs, FAQ et ses données structurées, offres du JSON-LD, `data-prix` du calcul « Votre devis fait combien ? »), `site.js` (texte de la barre mobile « dès 16,50 € »), `tools/build.py` (encadré latéral SIDE et bloc CTA), `chat.js`, l'annonce ComeUp et l'agent carrousel.

## Offre de lancement
Le texte « −50 % pour les 20 premières commandes » figure dans index.html (badge des tarifs, FAQ et JSON-LD FAQ) et chat.js (réponse sur le prix). Le retirer à ces endroits quand l'offre se termine, et passer le prix à 33 €.

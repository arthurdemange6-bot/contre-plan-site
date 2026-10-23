# contre-plan-site

Site vitrine Contre-Plan (GitHub Pages) : index.html, guides (guides.html, guide-*.html), 404.html, mentions-legales.html.
Mesure d'audience : GoatCounter (code contreplan).

## Ajouter ou modifier un guide

Les guides, la page Guides, la page 404 et le sitemap sont générés par `tools/build.py`.

1. Ajouter un appel `article(...)` dans `tools/build.py` (même format que les guides existants), avec `date="AAAA-MM-JJ"` = date de publication.
2. Lancer `python3 tools/build.py` depuis n'importe où : il réécrit les fichiers à la racine du site.
3. Ne jamais modifier à la main les fichiers générés (guide-*.html, guides.html, 404.html, sitemap.xml) : ils seraient écrasés au prochain build.

`index.html` et `mentions-legales.html` ne sont pas générés : on les modifie directement.

# Décodeur de ligne de devis – relais Cloudflare

Le navigateur du visiteur appelle ce Worker, qui appelle l'API Claude avec la clé d'Arthur. La clé n'apparaît jamais sur le site ni dans ce dépôt. Rien n'est enregistré (ni la ligne, ni la réponse, ni l'IP).

## Mise en service (une fois)

1. **Console Claude** (platform.claude.com) :
   - créer un espace de travail « Décodeur » avec une **limite de dépense mensuelle** (par exemple 30 $) ;
   - dans cet espace, créer une **clé API** nommée « decodeur-site ». La copier une seule fois, directement dans Cloudflare (étape 2), sans l'envoyer à personne.
2. **Cloudflare** (compte gratuit) : Workers & Pages > Create > Worker, nom `contre-plan-decodeur` > Deploy, puis Edit code : remplacer tout le code par `worker.js`, Deploy.
   - Settings > Variables and Secrets > Add : type **Secret**, nom `ANTHROPIC_API_KEY`, valeur = la clé API.
   - Facultatif : variable texte `MODEL` (par défaut `claude-sonnet-5-5`).
   - Conseillé : protection anti-robot **Turnstile**. Créer un widget « Décodeur » (mode Managed, hostname contre-plan.com) dans Application security > Turnstile, mettre sa clé de site dans `TURNSTILE_SITEKEY` de `tools/decodeur.py` et sa clé secrète en secret `TURNSTILE_SECRET` du Worker. Le binding Rate limiting de `wrangler.toml` ne se configure qu'en ligne de commande (`npx wrangler deploy`).
3. Copier l'adresse du Worker (`https://contre-plan-decodeur.<compte>.workers.dev`) dans `DECODEUR_URL` de `tools/decodeur.py`, puis `python3 tools/build.py` : la page `decodeur-ligne-devis.html`, ses liens (page Guides, encadré latéral), le sitemap et la politique de confidentialité sont générés.

## Sécurité

- N'accepte que les requêtes venant de contre-plan.com (en-tête Origin).
- Une ligne de 400 caractères au maximum ; 5 demandes par minute et par visiteur si le binding `RL` existe.
- Les dépenses sont bornées par la limite de l'espace de travail dans la Console et par les crédits mensuels (aucune carte enregistrée).
- Pour couper l'outil : supprimer le secret `ANTHROPIC_API_KEY` (le site affiche « indisponible ») ou vider `DECODEUR_URL` et relancer le build.

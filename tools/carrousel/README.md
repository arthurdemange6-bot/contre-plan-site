# Carrousels « La ligne du devis »

Scripts utilisés chaque nuit par l'agent carrousel (ne pas renommer) :

- `gen_carousel.py spec.json .` : génère slide1..N.png (TikTok 1080x1920), ig1..N.png (carrousel Instagram 1080x1350), cover.png, story.png et slideN.html (rendu photoréaliste).
- `make_reel.py spec.json .` : filme les slides animées en reel.mp4 (1080x1920, bruitages discrets) et, si les slides ont un champ `vo`, écrit reel.srt (sous-titres calés sur la vidéo, pour CapCut).

Toute modification poussée sur `main` est utilisée dès l'épisode suivant.

Fond musical : `make_reel.py` génère lui-même une musique originale (lo-fi calme, 96 bpm, La mineur), donc libre de droits, mixée sous les bruitages à un volume global d'environ -19 dB. Pour une vidéo sans musique, ajouter `"music": false` dans spec.json.
